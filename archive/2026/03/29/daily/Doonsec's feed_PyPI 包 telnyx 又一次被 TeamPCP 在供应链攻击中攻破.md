---
title: PyPI 包 telnyx 又一次被 TeamPCP 在供应链攻击中攻破
url: https://mp.weixin.qq.com/s/4WHSUvfxwUv16VqV60nVxg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:29.299762
---

# PyPI 包 telnyx 又一次被 TeamPCP 在供应链攻击中攻破

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8kCBUL24smsfeGt0GwBCIhKWaicicGMDX347gxia16rSu5UpT2NibeR1SlbO0zO4coPhZM8rXybIwuMyh7IYhklNFJq2IrnUia26m8M/0?wx_fmt=jpeg)

# PyPI 包 telnyx 又一次被 TeamPCP 在供应链攻击中攻破

原创

忍者
忍者

Khan安全团队

![]()

在小说阅读器中沉浸阅读

该恶意软件在导入 telnyx 后立即执行。它会丢弃一个有效的 WAV 音频文件，并在帧中运行一个嵌入的可执行文件。

1.概述

2026年3月27日，知名通信平台Telnyx的官方Python SDK在PyPI仓库遭到供应链污染。攻击者TeamPCP上传了两个恶意版本（4.87.1和4.87.2），旨在遭受感染环境的严重后果。此次攻击是TeamPCP近期针对Trivy、Checkmarx和LiteLLM等一系列工具发起的大规模链式攻击的后续。

2.攻击链分析

TeamPCP 的攻击逻辑表示高度的自动化和关联性：

劫持：利用先前在 Trivy（漏洞扫描工具）中入口的后门，从未锁定版本的 CI/CD 模拟中提取 PyPI/npm 发布令牌。

包污染：利用窃取的令牌篡改合法仓库。在Telnyx案例中，恶意代码被入口在telnyx/\_client.py中，这意味着只需执行import telnyx，调用任何调用函数，恶意负载就会被触发。

隐写术逃逸：攻击者使用了先进的WAV音频隐写技术。

3. 技术细节：WAV 音频隐写术

这是本次攻击中最具一致性的部分。攻击者并不是直接下载.exe或.py文件，而是从C2服务器请求hangup.wav或ringtone.wav文件。

伪装性：这些文件是完全符合规范的音频文件，能够绕过基于文件类型和MIME-Type的防火墙过滤。

解密逻辑：恶意代码读取WAV的音频帧数据，将其作为Base64解码，并利用前8个字节作为XOR密钥进行解密，从而释放最终的攻击警报。

跨平台行为：

Windows：释放msbuild.exe到启动文件夹实现持久冷却，并设置12小时重滴落时间。

Linux/macOS：在内存中执行Python脚本，收集系统信息并保存为tpcp.tar.gz，通过AES-256-CBC加密后回传。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8l5a427toWDUnpoBEfib0xcKUryOu5icIc5y4TDKuLOfibQJDjJLH2tjMJOlPsj4ib88GMLZHGnzPyJtkiaaubSJLlicEhdf8ZocjLU4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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