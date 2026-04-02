---
title: 【安全圈】思科开发环境遭黑客攻破，超 300 个核心代码库外泄
url: https://mp.weixin.qq.com/s/TUNt6L8wpino91y68I9Mdw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:23:25.857800
---

# 【安全圈】思科开发环境遭黑客攻破，超 300 个核心代码库外泄

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGKCXiaoLSugOGNCvmHHqZzBtzFrmfdJCuE7JVIxI4JboNziaBAjBIINFQiaTF4ft6ob9mWvtEw8yKWYzsja14PayIFgszyt3ticgI/0?wx_fmt=jpeg)

# 【安全圈】思科开发环境遭黑客攻破，超 300 个核心代码库外泄

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyH7KZInQrQzjtATjGgLvvu4PdictVTLGAN3xXsaL5nEDN3A0qBic1Rl1v7XjibPUOOpSDSib3BC9J1Yjqyg0bTn6d5lOs2Mq1Sp3ibw/640?wx_fmt=png&from=appmsg)

科技媒体 bleepingcomputer 昨日（3 月 31 日）发布博文，报道称思科内部开发环境遭遇黑客攻击。**攻击者利用 Trivy 供应链攻击中窃取的凭证，成功突破思科安全防线。**

黑客植入恶意的 GitHub Action 插件，大肆窃取系统凭证与核心数据，**盗走多个亚马逊云服务密钥，并在部分思科云账户内执行越权操作。**

黑客还克隆了超过 300 个 GitHub 代码库，**这些代码不仅包含思科 AI 助手等核心人工智能产品，还涉及多款未发布的机密项目。**思科已紧急隔离受损系统，全面重装设备并轮换安全凭证。

本次数据泄露事件直接波及思科的企业客户。被盗的代码库中，**受害者名单涵盖大型银行机构、业务流程外包公司，甚至包括美国政府机构。**

这起入侵源于本月爆发的 Trivy 漏洞扫描器供应链攻击，黑客攻破该项目的官方发布管道，通过恶意插件大范围散播窃密软件。

现有证据表明这起攻击事件的主谋是 TeamPCP 黑客团伙，该团伙频繁使用专属窃密工具，持续攻击各类开发者代码平台，已威胁数千个内部构建环境。

尽管思科已切断初期的入侵途径，但安全危机远未结束。安全专家警告，思科仍需防范 LiteLLM 和 Checkmarx 供应链攻击引发的连锁反应。

***END***

阅读推荐

[【安全圈】小米新推出的输入法工具直接暴露AI模型密钥](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075253&idx=1&sn=1c85eb1ed9b6a52eda306974d0aff543&scene=21#wechat_redirect)

[【安全圈】360漏洞挖掘智能体发现OpenClaw高危漏洞，或波及全球17万实例](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075253&idx=2&sn=1c58b6f95327d26411281829e92a8fcd&scene=21#wechat_redirect)

[【安全圈】上海电信大规模断网，官方：宽带正常升级导致](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075253&idx=3&sn=8f39b5ecc97049877fd8c3fc36a901a3&scene=21#wechat_redirect)

[【安全圈】DeepSeek崩了！超过11小时仍未被修复](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075204&idx=1&sn=0d5532dced2ed29ce8b6dce346ba8f9f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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