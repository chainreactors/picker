---
title: PaperCut 双漏洞链式在野攻击爆发，欧美教育机构已遭入侵，47% 设备尚未打补丁
url: https://mp.weixin.qq.com/s/kvzFHISM36g-opZ0B-ZFdg
source: Doonsec's feed
date: 2026-09-07
fetch_date: 2026-09-08T06:40:43.211552
---

# PaperCut 双漏洞链式在野攻击爆发，欧美教育机构已遭入侵，47% 设备尚未打补丁

# PaperCut 双漏洞链式在野攻击爆发，欧美教育机构已遭入侵，47% 设备尚未打补丁

博士
博士

黑猫安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/DYqn7TU9icq23R1tHj3gCHqjPBlyTf2xy1qO60q12TLVtoH1VZicR1qggnesLbJJEWGYoRjB94RB6gUibibsx6y5vyydIcAMoXvVVmkj4LF0X2k/640?wx_fmt=png&from=appmsg)

#

> 打印管理软件 PaperCut 出现预认证远程代码执行攻击链，教育、医院、政企均为高危对象，大量旧版本暂无补丁，请立刻自查处置！

打印服务器往往是内网里容易被忽视的节点，但如今它已经成为黑客重点突破的入口。近期，**PaperCut NG/MF 两个高危漏洞 CVE‑2026‑81578（CVSS 8.8）、CVE‑2026‑82078（CVSS 9.4）被黑客链式组合利用**，已经出现针对美国、欧洲学校、教育机构的真实入侵事件，攻击者无需登录即可远程拿下服务器，窃取账号凭证，横向渗透内网。

美国 CISA 已于 8 月 31 日将这两个漏洞录入**KEV 已知被利用漏洞目录**，代表漏洞已经存在大规模现实攻击，联邦机构要求 9 月 14 日前完成修复整改。

## 🚨攻击链原理：无需登录即可接管服务器

本次攻击由两个漏洞串联形成完整预认证远程代码执行：

1. **CVE‑2026‑81578｜关键功能缺少身份认证（认证绕过）**

   PaperCut 鉴权逻辑存在缺陷：校验权限只校验页面，不校验后台实际执行动作。攻击者构造特殊请求，**无需登录就可以修改服务器配置**。
2. **CVE‑2026‑82078｜不安全 Java 反射加载漏洞**

   借助上面拿到的未授权配置修改能力，攻击者调用数据库工具加载恶意 Java 类，在服务器执行任意 Java 代码。

> 组合效果：**无账号密码，远程直接执行代码，拿到 Windows SYSTEM 最高权限**。

PaperCut 并非第一次出现严重安全事件，历史漏洞就曾被勒索团伙利用投递 LockBit 勒索病毒。本次安全事件中，Huntress 安全机构成功在干净环境复现完整攻击链；统计显示，被监测的 PaperCut 实例中，**47% 还在运行 23 及更早版本，该类旧版本目前暂无补丁**，风险极高。

## 🔥在野攻击实际行为（欧美教育机构受害样本）

根据 Arctic Wolf 威胁情报观测，真实入侵中攻击者完成如下动作：

1. 执行系统侦察命令：`whoami`、`ver`、`tasklist`等，收集主机信息；
2. 创建恶意高权限账号：`Administrator17`；
3. 通过`certutil`下载凭证窃取工具`lsa_collect.exe`、`save_hives.exe`；该工具提取注册表密钥，获取系统 BootKey，读取 SAM 数据库盗取账号密码；
4. 投放 Metasploit Meterpreter Java 载荷，建立远程控制会话；
5. 使用`findstr`检索 PaperCut 全部配置文件，抓取密码、密钥、LDAP、token 等敏感信息；
6. 将窃取数据保存到`/custom/pcp_*.txt`，远程下载带走。

> 攻击者入侵后会尝试删除日志掩盖痕迹，但 Derby 数据库日志`derby.log`往往会留下取证痕迹，例如特征字符串 `jdbc:derby:memory:pwn`，是高可信度失陷标记。

## 🔍失陷自查清单（运维必做）

> ⚠️打补丁不等于完成处置；如果服务器曾经暴露公网，打补丁后必须做入侵排查，补丁只能阻止后续攻击，不能清除已经入侵的痕迹。

### 日志检索

1. PaperCut `server.log`搜索特征字符串：`jdbc:derby:memory:pwn;create=true`、`ERROR DatabaseUtils - Database error looking up cardID: VALUES CAST`等；
2. 查看`/data/internal/derby.log`数据库日志。

### 文件排查

1. PaperCut 目录下查找 5 字符名称的异常 `.class`、`.cmd`、`.out` 文件；
2. 查找恶意工具：`lsa_collect.exe`、`save_hives.exe`。

### 进程监控

1. 监控父进程为 `pc‑app.exe` 衍生 `cmd.exe`、`powershell.exe`；
2. 关注命令行出现：`whoami`、`tasklist`、`ver`；
3. 审计账号事件，查找陌生账号 `Administrator17`。

### Web 访问日志

查找访问路径：`/custom/pcp_*.txt`、UA 为`python‑requests/*`的下载行为。

## 🛡️紧急处置方案

1. **立即切断暴露面**

> 最重要临时措施：禁止 PaperCut 管理接口直接暴露公网。旧版本（23 及更早）暂无补丁，务必通过 VPN、内网、堡垒机访问，禁止公网可达。

2. **升级安全补丁**

   PaperCut 先后发布紧急补丁，官方后续又发布二次更新，**即使打过第一版应急补丁也建议更新到最新 Release2 版本**。版本 24 报告遭受攻击时还没有补丁，需尽快跟进官方更新进度。
3. **全面核查入侵痕迹**

* 曾经对公网开放的服务器，升级补丁前先备份日志、配置，保留取证数据；
* 一旦确认失陷，不要直接恢复旧备份，建议重置设备，导入可信干净配置，修改全部账号密码。

4. **基线加固**

* PaperCut 服务只放内网，防火墙限制访问源 IP；
* 开启日志外送，防止攻击者本地删除日志销毁证据；
* 梳理存量资产，重点标记 23 及更早无补丁版本，优先隔离保护。

## 📝写在最后

PaperCut 广泛部署在学校、医院、企事业单位，打印服务器权限往往很高，一旦被攻破，就成为内网横向渗透的跳板。大量旧版本至今没有补丁，同时黑客已经有成熟的攻击工具链。

> 不要因为打印服务 “不起眼” 就忽略安全风险，请立刻梳理你的 PaperCut 资产清单。

> *本文安全信息来源于 Huntress、Arctic Wolf、CISA 公开威胁情报，仅做安全预警参考。*

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq2rFcDicicSujNE2Tndw5FmRJ9LU8gic3vfYS4oCayTkWCdjZPxFjpFUib9pHg6KeAJNE9K3gcbFRsZNRXblcqMb0xqlhiaAgjFhIrc/0?wx_fmt=png)

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