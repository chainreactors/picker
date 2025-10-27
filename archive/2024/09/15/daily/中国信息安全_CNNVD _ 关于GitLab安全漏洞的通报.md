---
title: CNNVD | 关于GitLab安全漏洞的通报
url: https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664225572&idx=5&sn=909cc8ab173a1ba6cdcd7a5a2c7c083b&chksm=8b59d9ddbc2e50cb971db9698bc8d95f04ffe8dff64c932d435490adae32bcaff9a711a38fa9&scene=58&subscene=0#rd
source: 中国信息安全
date: 2024-09-15
fetch_date: 2025-10-06T18:26:37.547072
---

# CNNVD | 关于GitLab安全漏洞的通报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5yIkCa12Va3ibRJqK8x0jTAEUZhSibU8r6neV3YDiaMUwapjiaNsKBtwMQdLCTZrFGicsWvDGyQNyIia9fw/0?wx_fmt=jpeg)

# CNNVD | 关于GitLab安全漏洞的通报

中国信息安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5yIkCa12Va3ibRJqK8x0jTAEDjPtucdFIqEzNdC0rnIn0EE8Ox3cQCg2sLRCmibPJl6JkZPhBiakgxqg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5yIkCa12Va3ibRJqK8x0jTAEdGEhBZ2q3OHOLtBMKAhC47JLnYKzGeCsnDUlzQh8fzPZOkqH6I6FxQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5yIkCa12Va3ibRJqK8x0jTAEDjPtucdFIqEzNdC0rnIn0EE8Ox3cQCg2sLRCmibPJl6JkZPhBiakgxqg/640?wx_fmt=gif&from=appmsg)

**扫码订阅《中国信息安全》**

邮发代号 2-786

征订热线：010-82341063

**漏洞情况**

近日，国家信息安全漏洞库（CNNVD）收到关于GitLab安全漏洞（CNNVD-202409-1044、CVE-2024-6678）情况的报送。攻击者可以利用漏洞绕过身份验证，导致软件项目仓库数据泄露，进而攻陷服务器。GitLab多个版本均受此漏洞影响。目前，GitLab官方已发布新版本修复了该漏洞，建议用户及时确认GitLab版本，尽快采取修补措施。

## 一 **漏洞介绍**

GitLab是美国GitLab公司的一款软件项目仓库应用程序，具有版本控制、问题跟踪、代码审查、持续集成和持续交付等功能。GitLab存在一个身份验证绕过漏洞，攻击者可以通过某种方式利用其他用户身份触发pipeline，从而绕过身份验证，导致仓库数据泄露，进而攻陷服务器。

## 二 **危害影响**

GitLab CE/EE 8.14 至GitLab CE/EE17.1.7之前版本、GitLab CE/EE 17.2至GitLab CE/EE 17.2.5之前版本、GitLab CE/EE 17.3 至GitLab CE/EE 17.3.2之前版本均受该漏洞影响。

## 三 **修复建议**

目前，GitLab官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方升级链接：

https://about.gitlab.com/update

本通报由CNNVD技术支撑单位——中国信息安全测评中心华中测评中心（湖南省信息安全测评中心）、奇安信网神信息技术（北京）股份有限公司、锐捷网络股份有限公司、三六零数字安全科技集团有限公司、内蒙古旌云科技有限公司、南京国云电力有限公司、深信服科技股份有限公司、杭州安恒信息技术股份有限公司、内蒙古万邦信息安全技术有限公司、广州纬安科技有限公司、广东省信息安全测评中心、郑州云智信安安全技术有限公司、河北华测信息技术有限公司等技术支撑单位提供支持。

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。

联系方式：cnnvdvul@itsec.gov.cn

（来源：CNNVD）

**分享网络安全知识 强化网络安全意识**

**欢迎关注《中国信息安全》杂志官方抖音号**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5yIkCa12Va3ibRJqK8x0jTAEswls19icZuKFmDYGE1mB50SMFb06dyCnl08jp1HjRkblSlDu2K0wBicg/640?wx_fmt=jpeg&from=appmsg)

**《中国信息安全》杂志倾力推荐**

**“企业成长计划”**

**点击下图 了解详情**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5yIkCa12Va3ibRJqK8x0jTAEaZ9sQLwHwPMuBJjcXicaPWxopUmWiaBdW71wjeCJ6rLQxl0hAibrfibxuQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664162643&idx=1&sn=fcc4f3a6047a0c2f4e4cc0181243ee18&chksm=8b5ee7aabc296ebc7c8c9b145f16e6a5cf8316143db3edce69f2a312214d50a00f65d775198d&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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