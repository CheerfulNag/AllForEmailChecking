import requests
import time
import concurrent.futures
import gc
import traceback

from py.config import Proxy,Url,HeadersFirst,HeadersLast,Payload
from py.csv_handler import csv_handler
from py.logs_handler import logs_handler

from py.config import ResetHeadersOne,ResetHeadersTwo,ResetPayload,ResetUrl,ResetPayload

def checker_reset(record):
    #Reset is faster than login, sometimes "wrong token" error and sometimes "timeout" and "proxy error"
    global count
    email = record[1]
    phone = str(record[0]) 
    done = False
    error_count = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy)
            r = s.get(ResetUrl,headers=ResetHeadersOne,timeout=10)
            token = r.text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
            ResetPayload["Email"] = email
            ResetPayload["__RequestVerificationToken"] = token
            r = s.post(ResetUrl,headers=ResetHeadersTwo,data = ResetPayload,timeout=10)
            #print(r)
            response = r.text #Your request was successfully submitted.If this is a valid account, you will be receiving an email to reset or retrieve the information for your account.
            from bs4 import BeautifulSoup
            item = BeautifulSoup(r.text,'html.parser').select_one("div.card-body").text.replace("  ","").replace("\n\n","")
            if "Email address entered is not a registered email address" not in item:
                if "The anti-forgery cookie token and form field token do not match." in item:
                    raise Exception("Token error")
                #if "Your request was successfully submitted." in item:
                #    chunk_results.append((phone,email,"Registered"))
                log.add_records_to_logs(email)
                log.add_records_to_logs(item)
                #####log.add_records_to_logs("___")
                #####log.add_records_to_logs(email)
                #####log.add_records_to_logs(item)#log.add_records_to_logs(item)
            s.close()
            done = True
            count+=1
            if count%50 == 0:
                print(f"{count} emails checked.")
                log.add_records_to_logs(f"{count} emails checked.")
        except Exception as exc:
            s.close()
            error_count +=1
            if error_count > 5:
                log.add_records_to_logs(exc)
                done = True
                skipped_emails.append((phone,email))


def checker(record):
    #No errors "wrong token", but after some time can be a lot of errors "timeout" and "proxy error"
    global count
    email = record[1]
    phone = str(record[0]) 
    done = False
    error_count = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy)
            try:
                r = s.get(Url,headers=HeadersFirst,timeout=5)
            except Exception as exc:
                raise Exception("First one")
            token = r.text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
            Payload["UserName"] = email
            Payload["__RequestVerificationToken"] = token
            r = s.post(Url,headers=HeadersLast,data = Payload,timeout=5)
            response = r.text
            if "User Name was not found." not in response:
                from bs4 import BeautifulSoup
                item = BeautifulSoup(r.text,'html.parser').select_one("div#loginCard").text.replace("  ","").replace("\n\n","")
                log.add_records_to_logs(email)
                log.add_records_to_logs(item)

            s.close()
            done = True
            count+=1
            if count%50 == 0:
                print(f"{count} emails checked.")
                log.add_records_to_logs(f"{count} emails checked.")
        except Exception as exc:
            s.close()
            error_count +=1
            if error_count > 5:
                log.add_records_to_logs(exc)
                done = True
                skipped_emails.append((phone,email))


def main(start_from):
    global log
    global count
    global skipped_emails
    global chunk_results

    log = logs_handler("Logs/GuardianProtection")
    csv_handler.create("GuardianProtection")
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
            executor.map(checker_reset,chunk)
        log.add_records_to_logs(f"{count} emails checked.")
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