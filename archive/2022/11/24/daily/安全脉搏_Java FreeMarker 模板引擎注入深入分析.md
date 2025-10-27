---
title: Java FreeMarker 模板引擎注入深入分析
url: https://www.secpulse.com/archives/191972.html
source: 安全脉搏
date: 2022-11-24
fetch_date: 2025-10-03T23:37:46.761931
---

# Java FreeMarker 模板引擎注入深入分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Java FreeMarker 模板引擎注入深入分析

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-23

10,626

温馨提示：图片有点多，请耐心阅读哦

## 0x01 前言

最近和 F1or 大师傅一起挖洞的时候发现一处某 CMS SSTI 的 0day，之前自己在复现 jpress 的一些漏洞的时候也发现了 SSTI 这个洞杀伤力之大。今天来好好系统学习一手。

* • 有三个最重要的模板，其实模板引擎本质上的原理差不多，因为在 SpringBoot 初学习的阶段我就已经学习过 Thymeleaf 了，所以大体上老生常谈的东西就不继续讲了。

三个模板的模板注入攻击差距其实还是有点大的，而且 Java 的 SSTI 和 Python Flask 的一些 SSTI 差距有点大。我们今天主要来看看 FreeMarker 的 SSTI

## 0x02 FreeMarker SSTI

FreeMarker 官网：http://freemarker.foofun.cn/index.html

对应版本是 2.3.23，一会儿我们搭建环境的时候也用这个版本

### FreeMarker 基础语法

关于文本与注释，本文不再强调，重点看插值与 FTL 指令。

#### 插值

* • 插值也叫 Interpolation，即 `${..}` 或者 `#{..}` 格式的部分，将使用数据模型中的部分替代输出

比如这一个 .ftl 文件

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello ${name}!</title>
    <link href="/css/main.css" rel="stylesheet">
</head>
<body>
    <h2 class="hello-title">Hello ${name}!</h2>
    <script src="/js/main.js"></script>
</body>
</html>
```

* • 那么 `${name}` 的数据就会从传参里面拿，对应的这个是在 `addAttribute` 中的 name 参数

#### FTL 指令

FTL 指令以 `#` 开头，其他语法和 HTML 大致相同。

> 我这里其实也花了不少时间看了 FreeMarker 的基础语法，但是并非很透彻，就不误人子弟了，有兴趣的师傅可以自己前往 FreeMarker 手册查看。

https://freemarker.apache.org/

### FreeMarker SSTI 成因与攻击面

看了一些文章，有些地方有所疏漏，先说 SSTI 的攻击面吧，我们都知道 SSTI 的攻击面其实是模板引擎的渲染，所以我们要让 Web 服务器将 HTML 语句渲染为模板引擎，前提是要先有 HTML 语句。那么 HTML 如何才能被弄上去呢？这就有关乎我们的攻击面了。

* • 将 HTML 语句放到服务器上有两种方法：
* • 1、文件上传 HTML 文件。
* • 2、若某 CMS 自带有模板编辑功能，这种情况非常多。

因为之前有接触过 Thymeleaf 的 SSTI，Thymeleaf 的 SSTI 非常锋利， Thymeleaf SSTI 的攻击往往都是通过传参即可造成 RCE（当然这段话很可能是不严谨的

在刚接触 FreeMarker 的 SSTI 的时候，我误以为它和 Thyemelaf 一样，直接通过传参就可以打，后来发现我的想法是大错特错。

#### 环境搭建

* • 一些开发的基本功，因篇幅限制，我也不喜放这些代码的书写，贴个项目地址吧

https://github.com/Drun1baby/JavaSecurityLearning/tree/main/JavaSecurity/CodeReview

#### 漏洞复现

前文我有提到，FreeMarker 的 SSTI 必须得是获取到 HTML，再把它转换成模板，从而引发漏洞，所以这里要复现，只能把 HTML 语句插入到 .ftl 里面，太生硬了简直。。。。。不过和 F1or 师傅一起挖出来的 0day 则是比较灵活，有兴趣的师傅可以滴一下我

payload：

```
<#assign value="freemarker.template.utility.Execute"?new()>${value("Calc")}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182138.png "null")

构造出这个 PoC 的原因是 `freemarker.template.utility.Execute` 类里面存在如下图所示的命令执行方法，都写到脸上来了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182140.png "null")

漏洞复现如图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182143.png "null")

#### 漏洞分析

我们要分析的是，MVC 的思维，以及如何走到这个危险类 ———— `freemarker.template.utility.Execute` 去的。

下一个断点在 `org.springframework.web.servlet.view.UrlBasedViewResolver#createView`，开始调试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182144.png "null")

跟进 `super.createView()`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182146.png "null")

进一步跟进 `loadView()` 以及 `buildView()`，这些方法的业务意义都比较好理解，先 create 一个 View 视图，再将其 load 进来，最后再 build。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182150.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182152.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182154.png "null")

在 `buildView()` 方法当中，先通过 `this.instantiateView()` 的方式 new 了一个 `FreeMarkerView` 类，又进行了一些基础赋值，将我们的 View Build 了出来（也就是 View 变得有模有样了）

继续往下走，回到 `loadView()` 方法，`loadView()` 方法调用了 `view.checkResource()` 方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182157.png "null")

`checkResource()` 方法做了两件事，第一件事是判断 `Resource` 当中的 url 是否为空，也就是判断是否存在 resource，如果 url 都没东西，那么后续的模板引擎加载就更不用说了；第二件事是进行 `template` 的获取，也可以把这理解为准备开始做模板引擎加载的业务了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182160.png "null")

跟进 `getTemplate()` 方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182162.png "null")

首先做了一些赋值判断，再判断 Template 的存在，我们跟进 `this.cache.getTemplate`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182165.png "null")

这里从 cache 里面取值，而在我们 `putTemplate` 设置模板的时候，也会将至存储到 cache中。

跟进 `getTemplateInternal()`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182168.png "null")

先做了一些基本的判断，到 202 行，跟进 `lookupTemplate()` 方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182173.png "null")

这里代码很冗杂，最后的结果是跟进 `freemarker.cache.TemplateCache#lookupWithLocalizedThenAcquisitionStrategy

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182175.png "null")

代码会先拼接 `_zh_CN`，再寻找未拼接 `_zh_CN` 的模板名，调用 `this.findTemplateSource(path)` 获取模板实例。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182178.png "null")

这里就获取到了 handle 执行返回的模板视图实例，这里我 IDEA 没有走过去，就跟着奶思师傅的文章先分析了。

`org.springframework.web.servlet.DispatcherServlet#doDispatch` 流程

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182185.png "null")

handle 执行完成后调用 `this.processDispatchResult(processedRequest, response, mappedHandler, mv, (Exception)dispatchException);` 进行模板解析。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191972-1669182189.png "null")

调用 `view.render(mv.getModelInternal(), request...