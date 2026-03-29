---
title: 2026 红队终极渗透指南：漏洞利用 + 权限维持 + EDR 绕过，全程干货 | 打点 | 撕口子 | 渗透测试 | Web安全
url: https://mp.weixin.qq.com/s/fIijPpB5VIKTytqdVO8mCQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:39:06.308008
---

# 2026 红队终极渗透指南：漏洞利用 + 权限维持 + EDR 绕过，全程干货 | 打点 | 撕口子 | 渗透测试 | Web安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BV6cRFk2iaVv2qGGHIxF88k2twiaLNcb4Cr8YbLfSriboOnkFQnmQjDcGR6eibWvbxwSRcKnDPX3ribyjQtVtclSqfjwCuUvfhXAicmVGv4RhvVJQ/0?wx_fmt=jpeg)

# 2026 红队终极渗透指南：漏洞利用 + 权限维持 + EDR 绕过，全程干货 | 打点 | 撕口子 | 渗透测试 | Web安全

原创

异空间安全
异空间安全

异空间安全

![]()

在小说阅读器中沉浸阅读

# 红队漏洞利用与权限获取 | FALSESPACE WIKI

> 语录：渗透不是硬刚，是找薄弱、撕口子、拿权限、进内网。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BV6cRFk2iaVtCAwamYicmVIdVRtT8WvuSibMSk0xJtBBbmylVGNH4ZL4E9zrdzkwHpu2lZCRa4YKtibfzkQUmOtVQZ9DArQbdbV7UYpWcmMQSy8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BV6cRFk2iaVsicrZvJgm1y3V9sV8kmXia7rLUISQIibeZcmd4jRpo6Von85CYPjNzFbFewlejuxLoclaniaeMf8xHEuPBYojsxpO1nZxFIKILZiao/640?wx_fmt=png&from=appmsg)

## 开篇：漏洞利用与权限获取——渗透的核心战斗

🔖 **核心认知**
很多小白以为渗透就是用工具乱扫漏洞、暴力破解，结果**立刻被拦截、被封禁、被告警**，完全摸不到门道。

**真正的红队打法：不硬刚、不蛮干、精准打击**。漏洞利用的本质，是找到目标最薄弱的环节，用最低成本、最隐蔽的方式撕开缺口，一步步拿到权限、进入内网。

## 01 核心总纲：渗透到底在干什么？

### 1.1 一句话通俗解释

红队实战 = 像黑客一样，**合法授权**攻破企业网络，拿到服务器/电脑控制权，进入内部网络。

### 1.2 核心四步流程

* ✅ **找薄弱点**：哪里没人管、哪里防守弱、哪里有漏洞，优先打击，绝不硬碰硬
* ✅ **撕口子**：利用漏洞、弱口令、配置错误，搭建入侵入口
* ✅ **拿权限**：控制服务器、管理员账号、内网关键节点
* ✅ **进内网**：外网打入内部，开展横向移动，扩大控制范围

## 02 核心突破：集权系统默认口令清单

🔖 **红队法则**
集权系统（管理中枢）是企业的“命门”。默认口令攻破即可一刀破防，直接拿下核心业务权限或内网凭证。

| 系统 / 组件 | 默认账号 / 密码 | 提权路径 / 严重后果 |
| --- | --- | --- |
| XXL-JOB | `admin / 123456` | 后台任务反弹Shell，获取应用服务器权限 |
| K8s 控制台 | `admin / P@88w0rd` | 接管Pod，容器逃逸控制集群宿主机 |
| Zabbix 监控 | `admin / zabbix` | 脚本执行直接反弹高权限Shell |
| Grafana | `admin / admin` | 泄露敏感看板、数据库拓扑与业务配置 |
| Nacos | `nacos / nacos` | 窃取AK/SK、数据库连接池核心凭证 |
| Tomcat | `admin / tomcat` | 部署恶意WAR包，写入WebShell接管服务 |
| Weblogic | `weblogic / weblogic` | 后台部署+反序列化RCE，拿下中间件权限 |
| ActiveMQ | `admin / admin` | 控制消息队列，监听核心业务流水数据 |
| 若依(RuoYi) | `admin / admin123` | SQL注入/模板注入实现远程代码执行 |

💡 **老兵打点技巧**

1. 用户名枚举：登录提示账号不存在，优先用工号/手机号字典跑有效账号
2. 指纹关联：看到`/druid/index.html`、`/swagger-ui.html`，立刻排查未授权访问
3. 账号复用：边缘系统拿到的账号，90%可直接登录VPN、主站SSO

## 03 总思路：红队最高级打法

### 2.1 核心策略：先软后硬、先边缘后核心

✅ 正确顺序：**没人管的系统 → 防守弱的系统 → 核心业务系统**

* 🧩 **边缘迂回（首选）**：废弃/测试/闲置资产，无防护，成功率最高
* ⚔️ **正面硬刚（高风险）**：直打VPN、邮箱、堡垒机，突破直接进内网
* 🕵️ **化黑为白**：利用泄露文档、源码、配置，盲打变开卷渗透

## 04 边缘资产攻击：90%打点都靠它

* 🗑️ **废弃资产**：下线旧项目、遗忘服务器、废弃网站，无人维护
* 🧪 **测试环境**：开发站、预发布环境，企业几乎无安全防护
* 🛡️ **弱防护资产**：无补丁、无安全设备、无监控，防守极度薄弱

## 05 核心高价值资产：突破=半只脚进内网

* 🔐 **VPN类（最快入口）**：深信服、华为、Cisco、Citrix，拿下直连内网
* 📧 **邮箱类**：Exchange、Coremail、Zimbra，账号全内网通用
* 📋 **OA办公系统**：泛微、致远、金蝶、用友，权限覆盖内部全业务

## 06 社工与网络钓鱼：人是最大漏洞

* 🎣 **鱼叉钓鱼**：伪造内部邮件、登录页、恶意文档，诱导泄露账号密码
* 📱 **钓鱼渠道**：企业微信、钉钉、电话、工单系统，精准触达员工

## 07 高阶攻击手段：极难检测的红队打法

* 🧬 **供应链投毒**：污染开源库、Docker镜像，企业下载即被入侵
* 🛠️ **工具投毒**：篡改Xshell、Phpstudy、TeamViewer，运行即被控

## 08 实战高频漏洞：小白最容易拿权限

* SQL注入：操控数据库，篡改窃取数据，提权服务器
* 文件上传：植入木马，直接接管网站/服务器
* 命令/代码执行：服务器本地运行指令，最高权限控制
* AK/SK云凭证泄露：通过代码/报错拿密钥，接管云主机、存储桶
* 内存马(MemShell)：Shiro/Fastjson注入，无文件落地，隐匿存活
* 配置中心未授权：Nacos/Consul一键抓取数据库、Redis生产凭证
* K8s集群攻击：未授权API、容器逃逸，接管整个集群
* 云权限越权：利用角色漏洞，普通账号升全局管理员

## 09 红队作战体系（实战版）

🔖 **护网核心**
红队本质是模拟真实APT入侵，核心目标：**打点成功、权限提升、内网漫游、全程隐匿**。

### 0x00 作战哲学

* 技术核心：不迷信工具，吃透漏洞原理，可自定义修改EXP
* 防御思维：看透防守逻辑，精准绕过WAF/EDR/态势感知
* 隐匿准则：最大化溯源难度，不被发现才是顶级红队

### 0x01 红队战略：护网计分打法

* 计分驱动：优先打高分靶标，利用下属单位/供应链降维打击
* APT闭环：侦察→打点→维持→横向→回传全流程，主打隐匿存活
* 专家信条：未知攻，焉知防，渗透就是深度体检防御体系

### 0x02 打点艺术：三维全景资产测绘

* 物理测绘：绕过CDN找真实IP，FOF/Hunter静默画像
* 信息泄露：挖掘GitHub、JS配置、内存凭证，无接触打点
* 人性弱点：鱼叉钓鱼、宏木马、LNK文件，突破员工终端

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BV6cRFk2iaVvFEWVQiacxwXKHRXmCqAicGxbia0WunUhklWYVdAlL36GOXtK01tGEWnbbAvSMTNDN47NB9v9UsQrEBaLqanlJj3OJRrW9LQloQ8/640?wx_fmt=png&from=appmsg)

###

### 0x03 极速打点：资产测绘三剑客

FOFA、Hunter、Quake联动 + EHole指纹 + BBScan敏感目录 + C段批量扫描 + 企查查深挖关联资产

### 0x04 HW必背：30条红队实战打点思路

1. 企查查+子域名爆破，测试环境多藏在二级域名
2. GitHub搜配置/密钥，云凭证是最高效打点入口
3. 关联历史CNVD漏洞，老旧系统必中Nday
4. 证书监控发现未备案VPN、新业务系统
5. 员工信息生成社工字典，精准命中弱口令
6. 接管失效子域名，利用云解析残留建站入侵
7. 劫持OAuth登录态，无校验直接盗号
8. API未授权/Actuator接口是外网重灾区
9. 匿名云存储桶，可拖库控页面拿高分
10. 开放SMTP端口，直接发送钓鱼邮件
11. VPN高危Nday一键突破内网
12. 内联注释/分块传输绕过WAF检测
13. Git/.svn泄露还原源码，挖掘硬编码密钥
14. Windows最新内核提权漏洞应急利用
15. Linux sudo配置滥用提权
16. Kerberos委派攻击，BloodHound直控域管
17. 云角色PassRole越权提权
18. MSSQL开启xp\_cmdshell弹Shell
19. 劫持计划任务实现稳定权限维持
20. DLL劫持开机自启，无文件落地
21. NTLM中继攻击，关闭SMB签名直接控机
22. 哈希传递PTH，不出密码横扫内网
23. 生成黄金票据，永久控制域控
24. WMI无文件远程执行，规避查杀
25. SCF文件劫持窃取NTLM凭证
26. 打印服务漏洞/Win32k内核提权
27. 隐藏系统计划任务，长效存活
28. 注册表克隆影子管理员账号
29. Office加载项后门，办公软件自启上线
30. 云函数持久化后门，长期隐匿不掉线

⚠️ **打点常见坑&解决方案**

* 发包封IP：代理池轮换+爬虫伪装+低速发包
* 有密码开MFA：撞未开二次验证的旧系统
* Shell不出网：DNS/HTTP隧道替代反向连接
* 木马被杀：放弃文件落地，注入内存马
* EXP崩服务：用轻量无回显POC，提前备份进程
* 识别蜜罐：看端口全开放、响应异常快、无真实业务
* CDN隐IP：查历史DNS、证书日志找真实地址
* 验证码拦截：找移动端旧API、AI打码绕过
* 扫C段卡网：改用被动扫描收集资产

🔖 **红队铁律**

1. 必须书面授权 2. 数据匿名化 3. 清理痕迹 4. 不留个人指纹

### 0x05 Web打点核心战术

0day定点突破 > Nday常规利用（Shiro/Fastjson）> 内存马注入 > Webpack源码还原 > Nacos未授权拿凭证 > 被动Burp扫描

![](https://mmbiz.qpic.cn/mmbiz_png/BV6cRFk2iaVuIzpaichZYuY6rr484d3fxGuibHQqyaevUpklFUwOEaX5u63mVd1OB9HicRVl0fLBvZonTnUb3JM3WzYrytyr40ZkGhhiaKTCvibak/640?wx_fmt=png&from=appmsg)

### 0x06 外网必杀技

无MFA账号喷洒、源码泄露审计、敏感接口扒数据、后台弱口令上传WebShell

### 0x07 内网纵深渗透

Java中间件全漏洞利用 + 域渗透全套（金票/银票/DCSync）+ 不出网隧道搭建

### 0x08 横向移动端口全解

135/445（WMI/SMB/PTH）、5985 WinRM、3389 RDP，熟记错误码快速排障

### 0x09 C2隐匿

修改默认端口、伪造SSL证书、定制流量Profile、云函数中转上线

### 0x0A 绕杀软&文件限制

certutil编码绕过、文件拆分上传、BOF内存无文件执行

### 0x0B 全链路Bypass

免杀提权、日志痕迹清理、CDN/域前置流量伪装

### 0x0C 现代EDR对抗

* Unhooking内存钩子、Direct Syscalls绕过API监控
* PPID伪装进程父节点，规避异常行为审计
* BYOVD脆弱驱动提权内核，致盲高端EDR

## 10 红队Trick｜小灰实战分享

👤 作者：小灰（rainismG）无声双螺旋团队渗透工程师

### 一、外网破冰思路

1. 天眼查梳理组织架构、分公司、合作方
2. SSRF/内网泄露IP判断网络拓扑
3. 锁定OA/邮箱/VPN/SSO等高价值入口

📌 **外网五大核心攻击入口**

1. 办公集权系统：OA、邮箱、VPN、SSO
2. 信息泄露系统：Git、云盘、内部文档
3. 低防护系统：无MFA、老旧基层资产
4. 多级业务系统：分公司、省市联动网络
5. 供应链资产：外包/服务商弱安全节点

### 经典4大实战案例

1. SSRF定位内网资产，后台潜伏盗号
2. OSINT社工+爆破，横向打通全邮箱
3. 邮箱0day拿下运维密码，直连内网
4. OA漏洞窃取账号，拿下全网拓扑

![](https://mmbiz.qpic.cn/mmbiz_png/BV6cRFk2iaVuJKfiagrQutSZJGCM9KZSHtMWJ8FyQYyYQQg7x3Jpq72Jb8p2ibFHeN1faqjIrslQA4vsgXvEgupxV5o7icKd4kuMsXhmCPekQicU/640?wx_fmt=png&from=appmsg)

###

### 二、内网横纵核心战术

* 进内网先潜伏，不暴力扫描
* 优先占领老旧低活跃度机器做据点
* 精通NTLM/Kerberos/票据传递/域权限维持全套技术

### 三、高阶信息收集

路由/ARP/DNS/SMB/SPN枚举 + 主机软件记录 + 浏览器凭证抓取 + AD域高阶查询

### 四、攻防绕避技巧

IP封禁用代理池、WAF绕协议污染、EDR逆向流量加密、精准识别蜜罐

## 11 红队实战思维导图

🌍 **外网打点**
资产测绘→信息泄露→薄弱点筛选→OA/VPN/中间件漏洞入口

🔐 **权限获取**
注入漏洞→弱口令撞库→钓鱼社工→拿到初始Shell

🌐 **内网漫游**
信息枚举→横向移动→域提权→权限潜伏隐匿

🛡️ **防御对抗**
IP封禁/CDN/EDR/溯源全场景绕过方案

## 12 红队常用工具命令

### 信息收集

```
route print
arp -a
SharpAdidnsdump.exe
dnscmd /Info
setspn -T 域 -q */*
wmic product get name,version
```

### 内网横向

```
wmic /node:ip process call create "cmd"
netsh advfirewall firewall add rule name=BYPASS dir=out action=block remoteip=IP
```

### 专家级工具

```
./cloudfox aws -p profile_name instances
./amicontained
java -jar JNDIExploit.jar -i [YourIP]
runas /trustlevel:0x20000 "cmd.exe"
```

## 13 红队完整实战流程（0到域控）

资产测绘 → 泄露挖掘 → 筛选薄弱点 → 外网打点 → 内网潜伏 → 信息枚举 → 横向移动 → 域内提权 → 权限维持 → 全域接管

⚠️ **老兵避坑**

1. 内网严禁全端口Nmap扫描，高噪声秒告警
2. 禁止直接落地mimikatz，优先内存加载无文件版本
3. 打点后立刻搭建加密C2隧道，防止快速溯源封禁

## 14 红队实战Tips

✅ 边缘资产最好打
✅ 办公系统是内网大门
✅ 人永远是最大漏洞
✅ 隐蔽比速度更重要

## 15 权限维持：长效存活方案

1. Web层：内存马无文件驻留，重启不落地
2. 系统层：WMI订阅/隐藏计划任务/DLL劫持自启
3. 云端层：隐藏云用户、函数计算后门持久化
4. 域控层：黄金票据/Skeleton Key永久掌控域环境

## 16 现代防御高阶对抗

### 1. EDR底层绕过

内存钩子摘除、AMSI/ETW静默禁用、汇编级直接系统调用

### 2. 无文件隐匿执行

反射DLL注入、幽灵进程、脆弱驱动内核提权

### 3. C2流量伪装

定制流量特征、CDN域前置、云函数中转隐匿回连IP

### 实战破局经典案例

* SSO信任链漏洞，绕过全站WAF抓取全员账号
* 无网环境内存马封装HTTP隧道，伪装图片流量潜行
* 供应链外包资产溯源，窃取核心内网接入凭证
* 公众号SSRF突破军工隔离内网
* 打印机UDP固件漏洞，打通全TCP封禁部委网络
* 废弃测试备份，穿越零信任防线接管生产环境

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BV6cRFk2iaVvIP3hibL6ykKkkBrEyTFrgYaCChprLpaCRqpicy9rSCSF8s422B6Tmz3teWhw67F3DmBXAIEuBbc08xO07FW1UvicPrUE588bGzU/640?wx_fmt=png&from=appmsg)

###

### 困局速查表

| 死局场景 | 破局方案 |
| --- | --- |
| IP频繁被封 | 云函数Serverless代理池，动态换IP |
| Shell被杀软查杀 | 全面转向内存无文件执行/BOF |
| 内网不出网 | 抓取运维历史凭证，本地横向渗透 |
| SQL注入被WAF拦截 | JSON/XML嵌套注入，绕过常规规则 |

💡 十年感悟：HW拼的不只是技术，更是思维；没路时跳出工具局限，从业务、人员、供应链找突破口

## 17 法律红线 ⚠️

1. 严格遵守《刑法》285/286条、网络安全相关法规，**无书面授权禁止任何渗透测试**
2. 仅可在授权范围内开展演练，严禁越界攻击、窃取泄露敏感数据
3. 测试全程匿名化数据，结束后彻底清理所有后门与日志，杜绝黑产滥用

---

✨ **出品：FALSESPACE WIKI | 10年攻防实战总结**
合规学习，坚守底线，技术共享，安全致远

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BV6cRFk2iaVvDva1M7MpGHdIVjUYPDI60nWfHaZicPG304...