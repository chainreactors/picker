---
title: 网站加密传输场景下的通用漏扫思路
url: https://zgao.top/%e7%bd%91%e7%ab%99%e5%8a%a0%e5%af%86%e4%bc%a0%e8%be%93%e5%9c%ba%e6%99%af%e4%b8%8b%e7%9a%84%e6%bc%8f%e6%b4%9e%e6%89%ab%e6%8f%8f%e6%80%9d%e8%b7%af/
source: Zgao's blog
date: 2023-07-12
fetch_date: 2025-10-04T11:51:22.748905
---

# 网站加密传输场景下的通用漏扫思路

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 网站加密传输场景下的通用漏扫思路

* [首页](https://zgao.top)
* [网站加密传输场景下的通用漏扫思路](https://zgao.top:443/%E7%BD%91%E7%AB%99%E5%8A%A0%E5%AF%86%E4%BC%A0%E8%BE%93%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%E6%80%9D%E8%B7%AF/)

[7月 11, 2023](https://zgao.top/2023/07/)

### 网站加密传输场景下的通用漏扫思路

作者 [Zgao](https://zgao.top/author/zgao/)
在[[渗透测试](https://zgao.top/category/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)](https://zgao.top/%E7%BD%91%E7%AB%99%E5%8A%A0%E5%AF%86%E4%BC%A0%E8%BE%93%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%E6%80%9D%E8%B7%AF/)

![](https://zgao.top/wp-content/uploads/2023/07/image-1024x259.png)

最近的一个渗透项目中，网站的流量用到了AES+SM4 两层加密算法加密传输。遇到传输加密的网站，通常是没办法上漏扫的。奈何手工测试效率太低，故研究了加密传输场景下漏洞扫描通用解决思路。

文章目录

[ ]

* [如何加解密传输流量？](#%E5%A6%82%E4%BD%95%E5%8A%A0%E8%A7%A3%E5%AF%86%E4%BC%A0%E8%BE%93%E6%B5%81%E9%87%8F%EF%BC%9F "如何加解密传输流量？")
  + [用Python重新实现加解密算法](#%E7%94%A8Python%E9%87%8D%E6%96%B0%E5%AE%9E%E7%8E%B0%E5%8A%A0%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95 "用Python重新实现加解密算法")
  + [JSRPC 转发加解密函数](#JSRPC_%E8%BD%AC%E5%8F%91%E5%8A%A0%E8%A7%A3%E5%AF%86%E5%87%BD%E6%95%B0 "JSRPC 转发加解密函数")
* [Mitmproxy 对流量进行加解密](#Mitmproxy_%E5%AF%B9%E6%B5%81%E9%87%8F%E8%BF%9B%E8%A1%8C%E5%8A%A0%E8%A7%A3%E5%AF%86 "Mitmproxy 对流量进行加解密")
  + [mitmproxy命令行](#mitmproxy%E5%91%BD%E4%BB%A4%E8%A1%8C "mitmproxy命令行")
  + [mitmproxy 代码模版](#mitmproxy_%E4%BB%A3%E7%A0%81%E6%A8%A1%E7%89%88 "mitmproxy 代码模版")
    - [第一次流量加解密代码模板](#%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%B5%81%E9%87%8F%E5%8A%A0%E8%A7%A3%E5%AF%86%E4%BB%A3%E7%A0%81%E6%A8%A1%E6%9D%BF "第一次流量加解密代码模板")
    - [第二次流量加解密代码模版](#%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%B5%81%E9%87%8F%E5%8A%A0%E8%A7%A3%E5%AF%86%E4%BB%A3%E7%A0%81%E6%A8%A1%E7%89%88 "第二次流量加解密代码模版")
* [xray的配置修改](#xray%E7%9A%84%E9%85%8D%E7%BD%AE%E4%BF%AE%E6%94%B9 "xray的配置修改")
* [实战测试](#%E5%AE%9E%E6%88%98%E6%B5%8B%E8%AF%95 "实战测试")

## 如何加解密传输流量？

这里通常是有两种方式来实现。

### 用Python重新实现加解密算法

如果网站的加密算法是标准的加密算法如AES等，可以直接用Python的pycrypto模块原生实现。遇到相对简单的加密算法也可以把js中的加解密代码抠出来，用Python的execJs执行得到结果。

例如用Python手动实现网站的加解密代码如下：

![](https://zgao.top/wp-content/uploads/2023/07/image-1-1024x913.png)

这种方式只能实现简单的加密算法，而且需要写代码处理相对麻烦。

### JSRPC 转发加解密函数

如果遇到复杂的加解密算法，比如某些在标准算法上魔改的算法，根本没法从JS中扣出关键代码的场景，就非常适合jsrpc的方式直接调用浏览器中的加解密函数。

<https://github.com/jxhczhl/JsRpc>

![](https://zgao.top/wp-content/uploads/2023/07/image-2-1024x641.png)

既然网站的传输内容是加密的，所以就需要在流量进入被动扫描器之前把流量先进行解密。

## Mitmproxy 对流量进行加解密

[mitmproxy](https://mitmproxy.org/) 就是用于 MITM 的 proxy，MITM 即中间人攻击（Man-in-the-middle attack）。用于中间人攻击的代理首先会向正常的代理一样转发请求，还能适时的查、记录其截获的数据，或篡改数据，引发服务端或客户端特定的行为。不同于 fiddler 或 wireshark 等抓包工具，mitmproxy 不仅可以截获请求帮助开发者查看、分析，更可以通过自定义脚本进行二次开发。

上面提到可以用Python重新实现加解密算法，但是在流量进入到被动扫描器之前，需要有一个中间人来做加解密操作，而mitmproxy就充当了这个角色。可以把Python实现加解密的代码放在mitmproxy中运行，在系统中安装信任mitmproxy的证书，让mitmproxy解密https的流量后再进行二次解密。

### mitmproxy命令行

第一个mitmproxy的命令行需要设置上游代理为xray监听的ip和端口。

```
mitmdump -s code.py -p 8010 --set block_global=false --mode upstream:http://xray-ip:port --ssl-insecure
```

第二个mitmproxy的命令行是直接转发给目标网站的。

```
mitmdump -s code.py -p 8020 --set block_global=false --ssl-insecure
```

### mitmproxy 代码模版

由于流程中涉及到4次mitmproxy的加解密，所以要开启两个mitmproxy监听端口来转发流量。

#### 第一次流量加解密代码模板

```
from mitmproxy import http

# 加解密函数可以用Python重新实现，也可以用jsrpc直接转发加解密函数接口

# 解密函数
def myEncrypt(data):
    pass

# 解密函数
def myDecrypt(data):
    pass

# 对 浏览器 请求内容进行解密，转发给 扫描器
def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host != "target.com":
        return          # 如果不是目标域名，直接转发不做任何操作
    try:
        param = flow.request.content.decode()
        decryptData = myDecrypt(param)

        print("第一次请求解密：\n"+decryptData)

        # 将解密后的报文替换加密报文
        flow.request.content = decryptData

    except Exception as e:
        print(f"报文解密失败: {e}")

# 对 扫描器 响应内容进行加密，转发给 浏览器
def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host != "target.com":
        return          # 如果不是目标域名，直接转发不做任何操作
    try:
        param = flow.response.content.decode()
        encryptData = myEncrypt(param)

        print("第一次响应加密：\n" + encryptData)

        # 将明文的报文加密传输
        flow.response.content = encryptData

    except Exception as e:
        print(f"报文加密失败: {e}")
```

#### 第二次流量加解密代码模版

```
from mitmproxy import http

# 加解密函数可以用Python重新实现，也可以用jsrpc直接转发加解密函数接口

# 解密函数
def myEncrypt(data):
    pass

# 解密函数
def myDecrypt(data):
    pass

# 对 扫描器 请求内容进行加密，转发给 网站
def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host != "target.com":
        return          # 如果不是目标域名，直接转发不做任何操作
    try:
        param = flow.request.content.decode()
        encryptData = myEncrypt(param)

        print("第二次请求加密：\n" + encryptData)

        # 将明文报文替换为加密报文
        flow.request.content = encryptData

    except Exception as e:
        print(f"报文加密失败: {e}")

# 对 网站 响应内容进行解密，转发给 扫描器
def response(flow: http.HTTPFlow) -> None:
    if flow.response.pretty_host != "target.com":
        return          # 如果不是目标域名，直接转发不做任何操作
    try:
        param = flow.response.content.decode()
        decryptData = myDecrypt(param)

        print("第二次请求解密：\n"+decryptData)

        # 将加密报文替换为明文报文
        flow.response.content = decryptData

    except Exception as e:
        print(f"报文解密失败: {e}")
```

## xray的配置修改

因为在xray的前后都有mitmproxy对流量进行加解密，所以xray只需要配置上游代理即可。但是需要修改两处配置，http和upstream\_proxy都要改为mitmproxy的ip端口。

![](https://zgao.top/wp-content/uploads/2023/07/image-3-1024x531.png)

![](https://zgao.top/wp-content/uploads/2023/07/image-4-1024x610.png)

## 实战测试

![](https://zgao.top/wp-content/uploads/2023/07/image-5-1024x579.png)

虽然加密传输场景下的渗透测试流程上比较复杂，但是流量本身自带加密，waf也拦截不了，也省了些麻烦事。

实战中使用上面我提供的mitmproxy模版并替换加解密函数，就可以对加密传输的网站直接上漏扫了，收工！

Post Views: 1,518

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 2条评论

###### 张飞 发布于3:12 下午 - 10月 16, 2023

大佬思路就是骚

[回复](https://zgao.top/%E7%BD%91%E7%AB%99%E5%8A%A0%E5%AF%86%E4%BC%A0%E8%BE%93%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%E6%80%9D%E8%B7%AF/?replytocom=6082#respond)

###### zgaolove666 发布于7:13 下午 - 7月 12, 2023

还得是zgao

[回复](https://zgao.top/%E7%BD%91%E7%AB%99%E5%8A%A0%E5%AF%86%E4%BC%A0%E8%BE%93%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%E6%80%9D%E8%B7%AF/?replytocom=5534#respond)

### 发表评论 [取消回复](/%E7%BD%91%E7%AB%99%E5%8A%A0%E5%AF%86%E4%BC%A0%E8%BE%93%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%E6%80%9D%E8%B7%AF/#respond)

Δ

版权©2020 Author By : Zgao