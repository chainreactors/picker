---
title: node-ipc再遭投毒：npm供应链攻击第二波
url: https://mp.weixin.qq.com/s/KFYKO0mFl4uapqCo-G2LWg
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:46:47.277002
---

# node-ipc再遭投毒：npm供应链攻击第二波

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PZu7FPlo96HpGPeSOjbcfK3NICzCYWXEG177qHt5EeRqbaic9KiaM3HTichKIppSaY4F4esLRtiaKApeodr8H4BNqgohx2USW9p98/0?wx_fmt=jpeg)

# node-ipc再遭投毒：npm供应链攻击第二波

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6POcNFl23k1SSY97AuZmrzRD0rf1JaE5I9DzQf1JyFbjFAE8Or7uoQIFhfaxDTUEqvtBH6nTOOj0LwSfRbHKxtCl9A6oDTZxfI/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617500&idx=1&sn=73c0634d23ef9a5a7ca009cf0e3b1929&scene=21#wechat_redirect)

> **导语**：2026年5月14日，安全研究人员发现node-ipc的三个npm版本已被植入恶意代码，与2023年首发的那次类似，本次仍是账户劫持路径——攻击者获取了一个已注销邮箱域名后重置账户密码，直接发布了恶意版本。

---

![node-ipc供应链攻击示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OQLYDQmvibYZzxUb2icNf99nfESuPJSgK8u9SF3ic9mFoW0p8b2dGW9STLibibNWkiaZt5MyeicKYIhl65uu6nSBjUVNxqP9rcbxAdxU/640?wx_fmt=png "node-ipc供应链攻击示意图")

## 事件概述

5月14日，Socket Security、StepSecurity、Datadog安全实验室等多个团队几乎同时确认：node-ipc@9.1.6、9.2.3、12.0.1三个版本存在恶意载荷。该包每周下载量约82.2万次，受波及范围极广。

这次投毒手法与2023年首次遭袭高度相似，属于"睡莲叶"（Lily Pad）攻击模式——攻击者不是伪造新包名（如typosquatting），而是直接盯上活跃维护者的账号权限，通过劫持域名逆向接管。

## 攻击手法还原

1. **账户劫持**：攻击者发现并注册了一个曾属于维护者、现已注销的邮箱域名，利用密码重置功能重置了npm账户。
2. **版本发布**：以合法维护者身份，在npm仓库发布了上述三个含恶意代码的版本。
3. **载荷注入**：三个版本的node-ipc.cjs主文件中，合法的esbuild产物之后被追加了一段约80KB高度混淆的恶意代码。StepSecurity称三个版本携带"完全相同的凭证窃取载荷"。
4. **静默运行**：在非Windows环境下，恶意代码行为相对克制；但在Windows平台，会额外写入`/tmp/nt-<pid>/`目录并部署持久化机制。

## 恶意载荷分析

![攻击流程图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OQLYDQmvibYZzxUb2icNf99nfESuPJSgK8u9SF3ic9mFoW0p8b2dGW9STLibibNWkiaZt5MyeicKYIhl65uu6nSBjUVNxqP9rcbxAdxU/640?wx_fmt=png "攻击流程图")

恶意代码通过DNS TXT查询与C2服务器通信，核心行为包括：

| 窃取目标 | 内容说明 |
| --- | --- |
| 本地密钥 | SSH私钥、PGP密钥、GPG密钥 |
| 云凭证 | AWS、Azure、GCP密钥及配置 |
| 环境变量 | `.env` 文件、CI/CD Secrets |
| AI工具配置 | Claude API密钥、OpenAI Token等 |
| 开发工具 | Git凭据、npm/github token |

**C2通信域名**：`bt.node.js`（引导域`sh.azurestaticprovider.net`，解析至IP `37.16.75.69`）。

数据外泄方式为DNS隧道（DNS Tunneling），每类凭证以TXT记录分批回传，绕过防火墙与日志监控的难度极高。

## 排查与缓解

| 措施 | 操作步骤 |
| --- | --- |
| **版本排查** | 全局检索package-lock.json或yarn.lock中是否存在node-ipc@9.1.6、9.2.3、12.0.1 |
| **DNS日志检查** | 检索服务器DNS日志中是否有对`bt.node.js`的TXT查询记录 |
| **立即升级** | 升级至node-ipc@9.2.4、12.0.2或更高安全版本 |
| **凭据轮换** | 隔离并检查受影响构建环境，轮换所有已泄露凭证 |

**影响范围评估**：高置信度。node-ipc是广受欢迎的IPC通信库，多个知名开源项目依赖，全球范围内受波及系统数量预计以十万级计。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NQ6CxqNHoxJrcJDVfGzWuzbYtcpG9HEnzC4Zcz4uGxe0xmWAT0Es0kYMe15ic4u49CpaGUXcOZQeoDTibFIx8f1BqpibsE8fJkW0/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650616704&idx=1&sn=e204caf547841c48d23fcb348d7f8981&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OsBeXPWu4iar3ibY25Do5DQramwZKHh1bFzKdgUPTvdulBnPkkkpgTa8QibBo3giaiaGr50xX6UhoVkUrpicIWp5EKQZmMSZ75qId3A/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650616766&idx=1&sn=36bf5623528d55e0bd9e30dbdd98a2b0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N1IAwSVHkYa2VvYib0zgY0xfmib3CWyuD9OwVKbwQ9mBWQVdxuf0Bgk6GN8ibGvm9CgFK0l3WFQodF0vZ90f07ib5qpiaQqUaaVdCQ/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650616732&idx=1&sn=5a7da8f181cfc3e7022e20061ba0fc51&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NsIFjCJiaB2Rx8tnw7UMljctOW4EqzA3dPJU5MEUHofWvXvrpianERqvia4Ly8xhJZxpVc76CI31eSIIXkqC1Ke1ZTEY7vf4sVicU/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650615329&idx=1&sn=e30c6d05f738ec157b3209a9b6f37ff9&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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