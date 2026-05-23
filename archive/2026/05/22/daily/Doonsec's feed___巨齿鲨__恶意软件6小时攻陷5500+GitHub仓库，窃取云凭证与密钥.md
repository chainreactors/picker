---
title: \"巨齿鲨\"恶意软件6小时攻陷5500+GitHub仓库，窃取云凭证与密钥
url: https://mp.weixin.qq.com/s/3-U6w4A4ycbp48BNFLmKyQ
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:34:07.443690
---

# \"巨齿鲨\"恶意软件6小时攻陷5500+GitHub仓库，窃取云凭证与密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX22iausjX0Fgz08Kq8UXqc89ic0wJfxJhDK88yeFIN4QLfuDHBxlr76R0j8XCic9ctBGPjVpvAaOoMjPkgYBXqdQWsd01iajeWxmak/0?wx_fmt=jpeg)

# "巨齿鲨"恶意软件6小时攻陷5500+GitHub仓库，窃取云凭证与密钥

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0yrwoaQmibiaOjdqNgDU2RSbAY8ZsqPWOanQ9uMXoliaibx0a9O2YeUibgZqibkZaZWLMve8lMIaRQHTfUnZPOAkSWap5cDoqII7III/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3NKWrUDmZ9meKVUqpMUjZ1ZRJF3icuJK0IDbJGksf69qicm8ZmibIemqXl4Ucic1uthGd4Og9P2PM0ztUNicxKXpRNcCtfdjPQ23fg/640?wx_fmt=png&from=appmsg)

2026年5月18日，代号"巨齿鲨"（Megalodon）的大规模自动化供应链攻击席卷GitHub平台，在不到六小时内向超过5,500个代码库注入了恶意CI/CD后门，创下GitHub Actions投毒攻击的最快扩散纪录。

Part01

攻击时间线与手法

安全公司SafeDep发现，2026年5月18日UTC时间约11:36至17:48期间，"巨齿鲨"行动通过随机八字符用户名的临时账户，向5561个GitHub代码库推送了5,718个恶意提交。攻击者伪造了build-bot、auto-ci、ci-bot、pipeline-bot等作者身份，使用build-system@noreply.dev和ci-bot@automated.dev邮箱伪装常规CI自动化维护。提交信息如"ci: add build optimization step"和"chore: optimize pipeline runtime"经过精心设计，可规避常规代码审查。

Part02

恶意负载变体分析

该攻击部署了两种共享同一C2服务器（216.126.225.129:8443）的GitHub Actions工作流变体：

* **SysDiag（大规模变体）：**

新增.github/workflows/ci.yml文件，触发条件设为每次push和pull\_request\_target，确保所有分支的提交都会自动执行

* **Optimize-Build（定向变体）：**

替换现有工作流为workflow\_dispatch触发，创建静默后门，攻击者可随时通过GitHub API激活且不产生可见的CI运行记录

两种变体均要求id-token: write和actions: read高权限，用于窃取 OIDC令牌，实施云身份冒充。Base64编码的bash脚本（共111行）被触发后会执行多阶段凭证窃取：

* 收集所有CI环境变量、/proc/\*/environ及PID 1环境数据

* 提取AWS凭证（访问密钥、秘密密钥、会话令牌）

* 通过gcloud auth print-access-token获取GCP访问令牌

* 从AWS IMDSv2、GCP元数据和Azure IMDS端点获取实时凭证

* 窃取SSH 私钥、Docker认证配置、.npmrc、.netrc、Kubernetes 配置、Vault令牌和Terraform凭证

* 使用30多个正则表达式扫描源代码中的API密钥、JWT、数据库连接字符串、PEM 密钥和云令牌

* 窃取GitHub Actions OIDC令牌实施直接云身份冒充

Part03

典型受害案例分析

开源在线聊天平台Tiledesk成为关键下游攻击目标。攻击者通过提交acac5a9入侵其GitHub代码库，将合法Docker构建工作流替换为Optimize-Build后门。维护者在不知情的情况下，将受污染的@tiledesk/tiledesk-server 2.18.6至2.18.12版本发布到npm registry，导致后门通过软件包传播（应用代码未改动，仅工作流文件被篡改）。

Part04

入侵指标(IoC)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX32Q1JbugoicygUJDT9PYhZ43QeWfB4LJHZtok85krpbmPTXWLXOxf46nwM5zxsqIuHI9IU1a56SdXiaIKPmSSzEnV7WWmhsicPMM/640?wx_fmt=png&from=appmsg)

注：IP地址和域名已做无害化处理（如[.]），仅在MISP、VirusTotal等威胁情报平台使用时需还原

Part05

应急缓解措施

若代码库在2026年5月18日收到来自build-system@noreply[.]dev或ci-bot@automated[.]dev的提交，应立即：

1. 回退恶意提交并审计所有.github/workflows/文件
2. 轮换GitHub Actions运行器可访问的所有密钥（令牌、API密钥、SSH密钥、云凭证）
3. 检查云日志中是否存在未知工作流运行的异常OIDC令牌请求
4. 在Actions标签页检查意外的workflow\_dispatch执行记录
5. 将GitHub Actions固定到特定提交SHA而非可变版本标签
6. 为外部贡献者的拉取请求设置工作流审批关卡

SafeDep的Malysis引擎在检测@tiledesk/tiledesk-server@2.18.12捆绑工作流文件中的base64编码负载时首次发现该攻击，凸显了自动化供应链扫描工具在捕获绕过传统代码审查的攻击时的价值。

参考来源：

Megalodon Malware Compromised 5,500+ GitHub Repos Within 6 Hours

https://cybersecuritynews.com/nine-year-old-linux-kernel-vulnerability/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0TPDSBGWyOrBX6roghTcfJ7S0Uk6LPc6NiazIJCibS6wTdC64AxlpIAv3YZ2LoZFsJy3UHwic3ohlaRGRMZkKBW03QD5AMj5yuicM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338385&idx=1&sn=a442efc5bf8726e3e4239bc246e2976b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2A30nW87bmYJO7PWcHicOLnjA5DRaqykn6a3r9Nvg2PUTX1XkGuXcekoXza0aIXeq8O4ZwnhjLdFba5NEv5NQetNb0KjM9Mnb8/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX36icYI2CXicl9uUy5fmKHIdxgDmJcibjNUK1s23sY1GnkeibMK4Dk6OcCtxdaTQL0pel4YNGX3RKhaeuS8mqdE6BibxkPKUDwQjBGE/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24jhTVobqv3Ooeu9m1BQAhaLDl8icW7ibmSG7VxdACficvxezGvuyRN5qlZ3UsB378ghMfkLUcAlsn7uFIBMRQkcVpD0ib3O31uvg/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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