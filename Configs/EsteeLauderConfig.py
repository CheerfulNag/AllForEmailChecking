
headers_first = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.esteelauder.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

headers_second = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.esteelauder.com",
    "Origin":"https://www.esteelauder.com",
    "Referer":"https://www.esteelauder.com/account/signin.tmpl",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

first_url = "https://www.esteelauder.com/account/signin.tmpl"

second_url = "https://www.esteelauder.com/account/signin.tmpl"

payload = {
    "_SUBMIT":"signin",
    "_TOKEN":"", #crsf
    "EMAIL_ADDRESS":"vorolexas@gmail.com",
    "PASSWORD":"d12d2d12d2d12", #Random
    "RETURN_URL":"",
    "LOSTPWMODE":"signin",
    "IS_PRO":"0",
    "op":"Sign+In",
    "":"",
}

