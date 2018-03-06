import re

pattern = r'(.*?) (/[^?]*)[\?]*(.*) (.*/.*)\n([\s\S]*)'
compiler = re.compile(pattern)
'''Basic parser '''
class Http_parser(object):
	def __init__(self):
		pass
	
	#request
	def parse(self,raw_text):
		method = ""
		url = ""
		version = ""
		headers = dict()
		args = dict()
		data = dict()
		
		front,raw_data = raw_text.split('\n\n')
		request_method,url,raw_args,version,raw_headers,= compiler.findall(front)[0]
		for i in raw_args.split('&'):
			k,v = i.split('=')
			args[k] = v
		for i in raw_headers.split('\n'):
			k,v = re.findall(r'(.*): (.*)',i)[0]
			headers[k] = v
		for i in raw_data.split('&'):
			k,v = i.split('=')
			data[k] = v
			
		info = {
			'method':method,
			'url':url,
			'version':version,
			'headers':headers,
			'args':args,
			'data':data
			}
			
		return info
	
	#response
	def pack(self,headers,text):
		pass

	def url_split(self,url):
		return [ x for x in url.split('/') if x != '']
		