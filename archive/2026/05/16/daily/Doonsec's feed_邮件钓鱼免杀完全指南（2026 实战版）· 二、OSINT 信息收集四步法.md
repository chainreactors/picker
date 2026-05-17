---
title: 邮件钓鱼免杀完全指南（2026 实战版）· 二、OSINT 信息收集四步法
url: https://mp.weixin.qq.com/s/P6xV5_yhvX9UDM4wBL1i7w
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:42:32.298320
---

# 邮件钓鱼免杀完全指南（2026 实战版）· 二、OSINT 信息收集四步法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P8tspoQj3VoxheceVXPBSbRcWl2dLicO8gqGgdsV2RESLmMRvze2xDia9YtfPkVRdagFSE6ww24mwsFpOMYeYqT9bdJtYDia6m7D50yjZD1x2Q/0?wx_fmt=jpeg)

# 邮件钓鱼免杀完全指南（2026 实战版）· 二、OSINT 信息收集四步法

原创

IceByte
IceByte

IceByte-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/P8tspoQj3Vr3LwA37r7WI0JOMybuMl6fhkOyDXtYlocfFxSKET3AfOicz3cepzc2R61MSfxWkZJNiaick8yqUBibUEl54COsBu4Nlib7sO68fY50/640?wx_fmt=png&from=appmsg)

> **系列说明**：本文是《邮件钓鱼免杀完全指南（2026 实战版）》系列的第二篇。上篇建立了全链路攻击视野，本篇深入攻击链最前端——如何利用开源情报（OSINT）在不动声色间获取目标企业的完整邮箱清单和人员画像。

---

## 前言：为什么 OSINT 是钓鱼攻击的"七寸"？

大多数钓鱼攻击失败，不是因为载荷不够先进，而是因为**发错了人**。

* 把财务诈骗邮件发给实习生 → 被直接忽略
* 把 IT 钓鱼邮件发给 HR → 话题不对，警觉性高
* 用采购话术发给没有采购权限的员工 → 打开率极低

精准的 OSINT 信息收集，能让攻击者将**有限的钓鱼邮件配额**（企业邮件网关通常限制每小时发送量）用于最高价值目标。**OSINT 的质量直接决定了钓鱼攻击的成功率。**

根据 2025 年 Cozy Bear（APT29）攻击 Hydro-Québec 的事件复盘，攻击者花费了**超过 3 周时间**进行前期情报收集，最终针对 14 名高价值目标发送高度个性化钓鱼邮件，成功率 100%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3VqBH2lxFtJ5ktJY3Hzlpa9B6S40gWpn209hT6TAibibgFbEFkXVQyT3Kr8JVyZxicvoAKbKHETcdPWspuiasTYgRAibs4CPpS3g63fA/640?wx_fmt=png&from=appmsg)

---

## 第一步：域名发现与邮件系统指纹识别

### 1.1 提取企业邮箱域名

大多数企业的公开邮箱后缀可以通过以下途径获取：

**方法 A：企业官网"联系我们"页面**

几乎每家企业官网都有"联系我们"或"商务合作"页面，通常会列出类似 `contact@company.com` 或 `sales@company.com` 的联系方式。这就是企业的**主邮箱域名**。

**方法 B：招聘信息挖掘**

企业在智联招聘、BOSS 直聘、LinkedIn Jobs 发布的职位中，通常会留下 `hr@company.com` 或 `recruitment@company.com`。这类邮箱的域名通常是企业统一使用的。

**方法 C：WHOIS 历史记录**

有时企业更换过邮箱域名（如从 `company.net` 迁移到 `company.com`），旧的 WHOIS 记录或历史 DNS 解析记录中可能留有痕迹。可以使用 SecurityTrails 或 ViewDNS 查询历史 DNS 记录。

### 1.2 MX 记录分析（判断邮件系统类型）

获取域名后，第一步是通过 MX 记录判断目标使用的邮件系统——这决定了后续的投递策略。

```
# 查询 MX 记录
$ dig MX target-company.com +short

# 常见返回结果及其含义：
0 target-company-com.mail.protection.outlook.com.   # → Microsoft Defender for Office 365
10 inbound.mailguard.com.au.                          # → MailGuard（澳洲常用 SEG）
1 aspmx.l.google.com.                                 # → Google Workspace
10 mx1.coremail.cn.                                   # → Coremail（中国企业常用）
0 target-company-com.mxrecord.io.                     # → Mimecast
```

**不同邮件系统的攻击策略差异**：

| 邮件系统 | 绕过难度 | 典型弱点 | 推荐手法 |
| --- | --- | --- | --- |
| Microsoft Defender | ⭐⭐⭐⭐ | 用户安全意识高；沙箱强 | EchoSpoofing / 被入侵域名代发 |
| Google Workspace | ⭐⭐⭐ | DKIM 配置复杂易出错 | SPF 绕过 / 弱 DMARC 策略 |
| Coremail（中国） | ⭐⭐ | 已知漏洞多（CVE-2023-46809 等） | 直接利用 Coremail 漏洞 |
| Mimecast | ⭐⭐⭐⭐ | 附件沙箱极强 | HTML Smuggling（网关视角无害） |

### 1.3 自动化域名发现脚本

以下是一个简单的 Python 脚本，可以批量从企业官网抓取邮箱域名：

```
import requestsimport refrom urllib.parse import urljoin, urlparse
def extract_emails_from_url(url):    """从指定 URL 页面提取邮箱地址和域名"""    try:        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})        r.raise_for_status()        # 匹配邮箱正则        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', r.text)        return emails    except Exception as e:        print(f"[-] 无法访问 {url}: {e}")        return []
def discover_email_domain(company_name, website):    """自动化发现企业邮箱域名"""    parsed = urlparse(website)    base = f"{parsed.scheme}://{parsed.netloc}"
    pages_to_check = [        base,        urljoin(base, '/contact'),        urljoin(base, '/contact-us'),        urljoin(base, '/about'),        urljoin(base, '/team'),    ]
    all_emails = []    for page in pages_to_check:        emails = extract_emails_from_url(page)        all_emails.extend(emails)
    # 提取独特域名    domains = set(email.split('@')[1] for email in all_emails)    return list(domains), all_emails
# 使用示例domains, emails = discover_email_domain("ExampleCorp", "https://example.com")print(f"[+] 发现域名: {domains}")print(f"[+] 发现邮箱: {emails[:5]}")  # 只打印前 5 个
```

---

## 第二步：邮箱枚举（Email Enumeration）

确认域名后，下一步是**批量收集该域名下的有效邮箱地址**。

### 2.1 theHarvester：最强大的多源邮箱枚举工具

`theHarvester` 是 Kali Linux 内置的 OSINT 工具，支持从 **50+ 个数据源** 批量收集邮箱、子域名、虚拟主机等信息。

**安装**：

```
$ pip3 install theHarvester# 或者从 GitHub 克隆最新版$ git clone https://github.com/laramies/theHarvester.git$ cd theHarvester && pip3 install -r requirements.txt
```

基础用法：

```
# 从所有数据源搜索目标域名$ theHarvester -d target-company.com -b all
# 指定特定数据源（速度更快）$ theHarvester -d target-company.com -b google,bing,linkedin,hunter
# 限制结果数量（避免被目标发现）$ theHarvester -d target-company.com -b google,bing -l 100
# 输出到文件（XML/JSON/HTML）$ theHarvester -d target-company.com -b all -f results.html
```

**输出示例**（部分）：

```
[*] 开始搜索 target-company.com
[*] 搜索引擎结果:[+] 找到 23 个邮箱地址:------------------------zhangsan@target-company.comlisi@target-company.comwangwu@target-company.comhr@target-company.comit-support@target-company.com...
[+] 找到 8 个子域名:------------------------mail.target-company.comvpn.target-company.comoa.target-company.com...
[+] 找到 3 个虚拟主机:------------------------184.23.45.67:8080...
```

**theHarvester 的 50+ 数据源分类**：

| 类型 | 代表数据源 | 特点 |
| --- | --- | --- |
| 搜索引擎 | Google、Bing、Baidu、DuckDuckGo | 覆盖广，但结果重复率高 |
| 商业平台 | Hunter.io、Clearbit、EmailValidator | 数据质量高，但需 API Key |
| 代码仓库 | GitHub、GitLab、Bitbucket | 可发现开发者邮箱 + 代码泄露 |
| 社交平台 | LinkedIn、Twitter、Reddit | 需要登录，部分数据需付费 |
| DNS 服务 | DNSDumpster、SecurityTrails | 发现子域名和 MX 记录 |
| 泄露数据库 | HaveIBeenPwned、LeakCheck | 历史泄露数据，可能已失效 |

### 2.2 LinkedIn 员工信息挖掘

LinkedIn 是获取企业员工姓名和职级的**最精准来源**。问题是 LinkedIn 有严格的反爬虫机制，直接爬取会被封号。

**方法 A：linkedin2username.py**

这是一款专为 OSINT 设计的工具，可以通过 LinkedIn 企业页面批量提取员工姓名，并自动生成常见邮箱格式（如 `firstname.lastname@company.com`）。

```
$ git clone https://github.com/initstring/linkedin2username.git$ cd linkedin2username$ pip3 install -r requirements.txt
# 使用你的 LinkedIn 账号登录（需要有效的 LinkedIn 账号）$ python3 linkedin2username.py -c target-company -n 50
```

**输出示例**：

```
[+] 找到 47 个员工:------------------------Zhang San (Senior Manager, IT Department)Li Si (HR Director)Wang Wu (CFO)...
[+] 生成可能的邮箱格式:zhangsan@target-company.coml.si@target-company.comwang.wu@target-company.com...
```

**方法 B：CrossLinked**

更先进的 LinkedIn 爬虫，利用 Google 搜索引擎间接获取 LinkedIn 员工信息（绕过 LinkedIn 反爬虫）：w

```
$ git clone https://github.com/m8sec/CrossLinked.git$ cd CrossLinked && pip3 install -r requirements.txt
$ python3 crosslinked.py -i target-company -o emails.txt
```

### 2.3 GitHub 代码泄露扫描

企业员工常将包含邮箱信息的代码推送到 GitHub（如 Git 配置、提交记录、`package.json` 中的 `author` 字段）。

**工具 A：gitrob**

自动扫描目标企业的 GitHub 组织，发现敏感文件和邮箱信息：

```
$ git clone https://github.com/michenriksen/gitrob.git$ cd gitrob && go build -o gitrob .
# 扫描目标 GitHub 组织$ ./gitrob organizations target-company
```

**工具 B：truffleHog**

专注于发现提交历史中的敏感信息（密码、API Key、邮箱）：

```
$ pip3 install truffleHog
# 搜索 GitHub 仓库中的敏感信息$ trufflehog github --repo https://github.com/target-company/main-repo
```

**真实案例**：2024 年，某互联网大厂的运维工程师将内部自动化脚本推送到个人 GitHub 仓库，脚本中包含 `it-admin@company.com:Password123` 的硬编码凭证。攻击者通过 `truffleHog` 扫描发现后，直接登录了企业 VPN。

### 2.4 文档元数据提取

企业公开发布的 PDF 报告、Word 文档、Excel 表格中，通常包含**作者邮箱**（存储在文件元数据的 `Author` 或 `Last Modified By` 字段）。

**工具：exiftool + Metagoofil**

```
# 使用 Metagoofil 自动化下载并分析文档元数据$ python3 metagoofil.py -d target-company.com -t doc,pdf,xls -l 50 -n 10 -o ./results/
# 输出示例：[+] 下载了 37 个文件[+] 提取到 28 个唯一邮箱:Author: zhangsan@target-company.comLast Modified By: lisi@target-company.com...
```

**手动验证**：也可以用 `exiftool` 直接分析单个文件：

```
$ exiftool downloaded_file.pdf | grep -i "author\|creator\|email"
```

### 2.5 商业平台：Hunter.io

Hunter.io 是目前最精准的邮箱枚举平台，它使用网页爬虫 + 邮件服务器验证 + 公开数据源聚合，提供极高的准确率。

**免费版限制**：每月 25 次查询。

**API 调用示例**（Python）：

```
import requests
API_KEY = "YOUR_HUNTER_API_KEY"domain = "target-company.com"
url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEY}"r = requests.get(url)data = r.json()
print(f"[+] 域名: {data['data']['domain']}")print(f"[+] 发现邮箱数量: {data['data']['stats']['emails']}")
for email in data['data']['emails']:    print(f"  - {email['value']} ({email['type']}, 置信度: {email['confidence']}%)")
```

**返回示例**：

```
{  "data": {    "domain": "target-company.com",    "emails": [      {        "value": "zhangsan@target-company.com",        "type": "personal",        "confidence": 98,        "sources": [{"domain": "target-company.com", "uri": "..."}]      }   ...