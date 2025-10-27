---
title: 对某bc站点的一次渗透
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495451&idx=1&sn=d6ac8648b6c2329dc5e8b8acadc9149e&chksm=e8a5e578dfd26c6e0f6486bd673ab3b3b85293db073c16eb07562f94f0417b3f016c316bb95f&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-04
fetch_date: 2025-10-06T18:04:03.723110
---

# 对某bc站点的一次渗透

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4CBZermKTpS6SqTopeRjYL1aUdgiaJ9UicR6V8qjGSl9Wuft0wmM2qCnMn3t1CE3LapOBYx0KFXWXg/0?wx_fmt=jpeg)

# 对某bc站点的一次渗透

2654470642

迪哥讲事

很多人问我你日站是用手工还是工具扫？我觉得两者同时进行效率会高些，所谓双管齐下，无站不破，当然还得看人品。

前段时间经常日有颜色的站，懂得都懂，emmm哈哈哈，但都是套路，跟bc又密不可分。

于是就按着套路顺利打开下面这个站：

![](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLgRxALMz2mj0xSicBl2CY84qTx4tFRYYzGVoJ7pP8IFPGabibvoJOrJ9A/640?wx_fmt=jpeg&from=appmsg)

刚好正是中午的时候，准备恰饭去，先将这个站丢到某W某S里面，如果有东西就直接捡现成的，于是：

(ps:不得不承认我长得帅！)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLjkxxzhHlt1iaGNtnZ9FeeVLFR2BkMfBlomDOCrSDZBzhJxbqa0TRfibQ/640?wx_fmt=png&from=appmsg)

懂的都懂

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLUMQfEibL4r4OAxDBnZJgIniaUADXibLNo4CgXDpCmVgnW3pibx2IwJvSsA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLAFVFVX6ZA7CqNzAL1pfa12LnteeNbMy5lJibpQM898hxTkIOcvZILibw/640?wx_fmt=png&from=appmsg)

猜测估计是xp\_cmdshell禁用或者删除

当前权限又是dba，而且支持堆叠可以执行update ，insert，等

于是就准备开启xp\_cmdshell

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLOxFCS79kZoUE5bOA2BBiasfOfpZqsF9GAxLJYyM1OofXrkWWBAf4daQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLMHoZcZapf6ECYXLCKpg0uyZp6icUQeeImRKPT1IqogAOSmibCIKK0IRQ/640?wx_fmt=png&from=appmsg)

再次osshell看xp\_cmdshell是否开启成功。然儿….

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLcoxzkBPNjHbN8VNlBq9veDtRZcEUKGxF4ib3ey8F4HuuS2wXKyZjNcg/640?wx_fmt=png&from=appmsg)

不甘心，于是来到burp，如果xp\_cmdshell启用返回时间应该是>=5,然儿只有1秒多钟，

证明没有开启成功。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLicuLhv0eY4SvoCHrAgP8mcjRALibic4ocCjuhvL41p9gKSC5nhNswAMow/640?wx_fmt=png&from=appmsg)

于是，利用burp再次开启xp\_cmdshell,然儿好像还是不得行

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLphNUvA2OKDkicOicW0WibWWIibN7UMkhV1jeTj5AnqORFglc3E0iaqT5nNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLcGmvra8uiaYPF9EOkEJsDCPv3S2wD4c14ExCWYvwgt34aFiapu2Tg50A/640?wx_fmt=png&from=appmsg)Xp\_cmdshell哪里=0呢看看语句是不是有毛病

看返回时间是没毛病的，在这里就纳闷了….

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLPsXe3QFd485BQ2B9emkVJg6nMqiccn824icfZvNgEFTlUrf3Egc6Bj0Q/640?wx_fmt=png&from=appmsg)

在此期间尝试了很多 ，包括沙箱等等burp跟sqlmap都尝试过，

参考文章：https://blog.csdn.net/sircoding/article/details/78681016 63

后面还考虑过了站库分离的情况，burp构造发包，发现不是。

想到写shell

必须满足：

1.网站绝对路径

2.目录写权限

3.数据库是Dba

但没有站点绝对路径，那岂不是要凉凉。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLAgrm2xnkrKGEabPaYVpehPxvFPzL8VVBa8j1DHhGNjFpeSYLnEQ9wQ/640?wx_fmt=png&from=appmsg)

鼓捣了好一会儿，找到该站点真实ip，从旁站入手了，万一·····，一般bc旁站一般也是bc

只能抱着试一试心态去，果不其然，也是bc，但感觉模板是一样的，同样的注入点，再次用sqlmap来梭哈，奇迹出现了哇哈哈哈：（ps：之前的注入点也尝试过union，没幼结果）：

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLQyjRiaMHEHBKIoGwxWCvlQkmqv2ZeQzg5hRt5Ef0IACiaVaNoApNDmAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLuho2GHUht2hu2QzfCbsHoJpjialTicibPhfWhEyBxVR6XJyjmXIRxMo0w/640?wx_fmt=png&from=appmsg)

终于能执行命令了

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLMXG5SZVgJbMFnfQyMhoRayrs2Kd66h4oSf6ibmxK831TxL72eWn7IKA/640?wx_fmt=png&from=appmsg)

接下来就是cs上线，提权，不是特殊目标，不上桌面的黑客不是好黑客

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYL3R2XqNBKdY2icicz7Nib9C4aOWykibGG6kZk0ZicDYhUibFMxaeny3rLeYNg/640?wx_fmt=png&from=appmsg)

Sqlserver被降权，利用ms16-032提权，或者其他权限提升机器未安装的补丁进行提权

System

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYL0oBfBOdKYz4HESy7Q1UDd1l5o2N3iaTxXyWlQMXtu3f7RKpcJov134w/640?wx_fmt=png&from=appmsg)

利用mimikatz dump账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLtdbRA8A8m3J9I8XUY5jHibkicXSRYwVPk7GZ8MRKDPTgrQ2muvMZTMpA/640?wx_fmt=png&from=appmsg)

没有明文，可以利用mimikatz传递ntml，感觉不得行，成功率低。

命令：

```
sekurlsa::pth /user:Administrator /domain:WORKGROUP /ntlm:206ca710d5b82f1c988b301808d1016e/run:powershell.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLBDicIlMJnW3kziaktzR8U8MIcdt4FcA5O8cDU2UOPwBsvsociaenfB3BA/640?wx_fmt=png&from=appmsg)

然而好像不得行，算了直接加帐号吧

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLsh2PAmGwyaiaYtDtUIYz83EZA0xIeDic4WRP177m5jLSWu4lW9L0XGGw/640?wx_fmt=png&from=appmsg)

imag

登录远程终端

看了浏览器的历史记录

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLLWz9dicbt0mIceK3Yt65oS6H6QtHpoQzL0Bo2bETic4ohxPxBhEUUDfA/640?wx_fmt=png&from=appmsg)

顺其自然的登录后台：

开始以为这个后台是另外一台服务器，结果看了iis还有域名解析才发现是当前机器。。。有点小失望emmm

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLhiaKic1lyFic8iaYpKTa0icFSgqRfXA6hHdsjlXCU6ZibMS7tEaSWW9b3CNA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYLpetUGsrfSicaaqtkXRtX9zY6DictWNYXzt0buW4LC1olMqLN2jQJQ7Rw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4CBZermKTpS6SqTopeRjYL1sUNjldamQV07n62jCHhVjN7pvkmw9zUMhItYJOI8nIs1YzYnB9e8w/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

原文:https://forum.90sec.com/t/topic/876

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