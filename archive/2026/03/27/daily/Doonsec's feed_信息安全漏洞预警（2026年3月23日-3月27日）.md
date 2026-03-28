---
title: 信息安全漏洞预警（2026年3月23日-3月27日）
url: https://mp.weixin.qq.com/s/jnk0D6FlxLlVohP2gQ9oDw
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:16:17.389978
---

# 信息安全漏洞预警（2026年3月23日-3月27日）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagfibQXkKRw4dnU6w27wz8HibsnmnaAHOsxdiaaSqibpHHLxRMicgicy1FNfaLdPINRqCfSjYdJG9fEedqLbeuyAQBs0WwROfibVhtw9pmE/0?wx_fmt=jpeg)

# 信息安全漏洞预警（2026年3月23日-3月27日）

松杨网络安全资料库

![]()

在小说阅读器中沉浸阅读

我司致力于持续观察与收集国内外最新的漏洞情报，重点关注CNVD、CNNVD等权威安全平台发布的漏洞公告，及时整理和收录相关漏洞信息，助力提升信息安全防护能力，保障客户系统的安全稳定运行。经过我们团队的分析和筛查，我们收录了以下安全漏洞信息。目前，相关官方机构已经发布了针对这些安全漏洞的补丁和修复方案。我们建议相关用户和组织及时关注并采取相应的安全措施，以确保信息系统的安全和稳定。收录的漏洞详细信息如下：

涉及漏洞数量：CVE漏洞：752个；CNVD漏洞：2个 ；其它漏洞：1个；

重点关注漏洞：

### 1.Litellm 2026.3.24 供应链投毒事件

| 漏洞名称 | Litellm 2026.3.24 供应链投毒事件 |
| --- | --- |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-24 |
| 影响版本 | LiteLLM 1.82.7，LiteLLM 1.82.8 |
| 漏洞说明 | 2026年3月24日，互联网上披露 Litellm项目遭受供应链攻击。在 Litellm 的1.82.7 和 1.82.8 版本中存在proxy\_server.py与litellm\_init.pth恶意文件。安装受影响版本的包后，将造成包括SSH Key、云凭证等各类敏感信息泄漏。官方已下线相关影响包，建议客户尽快排查。 |
| 修复方式 | 1、排查是否有对应受影响的包。2、云安全中心镜像应用漏洞检测 与 漏洞管理应用漏洞已支持针对该起供应链攻击受影响包检测。 |
| 相关链接 | https://github.com/BerriAI/litellm/issues/24512 |

2.OpenClaw数据伪造问题漏洞（CNVD-2026-14827）

| 漏洞名称 | OpenClaw数据伪造问题漏洞（CNVD-2026-14827） |
| --- | --- |
| 漏洞编号 | CNVD-2026-14827 |
| 影响等级 | 中危 |
| 漏洞披露时间 | 2026-03-25 |
| 影响版本 | OpenClaw OpenClaw <2026.2.21 |
| 漏洞说明 | OpenClaw是OpenClaw开源的一个智能人工助理。OpenClaw存在数据伪造问题漏洞，该漏洞源于解析X-Forwarded-For标头值不当，攻击者可利用该漏洞欺骗客户端IP地址并影响安全决策。 |
| 修复方式 | 目前厂商已经发布了升级补丁以修复这个安全问题，请到厂商的主页下载：https://github.com/openclaw/openclaw/security/advisories/GHSA-2rgf-hm63-5qph |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-14827 |

### 3.OpenClaw元数据欺骗漏洞

| 漏洞名称 | OpenClaw元数据欺骗漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-14836 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-25 |
| 影响版本 | OpenClaw OpenClaw <2026.2.26 |
| 漏洞说明 | OpenClaw是OpenClaw开源的一个智能人工助理。OpenClaw存在元数据伪造漏洞，该漏洞源于客户端提交的reconnect平台和设备族字段未被绑定到设备认证签名中。攻击者可利用该漏洞绕过基于平台的节点命令策略并访问受限命令。 |
| 修复方式 | 目前厂商已经发布了升级补丁以修复这个安全问题，请到厂商的主页下载：https://github.com/openclaw/openclaw/security/advisories/GHSA-r65x-2hqr-j5hf |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-14836 |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

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