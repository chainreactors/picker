---
title: 黑客利用伪造DeepSeek TUI GitHub仓库传播恶意软件
url: https://mp.weixin.qq.com/s/jCu1hHqoAA7k8jvZwPsp3w
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:10.486872
---

# 黑客利用伪造DeepSeek TUI GitHub仓库传播恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3yLeZl8mniaZlQyhZloV6KjiaKl9fxBmm2PdnM1R5QH8LSIJYLEsZT5iatdDhian04c7gZ88jHkd3YlU2TOVbIYtpX8DfcUxwapmk/0?wx_fmt=jpeg)

# 黑客利用伪造DeepSeek TUI GitHub仓库传播恶意软件

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1e3jPAbmIFE7wKj71xiadT3tSGfuRujF7PyUQdweLS6ADrEiaPwIMGsyjXYJe6WQ0diaf4VbkJcwK5Vx5SljojWqhPPPg5bcg8W8/640?wx_fmt=png&from=appmsg)

##

AI供应商宣称的"最强防护"实际上只能降低大语言模型被恶意提示词攻击的概率，无法完全杜绝；攻击者开始利用AI工具生成虚假漏洞报告，对漏洞赏金平台造成冲击；此外，xAI开发者在GitHub泄露了特斯拉等平台的API密钥，暴露出AI公司在密钥管理方面的严重安全漏洞；Kibana也被曝出高危漏洞可导致远程代码执行。

##

**Part01**

## ****攻击手法分析****

黑客再次通过伪造GitHub上的热门开源工具瞄准开发者和AI爱好者。此次攻击目标是DeepSeek TUI——一款合法的基于终端的智能Agent，允许用户直接从命令行与DeepSeek大语言模型交互。随着DeepSeek v4的发布和开发者Hunter Bown在中文技术社区广泛分享的帖子引发热议，该项目迅速成为威胁行为者利用热门AI软件进行欺骗的高价值目标。

这种攻击模式在开发者社区已日益常见。网络犯罪分子在GitHub上创建高度仿真的虚假仓库，模仿真实项目的外观和布局。不知情的用户访问这些页面后，会被诱骗下载看似合法的工具。在此次攻击中，恶意软件隐藏在欺诈仓库"Releases"页面的7z压缩包内，伪装成标准软件下载。

**Part02**

## ****技术溯源与关联分析****

奇安信威胁情报中心的研究人员率先详细识别出此次攻击活动。他们指出，该恶意软件特征与2026年3月曝光的OpenClaw欺骗攻击几乎完全相同。早期攻击活动中使用的相同恶意域名也出现在此次攻击中，表明是同一威胁行为者在持续演变其攻击能力。

特别令人担忧的是，同一攻击基础设施关联了大量伪造的AI主题安装程序名称。除DeepSeek TUI外，研究人员还发现冒充Claude、Grok、WormGPT、KawaiiGPT、fraudGPT等工具的伪造文件。

**Part03**

## ****恶意软件技术细节****

基于样本中发现的共享PDB路径"ClawCode.pdb"，所有这些恶意可执行文件都与同一Rust编写的恶意软件家族相关联，表明威胁行为者正在协调轮换欺骗目标。

此次攻击活动中识别出的主要恶意软件文件名为DeepSeek-TUI\_x64.exe（MD5哈希：b96c0d609c1b7e74f8cb1442bf0b5418），编译时间戳为2026年4月29日。在执行任何恶意行为前，它会进行广泛的环境检查以确定是否在沙箱中运行。如果检测到虚拟机、已知分析工具或可疑系统特征，则显示"抱歉，您的系统不满足最低要求"并静默退出。

确认在真实用户机器上运行后，恶意软件会使用XOR加密的PowerShell脚本禁用Windows Defender关键防护功能：添加六个文件夹排除项、禁用基于云的报告、关闭行为监控，并开放三个入站防火墙端口（57001、57002和56001）。样本中使用的字符串解密密钥为"xnasff3wcedj"，恶意软件会访问Pastebin和snippet.host链接获取Azure托管的第二阶段有效载荷。

**Part04**

## ****多阶段持久化与反沙箱规避****

下载的第二阶段组件各自承担维持攻击者访问权限的特定角色：OneSync.exe和WinHealhCare.exe处理安装和计划任务设置，同时通过Telegram报告；onedrive\_sync.exe通过Windows Run注册表项确保持久性；而svc\_service.exe作为常驻核心，使用NT系统调用进行线程注入，并完全在内存中加载.NET程序集以避免检测。

该攻击活动采用的多重持久化机制使得系统一旦被入侵就难以清除。恶意软件可通过计划任务、注册表Run键、Winlogon钩子和启动快捷方式存活。第二阶段加载程序autodate.exe伪装成服务管理器，同时悄悄将有效载荷注入内存。使用的C2域名为mikolirentryifosttry.info和zkevopenanu.cfd。

**Part05**

## ****防御建议****

开发者和安全团队强烈建议在下载文件前验证GitHub仓库的真实性，特别是对突然引起公众关注的AI相关工具。在信任发布版本前，务必检查账户年龄、提交历史和真实贡献者数量。监控内存注入技术和异常PowerShell活动的终端检测工具也有助于早期标记此类威胁。

**Part06**

## ****入侵指标(IoCs)****

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0zmDXscrbN0eiax2moLXs3pyia08PD9uysJZ7qEFaUblkia237znvxwYfP9kqicVvVnvBtUwXGqVRCHt1ficeIzibdUMXOZZgWSlZG8/640?wx_fmt=png&from=appmsg)

注： IP地址和域名已进行无害化处理（例如用[.]代替.），以防止意外解析或超链接。仅在MISP、VirusTotal或SIEM等受控威胁情报平台中恢复原始格式。

**参考来源：**

Hackers Use Fake DeepSeek TUI GitHub Repositories to Deliver Malware

https://cybersecuritynews.com/hackers-use-fake-deepseek-tui-github-repositories/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

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