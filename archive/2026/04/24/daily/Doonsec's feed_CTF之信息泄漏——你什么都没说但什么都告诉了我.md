---
title: CTF之信息泄漏——你什么都没说但什么都告诉了我
url: https://mp.weixin.qq.com/s/hB9AnGy1tDxMoFhKZWeSrQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:31:45.399344
---

# CTF之信息泄漏——你什么都没说但什么都告诉了我

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIytJI9GgswbFhJyRia0wmweaXVic3JX1NCyGGPAlEL7xlkw7GAZt10gmiaSSiavszPbgZm9X7N00DQFbAWHCAUicKJuHVGxd5TDPmCQ/0?wx_fmt=jpeg)

# CTF之信息泄漏——你什么都没说但什么都告诉了我

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在CTF比赛和常见网络防护中，通过分析泄漏的信息可以有效获取目标相关信息，有些时候，泄漏的信息成为攻击成功或失败的关键所在。

# 一、常见信息泄漏方式

## （一）遍历类

### 目录遍历

一般通过遍历服务器目录获取 `flag`、后台地址、备份文件等关键信息。其核心原理是利用字典对 Web 服务器进行暴力猜解。

**相关工具：**

1. **dirsearch**

* 在终端中进入 dirsearch 目录。
* 基础扫描命令：

  ```
  python3 dirsearch.py -u 目标网址 -e *
  ```
* **参数解释**：

* `-u`

  ：指定目标 URL。
* `-e *`

  ：指定要扫描的文件后缀（如 php, html, js, zip 等），`*` 代表扫描所有常见后缀。
* `-w`

  ：指定自定义字典路径（如 `-w /path/to/dict.txt`）。

* **简介**：一个基于 Python 开发的命令行工具，相比传统工具速度更快，支持递归扫描。
* **安装**：`git clone https://github.com/maurosoria/dirsearch.git`
* **使用教程**：

2. **御剑**

* **多线程**

  ：用户可根据自身电脑配置设置调节扫描线程，提高速度。
* **全面性**

  ：集合了 DIR 扫描、ASP/ASPX/PHP/JSP 脚本路径、MDB 数据库等常见敏感路径。
* **精准度**

  ：默认探测状态码 200（即扫描网站真实存在的路径文件），过滤无效链接。

* **特点**

  ：

### 域名挖掘

在渗透测试中，主站往往防护严密，通过挖掘子域名（如 `dev.example.com`, `test.example.com`）往往能发现防护较弱的入口或遗留系统。

**常用方法：**

1. **工具扫描**

* **Layer 子域名挖掘机**

  ：Windows 下常用的图形化工具，集成了爆破、搜索引擎查询等功能。
* **SubDomainBrute**

  ：基于 Python 的高性能子域爆破工具，适合在 Linux/Kali 下使用。

2. **搜索引擎语法**

* `site:xxx.com`

  ：列出该域名下所有被搜索引擎收录的页面和子域名。
* `site:xxx.com -www`

  ：排除主站，专门查找子域名。

* 使用 Google 或 Bing 的 `site` 语法：

3. **第三方平台聚合**

* **DNSdumpster**

  ：免费查询 DNS 记录，可视化展示子域名拓扑图。
* **VirusTotal**

  ：在搜索域名时，查看 "Relations" 或 "Communicating" 标签页，常能发现关联子域名。
* **Sublist3r**

  ：一款强大的 Python 工具，聚合了 Google, Yahoo, Bing, Baidu, Ask, Netcraft, Virustotal 等多个数据源。

### 证书伪造与查找

SSL/TLS 证书中通常包含域名信息，攻击者可以通过查询公开的数字证书透明度日志（Certificate Transparency Logs）来发现目标的主域名、子域名甚至内网域名。

**核心平台：**

1. **crt.sh**

* 最常用的免费证书查询网站，输入域名即可查询所有相关的证书记录。

2. **Censys**

* **资产发现**

  ：查找组织名下所有持有有效 SSL 证书的 IP 和域名。
* **漏洞排查**

  ：快速检索全网受特定漏洞（如 Log4j）影响的设备。

* **互联网地图**

  ：Censys 维护着全球互联网基础设施的权威地图，提供实时数据。
* **证书与攻击面管理**

  ：安全团队利用 Censys 发现未知的互联网暴露资产（包括通过证书关联的资产），识别“影子 IT”。
* **威胁情报**

  ：通过 Censys 可以追踪攻击者的基础设施（Adversary Infrastructure），例如分析恶意软件的 C2 服务器证书。

* **简介**

  ：Censys 是一个强大的互联网资产搜索引擎（类似 Shodan），它不仅提供证书查询，还能提供全网的设备指纹、端口和服务信息。
* **核心能力（基于参考材料）**

  ：
* **应用场景**

  ：

### DNS解析获取

DNS 信息泄露可能导致攻击者获取内网结构或管理员邮箱。

**常用命令与技巧：**

1. **查询域名服务器 (NS 记录)**

* 使用 `dig` 工具查询负责该域名的 DNS 服务器：

  ```
  dig xxx.com ns
  ```

2. **DNS 域传送漏洞利用**

* 如果 DNS 服务器配置不当，允许任意 IP 进行区域传输，攻击者可以获取该域名下所有的 DNS 记录（包括内网记录）。
* 命令格式：

  ```
  dig axfr @目标DNS服务器IP 目标域名
  ```

  > 注：现代互联网环境中此漏洞已较少见，但在内网渗透中仍值得尝试。

### 真实IP获取

当目标使用了 CDN（内容分发网络）时，直接扫描域名得到的是 CDN 节点的 IP，无法对源站进行攻击。因此需要寻找“绕过 CDN 获取真实 IP”的方法。

**寻找真实 IP 的思路：**

1. **子域名解析**

* 很多网站的 `www` 或主站走了 CDN，但 `mail.xxx.com`、`ftp.xxx.com`、`vpn.xxx.com` 或测试环境的子域名可能未配置 CDN，直接解析到源站 IP。

2. **历史 DNS 解析记录**

* 查询域名的历史 DNS 记录（如通过 SecurityTrails, ViewDNS 等平台）。在网站启用 CDN 之前，A 记录指向的往往就是真实 IP。

3. **邮件地址与邮件头**

* 如果目标网站有邮件发送功能（如注册验证、密码找回），邮件源码中的 `Received` 字段通常包含源站 IP。

4. **国外访问**

* 部分 CDN 仅针对国内或特定地区生效，使用海外 VPS 进行解析可能直接获得真实 IP。

5. **相关站点记录**

* 查询同服务器下的其他站点（旁站），通过 C 段扫描寻找真实 IP。

### 端口扫描

端口扫描是了解目标开放服务、操作系统版本和潜在漏洞的关键步骤。

**工具：Nmap (Network Mapper)**

Nmap 是网络探测和安全审计的行业标准工具。

#### Nmap 基本语法与实战

1. **扫描指定目标**

* 基础扫描，探测最常见的 1000 个端口：

  ```
  nmap <目标IP或域名>
  ```

2. **全端口扫描**

* 扫描所有 65535 个端口，防止遗漏非常用端口（如 30000+ 的管理端口）：

  ```
  nmap -p- <目标IP>
  ```

3. **服务版本探测**

* 识别端口上运行的具体软件版本（如 Apache 2.4.1），这对寻找已知漏洞（Exploit）至关重要：

  ```
  nmap -sV <目标IP>
  ```

4. **综合扫描（推荐）**

* 结合操作系统探测、版本探测、脚本扫描和路由跟踪：

  ```
  nmap -A <目标IP>
  ```

5. **UDP 扫描**

* 默认 Nmap 扫描 TCP 端口，UDP 端口（如 DNS, SNMP, DHCP）需要专门参数：

  ```
  nmap -sU <目标IP>
  ```

## （二）语言相关文件

### phpinfo

**phpinfo** 是 PHP 的内置诊断函数，用于输出当前 PHP 环境的完整配置快照。若在生产环境中未删除或限制访问该页面，将导致严重的信息泄露。

#### 泄露内容与危害

* **敏感配置**

  ：暴露 `disable_functions`（禁用函数列表）、`open_basedir`（目录限制）、`extension_dir`（扩展目录）等，攻击者可据此寻找绕过防护的路径。
* **环境变量**

  ：泄露服务器路径、系统版本、数据库连接信息等。
* **利用方式**

  ：

+ **文件包含**

  ：配合 `allow_url_include=On`，利用 `php://filter` 等伪协议读取敏感文件。
+ **临时文件包含**

  ：利用 PHP 上传临时文件的机制，结合条件竞争读取临时文件 GetShell。
+ **命令执行**

  ：若启用了 `expect` 扩展，可直接通过 `expect://` 协议执行系统命令。

#### 探测与利用

* **常见路径**

  ：直接尝试访问 `phpinfo.php`、`info.php`、`test.php` 等。
* **工具**

  ：使用目录扫描工具（如 dirsearch）或 BurpSuite 进行探测。

### robots.txt

**robots.txt** 是网站与网络爬虫之间的核心交互规则，用于指导搜索引擎爬虫的访问权限。但其“禁止访问”的规则往往会反向暴露敏感路径。

#### 泄露原理

* **反向推断**

  ：`Disallow` 字段列出的路径（如 `/admin/`、`/backup/`）通常是管理员不希望被索引的敏感目录，攻击者可据此直接访问。
* **系统指纹**

  ：禁止的路径可能暴露 CMS 类型（如 `/wp-admin/` 暗示 WordPress）或中间件（如 `/tomcat-manager/`）。

#### 利用步骤

1. **访问文件**

   ：在目标 URL 后拼接 `/robots.txt`。
2. **提取路径**

   ：查找 `Disallow` 后的路径。
3. **直接访问**

   ：拼接目标 URL 与提取的路径，查看是否存在敏感信息或后台入口。

### 注释

前端注释常包含开发人员遗留的调试信息、敏感数据或逻辑说明。

#### 查看源码方法

* **浏览器快捷键**

  ：`Ctrl + U` 或 `F12`（开发者工具）。
* **协议头**

  ：在网址前加上 `view-source:`。
* **禁用 JS**

  ：在浏览器设置中禁用 JavaScript 后查看源码，防止代码动态修改 DOM。

#### 常见泄露内容

* **敏感凭证**

  ：泄露的用户名、密码、API Key。
* **隐藏逻辑**

  ：前端 JS 绕过逻辑、未公开的接口参数。
* **Meta 标签**

  ：`<meta>` 标签中可能包含框架版本或管理后台入口。

### 响应头

HTTP 响应头中常包含服务器软件版本、框架信息及自定义规范，是信息收集的重要来源。

#### 常见泄露字段

* **Server**

  ：Web 服务器类型及版本（如 `Apache/2.4.41`）。
* **X-Powered-By**

  ：开发语言及框架（如 `PHP/7.4.3`、`ASP.NET`）。
* **自定义头**

  ：部分网站采用自定义响应头（如 `X-Debug-Info`），可能包含内部调试信息。

#### 工具

* **BurpSuite**

  ：使用 Repeater 模块发送请求，观察响应头。
* **浏览器开发者工具**

  ：在“网络”标签页查看请求详情。

### 网站框架获取

识别网站使用的 CMS、框架、库及服务器版本，有助于查找已知的历史漏洞。

#### 常用工具

* **Wappalyzer**

  ：浏览器插件，实时识别网站技术栈。
* **WhatWeb**

  ：命令行工具，支持多种识别策略。
* **W11scan**

  ：分布式 Web 指纹识别系统。
* **云悉**

  ：在线指纹识别平台。

#### 识别内容

* **CMS**

  ：WordPress, Joomla, Drupal 等。
* **JS 框架**

  ：Vue.js, React, Angular 等。
* **Web 服务器**

  ：Nginx, Apache, IIS 等。

### WEB-INF/web.xml 泄露

**WEB-INF** 目录包含了所有 web 应用会用到但不处于 web 路径中的资源，即不属于公开页面。通常开发者会把 JSP 文件、Jar 包、Java 类文件放在该目录下。

#### 1. 漏洞产生

* **原理**

  ：在 Java 的 Servlet 文档中，`WEB-INF`  目录包含了所有 web 应用会用到但不处于 web 路径中的资源，即不属于公开页面。通常开发者会把 JSP 文件、Jar 包、Java 类文件放在该目录下。
* **常见泄露文件**

  ：

+ `WEB-INF/web.xml`

  ：Web 应用程序配置文件，描述了 servlet 和其他的应用组件配置及命名规则。
+ `WEB-INF/database.properties`

  ：数据库配置文件。
+ `WEB-INF/classes/`

  ：一般用来存放 Java 类文件 (.class)。
+ `WEB-INF/lib/`

  ：用来存放打包好的库 (.jar)。
+ `WEB-INF/src/`

  ：用来放源代码 (.asp 和 .php 等)。

#### 2. 漏洞利用

* **信息收集**

  ：通过 `web.xml` 文件推测应用组件相关类的名字，然后在 `src` 目录下查找代码。
* **代码审计**

  ：如果没有源代码，可以直接下载 `class` 文件进行反编译（使用 JD-GUI 等工具）。
* **利用方式**

  ：

+ **Tomcat 路径遍历**

  ：利用 CVE-2020-1938 (Ghostcat) 等漏洞，通过 AJP 协议读取 `WEB-INF` 下的文件。
+ **文件包含**

  ：若存在文件包含漏洞，尝试包含 `WEB-INF/web.xml`。

## （三）备份文件获取

常见备份文件前缀：

web、website、backup、back、www、wwwroot、temp

常见备份文件类型：

tar、tar.gz、zip、rar

看看提示有没有关键信息，没有的话就用目录扫描工具扫描备份文件，对于.bak文件可以尝试用notepad++或文本编辑器打开搜索flag。

## （四）代码管理不当

### git

**Git** 是目前最流行的分布式版本控制系统。在自动化部署站点时，如果配置不当，可能会将 `.git` 文件夹直接暴露在线上环境中。攻击者可以利用该文件夹恢复源代码，从而审计代码并挖掘文件上传、SQL注入等Web安全漏洞。

#### 目录结构

* **hooks**

  ：存放一些 shell 脚本的地方。
* **info**

  ：存放仓库的信息。
* **objects**

  ：存放所有 git 对象的地方。
* **refs**

  ：存放提交 hash 的地方。
* **config**

  ：github 的配置信息。
* **description**

  ：仓库的描述信息，主要给 gitweb 等 git 托管系统使用。
* **HEAD**

  ：映射到 ref 引用，能够找到下一次 commit 的前一次哈希值。

#### 工具与利用

**1. GitHack**

* **简介**

  ：一个 `.git` 文件夹泄露利用脚本，通过泄露的 `.git` 文件夹下的文件，重建还原工程源代码。
* **环境**

  ：需 Python 2 环境。
* **地址**

  ：GitHub - lijiejie/GitHack: A .git folder disclosure exploit · GitHub
* **使用教程**

  ：

1. 打开终端，进入 GitHack 目录：`cd GitHack/`
2. 运行脚本：`python GitHack.py http://www.target.com/.git/`
3. 执行后会在本目录生成以网址命名的文件夹。

**2. dvcs-ripper**

* **简介**

  ：功能全面的版本控制系统泄露利用工具，支持 SVN, GIT, Mercurial/hg, bzr 等。
* **环境**

  ：需 Perl 环境。
* **地址**

  ：GitHub - kost/dvcs-ripper: Rip web accessible (distributed) version control systems: SVN/GIT/HG... · GitHub

> **技巧**：一般先看题目或页面是否有 Git 相关提示，没有的话需通过目录扫描发现。使用 `git diff` 可比较不同版本差异，在某些题目中可直接获取 flag。

### svn

**SVN** 是一个开放源代码的版本控制系统。在服务器部署代码时，如果使用 `svn checkout` 功能更新代码且未配置好目录访问权限，会存在此漏洞。黑客可利用此漏洞下载整套网站源代码。

#### 工具与利用

**SvnExploit**

* **简介**

  ：一个 `.svn` 泄露利用测试脚本，通过泄露的文件还原重建工程源代码。
* **地址**

  ：GitHub - admintony/svnExploit: SvnExploit支持SVN源代码泄露全版本Dump源码 · GitHub
* **使用教程**

  ：

1. 下载：`git clone https://github.com/admintony/svnExploit`
2. 进入目录：`cd svnExploit/...