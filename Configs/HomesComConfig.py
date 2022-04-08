
HeadersMain = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.homes.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
}
HeadersPost = {
    "Accept":"application/json",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Authorization":"", #generated
    "Content-Type":"application/json",
    "Host":"microservices-ind.homes.com",
    "Referer":"https://www.homes.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

Payload = '[{"name":"email_exists","relative_url":"/myhomes-account/v1/exists/?email=EMAILTOCHECK","method":"GET"}]'


UrlMain = "https://www.homes.com/welcome/"
UrlPost = "https://microservices-ind.homes.com/v1/batch/?app=hdc_portal&app_platform=desktop"

