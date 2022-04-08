import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures
import gc

from py.config import Proxy,UrlFirst,UrlLast,HeadersFirst,HeadersFinal,Payload
from py.csv_handler import csv_handler
from py.logs_handler import logs_handler




def checker(record):
    global count
    email = record[1]
    phone = str(record[0]) 
    done = False
    error_count = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy)
            r = s.get(UrlFirst,headers=HeadersFirst,timeout=5)
            sIdString = r.text.split('type="hidden" name="sIdString" value="')[1].split('"')[0]
            PageInstance = r.text.split('<input type="hidden" name="pageInstance" value="')[1].split('"')[0] #check if something
            csrfToken = s.cookies["JSESSIONID"].replace('"','')
            loginCsrfParam = s.cookies['bcookie'].replace('"v=2&','').replace('"','')
            Payload["csrfToken"] = csrfToken
            Payload["session_key"] = email
            Payload["sIdString"] = sIdString
            Payload["pageInstance"] = PageInstance
            Payload["loginCsrfParam"] = loginCsrfParam
            r = s.post(UrlLast,headers=HeadersFinal,timeout=5,data=Payload)

            soup = BeautifulSoup(r.text,'html.parser')
            resp = (soup.select_one('form.login__form').text.replace("\n\n",""))
            if "s not the right password." in resp:
                chunk_results.append((phone,email,"Registered"))
            elif ("Couldn’t find a LinkedIn account associated with this email." in resp) or ("We don't recognize that email." in resp):
                pass
            else:
                raise Exception("Retrying")

            s.close()
            done = True
            count+=1
            if count%50 == 0:
                print(f"{count} emails checked.")
                log.add_records_to_logs(f"{count} emails checked.")
        except Exception as exc:
            s.close()
            error_count +=1
            if error_count > 10:
                count+=1
                if "'NoneType' object has no attribute 'text'" not in str(exc):
                    log.add_records_to_logs((email,exc))
                done = True
                skipped_emails.append((phone,email))
            

def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/LinkedIn")
    csv_handler.create("LinkedIn")
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


MaxWorkers = 50
ChunkSize = 1000
InputName = "november_filtered"

main(0)