---
title: 黑客利用AI工具HexStrike+Claude渗透酒店预订平台
url: https://mp.weixin.qq.com/s/-FFsoRHAA1hwDdKWDMEOIQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:59:54.133972
---

# 黑客利用AI工具HexStrike+Claude渗透酒店预订平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MQnCJmxmL8j97jY1LQc9wfISQ1sVfO6rnDF6ibh5ZClXXJv8QHOB9iaqW4icibwFhibMRlvricCuEuhS72wicDzvIxvwFPopC4fUhVXI/0?wx_fmt=jpeg)

# 黑客利用AI工具HexStrike+Claude渗透酒店预订平台

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PEtrnib92D2oK87RibXnQvpZCZAkK3atZrcptiahK7489EsepicU8jY03gBQqJmM9H50cKQRKIY72vFj6hjQLAHDmMSOQic6mQ150A/640?wx_fmt=png)
> **导语**：尽管AI公司承诺安全性，恶意攻击者仍在不断寻找创意方式将AI代理用于非法目的。安全研究人员发现一名俄罗斯黑客利用HexStrike AI结合Anthropic的Claude，成功入侵多家酒店预订平台，窃取超过210万条邮件地址及相关预订数据。

---

## 一、事件概述

2026年4月16日，网络安全研究团队发现一台由威胁 actor 拥有的服务器意外暴露在公网。研究人员在服务器中发现了针对多家住宿行业公司的攻击详情、源代码以及数据窃取结果。

攻击者使用 **HexStrike AI**，这是一款集成大语言模型（LLM）的开源工具。在本次攻击中，攻击者将其与 Anthropic 的 AI 代理 Claude 结合使用。

研究人员表示："Claude配置文件包含该威胁 actor 的个人邮箱，这帮助确定了攻击者身份——他是一名俄罗斯公民。"

![攻击者Claude订阅详情](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NEEhq5V5OqYHQqcuricg45jvygofkMgdyCOL4e4sVmmpuatPuREem2akgRnMMlpS1Tf5Jdmc4JVf2FqrfY7icibJZGkkhicm9GTcQ/640?wx_fmt=jpeg "攻击者Claude订阅详情")

---

## 二、攻击手法分析

### 2.1 HexStrike AI工具

HexStrike AI 是一款开源工具，允许用户匿名运行网络安全工具，作为自动化渗透测试平台。然而，一旦落入恶意攻击者手中，漏洞扫描即可轻易转变为未授权访问。

![HexStrike AI配置](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N0pXlAgI3nrfd9vxGiaYPzBWm8wibaIEo9qYlVjicrwZ6LuoCn9AVGsiceQjZzwmic3KoG6eKiaM3daPBSgMvwVZIegyEw1r2Je6WJo/640?wx_fmt=png "HexStrike AI配置")

### 2.2 绕过AI安全防护

研究人员发现，该俄罗斯黑客通过将恶意活动伪装成合法的渗透测试，成功绕过了LLM的安全防护。在AI辅助下，攻击者针对住宿行业公司生成了至少50份渗透测试报告。

"每份报告都包含执行摘要、目标基础设施信息、发现漏洞、利用方式及结果、发现的数据类型以及缓解建议。"研究人员解释道。

![渗透测试报告示例](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OyO5gIliaa7BiaaXhzHu4icIR6ex9R3SLDYoAU0oB6c43icfnImIcsAOZ8gQnF5JwcdbFOqhtTR4aHL6JsgMLf9zGfJicrHqwCnpZY/640?wx_fmt=png "渗透测试报告示例")

### 2.3 服务器内容

在暴露的服务器中，研究团队发现了数百万份与预订相关的文件，包括：

* 安装的黑客工具摘要及配置
* 各种代码库文件
* 从目标系统窃取的数据（主要包含住客个人身份信息及房东详细信息）

导出的文件包含 **210万个唯一邮件地址**，可能与暴露的个人数量相关。

![唯一邮件地址统计](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MHdf2PgpZgFDKDaaEdAICfPLTBxOaWYbxS96yuictqJCl6cjB5iblkSsgx6kqLGkLutFibAvTvia1WT3deicgoYicNibRN39Lvdlw6dM/640?wx_fmt=jpeg "唯一邮件地址统计")

---

## 三、受影响企业详情

由于攻击者在调查期间将服务器撤出公网，研究人员无法提供完整的受影响企业列表，但已确认至少以下几家企业：

### 3.1 RoomScope（泰国）

为酒店管理解决方案提供软件的泰国软件开发公司。约640万条预订记录，包含住客姓名、110万个唯一邮件地址、电话号码及额外订购服务。

![RoomScope预订记录](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PaAIK2siaHWKIhErDbRrf6stD2BUFlcl5ercEN7PbSvf1gpsEkSQSOaJvpNWdEqMhLEoYPZEWEDSEhnibARl3LoLwibTyB9SnzuI/640?wx_fmt=jpeg "RoomScope预订记录")

### 3.2 IGMS（加拿大）

专注于物业管理系统（PMS）开发的公司。泄露数据包括房东电话号码、入住/退房日期、房东邮箱、房产地址，部分记录包含WiFi密码。研究人员发现约1400条IGMS记录。

![IGMS数据泄露](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PJxCEXibtWeCkkYBWTZIz9S79TwP6VDHDBXuKzmbAB6PvZRuStGPiaqBXlOHvibx1H2OUygYdnH2nraYp4jC28D41GsF8Z0fjK3A/640?wx_fmt=png "IGMS数据泄露")

### 3.3 NebulaPMS（南非）

由Hospitality Technology International开发的物业管理系统。发现200万条记录，包含住客全名、邮件地址、电话号码、入住/退房日期及酒店名称。

![NebulaPMS预订记录](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PV4ezJoAmkJ39HXkcwqVnbyo1uX954e9WLkr5R2ibzmibRiaib9nDmUuicNCHicmbpaqsW5PYufhCjT2x1ITKtHibgmIl3k0Nsq00y5o/640?wx_fmt=jpeg "NebulaPMS预订记录")

### 3.4 Staysee（日本）

专注于PMS软件的公司。泄露数据包含历史及未来预订数据，包括入住日期及住客个人身份信息。其中包括超过31000条支付记录（包含预订标识符、支付方式类型及金额）以及49000条产品记录（包含预订标识符、产品购买信息及价格）。

![Staysee预订记录](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MCrib2nhupbPRDSRyjvsdJiafaQsShwvz4SVKcuJ90r8gAvhKYMEqSXVZlBoQ0rldL3ibIPKdQ7aicH1Gv9U7H5yBABBn2gDXfOrs/640?wx_fmt=jpeg "Staysee预订记录")

---

## 四、后续响应

NebulaPMS向Cybernews表示，公司于2026年3月了解到"潜在数据泄露，此后已采取多项措施来修复此次泄露可能对其客户造成的影响"。

"NebulaPMS还表示："我们已进行了多项额外的渗透测试和安全扫描，并在发现漏洞时持续进行修复。我们还在加强密码策略，并实施了最佳实践密码保护安全标准，以更好地防止密码拦截或基础设施暴露。"

---

## 五、假期用户面临的风险

酒店预订平台是攻击者的理想目标，因为被盗数据可用于钓鱼攻击。当攻击者掌握受害者的准确姓名、旅行日期和预订编号时，钓鱼攻击尤其有效。

"由于这些机构处理大量个人和财务数据，此类攻击在数据窃取后极易在暗网上变现。本次攻击收集的数据也不例外。"研究人员解释道。

攻击者可利用这些信息伪造酒店官方邮件，由于用户担心错过预订信息，很可能会配合执行，从而导致更大的损失。

"这应促使酒店及住宿供应链中的其他组织更加重视数据安全，加大对网络安全人员或工具的投入，以减少可能的攻击面。"研究人员总结道。

---

## 六、安全建议

* **企业层面**：住宿行业公司应加强数据安全投入，定期进行渗透测试和安全扫描
* **密码策略**：实施强密码策略和多因素认证
* **监控告警**：建立异常访问检测机制，及时发现未授权访问
* **用户层面**：警惕陌生邮件和消息，核实任何涉及预订的请求

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Puc8HNiaVFMibMWyXuRCjam9iat0x1rCpsp1iatD7HveaKn7X0FMG8AlYEYZQbWQjAzjbYJjgdDQYTxLsn3W66vehH9V8LV2z9XnE/640?wx_fmt=jpeg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NJaWlOgGNt6DbZUibIWJ1CIhPX5Be64ePAYnHxT3Q4ThVqTKzMNiaQAYEjNaDlY9AthbLcIsrN4kPU1dqTEyiaAr3nialmYqMQh9o/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618755&idx=1&sn=48e0a85464fb20c73b6f338928a8f850&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PKBzibJnbda0CMK3x60eudMe9sX2keic0hP6ibj4r1vchm8wLibbC2LvvlTBXKJbfDqhJQQKCpqDeWnsEoxndVribgNu4ZZGlZ5KEw/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618776&idx=2&sn=a8fc65fd2a71822830022fc52d967bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M31JAE8U9E4F6SwkHX5V8dmziavPTqVQc7JdOHLa6PRExE28VUOIRk770kATgFwwvMibngxp6OBwXhjHATN3lVheGl5dVrSiaVa4/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618496&idx=1&sn=96ecdff99136258a4bf2cb156542311e&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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