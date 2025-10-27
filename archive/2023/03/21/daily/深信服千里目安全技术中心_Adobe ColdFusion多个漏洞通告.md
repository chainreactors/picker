---
title: Adobe ColdFusion多个漏洞通告
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247517954&idx=1&sn=7820c08652736e96e2fe15c221314b4b&chksm=ce460c12f9318504184b33040cbede8c35d60da7b8bc41a8b55b2c8ecad807f8208e30d63288&scene=58&subscene=0#rd
source: 深信服千里目安全技术中心
date: 2023-03-21
fetch_date: 2025-10-04T10:09:48.559670
---

# Adobe ColdFusion多个漏洞通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxT4ntXdCCQW6ibkL9KrVd8pICAibJqT2yZ8SZVXJCQ3Lj1DMPaBTZtalzQ/0?wx_fmt=jpeg)

# Adobe ColdFusion多个漏洞通告

深瞳漏洞实验室

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTbiaw0FyYcg6lmTNjHE1XHibMeOWSKWqchXkAotEOk7FmCJa3HuQwRhqQ/640?wx_fmt=gif)

**漏洞名称：**

Adobe ColdFusion多个漏洞

**组件名称：**

Adobe ColdFusion

**安全公告链接：**

https://helpx.adobe.com/security/products/coldfusion/apsb23-25.html

**官方解决方案：**

已发布

**漏洞分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQumzqu2Bt9wnicxbHzL6jIScDjRoJDZpkxhibpE8Z0xyib1Sicu9soobzA/640?wx_fmt=gif)

**组件介绍**

Adobe ColdFusion 是美国 Adobe 公司的一款动态Web服务器产品，其运行的CFML(ColdFusion Markup Language)是针对Web应用的一种程序设计语言。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQumzqu2Bt9wnicxbHzL6jIScDjRoJDZpkxhibpE8Z0xyib1Sicu9soobzA/640?wx_fmt=gif)

**漏洞描述**

近日，深信服安全团队监测到一则 Adobe 官方发布安全补丁的通告，共修复了 3 个安全漏洞，其中包含 2 个严重漏洞的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQYrqeBA3GXtfWoVqV0ub15ichGUkJwEjIlDDp0wUkW9rvTzWpF2LoxQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQumzqu2Bt9wnicxbHzL6jIScDjRoJDZpkxhibpE8Z0xyib1Sicu9soobzA/640?wx_fmt=gif)

**高危漏洞描述**

Adobe ColdFusion 反序列化远程命令执行漏洞 （CVE-2023-26359）

该漏洞是由于 ColdFusion 允许对不受信任的数据进行反序列化导致。**攻击者可利用该漏洞在未授权的情况下，构造恶意数据进行远程代码执行攻击，最终可以在服务器上执行任意命令。**

Adobe ColdFusion 访问控制不当远程命令执行漏洞 （CVE-2023-26360）

该漏洞是由于 ColdFusion 对用户的访问控制校验不当导致，**攻击者可利用该漏洞在未授权的情况下，构造恶意数据进行远程命令执行攻击，最终可以在服务器上执行任意命令。**

**影响范围**

目前受影响的 Adobe ColdFusion 版本：

ColdFusion 2018 ≤ Update 15

ColdFusion 2021 ≤ Update 5

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQumzqu2Bt9wnicxbHzL6jIScDjRoJDZpkxhibpE8Z0xyib1Sicu9soobzA/640?wx_fmt=gif)

**如何检测组件版本**

登陆 Adobe ColdFusion 管理员后台，点击 “System Information” 按钮即可查看版本号。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxT83E68FibJYvPyeibHibZ3Fht4pfem9qoBAJhvTBHQicAeia49tJ1AicUM32w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQumzqu2Bt9wnicxbHzL6jIScDjRoJDZpkxhibpE8Z0xyib1Sicu9soobzA/640?wx_fmt=gif)

**官方修复建议**

当前官方已发布最新版本，建议受影响的用户及时更新升级到最新版本。链接如下：

https://helpx.adobe.com/coldfusion/kb/coldfusion-2018-update-16.html

https://helpx.adobe.com/coldfusion/kb/coldfusion-2021-update-6.html

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTQumzqu2Bt9wnicxbHzL6jIScDjRoJDZpkxhibpE8Z0xyib1Sicu9soobzA/640?wx_fmt=gif)

**深信服解决方案**

**1.风险资产发现**

支持对 Adobe ColdFusion 的主动检测，可批量检出业务场景中该事件的受影响资产情况，相关产品如下：

**【深信服主机安全检测响应平台 CWPP】**已发布资产检测方案。

**【深信服云镜 YJ】**已发布资产检测方案。

**参考链接**

https://helpx.adobe.com/security/products/coldfusion/apsb23-25.html

**时间轴**

**2023/3/20**

深信服监测到 Adobe 官方发布安全补丁。

**2023/3/20**

深信服千里目安全技术中心发布漏洞通告。

点击**阅读原文**，及时关注并登录深信服**智安全平台**，可轻松查询漏洞相关解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxTZFbsg1LHD1ygpEChcIMmdQBsyBdCesYKZgukjibpwLicJGskz2sBojLg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5w6l9nMTe3NBU5AEwFJicPxT6bkD3RrK5HJHCCvj37RmeSVnpfgS9rOeOEuW5pErHKREDMR6cVt4uQ/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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