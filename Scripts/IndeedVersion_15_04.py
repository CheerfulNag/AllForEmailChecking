
import requests
import concurrent.futures
import time
import gc
import sys
import random

sys.path.append("./")
from SharedModules.Proxy import Proxy
from Configs.IndeedConfig import MainUrl,PostUrl,HeadersMain,HeadersPost,Payload,HeadersJs
from SharedModules.csv_handler import csv_handler
from SharedModules.logs_handler import logs_handler


def checker_backup (record):
    #Works with one thread, both with JS requests and without it
    global count
    email = record[1]

    phone = str(record[0])
    done = False
    error_count = 0
    email_valid = 0
    while not done:
        try:
            s = requests.Session()
            s.proxies.update(Proxy)
            s.headers.update(HeadersMain)
            r = s.get(MainUrl,timeout=5)
            page_html = r.text

            Ctk = s.cookies["CTK"]
            Surf = s.cookies["SURF"]

            Apple_N = s.cookies["APPLE_N"]
            Nonce = s.cookies["nonce"]

            #s.cookies.clear()
            #s.cookies.set('CTK', Ctk, domain=".indeed.com")
            #s.cookies.set('SURF', Surf, domain=".indeed.com")


            id_payload = page_html.split("var tk = encodeURIComponent('")[1].split("'")[0]
            Payload["__email"] = email
            Payload["form_tk"] = id_payload
            #LogId = page_html.split('"turnstileOriginLogId":"')[1].split('"')[0]
            #Olth = page_html.split('"turnstileHash":"')[1].split('"')[0]
            #LogIdSmall = page_html.split('","serviceRequestLogUID":"')[1].split('"')[0]
            #Lth = page_html.split('","jsEnabledLth":"')[1].split('"')[0]
            #JsUrl1 = f'https://t.indeed.com/gnav/log?from=passport--passport-webapp-/auth&parentLogId={LogIdSmall}&hostAppTk=&logType=gnavJSEnabled&lth={Lth}&jsEnabled=1'
            #r  = s.get(JsUrl1,headers=HeadersJs,timeout=5)
            #LthNew = page_html.split('"pageSpeedLth":"')[1].split('"')[0]
#
            #FirstNumb = random.randint(640,695)
            #ThirdNumb = FirstNumb + random.randint(1,3)
            #Numb4 = ThirdNumb + random.randint(230,300)
            #Numb5 = Numb4 - random.randint(100,150)
            #Numb6 = Numb4 + random.randint(900,1000)
            #Numb7 = Numb4 + random.randint(2200,2500)
            #Numb8 = Numb7 + random.randint(15,20)
            #Numb9 = Numb8 + random.randint(15,20)
            #Numb10 = Numb9 + random.randint(1500,2000)
            #Numb11 = Numb10 + random.randint(2,5)
            #JsUrl2 = f'https://t.indeed.com/gnav/log/?hostAppTk=&canonicalPageId=&connectionType=unknown&parentLogId={LogIdSmall}&logType=gnavPageSpeed&lth={LthNew}&application=globalnav&navigationStart=0&unloadEventStart=-1&unloadEventEnd=-1&redirectStart=-1&redirectEnd=-1&fetchStart=1&domainLookupStart={FirstNumb}&domainLookupEnd={FirstNumb}&connectStart={ThirdNumb}&connectEnd={Numb4}&secureConnectionStart={Numb5}7&requestStart={Numb4}&responseStart={Numb4}&responseEnd={Numb4}&domLoading={Numb6}&domInteractive={Numb6}&domContentLoadedEventStart={Numb8}&domContentLoadedEventEnd={Numb9}&domComplete={Numb10}&loadEventStart={Numb10}&loadEventEnd={Numb11}&navTimeApiIsSupported=1&navigationType=-1&redirectCount=-1&paintTimingApiIsSupported=1&firstContentfulPaint=-1&firstPaint=-1'
            #from Configs.IndeedConfig import HeadersJs2
            #r  = s.get(JsUrl2,headers=HeadersJs2,timeout=5)
            #JsUrl3 = f'https://t.indeed.com/log?application=passport-webapp&component=auth-page-email-input&element=auth-page-email-input-form-field&action=click&originUrl=https://secure.indeed.com/auth&originLogType=passPageLoad&originLogId={LogId}&olth={Olth}'
            #
            #r  = s.get(JsUrl3,headers=HeadersJs,timeout=5)
#
            #JsUrl4 = f'https://t.indeed.com/log?application=passport-webapp&component=auth-page-email-input&element=auth-page-email-submit-button&action=click&originUrl=https://secure.indeed.com/auth&originLogType=passPageLoad&originLogId={LogId}&olth={Olth}'
#
            #r  = s.get(JsUrl4,headers=HeadersJs,timeout=5)
            #s.cookies.clear()
            s.cookies.set('CTK', Ctk, domain=".indeed.com")
            s.cookies.set('SURF', Surf, domain=".indeed.com")
            s.cookies.set('APPLE_N', Apple_N, domain=".indeed.com")
            s.cookies.set('nonce', Nonce, domain=".indeed.com")
            preExtAuthParams = f"form_tk={id_payload}&hl=en&surftok={Surf}"
            s.cookies.set('preExtAuthParams', preExtAuthParams, domain=".indeed.com")

            r = s.post(PostUrl,data=Payload, headers=HeadersPost,timeout=5)
            response = r.json()

            if response["isEmailInvalid"] == True:
                raise Exception("EmailInvalid")

            if (response["isEmailInvalid"]==False) and (response["isEmailTaken"]==True):
                    log.add_records_to_logs((email))

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

            Ctk = s.cookies["CTK"]
            Surf = s.cookies["SURF"]

            Apple_N = s.cookies["APPLE_N"]
            Nonce = s.cookies["nonce"]

            id_payload = page_html.split("var tk = encodeURIComponent('")[1].split("'")[0]
            Payload["__email"] = email
            Payload["form_tk"] = id_payload

            s.cookies.clear()
            #s.cookies.set('CTK', Ctk, domain=".indeed.com")
            #s.cookies.set('SURF', Surf, domain=".indeed.com")
            #s.cookies.set('APPLE_N', Apple_N, domain=".indeed.com")
            #s.cookies.set('nonce', Nonce, domain=".indeed.com")
            #preExtAuthParams = f"form_tk={id_payload}&hl=en&surftok={Surf}"
            #s.cookies.set('preExtAuthParams', preExtAuthParams, domain=".indeed.com")


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
InputName = "ChrisjankonRecreated"

main(0)

#"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#('mommora71@gmail.com', {'suggestedDomain': '', 'hrtechSSOUrl': None, 'enterpriseSSOUrl': None, 'isEmailTaken': True, 'isDomainFree': True, 'isDomainGSuite': True, 'isEmailInvalid': False})


#30700, one thread, 3 JS requests before the actual one - working
#30400, 10 threads, 3 JS requests before the actual one - broken