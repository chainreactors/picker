---
title: [工具推荐]新一代webshell管理工具默连(morelian)
url: https://mp.weixin.qq.com/s/AGKETOvMnzHOf0SLKzCyaA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:31.878115
---

# [工具推荐]新一代webshell管理工具默连(morelian)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboT44Ux76SUmfCRzglWOadBSct8UUQvv4pSh2A2Rd2zWeHCgNeuPXarITU2UGdfPTiaHH5lg0tlCy0FcaRS8L2M53glEDS3f6siao/0?wx_fmt=jpeg)

# [工具推荐]新一代webshell管理工具默连(morelian)

doki-byte
doki-byte

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

前言

默连，面向 Webshell的目标管理与远程会话：本地保存配置、连接目标，并在会话中提供文件、命令、数据库及 Godzilla 兼容插件等能力。

**支持GUI运行，同时也支持后端运行，通过浏览器进行访问控制**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboToibLqF61FPk0D1LeCVFWNiaMNKBWkhwLnjGJGURmwWo16M91tIabVbmcB1pZib4Fr5GEhT82nfauebvKiah1LA4O9x0FQ4Jn8848/640?wx_fmt=png&from=appmsg)

功能概览

目标与连接

- 分组与列表：按路径式分组管理目标，支持分页、搜索与右键快捷操作。

- 存活检测：单目标「测试连接」与导航栏「批量测试存活」（可后台进行）。

- 多协议握手：按目标配置的 Payload、加密器与 URL 建立会话；会话内可切换 UTF-8 / GBK等编码。

- 代理：支持为单目标配置 HTTP / SOCKS 等代理类型（以界面与配置为准）。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQRWygiaVSUGoFWEVickPM3K5Eochqx68c6AAhibENib2BZnQdjqSb2u9U1cQ0meLOHHPWXic5pdCSn9NV2oOe3UwTqFT6A6Wlqy1jg/640?wx_fmt=png&from=appmsg)

载荷与生成

- GenerateShell / 生成：按密码、密钥、载荷类型、加密器生成服务端脚本；可配置 Header Gate（指定 Header 名与值）、浏览器伪装（模板与变种）、以及与 Tomcat 版本相关的 javax / jakarta 等选项。

- 连接脚本导出：从目标列表生成/导出连接所需脚本（与导航「生成连接脚本」等入口配合）。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRHCibV5R8Ge5ibzWLlKrzyt2PdNRWtkBqTk1J36MVwZVMhRV0J4ia5UZGdaTmtX8kXMYaot5SKEqsyVX6dUhSiaeicldw0BIm2zR8I/640?wx_fmt=png&from=appmsg)

 会话能力

- 命令与终端：统一执行命令、交互式终端等（合并原「执行 / 虚拟终端」等能力）。

- 文件管理：远程文件浏览与操作。

- 基础信息：会话与目标基础信息展示。

- 笔记：会话侧笔记。

- 数据库：数据库相关操作面板。

- 网络：如 `netstat` 等网络信息查看。

- 标签管理：自定义标签顺序与显示，支持「复制标签配置」等。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTibSfFUrQ0erfHToUIPvk6rW83hiccQWZ73czeVLX5ic5iaavPYT0V9MOicmibd1MbI4db5BC45qgFhibgcMhny1W0iaFmh7icRrVaCF1Y/640?wx_fmt=png&from=appmsg)

* ### 会话能力

+ **命令与终端**：统一执行命令、交互式终端等（合并原「执行 / 虚拟终端」等能力）。
+ **文件管理**：远程文件浏览与操作。
+ **基础信息**：会话与目标基础信息展示。
+ **笔记**：会话侧笔记。
+ **数据库**：数据库相关操作面板。
+ **网络**：如 `netstat` 等网络信息查看。
+ **标签管理**：自定义标签顺序与显示，支持「复制标签配置」等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTJkicibwtLzS3Lpz6ESS6KsbaQVibOHekZicaAXb2kicYXTv10iadiar4icrnFBbCPELIXGoS2m7sichmIYKXMjviaIzoCE5tebnXQXAops/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTrKvBI33JWMarxH3YBEyQLL4Q4DYkKkk1gauxg6rAfoYniafNk7iaMVeYAxMhnxXNwYaHsTz4RMtGLCvFGSzgmxjXP4ia0TpuGrY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCBf3pXaicnhic3OXibuOPGNPSKUyMenaeEOaxallGbgHvy7tVFNWricgyh6vxG3X5sdAWHAzg4Z3pPFyyOZTGqw9Ajt4IUuICT0w/640?wx_fmt=png&from=appmsg)

运行模式

- 桌面模式：默认启动 Wails 窗口，数据存放在用户配置目录下的本地 SQLite。

- Web 模式：使用命令行 `-web` 在本地启动 HTTP 服务，用浏览器访问界面（适合仅需浏览器、或与其它工具联动）。监听地址可省略（默认 `127.0.0.1:34116`），也可传入端口或完整 URL。

如何运行

GUI运行

直接双击就行

Web 模式（浏览器）

在已构建的可执行文件或开发构建上，使用例如：

```
# 默认监听 127.0.0.1:34116./morelian -web
# 指定端口./morelian -web 8801
# 或使用 -web= 形式./morelian -web=:8801
```

* Windows 下将 `./morelian` 换成 `morelian.exe` 即可。

## 测试效果

### D盾效果：

php 所有版本无感，但是其余版本还是会警告，下一版本优化

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTASFgNO8BM8Z2icCUyEaHftsW9CO0eSvdc0FFGEbia77Q2lica5ENQU1bgKGK18UTf6IqupW8YpoRZGKauArm48MUuwElFzy7fOc/640?wx_fmt=png&from=appmsg)

阿里云效果:

借助ai，目前感觉还是很哇塞的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRYuPHgSIGXfgZM99TG59KN3JUEib5jtwdonfnS7NzFwDSicadhqTSLIEuMErj4vvrgz15EWCKVDfOlhqK5D0IwXjOMPZMBBO6QQ/640?wx_fmt=png&from=appmsg)

工具地址

```
https://github.com/doki-byte/morelian
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**POC库****&&更新适配afrog&&nuclei&&dddd的POC&1day/Nday等&&******dddd二开******工具[助力渗透测试&&红蓝攻防]**

**工具截图**

**![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRLmmY4kF0AaQjAJUQzH1sAExGoE7AmDJZXcEgdnKuRkpgZ9xYflY0UxtVkrP4HicDfvCWibXY86fAjH1E0TDJ5YqatD9fjZrUYk/640?wx_fmt=png&from=appmsg)**

**实战效果**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSKqLXNcOPE07xOwOUCjRGuFphopPumW9RaticmNCuEUXu52GtdTTfpTUicrBj80kMcZzJsnps3abyvXIvLHEIhvMoXUApOqZCe4/640?wx_fmt=png&from=appmsg)

**poc库【后续持续更新】**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTG9Lyp44aFffUOxQKtHjToGfqFWTjswYft0VtAPINtV5MqmrTTj8GWrVb6yowvHURubPgOqdribmibWEb0Fcj3YdN4iahUwItcxE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRAMJIIvexOOJa5KhrsKmlsx8bkwib9SPoK72Q0OSPWR5qx67yvl8scMQ5bg8caBXZH01kM39RDnKpnWSaTicgobRmLygERGFWls/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY8wUetFibPmetZdkicr4BNvPF0cBibqyS9emwayFf6njw9kjvBvWLoFDQJY5JQDMSUqh4E/640?wx_fmt=png&from=appmsg)

云安全&AI安全

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ9qiavETNjaaX162czpNCqpw3uJqVpicbI15AXzhf5x8icmHxBdTGOgRgzNPGF3Aw2gglT4Fx09JGXYibQC6U7CQKVmoH08l3meia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRfLMPDcF7l8FiaicK20uQdqQ9jrQnlIHk3J3DPhEpPxLfNia23dOuelLicVlNsvXgvSGa9Y4NfuTqUhxBOfF0nzHngWK01icdQWIDM/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
最新漏洞查看1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFBRMa8XwYxfcZMyXicx94xSKxawPcqFia2rJKOL7fSLYXiccwHc868XxNGIQ5z7ibiaI1MNAGRrK7U6wXJTsZOCAu2I5XV1boTAL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBzdakI9XI33ReAm2dxO8vgzw3JicQmUuWCb5ayBlKR1PoQHEHFETteBnicyupwU0mXvXibfrDoyg8nSWBGoK1p2YXY3ElhcvOQ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**陌笙****纷传****圈子介****绍**

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&...