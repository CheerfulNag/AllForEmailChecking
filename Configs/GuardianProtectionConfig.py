def generate_pass():
    import string
    import random
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num
    passw = ""
    for x in range(0,20):
        passw += random.choice(all)
    return passw

HeadersFirst = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"customercare.guardianprotection.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

HeadersLast = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"customercare.guardianprotection.com",
    "Origin":"https://customercare.guardianprotection.com",
    "Referer":"https://customercare.guardianprotection.com/Account/Login?ReturnUrl=%2F",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

Payload = {
    "__RequestVerificationToken":"",
    "UserName":"",
    "Password":generate_pass(),
    "RememberMe":"false"
}

Url = "https://customercare.guardianprotection.com/Account/Login?ReturnUrl=/"


ResetHeadersOne = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"customercare.guardianprotection.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

ResetHeadersTwo = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"customercare.guardianprotection.com",
    "Origin":"https://customercare.guardianprotection.com",
    "Referer":"https://customercare.guardianprotection.com/Account/ForgotPassword",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}


ResetUrl = "https://customercare.guardianprotection.com/Account/ForgotPassword"

ResetPayload = {
    "__RequestVerificationToken":"",
    "ResetType":"Username",
    "Email":""
}




