---
title: 朝鲜APT37黑客组织利用新型恶意软件渗透物理隔离系统
url: https://mp.weixin.qq.com/s/rpFsW8F8dHEFVgQV246GXw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:40.395393
---

# 朝鲜APT37黑客组织利用新型恶意软件渗透物理隔离系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2WmVoEkmUGuViaVica1YrCh57KPu37XMicHYR09MChib94olO8iamtuA4GxVM4f3ctF30EUkAptrPLbgmHqUxkk2mAFSUAmCVTqCr8/0?wx_fmt=jpeg)

# 朝鲜APT37黑客组织利用新型恶意软件渗透物理隔离系统

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0YOJIyyib2iaWpT4P7bblkeqeibBheoFjNnA7icgyjT3cwP3iaibfRO6jcmkhbWjFiaWSIOKrJTBLw73WmYlBGrFpH3jica5SHgbFKIGI/640?wx_fmt=jpeg&from=appmsg)

##

## 与朝鲜有关联的APT37威胁组织近期发动了一场复杂的新型攻击活动，使用专门针对物理隔离系统（长期被视为全球最安全系统类型）定制开发的全套恶意软件工具。这项代号为"Ruby Jumper"的行动标志着该组织攻击能力的显著升级，揭示了国家支持的黑客如何巧妙突破企业用于保护核心数据的物理安全措施。

##

**Part01**

## ****攻击组织背景与工具演变****

APT37（又名ScarCruft、Ruby Sleet和Velvet Chollima）是朝鲜政府支持的老牌黑客组织，长期针对与朝鲜国家利益相关的政府机构、国防组织和特定个人。该组织过去主要使用Chinotto恶意软件家族实施间谍活动和数据窃取。而此次Ruby Jumper行动则引入了五个全新恶意软件组件：RESTLEAF、SNAKEDROPPER、THUMBSBD、VIRUSTASK和FOOTWINE，这些工具在多阶段攻击链中各司其职，最终在物理隔离设备上植入监控程序。

Zscaler威胁研究团队ThreatLabz于2025年12月发现该活动，揭露了攻击者如何构建能跨越网络边界的隐蔽感染链。攻击始于一个恶意的Windows快捷方式文件（LNK），受害者打开后会在后台静默释放并执行多阶段载荷。诱饵文件是一份从朝鲜媒体翻译成阿拉伯语的巴以冲突文档，表明攻击目标可能包括对朝鲜叙事感兴趣的阿拉伯语使用者——这与APT37已知的受害者特征相符。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1VibyA5gzcmwO0mugRm5I9exELIVqnrThXcP4dTKn4ia6zu5KoM6najaeouXPqZgdBahUZpEcNdGCbHMAbUIBgOicrkicHQfkVNcw/640?wx_fmt=jpeg&from=appmsg)

**Part02**

## ****多阶段攻击链解析****

完整攻击链从初始LNK文件开始，依次通过RESTLEAF（第一阶段下载器）、SNAKEDROPPER（第二阶段载荷投放）、THUMBSBD和VIRUSTASK（通过可移动介质桥接物理隔离主机），最终由BLUELIGHT和FOOTWINE实现全面监控。该攻击的突破性在于：当U盘等可移动介质在联网设备和物理隔离设备间交叉使用时，恶意软件就能侵入本应与外界隔绝的系统。攻击者还滥用Zoho WorkDrive、Microsoft OneDrive、Google Drive和pCloud等云服务作为命令控制（C2）基础设施，使恶意流量隐匿于正常业务通信中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2K7Ite5c1Ipicutc5YwtX8K1TNGyvpYyt93g3fiaVTkKFibjn9U4JYtHRibNP1WScyuSiamq9mIibkJePJ93MibohX5edVC14IicgFI2Q/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****THUMBSBD突破物理隔离的技术原理****

Ruby Jumper行动中最具技术突破性的组件是THUMBSBD后门，它能将普通可移动介质转变为联网系统与物理隔离系统间的隐蔽双向通信通道。当U盘连接已感染的联网设备时，THUMBSBD会将预置命令文件复制到驱动器的隐藏目录$RECYCLE.BIN（该目录在Windows资源管理器默认设置下不可见）。当该U盘接入运行THUMBSBD植入程序的物理隔离设备时，恶意软件会读取这些隐藏文件，用单字节XOR密钥解密后执行攻击者指令，包括文件窃取、系统侦察和任意命令执行等操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2B3lq2mJbyACBhYpzyssS0bmbuSZ6fuTz897Lmb0IPFL7cr1RUC592XicT8huyH0U5VfiabZgyltzLsEv4QJExbJ5sjeVO1d2c4/640?wx_fmt=jpeg&from=appmsg)

**Part04**

## ****协同攻击组件与防御建议****

VIRUSTASK与THUMBSBD协同工作，通过用恶意LNK快捷方式替换U盘上的合法文件实现感染扩散。当新设备用户点击看似正常的文件时，会无意中激活基于Ruby的执行环境。SNAKEDROPPER则将完整的Ruby 3.3.0运行时环境伪装成名为usbspeed.exe的USB速度测试工具，并创建每5分钟运行一次的rubyupdatecheck计划任务维持持久性。最终载荷FOOTWINE提供键盘记录、音视频捕获等监控功能，并通过自定义XOR密钥交换协议建立加密C2通道。

针对该攻击活动，安全团队（特别是管理物理隔离环境的机构）应采取以下防护措施：

* 严格限制可移动介质使用，对物理隔离系统实施硬件级管控
* 监控异常计划任务，审查所有新建的端点计划任务（如rubyupdatecheck）
* 审计云存储访问，重点关注Zoho WorkDrive、OneDrive等被滥用的云服务
* 检查LNK文件，警惕邮件附件和下载内容中的恶意快捷方式
* 排查入侵痕迹，检查%PROGRAMDATA%\usbspeed路径、HKCU\SOFTWARE\Microsoft\TnGtp注册表键及U盘隐藏目录
* 加强终端活动监控，按照ThreatLabz建议强化物理接入点防护

**参考来源：**

North Korean APT37 Hackers Leverages Novel Malware to Infect Air‑Gapped Systems

https://cybersecuritynews.com/north-korean-apt37-hackers-leverages-novel-malware/

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