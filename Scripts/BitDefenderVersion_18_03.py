import requests
import concurrent.futures
from math import ceil
import time
import gc


from py.csv_handler import csv_handler
from py.logs_handler import logs_handler
from py.config import headers_default,proxy,headers_post,payload_json

def checker(record):
    global count
    email = record[1]
    phone = record[0]
    error_count = 0
    done = False
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(proxy)
            s.headers.update(headers_default)
            time_stamp = ceil(time.time()*1000)
            r = s.get("https://account.bitdefender.com/v1/auth/init?=&redirect_uri=/&lang=en_US",allow_redirects=False,timeout=10)
            login_url = r.headers['location']
            headers_post["Referer"] = login_url
            s.headers.update(headers_post)
            payload_json["user"] = email
            payload_json["timestamp"] = time_stamp
            response = s.post("https://login.bitdefender.com/v1/user/lookup",json=payload_json,timeout=10).json()
            if "User not found" not in str(response):
                if "pow_challenge" in str(response):
                    log.add_records_to_logs(record)
                #log.add_records_to_logs(response)
                
                chunk_results.append((phone,email,"Registered"))
            count+=1
            s.close()
            if count%200==0:
                print(f"{count} emails checked.")
                log.add_records_to_logs(f"{count} emails checked.")
            done = True
            
        except Exception as exc:
            s.close()
            error_count +=1
            if error_count >5:
                log.add_records_to_logs(exc)
                skipped_emails.append(record)
                done = True


def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/BitDefender")
    csv_handler.create("BitDefender")
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
        end = time.time()

        log.add_records_to_logs(f"Total: {end-start}")

        gc.collect()

        csv_handler.save(records_to_save=chunk_results)
        csv_handler.skipped_save(records=skipped_emails)

        print(f"Chunk complete. {len(skipped_emails)} emails skipped.")
        log.add_records_to_logs(record_text=f"Chunk complete. {len(skipped_emails)} emails skipped.")

MaxWorkers = 200
ChunkSize = 2000
InputName = "november_filtered"

main(0)