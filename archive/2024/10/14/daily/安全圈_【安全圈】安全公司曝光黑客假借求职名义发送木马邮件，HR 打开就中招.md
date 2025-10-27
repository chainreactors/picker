---
title: 【安全圈】安全公司曝光黑客假借求职名义发送木马邮件，HR 打开就中招
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=4&sn=0401fbd7c8c87dba65ea5338166a7d73&chksm=f36e61e6c419e8f02fca8fa6dbad1acf009cdeab95878710b0d2a1a4f3adda6641690f978fe8&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-14
fetch_date: 2025-10-06T18:47:46.338354
---

# 【安全圈】安全公司曝光黑客假借求职名义发送木马邮件，HR 打开就中招

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwpMcbNG1CnfwDa89TbsZB4l3tkNAY46WcYkgys8le4WQCib9k7Hzpk9A/0?wx_fmt=jpeg)

# 【安全圈】安全公司曝光黑客假借求职名义发送木马邮件，HR 打开就中招

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

木马

安全公司 trendmicro 本周发布报告称有黑客组织 FIN6 专门针对招聘销售工程师的公司发动攻击，相关黑客将附带有恶意木马 More\_eggs 运行文件的链接打包入简历邮件中，只要 HR 点击邮件里的链接下载打开文件便会中招。

据悉，这些黑客使用的简历通常以 "John Cboins" 署名，相关邮件中没有包含附件，但一旦 HR 点击邮件中的链接便会跳转到一个虚假的招聘平台，特别的是，下载黑客所谓 " 作品集 " 需要通过 Captcha 验证，研究人员推测这可能是为了赢得 HR 的信任。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwD5omE3x65h5waBCOc788Wc4OBAUNxbo9aFd5ibU6W9xRcFSenopDfng/640?wx_fmt=jpeg&from=appmsg)

▲ 图源 trendmicro

从报告中获悉，黑客提供的作品集中主要包含 John Cboins.lnk 和 6.jpeg，其中 "John Cboins.lnk" 便是木马，一旦 HR 运行这一文件，木马便会在 Windows 系统文件夹之外生成 ieuinit.inf 文件，其中包含设备机器码等信息，同时还会通过 regsvr32.exe 加载恶意动态文件 38804.dll，进而自动部署 More\_eggs 木马，便于黑客远程运行恶意代码。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhop44vsRWpfyDxWRNAbcEfEMzfYENvLoCQ0EFlJfILOazyNIy5EZkoPxN5MlnssicYYg0ly9he5Qg/640?wx_fmt=png)[【安全圈】日本电子产品制造商卡西欧遭到勒索软件攻击 泄露大量公司内部敏感数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065140&idx=1&sn=d05df59d5c793cc66f912668c5cedc8b&chksm=f36e6134c419e8228918442ea8aaa5116ff26c0fcdedf36649a4675a2c9e17992571fd217158&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhop44vsRWpfyDxWRNAbcEf406wQmF5lOfN3xLG7s0CzTpEG3xlUa3HgodsQ5JD7EIicgJ5IF8eIww/640?wx_fmt=jpeg)[【安全圈】泄露3.34亿客户信息，万豪决定支付3.6亿元和解](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065140&idx=2&sn=de96b8a15e19764dd3f4bc37fc99f746&chksm=f36e6134c419e82222bb9ed67e6786eb5cdea12c182524e7d7f612f4ba092b3c290f3ef7a494&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhop44vsRWpfyDxWRNAbcEfOhkvHEumLeEJauY41JbUPNmGZCCWCCtLSI2lDvWGy6YRTBeNzdV9ug/640?wx_fmt=jpeg)[【安全圈】因泄露数亿人数据，美国国家公共数据公司申请破产](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065140&idx=3&sn=9906b8098e4404360fec374bae030d94&chksm=f36e6134c419e822f1e3cd89be31f7e366e3325b20c9d674369d4061ad96ae78fc5696deb5c1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhop44vsRWpfyDxWRNAbcEfvDnlicK8FMDL0WjdhN6UNNvJCt8VfIk06drjEYt88A4icboFJtcU4Cuw/640?wx_fmt=jpeg)[【安全圈】GitLab 曝出严重漏洞，可能导致任意 CI/CD 管道执行](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065140&idx=4&sn=1c9477d3d6b96c81067c89ebb34124e3&chksm=f36e6134c419e822acded849ded66ac9d1a57275cb8f248e7f8b2f0fb19ffd374a1161af7a7e&scene=21#wechat_redirect)

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