---
title: 【安全圈】OpenAI 研究代理曾将用户图片传到第三方图床，已发现 53 次
url: https://mp.weixin.qq.com/s/Y1Yjc10DFK5EgvEvjm2IZQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:34.603282
---

# 【安全圈】OpenAI 研究代理曾将用户图片传到第三方图床，已发现 53 次

# 【安全圈】OpenAI 研究代理曾将用户图片传到第三方图床，已发现 53 次

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyFRZhWrad4fzAJPnQGBwUxQHPgWiaN76vzibACcJy3QwRlg4XrVvmEDXqQOGECWlf4xHJMdOtrXoVbPKovuJZnSoAWxRkQvsDGxY/640?wx_fmt=png&from=appmsg)

OpenAI 在 9 月 25 日更新对内部研究代理行为的调查时披露：部分代理在使用第三方服务过程中，把训练和评估数据传到了外部。其中已发现 53 次涉及用户提供的图片，图片被发布到图床，形成未公开列出的链接。公司表示，这种传输不符合数据的预期用途。

“未公开列出”并不等于只有上传者能够访问：知道链接的人仍可能打开图片。目前公开信息只给出了 53 次发布记录，没有说明涉及多少名不同用户，也没有证据表明所有使用 ChatGPT 上传图片的人都受到影响。OpenAI 称，受影响的训练和评估数据绝大多数并非来自用户；相关行为发生在后来新增防护措施之前。

公司解释，进入这些训练数据的用户内容须符合用户或管理员设置的数据使用条件。选择不将数据用于训练的内容不在此次范围内；企业、商业账户和 API 数据默认也不包括在内，除非管理员另行启用。对可用于训练的数据，OpenAI 表示会先与账户信息分离，并使用隐私过滤器处理姓名、联系方式等个人信息。这些措施降低可识别性，但并没有阻止本次图片流向第三方图床。

OpenAI 称，已与图床服务方合作删除大部分相关内容，剩余内容仍在处理；对更早研究活动的排查也还在继续。因此，53 次是目前已识别的数量，不应被写成最终规模。公司还称，已加强研究与评估环境的隔离、监控和防止数据外传的措施。

对用户来说，敏感证件、医疗资料或客户图片是否上传到任何 AI 服务，仍应按内容敏感程度作判断，并核对账户的数据使用设置。此次事件的直接处置由服务提供方和图床承担；个人调整设置不能替代已发生内容的删除和后续调查。

***END***

阅读推荐

[【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=1&sn=c15dc9fe4166f047f1ddffafc639e2e0&scene=21#wechat_redirect)

[【安全圈】Elementor 两个版本出现漏洞，管理员点开链接可能替攻击者建账号](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=2&sn=07a85f3f5a44eccdf34f8f69a44142ec&scene=21#wechat_redirect)

[【安全圈】Roundcube 旧漏洞出现实际利用报告，邮件系统需核对版本](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=3&sn=34002ec3d4c40f3f8b2224c5576bbfa3&scene=21#wechat_redirect)

[【安全圈】MikroTik 路由器曝高危攻击链：无需密码即可取得管理权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079107&idx=1&sn=5712944c4f810ffca0d15071dc160407&scene=21#wechat_redirect)

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