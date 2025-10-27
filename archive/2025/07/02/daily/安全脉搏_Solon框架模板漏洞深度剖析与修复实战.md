---
title: Solon框架模板漏洞深度剖析与修复实战
url: https://www.secpulse.com/archives/206316.html
source: 安全脉搏
date: 2025-07-02
fetch_date: 2025-10-06T23:28:39.013033
---

# Solon框架模板漏洞深度剖析与修复实战

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

# Solon框架模板漏洞深度剖析与修复实战

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-07-01

15,687

## 前言

分析发现 Solon 框架在3.1.0版本上存在一个有意思的模板漏洞，对这个漏洞进行简单分析后，发现整个漏洞的利用链是非常有意思的。同时发现最新版的修复方式过于简单，询问 AI 后，AI 也认为修复也是不完善的安全修复，于是进行一系列的绕过尝试，最后还是没有利用成功，简单进行分享。

## 环境搭建

### Solon 框架简介

Solon 是一个轻量级的 Java 应用开发框架，类似于 Spring Boot ，但更加轻量。支持多种模板引擎，包括 Beetl、FreeMarker、Velocity 等。在模板处理方面，Solon 采用了灵活的渲染器映射机制，也是出现这个漏洞的关键原因。

### 测试环境搭建

<https://solon.noear.org/start/build.do?artifact=helloworld_jdk8&project=maven&javaVer=1.8>

可以下载 solon 的项目模板 并进行修改

修改一下 pom.xml 文件 设置 solon 的版本为 3.1.0

将原本的视图插件 solon-view-freemarker 替换为以下的任意一种

```
<dependency>
    <groupId>org.noear</groupId>
    <artifactId>solon-view-enjoy</artifactId>
</dependency>

<dependency>
    <groupId>org.noear</groupId>
    <artifactId>solon-view-beetl</artifactId>
</dependency>

<dependency>
    <groupId>org.noear</groupId>
    <artifactId>solon-view-thymeleaf</artifactId>
</dependency>

<dependency>
    <groupId>org.noear</groupId>
    <artifactId>solon-view-velocity</artifactId>
</dependency>
```

‍

在 DemoController.java 中 添加代码 并启动运行

```
    @Mapping("/templates")
    public ModelAndView templates(Context ctx) throws IOException {
        ModelAndView modelAndView = new ModelAndView(ctx.param("templates"));
        return modelAndView;
    }
```

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7e9de840-c3c3-48fe-bdc9-7112f1839fa3.png)

## 漏洞验证与分析

### 漏洞验证

我们选用视图插件solon-view-velocity，不同的视图插件对跨目录的处理有所不同，之后会对此进行详细解释

```
<dependency>
    <groupId>org.noear</groupId>
    <artifactId>solon-view-velocity</artifactId>
</dependency>
```

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/f501fa3e-38bd-42ca-9bd4-bc395e6e1c05.png)

可以看到传入的参数通过 ../ 实现了跨目录的文件读取并将内容解析到页面上

### 核心调用链分析

通过调试对这个漏洞进行分析

遇到这种情况有一个小的 tips 我们可以通过尝试加载一个不存在的文件，这样 idea 的控制台中会输出相对详细的调用链，方便我们下断点进行调试分析。

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/b1d9d08f-56fc-4b9c-b310-f2b884cdf269.png)

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/4e01dc20-4711-44a6-94d1-fa785e5dde96.png)

org.noear.solon.core.handle.RenderManager#render

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/d95249b5-dd06-4e5e-8e95-fdeb61ffbe7d.png)

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/eb7c9eff-b110-4374-ad77-7a157939e050.png)

这里会根据文件后缀来选择视图插件，如果没有匹配的就选择用默认渲染器来处理

org.noear.solon.view.velocity.VelocityRender#render

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/5733c9a7-695e-4e55-a794-4e2af33e564c.png)

org.noear.solon.view.velocity.VelocityRender#render\_mav

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/edec2dd0-b01f-4fcc-b3a2-62f8ef36babc.png)

org.apache.velocity.runtime.RuntimeInstance#getTemplate(java.lang.String, java.lang.String)

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/0eae6f34-8691-4df7-a708-6634e6e06760.png)

org.apache.velocity.runtime.resource.ResourceManagerImpl#getResource

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/3fbe072c-7e6e-4ec3-b7e5-9ba3cc9b5ddb.png)

‍

整体流程顺下来应该是

用户输入 → Context.param() → ModelAndView() → RenderManager.render()→ 模板引擎处理

在模板引擎处理之前没有对模板文件的路径进行处理和限制，这样一来如果模板引擎处理的时候没有对模板文件的路径进行处理时，就会产生任意文件读取漏洞。

我们可以尝试看看利用别的视图插件看看效果如何。

### solon-view-freemarker 为什么不可以

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/e77332bb-f3d5-4633-8bbd-d75cf20e359b.png)

我们看到 freemarker 对 模板文件的路径进行了处理，不允许跨目录的访问

org.noear.solon.view.freemarker.FreemarkerRender#render

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/bb3939c6-2c8d-400b-acf1-b686737c5f18.png)

org.noear.solon.view.freemarker.FreemarkerRender#render\_mav

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/94782af3-12be-4f6d-b180-44fe5fa06dcd.png)

freemarker.template.Configuration#getTemplate(java.lang.String, java.lang.String)

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/06d5f668-b0c9-44bc-9505-a7822a83d546.png)

freemarker.template.Configuration#getTemplate(java.lang.String, java.util.Locale, java.lang.Object, java.lang.String, boolean, boolean)

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7790130f-c007-4fd6-a906-1c46a65269b3.png)

freemarker.cache.TemplateCache#getTemplate(java.lang.String, java.util.Locale, java.lang.Object, java.lang.String, boolean)

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/4f92e49b-ee06-4f12-97ee-cf682ae512c3.png)

调用 `name = templateNameFormat.normalizeRootBasedName(name);` 来对传入的模板文件名进行处理

freemarker.cache.TemplateNameFormat.Default020300#normalizeRootBasedName

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/b06a305a-8272-4145-86e1-799c81f57c4b.png)

对传入的参数进行规范化处理，以确保安全并处理路径中的特殊序列。

## 漏洞修复

org.noear.solon.core.handle.RenderManager#getViewRender

![image](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

我们注意到修复方式是添加了这一部分代码

```
 if (mv.view().contains("../") || mv.view().contains("..\\")) {
            // '../','..\' 不安全
            throw new IllegalStateException("Invalid view path: '" + mv.view() + "'");
        }
```

看起来处理方式简单粗暴，实际上是非常有效的

用户输入 → Context.param() → ModelAndView() → RenderManager.render()→ RenderManager.getViewRender()`安全检测`→模板引擎处理

在模板引擎处理之前就添加了对传入路径的检测，一次 url 编码无法绕过，两次 url 编码虽然可以绕过检测，但是实际处理时，找不到文件所...