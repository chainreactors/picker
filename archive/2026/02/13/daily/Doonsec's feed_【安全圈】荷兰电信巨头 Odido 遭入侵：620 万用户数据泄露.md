---
title: 【安全圈】荷兰电信巨头 Odido 遭入侵：620 万用户数据泄露
url: https://mp.weixin.qq.com/s/BdGwsg5Gw5PzBKBUjsXL4Q
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:20.750370
---

# 【安全圈】荷兰电信巨头 Odido 遭入侵：620 万用户数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFP4LD3nbFgXtJqGOA1Heu0mtYJibquoaI1tHQYpm1T16N5amKMe48eqJwZwzw25WFNNChBxNnG7AH2WjKpMRNibnQPcgRI3w65o/0?wx_fmt=jpeg)

# 【安全圈】荷兰电信巨头 Odido 遭入侵：620 万用户数据泄露

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFKuJBKbzo5a6JQcic1yA8jLwKaof3C6ibrFNkJZUtQNl5EwDYSnZ1rE7MmDVWfpTSKM4IlhTxd3OKKVCKQQ0OJrXsfjmwXslFKI/640?wx_fmt=png&from=appmsg)

总部位于荷兰的电信运营商 Odido 披露，其客户联络系统遭到未授权访问，约 620 万名用户的个人信息被窃取。被获取的数据包括姓名、住址、电话、电子邮件、银行账户信息以及身份证件编号等敏感字段。公司表示核心通信网络未受影响，移动通信、宽带与电视业务运行正常，但此次事件已正式上报至 Autoriteit Persoonsgegevens。

从公开信息推测，攻击并未触及电信核心网或计费系统，而是集中在“客户联系与信息管理平台”。这一类系统通常与 CRM、客服工单、营销数据库相连，数据集中度高，但往往与核心生产网逻辑隔离。攻击者疑似通过该系统的漏洞实现权限绕过或横向访问，随后进行批量数据导出。由于未披露使用勒索或加密行为，且未见公开勒索声明，更像一次“静默式数据窃取”，而非破坏型攻击。

事件时间线显示，异常活动在 2026 年 2 月 7–8 日周末被内部团队发现。说明攻击流量或访问模式已经触发监控规则，可能表现为异常 API 调用频率、批量导出行为或越权查询日志。Odido 随后切断未授权访问通道，引入外部安全团队进行取证与环境加固。从公司声明看，未泄露密码、通话详单、定位数据与账单记录，这意味着攻击范围可能局限于客户资料库，而非多系统横向失陷。

值得关注的是泄露字段的敏感程度。银行账户信息与身份证件编号一旦结合姓名、电话与地址，足以支撑高仿真社会工程攻击，包括定向钓鱼、伪造账单、冒充客服或金融诈骗。即便数据尚未在暗网或勒索站点公开，也无法排除后续分批出售或用于欺诈链条的可能。对攻击者而言，此类“干净数据集”在地下市场具有较高价值。

从攻击面分析，客户联系系统往往通过 Web 前端、API 网关或第三方客服接口对外暴露。如果访问控制策略过于宽松，或存在输入验证缺陷、认证逻辑错误、令牌管理不当等问题，便可能成为突破口。若系统缺乏细粒度审计与异常数据导出检测，攻击者可在不触发告警的情况下完成数据外流。当前未见证据表明使用勒索软件或破坏行为，更符合“定向数据采集”的攻击模型。

公司已通知受影响用户，并提醒警惕来自未知来源的链接、账单与支付请求。对于用户而言，风险重点不在服务中断，而在后续欺诈利用。建议重点关注以下风险场景：

第一，仿冒官方邮件或短信，诱导点击“账户异常”“账单更新”等链接；
第二，冒充客服索要验证码或银行确认信息；
第三，利用真实个人信息进行精准诈骗，降低受害者警觉性。

企业层面，此类事件再次印证“外围系统往往是主入口”。即便核心通信网络隔离良好，客户数据平台若缺乏零信任访问控制、严格日志留存与数据导出阈值监控，仍可能成为高价值突破点。

从态度上看，Odido 的披露节奏相对及时，主动向监管机构报告并公开影响范围，属于合规框架下的标准响应。但后续仍需明确几点：攻击路径的技术细节、是否存在凭证滥用、数据是否经过加密存储、以及是否已对所有高风险接口完成独立安全审计。只有公开透明的技术复盘，才能恢复用户信任。

对整个行业而言，这起事件的警示意义在于：在电信等高数据密集行业，客户资料系统的安全等级应等同于核心生产系统。数据本身就是资产，一旦失守，损失不一定立刻显现，却会在数月甚至数年内持续释放风险。

***END***

阅读推荐

[【安全圈】“本地回环”成突破口：Clawdbot 默认配置漏洞导致上千实例暴露公网](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=1&sn=9b1a9c993553c060ba4ff0723b80d66f&scene=21#wechat_redirect)

[【安全圈】7zip.com 并非官方：钓鱼站分发恶意程序](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=2&sn=9be4e7b66acf43666e3f3384a184941e&scene=21#wechat_redirect)

[【安全圈】Apple 紧急修复在野零日漏洞：dyld 组件被用于“高度复杂”定向攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=3&sn=56d3b7691413517a4c4f08c06962d8c9&scene=21#wechat_redirect)

[【安全圈】UEFI 安全启动证书 2026 年 6 月到期，微软已启动轮替更新](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=4&sn=46229fdaa0f74e089f4e426e295916b2&scene=21#wechat_redirect)

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