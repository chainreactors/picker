---
title: web服务器启用了不安全的HTTP方法(转)
url: https://blog.csdn.net/aomandeshangxiao/article/details/127899208
source: 傲慢的上校的专栏
date: 2022-11-18
fetch_date: 2025-10-03T23:05:13.329305
---

# web服务器启用了不安全的HTTP方法(转)

# web服务器启用了不安全的HTTP方法(转)

最新推荐文章于 2024-06-22 22:41:54 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png)

[傲慢的上校](https://blog.csdn.net/aomandeshangxiao "傲慢的上校")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
最新推荐文章于 2024-06-22 22:41:54 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.2k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

分类专栏：
[Spring](https://blog.csdn.net/aomandeshangxiao/category_12014592.html)
文章标签：
[服务器](https://so.csdn.net/so/search/s.do?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

原文链接：<https://blog.csdn.net/bobozai86/article/details/82708449?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-82708449-blog-108851572.pc_relevant_landingrelevant&depth_1-utm_source=distribute.pc_relevan>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Spring
专栏收录该内容](https://blog.csdn.net/aomandeshangxiao/category_12014592.html "Spring")

6 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了一种通过配置web服务器来禁用不安全的HTTP方法（如PUT、DELETE等）的方法，以增强应用的安全性。文章展示了如何使用web.xml文件进行具体配置。

[web服务器启用了不安全的HTTP方法\_波波仔86的博客-CSDN博客\_配置错误的web服务器允许远程客户端执行危险的http方法,如put和delete。](https://blog.csdn.net/bobozai86/article/details/82708449?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-1-82708449-blog-108851572.pc_relevant_landingrelevant&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-1-82708449-blog-108851572.pc_relevant_landingrelevant&utm_relevant_index=2 "web服务器启用了不安全的HTTP方法_波波仔86的博客-CSDN博客_配置错误的web服务器允许远程客户端执行危险的http方法,如put和delete。")

```
<security-constraint>
<web-resource-collection>
<web-resource-name>fortune</web-resource-name>
<url-pattern>/*</url-pattern>
<http-method>PUT</http-method>
<http-method>DELETE</http-method>
<http-method>HEAD</http-method>
<http-method>OPTIONS</http-method>
<http-method>TRACE</http-method>
</web-resource-collection>
<auth-constraint></auth-constraint>
</security-constraint>
<login-config>
<auth-method>BASIC</auth-method>
</login-config>
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/d2d7957684914173b2ea5ac8d23c76be_aomandeshangxiao.jpg!1)

傲慢的上校](https://blog.csdn.net/aomandeshangxiao)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  0

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

[【已解决】无法在*web*.xml或使用此应用程序部署的jar文件中解析绝对uri：[*http*://java.sun.com/jsp/jstl/core]](https://blog.csdn.net/weixin_44081211/article/details/129890577)

[weixin\_44081211的博客](https://blog.csdn.net/weixin_44081211)

03-31
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
6487

[这个jar包也会出现无法在*web*.xml或使用此应用程序部署的jar文件中解析绝对uri这个问题，至于其他的standard.jar，standard-impl等等jar包我都没有引入，Tomcat的lib中我也没有添加其他解决方案中的jar包，也可以使用。解决时间：2023/3/31，我使用的tomcat是8.5版本的，在整合SSM项目时在jsp中使用JSTL的核心标签库 - core，也就是使用。有知道的大佬麻烦说明一下，解答我的疑惑。，搜索出来的*方法*都没成功，这个是我页面上出现的报错。](https://blog.csdn.net/weixin_44081211/article/details/129890577)

[【*安全*问题】*启用*了*不**安全*的*HTTP**方法*——深度分析及解决方案](https://blog.csdn.net/Hello_MiaoJiang/article/details/108851572)

[Hello\_MiaoJiang的博客](https://blog.csdn.net/Hello_MiaoJiang)

09-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
7541

[前言
*启用*了*不**安全*的*HTTP**方法*是常见的*安全*报错。本文将对八种主要的*HTTP**方法*进行原理及*安全*性分析，并提供简单的解决方案。
1、*HTTP**方法**安全*性分析
1.1 *HTTP**方法*由来
*HTTP*协议提供了集中请求方式，每种请求方式都有*不*同的作用，*HTTP*请求可以使用多种请求*方法*。
*HTTP*1.0定义了三种请求*方法*： GET, POST 和 HEAD*方法*。
*HTTP*1.1新增了五种请求*方法*：OPTIONS, PUT, DELETE, TRACE 和 CONNECT *方法*。
1.2 *HTTP**方法*详述
GET*方法*：G](https://blog.csdn.net/Hello_MiaoJiang/article/details/108851572)

参与评论
您还未登录，请先
登录
后发表或查看评论

[*启用*了*不**安全*的*http**方法*漏洞](https://download.csdn.net/download/lzwlove/10197020)

01-09

[在*web*.xml文件中配置下面一段内容
/\*
PUT
DELETE
HEAD
OPTIONS
TRACE
BASIC](https://download.csdn.net/download/lzwlove/10197020)

[漏洞挖掘-*不**安全*的*HTTP**方法*](https://blog.csdn.net/weixin_48421613/article/details/128611546)

[weixin\_48421613的博客](https://blog.csdn.net/weixin_48421613)

01-09
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
5426

[如果文件修改失败，则会返回其他状态码，例如 405 *Method* Not Allowed。如果文件删除成功，*服务器*会返回 200 OK 状态码；使用 PROPFIND *方法*，客户端可以请求*服务器*上的资源的属性列表，也可以请求具体的属性值。笔者在一次漏洞挖掘的过程中，几乎是习惯性的看了一眼OPTIONS*方法*，OPTIONS*方法*很简单，只需要在请求包里直接将GET/POST*方法*进行替换，即可看到*服务器*开启了哪些*方法*。​使用 DELETE *方法*时，客户端向*服务器*发送 DELETE 请求，并指定要删除的资源。](https://blog.csdn.net/weixin_48421613/article/details/128611546)

[*启用*了*危险*的*Method*](https://blog.csdn.net/qq_24313643/article/details/82457285)

[曉儂](https://blog.csdn.net/qq_24313643)

09-06
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3639

[漏洞名称：
*启用*了*危险*的*Method*
描述：
*目标**WEB**服务器**启用*了TRACE *Method*。
1.TRACE\_*Method*是*HTTP*（超文本传输）协议定义的一种协议调试*方法*，该*方法*会使*服务器*原样返回任意客户端请求的任何内容。
2. 由于该*方法*会原样返回客户端提交的任意数据，因此可以用来进行跨站脚本（简称XSS）攻击，这种攻击方式又称为跨站跟踪攻击（简称XST）。
危害：
1. 恶意...](https://blog.csdn.net/qq_24313643/article/details/82457285)

[若依（*不*分离版）*启用*了*危险*的*Method* *(*TRACE*)*](https://devpress.csdn.net/v1/article/detail/139889370)

[rckliaoming的博客](https://blog.csdn.net/rckliaoming)

06-22
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
386

[最近被扫描出来的第二个问题，*启用*了*危险*的*Method* *(*TRACE*)* ，A5 *安全*配置错误，搜索了一些文章，发现主要是*服务器*未禁用这些*方法*的调用，那么我们就从系统出发，再系统层面解决，参考的文章是。我是直接在启动类里面设置的。打印日志即可看出效果。](https://devpress.csdn.net/v1/article/detail/139889370)

[如何关闭*http* *Method*s中的Trace 提高*安全*意识](https://download.csdn.net/download/weixin_38738528/14890789)

01-20

[TRACE和TRACK是用来调试*web**服务器*连接的*HTTP*方式。 支持该方式的*服务器*存在跨站脚本漏洞，通常在描述各种浏览器缺陷的时候，把”Cross-Site-Tracing”简称为XST。 攻击者可以利用此漏洞欺骗合法用户并得到他们的...](https://download.csdn.net/download/weixin_38738528/14890789)

[*Web**服务器*配置*安全*](https://blog.csdn.net/xiao1234oaix/article/details/135941554)

[Kali与编程](https://blog.csdn.net/xiao1234oaix)

01-30
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1006

[在评估*Web**服务器*配置的*安全*性时，需要了解一些常见的*Web**服务器**安全*漏洞，并采取一些*方法*来发现潜在的漏洞和*安全*问题。*Web**服务器*是提供网站和应用...