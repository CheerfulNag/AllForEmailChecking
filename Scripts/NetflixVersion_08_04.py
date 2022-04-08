import traceback
import requests
import concurrent.futures
import time
import gc
from bs4 import BeautifulSoup
import sys 


sys.path.append("./")
from SharedModules.Proxy import Proxy
from Configs.NetflixConfig import MainUrl,HeadersMain,HeadersPost,Payload,PassGenerator,FormatPayload
from SharedModules.csv_handler import csv_handler
from SharedModules.logs_handler import logs_handler


def checker(record):
    global count
    email = record[1]
    phone = str(record[0])
    password = PassGenerator() 
    done = False
    error_count = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy) 
            s.headers.update(HeadersMain)

            resp = s.get(MainUrl,timeout=10)

            authURL = (resp.text).split('name="authURL" value="')[1].split('"')[0]
            SecureNetflixId = s.cookies["SecureNetflixId"]
            NetflixId = s.cookies["NetflixId"]
            nfvdid = s.cookies["nfvdid"]


            payload = FormatPayload(email,password,authURL,Payload)

            s.cookies.clear()
            s.cookies.set('SecureNetflixId', SecureNetflixId, domain=".netflix.com")
            s.cookies.set('NetflixId', NetflixId, domain=".netflix.com")
            s.cookies.set('nfvdid', nfvdid, domain=".netflix.com")

            s.headers.update(HeadersPost)
            r = s.post(MainUrl,data=payload,timeout=10)

            if "we can't find an account with this email address" in r.text:
                done = True
            elif "Incorrect password" in r.text:
                chunk_results.append((phone,email,"Registered"))
                done = True
            elif "Sorry, the password for this account needs to be reset" in r.text:
                chunk_results.append((phone,email,"Registered"))
                done = True
            elif "We are having technical difficulties and are actively working on a fix" in r.text:
                raise Exception("Tech Difficulties")
            else:
                message = BeautifulSoup(r.text,"html.parser").select("div.ui-message-contents")[1].text
                log.add_records_to_logs(f"Didn't recognize the message: {message}")
                skipped_emails.append(record)
                done = True
 
            s.close()
            count +=1
            if count%200 == 0:
                print(f"{count} emails checked.")
                log.add_records_to_logs(f"{count} emails checked.")
        except Exception as exc:
            s.close()
            error_count +=1
            if error_count > 5:
                count+=1
                skipped_emails.append((phone,email))
                done = True
                if "Tech Difficulties" not in str(exc):
                    log.add_records_to_logs(exc)


def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/Netflix")
    csv_handler.create("Netflix")
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
        log.add_records_to_logs(f"Chunk complete. {len(skipped_emails)} emails skipped.")


MaxWorkers = 50
ChunkSize = 2000
InputName = "november_filtered"

main(0)


