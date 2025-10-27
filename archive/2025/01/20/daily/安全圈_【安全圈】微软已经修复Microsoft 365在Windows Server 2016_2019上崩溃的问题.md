---
title: 【安全圈】微软已经修复Microsoft 365在Windows Server 2016/2019上崩溃的问题
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=2&sn=e94b5cb3a624cdca3e6452bf7c79d7a8&chksm=f36e7ad8c419f3cef73c242196a8499de4c2c79ec90ca98bd662ee5575f6ac22d4041dcd89d4&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-20
fetch_date: 2025-10-06T20:09:21.345292
---

# 【安全圈】微软已经修复Microsoft 365在Windows Server 2016/2019上崩溃的问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaPe1B66JiaecZicwXgaw8TlGJafZ5cRYtDAneOwLDxicT0DTgJ8e6hd0vqIk32KoIjVJ7tkMhpAW6yQ/0?wx_fmt=jpeg)

# 【安全圈】微软已经修复Microsoft 365在Windows Server 2016/2019上崩溃的问题

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Windows

据微软发布的最新支持文档，微软已经成功解决 Microsoft 365 系列应用和经典版 Outlook 邮箱在 Windows Server 2016/2019 服务器系统上崩溃的问题。

经过开发团队的排查微软发现导致此次问题的根本原因是近期发布的 Microsoft 365 更新集成 React Native 框架以支持某些新功能，这次变更导致某些兼容性问题从而引发了崩溃。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaPe1B66JiaecZicwXgaw8TlGCiboxk93vw6XbZZ5qOMAwQLBM2S3wVCSDNtCRQ4SqlCQpXYfN2ZoQgw/640?wx_fmt=png&from=appmsg)

受影响的主要是经典版 Outlook 邮箱和 Microsoft 365 的 Build 2412.18324.20168 版，该问题不影响非 Microsoft 365 订阅版，例如 Office 2024 LTSC 这类买断版本就不存在问题。

修复方案上用户只需要更新即可，版本号没有变化但微软已经在后端服务器上部署了补丁因此在 Microsoft 365 自动接收到补丁后问题就可以解决。

如果无法接收在线更新则可以考虑通过命令行方式执行降级，将 Microsoft 365 降级到 Build 2412.18227.20162 版作为临时解决方案，降级后即可正常使用。

**下面是降级方法：在管理员权限的命令提示符中分别执行如下命令**

1. cd % programfiles%\Common Files\Microsoft Shared\ClickToRun
2. officec2rclient.exe/update user updatetoversion=16.0.18227.2015

执行完毕后 Microsoft 365 就已经完成降级，但为了防止再次自动升级到最新版，请转到任意 Office 组件、文件、Office 账户、更新选项、禁用更新以暂时关闭自动更新功能。

不过在 Windows Server 服务器系统上使用 Microsoft 365 的用户相对来说不算多所以这次问题并未造成太大的影响，通常只有部分企业会因为某些场景会在服务器系统上安装 Office 处理某些事情。

来源：https://www.landiannews.com/archives/107614.html

***END***

阅读推荐

[【安全圈】高危！rsync被爆出多个安全漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=1&sn=7e41cdf5b76e20186089903f7171a588&scene=21#wechat_redirect)

[【安全圈】国家互联网应急中心通报两起美方对我国网络攻击事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=2&sn=1eeea145994ab308cf3f78f1ca987a19&scene=21#wechat_redirect)

[【安全圈】网络安全态势研判分析报告 （2024年12月）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=3&sn=86d02f407c0e151d308f83282274bf31&scene=21#wechat_redirect)

[【安全圈】支付宝P0级重大事故：整整5分钟所有订单打8折，官方回应：不向用户追款](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067425&idx=1&sn=c8e7e9e9cc66acce28dbc15174a86f30&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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