---
title: 抓包 + AI 逆向神器来了！全平台通吃，自动解析协议与加密
url: https://mp.weixin.qq.com/s/CA7DKwWTLeHZnTG0zsgJ_g
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:22:51.712894
---

# 抓包 + AI 逆向神器来了！全平台通吃，自动解析协议与加密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwRSyUHicyDwZhlxheoL6gaxPZz4cxT9Vbjciam6gGmwfiaIYFVlkUftXdRDiap4kiapzZYQ9x0q1t9ibkPoQGk4Ge6lIBic95qYD0slw4/0?wx_fmt=jpeg)

# 抓包 + AI 逆向神器来了！全平台通吃，自动解析协议与加密

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近在开源圈里，一款叫**Anything Analyzer**的工具火得很快，上线没几天就收获了上千 Star。很多做爬虫、逆向、接口调试、安全测试的朋友都在用，今天就给大家好好介绍一下。

简单说，它不是一个普通的抓包工具，而是一套**全场景流量捕获 + AI 自动分析**的一体化工具。

平时我们抓包，可能要开浏览器 DevTools、开 Charles、开 Fiddler，手机还要单独配代理，抓完几百条请求还得自己一条条看，头都大了。

Anything Analyzer 直接把这些事全部整合：**网页、桌面软件、终端命令、代码脚本、手机 App、IoT 设备**，只要走 HTTP/HTTPS/WebSocket，它都能抓，而且抓到之后直接丢给 AI 自动分析。

**场景抓包：哪里有流量，就能抓到哪**

它支持几乎所有你能想到的场景，而且所有流量最后都汇入同一个会话，AI 一次性分析：

* 网页：内置 Chrome 浏览器，直接打开就能抓，适合网站 API、登录流程、前端加密。
* 桌面应用：开系统代理，Electron 应用、客户端软件、Postman 全都能抓。
* 终端命令：curl、wget、httpie 加个代理就能捕获。
* 代码脚本：Python、Node.js 里配置代理，请求一目了然。
* 手机/平板：连同一 Wi‑Fi，设置 HTTP 代理，App、小程序、H5 全拿下。
* IoT 设备：通过网关代理，抓智能家居、嵌入式设备的通信。

不用来回切换工具，一个界面全部搞定。

![](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwS5nF3jEGUkPogtZcicD6ltUHWrpouTuGlBTRic9ZjZFC4rOQgm3APA2BNjlgdbUGutEP9PTuOW7xNpIUY0gK6KAwwXfETvy736A/640?wx_fmt=png&from=appmsg)

**AI 智能分析：真正帮你 “看懂” 协议**

这是它最核心、最香的功能。抓完包，点一下分析，AI 直接帮你干活：

两阶段智能分析先

自动过滤掉图片、样式、静态资源这些没用的请求，再对关键接口深度分析，省掉大量人工筛选。

5 种分析模式

* 自动识别
* API 逆向
* 安全审计
* 性能分析
* JS 加密逆向

JS 加密直接扒

自动 Hook 注入，拦截 fetch、XHR、原生 crypto、CryptoJS、国密 SM2/SM3/SM4 等加密调用，还能从 JS 里把加密代码片段提取出来，AES、RSA、国密都支持。

一键出报告AI

自动生成：

* 接口文档
* 鉴权流程
* 协议逻辑
* 加密算法还原
* 支持流式输出，还能继续追问细节

**MCP 生态集成：AI Agent 也能用它**

现在很多人用 Cursor、Claude Desktop 这类 AI 编辑器，Anything Analyzer 直接内置 MCP Server，把抓包能力开放成工具，AI 可以直接调用它：

* 新建会话
* 开始 / 停止抓包
* 查询请求
* 执行 AI 分析
* 多轮对话

相当于给你的 AI 助手装上了 “网络透视眼”。

**谁适合用？**

* 做API 逆向、接口分析的开发
* 搞App 抓包、协议还原的工程师
* 做前端加密逆向、JS 算法分析的同学
* 负责安全审计、漏洞测试的安全人员
* 经常调试微服务、CLI 工具的后端开发

**下载地址**

**点击下方名片进入公众号**

**回复关键字【****26****0427****】获取**下载链接****

排版来自：Hack分享吧

---

**下面是一则内部学习圈广告😜**

**别着急退，看完的师傅们有福了/doge**

欢迎师傅们加入内部网络安全学习圈子。圈子提供三大板块的内容：

**1**

**网络安全0→1学习路径**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1. 完整的「30+周安全学习任务路线图」公开，每周任务明确，清晰的学习重点和目标，从入门到进阶，由浅入深，循序渐进；
2. 学习内容涵盖：

* 常见的Web漏洞原理与利用
* 业务逻辑漏洞挖掘
* SRC实战技巧
* WAF绕过、代码审计、免杀钓鱼
* 内网渗透

  （Linux&Windows）提权与权限维持
* 隧道代理、域渗透、云安全、AI安全

3. 每周发布学习任务+参考资料+建议，学员可自主学习+实战练习；

**2**

**SRC漏洞专项挖掘**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

1. SRC漏洞知识库持续更新；
2. SRC挖掘技巧、分析方法、视频教程打包；
3. 分享优质挖矿案例，降低上手门槛，教你赚赏金。

**3**

**常态化内容更新**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

日常分享优质学习资源与攻防渗透技巧，包括但不限于：

1. 红队/蓝队安全攻防、免杀、钓鱼技巧、攻防渗透tips；
2. 学习路线推荐，教程、方法、技巧tips打包分享，实战视频、工具、手册一应俱全；
3. 根据网络安全初中级学习者水平，精选最有用的内容，不让你在信息洪流中迷路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYnqBadHPfYribO0Eh7AO6sZtibP7icnEL1CIv2ibPnlUibbBzpK1lImaQsiawxpEKD4wOE3B9tBMll0HBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=81)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzD6B7ialvhZB0XJtGrrSiawmjIhv4ZRW4gTvdhQ1MkSTNvv530EOqSfKBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDQL6MIsF3Yqiczbczx67Z76BjgaXGGn8anlibtj82icib29ZyuuP3N7s9gw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

![Image](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwRoUNibnfBZmLRfGTjQRxfgTe2JXSIH8MJvialwFsIEpLL8AJPSuibZw8xf5c11KQMT7WUYetlN8lGnSmVKOzCkoRxpVGgWxFvibPc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwRAZSibC7tgUY1EVHBwNqibSthe0UBiavQfeOsdRibv8AKOibibsULnWIK40qvdzJjxkZrvFDE8xpuGW8ibgNoKf54ITZzibKJ5rwxbnEA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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