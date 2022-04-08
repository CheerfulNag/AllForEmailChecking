def generate_pass():
    import string
    import random
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + num + upper 
    passw = ""
    for x in range(0,32):
        passw += random.choice(all)
    return passw


HeadersFirst = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.linkedin.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

HeadersSecond = {  #Same as final
    "Accept":"application/json, text/plain, */*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/json;charset=utf-8",
    "Host":"api.bodybuilding.com",
    "Origin":"https://www.bodybuilding.com",
    "Referer":"https://www.bodybuilding.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

HeadersFinal = {
    "Accept":"application/json, text/plain, */*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/json;charset=utf-8",
    "Host":"api.bodybuilding.com",
    "Origin":"https://www.bodybuilding.com",
    "Referer":"https://www.bodybuilding.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

PayloadFirst = {
    "username":"fgeahkfaksjf@gmail.com",
    "password":"02a13c55564a94c9a3798a088f3719be"
    }

PayloadFinal = {
    "challenge":
        {"iterations":"",
        "timestamp":"",
        "version":"",
        "dataToHash":"",
        "hashMethod":"",
        "username":"",
        "password":"",
        "showCaptcha":"false",
        "verificationUrl":"https://api.bodybuilding.com/login/web/verify",
        "signature":""},
    "hashResult":""} #leave empty


UrlFirst = "https://www.bodybuilding.com/combined-signin"
UrlSecond = "https://api.bodybuilding.com/login/web"
UrlLast = "https://api.bodybuilding.com/login/web/verify"
























#HeadersOptions_Both = {
#    "Accept":"*/*",
#    "Accept-Encoding":"gzip, deflate, br",
#    "Accept-Language":"en-US,en;q=0.5",
#    "Access-Control-Request-Headers":"content-type",
#    "Access-Control-Request-Method":"POST",
#    "Host":"api.bodybuilding.com",
#    "Origin":"https://www.bodybuilding.com",
#    "Referer":"https://www.bodybuilding.com/",
#    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
#}