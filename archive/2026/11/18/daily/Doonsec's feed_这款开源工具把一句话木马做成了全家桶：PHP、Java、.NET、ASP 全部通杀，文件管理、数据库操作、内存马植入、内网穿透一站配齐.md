---
title: 这款开源工具把一句话木马做成了全家桶：PHP、Java、.NET、ASP 全部通杀，文件管理、数据库操作、内存马植入、内网穿透一站配齐
url: https://mp.weixin.qq.com/s/6wrt5jTWJZvV51sf11h0vQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:46.628192
---

# 这款开源工具把一句话木马做成了全家桶：PHP、Java、.NET、ASP 全部通杀，文件管理、数据库操作、内存马植入、内网穿透一站配齐

# 这款开源工具把一句话木马做成了全家桶：PHP、Java、.NET、ASP 全部通杀，文件管理、数据库操作、内存马植入、内网穿透一站配齐

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明：本文仅用于技术研究与已授权环境下的安全测试，禁止在未获授权的系统或网络中使用，产生的全部后果由使用者自行承担。

## 重点导读概述

Behinder（冰蝎）是一款以动态二进制加密为核心思路的网站管理客户端，服务端与客户端分离：服务端是一段可植入 Web 应用的单文件代码，客户端是 JavaFX 编写的跨平台桌面程序。

从 GitHub 仓库结构看，master 分支只保留 README 与 SECURITY policy 两份文档，不含工程源码；客户端程序、插件与服务端模板以 Release 压缩包形式分发，最新公开版本为 v4.1（2023 年 8 月发布），工程化程度体现为随包附带 SQLite 数据文件、Plugins 插件目录、server 服务端模板目录与独立的更新日志。

从功能覆盖看，它把远程文件读写、命令执行、数据库查询、内存马注入、网络隧道、资产扫描、插件扩展等能力集中在同一个图形界面内，服务端侧按语言拆成 PHP、Java（JSP/JSPX）、C#（ASP/ASPX/ASHX）四套实现，跨语言、跨中间件的适配工作基本由客户端承担。

## 重点导读架构

### PART 01分层

* 表现层：JavaFX 界面，FXML 描述布局，Controller 绑定事件
* 服务层：Console、File、Plugin、Tunnel、PortScan、Offline、BShell 等业务服务
* 通信层：ShellService、Params、Crypt、AESCryptor、CustomCryptor、ICrypt
* 持久层：ShellManager、ShellDao、HostDao、ServiceDao、TunnelDao、TransProtocolDao、PluginDao、DBManager
* 实体层：Shell、Host、Service、Tunnel、Plugin、TransProtocol、BShell
* 载荷层：php、java、csharp、asp 四组功能载荷
* 插件层：Plugins 目录，index.htm 描述界面，payload 目录存放多语言实现

### PART 02载荷体系

功能不写在服务端文件里，而是拆成独立载荷类，由客户端按需组合并加密下发。

* 命令执行：Cmd、RealCMD
* 文件管理：FileOperation、Transfer
* 数据库操作：Database
* 内网探测：BasicInfo、Scan、NewScan、ServiceScan
* 内存马：MemShell、BShell、Loader、LoadNativeLibrary
* 隧道代理：PortMap、ReversePortMap、SocksProxy、RemoteSocksProxy、Proxy
* 外连回连：ConnectBack
* 扩展入口：Plugin、Echo、Utils

### PART 03服务端

服务端为一行到几十行的加载器，负责解密请求体并反射执行载荷。

* PHP：读取 php://input，AES128 或异或解密，按竖线切分出函数名与参数，eval 执行
* JSP：自定义 ClassLoader 继承类，defineClass 加载解密后的字节码，反射实例化
* ASPX/ASHX：RijndaelManaged 解密请求体，Assembly.Load 加载程序集并实例化
* 密钥传递：服务端把密钥写入 Session，载荷从 Session 读取

### PART 04客户端

* 单 jar 交付，内置 JavaFX 与依赖库
* data.db 使用 SQLite 存储资产、隧道、插件与协议配置
* 启动即进入主窗口，标签页对应文件、命令、数据库、隧道、插件等模块

## 重点导读加密

### PART 05密钥派生

连接密码经 MD5 计算后取前 16 位作为 AES 密钥，服务端与载荷共享同一密钥字符串；PHP 侧通过 Session 变量传递，Java 与 .NET 侧直接写入代码常量或 Session。

### PART 06内置模板

内置模板以数据结构形式保存在 TransProtocol 表中，每条记录关联名称、语言类型与加解密代码片段。

* default\_xor：密钥字节循环异或
* default\_xor\_base64：异或后 Base64
* default\_aes：AES-128-ECB 与 PKCS5Padding
* aes\_with\_magic：AES 加密后追加随机字节，尾部长度由密钥前两位十六进制模 16 决定
* default\_image：明文嵌入 PNG 负载，响应剥离头部后还原
* default\_json：以 JSON 字段承载 Base64 密文

### PART 07自定义协议

v4.0 起传输协议不再硬编码，客户端提供协议的增删改查、模板套用与在线连通性校验；服务端在解析时按当前协议的解密代码处理请求体，协议变更即时生效，无需重启客户端。

## 重点导读功能

### PART 08文件管理

* 目录浏览、文件读取、在线编辑与保存
* 上传下载，v4.0 支持多线程大文件传输与百分比进度显示
* 目录内文件打包压缩与时间戳修改
* 中文路径与编码兼容处理，PHP 侧针对 UTF-8 与 GBK 互转

### PART 09命令执行

* 虚拟终端支持交互式输入，可使用 vi、top 等依赖终端状态的程序
* RealCMD 载荷用于获取真实命令行环境
* 兼容禁用函数列表，PHP 载荷按 system、proc\_open、passthru、shell\_exec、exec、popen 顺序探测可用执行接口

### PART 10数据库

* 通过 JDBC 驱动访问数据库，支持自动上传驱动
* 表结构浏览、字段查看、条件查询与结果导出
* 连接配置可保存复用

### PART 11内存马

* Java Agent 无文件落地注入，注入前进行 CPU 架构判断
* 内存马载荷类名随机化
* 注入模块适配 Tomcat、JBoss、WebLogic 等容器

### PART 12内网穿透

* 端口映射与反向端口映射，把内网监听端口暴露至本地或远端 VPS
* Socks 代理与远端 Socks 代理，基于 HTTP 隧道转发，PHP 侧不依赖 socket 扩展
* 多层子 Shell 穿透
* 反弹连接支持直连本地、局域网与 VPS

### PART 13扫描

* 主机存活扫描、端口扫描、服务识别
* 资产信息以平行世界视图集中管理

### PART 14插件

插件系统开放给第三方扩展，随包内置的服务扫描、JND 注入、SSH 助手、HTTP 助手、Solr 利用、存活检测等插件；插件界面用 HTML 编写，载荷同样按语言分目录组织。

## 重点导读兼容

* 客户端运行环境：JRE 8 起，v4.1 覆盖 JDK 8 至 JDK 20
* 服务端运行环境：.NET 2.0 以上、PHP 5.3 至 7.4、Java 5 以上
* 中间件适配：Tomcat 10 及使用 jakarta API 的容器、Exchange、Zimbra 等定制环境

## 重点导读演进

* v3.0 系列补齐交互式终端、内存马注入、反向端口映射、批量存活检测
* v4.0 引入传输协议自定义、离线缓存、插件开放、多线程大文件传输
* v4.0.7 修复 JavaFX WebView 中 JavaScript 内容可控导致的安全漏洞
* v4.1 增加 ashx 类型支持，兼容 JDK 20

## 重点导读风险

* 客户端与载荷内置了针对检测与查杀的规避逻辑，v3.0 起包含内存马防查杀机制与反 RASP 处理
* 载荷具备反弹连接与代码执行能力，落地后可被直接用于二次攻击
* 该类工具在国内安全事件中常被黑产批量使用，运维侧应把 Web 应用目录中新出现的单文件加载器、异常 Session 写入与异常外连行为纳入基线巡检

## 重点导读开源地址

本文介绍的项目开源地址如下：

本公众号非项目作者，仅做技术分享。

```
https://github.com/rebeyond/Behinder
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqQxX9SjGUY7lq88XAoyQ3EopLqUsh2JoAHn8VN75E95vhQAnIQuESiaZukVfHwnznd9MjwzcQxqMglEIXWhD500gJxicAotK1so/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqibmqzqChNo7kFrU5wFDdUlE22azvp7fS8ww4UviaOHChUpYeiboY3odzqx0hJamO0YjNXyQUV6IkwkNSYGJgTY0CdggcO1gyOQQ/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过