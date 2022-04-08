
from turtle import title
import requests
import time
import gc
import concurrent.futures


from Configs.RealtorConfig import MainUrl,Proxy,HeadersOptionsLast,HeadersLast
from SharedModules.csv_handler import csv_handler
from SharedModules.logs_handler import logs_handler


def checker(record):
    global count
    email = str(record[1])
    phone = str(record[0])
    error_count = 0
    done = False
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy)
            s.headers.update(HeadersOptionsLast)
            r = s.options(MainUrl+email,timeout=5)
            s.headers.update(HeadersLast)
            r = s.get(MainUrl+email,timeout=5)
            response = r.json()
            if ("status" in str(response)):
                chunk_results.append((phone,email,response["status"].title()))

            done = True
            s.close()
            count +=1
            if count%100 == 0:
                print(f"{count} emails checked.")
                log.add_records_to_logs(f"{count} emails checked.")
        except Exception as exc:
            s.close()
            error_count+=1
            if error_count >15:
                done = True
                count +=1
                skipped_emails.append((phone,email))
                if "<center><h1>403 Forbidden</h1></center>" in str(exc):
                    exc = "403 Forbidden"
                log.add_records_to_logs(exc)


def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/Realtor")
    csv_handler.create("Realtor")
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
        with concurrent.futures.ThreadPoolExecutor(max_workers=MaxWorkers) as executor: #
            executor.map(checker,chunk)
        end = time.time()

        log.add_records_to_logs(f"Total: {end-start}")

        gc.collect()

        csv_handler.save(records_to_save=chunk_results)
        csv_handler.skipped_save(records=skipped_emails)

        print(f"Chunk complete. {len(skipped_emails)} emails skipped.")
        log.add_records_to_logs(f"Chunk complete. {len(skipped_emails)} emails skipped.")


MaxWorkers = 250
ChunkSize = 3000
InputName = "november_filtered"

main(0)
