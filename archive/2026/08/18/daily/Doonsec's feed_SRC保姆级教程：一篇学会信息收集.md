---
title: SRC保姆级教程：一篇学会信息收集
url: https://mp.weixin.qq.com/s/ToQALoBT1JoxyKgEGJrQHw
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:55:30.894185
---

# SRC保姆级教程：一篇学会信息收集

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DJX1rNqJe4niciaoNibf7VcXwcYZWvc7TgRbA9T2gZ5yfE7ZDFAhmiat63wkwyp0zTlqFsfYesMojTKEbJguNIX9UmYLJb2Y2jfhqTVWIAuG1zY/0?wx_fmt=jpeg)

# SRC保姆级教程：一篇学会信息收集

隐雾安全
隐雾安全

隐雾安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多刚开始挖SRC的同学，遇到的第一个问题都是：

**「拿到目标以后，我到底应该从哪里开始？」**

打开官网？扫目录？跑扫描器？还是直接拿 Burp 抓包？

其实都可以。

但如果让我来，我做的第一件事情一定是：

**「信息收集。」**

因为你看到的官网，只是一个企业互联网资产里非常小的一部分。

真正值得关注的东西，往往藏在：

* 子域名
* 历史域名
* APP
* 小程序
* API
* JS 文件
* 开发测试环境
* 云上资产
* 历史系统
* 供应商系统
* 遗留后台

这篇就把SRC中常用的信息收集思路、工具、网站和基础用法整理出来。

建议收藏，需要的时候直接当 Checklist 用。

---

## 一、先搞明白：SRC 信息收集到底在收集什么？

假设 SRC 给你的核心目标是：

```
example.com
```

不要把它理解成：

```
我要测试 www.example.com
```

应该把它理解成：

```
example.com
        │
        ├── 域名资产
        │     ├── www.example.com
        │     ├── api.example.com
        │     ├── admin.example.com
        │     └── ...
        ├── IP资产
        │     ├── 服务器
        │     ├── 云主机
        │     └── 历史IP
        ├── Web资产
        │     ├── 官网
        │     ├── 管理后台
        │     ├── API
        │     └── 测试环境
        ├── 移动端资产
        │     ├── Android APP
        │     ├── iOS APP
        │     └── H5
        ├── 微信生态
        │     ├── 小程序
        │     ├── 公众号
        │     └── H5
        └── 关联资产
              ├── 子公司
              ├── 品牌
              ├── 产品
              └── 历史业务
```

所以信息收集真正要解决的是：

> ❝
>
> **「这个企业到底有哪些互联网资产？」**
>
> ❞

---

## 二、第一阶段：确定资产边界

在SRC场景里，不是"搜到的资产都能测"。

第一步应该先阅读 SRC 的测试规则，重点记录：

```
允许测试的根域名：
允许测试的APP：
允许测试的小程序：
允许测试的IP段：
禁止测试的业务：
禁止测试的漏洞类型：
是否允许自动化扫描：
是否限制请求频率：
```

建议自己建立一个 `scope.txt`：

```
example.com
example.cn
exampleapp.com
```

后面的所有信息收集，都围绕 Scope 展开。

### 可参考平台

**「1. 补天漏洞响应平台」**
地址：`https://www.butian.net/`

**「2. 漏洞盒子」**
地址：`https://www.vulbox.com/`

**「3. HackerOne」**
地址：`https://www.hackerone.com/`

**「4. Bugcrowd」**
地址：`https://www.bugcrowd.com/`

> ❝
>
> 不同 SRC 的测试范围和规则差异很大，具体以目标 SRC 公布的规则为准。
>
> ❞

---

## 三、企业主体信息收集

先确认：

* 公司全称
* 曾用名
* 品牌名称
* 子公司
* 控股公司
* 产品名称
* APP 名称
* 公众号
* 小程序
* 官方网站

### 推荐网站

---

**「1. 企查查」**
用途：企业主体、股权、品牌、关联企业
地址：`https://www.qcc.com/`

**「2. 天眼查」**
用途：企业关系、产品、投资关系
地址：`https://www.tianyancha.com/`

**「3. 爱企查」**
用途：企业工商与关联信息
地址：`https://aiqicha.baidu.com/`

**「4. 国家企业信用信息公示系统」**
用途：官方工商主体查询
地址：`https://www.gsxt.gov.cn/`

---

这里最重要的并不是看注册资本，而是找：

**「企业 → 品牌 → 产品 → 域名之间的关系。」**

例如：

```
公司A
├── 产品A
├── 产品B
├── APP C
├── 子公司D
└── 品牌E
```

这些关键词都可以成为下一轮资产搜索的入口。

---

## 四、WHOIS 信息

WHOIS 可以帮助了解：

* 域名注册时间
* 注册商
* DNS 服务器
* 域名状态
* 部分注册信息

### 推荐网站

**「1. 站长之家 Whois」**
地址：`https://whois.chinaz.com/`

**「2. ICANN Lookup」**
地址：`https://lookup.icann.org/`

现在很多域名开启了隐私保护，所以 WHOIS 不一定能直接找到联系人。

但它仍然适合用来确认域名注册时间、注册商、DNS 服务商和域名状态。

---

## 五、根域名与备案信息收集

这是很多新手最容易漏掉的一步。

我们通常拿到：

```
example.com
```

但一家大型企业可能还有：

```
example.cn
example.net
examplecloud.com
exampleapp.com
examplegroup.com
```

甚至不同产品使用完全不同的域名。

### 常见思路

搜索：

```
"公司名称" "官网"
"公司名称" "ICP备案"
"品牌名称" "官网"
"产品名称" "官网"
```

### 推荐网站

---

**「1. 工信部 ICP/IP」**
用途：官方备案查询
地址：`https://beian.miit.gov.cn/`

地址/域名信息备案管理系统
**「2. 企查查」**
用途：企业主体、股权、品牌、关联企业
地址：`https://www.qcc.com/`

**「3. 天眼查」**
用途：企业关系、产品、投资关系
地址：`https://www.tianyancha.com/`

**「4. 爱企查」**
用途：企业工商与关联信息
地址：`https://aiqicha.baidu.com/`

---

重点关注：

```
备案主体
网站名称
域名
APP备案
小程序备案
```

---

## 六、子域名收集

确定根域名之后，就可以开始扩展子域名。

例如：

```
www.example.com
api.example.com
admin.example.com
oa.example.com
mail.example.com
test.example.com
dev.example.com
open.example.com
```

### 推荐工具

---

**「1. Subfinder」**
用途：被动子域名收集，速度快
地址：`https://github.com/projectdiscovery/subfinder`

**「2. OneForAll」**
用途：多数据源子域名收集
地址：`https://github.com/shmilylty/OneForAll`

**「3. OWASP Amass」**
用途：攻击面映射与资产发现
地址：`https://github.com/owasp-amass/amass`

\*\*4. crt.sh \*\*
用途：证书透明度查询
地址：`https://crt.sh/`

---

### Subfinder 基础使用

```
subfinder -d example.com -o domains.txt
```

得到：

```
www.example.com
api.example.com
admin.example.com
test.example.com
...
```

这份 `domains.txt` 后面可以继续交给 httpx 做存活探测。

---

## 七、证书透明度收集

HTTPS 证书也是非常重要的数据来源。

很多企业申请证书时，会把多个子域名写进证书：

```
*.example.com
www.example.com
api.example.com
passport.example.com
admin.example.com
```

### 推荐网站

**「crt.sh」**

```
https://crt.sh/
```

查询时可以搜索：

```
%.example.com
```

还可以配合：

**「1. Censys」**
地址：`https://search.censys.io/`

**「2. Shodan」**
地址：`https://www.shodan.io/`

证书透明度有时能够发现常规子域名工具没有找到的历史资产。

---

## 八、DNS 信息收集

对子域名进行整理以后，需要继续查询 DNS。

重点关注：

```
A
AAAA
CNAME
MX
NS
TXT
```

### 本地工具

Windows：

```
nslookup example.com
```

Linux/macOS：

```
dig example.com
```

### 在线网站

**「1. DNSdumpster」**
地址：`https://dnsdumpster.com/`

**「2. DNSChecker」**
地址：`https://dnschecker.org/`

**「3. ViewDNS」**
地址：`https://viewdns.info/`

我们主要想搞清楚：

```
域名
 ↓
CNAME
 ↓
CDN / 云服务
 ↓
最终服务
```

DNS 信息还能帮助识别邮件服务、CDN、云厂商和第三方 SaaS。

---

## 九、空间测绘搜索

空间测绘是 SRC 信息收集中非常重要的一环。

### 常见平台

**「1. FOFA」**
地址：`https://fofa.info/`

**「2. Hunter」**
地址：`https://hunter.qianxin.com/`

**「3. ZoomEye」**
地址：`https://www.zoomeye.org/`

**「4. Shodan」**
地址：`https://www.shodan.io/`

**「5. Quake」**
地址：`https://quake.360.net/quake/`

**「6. Censys」**
地址：`https://search.censys.io/`

它们可以帮助我们从：

```
域名
IP
证书
Title
ICON
组件
备案信息
```

继续扩展资产。

不同平台的查询语法并不完全一致，建议以各平台当前语法文档为准。

---

## 十、IP资产收集

域名整理完成以后，可以开始建立：

```
域名 → IP
```

映射关系。

例如：

```
api.example.com      1.1.1.1
oa.example.com       2.2.2.2
mail.example.com     3.3.3.3
```

### 推荐工具/网站

**「1. nslookup」**
地址：`Windows 系统自带`

**「2. dig」**
地址：`https://www.isc.org/bind/`

**「3. DNSChecker」**
地址：`https://dnschecker.org/`

**「4. ViewDNS」**
地址：`https://viewdns.info/`

建议建立 `assets.csv`，至少记录：

```
Domain
IP
Port
Title
Status
Technology
Source
Remark
```

这样后面不会越来越乱。

---

## 十一、CDN识别

拿到 IP 以后，不要马上认为：

> ❝
>
> 这个 IP 就是目标服务器。
>
> ❞

很多网站前面都有 CDN、WAF、负载均衡或云加速。

### 推荐工具/网站

**「1. CDNCheck」**
地址：`https://cdncheck.tools/`

**「2. DNSChecker」**
地址：`https://dnschecker.org/`

**「3. SecurityTrails」**
地址：`https://securitytrails.com/`

**「4. ViewDNS」**
地址：`https://viewdns.info/`

可以结合：

```
DNS解析
CNAME
不同地区DNS结果
历史DNS
证书
空间测绘
```

综合判断。

---

## 十二、历史DNS与历史IP

企业迁移服务器以后可能出现：

```
新IP → 有CDN/WAF

旧IP → 历史上曾承载业务
```

常见思路：

```
域名
 ↓
历史DNS
 ↓
历史IP
 ↓
空间测绘
 ↓
重新确认资产归属
```

### 推荐网站

**「1. SecurityTrails」**
地址：`https://securitytrails.com/`

**「2. ViewDNS IP History」**
地址：`https://viewdns.info/iphistory/`

**「3. VirusTotal」**
地址：`https://www.virustotal.com/`

**「4. DNSlytics」**
地址：`https://dnslytics.com/`

> ❝
>
> \*\*历史关联不等于当前授权。\*\*发现历史 IP 后，应重新确认是否仍属于目标以及是否处于 SRC 授权范围。
>
> ❞

---

## 十三、端口与服务信息

确认属于授权范围的 IP 后，可以进一步了解暴露服务。

常见 Web 端口：

```
80
443
8080
8443
8000
8888
```

### 推荐工具

**「1. Nmap」**
地址：`https://nmap.org/`

**「2. Naabu」**
地址：`https://github.com/projectdiscovery/naabu`

**「3. Masscan」**
地址：`https://github.com/robertdavidgraham/masscan`

例如，对**「明确授权」**的目标进行有限端口检查：

```
naabu -host example.com -p 80,443,8080,8443
```

或者：

```
nmap -sV -p 80,443,8080,8443 example.com
```

SRC 场景尤其需要控制扫描速率、扫描范围和请求数量。

---

## 十四、Web存活探测

收集几百个子域名以后，一个一个打开显然不现实。

### 推荐工具：httpx

GitHub：

```
https://github.com/projectdiscovery/httpx
```

基础使用：

```
httpx -l domains.txt -title -status-code -o live.txt
```

这样可以得到：

```
URL
状态码
Title
```

完整流程：

```
example.com
   ↓
Subfinder
   ↓
domains.txt
   ↓
httpx
   ↓
live.txt
```

---

## 十五、Title 收集

Title 是非常容易被低估的信息。

例如：

```
统一身份认证平台
XX管理后台
订单管理系统
API Documentation
Swagger UI
XX测试平台
XX运营后台
```

### 推荐工具

**「1. httpx」**
地址：`https://github.com/projectdiscovery/httpx`

**「2. WebBatchRequest」**
地址：`https://github.com/ScriptKid-Beta/WebBatchRequest`

httpx 可以直接：

```
httpx -l domains.txt -title -status-code
```

建议最终保存：

```
URL + Status + Title + Technology
```

---

## 十六、Web指纹识别

我们关心：

```
CMS
框架
中间件
Web Server
编程语言
前端框架
后台系统
开源组件
版本
```

### 推荐工具

**「1. Wappalyzer」**
地址：`https://www.wappalyzer.com/`

**「2. ObserverWard」**
地址：`https://github.com/0x727/ObserverWard_0x727`

**「3. EHole」**
地址：`https://github.com/EdgeSecurityTeam/EHole`

**「4. TideFinger」**
地址：`https://github.com/TideSec/TideFinger`

例如识别出：

```
Spring Boot
ThinkPHP
WordPress
Jenkins
Nginx
Apache
Vue
React
```

后续分析方向就会更清晰。

---

## 十七、目...