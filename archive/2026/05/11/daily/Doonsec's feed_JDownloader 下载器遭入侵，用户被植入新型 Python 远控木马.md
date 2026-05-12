---
title: JDownloader 下载器遭入侵，用户被植入新型 Python 远控木马
url: https://mp.weixin.qq.com/s/90q38E8GKrO2alavTNm_eA
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:12.515933
---

# JDownloader 下载器遭入侵，用户被植入新型 Python 远控木马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1kTnLLyFiaCTXE6TXA9lY9EbF4uD3Vn09nniceQgfTTePJrYM2icROvUnWVngnxXv38oh4cuTlHAW0KLs4qFFDTKj6kAjRNwjreg/0?wx_fmt=jpeg)

# JDownloader 下载器遭入侵，用户被植入新型 Python 远控木马

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2kFbwaO18icBK2u17GTDtPtPV3LAXFSAVICRqscmFFic5h7iaIxEe4kXcWp8Gu98gc9njpk2sWshlJicS3pWUYlZLb1fzTict3SpEM/640?wx_fmt=png&from=appmsg)

##

2026年5月初，全球数百万用户信赖的知名开源下载管理器 JDownloader 遭遇严重供应链攻击。攻击者暗中入侵了官方网站 jdownloader.org，将正版安装程序下载链接替换为携带全功能 Python 远程访问木马（RAT）的恶意文件。在为期两天的攻击窗口期内，任何下载了所谓"标准安装程序"的用户，都可能已在不知情的情况下将危险且具有持久性的后门程序植入其设备。

##

**Part01**

## ****攻击技术细节****

此次攻击并未篡改 JDownloader 实际软件或其应用内更新系统，而是专门针对网站下载链接实施入侵，具体包括 Windows 系统的"下载替代安装程序"选项和 Linux shell 安装程序链接。在2026年5月6日至7日期间点击这些链接的用户，接收到的文件看似正常，实则是包含分层恶意载荷的未签名封装程序。该欺骗手段极为逼真，致使许多用户绕过了 Windows SmartScreen 警告，误以为这些警报只是误报。

jdownloader.org 的研究人员和开发者在 Reddit 用户 PrinceOfNightSky 于2026年5月7日报告可疑行为后确认了入侵事件。该用户指出，下载的可执行文件被归为"Zipline LLC"和"The Water Team"等虚假发布者，而非合法开发商 AppWork GmbH。开发团队在UTC时间17:24将网站下线并展开全面调查。截至5月8日晚至9日，在清除所有恶意内容并加固服务器配置后，网站已恢复提供经过验证的安全下载链接。

**Part02**

## ****漏洞成因与影响范围****

社区研究员 Takia\_Gecko 对恶意安装程序样本进行了深入技术分析，揭示了令人不寒而栗的复杂程度。假冒安装程序是一个未签名的封装程序，捆绑了真实的 JDownloader 安装程序和一个经过 XOR 加密的恶意可执行文件。该隐藏可执行文件使用 XOR 密钥"ectb"解码后，会显示一个 Windows x64 加载程序，随后该加载程序使用密钥"fywo"解密更多资源，最终解包一个受 PyArmor 8 保护的 Python 3.14 有效载荷。

最终载荷是一个用 Python 编写的完整远程访问木马框架，具有以下特征：

* 使用 RSA-OAEP 和 AES-GCM 加密与命令控制服务器通信
* 支持通过 Telegraph、Rentry、Codeberg 和洋葱地址等平台进行死投解析
* 使用 RC4 加密（密钥为"Chahgh4a"）解码实时 C2 URL
* 以 pythonw.exe 为宿主进程
* 允许攻击者随意推送并执行任意 Python 代码

**Part03**

## ****受影响用户应对措施****

jdownloader.org 给出的最关键建议是：如果您下载并运行了受影响的安装程序，请对操作系统执行全新安装。虽然杀毒软件扫描可能检测到部分威胁，但无法保证清除恶意软件可能建立的所有持久化机制。多位用户使用 Malwarebytes 和 Windows Defender Offline 进行全盘扫描后未发现任何检测结果，这表明该恶意软件能够有效隐藏其在受感染系统中的存在。

若您仍保留下载文件但尚未运行：

* 切勿执行该文件
* 右键点击文件→属性→数字签名选项卡，验证数字签名
* 正版 JDownloader 安装程序应由 AppWork GmbH 签名，任何未知发布者或缺失签名都是严重危险信号
* 在确认系统清洁前，避免从受影响设备登录敏感账户
* 通过其他可信设备修改所有重要密码

**Part04**

## ****入侵指标(IoCs)****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2pqoAFmyWibClJGAQtQGJvBxYPXCuGWv6wpJZjQniazun6g8UO3Z9jznaibCVnffhYdlJA0WfVJicKcnxNeL9n3uWYmJ18JXQAHN4/640?wx_fmt=png&from=appmsg)

注：为防止意外解析或超链接，IP地址和域名已进行无害化处理（如使用[.]）。仅在MISP、VirusTotal或SIEM等受控威胁情报平台中恢复原始格式。

**参考来源：**

JDownloader Downloader Hacked to Infect Users With New Python RAT

https://cybersecuritynews.com/jdownloader-downloader-hacked/

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