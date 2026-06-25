---
title: Burp/Yakit平替？一个更适合新人用的抓包工具 + 插件扩展
url: https://mp.weixin.qq.com/s/ks3-CQnXZZgdlu9qP_Tmdg
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:00:23.020616
---

# Burp/Yakit平替？一个更适合新人用的抓包工具 + 插件扩展

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj55XEXZmnzmMLXQGI87AF0V9NbLqws3AwHfiaiaS3B6FpmloLia8Giaz1DFwKzEESqYD4CD7Evk1dEdpED3QEE3udicLeaic5tmBEcFR8/0?wx_fmt=jpeg)

# Burp/Yakit平替？一个更适合新人用的抓包工具 + 插件扩展

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

做渗透测试、抓包改包、流量分析的朋友，应该都对 Burp Suite 又爱又恨。功能强是真强，但资源占用、上手门槛、扩展灵活性，总让人想找个更顺手的平替。

最近，一款国产开源工具 **SwordfishSuite** 悄然上线。它以 Burp 为灵感，做轻量、高效、可扩展的 Web 安全测试平台，最新 v0.1.2 版本还重点优化了资源占用，日常测试更稳更丝滑。

今天就带大家快速上手，看看它到底香在哪。

**一、SwordfishSuite是什么？**

SwordfishSuite 是面向安全研究员、渗透测试工程师的**现代化 Web 安全测试平台**，核心定位：

* 轻量高效，不卡不崩
* 图形界面友好，上手快
* 插件化扩展，想加功能自己写
* 兼顾 Web 与 APP 流量分析

一句话：**日常抓包、重放、扫描、插件扩展，一套搞定**。

**二、核心功能，一次看懂**

### 1. 智能代理 + HTTPS 流量拦截

无缝拦截、查看、修改 HTTP/HTTPS 流量，支持多客户端接入。

第一次运行安装 CA 证书，就能正常解密 HTTPS，不用复杂配置。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kCkxT2rCp3TloeFBx2Xh6jvqPGgTmSFcZFFxJXDW50CIYK4AlH0ibj6c8kicWS3iajjOTDYFib7fjAkyxBOmck5Fqhh5zChXUhiakN0/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

### 2. 图形化 GUI，操作直观

不用记一堆命令，点一点就能：

```
开启/关闭代理查看请求/响应详情数据包重发发起负载扫描对新手非常友好
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kBCH4sQmXfdRhyialPLjIPicibkmefUEcMx94KViagiaGtV2yRef0RJhfeX1bu0QWmowSjzHXWVqiaDLZ9EOSsFvd6lica0hQaPa2NaWA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

### 3. 强大插件系统，Python 一键扩展

基于 Python 的插件生态，自带实用插件：

* JS 敏感信息提取：自动扒 JS 里各大云厂商 AK/SK 等密钥
* 规则自定义：字典规则写在 extract-string-list.json，想加就加自己写扫描器、分析脚本也很简单，高度定制化。

![图片](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kCGtg3T7FGCYbvhOjxqWCnJeuehCDnUDl3dKRFy1tocPkRlIqR0rQ4ILqBZ992KrhfYIRVnfTN3VYbIsqgCBXOZCpqKicxy30vM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

### 4. APP 流量分析（内测中）

支持对接云手机，直接在工具里查看、分析 APP 流量。目前暂未完全开放，但已经能看出作者对移动端安全测试的布局。

![图片](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kBN5squN3ajqxB8y514erWkrbtfvHiaETfKSFdAfSsjjiafic81plVAFOiaia23AOQ3r7icU0l7Mjek5pGiaC3RmJn37VTonficK0afQFg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

### 5. 流量转发与数据导出

支持原始流量、HAR 格式二次转发，方便对接其他工具、做自动化流程、复现测试场景。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kBRzm4mHk5djdwUJsPjDs9SIkqib31QeJNqlw1wia1lty90kaOXWPXCrAiccymz5DicuLdgfntuNSZRN9dj7hB7sxT3MvJMtgsIp3s/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kAnIpu3HXW36mOX8nVkmUUicBYmvhxXZoqftfV3HMbNFnNgCFjLhGc0S9ib3tPibOeuNmhC94qmN2Jk7jhluo7m2LEUQgYg7icqOXk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

**三、快速上手，5 分钟跑起来**

### 前置条件

* 想用插件：Python 3.10 或更高版本
* 依赖：pip install grpcio grpcio-tools protobuf numpy

### 安装启动

* 去 GitHub Releases 下载压缩包
* 解压进入目录
* 双击或运行 Swordfish.exe 即可打开 GUI
* 首次使用点「安装证书」，按提示导入受信任根证书
* 点开始，就能拦截、重放、扫描了。

**四、适合谁用？**

* 渗透测试工程师：日常抓包、改包、重放、批量扫描
* 安全研究员：分析 JS 密钥、APP 接口、协议行为
* 开发 / 运维：自测接口安全、排查敏感信息泄露
* 学生 / 入门者：图形界面友好，学习成本低

**五、小结**

SwordfishSuite 走的是**轻量、好用、可扩展**路线，没有过度堆砌功能，把 Web 安全测试最常用的代理、重放、扫描、插件做扎实，同时优化资源占用，长时间运行也不卡顿。

对厌倦了笨重工具、想要一套顺手国产测试平台的朋友来说，非常值得一试。

感兴趣可以去下载体验，也欢迎提交 Issue 或 PR，一起把这款国产安全工具做得更完善。

**六、下载**

**点击下方名片进入公众号**

**回复关键字【****260624****】获取**下载链接****

内容转自HACK分享吧，侵删

**更多福利**

2026年AI+网络安全专家班是今年最新更新的系统培训课程，欢迎大家咨询参加！

本培训旨在为对安全感兴趣的师傅们提供系统的安全学习路线，在短时间内习得AI+网络安全领域的关键技能，将网络安全核心技能一网打尽，实现AI环境下网络安全高端人才的培养。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAnPKNEglFy69HR9vFlRSicsR5SibFMswbkKtibCwUOtKHgXbjyoxia12j6JhpktMywVmDpQUqkoQKvdmg/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57Tl1oOKiaibib4umsIibAvgUtZyFeKYnOgkTwXGnIte0J1XA6VkH8yTeOPm2wHcwRzqdQ6NYDNeA3Jmf82IVG3xqgMBz4QEt7hdcI/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

完整版课程内容

请扫码备注：**【安全课程】**免费领取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj568J1dg5nlyfZghicYudMgPmng1QhQLJQwARGFiavOK45Bn7ko5bMn0rnG2w00icA4lp5iaeKOrXWNpFheOhM28fQv9DiabmbdOQnGg/640?wx_fmt=png&from=appmsg)

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