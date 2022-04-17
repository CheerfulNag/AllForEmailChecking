
HeadersMain = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    #"Connection":"keep-alive",
    "Host":"secure.indeed.com",
    #"Sec-Fetch-Dest":"document",
    #"Sec-Fetch-Mode":"navigate",
    #"Sec-Fetch-Site":"none",
    #"Sec-Fetch-User":"?1",
    #"Sec-GPC":"1",
    #"Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

HeadersJs = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Connection":"keep-alive",
    "Host":"t.indeed.com",
    "Referer":"https://secure.indeed.com/auth",
    "Sec-Fetch-Dest":"script",
    "Sec-Fetch-Mode":"no-cors",
    "Sec-Fetch-Site":"same-site",
    "Sec-GPC":"1",
    "TE":"trailers",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
}

HeadersJs2 = {
    "Accept":"image/avif,image/webp,*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Connection":"keep-alive",
    "Host":"t.indeed.com",
    "Referer":"https://secure.indeed.com/auth",
    "Sec-Fetch-Dest":"script",
    "Sec-Fetch-Mode":"no-cors",
    "Sec-Fetch-Site":"same-site",
    "Sec-GPC":"1",
    "TE":"trailers",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
}

HeadersPost = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    #"Connection":"keep-alive",
    "content-type":"application/x-www-form-urlencoded",
    "Host":"secure.indeed.com",
    "Origin":"https://secure.indeed.com",
    "Referer":"https://secure.indeed.com/auth",
    #"Sec-Fetch-Dest":"empty",
    #"Sec-Fetch-Mode":"cors",
    #"Sec-Fetch-Site":"same-origin",
    #"Sec-GPC":"1",
    #"TE":"trailers",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

Payload = {
    "__email":"",
    "form_tk":"",
    "h-captcha-response":"",
}



MainUrl = "https://secure.indeed.com/auth"
PostUrl = "https://secure.indeed.com/account/emailvalidation"














#Useful for the future updates
#Apple_N = s.cookies["APPLE_N"]
#Ctk = s.cookies["CTK"]
#Nonce = s.cookies["nonce"]
#Surf = s.cookies["SURF"]
#s.cookies.clear()
#s.cookies.set('CTK', Ctk, domain=".indeed.com")
#s.cookies.set('SURF', Surf, domain=".indeed.com")
#preExtAuthParams = f"form_tk={id_payload}&hl=en&surftok={Surf}"
#s.cookies.set('preExtAuthParams', preExtAuthParams, domain=".indeed.com")