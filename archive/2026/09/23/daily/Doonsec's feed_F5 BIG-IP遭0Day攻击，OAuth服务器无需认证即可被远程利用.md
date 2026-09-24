---
title: F5 BIG-IP遭0Day攻击，OAuth服务器无需认证即可被远程利用
url: https://mp.weixin.qq.com/s/zwBuzMttM7xYjpz5iCtwSQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:13.305452
---

# F5 BIG-IP遭0Day攻击，OAuth服务器无需认证即可被远程利用

# F5 BIG-IP遭0Day攻击，OAuth服务器无需认证即可被远程利用

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1Yr87vibr7gVaCfZ2o0qudOLQ4qY9u6oAxujolW86bZyNAuGPWR9UUPoNpMnaEozicjsFjSCL9clRNnhm9MwDqAiaxDv2baMJKl8/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2s3NJssic5iciapzGIIiaqVvyLZegKiacQRCo6sftxu5Zk7Y6SQ3gKcrz5OVyP9vZWIQMLlRjjAx5050qYVY1CTg7XmMJM6Owc8ZSM/640?wx_fmt=png&from=appmsg)

F5发布警告称，攻击者正在主动利用BIG-IP访问策略管理器（APM）中的一个严重0Day漏洞，无需认证就可以远程执行代码。

该漏洞编号为CVE-2026-94127，仅影响同时配置了APM访问策略和OAuth配置文件的虚拟服务器，尤其是APM作为OAuth授权服务器运行的场景。F5在确认攻击者已将该漏洞武器化后，于2026年9月22日发布了编号为K000162605的安全公告。

该漏洞属于堆缓冲区溢出，归类为CWE-122，F5内部跟踪ID为2524777。攻击者发送特制网络流量就可以破坏内存，在BIG-IP系统上执行任意代码。

该漏洞CVSS v3.1评分为9.8，CVSS v4.0评分为9.3，均属严重级别。该漏洞攻击复杂度低，可通过网络远程利用，无需权限或用户交互。一旦利用成功，可能对系统机密性、完整性、可用性造成严重破坏。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0uob6DaxoSZnmqpzgs3oJscyYzzNs9GUUlbLbM1s2nzgduiaIiawiciaocSQwlGXcPKuKWUtPicrthh0AVuDzhGKcFKKj6RJd9w1WM/640?wx_fmt=png&from=appmsg)

Part01

漏洞仅影响特定OAuth配置

需要重点说明的是，漏洞暴露风险取决于具体配置，并非安装APM组件就会受影响。如果部署中仅将APM用作OAuth客户端或资源服务器，未配置OAuth授权服务器配置文件，就不会受到该漏洞影响。但设备模式运行的系统仍存在风险。

F5表示，该漏洞位于处理应用流量的数据平面，不会暴露控制平面。因此，仅限制管理接口访问，无法阻断针对受影响虚拟服务器的利用行为。

目前已知受影响的版本包括BIG-IP APM 21.1.0、17.5.0至17.5.1版本，以及17.1.0至17.1.3版本。其他BIG-IP模块、BIG-IQ集中管理平台、BIG-IP Next、F5分布式云服务、NGINX系列产品、F5OS各版本、F5 AI Gateway经评估均不受影响。

F5提醒，已过技术支持周期的版本未纳入本次评估范围，管理员不能因为这些版本不在受影响列表中，就判定其不存在风险。

Part02

官方已发布工程热补丁

目前F5已针对各受影响分支发布工程热补丁，对应文件分别为Hotfix-BIGIP-21.1.0.2.0.30.22-ENG.iso、Hotfix-BIGIP-17.5.1.9.0.160.12-ENG.iso、Hotfix-BIGIP-17.1.3.5.0.41.14-ENG.iso。

企业应首先梳理所有BIG-IP APM虚拟服务器资产，识别存在风险的访问策略与OAuth配置文件组合。确认受影响资产后，需立即安装对应版本的热补丁。

如果因业务原因无法紧急安装补丁，客户可联系F5支持获取iRule规则，临时缓解针对受影响虚拟服务器的攻击。

Part03

CISA将漏洞纳入已知利用目录

防御方同时应排查网络中是否存在漏洞利用尝试或成功入侵的痕迹。F5建议重点关注三类时间相近的事件：反复出现的OAuth认证失败、可疑命令执行，以及后续发生的流量管理微内核（TMM）SIGABRT事件。

如果/var/log/apm日志中出现10条及以上无效令牌消息，尤其是来自同一IP地址的记录，分析人员需要进一步核查。分析人员可通过tmctl global\_oauth\_stat -s total\_requests,total\_userinfo\_requests,total\_failed命令查看失败计数，再将时间戳与/var/log/audit日志中的条目关联分析。

当TMM进入循环、SOD守护进程触发SIGABRT信号时，系统可能生成TMM核心转储文件。但单独出现核心转储文件或认证失败，都不能直接证明系统已被入侵，需要结合两类事件的出现频率和时间关联关系综合判断。

目前已有证据显示该漏洞在野利用，CISA已将CVE-2026-94127列入已知被利用漏洞目录，再次提醒相关用户需紧急处置。

该漏洞由F5内部发现，目前公开信息尚未确认攻击者身份、利用规模，以及攻击者得手后的具体目标。

安全团队应妥善留存日志，排查认证失败记录前后的可疑活动。在事件响应过程中，需优先处置暴露在公网的OAuth授权服务器配置。由于目前信息尚不明确，除了第一时间修复漏洞消除暴露面外，回溯排查历史威胁也同样重要。

参考来源：

Hackers Exploiting F5 BIG-IP OAuth Server 0-day Flaw to Gain Remote Code Execution

https://cybersecuritynews.com/f5-big-ip-oauth-server-0-day-flaw/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0XsTyO4SuMuGUvEh6HBoZLXPa9xnn1UsveAZRjUSfAKwT77dFfrwAPbRgSe6l66sYOBiaFSfWMn3DL4IfDrDmexoxCYLftaleo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651346509&idx=1&sn=71e02ef8b6a2ed67fdc94aa19b152171&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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