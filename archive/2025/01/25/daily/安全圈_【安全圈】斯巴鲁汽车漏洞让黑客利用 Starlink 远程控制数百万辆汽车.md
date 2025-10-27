---
title: 【安全圈】斯巴鲁汽车漏洞让黑客利用 Starlink 远程控制数百万辆汽车
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067590&idx=1&sn=32ea96086da2a1f7d7b7c25530ca8d55&chksm=f36e7b46c419f2508759cde38a0b63b3f4b1442bc7655fa88acfdb556c1fefa5e78211594fc2&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-25
fetch_date: 2025-10-06T20:10:58.278140
---

# 【安全圈】斯巴鲁汽车漏洞让黑客利用 Starlink 远程控制数百万辆汽车

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljmku6eiapKnvNCalPibs0iaib8pd89z1Gf38Yl6IEXY2z8mnpgHq3RnFToxlp8vzjriciaHG0yPh54ibXNQ/0?wx_fmt=jpeg)

# 【安全圈】斯巴鲁汽车漏洞让黑客利用 Starlink 远程控制数百万辆汽车

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljmku6eiapKnvNCalPibs0iaib8jWvINzB1GKbdGwkYU6saU8PyWDa9fkhUaM08fTE7BI7GfKK0YGATBg/640?wx_fmt=jpeg&from=appmsg)

去年年底，斯巴鲁 STARLINK 车联网服务被发现存在严重漏洞，导致美国、加拿大和日本的数百万辆汽车和客户账户面临潜在的网络攻击。

斯巴鲁以其全轮驱动汽车、高安全评级和在赛车运动中的强大影响力而闻名。Outback 和 Forester 等热门车型为其在美国销量排名前 10 名做出了贡献。

该安全漏洞允许攻击者使用姓氏和邮政编码、电子邮件地址、电话号码或车牌等最少的信息远程访问敏感车辆和个人数据。利用此漏洞，恶意行为者可以：

* 远程启动、停止、锁定和解锁车辆。
* 访问实时车辆位置并检索过去一年的详细位置历史记录。
* 提取客户的个人身份信息 (PII)，包括地址、账单详情（部分信用卡信息）、紧急联系人和车辆 PIN。
* 查询其他用户数据，如支持呼叫历史记录、里程表读数、销售记录等。

研究人员通过仅使用车牌号成功控制车辆证明了这一漏洞。他们还从一辆测试车辆中获取了一年多的精确位置数据。这些数据包括每次发动机启动时更新的数千个 GPS 坐标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljmku6eiapKnvNCalPibs0iaib8JcCP22m9ulZxEWNyHAeoScSL93NI0mPab5G4ibZzM5OcLkAuphBiaTxw/640?wx_fmt=png&from=appmsg)

### 如何发现漏洞

研究人员最初检查了斯巴鲁的 MySubaru 移动应用程序，发现其安全性很好。他们将注意力转移到面向员工的系统，通过子域扫描发现了 STARLINK 服务的管理门户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljmku6eiapKnvNCalPibs0iaib8BHwtNGuabwVDxmVwexTRb7AHZnKkMsHjZlhLGtBFwiazhkbunwnXh2g/640?wx_fmt=jpeg&from=appmsg)

起初，该网站似乎没什么内容——只有一个登录面板，也没有任何可用的凭证。然而，在研究该网站的源代码时，这一点引人注目：

```
<script type="text/javascript" src="/assets/_js/starlinkEnroll.js"></script>
```

这指向/assets/\_js/文件夹中一些有趣的 JavaScript 文件。为了深入挖掘，对目录进行了暴力破解，以发现任何隐藏的文件。

使用 FFuF 几分钟后，login.js发现一个名为的文件，其中包含以下代码：

```
$('#new_password_submit').on('click', function(e) {  e.preventDefault();  if($('#forgot-password-step4-form').valid()) {    disableBtns();    $.ajax({            url: "/forgotPassword/resetPassword.json",      type: "POST",            contentType: "application/json",            data: JSON.stringify({                email: email,                password: $('#new_password').val(),                passwordConfirmation: $('#confirm_new_password').val()            }),      async: false    }).done(function (response) {
```

代码表明/forgotPassword/resetPassword.json端点可以重置员工帐户而不需要确认令牌！

如果这是真的，攻击者可以利用任何有效的员工电子邮件来接管他们的帐户。为了验证这一点，我们发送了一个 POST 请求来检查该功能是否已公开且可运行。

该门户包含一个密码重置端点，允许在无需确认令牌的情况下接管帐户。他们利用来自 LinkedIn 和其他来源的公开信息，确定了有效的员工电子邮件地址以利用此漏洞。

进入管理系统后，他们通过禁用客户端安全覆盖绕过了双因素身份验证 (2FA)。这让他们可以不受限制地访问 STARLINK 的后端功能，包括：

* 查看和导出任何已连接斯巴鲁汽车的详细位置历史记录。
* 使用邮政编码或 VIN 等基本标识符搜索客户帐户。
* 在未通知车主的情况下将未经授权的用户添加到车辆中。

为了进一步验证他们的发现，研究人员在朋友的汽车上测试了他们的访问权限。他们成功地远程解锁了车辆，没有触发任何警报或通知。

该漏洞是由网络安全研究人员 Shubham Shah 和一位同事发现的，他们于 2024 年 11 月 20 日向斯巴鲁报告了该问题。该汽车制造商迅速采取行动，在报告后的 24 小时内修补了漏洞。

斯巴鲁在收到研究人员的报告后迅速做出了回应，该漏洞于2024年11月21日数小时内就被修复。研究人员表示，没有证据表明该漏洞在被修补之前被恶意利用。

此次事件凸显了人们对联网汽车网络安全的广泛担忧。现代汽车收集大量数据，并依赖于难以全面保护的互联系统。

研究人员指出，员工在日常工作中经常可以广泛接触敏感信息，这使得此类系统本质上存在漏洞。

这一发现清楚地提醒我们，强有力的安全措施对于保护消费者数据和确保对联网技术的信任的重要性。

来源：https://cybersecuritynews.com/subaru-car-vulnerability-lets-hackers-control-the-millions-of-cars-remotely/

***END***

阅读推荐

[【安全圈】美国前中情局分析师承认泄露国防信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=1&sn=a6a2923967fc3df6b71885df15512f84&scene=21#wechat_redirect)

[【安全圈】威胁者利用语音通话通过 Microsoft Teams 传播勒索软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=2&sn=45297a18045334bd95045d0b8a1349db&scene=21#wechat_redirect)

[【安全圈】1,000 多个恶意域名模仿 Reddit 和 WeTransfer 来传播恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=3&sn=73a9d0ef87cb24230598fa943275617a&scene=21#wechat_redirect)

[【安全圈】美国政府公布攻击Ivanti云服务设备的技术细节](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=4&sn=77fe4aa9d36cfc0f445aaaa0237973dc&scene=21#wechat_redirect)

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