import traceback
import requests 
import concurrent.futures
import time
import gc
import json

from py.config import proxy, headers, payload ,url_get_answer
from py.csv_handler import csv_handler
from py.logs_handler import logs_handler


def checker(record):
    global count
    email = record[1]
    phone = record[0]
    done = False
    error_count = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(proxy)
            s.headers.update(headers)

            payloadd = payload
            payloadd["variables"]["input"]["email"] = email

            resp = s.post(url_get_answer,data=json.dumps(payloadd),timeout=10)
            print(resp)
            resp = str(resp.json())
            print(resp)
            if "AUTH_EMAIL_NOT_REGISTERED" not in resp:
                if "Transaction cancelled, please refer cancellation reasons for specific reasons" in resp:
                    resp = "Registered"
                chunk_results.append((phone,email,resp))
            count +=1
            if count%1 == 0:
                print(f"{count} emails scrapped.")
                log.add_records_to_logs(f"{count} emails scrapped.")

            s.close()
            done = True
        except:
            s.close()
            error_count +=1
            if error_count > 10:
                done = True
                log.add_records_to_logs(traceback.format_exc())
                skipped_emails.append(record)


def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/BurgerKing")
    csv_handler.create("BurgerKing")
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
        print("Program started.")
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
        end = time.time()

        log.add_records_to_logs(f"Total: {end-start}")

        gc.collect()

        csv_handler.save(records_to_save=chunk_results)
        csv_handler.skipped_save(records=skipped_emails)

        print(f"Chunk complete. {len(skipped_emails)} emails skipped.")
        log.add_records_to_logs(f"Chunk complete. {len(skipped_emails)} emails skipped.")


MaxWorkers = 1
ChunkSize = 5
InputName = "november_filtered"

main(200000)