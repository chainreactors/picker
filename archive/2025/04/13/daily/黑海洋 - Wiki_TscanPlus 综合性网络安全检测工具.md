---
title: TscanPlus 综合性网络安全检测工具
url: https://blog.upx8.com/4735
source: 黑海洋 - Wiki
date: 2025-04-13
fetch_date: 2025-10-06T22:05:26.624594
---

# TscanPlus 综合性网络安全检测工具

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# TscanPlus 综合性网络安全检测工具

发布时间:
2025-04-12

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
23152

## Tscanplus简介

一款综合性网络安全检测和运维工具，旨在快速资产发现、识别、检测，构建基础资产信息库，协助甲方安全团队或者安全运维人员有效侦察和检索资产，发现存在的薄弱点和攻击面。

## **【主要功能】**

 端口探测、服务识别、URL指纹识别、POC验证、弱口令猜解、目录扫描、UrlFinder、域名探测、网络空探、项目管理等。

## **【辅助功能】**

编码解码、加密解密、CS上线、反弹shell、杀软查询、提权辅助、常用命令、字典生成、JAVA编码、资产分拣、Hots碰撞、40xBypass、Jwt破解、Ip归属地查询等。

在2019年就用Python写过指纹识别工具—— [TideFinger](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1RpZGVTZWMvVGlkZUZpbmdlcg) ，并实现了一个免费在线的指纹检测平台——潮汐指纹 [finger.tidesec.com](https://blog.upx8.com/go/aHR0cDovL2Zpbmdlci50aWRlc2VjLmNvbS8) ， 目前已积累用户3万余人，每日指纹识别约2000余次，2023年初又基于Go语言开发了Go版的 [TideFinger\_Go](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1RpZGVTZWMvVGlkZUZpbmdlcl9Hbw) ，在web指纹和服务指纹的识别方面积累了一些经验。后来我们团队内部大佬基于Fscan开发了一个Tscan，主要是用于内部的POC收集整理并形成自动化武器库，可基于指纹识别结果对poc进行精准检测。无影(TscanPlus)就是以指纹和Poc为根基，扩展了多项自动化功能，可大大提高安全运维和安全检测的效率，方便网络安全从业者使用。

## **【特色功能】**

1、内置5.2W余条指纹数据，对1万个web系统进行指纹识别仅需8-10分钟，在效率和指纹覆盖面方面应该是目前较高的了。

2、在指纹探测结果中，对130多个红队常见CMS和框架、Poc可关联CMS进行了自动标注。内置大量高质量Poc，并可外接Nuclei、Afrog、Xray等Poc工具，可实现指纹和Poc的联动，根据指纹识别的结果自动关联Poc，并可直接查看poc数据包相关信息。

3、在创建IP端口扫描、Url扫描时，可关联Poc检测、密码破解、目录扫描等功能，发现匹配的服务或产品时会自动触发密码破解或poc检测。

4、内置34种常见服务的弱口令破解，可方便管理员对内网弱口令进行排查，为提高检测效率，优选并精简每个服务的用户名和密码字典。覆盖的服务包括：

```
SSH
RDP
SMB
MYSQL
SQLServer
Oracle
MongoDB
Redis
PostgreSQL
MemCached
Elasticsearch
FTP
Telnet
WinRM
VNC
SVN
Tomcat
WebLogic
Jboss
Zookeeper
Socks5
SNMP
WMI
LDAP
LDAPS
SMTP
POP3
IMAP
SMTP_SSL
IMAP_SSL
POP3_SSL
RouterOS
WebBasicAuth
Webdav
CobaltStrike
...
```

5、实现了编码解码、哈希计算、加密解密、国密算法、数据格式化、其他转换等共36种类型，其中编码解码类8种、哈希计算13种、加密解密9种、国密算法3种、数据格式化9种、其他2种。包含了AES、RSA、SM2、SM4、DES、3DES、Xor、RC4、Rabbit、Base64、Base32、URL、ASCII、各进制转换、字符串与进制转换、HTML、Unicode、MD5、Hmac、SM3、SHA1、SHA2、SHA3、NTLM、JSON格式化与压缩、XML格式化与压缩、IP地址与整数互转、String.fromCharCode、Unix时间戳互转、文本去除重复行、字母大小写、生成各类随机字符串、字符串反转、JWT解析与弱密码、一键解密OA等。

6、目录枚举默认使用HEAD方式，可对并发、超时、过滤、字典等进行自定义，内置了DirSearch的字典，可导入自己的字典文件，也可用内置字典fuzz工具进行生成。

7、内置各类反弹shell命令85条、Win内网(凭证获取、权限维持、横向移动)命令26类、Linux内网命令18类、下载命令31条、MSF生成命令21条、CS免杀上线命令等，可根据shell类型、操作系统类型、监听类型自动生成代码。

8、灵活的代理设置，可一键设置全局代理，也可以各模块单独开启代理功能，支持HTTP(S)/SOCKS5两种代理，支持身份认证。

9、快速的子域名探测，域名可联动其他子功能，可配置key后对接多个网络空间探测平台，一键查询去重。

10、内置资产分拣、JsFinder、Host碰撞、Jwt秘钥破解、IP查询、Windows提权辅助、杀软查询、shiro解密等各类工具。

## **【免责声明&使用许可】**

1、本工具禁止进行未授权商业用途，**禁止二次开发后进行未授权商业用途**。

2、本工具仅面向合法授权的企业安全建设行为，在使用本工具进行检测时，您应**确保该行为符合当地的法律法规**，并且已经**取得了足够的授权**。

3、如您在使用本工具的过程中存在任何**非法行为**，您需自行承担相应后果，我们将不承担任何法律及连带责任。

4、在安装并使用本工具前，请**务必审慎阅读、充分理解各条款内容，并接受本协议所有条款，否则，请不要使用本工具**。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。

## 更新日志

感谢各位师傅提出的宝贵修改建议和诸多bug！

v2.7.2 【2025.02.18】 增加MQTT端口破解功能、代理池增加根据关键词切换代理等

v2.7.1 【2025.01.23】 增加导出项目所有数据到Excel、代理池增加自动破解功能等

v2.7.0 【2025.01.18】 代理池可批量启用、禁用、删除等，显示当前代理IP及手工切换

v2.6.9 【2025.01.10】 Zoomeye接口API升级、资产分拣功能完善和优化、过滤打印机

v2.6.8 【2025.01.06】 部分web指纹优化完善、密码猜解线程优化、jwt字典自定义等

v2.6.7 【2024.12.25】 代理先验证后使用、前后台数据同步、Fofa不同权限查询

v2.6.6 【2024.12.22】 空间测绘功能增加查询语法聚合、url探测异常修复

v2.6.5 【2024.12.18】 增加代理池管理、中英文切换、多网卡选择等，修复增强多项功能

v2.6版 【2024.10.18】 增加程序自动更新、密码破解结果连接验证、内置poc增至2300+等

v2.5版 【2024.09.15】 重构端口扫描模块，效率提升2-3倍、Poc检测资源占用高等修复等

v2.4版 【2024.09.01】 防误报算法优化升级、新增webshell生成、密码破解漏报和闪退修复等

v2.3版 【2024.08.12】 升级框架、增加Log功能、资源占用优化、空间探测算法优化等

v2.2版 【2024.07.22】 增加1300+Poc、Key认证、Host碰撞、40xBypass检测、Jwt破解和加解密、IP归属查询等

v2.1版 【2024.07.01】 增加自定义被动指纹、程序中断恢复、自定义header信息、导出资产excel高危标红等

v2.0版 【2024.06.18】 增加编解码功能，支持36种编解码、加解密、哈希等，Nuclei自定义poc智能匹配

v1.9版 【2024.05.28】 增加指纹探测规则8327条，总计51873条，远程下载非核心配置文件，增加主动指纹探测

v1.8版 【2024.05.01】 密码破解功能完善及多线程优化、资产较多时的前端响应优化，项目漏洞详情展示

v1.7版 【2024.04.16】 增加资产分拣功能，Poc检测可直接调用Nuclei、Xray、Afrog，增加自定义poc功能

v1.6版 【2024.03.25】 增加项目管理流程，增强各功能模块联动，数据库可对所有功能和数据进行增删改查

v1.5版 【2024.03.01】 增加一键检测ApiKey可用性功能，AV识别数据库更新，支持自定义添加红队命令

v1.4版 【2024.02.18】 增加网络空间探测功能模块，内置9种常见空间探测API，增加目录枚举递归限制及过滤功能

v1.3版 【2024.01.22】 增加密码生成功能，内置三种生成模式，增加设备弱口令查询功能，内置1.1万条记录

v1.2版 【2024.01.10】 增加子域名枚举、接口查询功能，针对非web服务的指纹识别进行优化，增加导出excel功能

v1.1版 【2023.12.27】 新增加java命令编码，重构目录枚举实现方式，效率提高10倍，IP扫描和指纹识别同步进行

v1.0版 【2023.12.21】 实现局部/全局代理功能，支持HTTP(s)/SOCKS5，正式版发布

v0.9版 【2023.12.19】 实现各功能之间的任务联动及右键菜单联动

v0.8版 【2023.12.15】 增加版本更新检查、有效期校验、配置文件读写等

v0.7版 【2023.12.12】 辅助功能杀软查询、提权辅助完成

v0.6版 【2023.12.10】 反弹shell、CS上线、下载命令、红队命令完成

v0.5版 【2023.12.08】 目录枚举及Fuzz模式实现

v0.4版 【2023.11.29】 弱口令破解模块功能实现

v0.3版 【2023.11.18】 Poc检测及Poc指纹匹配功能实现

v0.2版 【2023.11.01】 Url扫描及web指纹精简功能实现

v0.1版 【2023.10.23】 Ip及端口扫描、服务识别功能实现

v0.0版 【2023.10.10】 TscanPlus架构选择及功能初步规划

## 软件使用

### 1、软件下载及更新

Github下载：[https://github.com/TideSec/TscanPlus/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1RpZGVTZWMvVHNjYW5QbHVzL3JlbGVhc2Vz)

知识星球：【剑影安全实验室】见下方二维码（**更多、更新版本**）

软件基于Wails开发，可支持Windows/Mac/Linux等系统，下载即可使用。

由于MacOs的一些安全设置，可能会出现个别问题，如报错、闪退等情况，详见最下方FAQ。

Windows运行时依赖 [Microsoft WebView2](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXIubWljcm9zb2Z0LmNvbS9lbi11cy9taWNyb3NvZnQtZWRnZS93ZWJ2aWV3Mi8)，默认情况下，Windows11和win2012会安装它，但有些旧机器(如Win2k8)不会，如机器没有webview2环境，程序会引导下载安装webview2。另外Windows程序使用了Upx压缩，杀毒软件可能会报病毒，请自查。

### 2、Welcome

软件运行后，需审慎阅读、充分理解 **《免责声明&使用许可》** 内容，并在Welcome页面勾选 **“我同意所有条款”** ，之后方可使用本软件。

[![TscanPlus 综合性网络安全检测工具](https://www.ddosi.org/wp-content/uploads/2025/04/image-20240327171101515.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0L2ltYWdlLTIwMjQwMzI3MTcxMTAxNTE1LndlYnA)

### **【Key认证功能】**

为了”无影(TscanPlus)”的Poc检测更全面、精准，能形成良性生态，新增key认证功能。

经过key认证后，可使用所有内置POC，未认证用户只能使用420个POC，其他功能均可正常使用。

[![TscanPlus 综合性网络安全检测工具](https://www.ddosi.org/wp-content/uploads/2025/04/image-20240721003109091.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0L2ltYWdlLTIwMjQwNzIxMDAzMTA5MDkxLndlYnA)

通过key认证后，可使用所有内置的1300个poc。

[![TscanPlus 综合性网络安全检测工具](https://www.ddosi.org/wp-content/uploads/2025/04/image-20240721012102311.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0L2ltYWdlLTIwMjQwNzIxMDEyMTAyMzExLndlYnA)

**获取Key的三条途径:**

（1）在Poc平台提交3个Poc后可获得3个Key，之后每多提交一个Poc可多获得一个Key。

（2）在交流群或Github Issue中提交一个有效Bug，Bug修复后可获得一个Key。

（3）加入星球可直接获得3个Key，每隔三个月可重置一次key，之后每提交一个Poc可多获得一个Key。

**关于Key认证问题**

（1）只有初次进行Key校验的时候才需要联网(连接到poc.tidesec.com)认证，认证成功后不再需要再联网校验。

（2）每个Key只能使用一个客户端，目前主要结合网卡等硬件序列号进行匹配，所以当硬件更换时可能导致认证失败。

（3）Key认证只是为了能让poc使用和搜集形成良性循环，”取之于众，用之于众”，建议大家手头有poc的可以提交poc。

**详细Key提交、获取和使用说明可看这里：[http://poc.tidesec.com/index/explain.html](https://blog.upx8.com/go/aHR0cDovL3BvYy50aWRlc2VjLmNvbS9pbmRleC9leHBsYWluLmh0bWw)**

#### 3、项目管理

项目管理功能是把各功能进行流程整合，用户可根据自己的使用场景设计项目功能，完美融合了”资产测绘”、”子域名枚举”、”IP端口扫描”、”密码破解”、”POC检测”、”URL扫描”、”目录探测”、”UrlFinder”等功能。项目执行结果会存储到相应项目数据库中，方便后续查询和使用。

**【任务配置】**

在添加目标资产并配置任务参数后，TscanPlus会在后台对相应目标执行相应操作，并显示在对应功能Tab栏中。

1、各任务为顺序执行，”资产测绘” => “子域名枚举” => “IP端口扫描” => “密码破解” => “POC检测” => “URL扫描” => “目录探测” => “UrlFinder”，默认情况下，上一步探测发现的资产会作为后一阶段的资产输入。

2、在使用资产测绘功能时，如果测绘发现的资产可能不属于你的目标范围时，开启“对资产测绘结果进行扫描和POC检测”时，空间测绘的资产可能超授权范围，请慎用。

3、开启URL探测功能后，会对域名+IP+URL+空间测绘等发现的所有web应用进行URL指纹探测。

4、不选择“POC匹配指纹”时，会对所有探测到的资产+所有POC进行测试。

5、开启“所有端口和服务”后，会对匹配到的所有端口和服务进行破解，不开启时只破解常见的8种服务。

6、在使用目录探测功能时，如选择”仅URL列表”时，仅会对URL列表中的URL进行目录探测。选择”所有结果URL”时，会对IP探测、域名任务等发现的所有URL进行目录探测，当URL较多时可能会较慢。

[![TscanPlus 综合性网络安全检测工具](https://www.ddosi.org/wp-content/uploads/2025/04/image-20240327161224753.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0L2ltYWdlLTIwMjQwMzI3MTYxMjI0NzUzLndlYnA)

**【项目管理】**

在项目管理中，还可直观的展示项目概览，如项目总数、URL资产、IP资产、漏洞总数、敏感信息等，并可对所有项目进行编辑、重新执行、停止、删除等操作。

[![TscanPlus 综合性网络安全检测工具](https://www.ddosi.org/wp-content/uploads/2025/04/image-20240617182736349.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0L2ltYWdlLTIwMjQwNjE3MTgyNzM2MzQ5LndlYnA)

**【结果展示】**

所有扫描结果将显示在对应功能Tab中。

[![TscanPlus 综合性网络安全检测工具](https://www.ddosi.org/wp-content/uploads/2025/04/image-20240327160956342.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0L2ltYWdlLTIwMjQwMzI3MTYwOTU2MzQyLndlYnA)

#### 4、端口扫描

对目标IP进行存活探测、端口开放探测、端口...