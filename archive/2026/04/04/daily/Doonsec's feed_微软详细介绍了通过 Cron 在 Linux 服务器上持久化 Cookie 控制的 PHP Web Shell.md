---
title: 微软详细介绍了通过 Cron 在 Linux 服务器上持久化 Cookie 控制的 PHP Web Shell
url: https://mp.weixin.qq.com/s/UO2FfvqlCw_UbkrIk9zQIQ
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:34:43.512741
---

# 微软详细介绍了通过 Cron 在 Linux 服务器上持久化 Cookie 控制的 PHP Web Shell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7O6m2kxKibic3Qwxib8tFXiaB8IiayKG2ErJJoicQkZzcEXgJy1EicUoWnERV4X0IjW7MhgvYrtroZgSkiaK6ysz6omRuV46cxPDk1LfEs/0?wx_fmt=jpeg)

# 微软详细介绍了通过 Cron 在 Linux 服务器上持久化 Cookie 控制的 PHP Web Shell

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

微软 Defender 安全研究团队的调查结果显示，威胁行为者越来越多地使用 HTTP cookie 作为 Linux 服务器上基于 PHP 的 web shell 的控制通道，以实现远程代码执行。

“这些 Web Shell 不是通过 URL 参数或请求正文暴露命令执行，而是依靠威胁行为者提供的 cookie 值来控制执行、传递指令并激活恶意功能，”这家科技巨头表示。

这种方法更具隐蔽性，因为它允许恶意代码在应用程序正常执行期间保持休眠状态，仅在存在特定 cookie 值时才激活 Web shell 逻辑。微软指出，这种行为也适用于 Web 请求、计划任务和受信任的后台工作程序。

这种恶意活动利用了 Cookie 值可通过全局变量 `$\_COOKIE`在运行时获取这一特性，使得攻击者无需额外解析即可使用其提供的输入。此外，由于 Cookie 会融入正常的网络流量中，降低其可见性，因此这种技术不太可能引起任何警报。

cookie 控制的执行模型有不同的实现方式——

* 一个 PHP 加载器，在解析结构化 cookie 输入以执行编码的辅助有效负载之前，使用多层混淆和运行时检查。
* 一个 PHP 脚本，它将结构化的 cookie 数据分割成多个部分，以重建文件处理和解码功能等操作组件，并有条件地将辅助有效负载写入磁盘并执行它。
* 一个 PHP 脚本，使用单个 cookie 值作为标记来触发威胁行为者控制的操作，包括执行提供的输入和文件上传。

至少在一个案例中，威胁行为者被发现通过有效的凭据或利用已知的安全漏洞获得了对受害者托管的 Linux 环境的初始访问权限，从而设置了一个 cron 作业，该作业会定期调用 shell 例程来执行混淆的 PHP 加载器。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Nvp26dsstadcjNySAlApLOxum9rMib9W3SjXDkYBqY6dfZsqSn5PXShDr4JvGTRkFhxP3NXxGTIqGTX968wPZesyicXSQCe9Shg/640?wx_fmt=jpeg)

这种“自愈”架构允许计划任务反复重新创建 PHP 加载器，即使它在清理和修复工作中被移除，从而创建一个可靠且持久的远程代码执行通道。PHP 加载器部署后，在正常流量期间保持非活动状态，并在收到带有特定 cookie 值的 HTTP 请求时立即激活。

微软补充道：“通过将执行控制权转移到 cookie 中，Web Shell 可以隐藏在正常流量中，仅在用户主动交互时才会激活。通过将基于 cron 的重新创建实现持久化，与通过 cookie 门控激活实现的执行控制分离，攻击者降低了操作噪音，并限制了在常规应用程序日志中可观察到的指标。”

上述所有实现方式的共同之处在于，它们都使用混淆技术来隐藏敏感功能，并使用基于 cookie 的门控技术来启动恶意操作，同时尽可能减少交互痕迹。

为了应对这一威胁，微软建议对主机控制面板、SSH 访问和管理界面强制执行多因素身份验证；监控异常登录活动；限制 shell 解释器的执行；审核 Web 服务器上的 cron 作业和计划任务；检查 Web 目录中是否存在可疑的文件创建；并限制主机控制面板的 shell 功能。

微软表示：“持续使用cookie作为控制机制表明攻击者重复使用了已有的Web Shell攻击技术。通过将控制逻辑转移到cookie中，攻击者能够实现持续的入侵后访问权限，从而绕过许多传统的检查和日志记录控制措施。”

“攻击者并没有依赖复杂的漏洞利用链，而是利用环境中已有的合法执行路径，包括 Web 服务器进程、控制面板组件和 cron 基础设施，来部署和保存恶意代码。”

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