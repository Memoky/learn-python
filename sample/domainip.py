# -*- coding:utf-8 -*-
#auother: memoky

import requests
import json
import dns.resolver


url_input=input("Enter url:")  #enter url
def get_listip(domain):
	try:
		url_res = dns.resolver.query(domain, 'A')
	except Exception as e:
		print("error" +str(e))
		return
	for rdata in url_res:
		ip_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + rdata.address 
		r = requests.get(ip_url)
		paf = json.loads(r.text)
		print(str(rdata) + ' ' + paf['data']['country'], paf['data']['area'], paf['data']['region'], paf['data']['county'],paf['data']['city'], paf['data']['isp'])
	return 
	
get_listip(url_input)




