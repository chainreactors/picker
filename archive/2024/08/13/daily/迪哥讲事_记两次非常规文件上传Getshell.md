---
title: 记两次非常规文件上传Getshell
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495503&idx=1&sn=3009564f8521fd93668b81423b254144&chksm=e8a5e52cdfd26c3aea6394c5dee713d7949569da50f13864ce66c556117ce014b1ba11edd9c1&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-13
fetch_date: 2025-10-06T18:09:03.607098
---

# 记两次非常规文件上传Getshell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7qDr0KWtCXmBSD9wT7ddLozmR7WTbrFgseL5jUJQialUf2zS7ib4m89IrHUbJ29cKt2kjIf5ibBFoUg/0?wx_fmt=jpeg)

# 记两次非常规文件上传Getshell

迪哥讲事

以下文章来源于Hack All Sec
，作者Hack All

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5s3ZRBYQa0A234O10brMpTXETodZLOpwpfApdGMiceMTQ/0)

**Hack All Sec**
.

专注于网络安全，渗透测试，文章和工具分享，包括但不限于Web安全、物联网安全、车联网安全，我们的目标是Hack All！

常规绕过前端和后端的任意文件上传已经没意思了，本文记录下之前和最近遇到的2个不太常规的任意文件上传Getshell的案例。

## **[****路径穿越+文件上传Get Shell****]**

Nmap快速全端口扫描发现开放22，80和3306端口。访问目标，使用[hfinger](https://github.com/HackAllSec/hfinger)扫描发现Web应用使用了`Spring Boot`和`Ueditor`，同时在留言页面发现有个上传图片功能：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLfichGUDzMXDDYvA2m2sknuCbQjSjtTMNjldcOv4ZAkNcxf6lmZnn06G8w/640?wx_fmt=png&from=appmsg)

抓包发现上传采用自定义API实现，没有任何限制。但是访问正常图片、txt文件、html文件都可以，访问jsp时却返回404：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLfic8ibJzOyPADj1o4GuvIdt6peib3JANUbGnibhsqbyn7Hkwts8sojewLh5g/640?wx_fmt=png&from=appmsg)

经过查询可能的原因是：

* 缺少依赖：如`spring-boot-starter-tomcat`和`javax.servlet-api`
* 配置错误：`application.properties`或`application.yml`中的JSP配置可能不正确
* 文件位置不正确：JSP文件必须放在正确的目录下，通常是`/src/main/webapp/WEB-INF/views/`

访问`index.jsp`也返回404，应该是使用了默认的配置没有解析jsp。难道煮熟的鸭子就这么飞了？
俗话说只有不努力的黑客，没有攻不破的系统，继续尝试采用目录穿越上传到其它目录，发现报错信息返回了网站绝对路径，可以看出有tomcat（其实Spring Boot默认内置了Tomcat Web容器）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RRvwcPDcIk0m577p8x6oHbcrY0Jibet1oZo2x2TyL3rwa23xTicgT4P76LiauJlbYWVRl1FAQSgD4p1Q/640?wx_fmt=png&from=appmsg)

根据暴露的网站绝对路径，直接构造4个`../`将文件上传到网站根目录下，利用Tomcat进行解析jsp成功：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficupYp2FS3pL4iceITuB4tMSEN8IGwkr0jxvwXwPk87w8S00hxIj5uk7g/640?wx_fmt=png&from=appmsg)

然后替换为Webshell即可拿下目标：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficb3NibvUDvyLXEDHYhAz8Y7A2d2ujFDe0edMyMgYickQPKXfcQ30IicdQA/640?wx_fmt=png&from=appmsg)

## **[****Excel导入Get Shell****]**

某次项目中发现用户批量导入功能前端没有校验文件后缀和内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/s7bObPUU0RRvwcPDcIk0m577p8x6oHbcNtDGvunpfUX4qAvRzX25srKb1Owic5OBHzUmzya1akibwtibxj3UiaJ3Dw/640?wx_fmt=jpeg&from=appmsg)

但是提交后会返回“文件名称不支持”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/s7bObPUU0RRvwcPDcIk0m577p8x6oHbc6LuXwx4gic4gYMVYick1lxjFGcHrSx80cdyeqTYvHjttElMhj126M9Eg/640?wx_fmt=jpeg&from=appmsg)

而上传包含`.xls`或`.xlsx`的后缀时返回导入失败：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/s7bObPUU0RRvwcPDcIk0m577p8x6oHbcfmjIjDHKGzTQTfVVWOSO3icKmWbZxmrWpDKwGXmBOviaITEULR1n8yMg/640?wx_fmt=jpeg&from=appmsg)

这说明后端可能执行了Excel文件导入操作。上传名称为`xxx.xls.xxx`的正常模板文件时没有报错，这说明猜想是正确的。

然后构造名称为`xxx.xls.jsp`的webshell文件，虽然返回导入失败，但是根据目录扫描发现的`uploads`目录拼接上传的文件名后，返回200：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/s7bObPUU0RRvwcPDcIk0m577p8x6oHbcHTvs1t5FniaPuI2RbYWSRlGCkxB7ekCY5OZZFq1ia5SbrHRtKzDcvP0w/640?wx_fmt=jpeg&from=appmsg)

然后成功连接webshell：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/s7bObPUU0RRvwcPDcIk0m577p8x6oHbcIIF9Rz09dpGIq1RYnUr4w1yticRUKialwKExPKicIA3zcLwicTUCzJsCnQ/640?wx_fmt=jpeg&from=appmsg)

拿下目标：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/s7bObPUU0RRvwcPDcIk0m577p8x6oHbcW7u3Op3JtAbASMmvibz888wcap6FXytM1picjt5woDPic1W2HMWGFTrlg/640?wx_fmt=jpeg&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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