---
title: 每日安全动态推送(26/3/16)
url: https://mp.weixin.qq.com/s/D6-wmfqiaG4bS2o0v6Hoyg
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:13:58.299455
---

# 每日安全动态推送(26/3/16)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/3/16)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器中沉浸阅读

•  Joe Sandbox 对 YuboAPP (4).exe 的自动化恶意软件分析报告
<https://www.joesandbox.com/analysis/1883901/0/html>

本文详细列举了恶意软件的多个可疑行为特征，例如非标准端口通信、剪贴板读取、系统调用异常以及PE文件异常结构等，这些技术细节对理解现代恶意软件行为具有重要参考价值。

•  OpenClaw AI代理安全风险事件
<https://sectoday.tencent.com/event/D9xV25wBnYhVxRrjie3Q>

开源AI代理平台OpenClaw因其强大的自主执行能力和广泛部署，成为多起安全事件的焦点。OpenClaw被发现存在大量漏洞，包括12个超危漏洞和21个高危漏洞，以及超过1184个恶意插件。攻击者可利用提示注入、插件中毒、权限滥用等手段，操控代理行为，窃取敏感数据，甚至删除系统文件。中国国家互联网应急中心（CNCERT）、工业和信息化部（MIIT）及多所高校已发出警告，要求立即卸载或限制使用。部分政府机构和银行已全面禁用该工具。安全专家建议采取隔离部署、权限最小化、强化安全配置等措施以降低风险。

•  Glassworm 利用不可见 Unicode 字符与区块链C2窃取凭证
<https://www.tomshardware.com/tech-industry/cyber-security/malicious-packages-using-invisible-unicode-found-in-151-github-repos-and-vs-code>

本文揭示了Glassworm攻击者利用Unicode不可见字符注入恶意代码的新技术，并通过区块链进行凭证窃取，这是当前GitHub和VS Code生态中极具隐蔽性和威胁性的安全事件，值得立即关注。

•  CrackArmour：AppArmour漏洞可实现本地提权与容器隔离绕过
<https://securitybrief.asia/story/crackarmour-flaws-in-apparmour-risk-linux-root-access>

本文揭示了 AppArmour 中名为 CrackArmour 的多个漏洞，攻击者可借此绕过权限限制，获得 Linux 系统的 root 权限，这对依赖 AppArmour 进行容器隔离和主机加固的企业构成重大安全风险。

•  LnkMeMaybe：深入分析 CVE-2026-25185 与 Windows 快捷方式(.lnk)内部结构
<https://trustedsec.com/blog/lnkmemaybe-a-review-of-cve-2026-25185>

本文深入剖析了Windows快捷方式（.lnk）的结构，并开发了一个跨平台C#库用于创建和修改.lnk文件，最终发现并报告了一个关键漏洞（CVE-2026-25185），为Windows安全研究提供了新的视角。

•  OpenSSH 中 GSSAPI 密钥交换补丁漏洞分析
<https://seclists.org/oss-sec/2026/q1/299>

本文揭示了OpenSSH GSSAPI密钥交换补丁中的一个关键安全缺陷，可能导致预认证阶段的未初始化指针解引用和堆损坏，攻击者可通过构造的SSH数据包触发该漏洞，无需身份验证。这是对当前广泛部署的SSH服务安全性的重大警示。

•  蓝牙打印机服务器漏洞利用：从 GATT 到 UART 通信
<https://insinuator.net/2026/03/hacking-a-bluetooth-printer-server-gatt-to-uart-adapter/>

本文深入分析了一款物联网打印机服务器设备中的蓝牙SoC，揭示了其通过蓝牙和网络接口存在的未认证远程代码执行漏洞，允许攻击者以root权限完全控制设备。其最大亮点在于首次披露了Barrot BR8051A01芯片的iBridge功能漏洞，为物联网设备的安全性评估提供了重要参考。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/mmbiz_jpg/HhcytTU2b7cSVYH9KTtUE0fCYZwQWNYR6MMyIJWwZJTdhWZeeLkJRHDY3uLnKMy0XGtAbEHD2roaHED9Ho1C9icicFEzepEaMK0OFuMw0WXfk/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

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