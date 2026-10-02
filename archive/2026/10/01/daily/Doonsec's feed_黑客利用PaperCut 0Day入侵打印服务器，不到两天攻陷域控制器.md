---
title: 黑客利用PaperCut 0Day入侵打印服务器，不到两天攻陷域控制器
url: https://mp.weixin.qq.com/s/UlDalkFzjZ5D9El8szU3fA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:50.880931
---

# 黑客利用PaperCut 0Day入侵打印服务器，不到两天攻陷域控制器

# 黑客利用PaperCut 0Day入侵打印服务器，不到两天攻陷域控制器

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3ghHepypdxgxPibUgjzXIp8NDp8xwRh1CISiap1FhDunjt2G0UpibpdtL6EciaYoQTfZJTTiaTSw9FAJsLK3GCVDjdNuxncHd2V4fM/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX19OxXy4libVEZomicaKy0Zic3PrvcPElsxcm6ibmyeYPhfgy5fYFVNbVib21tBEMR50TFfcl5zVNr5g7eW6vKHx6PbGTT3bnfzWfiaU/640?wx_fmt=jpeg)

攻击者利用两个PaperCut MF 0Day漏洞，以存在漏洞的打印服务器为初始访问入口，最终攻陷企业活动目录系统。这起入侵充分说明，常被企业忽视的边缘业务系统，也可能成为攻击者访问核心身份基础设施的通道。

eSentire在向Cyber Security News（CSN）共享的报告中提到，其安全分析师于2026年8月31日，在一家教育行业客户的环境中发现本次入侵。攻击者从拿下打印服务器到移动至域控制器，整个过程耗时不到两天。

本次事件也再次警示，将管理类应用直接暴露在公网存在极高风险。此前已有报告显示相关PaperCut漏洞正遭在野利用，防御方已收到预警，需要严格限制应用的公网访问权限，同时监控服务产生的异常活动。

Part01

攻击者攻陷公网暴露打印服务器

本次初始入侵利用的两个漏洞分别为（CVE-2026-81578）和（CVE-2026-82078）。攻击者可将两个漏洞串联使用，无需认证即可修改服务器配置，并在PaperCut服务器的安全上下文内执行恶意Java字节码。此前已有针对这批在野利用漏洞的相关报道，也印证了公网暴露的应用服务器需要紧急排查加固。

攻击者将目标对准面向公网开放的PaperCut MF服务器，该服务器运行24.0.2版本，build号为69746。攻击者通过工卡/身份查询字段投递Java代码，安装内存加载器和Webshell，再依托这个立足点，将隐藏在篡改版Microsoft Copilot二进制文件中的AdaptixC2植入物部署到服务器上。

第一阶段加载器兼容多个版本的Tomcat，会在内存中重组载荷分片、启动下一阶段攻击，同时删除自身落地文件。后续部署的Webshell可通过自定义HTTP头接收指令，执行系统命令、读取配置值，还会清除日志和内部应用数据库中的攻击痕迹。

![攻击链概述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1lWb67AnVP8JtQ02F25SlWjYTxM95gUgwcP4SS7zjjJg1fpL8xcicsXiaGjL5MmF0t6HGW7c3mBAvnf678LjoQibFib8wf3Frib35k/640?wx_fmt=jpeg)

攻击链概述

这类痕迹清理操作对攻击者十分重要。该Webshell会将自身插入服务器请求处理链的靠前位置，阻断其他攻击者利用同一漏洞的尝试。攻击者通过这种方式维持对服务器的独占控制权，同时增加安全人员溯源原始入侵路径的难度。

篡改后的二进制文件会与远端攻击者基础设施建立连接，随后静默潜伏约一天时间。之后攻击者才返回服务器开展人工操作，这也体现出攻击者在突破漏洞边界后，通常会利用开源C2框架扩大访问权限。

Part02

攻击者窃取高权限访问令牌

不到两天攻入域控制器

成功建立据点后，攻击者开始扫描主机、网络、域信任关系和管理员组信息。他们定位到一个使用域高权限服务账户运行的进程，复制该进程的访问令牌，再利用该账户的权限重新启动植入物。整个过程无需窃取管理员密码，就可以开始向域控制器横向移动。

利用窃取到的高权限，攻击者通过管理文件共享将载荷复制到域控制器上。他们临时修改Windows PlugPlay服务的配置项，以此启动恶意载荷。

待载荷成功运行后，攻击者会停止该服务，再将服务路径恢复为合法配置。这套操作流程既能实现代码执行，又能减少配置篡改留下的痕迹。

进入域控制器后，攻击者从内存和注册表中转储凭证。他们开启Windows受限管理员模式，利用获取到的NTLM哈希通过远程桌面协议登录服务器。

得手后，攻击者复制了活动目录数据库文件。该数据库存储着域内所有账户的密码哈希，一旦被窃取，攻击者就可以通过哈希传递攻击进一步横向移动，风险极高。

攻击者将数据库和配套的注册表数据打包压缩，准备外传。他们定制的植入物采用加密配置和混淆程序逻辑，增加安全人员的分析难度。由于篡改的二进制文件依赖合法的配套支持库，公开沙箱在缺失该库的环境下也无法正常运行样本，难以自动检测。

Part03

管理员需及时升级PaperCut版本

管理员应尽快将PaperCut MF或NG升级到最新版本，同时配置访问控制规则，仅允许受信任的IP地址访问应用服务器。安全人员需要监控PaperCut服务的子进程，留意服务器日志丢失或异常缩短的情况，同时警惕各类后渗透异常行为。此前关于PaperCut紧急安全更新的报道也强调，企业必须第一时间应用厂商发布的修复补丁。

安全团队应核对厂商公告中的失陷指标（IoC），排查研究人员发现的日志报错信息，调查服务配置的异常变更。研究人员同时建议企业收缩服务账户权限，持续做好终端监控。本次入侵事件发生后，eSentire已隔离受影响主机，协助客户完成了全部处置整改工作。

失陷指标（IoCs）：

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX15SoDZqfzcziaTJXsB6UQkhALpcwoJEb7gC7DCA8IG9SDXNoDflnlf3PKqgST0Ie2OvNCicHPYhZm2dib534zskQQ4y0icubqehsE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2ibFOLCuuNU6OXydSWteqE2jZ0Rj71Bb3Y5C5iaWPudIOTfahanHnmRuL62yGeRFH1mbkQvYAibdA2YuJZTMKHfrlP6qfAmemuII/640?wx_fmt=png&from=appmsg)

注：文中IP地址和域名均已做去活化处理（例如使用[.]替代点号），防止意外解析或点击跳转。仅可在MISP、VirusTotal或企业内部SIEM等受控威胁情报平台内，将地址恢复为正常格式。

参考来源：

Hackers Turned a PaperCut Print Server Into a Path to the Domain Controller

https://cybersecuritynews.com/hackers-turned-a-papercut-print-server/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

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