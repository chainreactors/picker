---
title: 泄露用户信息长达一年半，丰田被服务商坑惨了
url: https://www.freebuf.com/news/361832.html
source: FreeBuf网络安全行业门户
date: 2023-03-29
fetch_date: 2025-10-04T11:01:36.225925
---

# 泄露用户信息长达一年半，丰田被服务商坑惨了

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

泄露用户信息长达一年半，丰田被服务商坑惨了

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

泄露用户信息长达一年半，丰田被服务商坑惨了

2023-03-28 17:02:49

所属地 上海

全球知名汽车制造公司丰田（TOYOTA）遭遇了严重的用户信息泄露事件。安全研究人员发现，黑客通过攻击丰田意大利数字营销自动化和分析软件服务提供商 Salesforce Marketing Cloud，从而获得了海量的用户数据，且至今为止数据泄露已有一年半之久。![](https://image.3001.net/images/20230328/1679994135_6422ad178c143d17f6923.jpg!small)

此外，丰田意大利还泄露了软件公司 Mapbox 的应用程序编程接口 (API) 令牌，导致敏感数据泄露范围增大。攻击者可能会借此获取丰田意大利用户的手机号码和电子邮箱等，并利用这些信息发起网络钓鱼攻击。

好消息是，截止到发稿时，丰田意大利已经将这些数据再次保护起来，该公司也表示，已经和第三方网络安全公司合作，采取了额外的措施加强其网络安全系统和协议。

公开信息显示，丰田是全球最大的汽车制造商之一，拥有超过37W名员工，去年收入约为2670亿美元。仅在欧洲，丰田的雇员就超过了2.5W名，共有八家汽车制造工厂。

目前虽然不清楚丰田意大利的官方数据，但是该公司已经在意大利屹立半个多世纪了，妥妥的老牌企业。根据 Statista 的数据，丰田意大利公司的收入预计到 2023 年将达到约18亿美元，汽车销量预计将接近8.3w辆。

## ****偶然发现数据被公开****

2023年2月14日，Cybernews的安全研究团队在丰田意大利官方网站上发现了一个环境文件(.env)。而该环境文件于2021 年 5 月 21 日首次被物联网 (IoT) 搜索引擎编入索引，这意味着很多人都可以进行公开访问。

根据 Cybernews 研究团队的说法，该环境文件泄露的原因是，丰田意大利数字营销自动化和分析软件服务提供商 Salesforce Marketing Cloud公开了用户账户凭证访问权限。黑客获取了Salesforce Marketing Cloud公司的权限，并借此访问丰田意大利用户的账户凭证。

通过账户凭证，攻击者顺势访问到了用户的电话号码、电子邮件地址、客户跟踪信息以及电子邮件、短信和推送通知内容。同时这些凭据可以进一步被用来发送虚假的SMS消息、电子邮件、编辑&启动营销活动、创建自动化脚本、编辑与 Salesforce 营销云相关的内容，甚至向丰田的客户发送推送通知。

Cybernews 安全研究人员称，此次敏感数据泄露事件对于丰田意大利来说十分严重，这些信息完全可以被用来发起一些复杂的网络钓鱼攻击，攻击者可以访问和控制丰田的官方通信渠道，从而使受害者更容易落入此类钓鱼攻击中，因为发件人的信息是被冒充的丰田意大利官方。

此外，丰田意大利还泄露了软件公司 Mapbox 的应用程序编程接口 (API) 令牌。虽然这部分数据不像 Salesforce Marketing Cloud 账号凭证那么敏感，但是攻击者可能会滥用它来查询大量请求并增加丰田 API 使用的成本。

## ****丰田********官方********回应****

Cybernews 将此漏洞告知丰田后，该公司立即采取了必要的措施来进行补救。据丰田公司称，此次安全事件的出现，是对方未能遵守公司的数据安全政策造成的。

目前丰田公司已经采取了一套额外的安全措施来恢复和加强网络安全系统和协议，并及时向意大利有关当局报告了隐私数据暴露的风险，全力配合正在进行的调查。

丰田公司进一步表示，丰田非常认真地对待此次事件，也非常重视网络安全建设，我们将借此机会从调查结果中吸取教训，进一步提升网络安全防护能力以及协议的安全性，防止再次出现此类安全事件。

目前尚不清楚攻击者具体访问了哪些数据，但丰田公司建议用户高度警惕网络钓鱼攻击，及时更换账号密码，以确保个人信息安全。

丰田公司称：“骗子可能会试图向您发送冒充丰田或任何其他流行品牌的虚假消息，因此请确保通过启用多因素身份验证 (MFA) 来保护您的电子邮件地址。小心电子邮件，不要点击链接或提供任何个人信息。如果您发现电子邮件可疑，请将其报告给您的提供商。

当涉及到电话号码时，您可能会受到垃圾/营销/钓鱼短信的轰炸，甚至会发现自己成为 SIM 交换攻击的受害者，攻击者部署该攻击以获取对基于 SMS MFA 代码的访问权限。”

这不是丰田第一次在网上公开其数据并将自身和客户置于风险之中。

2022年，丰田公司近30万用户数据被泄露，包括电子邮件地址和客户管理号码。开发人员在 GitHub 上发布源代码后，通过其客户应用程序 T-Connect 公开的数据已经泄露了五年。

2023年 1 月，丰田汽车在印度的业务也曝出信息泄露事件，部分用户的个人信息很有可能已经被攻击者获取。

参考来源：https://cybernews.com/security/toyota-customer-data-leak/

# 漏洞 # 黑客 # 数据泄露

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

偶然发现数据被公开

丰田官方回应

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)