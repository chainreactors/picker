---
title: Adminer 5.4.2 三个0-day漏洞分析与修复建议
url: https://mp.weixin.qq.com/s/AhltFvD-T53Is1fIMbNR5A
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:09.829827
---

# Adminer 5.4.2 三个0-day漏洞分析与修复建议

# Adminer 5.4.2 三个0-day漏洞分析与修复建议

原创

Dr. Clay
Dr. Clay

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M2rER7kVkwkT1faaElEficzLWwqFc6CD94YMO3F1moeibgH8YiaB7dWibLGRRWbBtKPG0eGXqibZQdvjdKxOcb6DmKGAXiaQnft92jo/640?from=appmsg)
> **导语**：2026年4月6日，Voorivex红队向Adminer官方上报了三个0-day漏洞，覆盖预认证RCE、存储型XSS和认证后RCE三种攻击路径。官方在5.4.3版本中修复了全部问题，但这些漏洞的存在本身就值得所有Adminer用户警惕——一个被遗忘在服务器上的adminer.php，可能正在静默等待被攻陷。

---

## 一、漏洞概述

Adminer是一款流行的开源数据库管理工具，以单个PHP文件的形式分发，全球有数百万开发者将其部署在服务器上用于数据库管理。这种"一个文件搞定一切"的便利性，恰恰也是安全风险的高发地带——当这个文件暴露在公网时，攻击面随之成倍放大。

本次Voorivex团队披露的三个0-day漏洞信息如下：

| 漏洞编号 | 类型 | 认证要求 | CVSS | 影响版本 |
| --- | --- | --- | --- | --- |
| CVE-2026-56705 | MSSQL PDO DSN注入RCE | 预认证 | **9.8** | < 5.4.3 |
| CVE-2026-56704 | MySQL版本字符串存储型XSS | 预认证 | 6.1 | < 5.4.3 |
| CVE-2026-56703 | SQLite VACUUM INTO文件写入RCE | 已认证 | 7.2 | < 5.4.3 |

其中最危险的CVE-2026-56705无需任何认证，只要Adminer配置了MSSQL/Azure SQL后端，攻击者即可在未登录的情况下直接获取服务器远程命令执行权限。

---

## 二、CVE-2026-56705：MSSQL PDO DSN注入（预认证RCE）

### 攻击面为何如此之大

CVE-2026-56705之所以危险，首先在于它的攻击条件极为宽松：攻击者只需要能够访问Adminer的登录页面，无需任何凭证即可发起攻击。其次，MSSQL/Azure SQL在企业环境中极为常见，许多开发者为了方便管理数据库，会将adminer.php保留在Web根目录下，这就给了攻击者天然的人口。

### 漏洞原理：ODBC参数的注入链

漏洞的根源在于Adminer在构建MSSQL PDO DSN时，未对用户输入的服务器地址进行充分的过滤。攻击者通过在连接参数中注入分号（;），可以在DSN字符串中追加任意ODBC驱动参数。

攻击者利用的核心ODBC参数是`TraceFile`和`TraceOn`。当DSN被构造为如下形式时：

```
sqlsrv:Server=127.0.0.1;TraceFile=shell.php;TraceOn=1
```

ODBC驱动在建立连接前会先打开`TraceFile`指定的文件，并向其中写入连接元数据。关键在于，这个写入过程会将攻击者控制的`UID={...}`字段一并记录进文件——而这个字段的内容完全可以注入PHP代码。

### 攻击流程

整个攻击链分为以下步骤：

攻击者构造一个恶意服务器地址，例如`Server=127.0.0.1;TraceFile=shell.php;TraceOn=1;UID=<?php system($_GET['cmd']);?>`，在登录页面的服务器地址字段中提交。Adminer直接将该字段拼接入PDO DSN字符串并传给sqlsrv PDO驱动。ODBC驱动尝试连接时，先将连接元数据（含攻击者注入的PHP代码）写入`shell.php`，最后连接失败返回错误。但恶意文件已经成功落地到Web目录。下一步攻击者只需请求`shell.php?cmd=id`即可在服务器上执行任意命令。

这是一个典型的"副作用型"文件写入漏洞——连接本身失败了，但写入操作在失败之前就已经完成。

### 影响范围

所有使用Adminer连接MSSQL或Azure SQL数据库，且adminer.php暴露在公网的部署均受影响。由于该漏洞在登录前即可触发，攻击门槛接近于零。

---

## 三、CVE-2026-56704：MySQL版本字符串存储型XSS

### CSP绕过的精妙之处

Content Security Policy（CSP）是现代浏览器提供的核心安全机制之一，能够有效阻止存储型XSS攻击的脚本执行。然而CSP并非无懈可击——如果攻击者能够控制一个带有有效随机数（nonce）的script标签内容，CSP的防护就会完全失效。

CVE-2026-56704正是利用了这一点。Adminer在登录页面会显示所连接的数据库服务器的版本信息，这个版本字符串被直接渲染到一个带有`nonce`属性的`<script>`标签内：

```
<script nonce="random_token">
  var version = "5.7.33";
</script>
```

Adminer的SQL查询层本已对ATTACH等危险命令做了限制，但MySQL的版本字符串是一个特殊的存在——它并非来自用户查询，而是来自数据库服务器本身。攻击者只需在网络中部署一个恶意的MySQL服务器，当Adminer尝试连接时，服务器返回的版本字符串会被Adminer直接渲染进DOM。

Voorivex团队发现的绕过技巧在于：版本字符串需要匹配一个数字格式的正则表达式，但攻击者可以通过精心构造的非数字字符破坏正则匹配，从而将该字符串"逃逸"出JavaScript上下文，插入任意HTML或脚本内容。由于渲染位置本身在一个有效的`<script nonce>`标签内，浏览器会正常执行其中的JavaScript代码。

### 实际危害

配合钓鱼攻击或中间人攻击，攻击者可以窃取登录凭据、劫持会话令牌，甚至进一步利用窃取的凭证登录Adminer并触发CVE-2026-56703实现RCE。

---

## 四、CVE-2026-56703：SQLite VACUUM INTO文件写入RCE

### 被遗漏的VACUUM命令

Adminer对SQLite的ATTACH命令做了安全限制，阻止用户附加外部数据库文件。但安全研究人员发现，ATTACH的封禁名单中遗漏了同样危险的`VACUUM INTO`命令。

`VACUUM INTO`本用于将SQLite数据库内容导出到文件，其语法为`VACUUM INTO 'filename'`。当攻击者通过Adminer执行以下SQL时：

```
ATTACH DATABASE '/var/www/html/shell.php' AS shell;
CREATE TABLE shell.pwn (data TEXT);
INSERT INTO shell.pwn VALUES ('<?php system($_GET["cmd"]); ?>');
VACUUM INTO '/var/www/html/shell.php';
```

SQLite将把一个完整的数据库文件（含PHP payload）写入指定路径。与CVE-2026-56705不同，这个漏洞需要攻击者已经拥有Adminer的有效登录凭证，属于"认证后RCE"范畴，但其危害依然是远程代码执行。

### 为什么VACUUM INTO被遗漏

开发者的防护思路是封禁`ATTACH`命令本身，防止用户操作外部数据库文件。但`VACUUM INTO`并不依赖ATTACH——它可以直接从当前数据库向任意路径写入数据，因此在ATTACH封禁规则中完全看不到它的身影。这是一个典型的"封禁名单不完整"的安全缺陷。

---

## 五、修复建议

首先，强烈建议所有Adminer用户立即升级到5.4.3或更高版本。Adminer的更新非常直接——只需下载最新的adminer.php替换旧文件即可。

对于暂时无法升级的环境，建议采取以下临时缓解措施：将adminer.php移除出Web根目录或配置访问控制，仅允许可信IP访问；使用MSSQL驱动的用户应特别警惕，因为CVE-2026-56705在登录前即可触发；如果必须保留公网访问，请务必检查是否使用了最小权限原则，禁止Adminer连接生产数据库。

---

## 六、总结与趋势预测

Adminer的安全问题，本质上是"便捷性与安全性的永恒博弈"。单个PHP文件的分发模式让它极易部署，但也意味着安全更新依赖开发者主动替换文件，而非通过包管理器的自动更新机制推送给用户。

从这次漏洞披露来看，企业环境中数据库管理工具的暴露面是一个被长期忽视的攻击向量。CTO和DevOps团队应当将adminer.php纳入资产清点范围，定期审查其访问控制策略和版本状态。

可以预见，随着自动化漏洞扫描工具的普及，这类"被遗忘的adminer.php"将成为红队和攻击者的重点目标。未来的安全研究可能会继续挖掘Adminer在其他数据库后端（如PostgreSQL、Oracle）上的类似攻击路径。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OZy9g4s1epKDWs72j82DO1zbDhCoQISI9wsyG0ZFBN6jbxCpiazE80L56FcodzibdDEq4dD1c3ISqZRA1pcicI918StJgJTMPSu4/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MMepeGzUK4gkWP5LhsxQlkc1h93r9MVNLFCy6UzJ2OibmPGf3BlkRe5560iawd29jrzHC3icwh0tvltNJklTibIjMt7vzvpKNug9k/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MjDSWmnHhbgJ1eS4Yvml7ibD9J2fLsH4oBaJTVkJZUfYl88aa9xkjWUzSjSfrKAXhxBURHTPEKbArQukZnBfSJbwgTADDGVxOY/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NI3OFKkCrhYmeibFIFFAdxRVM4Zp4iczua4a3sicIia1v1icMcsqkCZZr2gwgblzbrZZ7f33vbH8yayWjcxbuOVtj0qm85zyPpV00U/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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