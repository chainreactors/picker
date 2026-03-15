---
title: LeakyLooker：一组允许利用Google Cloud数据的高危Looker Studio漏洞
url: https://mp.weixin.qq.com/s/Hmn55aV81YkzArQMYi9_Cw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:28:59.444397
---

# LeakyLooker：一组允许利用Google Cloud数据的高危Looker Studio漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibcp0uPSeXUonXImjMRe687FtJ2FqgAIPNGicb4zslmSMNIdTOjxFU7J2uQvMicl2NDyQypr54kSLjZkSSFxfDjdvUoCgFZ7aUnn4/0?wx_fmt=jpeg)

# LeakyLooker：一组允许利用Google Cloud数据的高危Looker Studio漏洞

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> Tenable研究团队披露了一组名为“LeakyLooker”的九个跨租户漏洞。这些漏洞存在于Google Looker Studio中，攻击者可以借此窃取或修改BigQuery、Google Sheets等Google服务中的数据。所有漏洞目前已由Google修复。

## 漏洞概述

Tenable研究团队发现了九个Google Looker Studio（前身为Data Studio）中的新型跨租户漏洞，并将其命名为“LeakyLooker”。这套漏洞打破了基础的设计假设，展示了一类新的攻击方式。攻击者本可以利用这些漏洞，在受害者的服务和Google Cloud环境中外泄、插入和删除数据。

这些漏洞暴露了Google Cloud Platform (GCP)环境中的敏感数据，可能影响到任何使用Google Sheets、BigQuery、Spanner、PostgreSQL、MySQL、Cloud Storage以及几乎所有其他Looker Studio数据连接器的组织。

在Tenable报告后，Google已修复了所有问题。

* **九个新型漏洞：攻击者可通过0点击和1点击攻击，在受害者数据库上运行任意SQL查询并窃取敏感数据。**
* **跨租户数据暴露：攻击者能够访问不同云“租户”（不同公司）的整个数据集和项目。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/tbTbtBE6TibdlBh6ytOkNWXXibE6unB9YujV1guZ5Nn9UXxLpSuqQejmtm6ia11Dz1yqkpTib8nuRibXsQ0f9e45o4ECqgaHJIq0pSicYu8mZomFo/640?wx_fmt=gif&from=appmsg)

## 技术原理分析

### Looker Studio是什么？

Looker Studio是一个基于云的商业智能（BI）和数据可视化平台。通过连接Google Analytics、BigQuery或SQL数据库等各种数据源，它允许团队构建实时更新的报告。它建立在Google Cloud基础设施之上，严重依赖类似Google Docs的权限共享模型。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfqfzOIFH2aBREibSHjg600ZQTAcqkLL4cEJMJFz7KNTjCCzeZXeQK1jsWSXW6iaaHiaKNPMl3UvicM85q3V9RRLlPVLOF9JB36r5I/640?wx_fmt=png&from=appmsg)

### 所有者凭证 vs. 查看者凭证

理解这些漏洞的严重性，首先要看Looker Studio如何处理“信任”。当您将数据库连接到报告时，需要决定报告应使用谁的身份访问数据源。Looker Studio提供两种凭证模型：

* **所有者凭证：**

  报告使用所有者的权限获取数据，无论谁在看报告。数据通过所有者的身份验证令牌获取。
* **查看者凭证：**

  报告使用查看者自己的权限获取数据。这是确保人们只能看到被允许内容的最安全方式。每个查看者必须提供自己的身份验证令牌才能看到数据。

### 打破信任边界

这项研究的核心在于认识到这两种路径创建了两个截然不同的“信任边界”，可以被独立攻击。目标是孤立这些机制来突破平台：

* **攻击查看者凭证（1点击路径）：**

  寻找方法来操纵报告，迫使查看者在不知情的情况下执行他们有权限的查询或操作数据，并可能将结果发送给攻击者。这需要受害者与恶意链接交互，因此被归类为1点击攻击。
* **攻击所有者凭证（0点击路径）：**

  这里存在真正的“架构性缺陷”。如果我们能直接与设置为使用所有者凭证的报告后端通信，就能够以报告所有者的身份行事。通过向公共报告或共享报告发送精心构造的请求，攻击者触发Looker Studio服务使用所有者的身份获取或操纵数据。这完全在服务器端发生，不需要受害者点击任何东西。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeMAUib7KtIG7FpLOpwHCuJKO5Un0zn8mY1Zmxl8TZJxciaibFAOib2VdoCvCPwZVUbq3jnxfFeLucUV4qOtBeNFK3ggHw1wuwvIEE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibfly8RSJvGtfibhGUvVNf6tfCgRyfanEprduNUqicp5uHL8xgOG80QRbrjCm6B8srqWuF2ia5QPGWicFUyCvSszQxUia1EXbmoRUId4/640?wx_fmt=png&from=appmsg)

### 漏洞剖析

#### 漏洞 #1：别名注入（跨租户未授权访问 - 0点击SQL注入，针对数据库连接器）

我们观察报告加载时的网络流量，发现了一个名为`batchedDataV2`的HTTP请求。Looker Studio会为每一列生成唯一的别名，如`qt_1spiqerwsd`。问题在于，后端将这些用户可控的字符串直接拼接到实际作为BigQuery作业的实时SQL语句中：`SELECT column AS [USER_CONTROLLED_ALIAS] FROM table...`。

攻击者可以“跳出”别名字符串，从而劫持整个查询。Google设置了一些缓解措施（例如将点`.`替换为下划线`_`，剥离空格）。我们通过利用一些SQL特性绕过了它们：

* **绕过“无空格”：**

  使用SQL注释`/**/`，SQL引擎将其视为空白，而过滤器会忽略它们。
* **绕过“无点”：**

  使用BigQuery自己的SQL脚本功能，通过`CHR(46)`（点的ASCII码）和`CONCAT()`在过滤器查看输入后动态构建项目路径。

攻击者可以搜索公开的Looker Studio报告，或访问使用这些连接器的私有报告，完全劫持报告所有者的整个数据库，进行读取、写入、更新和删除操作。

#### 漏洞 #2：粘滞凭证（跨租户未授权访问 - 0点击SQL注入，通过存储的凭证）

第二个发现是Looker Studio处理“复制报告”功能时存在根本性的逻辑缺陷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibe5s23pTdaqVeHfiacuprpL0AsiaCkRXONB7QmnAEXnPozAxXuRKe6IM51GmuIR1mPjXHnX8lh9RcVO7Hx3xn6rMXbMia2icsiaJQfA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeCj65Za3DWcK1qy7pMbiayAVRM7OLXlyQficBSJxhGM56KwRRf3e4ibj6gnKL1sLlaYEWibezYAAgkLxhe6avByjgIgeosBwJo7uw/640?wx_fmt=png&from=appmsg)

对于基于JDBC的数据源（如PostgreSQL或MySQL），用户需要输入凭证以将数据源附加到报告。当您复制报告时，附加的数据源会被克隆并创建到新副本中。

我们发现，对于这类JDBC数据源，克隆的数据源在复制到新报告时保留了其凭证。问题在于，复制报告的用户现在是新报告副本的所有者，他们可以访问作为查看者时无法访问的功能，其中之一就是管理报告的数据源并对其运行自定义查询！

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcCssLibvhMicslRbCvsk4sXic8bqrnkEDaccBicl8ASzasCoXiacZjibVZibEj6qKRmewAibGKacoGAqOXYgqAoqF3A1ZriaibwpySXl8q4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfoGm4rZCQMysE5pKj3pcZTw3OlOeSwSsNCKYYDeAuDlreAsm59Hu8NsvgAOhL0j9jktk8xv90s7o9lc5FIbrDSRUibVCdBcM5o/640?wx_fmt=png&from=appmsg)

令人担忧的是，作为攻击者，我们无需重新验证那些我们不知道的数据库凭证，因为后端保留了受害者原始报告中的凭证。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibejou0O1fmgMhVVX7cWey3xuicLHoJARZaRRc6F5Wmic5Yj2TbRXiaUEGPklnGLADic4bhyHIXlQ5dIFvCboZWa5qvu3SVT17rT9kU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe6pZ4XIBGjlPVXdwtbVPlBW2LVoSiaHDYpicfmHuwjHcslfpxkcug2rCeO3MeicxqHzGOxbNh6Sapia4gc025EUcvLI9v2m1y9Gwk/640?wx_fmt=png&from=appmsg)

#### 漏洞 #3：通过原生函数对BigQuery的跨租户SQL注入（1-click）

一旦确定查看者的凭证可以作为1点击路径被利用，攻击路径就很清晰了：如果我们能迫使受害者的浏览器在他们自己的身份下执行我们的代码，平台的安全模型本质上就会为我们服务，而不是阻止我们。

**攻击的隐藏设置：** 使用网络代理工具拦截连接数据源的HTTP请求（如`createBlockDatasource`和`publishDatasource`），并修改它们，将我们的项目详情替换为跨租户受害者的详情。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfibKwggzp4icgEsmO3IH4poLLk6A3xFoHo7HSaAQoUicQjcT65UhupVibeGhFWojbbvGKBGMWNyaaQ9Tib87C7G0ia6QHccM3PZVxHU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdllaLe0qZ4MnsCROJPRw5PribLKFPYM837EXn2cjnwiaiaQGXkjG4nibtLs56fn63pPaJ3AUobicVPzH0htwQBtDJCyx6nnWQvSorM/640?wx_fmt=png&from=appmsg)

**利用原生函数和维度：** Looker Studio的`NATIVE_DIMENSION`功能允许在字段中直接写入原始SQL，并在报告加载时针对数据库运行。这成为了我们的切入点。

Google的保护机制会检查`SELECT`和`FROM`等特定关键词。我们通过将禁用词放入SQL注释中来绕过过滤器：`SEL/**/ECT`和`FR/**/OM`。底层的BigQuery引擎会忽略注释并执行命令。

**构建超级负载：** 我们可以在`NATIVE_DIMENSION`字段中编写一个完整的程序，利用BigQuery的多语句脚本支持，包含变量声明、查询受害者模式（使用`INFORMATION_SCHEMA.COLUMNS`）、循环遍历所有内容。

**利用跨租户日志进行盲数据外泄：** 我们无法将窃取的数据直接插入到我们自己的表中。因此设计了一个技巧：在我们的项目中创建一系列空白的、可公开访问的BigQuery表（命名为`exfil-a`、`exfil-b`等）。在注入的SQL中，当我们从受害者数据中发现一个字符时，会执行一个选择该表的查询。虽然读操作不会返回数据，但会在我们的Google Cloud项目中生成日志条目。通过监控这些日志并拼凑表访问序列，我们可以重建受害者的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfaicibGz8iaCpFAOvCUcPoSAuq35h8ZI9pRByvicVf6fOojVIV0gMYwYK8wKpx8MoxFHJA16XWKsusV2bib3EicY7icMibwxNL4iaOL9z0/640?wx_fmt=png&from=appmsg)

## 影响范围

这些漏洞暴露了GCP环境中的敏感数据，影响范围极广。任何使用以下Google数据连接器的组织都可能受影响：

* Google Sheets
* BigQuery
* Spanner
* PostgreSQL
* MySQL
* Cloud Storage
* 几乎所有其他Looker Studio数据连接器

## 攻击复现流程

攻击者可以创建一个恶意的Looker Studio报告，分享给受害者（甚至可以取消勾选“通知”框以隐蔽），或将其嵌入到网站上。

当受害者打开报告（或访问恶意网站）时，他们的浏览器会：

1. 连接到我们的报告。
2. 使用他们自己的凭证访问我们秘密配置为指向他们BigQuery的数据源。
3. 执行我们的`NATIVE_DIMENSION`计算字段以加载我们附加的受害者数据源。
4. 我们注入的多语句脚本运行，系统地提取他们GCP项目中所有BigQuery表和列名，然后提取所有数据。
5. 每个提取的字符触发对我们一个公开外泄表的“ping”操作。
6. 我们监控自己的GCP日志，重建受害者的整个数据库，而受害者从未看到警告或授予明确权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeEkfDS2rq2AGuUqXn6yHKtWkserGX4XqZdCZgibR29icgH3iajcXiaNBcia7lUMQX0KXyAzRtYUj5V9KmiaoRzFRmEuIUKBhBQC7pD0/640?wx_fmt=jpeg&from=appmsg)

## 修复建议与缓解措施

由于所有Looker Studio实例都由Google管理，客户无需采取任何行动，Google已在全球范围修复这些问题。

为限制此类攻击的暴露面，建议始终审计谁拥有对报告的“查看”访问权限（无论是公开还是私有），将BI连接器视为攻击面的关键部分，并且不再允许服务访问不再使用的连接器。

要限制对Looker Studio连接器的访问，应遵循以下指南：Google官方指南（https://docs.cloud.google.com/looker/docs/studio/remove-or-reconnect-looker-studios-access-to-your-google-account）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdELXcR2iaBrYAB0LxbgZfe0hb5pufwomwwsWAz2Miayg94gJJYjZiaXnACAGTeNl2iaicKHTgHkNR90tBvgZBiajhszk7Xx7vDZx37o/640?wx_fmt=png&from=appmsg)

### 参考资料

[1] https://docs.cloud.google.com/looker/docs/studio/remove-or-reconnect-looker-studios-access-to-your-google-account

[2] https://www.tenable.com/blog/leakylooker-google-cloud-looker-studio-vulnerabilities

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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