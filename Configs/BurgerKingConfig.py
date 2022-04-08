headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "content-type":"application/json",
    "Host":"use1-prod-bk.rbictg.com",
    "Origin":"https://www.bk.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
}

payload = {
    "operationName":"CreateOTP",
    "variables":{"input":{"email":"","platform":"web","sessionId":""}},
    "query":"mutation CreateOTP($input: CreateOTPInput!) {\n  createOTP(input: $input) {\n    maxValidateAttempts\n    ttl\n    __typename\n  }\n}\n"}
    
url_get_answer = "https://use1-prod-bk.rbictg.com/graphql"
