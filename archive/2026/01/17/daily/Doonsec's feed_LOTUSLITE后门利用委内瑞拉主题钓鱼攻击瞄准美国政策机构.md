---
title: LOTUSLITE后门利用委内瑞拉主题钓鱼攻击瞄准美国政策机构
url: https://mp.weixin.qq.com/s/ACQYwpOPgYwHQqHUMyzYDw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:52.922273
---

# LOTUSLITE后门利用委内瑞拉主题钓鱼攻击瞄准美国政策机构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atibVZtZUEZZlOoxF5AwaGrnh5QiadILHFYusV2o9qWYsibURcjtUobkcyQ/0?wx_fmt=jpeg)

# LOTUSLITE后门利用委内瑞拉主题钓鱼攻击瞄准美国政策机构

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atQ5WbUVnAs79dJwO0ZCu29Y0bibByZ45cIDJnKXANPfntN73icXaAR2JQ/640?wx_fmt=png&from=appmsg)

**Part01**

## ****攻击概括****

网络安全专家披露了一项针对美国政府及政策机构的新攻击活动细节，攻击者使用政治主题诱饵投放名为LOTUSLITE的后门程序。该定向恶意软件活动利用美委两国近期地缘政治动态作为诱饵，通过名为"US now deciding what's next for Venezuela.zip"的压缩包分发恶意DLL文件，并采用DLL侧加载技术激活。目前尚不清楚攻击是否成功入侵目标系统。

研究人员以中等置信度将该活动归因于黑客组织Earth Pret（又称HoneyMyte和Twill Typhoon），依据是其战术模式和基础设施特征。值得注意的是，该威胁组织长期依赖DLL侧加载技术投放后门程序，TONESHELL便是其常用工具之一。

"此次攻击延续了利用地缘政治诱饵实施定向鱼叉钓鱼的趋势，相比漏洞利用，攻击者更青睐DLL侧加载等可靠的执行技术。"Acronis研究员Ilia Dafchev和Subhajeet Singha在分析报告中指出。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atCzuN6yH2kI6lxTz7dbNCS7hONmwliakvUGPa95cmBw3baElnvJ1licvQ/640?wx_fmt=jpeg&from=appmsg)

**Part02**

## ****LOTUSLITE后门技术特征与功能解析****

攻击中使用的后门程序LOTUSLITE（"kugou.dll"）是一款定制化C++植入程序，通过Windows WinHTTP API与硬编码的命令控制（C2）服务器通信，支持信标活动、通过"cmd.exe"执行远程任务以及数据窃取。其完整命令列表包括：

* 0x0A：启动远程CMD shell
* 0x0B：终止远程shell
* 0x01：通过远程shell发送命令
* 0x06：重置信标状态
* 0x03：枚举文件夹内容
* 0x0D：创建空文件
* 0x0E：向文件追加数据
* 0x0F：获取信标状态

LOTUSLITE还能通过修改Windows注册表实现持久化，确保用户每次登录系统时自动运行。Acronis指出该后门"通过嵌入挑衅性信息模仿了Claimloader的行为特征"。Claimloader是Mustang Panda组织通过DLL侧加载技术投放的DLL文件，用于部署另一款工具PUBLOAD。IBM X-Force于2025年6月首次记录该恶意软件，其关联的攻击活动针对敏感地区社群。

**Part03**

## ****攻击关联与活动归因分析****

"此次攻击表明，当简单的成熟技术与精准投放和切合时局的地缘政治诱饵相结合，仍能产生显著效果。"这家新加坡网络安全公司总结道，"尽管LOTUSLITE后门缺乏高级规避功能，但其采用的DLL侧加载技术、可靠执行流程和基础命令控制功能，反映出攻击者更注重操作可靠性而非技术复杂性。"

此次披露恰逢《纽约时报》报道美国对委内瑞拉首都加拉加斯实施网络攻击的细节。报道称在2026年1月3日军事行动抓获委内瑞拉总统尼古拉斯·马杜罗前，该攻击导致首都大部分地区短暂停电。"切断加拉加斯电力供应并干扰雷达系统，使得美军直升机在执行抓捕任务时未被发现。目前马杜罗已被引渡至美国面临毒品指控。"报道指出，"攻击造成加拉加斯大部分区域停电数分钟，但马杜罗被捕军事基地附近部分社区断电长达36小时。"

**参考来源：**

LOTUSLITE Backdoor Targets U.S. Policy Entities Using Venezuela-Themed Spear Phishing

https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icIRaltrZVKxHyDE18c4IRVw3NnALmIwxqOb5mKhbDhBIRRU7MLD2zkbPgnNPvhyk5ibAhhLAavEIA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

内容含AI生成图片

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