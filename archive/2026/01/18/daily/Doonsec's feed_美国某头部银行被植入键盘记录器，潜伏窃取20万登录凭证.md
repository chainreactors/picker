---
title: 美国某头部银行被植入键盘记录器，潜伏窃取20万登录凭证
url: https://mp.weixin.qq.com/s/iMfx-ljT4RlA9DIQqj1Nsw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:36:43.544545
---

# 美国某头部银行被植入键盘记录器，潜伏窃取20万登录凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38daAluefq6JJ5FMSbia6MVR0tBib13UVF4KHIRibxKjC1hdgibZDZcEhuMkB0bssJPSAcW2H67oibD2Xg/0?wx_fmt=jpeg)

# 美国某头部银行被植入键盘记录器，潜伏窃取20万登录凭证

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38daAluefq6JJ5FMSbia6MVRh6U3VNKo4qy11bhwA8YEuWd64RRcstMGIUchCVs10rTbiaIQ8hlNF6g/640?wx_fmt=png&from=appmsg)

网络安全公司 Sansec 的研究人员发现，某美国头部银行的员工福利商城系统被植入键盘记录器。该恶意软件在运行约18小时后被清除，期间持续窃取网站表单内输入的所有内容，包括登录凭证、支付卡号及个人敏感信息，逾20万名银行员工数据面临泄露风险。

**Part01**

## ****第三方平台成攻击跳板****

银行通常将重金投入核心金融系统防护，但此次事件揭示关键隐患：内部门户及第三方平台形成的"侧门漏洞"正成为攻击突破口。报告指出：员工福利商城常被排除在标准安全审计范围外，因而成为理想攻击目标。更严峻的是，员工行为放大了风险。

Sansec 警告：银行员工常在多系统复用工作账号，失窃密码可能为攻击者打开内部系统跳板。

**Part02**

## ****高级攻击手法规避常规检测****

本次攻击采用精密的两阶段加载器（two-stage loader）规避监测。

第一阶段 ：恶意脚本检测用户是否进入结算页面，若是则从 https://js-csp.com/getInjector/ 加载外部脚本；

第二阶段 ：加载的组件会窃取页面所有表单字段数据，并通过图片信标（image beacon）技术外传——该手法将数据窃取伪装成普通图片请求，可绕过多数安全防护机制。

![banner](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38daAluefq6JJ5FMSbia6MVRyibErMmtKwvqyZlvsUdeA57yvNRyEp8l0xUoqqriaianw4tLusOeWdsyQ/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****模式化攻击暴露行业系统性漏洞****

此非事件并非独立事件。 Sansec 发现该攻击与既往行动存在明确关联，包括去年针对 Green Bay Packers 的入侵。研究人员证实：过去12个月中，这已是 Sansec 发现的第五起getInjector系列攻击，相关恶意域名包括artrabol.com、js-stats.com及js-tag.com等。

尤为值得企业警醒的是，常规安全工具完全失效：VirusTotal平台检测显示，发现时97家安全厂商中仅有1家识别出该恶意链接。报告总结道："万亿美元级的安全预算也难保万无一失"，企业亟需部署电商环境专用检测工具。此外，该银行未配置安全联络文件，导致研究人员"难以联系责任方通报漏洞"，进一步暴露应急机制缺陷。

**参考来源：**

Keylogger Found Harvesting Credentials on Top US Bank’s Employee Store

https://securityonline.info/keylogger-found-harvesting-credentials-on-top-us-banks-employee-store/

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