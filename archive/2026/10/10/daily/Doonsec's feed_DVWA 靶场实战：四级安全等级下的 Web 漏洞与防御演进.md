---
title: DVWA 靶场实战：四级安全等级下的 Web 漏洞与防御演进
url: https://mp.weixin.qq.com/s/Kz-OdYfRI-cCVeGwRRYhpQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:36.621916
---

# DVWA 靶场实战：四级安全等级下的 Web 漏洞与防御演进

# DVWA 靶场实战：四级安全等级下的 Web 漏洞与防御演进

原创

不懂安全的运维
不懂安全的运维

运维安全入门

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上一章我们用 SQLi-Labs 把 SQL 注入彻底拆开看了。但现实中，一个 Web 系统的漏洞从来不是孤立存在的——它面前有登录校验、有输入过滤、有 WAF，身后还有 CSRF 令牌、文件上传、会话管理。

这一章介绍 **DVWA（Damn Vulnerable Web Application）**。它最大的特色不是漏洞多，而是**提供了低、中、高、Impossible 四档安全等级**——这正是它区别于普通靶场的地方：同一个漏洞，你可以同时看到「裸奔」和「加固后」两种形态，把防御机制的作用量化在眼前。

**🛡️ 授权声明**　本文所有演示均在本地 Docker 环境中完成。对生产系统进行安全测试，必须先取得书面授权并约定测试窗口。

本文目录

1. DVWA 是什么，四档安全等级才是灵魂
2. 靶场架构与模块清单
3. Docker 部署：从 0 到可访问
4. 源码部署与 MariaDB 初始化
5. 核心机制：难度等级是如何生效的
6. 实战一：Brute Force 暴力破解与真实加固
7. 实战二：SQL Injection 与 CSRF Token 的攻防
8. 实战三：File Inclusion 本地/远程包含
9. 实战四：File Upload 文件上传绕过
10. 实战五：Weak Session 与 JWT 会话安全
11. 常见错误与排错清单
12. 等保视角：DVWA 各模块的合规映射
13. 总结

## 01DVWA 是什么，四档安全等级才是灵魂

DVWA 由 Ethical Hackers 社区维护，在 GitHub 上是 `digininja/DVWA`。官方定位是：*「一个故意设计为脆弱的 PHP/MySQL Web 应用，用于练习和演示 Web 应用安全课程」*。

和其他靶场相比，DVWA 有一个决定性的设计：**安全等级（Security Level）**。它位于页面左下角的 `DVWA Security` 菜单，包含四档：

| 等级 | 名称 | 防护状态 | 适合阶段 |
| --- | --- | --- | --- |
| Low | 低 | 几乎无防护，直接拼接 SQL/系统命令 | 理解漏洞原理 |
| Medium | 中 | 增加部分参数处理与简单过滤 | 学习基础绕过 |
| High | 高 | 严格过滤 / 类型约束 / 命令白名单 | 理解有效防御 |
| Impossible | 不可能 | 参数化查询、Prepared Statement | 理解根治方案 |

**💡 提示****为什么这个设计如此重要？**因为大多数教程只教你「怎么打」，不告诉你「为什么打不动了」。在 DVWA 里你可以亲手验证：把等级切到 High，同样一个注入 payload 会直接失效；切到 Impossible，源码里会明确写出 `prepare()` 和参数化写法。**这才是完整的知识闭环。**

**界面说明** DVWA 左侧栏底部是 Security 等级下拉菜单，四个档位分别是 Low、Medium、High、Impossible，可随时切换。建议按 Low → Medium → Impossible 的顺序把同一道题做三遍，直观感受过滤规则如何逐级收紧、防护代码如何从「完全不校验」演进到「参数化查询」，这是理解等保 2.0 中输入验证与代码审计要求的最快路径。

## 02靶场架构与模块清单

DVWA 的代码结构非常清晰，每个漏洞模块是一个独立目录，每个难度等级对应一个独立源码文件。例如 `vulns/` 目录下：

同一漏洞的四个等级各有一份源码，可直接对照阅读

```
vulns/ ├── exec/ │   ├── index.php          # Low  版 │   ├── index.medium.php   # Medium 版 │   ├── index.high.php     # High  版 │   └── index.impossible.php  # Impossible 版 ├── sqli/ ├── upload/ ├── fia/ └── ...
```

这意味着你可以**一边打，一边看源码**，这是理解「防御到底做了什么」最高效的方式。建议通关顺序：**先在 Low 打完所有模块，再回到每个模块看 Medium/High/Impossible 的源码差异**。

### DVWA 完整模块清单

| 模块 | 漏洞类型 | OWASP 对应 | 难度分布 |
| --- | --- | --- | --- |
| Brute Force | 弱口令 / 认证缺陷 | A07 身份识别失效 | Low/Medium/High |
| Command Injection | OS 命令注入 | A03 代码注入 | Low/Medium/High |
| CSRF | 跨站请求伪造 | A01 访问控制失效 | Low/Medium/High |
| File Inclusion | 本地/远程文件包含 | A03 代码注入 | Low/Medium/High |
| File Upload | 任意文件上传 | A04 不安全设计 | Low/Medium/High |
| Weak Passwords | 弱口令生成 | A07 身份识别失效 | Low/Medium/High |
| SQL Injection | SQL 注入 | A03 代码注入 | Low/Medium/High |
| SQL Blind | SQL 盲注 | A03 代码注入 | Low/Medium/High |
| Weak Session | 会话固定/劫持 | A07 身份识别失效 | Low/Medium |
| XSS DOM | DOM 型跨站脚本 | A03 代码注入 | Low/Medium/High |
| XSS Reflected | 反射型 XSS | A03 代码注入 | Low/Medium/High |
| XSS Stored | 存储型 XSS | A03 代码注入 | Low/Medium/High |
| JavaScript | 客户端校验绕过 | A04 不安全设计 | Low/Medium/High |
| Open Redirect | 开放重定向 | A01 访问控制失效 | Low/Medium/High |
| CSP Bypass | 内容安全策略绕过 | A05 安全配置错误 | Low/Medium/High |

**💡 提示**　注意 `Impossible` 等级并不覆盖所有模块——有些漏洞（如部分 XSS）本身就没有「完全不可能」的实现，DVWA 会在该等级下直接禁用相应功能。这本身也是一种工程现实的表达。

## 03Docker 部署：从 0 到可访问

DVWA 官方在 2021 年后已把 Docker Compose 作为主要推荐方式，并且**默认端口从 80 改成了 4280**。很多老教程还写着 `http://localhost/`，那是过时的。

### 方式一：官方 docker compose（推荐）

端口 4280 是官方当前默认值，不是 80

```
git clone https://github.com/digininja/DVWA.git cd DVWA docker compose up -d  # 浏览器访问 # http://localhost:4280
```

### 方式二：指定配置文件启动

DVWA 仓库提供多份 compose 文件：`docker-compose.yml`（常规）、`docker-compose.test.yml`（测试环境）。常规部署还支持通过环境变量初始化数据库口令：

环境变量优于命令行明文传参，避免密码进入 shell 历史

```
# .env 文件（放在 compose 文件同级目录） COMPOSE_PROJECT_NAME=dvwa DVWA_USERNAME=admin DVWA_PASSWORD=admin  docker compose up -d
```

### 启动后必做的初始化

第一次访问 `http://localhost:4280`，页面下方会出现红色的 `Setup / Reset Database` 链接，**必须点击它**，DVWA 才会创建数据库表和初始数据。这一步经常被忽略，导致后面所有模块都报「Table doesn't exist」。

**⚠️ 注意**　如果点击 Setup 后仍报错，检查日志：`docker compose logs -f dvwa`，常见原因是 MariaDB 尚未完全初始化就执行了建表脚本，这时**等 30 秒后重新点击 Setup**即可。

常用运维命令

```
docker compose ps                # 确认容器状态 docker compose logs -f           # 实时日志排错 docker compose down              # 停止环境 docker compose down -v           # 停止并删除数据卷（重置环境）
```

**⚠️ 注意**　依旧建议 compose 中把端口写成 `"127.0.0.1:4280:80"`，只监听本机回环地址。**含高危漏洞的服务绝不应暴露在可路由网络**——这是靶场使用中最重要的一条安全纪律。

**界面说明** DVWA 首页把所有练习按漏洞类型平铺成导航：Brute Force、Command Injection、CSRF、File Inclusion、File Upload、SQL Injection、Weak Session、Insecure CAPTCHA 等。每个模块内部再按 GET / POST / Session 拆成若干子题，点击条目进入对应关卡页面，右上角有 Submit 提交框用于验证攻击是否成功。

## 04源码部署与 MariaDB 初始化

如果你要改源码、或者需要长期保存练习进度，走源码部署。

```
git clone https://github.com/digininja/DVWA.git cd DVWA  # 1) 启动数据库 docker run -d --name dvwa-db \   -e MYSQL_ROOT_PASSWORD=root \   -e MYSQL_DATABASE=dvwa \   -p 127.0.0.1:3306:3306 \   -v dvwa-db:/var/lib/mysql \   mariadb:10.11  # 2) 等待数据库就绪 docker exec dvwa-db mysqladmin ping --silent  # 3) 等待后手动初始化（重启一次即可完成建表） docker restart dvwa-db
```

### 配置文件说明

DVWA 的核心配置在 `config/config.inc.php.dist`，首次运行需复制为 `config.inc.php`：

```
cp config/config.inc.php.dist config/config.inc.php  # 关键配置项 $dvwaDefaultSecurityLevel = 'low'; $dvwaDefaultSecurityLevel = 'impossible';   # 仅本地练习可设此值 define('DB_SERVER', '127.0.0.1'); define('DB_DATABASE', 'dvwa'); define('DB_USER', 'root'); define('DB_PASSWORD', 'root');
```

**⚠️ 注意**　官方明确提示：**不要把 DVWA 部署在有其他真实服务的机器上**，也不要用高权限数据库账号。DVWA 的配置文件里数据库口令是明文存储的，任何能读到该文件的人都能拿到数据库权限。

## 05核心机制：难度等级是如何生效的

这是 DVWA 最值得讲清楚的一个机制。等级切换**不是**简单地在前端加个遮罩，而是**服务端根据配置决定加载哪个 PHP 文件**。

等级通过 GET 参数 Security 传入，服务端动态 include 对应文件

```
// vulns/sqli/index.php 的核心逻辑 $data = dbQuery("SELECT * FROM users WHERE user='$user' AND password='$pass';");  // 载入对应等级的源码 if (file_exists(DVWA_WEB_PAGE_PATH . "vulns/{$page}/index.{$_GET['Security']}.php")) {     include(DVKA_WEB_PAGE_PATH . "vulns/{$page}/index.{$_GET['Security']}.php"); } else {     // 该等级未实现此模块     http_response_code(404);     exit; }
```

看懂这段代码，你就理解了 DVWA 的设计精髓：**同一个业务逻辑，四份完全不同的实现**。攻击者的每一步尝试，都可以立刻在源码里找到对应。

### Impossible 等级的源码才是精华

以 SQL 注入模块为例，Impossible 版本是这样的：

Impossible = 参数化查询 + CSRF Token + POST 方法限制，三重防护

```
// index.impossible.php // 数据访问层使用参数化查询 $data = $DB->prepare(     'SELECT * FROM users WHERE user = ? AND password = ?' );  // 调用 anti-CSRF token 校验 if (!checkToken($_GET['CSRFToken'], $_SESSION['token'])) {     http_response_code(403);     exit; }  if ($_SERVER['REQUEST_METHOD'] == 'POST') {     $user = $_POST['username'];     $pass = $_POST['password'];     $data->execute([$user, $pass]);   // 参数化，结构与数据分离     ... }
```

**💡 提示**　请注意最后一行：`$data->execute([$user, $pass])`。参数化查询的精髓在于——**SQL 语句的结构在执行前就已被数据库解析并锁定**，用户输入只是作为纯数据填进去，*永远不可能改变语法结构*。这就是为什么它对所有注入手法（包括你还没学到的那些）都天然免疫。

**💡 提示**　CSRF Token 的作用也要讲清楚：`Security=Impossible` 时，页面会生成一个随机会话令牌藏在表单里，提交时必须原样带回。攻击者即使能构造出合法请求，**也无法预测这个令牌**，因为它与受害者会话绑定且一次一换。

## 06实战一：Brute Force 暴力破解与真实加固

Brute Force 模块是一个没有验证码、没有锁定、没有限速的登录框。这在现实中早就被禁用了——但正是这种「裸奔」状态，让你看清了防护机制各自在防什么。

### Low 等级：完全裸奔

无验证码、无锁定、无延迟、用户名字段可注入

```
# Low 源码：无任何校验，直接查库 if (isset($_POST['Login'])) {     $user = $_POST['username'];     $pass = md5($_POST['password']);     $data = dbQuery("SELECT * FROM users WHERE user='$user' AND password='$pass';"); }
```

**⚠️ 注意**　Low 级的用户名参数同样可注入。一个 3 行的脚本就能判断用户是否存在：`admin' AND SLEEP(3)--+`，这说明**「用户名枚举」在没有任何防护时是零成本的**。

### Medium 等级：加了锁定与延迟

Medium 的防护：会话级锁定 + 服务端强制延迟

```
if (login_failed() >= 3) {          // 失败 3 次锁定会话     sleep(2);                      // 每次尝试强制延迟 2 秒     $page .= '<p>Brute force protection activated</p>';     exit; }
```

### High 等级：换了一套思路

High：无论成功与否都延迟，消除「响应时间差异」这一侧信道

```
if (login_failed() >= 3) {     $page .= '<p>Too many failed logins.</p>';     exit; } sleep(2);   // 无论成败都延迟，阻止时序侧信道
```

**⚠️ 注意****Low/Medium/High 的一个本质缺陷是：**锁定和延迟都只作用于*当前会话*。攻击者只要**每次换一个会话（比如清除 Cookie）就能无限重试**。真正的防护必须做到「跨会话、以账号为维度」的锁定——这正是 Impossible 级采用 CSRF Token 的原因：令牌与服务端会话绑定，攻击者无法自行生成。

**界面说明** DVWA 不做自动判题，每道题都要你自行取证。最稳妥的凭证有三种：提交框里回显出预期结果（如 SQLi 里拿到数据库版本号）、页面出现 flag 字符串、或弹窗 / 跳转出现预期页面。建议每关把终端命令与页面结果对照记录，形成可复查的通关台账，这也是等保测评里「漏洞验证需留存证据」的直接对应。

## 07实战二：SQL Injection 与 CSRF Token 的攻防

SQL 注入模块的设计很巧妙：**登录成功后服务端会告诉你注入是否成功**，这省去了手工判断回显的麻烦。

### Low 等级：经典字符型注入

注意 AND/OR 的运算优先级，这是 SQL 注入的必考点

```...