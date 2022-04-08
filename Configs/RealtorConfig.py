
HeadersFirst = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.realtor.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}


HeadersOptionsFirst = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Access-Control-Request-Headers":"content-type",#,x-braze-api-key,x-braze-contentcardsrequest,x-braze-datarequest,x-requested-with",#,x-braze-api-key,x-braze-contentcardsrequest,x-braze-datarequest,x-requested-with",
    "Access-Control-Request-Method":"POST",
    "Host":"sdk.iad-01.braze.com",
    "Origin":"https://www.realtor.com",
    "Referer":"https://www.realtor.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}


HeadersOptionsLast = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Access-Control-Request-Headers":"adobe-vistor,adobe_vistor,content-type",
    "Access-Control-Request-Method":"GET",
    "Connection":"keep-alive",
    "Host":"myaccount.realtor.com",
    "Origin":"https://www.realtor.com",
    "Referer":"https://www.realtor.com/",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "Sec-GPC":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"#,
}

HeadersLast = {
    "Accept":"application/json",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Connection":"keep-alive",
    "Content-Type":"application/json",
    "Host":"myaccount.realtor.com",
    "Origin":"https://www.realtor.com",
    "Referer":"https://www.realtor.com/",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "Sec-GPC":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}

PayloadAccessControl = {
    "device":{
        "browser":"Firefox",
        "browser_version":"98.0",
        "os_version":"Windows",
        "resolution":"1920x1080",
        "locale":"en-us",
        "time_zone":"Europe/Moscow",
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"},
    "api_key":"7cc9d032-9d6d-44cf-a8f5-d276489af322",
    "time":"",
    "sdk_version":"3.5.1",
    "device_id":"f196649c-e79b-8ea2-c464-3ead30adc0b8",
    "sdk_metadata":["wcd"],
    "last_full_sync_at":0,
    "last_card_updated_at":0,
    "user_id":""} #visitor_d40f7f71-4c8c-4cf6-b401-550a5bd8ce9a

FirstUrl = "https://www.realtor.com/"

AccessControlUrl = "https://sdk.iad-01.braze.com/api/v3/content_cards/sync"

MainUrl = "https://myaccount.realtor.com/find_user_by_email/"
