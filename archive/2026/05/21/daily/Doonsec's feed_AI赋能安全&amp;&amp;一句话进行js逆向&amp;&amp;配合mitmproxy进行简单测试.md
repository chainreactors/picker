---
title: AI赋能安全&amp;&amp;一句话进行js逆向&amp;&amp;配合mitmproxy进行简单测试
url: https://mp.weixin.qq.com/s/zPD_f5Equ8SeCdrsOLomYw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:02:06.881596
---

# AI赋能安全&amp;&amp;一句话进行js逆向&amp;&amp;配合mitmproxy进行简单测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSMlf0r7wUQM5RFNJTeN1GvGj42Wp7J03g8gPGVV3xEEjJXibTxqpicjBhJZ0ux2kjVjJ8ykXpvvSyiblYVGwOQJwzjhofKxplic1U/0?wx_fmt=jpeg)

# AI赋能安全&&一句话进行js逆向&&配合mitmproxy进行简单测试

原创

是陌不是笙
是陌不是笙

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文首发于先知
作者:是陌不是笙原文链接:https://xz.aliyun.com/news/92139
```

# 前言

在日常渗透测试与安全测试中，前端加密（尤其是登录参数的加密）是绕不开的一类场景。

传统的手工 JS 逆向虽然可靠，但往往需要投入大量时间在定位加密逻辑、调试堆栈、编写脚本等重复性工作上。

随着 AI 辅助编程工具的普及，这类问题正在被大幅简化。本文将以一个实际的edusrc登录页面为例，探索如何将 AI 能力引入 JS 逆向流程：

自动分析加密参数：通过自然语言指令，让 AI 直接定位 mm 参数的加密逻辑。

自动生成加密脚本：无需手动翻译加密算法，AI 可直接输出可运行的 Python 脚本用于验证。

联动 Burp 与 mitmproxy：将生成的脚本作为中间人代理，一键接入 Burp 的 Intruder 模块，实现加密参数的自动化爆破测试。

通过本文的实践，你将看到：一句自然语言 + 一个 MCP 环境 + 一套代理链路，如何将原本至少需要几十分钟的 JS 逆向工作，压缩到几分钟内完成。

# 测试流程

通过信息收集拿到这个网站

https://xxxx.edu.cn/xtgl/login\_mobileLogin.html

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQuzcg7TWeiaH6F5t6xWETvZHSa6XYyHxeHLiaBlm33yrPZsr5TmdFF2XKDtXbCSqrAKqRAticaWZ9r6gKKiaunylnsHTq8j4S2rtk/640?wx_fmt=png&from=appmsg)

随便输入一个用户名和密码点击登录

来到网络这里进行抓包->查看负载

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS2GzoervwhxcBM9x0s8qEMB2nR90kDxiaHDym9LyW4RoV9I4Ues0SwxcTtGRicfiaWLvQ8KCOycXgW70bO9u5u8jLGqEptsCTMQU/640?wx_fmt=png&from=appmsg)

发现密码参数是被加密的

我们先手工js逆向试试

一般我会习惯性的搜索这个请求的url

如果没有找到的话，之后再去搜索这种加密相关的关键字

```
 encrypt、encryptedData、setpublickey，Crypto,AES,RSA,CryptoJS,key
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRg1tK7UkMDvb3lYVlUfsDicqaf6FMjZWvSplI5uFzQJU5tsBAcsvfQZZQxA8oHLZm1a0Fp7VB45cbPc3CxPEYULQsS45lNvKCs/640?wx_fmt=png&from=appmsg)

上下找找，成功找到了加密方式，AES的CBC加密，key，iv都给出来了，我们直接打个断点调试一下

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSSvoBkUJ4nwVJMRX87qU2Ra2egb4mD5lcyVMmZYkK0n17JCTH3pSfwEUgqOhH9tKSRWcYgLHzmm3n9El8gdX7ictle689C044Y/640?wx_fmt=png&from=appmsg)

打几个断点，点击登录进行触发，进入作用域

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTJS0YLsU3xNIU10BnteicdAI6ia1OvvYicHVtLYY6icYXWBT44qIibJOmSQ2FiaxYRNzfUSwaUJdW2xghI6ChJ65P7icQ6ZLEDhTTCFU/640?wx_fmt=png&from=appmsg)

直接断到了，说明登录确实会触发这个加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRm6tJCGsPePZNOo3MibafEAicAwC8HcywhtEkPWssICnibrm9VSX2Cia6WE4UUBNhgMGpxWJHpcoyyGegFTianXLIm2R8GNcNdsPuM/640?wx_fmt=png&from=appmsg)

之后继续点击单步调试，发现这里会直接调回加密的方法，我们直接在控制台进行调用测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSg4V2LltTaz3qwdoOyEslbBdo10icQcFaQVYamRN6oTNJAt8Ccm82rsY9daf1kP4qicUkN3GlC0qkyBDZicV0gibGMontn7jwLhT0/640?wx_fmt=png&from=appmsg)

成功逆向，这里可以写解密脚本配合mitmproxy进行爆破，或者使用burp插件autoDecorder进行解决

抛开手动js逆向，这里我们可以直接使用浏览器插件AntiDebug\_Breaker测试

工具地址

https://github.com/0xsdeo/AntiDebug\_Breaker

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSMaiadUibaSggcZeQwuuiaPUwLydvx0gd6tyia9kguBGE4qVaicEcrs3RD0lV7ibXo9ibWlDQibIXx9xKpkfPcOT4DbjcCxfGfhG7bBR8/640?wx_fmt=png&from=appmsg)

安装之后，开启这个选项

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQwmCuC7xkaZZg1cktiaiaBXauITeoYGfS51S3vIS4nK8YIMFcqAY8SPiaVuvXzHlKJcTsIC4o7VfIIafdOXj1b8B9B0YdNwBaaso/640?wx_fmt=png&from=appmsg)

刷新页面，直接给你吐加密信息，然后可以使用插件解密，验证之后写脚本进行爆破

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQKDYUCMTSG2XOo0ibyIEwOVNJJUbWibh8EibFFib8vMIZUnIIEkscZrykibp6sLV3c0C6aXF6xibjy5lZuHlKp00MdJ4hQOicvYFpACk/640?wx_fmt=png&from=appmsg)

但是AI时代我们有更简单的方法

下载TRAE,我是windows直接下载这个，如果师傅们是其他操作系统，选择对应的就行

https://www.trae.cn/ide/download

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTLY0ahRb0Y6Y3Z4dm3zbEYnnL4GbmBmrKmjQosn5uPD61o0K67PkCC0E0TLcrm2NWbjRxutVsVJzA0by0D0Xc6Cve2SNwOXFo/640?wx_fmt=png&from=appmsg)

下载之后点击安装，然后选择我同意协议

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTPSdguYkjLB4cZicPTyctbejnpLf9WibJjEER2IN7zCicmiaOHFIic3Hp9z2tpT6yuk4vv5ftufThP0fJM9rZVPZ5v6wkE6MU3grbM/640?wx_fmt=png&from=appmsg)

按我这样选择，继续下一步

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRS1MoNeZ4xVEJW9kbCj59HJyboDAibS2S53Ss3LIw96icMGtN5A3jicpqUPbVFKr6z1AQAlM1TWeQl76icUiawBg5rmvZB1kQuyXd8/640?wx_fmt=png&from=appmsg)

这里应该会让你选择安装路径，因为我安装过了所以直接下一步了，师傅们选择自己要安装的路径（不要有中文），然后下一步

最后点击安装即可

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT6YL7MnK6klcmtlbuE6n7mVQ8tc1V02hSCpYFURfdfjlspr6xycTBctqUm1XPH23VgFEVcYFyIrZSNXknvA4vy9qzAYAUXiaJA/640?wx_fmt=png&from=appmsg)

这些配置也都需要安装，安装过程不在详细说明。

```
1.Google Chrome 浏览器作用Chrome 需要以远程调试模式启动，为 MCP 服务器提供操作接口。通过 --remote-debugging-port 参数，AI 可以连接到你当前已登录的 Chrome 实例，直接操作页面、获取网络请求、执行 JS 等，无需重复登录。安装方式从 Chrome 官网下载最新版本并安装确认版本号：地址栏输入 chrome://version/ 查看Windows 调试模式启动命令：chrome.exe --remote-debugging-port=9222 --user-data-dir=c:	empchrome-debug--user-data-dir 指向一个临时目录，这样启动的 Chrome 与日常使用的 Chrome 是隔离的，不会影响日常浏览数据，同时可以保持登录状态2.Node.js作用Node.js 是一个 JavaScript 运行时环境。MCP 服务器（如 chrome-devtools-mcp）依赖 Node.js 来运行。版本要求 > v20.19，这是因为较新的前端工具（如 Vite 7）已不再支持已结束生命周期（EOL）的旧版本 Node.js安装方式前往 nodejs.org 下载 LTS 版本（长期支持版，推荐 v20.19+ 或 v22.12+）按安装向导完成安装（建议保持默认路径）安装完成后，在终端（cmd）验证版本node -v如果输出版本号（如 v20.19.2），说明安装成功3.npm作用npm（Node Package Manager）是 Node.js 自带的包管理工具，用于下载、安装和管理项目所需的 JavaScript 依赖包。需要通过 npm 来安装 MCP 相关组件（如 chrome-devtools-mcp）。安装方式npm 不需要单独安装——它随 Node.js 一同安装。安装完 Node.js 后，npm 会自动可用验证安装：npm -v如果输出版本号（如 10.5.1），说明安装成功。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSOqWcicKv2e2iaoJo0GH389lQK9hhPSPflicmFuHicyWiauduqibCZTqWk92urNr0hkLDdjPpPQicGBNM38zbIVsYPVJhlCpYpCQbxPY/640?wx_fmt=png&from=appmsg)

现在准备工作就绪

我们直接打开trae进行登录

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSzvp5Jt1lJ58ylOPJRBPjlx4I0WHZoGkvS4gdt0CygOs01ffS2PRHUzAePRsFNyL10wSg04PJ2EtmYPsdtTSgfgMRX9gE0uS4/640?wx_fmt=png&from=appmsg)

登录完成之后

这里就可以正常进行使用

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTXgQTl0LPoicWgXPOXvEc11aMojFYHbciama6MhwyfHEQ7Pvqf7TGdasdmyB2O17mgzr8sY9esgia7nyYweDRgvjdWIburLZFepQ/640?wx_fmt=png&from=appmsg)

来到插件市场安装一个google的mcp

windows的话ctrl+,打开设置，点击mcp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRZ0N9tGXIr34n6XeeXPJ1LS2kvoqCJxB7Oa5BSicgrKG0zu0v9gLrDDEcA1rk4mf6Nqff5iaeES0ddWWSzVXBDN4yjFhmd3XZGw/640?wx_fmt=png&from=appmsg)

搜索Chrome DevTools，之后点击安装即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu0PWMLWe6LRLhu4gjrByCx5Z0EcSWVicBxpicQJV0tFpCEc1BicfmHR3jqpzj1422k1Rg6K4PmCMLE779OU3nxSs1rZy6d0jLsw/640?wx_fmt=png&from=appmsg)

如果找不到Chrome DevTools，也可以手动配置mcp

点击添加 -> 手动配置

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRyicdic2uqf7icicgWRVkwicqEqrEUjVnEIxaUqtz5UrFgib5eia53e4jxMEBrqspsdiberZbplMSwqic5icWwb6TnLFDtuJV29fqUicibibBQ/640?wx_fmt=png&from=appmsg)

然后输入这一段内容就行

```
{  "mcpServers": {    "Chrome DevTools MCP": {      "command": "npx",      "args": [        "-y",        "chrome-devtools-mcp@latest"      ],      "env": {}    }  }}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTV70uGTaR0xmB7j4z0hZzCeyVmqgvCZAZ9iatcVHhiaKeCHRTEOa4c2Q6PGoIvCakqJiaYCJZEQXtUicricAJ8MicvsmrJGfibnLDqmQ/640?wx_fmt=png&from=appmsg)

这个时候我们已经有了Google的mcp

来到trae的builder控制这里选择这个 Builder with MCP

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSs9EYML5VbIEN1cNtQsctsNSRPlCdNeOKOOxuzRjApT4icb210JbFDYJPSHGomSicIkDEkic81MV2kvwm7T62cZEy7ibhCzH5q3po/640?wx_fmt=png&from=appmsg)

发出指令，进行测试

帮我通过google的mcp打开百度页面，输入 site:edu.cn,并且进行搜索

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQGmAmpHrceF7vh1mMyFqOTT6kI5Fk2gy6D8fiaHRtogJlKFopM0UA0aFEbnTJID2D3VZbaHSVHDVnf99mXbeWVgjnXxKPhTsxU/640?wx_fmt=png&from=appmsg)

完美，这个时候环境已经配置完成

我们回到js自动逆向这个问题

输入这个就可以

http://xxxx.edu.cn/,这个一个登录页面，帮我分析mm参数对应的加密逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSP6QxAN0ichQvpcARibia8LSwlicQSRUqGicADsKYmymDAaeN78BreBYEoIicn1PutsQJCGmvOQ2cNwOtYeOFrib7184pDic3xAR5zSYI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR0gEhDEkib33AGeoicomeZpMiaxibSOsGyiapCKJt3StLsyUkVPvKPgfebnBwWWH1wiad1lBgibc5b3V8zcm8kTrlibs1kUl2NM4icXicgE/640?wx_fmt=png&from=appmsg)

几秒钟之后他会给分析出来，

这个时候我们继续

帮我生成一个python加密脚本我用来验证

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRoib7ibZYLDwW2pfUFUKPWfXJyJcciaDoUhTtT4JL5iaS8mLb74T0ic2PA2ibcHMVL17x4SLibmu95fEsSdNcRbficlWh7TK9bBXyMOJc/640?wx_fmt=png&from=appmsg)

拿到脚本之后运行进行验证，可以看到他生成的脚本123456加密之后是这个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRpPe92HyUWryDUgELPGeJcvL7TO8at3zx5rW1ULLphHDha31XBuArib1w2CgNq6a7fzjvw...