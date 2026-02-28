---
title: Claude Code遭入侵，RCE漏洞可窃取组织API密钥
url: https://mp.weixin.qq.com/s/3LiyL2Zx_iOibk-q1kYgfA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:26.045544
---

# Claude Code遭入侵，RCE漏洞可窃取组织API密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX03ib7tocQre1RPejwYdwSNyOYia68eKibzLoJ1SeR3qf5s6gyYuvu8g92DM3SMXPJIuUvMmeOhtan69dZQ47QL3xqcWiaeXzGQgj0/0?wx_fmt=jpeg)

# Claude Code遭入侵，RCE漏洞可窃取组织API密钥

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1sc3AZuVynSS0IlTfRMGEWeILb9STTZPeCkv2sj5Zr2rtxhfcL8bcyu8ErWZEfMWyY08V0lEyicI3WiaZ9DIdJBJUTCkTn0iaaTg/640?wx_fmt=png&from=appmsg)

##

Anthropic 公司开发的 AI 命令行开发工具 Claude Code 存在严重漏洞。攻击者可通过利用项目配置文件实现远程代码执行（RCE）并窃取 Anthropic API 密钥。

Check Point Research（CPR）报告了这些问题，Anthropic 已在公开披露前完成所有漏洞修补。这些漏洞凸显了 AI 辅助开发工具带来的攻击面扩大问题——存储库控制的配置文件可能被武器化，用于入侵开发者设备和共享工作区。

Claude Code 允许开发者直接从终端委派任务。为促进团队协作，该工具通过存储在代码库中的 .claude/settings.json 文件支持项目级配置。由于克隆存储库时会继承此文件，任何具有提交权限的贡献者都可修改它。CPR 发现恶意配置可能触发开发者设备上的意外操作，使被动设置文件变成执行载体。

**Part01**

## ****漏洞1：****

## ****通过不受信任的项目钩子实现RCE****

Anthropic 的"Hooks"功能允许用户定义在 Claude Code 生命周期特定节点自动执行的命令（如编辑后格式化代码）。这些钩子定义在存储库控制的 .claude/settings.json 中。CPR 发现当克隆配置了恶意 SessionStart 钩子的不可信存储库时，Claude Code 会在初始化时立即执行命令。

![计算器应用未经提示或执行警告立即打开（来源：checkpoint research）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1bVZDiaHJG4dlR8petHyFvostHxjEMFobjMTyS5tBog1SbglPG75kJKtNicWv0k2m9IGE3F2WHljibesqibCP4un2icsP72P7LTJAY/640?wx_fmt=jpeg&from=appmsg)

虽然工具会显示通用信任对话框，但未明确警告钩子命令已在后台未经用户确认运行。这使得攻击者可执行任意 shell 命令，例如建立反向 shell。

**Part02**

## ****漏洞2：****

## ****利用 MCP 同意绕过实现 RCE（CVE-2025-59536）****

Claude Code 支持通过 .mcp.json 文件配置的模型上下文协议（MCP）与外部工具交互。在 CPR 初始报告后，Anthropic 为 MCP 初始化添加了警告对话框。但 CPR 发现可通过 .claude/settings.json 中的两个设置实现绕过：

> enableAllProjectMcpServers 和 enabledMcpjsonServers

利用这些设置自动批准 MCP 服务器后，CPR 在用户与信任对话框交互前就通过运行 claude 执行了恶意命令，再次实现 RCE。

**Part03**

## ****漏洞3：****

## ****API 密钥泄露（CVE-2026-21852）****

对 .claude/settings.json 的进一步调查显示，环境变量也可被定义。CPR 针对控制 Claude Code API 通信端点的 ANTHROPIC\_BASE\_URL 变量。通过将此 URL 指向恶意服务器，攻击者可拦截工具的初始 API 请求。

CPR 观察到即使用户尚未与信任对话框交互，Claude Code 就已通过授权标头以明文传输完整 Anthropic API 密钥。窃取 API 密钥后，攻击者可实施账单欺诈或访问共享 Claude 工作区。虽然手动上传后无法下载工作区文件，但 CPR 通过代码执行工具重新生成文件使其可下载，从而暴露敏感团队资源。

这些漏洞带来严重的供应链风险，恶意配置可能通过拉取请求、蜜罐存储库或受感染的内部账户注入。Anthropic 已通过以下措施解决问题：增强对不可信配置的警告对话框；确保无论自动批准设置如何，MCP 服务器都需用户批准才能执行；推迟所有网络操作（包括 API 密钥传输）直至获得明确用户同意。开发者应立即更新至 Claude Code 最新版本，并以审查可执行代码的同等严格程度对待项目配置文件。

**参考来源：**

Claude Code Hacked to Achieve Full RCE and Hijacked Organization API keys

https://cybersecuritynews.com/claude-code-hacked/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3tSDVhn4H8MfzIKxtt4We0D52fia93Y5a2TI7y0t4j0PpiclCRBqdQCZWYrwG4B4hpaT2593sVoic8GylJKxPrgP1gyC1304Y78I/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX16d9YFd8C2ZLm5AxSaONt9eF8xcnfW9nhy3jyhoyrY28GWAnNeXJ0ojss2bj9w5V2asdI31nwVv2SUldtdhLfWuCE2l8fCzT8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

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