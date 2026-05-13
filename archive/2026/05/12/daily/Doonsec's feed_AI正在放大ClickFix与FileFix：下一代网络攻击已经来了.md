---
title: AI正在放大ClickFix与FileFix：下一代网络攻击已经来了
url: https://mp.weixin.qq.com/s/Cg5x3IvcrmcN4ueYO02O4A
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:43:22.546989
---

# AI正在放大ClickFix与FileFix：下一代网络攻击已经来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQlAUl2IYAuzM3lpn83VIX9zWdvfueLfGuIuDLdYJp0HPmeOcumSLdk2LuO8fctsjHk3OpyRMWccgw8DNCnfP0P4HUklMwVKbo/0?wx_fmt=jpeg)

# AI正在放大ClickFix与FileFix：下一代网络攻击已经来了

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

随着AI大模型与智能体技术的快速普及，ClickFix、FileFix 等“诱导式攻击”正在从小范围试探，逐步演变为未来最具威胁性的主流攻击方式之一。

这类攻击最大的特点，并不是依赖传统系统漏洞，而是绕过技术防线，直接“利用人”。

过去，网络攻击更多依赖漏洞利用、木马植入或权限突破；而如今，攻击者开始将重点转向“认知操控”。通过伪装成系统提示、安全告警、软件更新、验证码验证、文档修复等场景，诱导用户主动执行命令、打开文件、授予权限，甚至亲手完成恶意操作。

AI的出现，正在让这种攻击能力发生质变。

一方面，大模型能够快速生成高度拟真的诱饵文案，自动适配不同国家、行业、身份与使用场景，大幅降低黑产编写钓鱼内容的成本；另一方面，AI还能自动生成品牌页面、客服对话、登录界面甚至“官方通知”，使钓鱼伪装进入高度自动化阶段。

攻击者不再需要专业文案团队，仅依靠AI即可批量生成高可信度攻击内容，攻击效率呈指数级提升。

尤其是在智能体（Agent）时代，这种风险会进一步放大。

以 OpenClaw 为代表的智能体产品，通常具备文件读写、浏览器操作、命令执行、API调用等高权限能力。一旦攻击者通过恶意 Skill 插件、第三方工具链、被投毒的知识库或外部提示词，对智能体进行诱导，就可能让AI“主动”执行危险操作。

例如：

自动下载并运行恶意程序；

执行系统命令或脚本；

上传本地敏感文件；

泄露 API Key、账号密码、聊天记录；

访问企业内网资产；

被远程操控成为新的攻击跳板。

更危险的是，这类攻击很多时候并不会触发传统安全设备告警，因为从系统视角来看，真正执行操作的“合法用户”或“合法AI助手”。

未来的网络安全对抗，正在从“漏洞攻防”逐步转向“认知攻防”与“AI行为安全攻防”。

谁能够控制AI的决策链、工具链与执行链，谁就可能掌握下一代攻击入口。

PART.01

ClickFix介绍

## 1.什么是ClickFix攻击？

ClickFix是2024年开始流行的社会工程类网络攻击技术，属于复杂攻击链的初始访问向量。

● 核心特点：诱导用户主动在自身设备上执行恶意命令，无需攻击者直接投递恶意文件

● 命名由来：诱导页面通常设置「修复它」「立即纠正」「我是人类」等按钮，让用户误以为在处理技术问题

● 传播渠道：被入侵的合法网站、恶意广告、虚假验证码、仿冒Cloudflare/Google Meet/Zoom/DocuSign/Okta等平台的页面、社交媒体诱导视频、虚假技术支持论坛等

● 危害范围：可传播信息窃取程序、远程访问木马（RAT）、恶意加载器等，同时影响普通用户和企业

## 2.核心攻击原理

ClickFix 的核心是利用人的心理弱点和系统信任机制：

### 原理一：利用「验证疲劳」心理

用户长期接触各类网站验证、错误弹窗，习惯快速点击「我是人类」「修复问题」等按钮，不会仔细核查弹窗内容的合理性。攻击者通过仿冒用户熟悉的交互界面（如 Cloudflare 验证、Google CAPTCHA），大幅降低用户警惕性。

### 原理二：转嫁攻击操作，绕过传统防御

传统攻击通常由攻击者主动投递恶意文件、利用漏洞执行恶意代码，容易被安全设备检测。而 ClickFix不直接下载恶意程序，而是将混淆后的恶意命令通过 JavaScript 注入用户剪贴板，诱导用户自己将命令粘贴到系统自带的可信工具（如 PowerShell、运行框、浏览器控制台）中执行，让攻击行为看起来是用户的主动合法操作，大幅降低被检测的概率。

## 3.完整攻击流程

几乎所有ClickFix攻击都遵循以下标准化步骤：

流量引流 → 展示诱饵弹窗 → 注入恶意命令到剪贴板 → 诱导用户执行恶意命令 → 后续恶意载荷植入

### 步骤详解：

① 流量引流通过多种渠道将用户引导至恶意页面：

● 钓鱼邮件中的链接

● 恶意SEO操纵的搜索结果

● 恶意广告（Malvertising）

● 被入侵的合法网站（企业官网、高校官网等）

● TikTok/YouTube等平台的诱导视频（如「免费激活付费软件」教程）

② 展示诱饵弹窗用户访问恶意页面后，看到仿冒的技术类告警/验证弹窗，常见伪装包括：

● Cloudflare验证拦截提示

● Google CAPTCHA 验证要求

● Google Meet/Zoom 的麦克风/摄像头权限错误

● 浏览器更新失败提示

● 文档加载错误提示

③ 注入恶意命令到剪贴板用户点击弹窗中的「修复」「我是人类」等按钮后，页面内置的恶意 JavaScript自动将混淆后的恶意命令注入用户剪贴板，同时弹出详细的操作指引诱导用户执行。

④ 诱导用户执行恶意命令根据不同场景，诱导方式包括：

● 指引用户按Win+R打开运行框，按Ctrl+V粘贴并执行

● 指引用户按Win+X以管理员权限启动 PowerShell，再粘贴执行

● 指引用户打开浏览器控制台（F12 或Ctrl+Shift+I），粘贴恶意 JavaScript 执行

⑤ 后续恶意载荷植入用户执行命令后，脚本自动从 C2 服务器下载后续攻击组件，完成解压、恶意 DLL 侧加载、内存注入等操作，最终植入信息窃取程序、RAT 等恶意软件。

## 4.关键技术细节

### 4.1. 难以被检测的核心原因

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibQbELz6WaCL7wQ83EBspe9bUjzrVMUbwDSz3R0U1Df4pdus3MupPP5WTicicaYvDGPNLzpp1fBZb6tZyvbicjrhymiadibRRr4TXrwg/640?wx_fmt=png&from=appmsg)

### 4.2. 常配合传播的恶意软件类型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibTIvd3Vn3c1ub0TuuvibrNN4Mgu89ib3wWuKLMPfIcfpYWIlE5OfCj38qTCCmSW62PhwFn8UPAH66vHicQVgIudX6a66iahAeibr3bI/640?wx_fmt=png&from=appmsg)

### 4.3. 可检测的攻击痕迹

● RunMRU 注册表痕迹：

HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU会保存最近通过Win+R运行的命令，可检索其中是否存在混淆的 PowerShell/MSHTA 命令。

● 进程遥测痕迹

Windows 安全日志（事件 ID 4688）会记录explorer.exe生成powershell.exe的异常行为。

● 剪贴板滥用检测

高级 URL 过滤、DNS 安全设备可识别试图向剪贴板注入恶意命令的 JavaScript 代码。

PART.02

FileFix介绍

1.什么是FileFix攻击？

FileFix是2025年出现的新型社会工程学攻击手法，由安全研究员mr.d0x披露，被认为是ClickFix攻击的替代方案。它通过诱导用户主动执行操作，结合系统/浏览器的合法机制缺陷，绕过安全防护并静默执行恶意代码。

2.核心攻击原理

FileFix的攻击逻辑依赖三个关键点：

社会工程学诱骗：诱导用户主动完成高风险操作（保存文件、粘贴命令等），降低警惕性；

绕过MoTW机制：利用浏览器保存文件的漏洞，使生成的本地文件不带Windows「标记网络（Mark of the Web，MoTW）」安全标记，从而绕过打开文件时的安全警告；

利用合法系统程序：通过mshta.exe、PowerShell等系统内置的合法工具执行恶意脚本，规避安全软件检测。

3.攻击流程（两种主流路径）

路径一：恶意 PowerShell 命令诱导（初始版本）

钓鱼页面 → 诱骗用户复制"伪装成正常内容的恶意PowerShell命令"

             → 诱导用户将内容粘贴到Windows文件资源管理器地址栏

             → Windows自动调用PowerShell执行命令 → 恶意代码静默运行

路径二：HTA 文件诱导执行（新型攻击，含 2.0 变种）

诱饵页面（如"保存MFA验证码"）

    → 诱导用户按 Ctrl+S 保存页面

    → 指导用户将保存的文件重命名为 .HTA 后缀

    → 用户打开 .HTA 文件

    → Windows自动调用 mshta.exe 执行嵌入的恶意脚本（无安全警告）

FileFix 2.0变种进一步优化了针对 Chrome和 Edge浏览器网页保存机制的利用，更稳定地规避MoTW防护。

## 4.关键技术细节

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibRCvwaibFMBqysPymjNlqRrHOu5WLkZclvZAoGk6IMCjqqclCadP9xTOWicnrSWbdXffX1uYdO4f8JKFM5QmhxiadS1jvsa6zBFXU/640?wx_fmt=png&from=appmsg)

PART.03

ClickFix与FileFix的关系

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibT7RHicQHED2q3GGeEAhicfrS7LKpibNVZRIRynm6gTu3YicImiaoLt2WvZfXs3f8nBtw6fSp5aQd1NAReUPUUTKx5C24EGv5iadf7e8/640?wx_fmt=png&from=appmsg)

PART.04

为什么这类攻击越来越多？

原因其实很现实。

### 第一，漏洞越来越难打

高价值漏洞价格越来越高，利用成本也越来越大。

### 第二，用户永远是最薄弱的一环

相比研究0day：

“骗用户点一下”成本低太多。

### 第三，AI 正在放大社工攻击能力

现在攻击页面、钓鱼文案、伪装文件，甚至语音诈骗，都能通过AI批量生成。

基于AI会帮你从多个角度考虑生成社会工程攻击方法。

未来这类“高仿真社工攻击”只会越来越多。

很多攻击并不高级，但足够真实。

真正危险的，从来不是黑客技术本身，而是“你以为那只是一次正常操作”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibR9pziccwKmP0T0jaZZxDyTO1GqibInibGb6jl1muCiaJvcAyABues0GQ8hzfrib5T0gYdpX9HnGEebBC0RbpWPa6yl5xQZMcPzKf0A/640?wx_fmt=jpeg&from=appmsg)

知识点：

.HTA

.HTA（HTML Application）是微软推出的一种基于HTML、CSS、JavaScript 的 Windows 桌面应用程序格式，文件扩展名为“.hta”。与普通网页不同，HTA由系统组件mshta.exe 直接执行，不受浏览器沙箱限制，具备较高系统权限，可访问本地文件、注册表及系统命令。由于开发简单、执行灵活，HTA曾被用于轻量工具开发，但也常被攻击者用于投递恶意脚本和加载木马程序。

mshta.exe

mshta.exe（Microsoft HTML Application Host）是Windows系统内置的HTA文件解析与执行程序，默认路径包括 C:\Windows\System32\mshta.exe。它不仅能够执行本地 HTA 文件，还可直接加载远程脚本，因此长期被黑客用于“无文件攻击”。攻击者常借助 mshta.exe执行恶意PowerShell、加载内存木马或建立远程控制连接，例如配合Cobalt Strike、Remcos等恶意程序实施攻击。由于其属于系统合法组件，也常被用于绕过安全检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[2.75亿条数据被窃！全球最大教育平台Canvas遭遇黑色一周](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493117&idx=1&sn=54f73093b2c294302d4f2c7398d1d30c&scene=21#wechat_redirect)

2026-05-11

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTckjRZIIGHyia4EgyOicjJcwHIdYKNlY9ibWHy5ibj1Y51lhKXKl9DibJFCyknVrXUgvSt3e0x2bpvBnTv5r7tibl9AsgBxU48mibTVA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493117&idx=1&sn=54f73093b2c294302d4f2c7398d1d30c&scene=21#wechat_redirect)

[16起典型网络安全事件盘点：弱口令、漏洞未修复、网站被篡改成“重灾区”](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493110&idx=1&sn=64f850a071b6cb9e6b058d916e3ec4f3&scene=21#wechat_redirect)

2026-05-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSSfeJcHAxe7o8n536GiblJ9b72sJY3TjMh8WsMDT9DwQtnEMlFia9V8pNeWAzeWaWrBRyicCTYiczRzSHcPRB5C3oFibNHkMgzjuDk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493110&idx=1&sn=64f850a071b6cb9e6b058d916e3ec4f3&scene=21#wechat_redirect)

[聚势五月，职等你来｜非凡安全岗位热招！](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493100&idx=1&sn=62a52f10a576f0df9b27291e46fb3faf&scene=21#wechat_redirect)

2026-05-07

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibSSa8Na0P8hHxIrIiaKoZwbKPsibcEJYchibueFciaMZb11eOLictGViaGzyqlaVoBALnb9E2voKgtgoWXc0JNuoAt2UahPoM2kDhwkw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493100&idx=1&sn=62a52f10a576f0df9b27291e46fb3faf&scene=21#wechat_redirect)

[Harness 框架：AI Agent时代被忽视的“地基工程”](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493092&idx=1&sn=1f5c17dfb557cf196882cffe6a834f2e&scene=21#wechat_redirect)

2026-05-06

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSvGR77OAuWRpNZO54ScTJ1LXmyvCvib5IxJjnRgzDCgiaOoiaEhHVIUpFaHBGV9lKwqceQSsMa0rL8teMpkbaM1cHpaH7qxodUy0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493092&idx=1&sn=1f5c17dfb557cf196882cffe6a834f2e&scene=21#wechat_redirect)

[网络安全人士必知的OpenClaw提示词注入风险](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493042&idx=1&sn=5d6015548c6ffce69f2d2784a39fabe3&scene=21#wechat_redirect)

2026-04-24

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSogOibSicwWERwSeIGXibaBDnICQpCrrlPDVFtsz7PJJVuEJhKzCPKJa6PnDibINsouOsRiaGJ052QknNtzDdbFYtS02cmPo1ABicwY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493042&idx=1&sn=5d6015548c6ffce69f2d2784a39fabe3&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbi...