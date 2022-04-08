import traceback
from numpy import logical_and
import requests
import concurrent.futures
import time
import gc

from py.logs_handler import logs_handler
from py.stuff import FirstUrl,SecondUrl,Payload,Proxy,HeadersFirst,HeadersSecond
from py.csv_handler import csv_handler


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
            s.headers.update(HeadersFirst)
            resp = s.get(FirstUrl,timeout=5)
            print((resp,"First"))
            time.sleep(10)
            page_html = resp.text
            id_payload = page_html.split("var tk = encodeURIComponent('")[1].split("'")[0]



            #s.cookies.set('__ssid',"60431e9b12eer732a0c986304f233af",domain=".indeed.com") #this token is generated, but you can try to spot the pattern and 

            Payload["__email"] = email
            Payload["form_tk"] = id_payload

            payload = "__email={email}&form_tk={token}&h-captcha-response"

            

            #surf = page_html.split('"surftok":"')[1].split('"')[0]
            #print(surf)
            #preExtAuthParams = f'\\"form_tk={id_payload}&hl=en&surftok={surf}\\"'
            #s.cookies.set('preExtAuthParams',preExtAuthParams,domain=".indeed.com")
            #print(s.cookies)
            resp = s.post(SecondUrl,data=payload, headers=HeadersSecond,timeout=5)
            print((resp,"Second"))    
            print("-----------------")
            print(resp.json())
            s.close()
            #if "200" in str(resp):
            #    if ("True" in str(resp.json()['isEmailTaken'])) and ("False" in str(resp.json()['isEmailInvalid'])):
            #        chunk_results.append((phone,email,"Registered"))
            #else:
            #    raise Exception(f"Site's response code {resp}")
            done = True
            count +=1
        except Exception as exc:
            if "429" in str(exc):
                time.sleep(10)
            s.close()
            error_count +=1
            if error_count >5:
                done = True
                count+=1
                skipped_emails.append((phone,email))
                if "<Response [429]>" not in str(exc):
                    log.add_records_to_logs((email,exc))

    if count%50 == 0:
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


MaxWorkers = 1
ChunkSize = 500
InputName = "november_filtered"

main(0)









#from py.stuff import UrlMiddle,UrlMiddleHeaders
#r = s.get(UrlMiddle,headers=UrlMiddleHeaders,timeout=5)
#print((r,"Middle"))
#time.sleep(10)
#payload = payload.format(email = email.replace("@","%40"),token=id_payload )
#print(payload)





#apple_n = page_html.split('"nonce":"')[1].split('"')[0]
#print(apple_n)
#ctk = page_html.split('"ctk":"')[1].split('"')[0]
#print(ctk)
#nonce = page_html.split("nonce=")[1].split("\\")[0]
#print(nonce)
#surf = page_html.split('"surftok":"')[1].split('"')[0]
#print(surf)
#preExtAuthParams = f'\\"form_tk={id_payload}&hl=en&surftok={surf}\\"'

#s.cookies.set('APPLE_N',apple_n,domain=host)
#s.cookies.set('CTK',ctk,domain=host)
#s.cookies.set('nonce',nonce,domain=host)
#s.cookies.set('preExtAuthParams',preExtAuthParams,domain=host)
#s.cookies.set('SURF',surf,domain=host)

