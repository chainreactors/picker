---
title: 某健康教育平台 ASP.NET前台RCE代码审计
url: https://mp.weixin.qq.com/s/tlgsNLVwzYkvhSu7nM1LfQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:32.580757
---

# 某健康教育平台 ASP.NET前台RCE代码审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/10dIbyHH823bkmqFY1U62g41rGHV7bxugrRw4Ujpely6kib7m8gdLLuapPjO7vUvZOUD5LWQdnibQygAz5UQbf3RuY0npE1JP0mrKXBXKKT7A/0?wx_fmt=jpeg)

# 某健康教育平台 ASP.NET前台RCE代码审计

威零安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于进击安全
，作者学员投稿

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Eu4ArzE5xKh7ouSAzvohwFkvzPibNQxs6X4k2SxgCvBA/0)

**进击安全**
.

主要分享一些个人实战经验，以及漏洞复现，代码审计，等等方面的文章，欢迎大家关注我的公众号呀，可以投稿哦，有稿费的哦，菜鸟路过～～～

# 现在只对常读和星标的公众号才展示大图推送，建议大家能把**威零安全团队**“**设为星标**”，否则可能就看不到了啦！ ![](https://mmbiz.qpic.cn/mmbiz_png/DlIbJNHXhc1pC40KxSpjPOq2S0fHe2qPiaFvQ8pRogV5MEXG7q82OdZTUzic2vEOV4NfUpnHYdXQPhnYbdibctq0Q/640?wx_fmt=png&from=appmsg) 免责声明 本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。 由于传播、利用本公众号所发布的而造成的任何直接或者间接的后果及损失，均由使用者本人承担。威零安全实验室公众号及原文章作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

一、前言

来给尊师投稿一个ASPX借助AI分析挖掘出来的首洞！

二、框架识别

该系统基于 **ASP.NET Web Forms** 架构（非 MVC），核心入口位于 `AMHWeb.dll` 中的 `MvcApplication` 类（Global.asax）：

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTomClMFu85GbicicsShg9WXYFHWUXf46gBfhD45PvwfBbYicia053yxRdaKS9bCFXTcjq8Uhw9Gb7rI5A1iaKTSflmvtxjnaia5FJC0/640?wx_fmt=png&from=appmsg)

* `Application_BeginRequest` 中没有调用任何鉴权模块（如 FormsAuthentication、自定义 HTTP Module）
* 没有全局的 `AuthorizeRequest` 事件绑定

而且法发现该系统存在**两套独立的鉴权体系**，且完全分开管理：

三、鉴权分析

    主系统登录入口 `/ashx/Login.ashx`:

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTFLwcm72BcBl7VBy2jOWCoAUZ9w7G1y7rNjpvzmib5CJC4SrY0pLUhuSxyE6yicnbzGpj7MaNXvmDxQFaPl2Wto7tmLOYrRgfhM/640?wx_fmt=png&from=appmsg)

    用户类型包括：Student, Parent, Admin, Counselor, SchoolSuperAdmin, Teacher, CommissionAdmin, SuperAdmin, ClassTeacher。

    鉴权方式：部分后台 handler 在处理请求前**手动检查** Cookie 或 Session：

这里也就是尊师常说的文件开头鉴权。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTp2LpujeZf43PVYmaribg1oW0MjTwEl8icXibslnuAPc8LLRYYY2hicEic8QjGXOpARBl2ryQUU0aspELYNtns1saicO9fF7pcZia7xg/640?wx_fmt=png&from=appmsg)

#### 前台WebApp鉴权

####

前台门户 `/AppWeb/ashx/AdminLogin.ashx` 独立使用**纯明文 Cookie 鉴权**：

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kT3qH2gWFYQjYgCyISPFiaLulA3ZnBJia11QgMRjRDTnrMFiaM2gJfs1HsFiaZOW4DicSokHErAbXiaRmuenia5UCuXzicAChvKGtBibL1M/640?wx_fmt=png&from=appmsg)

其中 `WebAppAdminLogin` 直接在数据库中明文对比密码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kR8Tc3FnK7uSickFIo4rYovyC3j9paBNTzSn7BPZn4iaia9P5679qbolz9o7Wzx3QZIIAsSHlZUibwfGSXNcYmVyftPhibILtYIwnJ4/640?wx_fmt=png&from=appmsg)

该框架的鉴权不是通过中间件/模块全局强制执行的，而是**依赖每个 Handler 开发者手动编写鉴权检查代码**。这意味着：

* 如果开发者忘记写鉴权检查 → 该接口就是**公开可访问**的
* 没有编译器级别或框架级别的强制鉴权约束
* 没有任何 Base Class 或抽象方法强制子类实现鉴权

所有 `/AppWeb/ashx/` 目录下的 handler 均直接实现 `IHttpHandler`，无任何基类：

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kS9pcJ3XASicnVqjEHPUrnBfzVNOYn5E2U1CvMnVXw53QkJWxObhLGOibdiaAxmEr5ialkWpDDazRGNnmBHkPMKOJPbLa5Sqpw7t5s/640?wx_fmt=png&from=appmsg)

四、前台RCE

 这里直接进行定位到相关的文件上传搜索特征SaveAs(

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQxKGXepUYAmqmGIRBk5hM8QAcx41iajxjnfPhhyRXve2APeQx81eKjcrmfQMVaHMP4mzBREFlHPeiaLYwmCQoLdED4LMO17Mo7w/640?wx_fmt=png&from=appmsg)

        可以看到没有任何过滤直接将文件进行上传，并且也没有进行鉴权处理，前台可以直接进行访问。

/xxxxx/ashx/ImgUploader.ashx

尝试进行漏洞利用。

五、漏洞复现

构造相关的数据包，成功RCE！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kT18wzp9kIkiapoL0Ul8CSDal9IdxoPu59qJwGmlRc9HvyFWWiap6Nia6mP7NQ2gvx8AnjxsjqPcYqCDkzlxC81iaMYQ84lAVWvFyQ/640?wx_fmt=png&from=appmsg)

```
代码审计培训介绍&广告区域

二、第五期课程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dJGuszYr5iaRGiaZURAxJAROibCh1sjaZictcbC4iasuuOgCMQSDSwrG5Wfrx2QgfvKx8icDhm0gIia8fN6mThehEK8ww/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=121)

第五期课程仍然是以代码审计为主，本次课程还是为三个语言的代码审计0-1讲解，目的为帮助学员完成0-1+1的白盒（代码审计）漏洞挖掘，并且在出货的基础上再+1去出高质量的漏洞（例如组合拳RCE、前台相关漏洞等）。

1

课程周期

开课周期预计到：三个月左右（直播+录播）

课程大纲

本次课程分为PHP、JAVA、NET代码审计为直播+录播，为了照顾一些基础较为薄弱的师傅新增基础~技巧~番外（录播课程）。

01

PHP&JAVA&NET代码审计 (直播+录播)

之前课程大纲主要为xxx实战案例，本次课程大纲着重体现思路方向，并非取消了实战部分，实战部分之多不减。

PHP课程目录

✅  第一节课：多框架初识&路由认识&参数传递

✅  第二节课：多框架&鉴权分析&认证与鉴权&鉴权方式

✅  第三节课：多框架&常见漏洞函数&回显&非回显

✅  第四节课：注入漏洞&常见位置&实战审计注入类漏洞

✅  第五节课：前台RCE漏洞审计&漏洞案例技巧讲解

✅  第六节课：门户网站CMS&网络设备&审计经验讲解

✅  第七节课：多框架&鉴权对抗&权限绕过技巧&案例分析

✅  第八节课：组合拳RCE漏洞分析&漏洞组合拳利用&案例

✅  第九节课：PHP下反序列化漏洞&魔术方法&pop链分析

✅  第十节课：PHP下反序列化漏洞实战&phar协议RCE案例

JAVA课程目录

✅  第一节课：Servlet&Spring Boot&Spring MVC&Struts2

✅  第二节课：多框架下&拦截器&认证鉴权&组件鉴权分析

✅  第三节课：多框架下&权限绕过&鉴权对抗&案例分析

✅  第四节课：常见漏洞函数&案例分析&审计技巧

✅  第五节课：前台漏洞审计&组合拳rce漏洞&技巧&案例

✅  第六节课：反序列化&CC链利用&反序列化漏洞利用

✅  第七节课：Ognl&SpEl&EL表达式注入&漏洞案例

✅  第八节课：内存马简介&内存马原理分析&内存马注入方式

✅  第九节课：RMI&JNDI注入&JNDI注入漏洞利用&案例

✅  第十节课：组件漏洞&shiro&fastjson&log4j分析&利用

.NET课程目录

✅  第一节课：初识.NET&Web From & MVC架构框架分析

✅  第二节课：Web From&MVC框架&鉴权分析&认证方式

✅  第三节课：多框架下&鉴权对抗&权限绕过分析&案例

✅  第四节课：注入漏洞分析&文件操作类漏洞&实战分析

✅  第五节课：常见漏洞位置&前台漏洞审计&漏洞案例讲解

✅  第六节课：组合拳RCE漏洞分析&组合拳RCE案例讲解

✅  第七节课：.NET反序列化漏洞初识&反序列化漏洞原理

✅  第八节课：.NET安全反序列化链&反序列化触发场景

✅  第九节课：.NET反序列化漏洞案例&反序列化漏洞分析

02

基础~技巧~番外（录播)

该篇章为长期更新

1

基础篇章

1、由于之前上课时部分师傅存在一定基础，刚开始的课程部分师傅认为自己可以跟的上等问题，导致时间的浪费。

2、同时有一定的师傅存在无法搭建源码，以及软件下载等问题，于是将这种基础问题，统一归纳为基础篇章，供师傅们学习，节省师傅们时间提升学习效率及课程质量

3、同时面对部分学员频繁提出的一些问题，针对该问题同样会进行解答，并且进行录制上传至基础篇章中。

2

技巧篇章

1、随着自己技术的进步也了解到了一些新型的技巧或者手法，例如sql注入的某一个技巧，但是重新讲解又浪费大量时间，特地新增了技巧篇章，将单独的技巧进行讲解。

3

番外篇章

1、自己在第四期讲过一些逆向相关，并且还存在相关的一些好的案例，得到了挺多师傅的认可，例如某APP接管存储桶等案例，于是之后在有好的案例将进行上传更新。

课程思维导图

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQKhU3nNF3WFMgeJBzFezhmlK2T3o8oMFBeBhd5H8lfhsrkfww4JnqkibSU9uAengMOW2Bicw9UUCxNonq8k6YHIXWSFfclHSzm4/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=122)

常见疑问&课程讲解

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=123)

第五期课程收费多少？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=124)

本次课程收费仍然是1688，并且还是承诺一次报名后续不再进行任何二次收费保障（包含内部平台，以及后续推出一系列内容均可观看）。

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=125)

什么时间段上课，上课周期是多长时间？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=126)

第五期课程【直播+录播】上课周期为三个月，一般集中在周五六日这三天，一周保持2～3节课，每节课1小时左右。

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=127)

作为学员，我们都有哪些权益？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=128)

首先最关键的就是课程内容是可以一直学习的，同时内部报告平台也可进行观看，答疑是不限时长，不限类型方向，任何方向均可，再次同时代码审计最关键的就是源码，源码&课件&视频都是给兄弟们配套的，当然无聊找小朋友聊天一起打游戏也可以哦。

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=129)

学完之后可以达到什么水平？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=130)

学完之后可以达到可以进行独立审计的水平，在面对php、JAVA、NET主流语言的源码，可以进行独立审计，验证漏洞，对于一些JAVA安全内容例如：反序列化，内存马等也有一定的理解，可以进行打反序列化漏洞、注入内存马等操作，同时PHP的反序列化、pop链，phar协议等利用也有一定理解，且此类漏洞导致RCE均有案例。

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=131)

0基础可以学吗？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=132)

1、这是大家最常问的一个问题，0基础是可以的，我的代码审计课程一直秉持着帮助大家完成代码审计0-1的目标，同时往期（第四期）课程新增了进阶课，其目的也是帮助大家完成0-1出洞到0-1出有质量的漏洞。

2、另外考虑到有的学员基础较为薄弱，本期同时也开了番外篇&基础篇，师傅们可以观看这块分区课程内容，此类分块课程目的就是为协助到一些基础比较薄弱的师傅们。

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4P...