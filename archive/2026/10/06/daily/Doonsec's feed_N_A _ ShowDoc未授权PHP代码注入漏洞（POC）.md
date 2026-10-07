---
title: N/A | ShowDoc未授权PHP代码注入漏洞（POC）
url: https://mp.weixin.qq.com/s/VgA-72KbHkw8NIHgf_2bWw
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:40.882504
---

# N/A | ShowDoc未授权PHP代码注入漏洞（POC）

# N/A | ShowDoc未授权PHP代码注入漏洞（POC）

alicy
alicy

信安百科

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> **免责声明：**本文仅供安全研究与防御学习交流。漏洞技术细节均来源于公开可查证的安全研究资料，请勿将相关技术用于非授权测试，由此产生的一切后果与作者无关。

##

## 0x00、前言

ShowDoc 是国内开发者 star7th 维护的开源文档协作系统，基于 ThinkPHP 构建，支持用 Markdown 编写 API 文档、数据字典与在线手册，官方称有超过 10 万个互联网团队在使用，腾讯、百度、华为、字节跳动等均在其列，大量实例以私有化方式部署在企业内网。

2026 年 8 月 25 日，该系统的一处未授权 PHP 代码注入漏洞被提交至长亭漏洞平台；9 月 2 日官方发布 v3.9.3 修复；9 月 4 日微步情报局公开复现——恶意 PHP 代码不需要任何凭据，仅凭一个精心构造的"用户名"即可写入服务器数据库，而承载它的数据库文件恰好以 .php 为后缀躺在 Web 根目录，一次普通的 GET 请求就能让代码落地执行。

##

## 0x01、漏洞描述

 ShowDoc 旧版注册接口 `registerByVerify` 中的未授权 PHP 代码注入漏洞，接口对 username 参数仅做 trim() 处理、无字符白名单，攻击者可将包含 PHP 标签的恶意字符串作为用户名原样提交并存入 SQLite 数据库。

ShowDoc 默认 SQLite 部署时，数据库文件 `Sqlite/showdoc.db.php` 位于 Web 根目录且以 .php 结尾——攻击者直接 GET 请求该文件，Nginx 会按后缀交给 PHP-FPM 解析，PHP 词法器扫描文件内容时遇到注入的 PHP 标签即执行代码，最终以 Web 服务用户身份执行任意系统命令，可落地持久化 Webshell。利用仅需两个条件：注册功能开启（默认开启）与默认 SQLite 部署，全程无需认证与用户交互。

##

## 0x02、CVE 编号

| 项目 | 内容 |
| --- | --- |
| CVE 编号 | 无（未分配 CVE / CNVD 编号） |
| 其他编号 | XVE-2026-54414（微步）/ QVD-2026-61708（奇安信）/ CT-5505993（长亭） |
| 漏洞类型 | 未授权 PHP 代码注入 → 远程代码执行（RCE） |
| 影响组件 | ShowDoc（ThinkPHP + SQLite） |

##

## 0x03、影响版本

| 产品 | 受影响版本 | 修复版本 |
| --- | --- | --- |
| ShowDoc | ≤ 3.9.2（默认 SQLite 部署且注册功能开启的场景） | 3.9.3（2026-09-02 发布） |

两点边界说明：该漏洞的触发依赖 SQLite 数据库文件位于 Web 根目录，从原理上看采用 MySQL 部署的实例不在此攻击路径上；注册功能已关闭的实例则无法被写入恶意用户名。但历史版本长期未升级的实例仍建议一并升级。

##

## 0x04、漏洞详情

### 1、注入点：只 trim、不校验的用户名

ShowDoc 基于 ThinkPHP 3.x，出问题的旧版注册 API 位于 `/server/index.php?s=/Api/User/registerByVerify`。根据公开分析，接口的关键行为如下：

```
// 漏洞要素摘录（源自公开分析，非逐字源码）
接口: POST /server/index.php?s=/Api/User/registerByVerify
取参: getParam($request, 'username', '')
过滤: 仅 trim()，无字符白名单校验（存入 TEXT 字段）
落点: Sqlite/showdoc.db.php（Database.php 中 DB_NAME
      默认值，位于 Web 根目录）
触发: GET /Sqlite/showdoc.db.php?cmd=...
修复: v3.9.3 新增 username 字符白名单校验
```

接口取参后仅做 trim() 去除首尾空白，没有任何字符类型校验，恶意用户名作为普通 TEXT 值进入 INSERT 语句落库。注册虽有验证码环节，但公开复现中攻击者使用 OCR 自动识别即可通过，不构成实际门槛。

### 2、落地点：一个以 .php 结尾的数据库

ShowDoc 默认使用 SQLite，数据库文件名由 `server/app/Common/Database/Database.php` 中 DB\_NAME 常量决定，默认值为 `Sqlite/showdoc.db.php`。给数据库文件加 .php 后缀的设计意图，是防止数据库被当作静态文件直接下载——请求它时会被交给 PHP 解析而非吐出二进制内容。但副作用是：库文件的全部内容（包括其中的用户名字符串）都会进入 PHP 词法扫描范围。

### 3、触发链：一次 GET 请求

攻击者以含 PHP 标签的用户名完成注册后，payload 即随 INSERT 写入 `Sqlite/showdoc.db.php`。随后请求 `GET /Sqlite/showdoc.db.php`，Nginx 按 .php 后缀将请求交给 PHP-FPM；PHP 词法器扫描该文件时，把 PHP 标签之外的内容当作内联 HTML 原样输出，而扫描到注入的 PHP 标签时则执行其中的代码——命令以 Web 服务用户身份执行（公开复现环境中为 application 用户）。

完整攻击链四步：

**第 1 步 · 过验证码：**访问注册接口，自动或人工识别验证码；

**第 2 步 · 恶意注册：**提交包含 PHP 代码片段的 username，payload 随 INSERT 语句写入数据库文件；

**第 3 步 · 触发执行：**GET 请求数据库文件，Nginx 交由 PHP-FPM 解析，注入代码执行；

**第 4 步 · 持久化：**执行任意系统命令，落地持久化 Webshell，完全控制服务器。

### 4、官方修复

v3.9.3 为 username 增加了字符白名单校验，从源头封死 PHP 标签注入：

```
// v3.9.3 修复：username 增加字符白名单校验
^[a-zA-Z0-9_\-\x{4e00}-\x{9fa5}]{2,30}$
// 仅允许字母、数字、下划线、连字符与常用中文，长度 2-30
```

##

## 0x05、个人观察与判断

**设计点评：**“给数据库加 .php 后缀防下载”是典型的以安全为名的 hack——防住了静态下载，却把整个数据库暴露给 PHP 词法器，任何入库的用户可控字符串都成了潜在代码。数据库文件本就不该放在 Web 根目录。

**趋势思考：**ShowDoc 这类广泛私有化部署的开源系统是攻击者的批量猎物——其 2020 年的文件上传漏洞（CNVD-2020-26585）今年 4 月已被观测到在野利用。内部文档系统往往“部署即遗忘”、常年不升级，却承载着 API 密钥等敏感信息。

**排查建议：**升级至 3.9.3+；排查用户表中含 PHP 标签特征的异常用户名与 /Sqlite/ 目录访问日志；将数据库移出 Web 根目录或在 Web 服务器封禁 \*.db.php 访问；非必要关闭注册（options 表 register\_open 置 0）。

##

## 0x06、参考链接

https://rivers.chaitin.cn/vuldb/02c546e6-0b10-4936-b1dc-84c07399f35d

长亭百川云漏洞详情（评分、时间线与缓解措施）

https://github.com/star7th/showdoc/releases/tag/v3.9.3

ShowDoc v3.9.3 官方修复版本（厂商公告）

https://mrxn.net/jswz/ShowDoc-registerByVerify-username-rce.html

mrxn.net 技术分析（核心技术分析：注入点与触发链）

---

> **— END —**
>
> **❤ 如果觉得有帮助，点个红心支持一下吧。**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Whm7t4Je6uo1JKMTjhMXktIqbicYCN6oicwhNlcFIITib1fhU7xDnYZaOHP6kgm9Ih2JQkB1Lfx0V4iaJRickUYibQBg/0?wx_fmt=png)

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