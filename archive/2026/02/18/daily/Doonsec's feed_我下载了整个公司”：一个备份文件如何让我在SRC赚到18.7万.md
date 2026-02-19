---
title: 我下载了整个公司”：一个备份文件如何让我在SRC赚到18.7万
url: https://mp.weixin.qq.com/s/rNcv2r4lharFrbpkCSSZUQ
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:12:56.419136
---

# 我下载了整个公司”：一个备份文件如何让我在SRC赚到18.7万

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3oR6eMARh6xKWT1ePDIqSViaF7ZSNcfqGlcicf0zG6icRYx5t0icRgvNAOgh8gvDm6I6ibeIrjyHA9Ou6yDZU9iaSoH8tlFQV1Y1nJnPibjicGfpgms/0?wx_fmt=jpeg)

# 我下载了整个公司”：一个备份文件如何让我在SRC赚到18.7万

进击的HACK

![]()

在小说阅读器中沉浸阅读

以下文章来源于逍遥子讲安全
，作者逍遥安全实验室

![](http://wx.qlogo.cn/mmhead/naPHoFY2n5T1dyry62h352tUwxDvKDibwloicSNw3zl7W7LkPqQbpAPmnUvcVqYOYVEhtKCJmJq3U/0)

**逍遥子讲安全**
.

安全引路 | 红队渗透测试丨内网渗透 | SRC漏洞挖掘等安全技术

**当所有人都盯着SQL注入和越权时，聪明猎人正在下载你的整个业务系统——只需一条未被删除的备份文件。**

去年，我靠“源码泄漏”这一单点漏洞类型，在12家SRC提交了43个有效漏洞，其中**高危23个，总奖金18.7万元**。最贵的一单来自某大厂：一个藏在`/backup/2023-old.zip`的完整源代码包，我花3天审计出7个0day，最终拿到**35,000元**额外奖励。

这不是运气，是系统化方法论。本文将首次完整公开我的**源码泄漏狩猎工业化体系**——从情报发现、深度审计到武器化利用的全链路实战手册。

---

## 第一章 源码泄漏：为什么是SRC漏洞的“最高性价比”？

### 1.1 源码泄漏的四个碾压级优势

| 维度 | 传统黑盒测试 | 源码泄漏审计 | 优势倍数 |
| --- | --- | --- | --- |
| **漏洞发现效率** | 依赖扫描器+手工试探 | 直接阅读业务逻辑 | **10-50倍** |
| **0day发现概率** | 极低，需运气 | 系统性代码审计 | **∞** |
| **漏洞复杂度** | 多为简单注入/XSS | 反序列化、逻辑链等高危 | **5倍以上** |
| **奖金/积分** | 中低危为主 | 高危、严重占比80%+ | **3-10倍** |
| **提交通过率** | 70%左右 | 95%以上 | **极高** |

**一句话总结**：拿到源码，等于拿到了整个业务系统的**设计蓝图**——漏洞不再是“猜”出来的，而是“读”出来的。

### 1.2 源码泄漏的常见存在形态

```
text📁 网站根目录直接存放   ├── www.zip, web.rar, site.tar.gz, backup.sql   ├── .git/ , .svn/ , .idea/ , .DS_Store   ├── 2023-12-25.zip, 公司名-项目名.zip
📁 二级目录/隐藏路径   ├── /backup/, /temp/, /old/, /release/, /upload/, /download/   ├── /assets/, /static/, /public/, /dist/
📁 非标准端口/子域名   ├── dev.target.com, test.target.com, gitlab.target.com   ├── 8080, 8443, 9090, 7001
📁 第三方代码托管平台   ├── GitHub/Gitee/GitLab 公开仓库   ├── 网盘、文库、贴吧、CSDN
📁 互联网档案馆与快照   ├── Wayback Machine 历史版本   ├── 百度快照、Google缓存
```

## 第二章 工业化发现体系：如何将“偶然”变为“必然”

### 2.1 字典爆破：最直接、最有效

**核心思路**：不需要复杂技巧，把字典做到极致。

**我的专属备份文件字典**（节选，完整版700+条）：

```
python# 按频率排序，带权重的动态字典backup_dict = [    "www.zip", "web.zip", "site.zip", "website.zip", "wwwroot.zip",    "www.rar", "web.rar", "site.rar", "website.rar",    "www.tar.gz", "web.tar.gz", "site.tar.gz",    "backup.zip", "back.rar", "bak.zip", "old.zip",    "2024.zip", "2023.zip", "2022.zip", "2021.zip",    "2024-01-01.zip", "2023-12-31.zip", "release-1.0.zip",    "source.zip", "code.zip", "src.zip", "project.zip",    "app.zip", "application.zip", "api.zip", "admin.zip",    "dist.zip", "build.zip", "output.zip", "target.zip",    "database.zip", "db.zip", "sql.zip", "dump.zip",    "config.zip", "conf.zip", "setting.zip",    "upload.zip", "attachment.zip", "file.zip",    "www.7z", "web.7z", "site.7z",    "www.sql", "web.sql", "data.sql", "backup.sql",    "www.bak", "web.bak", "site.bak", "index.bak",    ".git", ".svn", ".env", ".config",    "Jenkinsfile", "Dockerfile", "docker-compose.yml",    "pom.xml", "build.gradle", "package.json", "composer.json",    "README.md", "CHANGELOG.md", "INSTALL.md",]
```

**爆破实战参数**（使用dirsearch/dirb/gobuster）：

```
bash# 高并发爆破，针对大目标gobuster dir -u https://target.com -w backup_super.txt -t 100 -x zip,rar,tar.gz,7z,sql,bak,tar# 带扩展名的智能模式dirsearch -u https://target.com -w backup_dict.txt -f -e zip,rar,7z,tar.gz,sql,tar,bak# 递归深度扫描（重要！）ffuf -u https://target.com/FUZZ -w backup_dict.txt -recursion -recursion-depth 3
```

**实战案例**：某招聘网站，扫描`/assets/`目录发现`assets.rar`，下载后得到前端源码，其中`config.js`硬编码阿里云OSS密钥，直接导致内部存储桶接管。**奖金：4,000元**。

### 2.2 版本控制系统泄漏（.git/.svn）

**Git泄露的终极利用工具链**：

```
bash# 1. 检测是否存在.git泄露git-hound --subdomain-file subs.txt --threads 100# 2. 自动下载所有可访问的.git文件./git_dumper.py https://target.com/.git/ output_dir/# 3. 恢复完整代码库git checkout --force# 4. 分析历史提交中的敏感信息（黄金）git log -p | grep -E "(password|secret|key|token|AKIA)"
```

**SVN泄露检测**：

```
bash# 检测.svn/entries文件curl https://target.com/.svn/entries# 下载整个.svn目录并重构./svn_extractor.py https://target.com/.svn/ output_dir/
```

**实战案例**：某金融科技公司主站无任何漏洞，但`test.target.com/.git/`可读。下载后查看`git log`，发现半年前的一次提交注释：“fix: remove hardcoded aws secret”。虽然该文件已被删除，但**历史版本**中仍保留着完整的AccessKey和SecretKey。**直接接管生产环境S3存储桶，奖金：8,000元**。

### 2.3 第三方代码托管平台狩猎

**GitHub高级搜索语法库**：

```
text# 组合搜索，精度提升10倍org:"target" AND ("backup" OR "config" OR "password")"target.com" filename:.env"target.com" extension:sql"target.com" "aws_access_key_id""target.com" path:config"target.com" "BEGIN RSA PRIVATE KEY"
```

**自动化监控方案**：

```
python# 使用GitDorker批量扫描python GitDorker.py -tf targets.txt -d dorks/alldorks.txt -o results# 结合Telegram机器人实时推送if "password" in result or "secret" in result:    send_to_telegram(f"新发现: {result['url']}")
```

**实战案例**：搜索`baidu.com extension:sql`，发现某第三方开发者上传的demo项目中包含`baidu_pay.sql`，内有**真实支付回调地址、商户密钥、测试账号密码**。通过该密钥可伪造支付成功通知。**奖金：12,000元**。

### 2.4 历史快照与互联网档案馆

**Wayback Machine 高级用法**：

```
bash# 获取目标所有历史URLwaybackurls target.com | grep -E "\.(zip|rar|tar|gz|sql|bak|git)"# 筛选特定时间段（漏洞高发期）waybackpy --domain target.com --from 2023 --to 2024 --get-urls | grep "backup"
```

**实战案例**：某SRC目标，当前站点无任何泄漏。通过Wayback查询，发现2022年8月的快照中存在`/download/website.zip`链接，但现已404。通过`archive.org`直接**下载历史快照版本**，得到当时泄露的源码。审计发现`class/config.php`包含数据库密码，且该密码至今未改。**拿下后台权限，奖金：5,000元。**

### 2.5 非标准路径与社会工程学组合拳

**技巧1：JS文件中提取隐藏路径**

```
javascript// 在某JS中发现var BACKUP_SERVER = "https://static-cdn.target.com/backup/";var VERSION = "v2.3.1";// 尝试拼接https://static-cdn.target.com/backup/v2.3.1.ziphttps://static-cdn.target.com/backup/release-v2.3.1.zip
```

****技巧2：HTML注释中的遗留信息****

```
html!-- 开发环境备份路径：\\192.168.1.100\backup\project\ -->!-- 测试账号: admin / 1qaz@WSX3edc -->
```

******技巧3：报错信息中的物理路径******

```
textWarning: include_once(/var/www/html/backup/config.php): failed to open stream
```

## 第三章 源码审计的“30分钟快速拿分法”

**目标**：不是做完整的代码审计，而是**在最短时间内找到最容易转化为SRC漏洞的高危点**。

### 3.1 第一优先级：硬编码与敏感信息（5分钟）

**自动扫描脚本**：

```
pythonimport re, osSENSITIVE_PATTERNS = {    'password': r'(?i)(password|pwd|passwd|pass)[\s]*[:=][\s]*["\']?([^"\'\s]+)',    'api_key': r'(?i)(api[_-]?key|apikey|secret[_-]?key|access[_-]?key)[\s]*[:=][\s]*["\']?([A-Za-z0-9_\-\.]{16,})',    'aws_key': r'(AKIA[0-9A-Z]{16})',    'private_key': r'-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----',    'jwt_token': r'eyJ[a-zA-Z0-9_-]{5,}\.[a-zA-Z0-9_-]{5,}\.[a-zA-Z0-9_-]{5,}',    'database_dsn': r'(?i)(mysql|postgres|mongodb|redis)://[^:]+:[^@]+@',    'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',    'ip_internal': r'\b(10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.|192\.168\.)\d+\.\d+\b',}def scan_secrets(root_dir):    findings = []    for root, dirs, files in os.walk(root_dir):        for file in files:            if file.endswith(('.php', '.py', '.js', '.java', '.properties', '.yml', '.env', '.conf', '.sql')):                path = os.path.join(root, file)                with open(path, 'r', errors='ignore') as f:                    content = f.read()                    for name, pattern in SENSITIVE_PATTERNS.items():                        matches = re.findall(pattern, content)                        if matches:                            findings.append((path, name, matches))    return findings
```

********实战案例**：某源码包解压后，5秒内发现`/config/database.php`中`DB_PASSWORD = "Root@123456"`，直接登录生产数据库，发现百万级用户明文手机号。**奖金：10,000元**。******

### 3.2 第二优先级：文件上传漏洞（10分钟）

**审计要点**：

* 上传接口是否校验文件类型（MIME、扩展名、文件头）
* 文件名是否可控（是否可路径穿越）
* 上传目录是否可执行脚本
* 是否存在二次渲染绕过

**经典绕过链案例**：

```
php// 某CMS上传代码$ext = pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);if (in_array($ext, ['jpg','png','gif'])) {    move_uploaded_file($_FILES['file']['tmp_name'], './uploads/'.$_FILES['file']['name']);}
```

**问题**：仅校验扩展名，未重命名，未校验文件内容。直接上传`shell.php.jpg`，Apache解析为`shell.php`（若配置不当）。**验证后提交，奖金：3,000元**。

### 3.3 第三优先级：反序列化与表达式注入（15分钟）

**快速定位**：

* Java：搜索`ObjectInputStream.readObject`、`FastJson.parse`、`Jackson.readValue`、`XStream.fromXML`
* PHP：搜索`unserialize`、`__destruct`、`__wakeup`
* Python：搜索`pickle.loads`、`yaml.load`、`eval`

**实战案例**：某电商系统使用`fastjson 1.2.24`，且代码中存在：

```
javaJSON.parseObject(request.getParameter("data"));
```

**无任何过滤**。直接使用`JNDI注入`Payload，成功执行命令。**奖金：8,000元**。

### 3.4 第四优先级：逻辑漏洞与越权（20分钟）

**审计思路**：

* 搜索`user_id`、`uid`、`userId`等参数，检查是否从客户端获取
* 搜索`isAdmin`、`role`、`permission`，检查是否可伪造
* 搜索`update`、`delete`、`modify`接口，看是否有权限校验

********典型案例**：******

```
php// 修改个人资料接口$user_id = $_POST['user_id'];...