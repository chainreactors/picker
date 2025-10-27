---
title: Java反序列化回显学习（一）
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247508240&idx=1&sn=806d0081f3ab6bf5f898861c06f7d7f2&chksm=ce5d8371f92a0a678d3c2d7cfaf6aa55140bb629741bbd0364d0dca5d22eeea090a15942003c&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-03-07
fetch_date: 2025-10-04T08:49:20.370954
---

# Java反序列化回显学习（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TREVoIVo9czPlfklQ6icxD3oqgibEyehgrmbtE7iaCCNYHyXrDtJC9u1vHg/0?wx_fmt=jpeg)

# Java反序列化回显学习（一）

原创

zhangy1da

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

# 前言

在测试某反序列化漏洞，可以通过URLDNS链确定漏洞是否存在但在利用时遇到了困难，相关利用链可以执行系统命令却无法得到回显。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRfKQXDHNBIhs8CdjeMEzENoYCTJPdzwRjgGYia3SWYuxCYF7xDAJTFkQ/640?wx_fmt=png "null")

因此需要在此基础修改利用链达到命令回显得目的，下边记录的即是此次修改的过程。

# Java反序列化回显方法

根据搜索到的资料给出的常见回显方法有以下几种：1、报错回显：要求服务器将报错信息打印到页面。2、写文件：把执行结果写入静态文件置于web目录下再读取结果。3、DNSLOG回显：通过DNSLOG将执行结果带出（未实现）。4、中间件回显：获取response对象，结果写入response对象中带出。5、.....

## 报错回显

此法要求服务器将报错信息打印出来，修改要反序列化执行的Java代码将结果写入异常再抛出即可实现。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRyAq0xHXXQbGVmuvYApwmcnjowFP3XAq7GGcjsl5xvlQ3GhuiaAiakzdw/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRKVtlFQhmLdy3o8SmOaAlIYBxhDJT1sXRFMTbaPTS9lut7znmD7SI5A/640?wx_fmt=png "null")

## 写文件回显

同样修改yso中Gadgets要执行的java代码即可实现，通过将执行结果写入web目录下的静态文件再读取来实现。此法的缺点是当目标不存在可访问静态web目录便无法使用了且要获取web目录的绝对路径，更适用于已知开发框架的反序列化漏洞利用。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRaoiaicicOichPgLQ4aahjxaXjz0jSZctiafClJ5hgicW9oQzGhQXd5b5w5kA/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRPtUPqg2LmHoTfjqxpbVxJUOD4EHxQZEOIlJvtj4kcc2dR22v14OGmw/640?wx_fmt=png "null")

## DNSLOG

一般作为检测反序列化漏洞是否存在用，贴出URLDNS Gadget的验证过程。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRDrD28TWRwFse1bDcjcialy9TkUNtPgomMzt1BibVrlDEsafY07FQk2uw/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRAHkoNiblP8LK6MaD8HE8sNz9yec12ggWia6lMYsdKKU9MWiaweq6e9XBg/640?wx_fmt=png "null")

## 中间件回显

中间件回显是目前所有反序列化工具中最为通用的方法，相比于上述的方法中间件回显有不需目标出网、没有目录限制等优势。中间件回显的原理简单来说是在运行的中间件中获取request&response对象，通过request对象获取执行参数等后将执行结果写入response对象带出完成回显。已知目标中间件为tomcat，参考feihong师傅公开的tomcat全版本回显测试代码来修改yso代码实现利用。Tomcat回显代码：

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TROa6IwQ3kuhXvgu0pm6ZY0aSaBoGNa0FKRSr9t5m8cf7wSacmZMnloQ/640?wx_fmt=png "Tomcat回显代码")

修改yso payload代码：

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRxxEaLpqaIWWWswScjQNQtQQicYq7icicWMSl46icIQMUhu750eELGWMEAg/640?wx_fmt=png "修改yso payload代码")

修改yso Gadgets代码：

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRV0wUBlgcHUaE3hyOglWtGLSkYwBK843Tz3VS8Ufgd76CAzNCDwGnJQ/640?wx_fmt=png "修改yso Gadgets代码")

实现回显：

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVBRPhuoPhvkoPsPg51y4TRbks2cEhWrJvqBrx2pIOUUmymcFHoKSmjU2gSnib2JZ2hzx0XlIXIvvQ/640?wx_fmt=png "实现回显")

# 总结

由于本菜鸡学习Java的路程不是很系统，在很多地方卡壳严重，还好最终实现了相关exp的编写。最后，感谢文中所用代码和知识的作者师傅们。

# 参考

https://www.cnblogs.com/nice0e3/p/14945707.html

往期推荐

[敏感信息泄露](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500219&idx=1&sn=8da48a9a049bab2f9215ad373868a1a5&chksm=ce5de3daf92a6acc7c2a58329c913062e9c34a9615ce742b761b2775916781abb50159a7d2d7&scene=21#wechat_redirect)

[潮影在线免杀平台上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499902&idx=1&sn=59cba8d980b4ecb0deefff99edaabd4d&chksm=ce5de21ff92a6b09a8972a0144557b0099e443aa8e018b17151c816fc7f08f3615ecb22617fc&scene=21#wechat_redirect)

[自动化渗透测试工具开发实践](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498466&idx=1&sn=085c15679436dedb06a179ca8d47951a&chksm=ce5dd883f92a5195ef74ac517741f6d3da0da40b5501d72016e52cb70344904bb85b8aef65ba&scene=21#wechat_redirect)

[【红蓝对抗】利用CS进行内网横向](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247492640&idx=1&sn=43b1991dc5628eab322923083fde8d70&chksm=ce5dc641f92a4f57ffb18e2977644b1f977fcc5e0eccdf10956d3ae4ce70dc95024500631e89&scene=21#wechat_redirect)

[一个Go版(更强大)的TideFinger](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498344&idx=1&sn=3679330363ff6890166b09f6a502f769&chksm=ce5dd809f92a511f6066fcbb12fb5c1dc8c2642e4e2690dad64d76cc6f9247eae356d16f5810&scene=21#wechat_redirect)

[SRC资产导航监测平台Tsrc上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499823&idx=1&sn=065ffeae6bd02fff922cfb12c5a0f4df&chksm=ce5de24ef92a6b58f709260b691e6b36e4a53aac00d3022946302b8e638696ed55c70e13e16f&scene=21#wechat_redirect)

[新潮信息-Tide安全团队2022年度总结](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247506056&idx=1&sn=ad6dd23f58f5fd8ce899a1e292f5b685&chksm=ce5dfae9f92a73ff4f14c812436cb5bfecb29db04eada11c409e946d5338c82a92bcaa425736&scene=21#wechat_redirect)

[记一次实战攻防(打点-Edr-内网-横向-Vcenter)](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498965&idx=1&sn=655548831da6808a020ad07294a92e60&chksm=ce5ddeb4f92a57a283d5692c246e54655319ab0d09f6403e354300a2777cda6ae4c787631ab3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/rTicZ9Hibb6RWbGNtVfIZbm2rmGO4hQDzQUrLN62vEGlA4fPmib5utUAp9gbQicb6FC82RjsVI5vx7wEc9yAAiaFEoQ/640?wx_fmt=gif)

E

N

D

**知识星球产品及服务**

**团队内部平台**：潮汐在线指纹识别平台 | 潮听漏洞情报平台 | 潮巡资产管理与威胁监测平台 | 潮汐网络空间资产测绘 | 潮声漏洞检测平台 | 在线免杀平台 | CTF练习平台 | 物联网固件检测平台 | SRC资产监控平台  | ......

**星球分享方向**:Web安全 | 红蓝对抗 | 移动安全 | 应急响应 | 工控安全 | 物联网安全 | 密码学 | 人工智能 | ctf 等方面的沟通及分享

**星球知识wiki**：红蓝对抗 | 漏洞武器库 | 远控免杀 | 移动安全 | 物联网安全 | 代码审计 | CTF | 工控安全 | 应急响应 | 人工智能 | 密码学 | CobaltStrike | 安全测试用例 | ......

**星球网盘资料**：安全法律法规 | 安全认证资料 | 代码审计 | 渗透安全工具 | 工控安全工具 | 移动安全工具 | 物联网安全 | 其它安全文库合辑  | ......

扫码加入一起学习吧~

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn4bib2lic6dng5krLaNOdrDVLcLylWP1Op3Kibz2n6pOZjibrFd1xATEoZ6dXhaicMLgRQSicNQwGmDwicvA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUGxmZ0l89buUNbyVALKxic2nM7hnDCkAKIrjKhdcDfVkGq3PxNzgs7m55BBMwmicc0AvFpYcrd6J6Q/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

Tide安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

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