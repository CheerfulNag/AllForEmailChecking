
import requests
import concurrent.futures
import time
import gc
import sys
import random

sys.path.append("./")
from SharedModules.Proxy import Proxy
from Configs.IndeedConfig import MainUrl,PostUrl,HeadersMain,HeadersPost,Payload
from SharedModules.csv_handler import csv_handler
from SharedModules.logs_handler import logs_handler

def checker(record):
    global count
    email = str(record[1])

    phone = str(record[0])
    done = False
    error_count = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy)
            s.headers.update(HeadersMain)
            r = s.get(MainUrl,timeout=5)
            page_html = r.text

            id_payload = page_html.split("var tk = encodeURIComponent('")[1].split("'")[0]
            Payload["__email"] = email
            Payload["form_tk"] = id_payload

            s.cookies.clear()

            r = s.post(PostUrl,data=Payload, headers=HeadersPost,timeout=5)
            response = r.json()

            if response["isEmailInvalid"] == True:
                raise Exception("EmailInvalid")

            if (response["isEmailTaken"]==True):
               chunk_results.append((phone,email,"Registered"))

            s.close()

            done = True
            count +=1
            
        except Exception as exc:
            s.close()
            error_count +=1
            if error_count >5:
                done = True
                count+=1
                skipped_emails.append((phone,email))
                if "Expecting value" in str(exc):
                    exc = "JSONDecodeError"
                log.add_records_to_logs((email,exc))

    if count%100 == 0:
        print(f"{count} scrapped.")
        log.add_records_to_logs(f"{count} scrapped.")

def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/Indeed")
    csv_handler.create("Indeed")
    csv_handler.skipped_create()

    records_len = len(csv_handler.read(input_file_name=InputName))
    for number in range(start_from,records_len,ChunkSize):
        #Clearing lists and creating index where to start from
        all_records = []
        skipped_emails = []
        chunk_results = []
        chunk = []
        count = 0

        all_records = csv_handler.read(input_file_name=InputName)
        
        for x in range(number,number+ChunkSize):
            #Filling chunk with records to process
            try:
                chunk.append(all_records[x])
            except Exception as exc:
                print(exc)
                break
        all_records = [] 

        print(f"Scraping {number}-{number+ChunkSize}.")
        log.add_records_to_logs(f"Scraping {number}-{number+ChunkSize}.")
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=MaxWorkers) as executor:
            executor.map(checker,chunk)
        print(f"{count}/{ChunkSize} emails checked.")
        log.add_records_to_logs(f"{count}/{ChunkSize} emails checked.")
        end = time.time()

        log.add_records_to_logs(f"Total: {end-start}")

        gc.collect()

        csv_handler.save(records_to_save=chunk_results)
        csv_handler.skipped_save(records=skipped_emails)

        print(f"Chunk complete. {len(skipped_emails)} emails skipped.")
        log.add_records_to_logs(f"Chunk complete. {len(skipped_emails)} emails skipped.")


MaxWorkers = 100
ChunkSize = 3000
InputName = "FILE_NAME"

main(0)
