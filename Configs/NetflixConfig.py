import string
import random

def FormatPayload(email,password,authURL,payload_dict):
    payload_object = payload_dict
    payload_object["userLoginId"] = email
    payload_object["password"] = password
    payload_object["authURL"] = authURL
    return payload_object

def PassGenerator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num
    passw = ""
    for x in range(0,20):
        passw += random.choice(all)
    return passw

HeadersMain = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.netflix.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}

HeadersPost = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"www.netflix.com",
    "Origin":"https://www.netflix.com",
    "Referer":"https://www.netflix.com/login",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
}

MainUrl = "https://www.netflix.com/Login"

Payload = {
    "userLoginId":"",
    "password":"",
    "rememberMe":"true",
    "flow":"websiteSignUp",
    "mode":"login",
    "action":"loginAction",
    "withFields":"rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode,recaptchaResponseToken,recaptchaError,recaptchaResponseTime",
    "authURL":"",
    "nextPage":"",
    "showPassword":"",
    "countryCode":"+1",  
    "countryIsoCode":"US"
}





