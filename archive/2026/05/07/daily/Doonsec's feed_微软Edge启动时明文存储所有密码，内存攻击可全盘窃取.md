---
title: 微软Edge启动时明文存储所有密码，内存攻击可全盘窃取
url: https://mp.weixin.qq.com/s/SjjOwfDjdAddb4HzYyaGig
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:53:52.008635
---

# 微软Edge启动时明文存储所有密码，内存攻击可全盘窃取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1t3gaotOvXNBQAYWeE3ib3Z7RqZu1sZ4k79TjE4V9PkvJ2I5oDfUeN5GzjZxoFWu1EXKibYHnVASjmz3kdfk0kfS2Xrj2E3RUDA/0?wx_fmt=jpeg)

# 微软Edge启动时明文存储所有密码，内存攻击可全盘窃取

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3VXCZ3JcRZ6WpXwrrqMmzTNLT2NwxM0UPRuHNy3HnibcViaibKr7FHysATY4cpcEYwiauOBNciamuTZkkJQ91siaZ62nE6QeibZk8HicA/640?wx_fmt=png&from=appmsg)

##

一位安全研究人员发现，微软Edge浏览器在启动瞬间会将所有已保存的密码解密并加载至进程内存，且以明文形式持续驻留——无论用户是否访问过相关网站。这项发现由PaloAltoNtwks Norway的研究员 @L1v1ng0ffTh3L4N 于4月29日在BigBiteOfTech上披露，源于其对主流Chromium浏览器凭证内存处理机制的系统性测试。

##

**Part01**

## ****对比分析****

Edge是唯一存在该行为的浏览器。它启动时会将整个密码库以明文形式加载至进程内存，并在整个会话期间保留。这与谷歌Chrome形成鲜明对比：

* Chrome采用按需解密机制，仅在自动填充或用户显式查看密码时才会解密凭证。
* Chrome通过应用绑定加密（App-Bound Encryption）技术，将解密密钥与经过身份验证的Chrome进程进行密码学绑定，防止其他进程复用该密钥访问凭证。

**Part02**

**安全风险**

Edge缺乏上述保护机制。从浏览器启动起，密码库中所有站点的凭证都以明文形式存在于进程内存中，这为能够读取进程内存的攻击者提供了持续、广泛的凭证提取目标。更矛盾的是：

* Edge在密码管理器界面仍然会要求用户重新认证才能显示密码。
* 但浏览器进程早已以明文形式持有全部凭证，任何能够查询进程内存的人均可获取。

这种重新认证机制仅营造了访问控制的假象，对基于内存的凭证提取毫无防护作用。在远程桌面服务（RDS）或终端服务器等多用户环境中，风险尤为严重——具备管理员权限的攻击者可同时读取所有登录用户进程的内存。

**Part03**

## ****概念验证****

随披露发布的概念验证视频显示，攻击者通过一个受控的管理员账户，成功从其他两名登录用户（包括会话已断开但进程仍活跃的用户）的Edge浏览器进程内存中提取出了存储的凭证。这使得单次管理员账户沦陷，演变为整个多用户环境的凭证全面泄露，直接对应MITRE ATT&CK攻击框架中的T1555.003技术（从Web浏览器获取凭证）。

**Part04**

## ****厂商回应与应对建议****

微软在接到漏洞披露后回应称，该行为“符合设计”。其公开文档承认，浏览器内存中的凭证在本地攻击场景下可能被读取，但将此类场景划归为“超出浏览器威胁模型”。

BigBiteOfTech同期发布了一款小型验证工具，供用户确认Edge是否存在明文凭证内存驻留现象。安全团队应特别注意：

部署了Edge的Windows终端服务器、虚拟桌面（VDI）等共享访问系统，需将此问题视为高优先级配置风险。

建议迁移至具备按需解密和应用绑定加密机制的浏览器，直至微软修正该项设计。

**参考来源：**

Microsoft Edge Stores All Saved Passwords in Cleartext Process Memory at Launch

https://cybersecuritynews.com/microsoft-edge-passwords-cleartext/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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