---
title: Splunk高危RCE漏洞可致服务器被完全控制
url: https://mp.weixin.qq.com/s/Z-eBavXSE5cxRXI3yowgAQ
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:08:32.075777
---

# Splunk高危RCE漏洞可致服务器被完全控制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2n8Hvw9vzoxvuzDdgXRrjmPiaCHlsZs2Ej0kREKSEDZ5GHdEDRoLTRUicXoabJ42hpFcg3QDZadKgWcTqgZR6UjqodO3klL8XvU/0?wx_fmt=jpeg)

# Splunk高危RCE漏洞可致服务器被完全控制

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1djr3vnEnT287mYf2a5arMT60zU0ricOklWU7wz35kuapWPZc7YvC7ZUrHxtofXLYdjeIPhEVzm2ciabiamr8VrIMibguMVQ1ydmU/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****漏洞概述****

Splunk发布紧急安全公告，警告用户其Enterprise和Cloud平台存在一个高危漏洞（CVE-2026-20163），CVSS评分为8.0。该漏洞允许攻击者在目标系统上执行远程命令（RCE）。

**Part02**

## ****漏洞成因****

漏洞源于系统在索引上传文件前的预览阶段对用户输入处理不当。虽然攻击者需要具备高级权限才能利用此漏洞，但一旦成功利用，恶意用户将能控制底层主机服务器。

该漏洞被归类为CWE-77（命令中特殊元素的不当中和），存在于Splunk的REST API组件中，具体涉及/splunkd/\_\_upload/indexing/preview端点。攻击者必须拥有包含edit\_cmd高级权限的用户角色才能利用此漏洞。

**Part03**

## ****攻击原理****

满足条件后，攻击者可在文件上传预览过程中操纵unarchive\_cmd参数。由于系统未能正确清理该输入，攻击者可轻易注入并直接在服务器上执行任意Shell命令。

**Part04**

## ****受影响版本****

该漏洞由安全研究员Danylo Dmytriiev（DDV\_UA）与Splunk内部团队成员Gabriel Nitu和James Ervin共同发现并报告。受影响版本包括：

* Enterprise：10.0.0–10.0.3、9.4.0–9.4.8、9.3.0–9.3.9
* Cloud Platform：低于10.2.2510.5、10.1.2507.16、10.0.2503.12和9.3.2411.124的版本

Splunk Enterprise 10.2基础版本不受影响。Splunk正在主动监控并向受影响的Cloud Platform实例直接部署补丁。

**Part05**

## ****修复建议****

Splunk强烈建议立即通过更新或临时缓解措施解决此漏洞：

* 升级Splunk Enterprise：管理员应将安装更新至10.2.0、10.0.4、9.4.9、9.3.10或更高版本
* 实施临时措施：若无法立即升级，可从所有用户角色中完全移除edit\_cmd高级权限，通过拒绝执行恶意命令所需的权限来阻断攻击链

目前该漏洞尚无特定的威胁检测签名，因此主动打补丁和严格的权限管理至关重要。

**参考来源：**

Splunk RCE Vulnerability Allows Attackers to Execute Arbitrary Shell Commands

https://cybersecuritynews.com/splunk-rce-vulnerability-2/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1c65Y8TDXkbFibGXhdaEZzcUriaA8IqQF7iaTLhndBBN5vkfOyQdEibFsFOMJdZZ5pCfAhpPK4ibkibtPXkEygVQuokHrDAqoQ4Ecib0/640?wx_fmt=png&from=appmsg)

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