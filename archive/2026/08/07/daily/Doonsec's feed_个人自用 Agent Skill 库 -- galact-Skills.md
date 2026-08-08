---
title: 个人自用 Agent Skill 库 -- galact-Skills
url: https://mp.weixin.qq.com/s/b2UBPdsZUJRmg-eYCmSNnQ
source: Doonsec's feed
date: 2026-08-07
fetch_date: 2026-08-08T03:22:23.741012
---

# 个人自用 Agent Skill 库 -- galact-Skills

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQvreH5fE1FhCGxHFicTBNY6XRUn9G88RWGa4DqRPRJojYfOIIAZianvHStY9kZ6mun8dhtK5Cud2gRMhfoKVo7uqu7A9HEUlBLdg/0?wx_fmt=jpeg)

# 个人自用 Agent Skill 库 -- galact-Skills

galact-byte
galact-byte

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

一套自用的 Agent Skill（SKILL.md 标准，跨 Claude Code / Codex 等）集合。现阶段聚焦渗透测试漏洞挖掘；后续会按需要扩展写作、工作流、数据处理等其它自用领域。 授权与用途声明：skills/ 下的渗透 skill 仅用于你有明确授权的安全测试、CTF、 教学与研究。每个 skill 内建 scope 确认与“7 问研判”纪律，只在授权范围内取证。 请勿用于未授权目标。

* **单类漏洞猎杀（hunt-\*）**

  ：ssrf、xss、sqli、command-injection、path-traversal、 xxe、csrf、open-redirect、cache-poisoning、request-smuggling、deserialization、 prototype-pollution、auth-bypass、nodejs-permission-bypass。
* **研判总线**

  ：recognize-attack-surface —— 拿到目标先分诊、路由到对应 hunt skill， 并处理跨组件攻击链 / 业务逻辑 / 配置错误 / 信息泄露等横切类别。

**0x02 安装与使用**

使用命令：

把某个 skill 目录整个拷进你 agent 的 skill 扫描目录，重开/刷新会话即可被识别：

```
# Claude Code（个人）cp -r skills/hunt-ssrf ~/.claude/skills/# Codexcp -r skills/hunt-ssrf ~/.codex/skills/# Pi / .agentscp -r skills/hunt-ssrf ~/.agents/skills/
```

之后直接描述任务（如“测下这个 URL 抓取有没有 SSRF”）；支持该标准的 Agent 会根据 skill 的 description 发现并选择合适的 skill。必要时也可明确要求使用对应 skill。

网盘下载链接（一定要在虚拟机运行）：

```
链接：https://pan.quark.cn/s/7d66a1b01507获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQvRM7omc2ES2NSLMZ2Nbib7VftC67uHpXxKTZqyibjeicgibLRzg0Xiao8B2x6JB25gOIdKTSwHD3F28Ek94lQmlM9E8xkAHvRjrLHw/640?wx_fmt=jpeg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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