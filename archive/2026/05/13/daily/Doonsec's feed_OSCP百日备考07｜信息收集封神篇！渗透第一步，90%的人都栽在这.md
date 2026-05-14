---
title: OSCP百日备考07｜信息收集封神篇！渗透第一步，90%的人都栽在这
url: https://mp.weixin.qq.com/s/R_33Fj6qc3DSY5f58yCxdg
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:43:23.154938
---

# OSCP百日备考07｜信息收集封神篇！渗透第一步，90%的人都栽在这

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydUqz5DOfXaUqEjpibImScalX8YJO3iaGhTsEKBIjxq5Ivm2eX9JPWcbLxEPgvHYDmkelO7TGXQcpa8riaruWvKjkTLmcoUs7ibeiaFA/0?wx_fmt=jpeg)

# OSCP百日备考07｜信息收集封神篇！渗透第一步，90%的人都栽在这

泷羽Sec-陌离

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前六期我们把系统基础、网络原理、核心工具、PowerShell全讲完了。从这期开始，正式进入渗透测试的全流程实战，第一关就是让最多人翻车的信息收集。

说实话，我见过太多人刷靶机的时候，上来就开Nmap扫端口、扔漏洞扫描器，结果扫了大半天，要么什么有用的都没找到，要么直接触发防护规则被踢下线。还有人打了一周靶机，最后发现人家的测试环境、后台管理页面，甚至硬编码的账号密码，Google一搜就出来了，当场拍大腿。

必须说句大实话：**渗透测试的上限，从来不是你收藏了多少漏洞利用工具，而是你的信息收集能力有多强。** 充分的信息收集能帮你把目标的攻击面扒得干干净净，很多时候根本不用挖什么复杂漏洞，靠收集到的敏感信息就能直接打点成功。

而信息收集里性价比最高的，就是**被动信息收集**——全程不和目标系统发生任何交互，完全通过公开渠道获取信息，不会在目标上留下任何痕迹，更不会触发安全防护。

今天这篇不讲干巴巴的理论，只讲OSCP靶场和实战里真正用得上的被动信息收集技术。从Google Hacking、域名信息扒取，到子域名爆破、代码仓库敏感信息查找、互联网资产搜索引擎，全给你拆解明白。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydVooLISsCTqj5ncKn9E14ROx8lOfWPxSoAUf9NtJSJTYWaRiau54mbpBtgNpYZNBFhia2fbxuo4X8Igpuw7WicbMyVthQyheShl4Q/640?wx_fmt=webp&from=appmsg)

## 一、先搞懂：为什么被动信息收集是OSCP的重中之重？

很多新手觉得被动信息收集就是“搜一下域名”，这是大错特错的。它的核心优势有四点，每一点都精准命中OSCP备考的命门：

1. **全程零痕迹，绝不打草惊蛇。** 你根本不向目标发任何数据包，完全通过公开渠道拿信息。目标再强的WAF、IPS、防火墙，也挡不住你搜Google、查Whois。
2. **低成本扩大攻击面。** 一个主域名可能只有一个Web站点，但它的子域名可能有几十上百个。测试环境、后台系统、内部服务全藏在子域名里，被动收集能把你的攻击面扩大十倍。
3. **找到最省力的突破口。** 很多时候你不用费劲挖SQL注入、XSS，靠被动收集就能找到硬编码的API密钥、SSH私钥、测试环境的弱口令，一步到位。
4. **OSCP的隐藏考点。** 很多靶机的隐藏入口和关键线索，都藏在公开信息里，不是扫描器能扫出来的。有些人打不下靶机，不是不会挖漏洞，而是根本没找到正确的攻击入口。

## 二、Google Hacking：搜索引擎的渗透骚操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nw0LxfseydW8SKIwGgwian80O27CMIEuRtAsatYSbJ6n4cSdhGqtU2hAIsdIo1EXZvjHu4Zjwd0VhHrQJfkXiaqBRSHZPJMW1ibpXSnibLUOqGA/640?wx_fmt=png&from=appmsg)

Google Hacking是被动信息收集里最基础也最强大的技术。说白了，就是用Google的高级搜索语法精准过滤结果，找到目标暴露在互联网上的敏感信息。不仅Google能用，Bing、DuckDuckGo也基本通用。

### 必背基础搜索语法

| 搜索语法 | 核心作用 | 实战场景 |
| --- | --- | --- |
| `site:example.com` | 限定只搜索指定域名 | 搜目标站点的所有页面，找后台、敏感文件 |
| `filetype:pdf` | 限定搜索指定文件类型 | 找PDF、Excel、Word，里面可能藏着敏感信息 |
| `intitle:"Index of"` | 标题包含指定内容 | 找开了目录浏览的页面，里面有源码、备份文件 |
| `inurl:admin` | URL包含指定字符串 | 找管理后台、登录页面 |
| `intext:"password"` | 正文包含指定关键词 | 找网页里泄露的密码、密钥 |
| `cache:example.com` | 查看Google缓存 | 目标下线了也能看历史内容 |

### 实战高频组合语句

直接把`example.com`换成你的目标域名就能用：

```
# 找目标站点的Excel/Word/PDF文件，里面可能藏着账号密码
site:example.com (filetype:doc | filetype:xls | filetype:pdf)

# 找开了目录浏览的页面，最容易找到备份文件和源码
site:example.com intitle:"Index of"

# 找所有登录/管理后台页面
site:example.com (intitle:"login" | intitle:"admin" | inurl:admin)

# 找页面里泄露的密码、密钥
site:example.com intext:"password" | intext:"api_key" | intext:"secret"

# 找子域名的测试/开发环境，防护通常更薄弱
site:*.example.com inurl:test | inurl:dev | inurl:staging -site:www.example.com
```

### Google Hacking Database（GHDB）

如果你不知道该搜什么，直接用现成的。GHDB是Exploit-DB维护的谷歌黑客数据库，里面有近8000条预定义的渗透搜索语句，地址：https://www.exploit-db.com/google-hacking-database

### 别只盯着Google

Bing对中文站点的收录更全，DuckDuckGo不会被个性化过滤，Baidu是国内企业信息收集的首选。多引擎交叉验证，才能拿到最全面的结果。

## 三、Whois查询：扒光目标域名的家底

Whois能拿到目标域名的全量注册信息，是域名信息收集的第一步。能拿到的信息包括：注册人/组织名称、联系邮箱电话、注册和到期日期、域名服务器、注册商信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Nw0LxfseydUvqOOC8libPKdt577nPsLLt91nxLVH3BiakaqRJZ22T2ctNowNnv0TU8HnDXmUrIJzWeFjpaBJWKrhOibR0VibYYtfe9WfOyyXZQw/640?wx_fmt=jpeg&from=appmsg)

### 命令行工具（Kali默认自带）

```
# 基础Whois查询
whois example.com

# 指定Whois服务器查询
whois -h whois.verisign-grs.com example.com

# 查IP地址的Whois信息
whois 8.8.8.8
```

### 在线工具

* whois.domaintools.com：能查历史Whois记录和关联域名
* whois.icann.org：ICANN官方查询，信息最权威
* who.is：界面简洁，域名IP都能查

### 实战技巧

通过注册人/注册邮箱/组织名找关联域名，扩大攻击面。很多目标现在用了隐私保护，但历史Whois记录里可能有真实信息。NS记录能揭示目标用的云厂商和托管服务，后续针对性地找配置漏洞。刚注册不久的域名，大概率是新业务系统，防护通常更薄弱，优先打点。

## 四、DNS信息收集：摸清目标网络架构

![](https://mmbiz.qpic.cn/mmbiz_png/Nw0LxfseydXROngiaRqfyjeTSticc6nmbM2WQ2B60kk4b3YUkoXPwsQz7DpwchmCHHFGKLibnI8eZeCMRUdkn5ukIN0reIwMRRJwT4mnTicibALg/640?wx_fmt=png&from=appmsg)

DNS记录里藏着目标的网络架构、服务器分布、邮件系统、内部服务的关键信息。

### 渗透必关注的DNS记录类型

| 记录类型 | 核心作用 | 渗透用途 |
| --- | --- | --- |
| A记录 | 域名→IPv4 | 拿到真实IP，绕过CDN |
| CNAME记录 | 域名别名 | 找第三方服务和云厂商 |
| MX记录 | 邮件服务器 | 找邮件系统，后续钓鱼攻击 |
| NS记录 | 域名服务器 | 找DNS服务器，尝试域传送漏洞 |
| TXT记录 | 文本记录 | SPF/DKIM配置、域名验证信息 |
| SRV记录 | 服务记录 | 找SIP、LDAP等内网服务 |

### 核心查询工具

```
# dig：最强大的DNS查询工具
dig example.com
dig example.com MX
dig example.com ANY          # 查询所有类型记录
dig @8.8.8.8 example.com    # 用指定DNS服务器查
dig +trace example.com       # 跟踪完整解析过程
dig -x 192.168.1.1           # 反向DNS查询

# nslookup：Windows/Linux通用
nslookup example.com
nslookup -type=MX example.com

# host：轻量简单
host example.com
host -t MX example.com
```

### 实战技巧

不要只查A记录，MX、TXT、NS记录里往往藏着更有价值的信息。用多个DNS服务器交叉验证，可能拿到不同的解析结果。如果DNS服务器配置不当允许匿名域传送，你能直接拿到目标的所有子域名记录。

## 五、子域名发现：把攻击面扩大10倍

很多人只盯着主站`www.example.com`，结果主站防护严得很。但目标的子域名里藏着大量测试环境、管理后台、内部系统，防护通常非常薄弱，是最容易突破的入口。

### 被动发现方法（零交互，不留痕迹）

#### 证书透明度日志（最有效）

HTTPS站点的SSL/TLS证书都会被记录到公开的证书透明度日志，一个证书里往往包含几十上百个关联子域名。最常用的工具是**crt.sh**（https://crt.sh），直接搜`%.example.com`。

命令行一键提取：

```
curl -s "https://crt.sh/?q=%.example.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```

#### 搜索引擎收集

```
site:*.example.com -site:www.example.com
```

#### DNS聚合服务

DNSDumpster（https://dnsdumpster.com）能可视化展示DNS记录和子域名分布，SecurityTrails能查历史DNS记录，VirusTotal查域名时会展示关联子域名。

#### 互联网档案馆（Wayback Machine）

https://web.archive.org，保存了目标十几年的历史页面，能找到已经下线但曾经存在的子域名。

### 自动化工具

```
# Subfinder：集成30+被动数据源，速度极快
subfinder -d example.com -o subdomains.txt

# Sublist3r：经典枚举工具，集成多个数据源
sublist3r -d example.com -o subdomains.txt

# Amass：功能最全面的信息收集工具
amass enum -d example.com

# Findomain：基于证书透明度日志，速度快
findomain -t example.com -o subdomains.txt
```

### 实战技巧

多工具交叉验证，合并去重才能拿到最全面的结果。拿到一级子域名后，对`test.example.com`再搜`%.test.example.com`，能找到更深层的内部子域名。`test`、`dev`、`uat`、`admin`、`api`、`vpn`、`mail`这些子域名，通常是核心系统，优先做漏洞测试。

## 六、OSINT开源情报：从“人”身上找突破口

再坚固的系统也架不住人的因素。通过社交媒体和开源平台，收集目标的组织架构、员工信息、技术栈，往往是突破目标的关键。

### 核心平台

**LinkedIn**是获取员工信息的最核心来源。能拿到组织架构、部门划分、员工名单、技能栈。整理员工姓名生成企业邮箱字典，从招聘信息和员工技能里找目标用的技术栈和系统版本，找对应的已知漏洞。

**GitHub/GitLab**是硬编码敏感信息的重灾区，后面单独讲。

**Twitter/Facebook/Instagram**上，员工发的办公电脑截图可能泄露内网地址和系统版本，公司动态会透露新上线的业务系统。

### 自动化工具

```
# theHarvester：经典的邮箱、子域名收集工具，Kali默认自带
theHarvester -d example.com -b all

# Recon-ng：全功能自动化信息收集框架
recon-ng
# 用Google搜索目标的子域名
marketplace install recon/domains-hosts/google_site_web
modules load recon/domains-hosts/google_site_web
options set SOURCE example.com
run
```

### 实战技巧

先搞定企业邮箱格式，绝大多数企业格式固定（如`名.姓@example.com`），拿到格式就能生成完整邮箱字典。重点关注招聘信息，里面会写清楚用什么技术栈、数据库、中间件。从多个平台拿到的信息一定要交叉验证。

## 七、代码仓库搜索：找硬编码密钥，一步打点

很多开发人员安全意识薄弱，会把公司的敏感信息、硬编码密钥、账号密码直接传到公开代码仓库。这些信息能让你直接拿到目标系统的权限。

### GitHub渗透搜索语句

```
# 搜索指定组织的代码
org:example-org

# 搜索包含目标域名的代码
"example.com" org:example-org

# 搜索敏感配置文件
org:example-org filename:.env | filename:config.json | filename:wp-config.php

# 搜索SSH私钥
org:example-org "BEGIN RSA PRIVATE KEY" | "BEGIN OPENSSH PRIVATE KEY"

# 搜索数据库密码、API密钥
org:example-org "db_password" | "api_key" | "aws_secret_access_key" | "password"

# 搜索内部URL和后台地址
org:example-org inurl:admin | "internal.example.com"
```

### 自动化扫描工具

```
# truffleHog：扫描Git仓库里的硬编码密钥
trufflehog --regex --entropy=True https://github.com/example-org/repo.git

# Gitleaks：轻量高效密钥检测
gitleaks --repo-url=https://github.com/example-org/repo.git

# GitRob：批量扫描GitHub组织的所有仓库
gitrob analyze example-org
```

### 实战技巧

不要只搜组织仓库，很多开发者会把公司代码传到个人GitHub账号里，这里的泄露比组织仓库多得多。哪怕最新代码删掉了敏感信息，旧的提交历史里可能还留着。Issues和Pull Requests里也经常泄露内部信息和漏洞细节。

## 八、Shodan：互联网设备搜索引擎

Shodan不搜网页，专门搜互联网上暴露的联网设备、服务器、摄像头、路由器、工控设备。通过它你能找到搜索引擎收录不到的内部服务。

### 必背搜索语法

| 语法 | 作用 | 场景 |
| --- | --- | --- |
| `hostname:example.com` | 搜主机名包含目标域名 | 找所有暴露的公网服务器 |
| `port:3389` | 搜开放指定端口 | 找RDP、SSH、数据库端口 |
| `os:windows` | 搜指定操作系统 | 筛选Windows/Linux服务器 |
| `org:"Example Inc"` | 搜指定组织 | 精准定位企业所有公网资产 |
| `net:192.168.1.0/24` | 搜指定网段 | 拿到IP段后扫整个网段 |

### 高级渗透搜索

```
# 找存在BlueKeep漏洞的Windows服务器
vuln:CVE-2019-0708 os:windows port:3389

# 找目标组织用的指定版本Nginx
product:nginx version:"1.14.0" org:"Example Inc"

# 找目标组织的后台管理页面
http.title:"Admin Login" org:"Example Inc"

# 找开放SMB端口的Windows服务器
port:445 os:windows org:"Example Inc"
```

### 命令行工具

```
pip install shodan
shodan init YOUR_API_KEY
shodan search "hostname:example.com"
shodan host 8.8.8.8   # 查看指定IP的详细信息
```

### 实战技巧

结合多个过滤器缩小范围，不...