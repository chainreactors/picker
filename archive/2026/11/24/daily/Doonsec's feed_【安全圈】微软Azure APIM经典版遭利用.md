---
title: 【安全圈】微软Azure APIM经典版遭利用
url: https://mp.weixin.qq.com/s/CSOumxRumRwIEJYRCi4eew
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:50.104936
---

# 【安全圈】微软Azure APIM经典版遭利用

# 【安全圈】微软Azure APIM经典版遭利用

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

微软，漏洞

**核心事实**：微软向全球受影响企业推送紧急安全通报（跟踪 ID: **MZK9-GH0**），确认 Azure API Management（APIM）经典版架构存在严重的未授权管理平面访问漏洞。黑客已在真实在野网络中利用该漏洞窃取企业托管的 API 凭证与机密，导致挪威能源巨头 Equinor 及区域电网 Skagerak Energi 相继触发入侵警报，挪威国家安全局（NSM）已向关键基础设施部门发出紧急处置指引。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHl2bZwyArYhibyBh7rTM02qfPPc0ONcSoqWveYXKsY1LbiaeSVqL91BnX9B5KeysGInsiaQc7o4tDfB34T3aYnf4DgK2zQ0BVuBo/640?wx_fmt=jpeg&from=appmsg)

Azure API Management（APIM）作为企业发布、管理、保护其跨应用接口的核心网关服务，通常集中存放着各类连通内部数据库、核心鉴权系统与第三方合作伙伴的高特权凭据。微软在通报中明确指出：未经授权的外部攻击者可在特定配置缺陷的实例中直接调用管理功能，读取服务内部存储的全部敏感机密。

## 🔍 受损资产清单：高特权凭据全线暴露

受漏洞影响的层级包括 APIM Classic 架构下的 Developer、Basic、Standard 以及 Premium 四种规格，而轻量无服务器的 Consumption 层和最新的 APIM v2 架构未受波及。根据微软官方通告，攻击者借此可能直接提取以下数据：

* **具名值（Named Values）机密**

  ：用户配置在 API 路由策略中的各类明文常量、数据库连接字符串及自定义鉴权头。
* **身份提供商凭据**

  ：与外部 Identity Providers（如 Azure AD、Google、GitHub 等）绑定的 Client Secret。
* **OpenID Connect 密钥**

  ：用于对接单点登录（SSO）与跨域授权协议的客户端保密凭证。
* **订阅密钥（Subscription Keys）**

  ：调用受保护下游 API 所必需的直接访问鉴权令牌。
* **直连管理 API 令牌**

  ：用于自动化运维与批量下发策略的管理级访问 Token。

## 💥 实战攻防复盘：零日绕过直抵 Key Vault

据 Reddit 上一名涉事企业安全运维负责人与多方技术情报还原，本次攻击的链条隐蔽性极高：

* **废弃遗留 API 成为突破口**

  ：黑客瞄准了 APIM 经典版后台尚未彻底下线的废弃老旧 API 接口。该接口存在逻辑鉴权缺失，允许攻击者伪造特权系统账号身份。
* **日志审计盲区**

  ：该遗留接口在处理请求时不生成标准的用户活动日志与访问跟踪，导致受害者在入侵初期完全没有触发 SIEM 异常告警。
* **横向打通 Azure Key Vault**

  ：某跨国团队是在监测到有外部 IP 使用合法的管理员特权 Token 登录 Azure Key Vault 提取密钥、且访问习惯严重违背日常白名单模式时，才最终顺藤摸瓜锁定了 APIM 的攻击入口。
* **能源行业率先撞线**

  ：挪威国家安全局（NSM）证实，最早侦测到并上报异常活动的正是挪威的能源基础设施单位。Equinor 与 Skagerak Energi 均紧急启动应急响应切断了可疑访问通道。

## ⚠️ 处置关键：微软补丁无法废除已失窃凭据

虽然微软已于 11 月 19 日在云端完成了控制平面的访问路径阻断并轮换了平台级密钥，但特别警告所有企业用户：**云端补丁不会自动吊销或使已失窃的客户侧 API 密钥失效**。运维与安全团队必须立即执行以下处置动作：

**步骤一：全量轮换 APIM 关联的所有凭据**
立即重置 APIM 实例中 Named Values 下的所有私钥、关联的 IdP / OIDC Client Secret、Webhook 签名密钥以及向第三方颁发的 API 订阅密钥，切勿存有侥幸心理。

**步骤二：全面复核 Azure Key Vault 访问审计日志**
调取 11 月 15 日至 22 日期间 Azure Key Vault、后端数据库与业务微服务的调用记录，重点核查非常用 IP 地址的非白名单读取行为。

**步骤三：核实自建及托管环境运行时构建版本**
参照挪威 NSM 发布的安全基准核查实例运行时版本，凡仍处于旧版运行环境的混合部署实例，须主动联系技术支持同步最新修复包。

**步骤四：启动架构向 APIM v2 迁移**
经典版 APIM 存在较多历史技术负债，建议规划升级到全面重构、具备更细粒度网络与角色隔离策略的 APIM v2 架构。

***END***

阅读推荐

[【安全圈】英伟达热修复驱动翻车：闲置9小时仍偷写36GB日志](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=1&sn=763967cc27dfc41b9938316226fa2d69&scene=21#wechat_redirect)

[【安全圈】AI Agent自主挖掘零日漏洞：11分钟拿下医疗服务器](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=2&sn=0979762f073753e029a45dc071f89129&scene=21#wechat_redirect)

[【安全圈】CISA紧急预警：VMware与Cisco等四枚高危遭在野利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=3&sn=cd19a06b8fed5919a4de9fec4b756e3a&scene=21#wechat_redirect)

[【安全圈】单月1130起勒索，3.11亿条数据被挂牌](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080017&idx=1&sn=70d92ae03f620a7ace3b8888d687816a&scene=21#wechat_redirect)

[【安全圈】UAC被曝蠢到离谱的绕过，微软不分配CVE](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080017&idx=2&sn=c4ef9c02feb49f867d9b5e707a06405a&scene=21#wechat_redirect)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过