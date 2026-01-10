---
title: 【云安全专题-2】IAM 与 AK/SK 密钥泄露攻防实战
url: https://mp.weixin.qq.com/s/RMMiRXzsu9N3uJET0WaaFg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:22:36.964888
---

# 【云安全专题-2】IAM 与 AK/SK 密钥泄露攻防实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nibcyUyib4otzv0K7iaucluTdwzQfzg3KeK7y9uvHiaIzic9nM8I1fgWUTD6MRkRhqiaatVmt70JiajStWv5YVzjuicTGw/0?wx_fmt=jpeg)

# 【云安全专题-2】IAM 与 AK/SK 密钥泄露攻防实战

原创

Ca1m

FunnyHacking

![]()

在小说阅读器中沉浸阅读

#### 00 引言

在传统的网络安全模型中，我们习惯于筑起高高的防火墙，守护内网边界。但在云时代，基础设施代码化，API 接口公网化，**传统的网络边界正在消融，取而代之的是“身份边界”**。

Gartner 曾预言：“到 2023 年，75% 的云安全故障将由客户对身份、访问和特权管理不当引起。”

而在云身份安全中，**AK/SK (Access Key / Secret Key)** 就是那把通往王座的钥匙。一旦泄露，攻击者无需突破任何防火墙，即可长驱直入，接管整个云数据中心。本章，我们将深入 IAM 的心脏，解构这场关于“身份”的攻防战。

#### 01 IAM 核心概念：云上的“身份证”与“马甲”

在开始实战前，我们必须厘清 IAM (Identity and Access Management) 的几个核心概念。很多初学者容易搞混“用户”和“角色”。

* • **User (用户)**：

+ • 这是云上的“实体人”。可以是员工张三，也可以是一个应用程序。
+ • **凭证形式**：控制台密码（用于 Web 登录）或 **AK/SK**（用于 API 调用）。
+ • **风险点**：AK/SK 是长效凭证，除非手动轮换，否则**永不过期**。

* • **Role (角色)**：

+ • 这更像是一个“马甲”或“帽子”。它没有密码，也没有长期的 AK/SK。
+ • **特点**：谁戴上这个帽子（AssumeRole），谁就拥有了帽子的权限。
+ • **凭证形式**：STS Token（临时凭证），通常有效期仅 1-12 小时。

* • **Policy (策略)**：

+ • 规定了“谁能干什么”的 JSON 文档。例如 `Allow: s3:ListBucket`。

> **💡 知识点**：AK/SK 通常由 `AccessKeyId`（20位左右字符）和 `SecretAccessKey`（40位左右字符）组成。对于 AWS，以 `AKIA` 开头代表长期用户密钥，以 `ASIA` 开头代表临时角色密钥。

---

#### 02 泄露源头：密钥是因何“离家出走”的？

根据实战经验，AK/SK 的泄露途径主要集中在以下三个重灾区：

**1. 代码与配置文件的硬编码 (Hardcoding)**
开发人员为了图省事，直接将 AK/SK 写在代码里。

* • **前端 JS**：这是重灾区。打包后的 Webpack 文件中常含有 OSS/S3 的上传密钥。
* • **GitHub/GitLab**：即便你删除了文件，密钥依然躺在 `.git` 的历史提交记录里（利用 `TruffleHog` 可挖掘）。
* • **移动端 APP**：反编译 APK 后，在 `res/strings.xml` 或 `classes.dex` 中常能发现惊喜。

**2. 云主机元数据服务 (Instance Metadata Service)**
这是云环境特有的攻击面。

* • **原理**：云主机为了获取自身的角色权限，会访问内网地址 `169.254.169.254`。
* • **攻击链**：Web 应用存在 **SSRF 漏洞** -> 攻击者请求元数据地址 -> 获取关联角色的临时凭证 (STS Token)。

**3. 第三方工具配置不当**
例如 `.aws/credentials` 文件被恶意软件窃取，或者 Jenkins、Airflow 等 CI/CD 平台的控制台未授权访问，导致环境变量中的密钥泄露。

---

这是一个非常实战且关键的问题。AK/SK（Access Key / Secret Key）泄露往往是云上资产沦陷的“第一块多米诺骨牌”。

对于安全从业者来说，发现泄露的途径主要分为三个场景：**前端 JS 泄露（你的重点关注）**、**代码仓库泄露（GitHub 等）**以及**历史记录泄露**。

---

#### AK/SK 泄露挖掘指南：工具与技巧

##### 场景一：Web 前端 JS 文件泄露（重灾区）

**原理：** 开发人员为了图省事（例如前端直接上传文件到 OSS/S3），有时会将 AK/SK 硬编码在前端 JavaScript 代码中。虽然代码经过 Webpack 打包压缩，但字符串常量通常不会被加密。

**主动发现工具与方法：**

**1. 浏览器插件 + 开发者工具 (DevTools)**

* • **方法：** F12 打开开发者工具，全局搜索（Ctrl+Shift+F）。
* • **搜索关键词：** `accessKey`、`secretKey`、`aliyun`、`oss`、`AKIA` (AWS特征)、`LTAI` (阿里云特征)。
* • **插件推荐：** **FindSomething** 或 **Moeals**。这些 Chrome 插件会自动在网页加载时匹配敏感信息并弹窗提示，非常适合被动发现。

**2. SecretFinder (JS 敏感信息提取神器)**

* • **介绍：** 这是一个 Python 脚本，专门用于爬取网页中的 JS 文件，并利用正则提取 API Key、Token 等。
* • **特点：** 能处理被压缩混淆的 JS，内置了大量云厂商的正则规则。
* • **使用：**

  ```
  python3 SecretFinder.py -i https://example.com -e
  ```
* • **点评：** 挖掘 JS 泄露的必装工具。

**3. Burp Suite 插件：HaE (Highlighter and Extractor)**

* • **介绍：** 它是 Burp 的一款被动扫描插件，通过自定义正则高亮显示流量中的敏感信息。
* • **配置：** 你需要在 HaE 的配置文件中添加云厂商 AK 的正则（见后文）。当你在测试网站时，一旦流量或 JS 文件中出现了 AK，Burp 的 History 列表会直接标红，非常直观。

**4. Nuclei (自动化漏洞扫描)**

* • **介绍：** 目前最火的漏洞扫描器。
* • **用法：** Nuclei 有专门的 `token-spray` 模板，可以扫描 JS 文件中的 Token。

  ```
  nuclei -u https://example.com -t exposures/tokens/
  ```

---

##### 场景二：代码仓库与历史记录泄露

**原理：** 开发人员不小心把包含密钥的配置文件（如 `.env`, `config.js`）提交到了 GitHub，或者虽然删除了文件，但**密钥还留在 Git 的 commit 历史记录里**。

**主动发现工具：**

**1. TruffleHog (特鲁法猪)**

* • **核心能力：** 它不仅扫描当前代码，还会**深度遍历 Git 的所有历史 Commit 记录**。很多时候，黑客就是通过翻“两年前的提交记录”找到的密钥。
* • **特点：** 基于“高熵”（字符串随机性）和正则检测。

  ```
  trufflehog git https://github.com/org/repo.git
  ```

**2. Gitleaks**

* • **核心能力：** 速度极快，适合集成在 CI/CD 流程中，也适合本地扫描。它内置了极其丰富的规则集（AWS, Alibaba, Tencent, Slack 等）。

**3. GitGuardian (SaaS 服务)**

* • **核心能力：** 商业化产品（有免费版），准确率极高，误报率低。如果你是扫描自己的企业资产，推荐接入这个。

---

##### 核心技法：正则表达式 (Regex)

工具只是外壳，**正则才是灵魂**。无论是配置 HaE、Burp 还是自己写脚本，你必须掌握主流云厂商的 Key 特征。

建议收藏以下正则：

* • **AWS (亚马逊)**

+ • Access Key ID (特征：`AKIA` 开头，20位字符):
  `(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])`
+ • 精确匹配 AKIA/ASIA:
  `(A3T[A-Z0-9]|AKIA|AGPA|AIDA|ARGB|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}`

* • **Alibaba Cloud (阿里云)**

+ • Access Key ID (特征：`LTAI` 开头，通常 16-24 位):
  `(LTAI)[a-z0-9A-Z]{20}`

* • **Tencent Cloud (腾讯云)**

+ • SecretId (特征：`AKID` 开头):
  `(AKID)[a-z0-9A-Z]{32}`

* • **Google Cloud (GCP)**

+ • API Key (特征：`AIza` 开头):
  `AIza[0-9A-Za-z\\-_]{35}`

* • **通用高熵检测 (简单粗暴)**

+ • 寻找 "AccessKey" 附近的疑似 32 位字符串：
  `(?i)((access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key|alias_pass|alicloud_access_key|amazon_secret_access_key|amazonaws|ansible_vault_password|aos_key|api_key|api_key_secret|api_key_sid|api_secret|api.googlemaps AIza|apidocs|apikey|apiSecret|app_debug|app_id|app_key|app_secret|app_token|appKey|appSecret|appspot|auth_token|authorizationToken|authsecret|aws_access|aws_access_key_id|aws_bucket|aws_key|aws_secret|aws_secret_key|aws_token|AWSSecretKey)[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"]([0-9a-zA-Z\-_=]{8,64})['\"]`

---

这里也附上大佬曾哥总结的一些特征和正则，已经挺全的了：

###### Amazon Web Services

亚马逊云计算服务 (Amazon Web Services, AWS) 的 Access Key 开头标识一般是 "AKIA"。

```
^AKIA[A-Za-z0-9]{16}$
```

* • Access Key ID: 20个随机的大写字母和数字组成的字符，例如 AKHDNAPO86BSHKDIRYTE
* • Secret Access Key ID: 40个随机的大小写字母组成的字符，例如 S836fh/J73yHSb64Ag3Rkdi/jaD6sPl6/antFtU（无法找回丢失的 Secret Access Key ID）。

###### #Google Cloud Platform

Google Cloud Platform (GCP) 的 Access Key 开头标识一般是 "GOOG"。

```
^GOOG[\w\W]{10,30}$
```

* • 服务账号的JSON文件中包含了Access Key和密钥的信息，其中Access Key为`client_email`，其长度不固定，由字母、数字和特殊字符组成。
* • 密钥（Key）的长度为256个字符，由字母、数字和特殊字符组成。

###### #Microsoft Azure

Microsoft Azure 的 Access Key 开头标识一般是 "AZ"。

```
^AZ[A-Za-z0-9]{34,40}$
```

* • Azure AD Application的Client ID通常用作Access Key，长度为36个字符，由字母和数字组成。
* • 对于Azure AD Application的密钥（Secret），长度为44个字符，由字母、数字和特殊字符组成。

###### #IBM Cloud

IBM 云 (IBM Cloud) 的 Access Key 开头标识一般是 "IBM"。

```
^IBM[A-Za-z0-9]{10,40}$
```

或者是以下规则：

```
[a-zA-Z0-9]{8}(-[a-zA-Z0-9]{4}){3}-[a-zA-Z0-9]{12}$
```

###### #Oracle Cloud

Oracle云 (Oracle Cloud) 的 Access Key 开头标识一般是 "OCID"。

```
^OCID[A-Za-z0-9]{10,40}$
```

###### #阿里云

阿里云 (Alibaba Cloud) 的 Access Key 开头标识一般是 "LTAI"。

```
^LTAI[A-Za-z0-9]{12,20}$
```

* • Access Key ID长度为16-24个字符，由大写字母和数字组成。
* • Access Key Secret长度为30个字符，由大写字母、小写字母和数字组成。

###### #腾讯云

腾讯云 (Tencent Cloud) 的 Access Key 开头标识一般是 "AKID"。

```
^AKID[A-Za-z0-9]{13,20}$
```

* • SecretId长度为17个字符，由字母和数字组成。
* • SecretKey长度为40个字符，由字母和数字组成。

###### #华为云

华为云 (Huawei Cloud) 的 Access Key 是20个随机大写字母和数字组成，较难用正则表达式匹配。

```
[A-Z0-9]{20}
```

###### #百度云

百度云 (Baidu Cloud) 的 Access Key 开头标识一般是 "AK"。

```
^AK[A-Za-z0-9]{10,40}$
```

###### #京东云

京东云 (JD Cloud) 的 Access Key 开头标识一般是 "JDC\_"。

```
^JDC_[A-Z0-9]{28,32}
```

###### #字节跳动火山引擎

字节跳动火山引擎 (Volcengine) 的 Access Key 开头标识一般是 "AKLT"，长度小于256位。

```
^AKLT[a-zA-Z0-9-_]{0,252}
```

###### #UCloud

UCloud (UCloud) 的 Access Key 开头标识一般是 "UC"

```
^UC[A-Za-z0-9]{10,40}$
```

###### #青云

青云 (QingCloud) 的 Access Key 开头标识一般是 "QY"。

```
^QY[A-Za-z0-9]{10,40}$
```

###### #金山云

金山云 (Kingsoft Cloud) 的 Access Key 开头标识一般是 "AKLT"。

```
^AKLT[a-zA-Z0-9-_]{16,28}
```

###### 联通云

联通云 (China Unicom Cloud) 的 Access Key 开头标识一般是 "LTC"。

```
^LTC[A-Za-z0-9]{10,60}$
```

###### 移动云

移动云 (China Mobile Cloud) 的 Access Key 开头标识一般是 "YD"。

```
^YD[A-Za-z0-9]{10,60}$
```

###### 电信云

中国电信云 (China Telecom Cloud) 的 Access Key 开头标识一般是 "CTC"。

```
^CTC[A-Za-z0-9]{10,60}$
```

###### 一云通

一云通 (YiYunTong Cloud) 的 Access Key 开头标识一般是 "YYT"。

```
^YYT[A-Za-z0-9]{10,60}$
```

###### 用友云

用友云 (Yonyou Cloud) 的 Access Key 开头标识一般是 "YY"。

```
^YY[A-Za-z0-9]{10,40}$
```

###### 南大通用云

南大通用云 (OUCDC) 的 Access Key 开头标识一般是 "CI"。

```
^CI[A-Za-z0-9]{10,40}$
```

###### G-Core Labs

G-Core Labs 的 Access Key 开头标识一般是 "gcore"

```
^gcore[A-Za-z0-9]{10,30}$
```

#### 03 攻防实战：拿到 Key 之后的第一步

当你发现了一对 AK/SK，千万不要直接盲目操作。

**第一步：我是谁？（身份验证）**
使用 AWS CLI 或阿里云 CLI 验证密钥有效性：

```
# AWS
aws sts get-caller-identity --profile target
# 阿里云
aliyun sts GetCallerIdentity
```

**第二步：我能干什么？（权限枚举）**
云厂商的权限策略成千上万，手动测试是不可能的。这里我们需要借助自动化工具（这块会单独出一个文章，就讲云安全攻防的相关工具，关注一下后边更精彩）。

* • **推荐工具**：**CF (Cloud Exploitation Framework)**

  ```
  cf alibaba perm
  ```

  CF 会自动通过 API 探测当前 Key 是否拥有 `DescribeInstances` (查主机)、`ListBuckets` (查存储) 或 `CreateUser` (建用户) 等高危权限。

---

#### 04 高阶攻击：IAM 提权之路 (Pri...