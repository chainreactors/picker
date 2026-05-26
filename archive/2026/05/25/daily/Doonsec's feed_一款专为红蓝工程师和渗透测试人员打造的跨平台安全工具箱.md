---
title: 一款专为红蓝工程师和渗透测试人员打造的跨平台安全工具箱
url: https://mp.weixin.qq.com/s/H1JazXTyLKPcZuGIcdm3OA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:48.602311
---

# 一款专为红蓝工程师和渗透测试人员打造的跨平台安全工具箱

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj55O0q87doFicS3uAic7N8ywtibfzOPG1wJXpRiaiaTDEaicxV0QMe92Mo2IXMhMiaQ9GevE5wVPpHKqSJyeDqEj8L2icIV4EQIhYCe6Xn8/0?wx_fmt=jpeg)

# 一款专为红蓝工程师和渗透测试人员打造的跨平台安全工具箱

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 项目简介

**ChiXiao (赤霄)** 是一款专为红蓝工程师和渗透测试人员打造的现代化、跨平台安全工具箱。它集成了工具管理、智能研判、资产测绘与攻防辅助等核心功能，旨在解决传统渗透测试中工具分散、环境配置繁琐、协作效率低下等痛点，构建个人专属的“数字化武器库”。

### 功能模块

按左侧导航划分，当前主要模块如下（与你在界面上看到的菜单一一对应）：

* **仪表盘：展示版本信息、更新状态、常用入口和最近操作，作为启动后的默认首页。**
* **工具箱：统一管理本地 GUI/CLI 工具，支持添加/编辑/分类、使用次数统计与按热度排序，一键启动常用渗透工具。**
* **信息收集：集成空间测绘、端口扫描、目录扫描、Web 指纹识别、Google Hack 等能力，用于前期资产摸排与面宽收集。**
* **漏洞管理：围绕 Nuclei 生态提供 POC 管理、扫描任务编排与 请求重发 (Repeater)，覆盖从 POC 维护到验证复现的完整闭环。**
* **攻防赋能：包含反弹 Shell 生成器、攻击载荷库、JWT 攻防平台 (JWTAttack)、Java 编码辅助、地图 API 泄露检测、默认密码查询等常用攻防小工具。**
* **备忘录：用于记录渗透过程中的笔记、任务清单与命令片段，支持分组与搜索。**
* **网址导航：内置安全相关网站导航，可自定义收藏、编辑与分组，方便日常查阅情报与文档。**
* **应急响应：提供 Web 日志分析、流量分析 (PCAP)、Windows 系统日志分析 (EVTX)、Webshell 检测与代码审计等能力，支持规则与 AI 结合的研判流程。**
* **辅助工具：包括漏洞文库、仓库/字典更新、数据对比、CyberChef、IP 与文本处理、随机密码/账号生成等效率工具。**

### 核心功能

### 智能工具箱 (Smart Toolbox)

* **统一入口：集中管理 Nmap、Burp Suite、sqlmap、浏览器插件等各种外部工具，一键启动。**
* **环境隔离：支持为不同工具配置独立的 Java / Python / 自定义启动命令，降低环境污染与版本冲突风险。**
* **快速检索：支持按名称、标签、类别搜索和按使用频次排序，高效定位目标工具。**

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6iblPp6mrkyEIqjYibZYzXIzS1dU4bp61UIVtEXGe88zibcEAo0JLTGBqnyrpME6gNbgZcGUK0mUFibHzPFEl7uMGEteFcjrrFEFIA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

设置工具路径，方便后面fzf模糊搜索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic68oqsYWibCE4H8tvxyewQzopy3IuaAcTeesGKWsnRHL5bMAnKGvQqmdDcFrlXkyFAgiabWXfmlyCEPFs1kf6EMjnAqqUL2vPzkW8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ibeAUgvZiabXF5jdYRU2JRw4uerRZhUMHKOV3WInrrII2CY5JCL2llgsn4s42EiaQW9qems0BPP9VMia4tOkn3iczeXMcbuK5HNj2M/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69DSVe8ofe80GibHPd1JrxNqRPmNqj6O0DWTucKKXSogdvkRIGP6sSaayQKxBk85j71SicYLODCribvzV3IOJqqN1aYKvnEtm7hVU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

### 漏洞管理与 POC 编排

* **POC 目录管理：从本地目录载入 Nuclei POC，解析元数据（名称、标签、严重级别、作者等）并以表格形式展示。**
* **扫描任务中心：基于选中的 POC 一键发起扫描任务，查看实时进度与历史结果。**
* **请求重发 (Repeater)：内置类 Burp Repeater 的请求调试面板，支持多标签、多次修改与对比响应，用于手工验证漏洞与调试 POC。**

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69zavcobzticZhNA8dKc89qasDYZnWhFuIYTK9hOnfctLv4ZCPETvYepWkZp0FibFwCvUkTnuXI6WQSQypvDMTwFJgg6icuwFsJ3I/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69WFyo9sZ3xOhyhhibnMB5lGvQTQVfPK9nIhBvrbya7sj6Cj68J5py55NRkRnImaqjUNz2DsiaVBMJ1pho9RyKTqA52Tf6BuvAug/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69G3QC0dOwCuIfZbClayPu4gtP6Wczzc5MfRJaOwP5TEdkJic5xfCaq7iaVIVQpQgvFDosgosEsM2BiascFwO6msmwczXwMpq7crg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

扫描以 【无镜 U .lab】CVE-2025-55182 dify环境 rce 漏洞环境做演示。

选择一个POC进行扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69L0LiaLdf94cRx7Zs3AuOrkaUuUtXoJAfqecOZcZFtlcxBmY15o12DTy3UqRUZqvXwzKHpvEft4sLORcIQiaIP80J9AlQ1KNicdQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ib5v2YgQGE68JQib3ic2SfQ9MDDFzKkXARM4RbFfBC7R0vVHYI8KRkiaffjwBQpZFqicaAJ3lTFtYcV1Fd0kHNn86Juu2kk4MQZdKU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

点击查看可以 查看具体的请求与响应数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ib0LGReoz04zia59JBJRQUCH2xZmtAPCiboH7OgaNtNMRoZ0CAVAryG2yu5vVLxXEsb8wByiarlDLicRGXCS52E4iaiarHWibiaM8ZVWsg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

可以与请求重放功能联动，点击发送至Repeater

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic68bjJDscf7jQ0eM4QOxmXAtdGdxNWelibdt2nDn3iaGsjm5FSIPWW4TA9kNEPecGlw2ZIqy87dxbNo18xJ749j8zPic7tEw4Rphbs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

### 攻防赋能中心 (Red Team Utils)

* **反弹 Shell 生成器：根据目标 IP/端口与环境，一键生成 Bash、Python、PowerShell、PHP、Java 等多语言反弹命令。**
* **攻击载荷库：按“攻击面/漏洞类型/攻击链”组织常见 Payload，支持查看利用步骤与复制命令。**
* **JWT 攻防平台：集成 JWT 解码与安全分析、攻击向量平台、密钥爆破、Token 编辑器与生成器，覆盖 JWT 场景的从分析到利用。**
* **编码/弱口令工具：Java 编码辅助、地图 API 泄露检测、默认密码/弱口令查询、密码/字典生成等。**

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69yViboOyMNBI5vjbmdZglSl3IQiaOmxOiaBNjAeXY0UlKrbpBJ1icut7nT6p925US17LJFckQYRLBcS6FEowQ9Wna9HdHMQFsuTcM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6icDb9ghjCPIv0FCOmaQkK8TBddyico1ib3zA5PptR2kpehKs9l6WWx9icd9iaU5qTld6DibV2NK0zicMx05C0KWOXibuQflRpTCmNTvfE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69VvsOO7E5xVFnpw2NMBo4EdVuSzALNEB8kB8d1If39GJU85reDuqF3sRwj4XHiciajIjYPvvbw5SjLCb0wIUO4IqqtdbAFVlHicQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=13)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69SibswmeGqSPdMwnJuENyficXHx1c2ibF5OEdmNs37X5LdVLbia4OTksqHwYhcsl3oUUH06KYoarNSwSusqtiayHrRlibc1MBylNMXs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ib4ZHDzhjrIZLA8fOYo05F9xa2sa20KI15ugPKImPgfDGrYI7FdUrm3HLDaQb2eYDgbt0rZ2r5ahTkiaOeYpgnlNQ0jpt9LSZS4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic694UYk8IxqClrEvkdR0ycfbBWfyL0hicThpUxUdcbAdS0AUuwiaNudPAa7Bv7u7HRxOFqibpvZ5VXxF0ZqfPzRSy57MxHZVwpXeyg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic68yNMPF1fNzV65sxc6iaTeN52xY6hRnntyekCoDgLhVzdhZicCxgRwH46aR11ia9cExZLvJwd8JWYKyicWx04CR4D9icdaXXxOgzYib8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=17)

### 信息收集与资产测绘 (Recon & Mapping)

* **多引擎空间测绘：聚合 Fofa、Hunter、Quake 等 API，统一搜索与导出资产，支持分页浏览与过滤。**
* **端口/目录扫描：提供端口扫描与目录扫描任务的配置与结果浏览接口，辅助快速摸清暴露面。**
* **指纹识别与 Google Hack：支持基础 Web 指纹识别和典型 Google Hacking 语句生成。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ibqTLDR3AEibmpfNYRGU2pkUELPZ4TlvhS8yicSrYYkNNLickicQmibo4A0jbh6x4hnp5D8ffThKOuzDHSR8WjibgumlQpMw7L2zmbib8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=18)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6icoYmjuibnocibezHGqicHywy18ksnCpJ1fbzYPq3yQ5JCObAQd503URN2knx1yf9Utn8kr6WedAg3jiaSjuEnQPNibnCktc4YcCFV4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=19)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ib5HpkTvWpYE2xLvluAoeibXuVQEpSppeWTIJ9KibkbsuLYyVjePDWTcsoklY74N2LVQQwkmiaC3djHwjBka0HOiaAed0PrESSL7icg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=20)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic68MfZNW9gmR1sgkwR4NFvxgLEU6yiawjsAW3KL7Gdc7Sd7uskUWzPWTKbhsGhm19VLW8tNBDfmB4lOVTPIECkxdPqCjIcbgmibqU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=21)

指纹识别截图预览

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic68BibMicRza10Iqp1PySByL0pick6WuLVT3geBS3rcAt6zHqlDj0XC01qAIU3bmeiaaCrpJGFwOkdeACuLs2pKwOYsHLz99gbymOQg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=22)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic68OUQCLF5ueMyAyrdhZh7voxFIP9k4E6VGoRLLPqKqEs7n2DmKkhTibaLRn04VMtO8RbcUR2GEApibibxfib5TCIoILQMMrZYRqXyc/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=23)

### 应急响应 & AI 智能研判

* **Web 日志分析：支持本地 Web 访问日志导入，结合规则库与大模型进行 SQLi/XSS/Webshell 等攻击识别，并输出处置建议。**
* **PCAP 流量分析：针对抓包文件做会话重组、协议解析与规则命中，辅助溯源。**
* **系统日志与告警扫描：对 Windows EVTX 日志进行加载、检索和规则化告警扫描，支持匹配规则与阈值规则两种模式。**
* **规则管理与导入：支持新增/编辑/启用规则、导入默认规则库以及导入 JSON 规则文件，便于团队协作与经验沉淀。**
* **WEBSHELL检查： AI助力**
* **代码审计：AI助力**

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic68tibQtgZQFJicvWOclTXR0DeWiaZ4fyRoyCONyzoIxwicGqG8zsYvQB2ZS2adylOjKORV0OAY0fXIguvv9q7Eawdr6cjHlfNIF1PA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=24)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69X05aaXFFaKQGJMGL0mpeBtGT0tlE6ZVO6cjKut8JWEfAK2LF9tYy9GTrEzmAOqibIrkC6Fq3k3LjhXAManLia5EibfkfugZSjicU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=25)

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ibrl0l8lh5n48UibLqrXye2QBaDNICRejqIZ7YKC8EohsvvPQGerjOMj5OoCJAsdbCTxicnBHuxHzUcC1ibMeYDyhhpO69KsjiaLg4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=26)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic68fSibrChibdZkkR88r6tp8mpT114TmnCSU81...