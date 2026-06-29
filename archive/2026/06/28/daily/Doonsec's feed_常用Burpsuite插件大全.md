---
title: 常用Burpsuite插件大全
url: https://mp.weixin.qq.com/s/la70h7QREK8xT0MGT4KX_A
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:33:22.673534
---

# 常用Burpsuite插件大全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj567aUiaLZeZK0Wx6qbhhgVKo2O9JucKDFVOn5z1gIYiaW3oM88DeHszxIibJnU9am05Lic6W462S4fx377S3PNv9CdeOXJRO7x4Ar0/0?wx_fmt=jpeg)

# 常用Burpsuite插件大全

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/56vojF9ZLWFoCVewibuUxAiaF5ISPfO3TCJ42dl8PwP1wa7AKLbjicIxyOISQkia8XLSBPnL2EQhXpqouhgxNd3KHJxbka7OsuXl0SmKwcWdTlU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

推荐默认关闭，使用时开启。

漏洞探测

Autorize：用来测试**垂直越权**和**未授权**。
项目地址：https://github.com/Quitten/Autorize

TsojanScan：这是一款基于 Jython 开发的 Burp Suite 自动权限校验检测插件，旨在简化应用安全人员的工作，助力其开展自动化权限测试。

项目地址：https://github.com/Quitten/Autorize

APIKit:APIKit 可以主动/被动扫描发现应用泄露的 API 文档，并将 API 文档解析成 BurpSuite 中的数据包用于 API 安全测试。

项目地址：https://github.com/API-Security/APIKit

Auto-SSRF：Auto-SSRF 是一款基于 BurpSuite MontoyaApi 的自动 SSRF 漏洞探测插件, 捕获 BurpSuite 流经 Passive Audit、Proxy、Repeater 的流量进行 SSRF 漏洞探测分析。

项目地址：https://github.com/banchengkemeng/Auto-SSRF

SQL 注入

DouSql：DouSql 是基于 Xia Sql 二次开发的 Burp Suite SQL 注入辅助检测插件。

项目地址：https://github.com/darkfiv/DouSql

SQL-Injection-Scout：测试 SQL 注入的。我挺喜欢用这个的。还可以配置额外的 Fuzzing 参数。

项目地址：https://github.com/JaveleyQAQ/SQL-Injection-Scout

文件上传

Upload\_Auto\_Fuzz：专为**文件上传**漏洞检测设计，提供自动化 Fuzz 测试，共 500+条 payload。在 intruder 模块下使用。

项目地址：https://github.com/T3nk0/Upload\_Auto\_Fuzz

权限绕过

BypassPro：对权限绕过自动化 bypass 的 burpsuite 插件。遇到 403、提示需登录和无权限的时候，拿出来跑一下。

项目地址：https://github.com/0x727/BypassPro

信息收集

HAE：通过关键词和正则匹配，分析 HTTP 请求与响应报文（包含 WebSocket），辅助我们快速锁定报文中的敏感信息。匹配信息的过程中，不可避免的产生误报，HAE 默认匹配的信息也许不是我们想要关注的，可以根据需要添加或删除。

项目地址：https://github.com/gh0stkey/HaE

CaA：CaA 主要用于分析、拆解 HTTP 协议报文，提取 HTTP 协议报文中的参数、路径、文件、参数值等信息，并统计出现的频次，帮助用户构建出具有实战应用价值的 Fuzzing 字典。除此之外 CaA 可以生成各类 HTTP 请求提供给 BurpSuite Intruder 用于 Fuzzing 工作。通过收集 HTTP 协议报文中的信息，辅助我们对网站进行 Fuzzing，发现隐藏的漏洞面。

项目地址：https://github.com/gh0stkey/CaA

BurpFingerPrint：BurpSuite 插件集成 Ehole 指纹库并进行常见 OA 弱口令爆破插件。我们直接使用`Ehole`工具对网站进行指纹匹配时，通常会遇到的一个问题，那就是这类工具通常只会访问网站的首页和网站的图标，如果特征是隐藏在网站的子路径下，或者藏在 js 文件中，那就可能被工具放过。开启该插件时，能随时匹配 JS、请求响应中的关键词，尽可能小的减少 CMS 特征匹配的失误。

项目地址：https://github.com/shuanx/BurpFingerPrint

BurpAPIFinder：攻防演练过程中，我们通常会用浏览器访问一些资产，但很多未授权/敏感信息/越权隐匿在已访问接口过 html、JS 文件等，通过该 BurpAPIFinder 插件我们可以：
1、发现通过某接口可以进行未授权/越权获取到所有的账号密码、私钥、凭证
2、发现通过某接口可以枚举用户信息、密码修改、用户创建接口
3、发现登陆后台网址
4、发现在 html、JS 中泄漏账号密码或者云主机的 Access Key 和 SecretKey
5、自动提取 js、html 中路径进行访问，也支持自定义父路径访问

项目地址：https://github.com/shuanx/BurpAPIFinder

加解密

autoDecoder：遇到网站/APP 的 HTTP 请求和响应报文被加密的情况时使用。使用案例：https://xz.aliyun.com/news/18018

项目地址：https://github.com/f0ng/autoDecoder

Galaxy：可以自定义 Python 脚本，并给出了常见的加密方式的 Python 脚本。

项目地址：https://github.com/outlaws-bai/Galaxy

生成测试信息

xia\_Liao：一般用来生成测试数据。

项目地址：https://github.com/smxiazi/xia\_Liao

HackBar：集成了常见漏洞的常用 payload，在 repeater 模块，右键选择插入即可。

项目地址：https://github.com/d3vilbug/HackBar

功能增强

MaR：一款网络安全（漏洞挖掘）领域下的辅助型项目，主要用于对 HTTP 协议报文进行精准匹配和智能替换。它可以根据用户定义的规则，在满足特定条件时自动修改 HTTP 请求或响应内容，帮助安全研究人员在渗透测试过程中实现自动化的数据篡改。

项目地址：https://github.com/gh0stkey/MaR

BurpHttpHelper：BurpHttpHelper 是一款 Burpsuite 插件，主要用于简化和解决 Burpsuite 对 Http 的一些操作。

目前实现: HttpHeader 增删改 HttpCookie 增删改 HttpBody 替换 随机 UserAgent RepeaterResponse 自动解码 丢弃特定数据包。

项目地址：https://github.com/MaskCyberSecurityTeam/BurpHttpHelper

MCP

* 1、Burpsuite 也有 mcp [https://mp.weixin.qq.com/s/pDe1F1Z-n1aziVDnovUa5g](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247489677&idx=1&sn=882fcc024d13aa3b9d8b45a347255bc4&scene=21#wechat_redirect)
* 2、 AI + Skill + Burp MCP 协同实战：从匿名入口到记录读取的一次移动端代码审计闭环
  https://forum.butian.net/ai\_security/95

过特征检测

burp-awesome-tls：遇到检测 Burpsuite 指纹、或者会收集浏览器指纹的网站时开启，避免被某些 WAF 记住特征。

项目地址：https://github.com/sleeyax/burp-awesome-tls

提示词绕过

PromptInjectionScanner：一款专业的 AI 应用 Prompt 注入漏洞检测工具，支持规则检测、AI 智能分析和多轮递归会话攻击。随着 LLM（大语言模型）的兴起，企业也陆续在自家的产品里加入相关的大模型，算是一个新兴的测试点。

项目地址：https://github.com/darkfiv/PromptInjectionScanner

内容转自维度攻防，侵删

![](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj57BfHc3nejvERBYZLD0jvKknuTIu6gSmfMXCzNAXP00kkDic7HViaS7twhtlnib3gaBoicFM5L4XLTTH0DwBwBWgCR3O3V9y94HYkk/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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