
HeadersFirst = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"secure.indeed.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
}

HeadersSecond = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "content-type":"application/x-www-form-urlencoded",
    "Host":"secure.indeed.com",
    "Origin":"https://secure.indeed.com",
    "Referer":"https://secure.indeed.com/auth",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
}

Payload = {
    "__email":"",
    "form_tk":"",
    "h-captcha-response":"",
}


FirstUrl = "https://secure.indeed.com/auth"
SecondUrl = "https://secure.indeed.com/account/emailvalidation"
UrlMiddle = "https://newassets.hcaptcha.com/captcha/v1/f5a464c/hcaptcha-checkbox.js"

UrlMiddleHeaders = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"newassets.hcaptcha.com",
    "Referer":"https://newassets.hcaptcha.com/captcha/v1/f5a464c/static/hcaptcha-checkbox.html",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}
