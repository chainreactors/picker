---
title: ​Apache Tomcat高危漏洞曝光，远程代码执行风险需警惕
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587465&idx=2&sn=e5d0f25746dce13de80ec7ed9907263f&chksm=b18c21c386fba8d5143def50c0fea96255f636311a6494c19b1e2f693f34d65cd53557264f87&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-20
fetch_date: 2025-10-06T19:38:53.980782
---

# ​Apache Tomcat高危漏洞曝光，远程代码执行风险需警惕

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr94tybSmiahsUXIWibmwpvaQOJXrPOiaIafh9vgsZqib9oqqoeZogLbicYdjw/0?wx_fmt=jpeg)

# ​Apache Tomcat高危漏洞曝光，远程代码执行风险需警惕

看雪学苑

看雪学苑

近期，Apache Tomcat，这款广泛使用的开源Web服务器和servlet容器，被披露存在两个严重的安全漏洞。这些漏洞可能使攻击者远程执行代码，甚至引发服务拒绝攻击，对企业信息系统安全构成严重威胁。

Apache软件基金会紧急发布了针对Apache Tomcat的补丁，以修复这两个被标识为CVE-2024-50379和CVE-2024-54677的漏洞，并强烈建议用户立即升级到最新版本以增强系统安全性。

CVE-2024-50379是一个“重要”级别的漏洞，影响了多个版本的Apache Tomcat，包括11.0.0-M1至11.0.1、10.1.0-M1至10.1.33以及9.0.0.M1至9.0.97。该漏洞允许在特定条件下远程代码执行，攻击者可以利用并发读取和上传操作中的竞态条件，如果默认的servlet配置了写权限，且文件系统不区分大小写，攻击者就能上传文件并使其被错误地当作JSP文件执行。

另一个被分类为“低”级别的CVE-2024-54677漏洞，虽然看似威胁不大，但同样不容忽视。它影响了相同版本的Apache Tomcat，由于Tomcat提供的示例Web应用程序未能限制上传数据的大小，攻击者可以通过上传大量数据触发内存溢出错误，导致服务拒绝。

值得注意的是，默认情况下，示例Web应用程序仅允许从本地主机访问，这在一定程度上限制了潜在的攻击范围。然而，安全研究人员Elysee Franchuk、Nacl、WHOAMI、Yemoli和Ruozhi以及Tomcat安全团队发现的这些漏洞，提醒我们必须重视定期的安全审计和及时的补丁更新。

资讯来源：cybersecuritynews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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