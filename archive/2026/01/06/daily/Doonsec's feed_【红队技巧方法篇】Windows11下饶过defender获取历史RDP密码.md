---
title: 【红队技巧方法篇】Windows11下饶过defender获取历史RDP密码
url: https://mp.weixin.qq.com/s/VEvFwIu9Hjiw6csaODt7OA
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:22.829700
---

# 【红队技巧方法篇】Windows11下饶过defender获取历史RDP密码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vkeEKQ1OUJs8Lh1uxQgBfaEuMPtmMFwW9Ko59ibLdSafpWxOkxUvfeThjUMicDTPR2sZvWHmgW50h9lKLPMknoibg/0?wx_fmt=jpeg)

# 【红队技巧方法篇】Windows11下饶过defender获取历史RDP密码

原创

AKA嘴嘴

嘴嘴SEC

![]()

在小说阅读器中沉浸阅读

# | | | --- | | **声明：**本公众号分享的安全工具和项目均来源于网络，仅供安全研究与学习之用，如用于其他用途，由使用者承担全部法律及连带责任，与工具作者和本公众号无关。文章未经授权禁止转载。 | 现在只对常读和星标的公众号才展示大图推送，建议大家把嘴嘴SEC“设为星标”，否则可能看不到了！

0x01 前言

目前公开获取RDP的密码的方法主要是通过以下命令获取Masterkey的值去解密Credentials文件夹下的密码文件获取RDP密码：

```
mimikatz.exe "privilege::debug" "sekurlsa::dpapi" "exit" > 1.txt
```

暂且不说mimikatz的免杀问题，在PPL保护下该命令是跑不动的：

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJs8Lh1uxQgBfaEuMPtmMFwWBUm7iaFQt2icPCsryt3pyP8eLgbtRAmYBweF4Rp2ZhSDT76NInRCuorg/640?wx_fmt=png&from=appmsg)

另外，众所周知windows11 22H2版本后引入了Credential Guard，具体原理可自行搜索，总之最后会使得lsass进程中的明文密码值、ntlmhash等密码信息被隐藏。

这使得传统的hashdump方式就算绕过了PPL也dump不出ntlmhash等密码值。那么针对windows11还有哪些导出RDP密码的方式呢？

0x02 导出RDP密码的几种思路

首先敲个cmdkey /list看下有没有3389连接记录：

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxle5rX6raQricRTeLDvic3QlIW95EbjeotETC1uD9ibibCbSMvjgIofnpjg/640?wx_fmt=png&from=appmsg)

在win11的加强版防护下，就算你把defender关了，直接把mimikatz传上去本地执行，利用传统绕PPL方式现在也是dump不下来密码的。

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxY8dL55ES6WmMLaCAhSRDg5GQOVLyZFvjbcBicDTz9thjWaoTcvVE7qw/640?wx_fmt=png&from=appmsg)

类似procdump、nanodump之类的工具在defender关闭的情况下也不行，都帮你们测过了。

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxiaY7jMpCYz9m8F1zcp85vUibWnwToI9ibjnQMVk5tpThryIHGmMJnnhwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxAMLj2kdjHAOP7IuVJdHrwBsH0TUxQjzPMwZSvhMC6WJJfzJXrqIsWQ/640?wx_fmt=png&from=appmsg)

那么接下来还有几种思路：

## **1.运气好导出的ntlmhash值能直接解出明文**

如今windows11下的hashdump操作已经没有win10的时候那么容易了，但是目前通过reg save下来的sam.hive和system.hive导本地解密出ntlm这个方法还是没被defender杀的（用其他偏门方案也行，总之能拿到ntlm就行），假如你的运气够好，拿到的ntlm丢到cmd5上能解出明文密码，也能获解出rdp密码，不过该方法不是本篇文章讨论的范围。

## **2.有免杀的键盘记录工具**

要是团队中有强劲的开发写个免杀的键盘记录工具，挂着等着对面3389登录都键盘记录也不失为一种方法。

## **3.通过WerFaultSecure.exe直接获取masterkey**

那么在极端情况下，有ntlmhash解不出来，有没有好的键盘记录工具情况下，如何导出RDP密码呢？在2025年9月份，出现了一种“利用 Windows WerFaultSecure.exe 绕过PPL转储 LSASS 进程”的hashdump方式，操作方式可自行搜索，实测下来win10还可以，win11的话有点鸡肋，由于Credential Guard的存在，导致导出的hash被隐藏：

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxTV53iaojGBN1hJQEPUWfwnoPvBqTsib7tXgUwibMkxjNUSovmN94jc9cA/640?wx_fmt=png&from=appmsg)

但是意外的masterkey其实是还在的：

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxCxJao1IMTKcEjnu7gktVghPAJmWrDxt1I0LdqOnZoR1bmic1R3JZkjg/640?wx_fmt=png&from=appmsg)

最后会报错一个error，原因正是上文提到的Credential Guard的机制，这个防护也能绕但不在今天讨论内容之内。因为拿到masterkey对于解密RDP密码来说已经足够。

接下来写个脚本把masterkey提出来

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxicD9hZaqq1yuEHHGc5z5uYUcG0ibibjUqNUdtOiacPCvZZXOIN2RmLP0RQ/640?wx_fmt=png&from=appmsg)

最后把目标机器上的c:\users\xxx\appdata\Local\Microsoft\Credentials目录下的文件拷贝回本地：

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWx7kzeia0qMqaNBKa0GUaycwCvgOgPQZSVMJz6SHv0rd1mc281u2VHagg/640?wx_fmt=png&from=appmsg)

再写个脚本用masterkey去对Credentials的加密文件做碰撞解密即可，最后得到RDP连接记录的账号密码：

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/vkeEKQ1OUJuwwQwt4eHS75vzQN2ibvbWxZbCib0uK7ib0OLsIEcdRxf27WU3hSpCdxiciaktlcBhsPlDQQYV4dRoBAg/640?wx_fmt=other&from=appmsg)

思路是比较清晰的，不过中间涉及到许多小的脚本，自己实现起来略微复杂，有需求师傅的可以加入星球直接获取。

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJs8Lh1uxQgBfaEuMPtmMFwWGddia2yjGqc29n0RaBkw6AOCkE4GrHj9ugxurru8FHaxoN6QpsiaEvog/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/vkeEKQ1OUJsTvS3BLGMBib6G4FLq87O9KXusCP58tV0qmkDDGhL8rspz7HGKEV4Hw4KAabacGD3zWpYM68X1cdw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

0x03 星球简介

相信很多新手师傅在面对网安庞大的知识体系时通常手足无措，目前各类线上培训、公众号、知识星球等付费资源也是眼花缭乱。本人作为开发转安全方向人员，网课少说也报过七、八门，星球也加了十几个，也算是韭菜王了，踩坑经验丰富，新手师傅必定也会遇到这些问题。

创办本号主要分享网安领域学习踩坑经历及红队进攻实战经验等优质内容。涉及方向包括WEB、内网渗透、免杀、社工钓鱼。计划分为三大板块：

【学习路线规划篇】

     【漏洞挖掘实战篇】

     【红队技巧方法篇】

  ![图片](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_67@2x.png?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)欢迎各位师傅关注点赞星标三连![图片](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_67@2x.png?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

星球资源

目前已经更新的星球内容：

* 安全C2链路搭建方案
* CVE-2024-9474 Palo Alto Networks防火墙RCE漏洞魔改工具
* Defender下BypassUAC提权工具

* Win11下Defender防护获取RDP密码方案

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=9)

![](https://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJs8Lh1uxQgBfaEuMPtmMFwW5d6hl00JvcTWHc1HC2IXFyOkibsBTAYXZDiaZWRiaW41ianvmwiaKhYUQzw/640?wx_fmt=png&from=appmsg)

往期推荐

[【学习路线规划篇】网络安全避坑指南之方向抉择](https://mp.weixin.qq.com/s?__biz=Mzk1NzI5ODg3Nw==&mid=2247483696&idx=1&sn=fc1c8dfda0fba2292dd22d9f7491d491&scene=21#wechat_redirect)

[【红队技巧方法篇】Webshell命令执行失败实战场景下解决思路](https://mp.weixin.qq.com/s?__biz=Mzk1NzI5ODg3Nw==&mid=2247483729&idx=1&sn=d50892ea1333ba23e92beaa8b2d58c04&scene=21#wechat_redirect)

[【漏洞挖掘实战篇】记一次SQL注入极限绕过](https://mp.weixin.qq.com/s?__biz=Mzk1NzI5ODg3Nw==&mid=2247483677&idx=1&sn=7063371da1ac54956c3ca4e031316df5&scene=21#wechat_redirect)

[【红队技巧方法篇】安全C2链路搭建](https://mp.weixin.qq.com/s?__biz=Mzk1NzI5ODg3Nw==&mid=2247483764&idx=1&sn=abd9441da1a5ece4c6276c1f958a1a31&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=9)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/vkeEKQ1OUJvyI1Q5Mdf6xpTy2iaM41sQHMlE5xDdjuOaiclDXY0trLuciaVJ8RKel4rt0DIu6tiaJULyACPGuAb8Qw/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=12)

---

**关注【嘴嘴SEC】，获取更多安全技术干货！**
🔐 **安全无小事，技术无止境！** 🔐

![图片](https://mmbiz.qpic.cn/mmbiz_gif/vkeEKQ1OUJvyI1Q5Mdf6xpTy2iaM41sQHEWhNbFulqvBemZLnbVcTAv1InCnjichH5M8Y5zmvnCO8GQLkWONn9ibA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=13)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJsZicMZWguKnAKxfzzfgSZCYq8Q95u08vkJrPYTeXEEgOFs6ULVDIMsJMeQAHlyWBhCDic8b4H0x7UQ/0?wx_fmt=png)

嘴嘴SEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vkeEKQ1OUJsZicMZWguKnAKxfzzfgSZCYq8Q95u08vkJrPYTeXEEgOFs6ULVDIMsJMeQAHlyWBhCDic8b4H0x7UQ/0?wx_fmt=png)

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