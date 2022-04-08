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
    "Host":"proofing.statefarm.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

HeadersFinal = {
    "Accept":"application/json",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/json",
    "Host":"proofing.statefarm.com",
    "Origin":"https://proofing.statefarm.com",
    "Referer":"https://proofing.statefarm.com/login-ui/login",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "X-SF_DEVICE_PRINT":"version=3.5.1_4&pm_fpua=mozilla/5.0 (windows nt 10.0; win64; x64; rv:98.0) gecko/20100101 firefox/98.0|5.0 (Windows)|Win32&pm_fpsc=24|1920|1080|1080&pm_fpsw=&pm_fptz=3&pm_fpln=lang=en-US|syslang=|userlang=&pm_fpjv=0&pm_fpco=1&pm_fpasw=&pm_fpan=Netscape&pm_fpacn=Mozilla&pm_fpol=true&pm_fposp=&pm_fpup=&pm_fpsaw=1920&pm_fpspd=24&pm_fpsbd=&pm_fpsdx=&pm_fpsdy=&pm_fpslx=&pm_fpsly=&pm_fpsfse=&pm_fpsui=&pm_os=Windows&pm_brmjv=98&pm_br=Firefox&pm_inpt=&pm_expt="
}

Payload = {
    "IDToken1":"",
    "IDToken2":generate_pass(),
    "IDToken3":"version=3.5.1_4&pm_fpua=mozilla/5.0 (windows nt 10.0; win64; x64; rv:98.0) gecko/20100101 firefox/98.0|5.0 (Windows)|Win32&pm_fpsc=24|1920|1080|1080&pm_fpsw=&pm_fptz=3&pm_fpln=lang=en-US|syslang=|userlang=&pm_fpjv=0&pm_fpco=1&pm_fpasw=&pm_fpan=Netscape&pm_fpacn=Mozilla&pm_fpol=true&pm_fposp=&pm_fpup=&pm_fpsaw=1920&pm_fpspd=24&pm_fpsbd=&pm_fpsdx=&pm_fpsdy=&pm_fpslx=&pm_fpsly=&pm_fpsfse=&pm_fpsui=&pm_os=Windows&pm_brmjv=98&pm_br=Firefox&pm_inpt=&pm_expt=",
    "IDToken4":"false",
}

UrlFirst = "https://proofing.statefarm.com/login-ui/login"
UrlLast = "https://proofing.statefarm.com/login-interceptor/authenticate?callingApplication=&cancel=https://www.statefarm.com&goto=https://apps.statefarm.com/my-accounts"