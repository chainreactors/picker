---
title: 第101天-Java安全攻防：从SPEL、SSTI注入到SpringBoot框架漏洞，一篇通关！
url: https://mp.weixin.qq.com/s/j8WQLe4JNp9WdLyz1KUjCA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:22:30.106158
---

# 第101天-Java安全攻防：从SPEL、SSTI注入到SpringBoot框架漏洞，一篇通关！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Byhdgj3e9quFbib2BbLKOyhbUtNM17jIYrkoRicMEfhmCiafJD2EqlAibAOXk1CFiaajQbaAcMryV88g8EouicupMURxB5vAvOeGibT8b5sEGE6k6U/0?wx_fmt=jpeg)

# 第101天-Java安全攻防：从SPEL、SSTI注入到SpringBoot框架漏洞，一篇通关！

原创

Сяо Яо
Сяо Яо

AlphaNet

![]()

在小说阅读器中沉浸阅读

大家好，我是Сяо Яо！欢迎来到今天的Java安全攻防专题。在Web应用开发中，Java以其强大的生态和稳定性备受青睐。然而，便利的框架和功能背后也可能隐藏着安全风险。今天，我们就来深入探讨几个常见的Java安全漏洞：**SPEL表达式注入**、**SSTI模板注入**以及**SpringBoot框架**中的一些典型安全问题。无论你是Java开发者还是安全爱好者，这篇文章都将为你提供一份清晰、实用的学习指南。

---

### 🧐 是什么：揭开漏洞的神秘面纱

在深入攻防之前，我们首先要理解这些漏洞到底是什么。

#### 1. SPEL 表达式注入 (Spring Expression Language Injection)

SpEL是Spring框架提供的一种强大的表达式语言，它允许在程序运行时查询和操作对象。但如果开发者不加过滤地将用户输入作为SpEL表达式的一部分来执行，攻击者就可以构造恶意的表达式，从而实现远程代码执行（RCE），这便是**SPEL表达式注入**。

```
// 示例：一个可能存在SPEL注入风险的代码
SpelExpressionParser parser = new SpelExpressionParser();
// 如果userInput是从前端接收且未经过滤的参数，就可能导致漏洞
Expression expression = parser.parseExpression(userInput);
expression.getValue();
```

#### 2. SSTI 模板注入 (Server-Side Template Injection)

SSTI，即服务器端模板注入，发生在服务端将用户输入作为模板内容的一部分进行渲染时。如果模板引擎没有正确处理这些输入，攻击者就能注入恶意的模板指令，最终可能导致服务器被控制。

常见的Java模板引擎包括：

* 🍃 **Thymeleaf**

* 💨 **Velocity**

* 🐴 **FreeMarker**

> 💬 **小提示**：不同的模板引擎有不同的注入语法和利用方式。如果你对其他语言的SSTI感兴趣，可以参考这篇文章。

#### 3. SpringBoot 框架安全问题

SpringBoot极大地简化了Java应用的开发，但其“约定优于配置”的特性也带来了一些常见的安全风险。

* **Swagger UI 接口泄露**：Swagger是流行的API文档生成工具。若配置不当，未设访问权限，会导致整个项目的API接口暴露给未经授权的访问者，攻击者可以轻易地了解系统架构并寻找攻击点。

* **Actuator 端点泄露**：Actuator是SpringBoot提供的监控和管理工具，它通过HTTP端点（如 `/actuator/env`, `/actuator/heapdump`）暴露应用的内部信息。如果这些端点可以被公网访问，将造成严重的信息泄露。

---

### 🤔 为什么：探究漏洞的成因与危害

理解了“是什么”，我们再来看看“为什么”这些漏洞会发生，以及它们会带来多大的危害。

* **核心原因**：**信任了不该信任的输入**。无论是SPEL、SSTI还是其他注入类漏洞，其根源都在于服务端程序将用户的输入数据当作了代码或指令来执行。

* **巨大危害**：

  + **远程代码执行 (RCE)**：攻击者可以在你的服务器上执行任意命令，相当于把服务器的控制权拱手相让。

  + **敏感信息泄露**：通过Actuator的 `heapdump` 或 `env` 端点，攻击者可以获取数据库密码、云服务密钥、内部接口地址等核心机密信息。

  + **业务逻辑破坏**：通过暴露的Swagger接口，攻击者可以随意调用系统功能，如删除数据、篡改用户信息等，对业务造成直接冲击。

---

### 🛠️ 怎么做：漏洞的发现与利用（攻防演练）

理论结合实践，我们来看看在真实的攻防场景中，如何发现和利用这些漏洞。

#### 1. SpringBoot 框架漏洞扫描与利用

**第一步：识别框架**
在渗透测试中，首先要识别目标是否使用了SpringBoot框架。常见的特征包括：

* 页面上标志性的绿色叶子图标 (favicon.ico)。

* 访问不存在的路径时返回的默认“Whitelabel Error Page”。

**第二步：自动化扫描**
使用专门的框架漏洞扫描工具可以快速发现已知漏洞点。

* **SBSCAN**: `https://github.com/sule01u/SBSCAN`

* **spring-scan**: `https://gitee.com/team-man/spring-scan`

* **SpringBootVul-GUI**: `https://github.com/wh1t3zer/SpringBootVul-GUI`

**第三步：Actuator 泄露利用**
如果扫描器发现或手动探测到`/actuator`端点开放，就可以进一步利用。

* **Heapdump 内存转储分析**

  1. 访问 `/actuator/heapdump` 端点，下载 `heapdump` 文件。这是一个巨大的内存快照文件。

  2. 使用专业工具从 `heapdump` 文件中提取敏感信息。

     + **JDumpSpider**: `https://github.com/whwlsfb/JDumpSpider`

     + **heapdump\_tool**: `https://github.com/wyzxxz/heapdump_tool`

     + **JDumpSpiderGUI** (图形化界面): `https://github.com/DeEpinGh0st/JDumpSpiderGUI`

  3. 通过分析工具的输出，可以快速定位到数据库连接信息、账号密码、API密钥等。

#### 2. Swagger UI 接口泄露利用

**第一步：发现 Swagger 页面**
常见的Swagger UI路径包括 `/swagger-ui.html`, `/swagger/index.html`, `/api/docs` 等。

**第二步：解析与测试**

1. 找到Swagger UI页面后，通常会有一个 `swagger.json` 或 `v2/api-docs` 链接，这是API的JSON描述文件。

2. 使用 **Apifox**、Postman等工具导入这个JSON文件，可以一键生成所有API的测试请求。

3. 在Apifox中，你可以系统地、自动化地测试每个接口，寻找未授权访问、越权等漏洞。

---

### 📝 总结：核心要点回顾

今天我们学习了Java中三种常见的安全问题，让我们来总结一下核心要点：

1. **SPEL & SSTI 注入**：本质都是将用户输入当作代码执行。防御的关键在于**永不信任用户输入**，对所有传入的数据进行严格的校验和无害化处理。

2. **SpringBoot 安全**：便捷性不应以牺牲安全为代价。

   * **Actuator**：在生产环境中，应关闭不必要的端点或通过Spring Security等安全框架进行保护，切勿暴露在公网。

   * **Swagger UI**：同样需要添加访问控制，只对授权的开发或测试人员开放。

3. **攻防思路**：从**信息收集**（识别框架）到**自动化扫描**（发现端点），再到**深度利用**（分析Heapdump、测试API），层层递进，精准打击。

---

今天的分享就到这里！希望这篇文章能帮助你更好地理解Java应用中的安全风险。

🤔 **最后，留一个思考题**：在你的项目中，是否也使用了Actuator或Swagger？你又是如何保护它们的安全的呢？欢迎在评论区留言讨论！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

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