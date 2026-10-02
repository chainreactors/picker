---
title: Google披露Citrix 0Day攻击，黑客植入Web Shell攻入企业内网
url: https://mp.weixin.qq.com/s/Su4MwA39jAdS93ia0iJo3Q
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:45.181805
---

# Google披露Citrix 0Day攻击，黑客植入Web Shell攻入企业内网

# Google披露Citrix 0Day攻击，黑客植入Web Shell攻入企业内网

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3rYK3TTJkwzEHe8jl7LzSViaw5jXXFg9aX4uyzYA8JqKOG8BzKZtWwODXyAjNoAoEwU1AfU5DRTOUwaAf1IkOpg49PwwN8tcS0/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3tREnC5K92OxS92DC7jZHmMiaZ1qSO7tVo005Tfk3CdxGdL2CDoibSHEYibBmZlq7CCPhNO7JC6ic5ricr6dnIbO38ibnDYzsapJvtI/640?wx_fmt=png&from=appmsg)

Part01

两个Citrix 0Day遭活跃利用

Google发布警告称，Citrix NetScaler近期遭到两个高危0Day漏洞的活跃利用。攻击者可借此绕过认证、获取root权限，并植入隐蔽Web Shell，进一步向受害企业内网渗透。

目前攻击已波及北美、欧洲地区的多个机构，覆盖政府、金融服务、科技、教育、法律及专业服务行业。Mandiant咨询团队与谷歌威胁情报小组（GTIG）表示，相关攻击活动最早可追溯至2026年9月初。

攻击者利用的漏洞共有两个。其一是CVE-2026-88772，存在于Citrix NetScaler ADC与NetScaler Gateway设备中，属于高危内存溢出漏洞；其二是CVE-2026-88771，由输入验证不当引发，可被未授权攻击者利用实现远程代码执行。

Citrix将两个漏洞的CVSS评分均定为9.5，且已确认存在活跃利用。其中，CVE-2026-88772影响开启了数据报传输层安全（DTLS）的设备，VPN虚拟服务器默认启用该配置。

利用成功后，攻击者可以绕过身份验证，使NetScaler数据包处理引擎（NSPPE）触发未处理异常并终止运行，随后获得底层FreeBSD系统的root权限。攻陷设备后，攻击者还会修改Web服务器配置文件httpd.conf，使原本并非PHP格式的文件也能被当作PHP脚本执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1MoyAusZceZ4LHcrSicT1ib7R6oAXicllhEFIPgUNEUk8sXcJaQtxDQ0dVbONvIZkOMV9e6pCLnVia0WmJtCUyhpiao808sZ7wONqc/640?wx_fmt=png&from=appmsg)

Part02

攻击链植入专属恶意工具

在已观测到的入侵活动中，攻击者将.deb安装包文件、.sig签名文件配置为可执行PHP脚本，还配置了图标别名规则：用户看似访问无害的.ico文件，实际请求会触发隐藏的Web Shell。

攻击过程中还出现了一款新发现的PHP Web Shell，名为WHIPSHOT。该恶意程序将Base64编码的C2数据隐藏在看似合法的HTTP头字段中，让恶意流量混入正常Web请求，规避检测。

WHIPSHOT可以转发攻击者指令与执行结果，同时返回伪造的HTTP 404 Not Found响应，很容易误导排查Web日志的管理员。

另一款被发现的工具名为SLAPSHOT，是一个Python隧道程序。该工具监听本地回环端口，将已攻陷NetScaler设备上的任意TCP流量代理转发至内网。攻击者可借此开展内网侦察、连接内部主机，窃取凭证后即可实现横向移动。在一起入侵事件中，攻击者就曾利用该代理手动开展内网侦察、窃取凭证。

为了长期保留root级访问权限，攻击者还会为/bin/sh设置setuid权限位。配置完成后，即使指令来自低权限的Web服务器进程，系统Shell也会以root高权限执行。在部分入侵案例中，攻击者还会重启设备或Apache服务，让恶意配置生效。

Part03

官方已推送修复版本

安全团队需尽快为受影响的NetScaler系统安装补丁。Citrix已公布修复版本，包括NetScaler 14.1-73.37及后续版本、NetScaler 13.1-64.23及后续版本，对应的FIPS合规修复版本也已同步推出。

入侵排查可以重点围绕三个方向展开。首先检查/etc/httpd.conf中是否存在可疑的AddHandler、AliasMatch、PHP指令；其次扫描VPN脚本目录，查找隐藏在.deb、.sig文件中的PHP代码；最后检查是否存在/tmp/.uxdport或/tmp/.uxdlock文件，这类文件是SLAPSHOT运行的典型痕迹。

如果设备出现/bin/sh被设置setuid权限、非预期NSPPE崩溃、DTLS握手失败、/vpn/media/或/vpn/scripts/路径收到异常请求等情况，需立即判定为高优先级入侵指标。

GreyNoise观测显示，早在Citrix公开披露这些漏洞前，互联网上就已出现利用尝试，9月24日还监测到来自IP地址149.104.78.141的攻击活动。这一发现再次凸显了联网边缘设备的长期风险：这类设备通常缺乏端点检测能力覆盖，却拥有敏感内网环境的直接访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX08gn58IN1bJUkEafEibdbnFRLHgyX2KEMNADappygTBZZhCIwlDS9F6Uia5LHxjCICR1T42Z53LvQNDicOeG1RdvJAAxZ2pFfBuY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2YuRhvlc0jIPicqDd7wlPvuyecuN9ibK6aKSDPR4WXiavgM5p3zS9X00E5cyytpz7Ikx7Hdr0GCXKLWN0OZorWYH7s8gFHq0aIx0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1uosI1IfoNPFib74o6JyUbLUP4iaXzhRxGuS86n9c1G7sNxlLZicFwvcWISvrN3ia96wWBGF77szS8KUS9r0K4MBiaMebBv8Oiba3nw/640?wx_fmt=png&from=appmsg)

备注：文中IP地址与域名均已做去活化处理（例如将.替换为[.]），防止意外解析或跳转。请仅在MISP、VirusTotal或内部SIEM等受控威胁情报平台中恢复原始地址。

参考来源：

Google Warns of Hackers Actively Exploiting Citrix 0-Day Vulnerabilities to Deploy Web Shells

https://cybersecuritynews.com/citrix-0-day-vulnerabilities-webshells/

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