from http_parser import Http_parser

P = Http_parser()

http_text = '''GET /sth/like/this?a=1&b=2 HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
Cookie: BAIDUID=919BCCD72A22B015CBFAAADB2FFAAE14:FG=1; BIDUPSID=919BCCD72A22B015CBFAAADB2FFAAE14; PSTM=1520343903; BD_LAST_QID=11840384597735017536
Host: www.baidu.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0

c=3&d=4'''

r = P.parse(http_text)
print('\nrequest info:\n'+r.__str__())

u = P.url_split(r['url'])
print('\nsplited url:\n'+u.__str__())

s = P.pack(**{'headers':{'server':'Tiny_server'},'text':'Hello web'})
print('\npacked response:\n'+s)



