from http_parser import Http_parser

P = Http_parser()

http_text = '''GET /sth/like/this?a=1&b=2 HTTP/1.1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: keep-alive\r\nCookie: BAIDUID=919BCCD72A22B015CBFAAADB2FFAAE14:FG=1; BIDUPSID=919BCCD72A22B015CBFAAADB2FFAAE14; PSTM=1520343903; BD_LAST_QID=11840384597735017536\r\nHost: www.baidu.com\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0\r\n\r\nc=3&d=4'''

http_text = '''GET / HTTP/1.1\r\nHost: 127.0.0.1:8989\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0 Light/49.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nDNT: 1\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1'''

http_text = '''GET /test/aaa HTTP/1.1\r\nHost: 127.0.0.1:8989\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=0'''

r = P.parse(http_text)
print('\nrequest info:\n'+r.__str__())

u = P.url_split(r['url'])
print('\nsplited url:\n'+u.__str__())

s = P.pack(**{'headers':{'server':'Tiny_server'},'text':'Hello web'})
print('\npacked response:\n'+s)



