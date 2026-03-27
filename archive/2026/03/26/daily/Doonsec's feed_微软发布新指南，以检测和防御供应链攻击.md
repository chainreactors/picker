---
title: 微软发布新指南，以检测和防御供应链攻击
url: https://mp.weixin.qq.com/s/3B-xLUVfnVz7NWr2tX3qxg
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:27.159131
---

# 微软发布新指南，以检测和防御供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PlfXPp4nYv8OYq3v4bbXxib5VB9GjoekXxxFD5m45cOgY5QElItGEn8zsM7JAl1lPww9GrF4umo5NWroFL12IvMadORXZf9OOY/0?wx_fmt=jpeg)

# 微软发布新指南，以检测和防御供应链攻击

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Aqua Security 的漏洞扫描器 Trivy 遭受了复杂的 CI/CD 供应链入侵。

被确认为 TeamPCP 的威胁行为者利用之前不完整的修复措施，将窃取凭证的恶意软件注入到官方版本中。

该事件（编号为 CVE-2026-33634）成功地将一款受信任的安全工具武器化，用于攻击依赖该工具来保持安全的组织。

此图可视化了攻击传播时间线和工作流程受损情况。TeamPCP 攻击活动利用 Git 的标准设计特性（特别是可变标签和自定义提交身份）实施了攻击。

攻击者强制向 `trivy-action` 存储库中的 77 个版本标签中的 76 个以及存储库中的所有 7 个标签 推送了恶意提交`setup-trivy` 。

因此，下游 CI/CD 工作流程执行了攻击者控制的代码，但并未更改可见的发布元数据。

与此同时，一个受感染的 Trivy 二进制文件被发布到官方 GitHub Releases 和容器注册表中。

为了保持隐蔽性，该恶意软件允许合法的 Trivy 扫描在窃取数据后成功完成，从而掩盖了入侵行为，使运营商无法察觉。

该活动已扩展到其他框架，包括 Checkmarx KICS 和 LiteLLM。

## **恶意软件特征及利用**

在 GitHub Actions 运行器中执行时，基于 Python 的有效载荷会进行进程发现，以定位携带密钥的运行器进程。

关键凭证采集功能包括：

* **云凭证**：目标包括 AWS 元数据终端节点、GCP 服务账户密钥和 Azure 环境变量。
* **Kubernetes Secrets**：枚举并提取已挂载的服务账户文件和集群密钥。
* **应用程序令牌**：对配置文件和开发者 webhook 中的 API 密钥执行递归文件系统搜索。
* **基础架构访问**：提取 WireGuard VPN 配置、SSH 身份验证日志和数据库连接字符串。

被盗数据使用 AES-256-CBC 和 RSA 方案进行加密，打包成存档，并泄露到抢注域名。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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