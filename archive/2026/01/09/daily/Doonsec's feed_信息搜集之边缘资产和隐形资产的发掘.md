---
title: 信息搜集之边缘资产和隐形资产的发掘
url: https://mp.weixin.qq.com/s/jVi2qTARBgMHFLY_algV_Q
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:28:05.883716
---

# 信息搜集之边缘资产和隐形资产的发掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXQuY7oPxUSGhJHPvZTV4UFibY1bHibcqKtAAnADbreiau6RcuC33fLdywg/0?wx_fmt=jpeg)

# 信息搜集之边缘资产和隐形资产的发掘

曾哥

国家网络空间安全云社区

![]()

在小说阅读器中沉浸阅读

近期有不少师傅咨询：常规的漏洞原理和利用都捻熟于心，但是为什么在SRC挖掘和攻防中，往往就是挖不到漏洞呢？

答案有两点：一是实战的经验比较少，对于漏洞在哪出现，有什么手法还掌握得不多；二是信息搜集没有得到要领，只会僵硬地进行信息搜集，对于边缘资产和隐形资产的发掘没有经验。

今天咱们就来好好唠唠这个“边缘资产和隐形资产的发掘”，为什么它在攻防场景下如此重要？

*注：本篇重心在于如何在攻防当中更快发掘脆弱资产，从而实现GetShell，并不关注XSS/逻辑漏洞这种漏洞。*

**01**

**什么是边缘资产和隐形资产？**

**在攻防中，整个攻击链路大致为七步：信息搜集/漏洞利用/建立据点/权限提升/权限维持/横向移动/痕迹清除。其中每一步都是承上启下，没有上一步就做不了下一步。**

而整个攻击链的开头——信息搜集就尤为重要，其实信息搜集是渗透测试中最简单的部分，也是渗透测试中最难的部分。渗透测试的本质是信息搜集，一个优雅、成熟的攻击者，一定是在信息搜集中拥有“灵敏嗅觉”的猎人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXWsusgn6Gg0Wt94lkhiamJPLSMBSlf63Yc65KK1OdwQWZDozsOZicQKvw/640?wx_fmt=png&from=appmsg)

在渗透测试的过程中，收集到目标的信息越多，渗透切入点就越多，对目标渗透的成功率也就越高。

而我们纵观信息资产的时候会发现，如果我们能找到目标最短的那块“短板”，就使得渗透测试更能成功，而这块“短板”一般不在正面，通常出现在侧面或者背面，这就意味着通过正面的资产信息搜集，往往无法搞定目标。

其实从企业安全负责人的角度来说，做暴露面收敛和边界安全的时候，一定是先做完正面资产（主域名下的所有子域名以及正式服务器）的架构梳理及风险排查，那攻击者去打主域名基本也是一无所获的状态。

这就意味着，对于边缘资产和隐形资产的发掘，才是渗透测试信息搜集的重点。那什么是是边缘资产和隐形资产呢？

* **边缘域名资产：**域名非主域名（可能是具体业务组或者全资子公司在用）；
* **隐形IP资产：**以IP形式提供服务（无法通过域名找到，可能是开发测试遗漏或者内部人员使用的系统）；
* **隐形C段资产：**目标持有该C段内一部分或者全部公网IP，开放提供具体业务服务；
* **关联性：**一定是企业的边缘业务平台，具有目标相关的具体特征。

**02**

**针对边缘域名资产的收集**

**2.1 找到目标旗下所有的备案域名**

通过爱企查、企查查平台查询：所有备案域名、所有微信公众号、所有微信小程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXZZIMW2EOX6UL1WeyFsEPAvue3RIt7vJSGav2agKDmaf1o59o9XmYVw/640?wx_fmt=png&from=appmsg)

通常情况下，如果挖腾讯相关的漏洞，首先想到的办法肯定是去看看qq.com，但是先别急，把旗下备案资产全拉出来，会发现有很多没见过的备案域名，而这些域名可以多多关注，肯定比正面的主域名要更好出漏洞。

**2.2 边缘子域名**

测绘SSL证书（挖SRC也有效）：https://crt.sh。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXicvFbqcJ3blvOZGNhaWgP6lf1gN6Q0pIybCAjx5eTRFK8svy5JTMFrA/640?wx_fmt=png&from=appmsg)

适用于补齐子域名缺失，以及找到一些多层级的子域名系统。

**2.3 小程序漏洞挖掘**

微信小程序抓包（新的域名==>查看是否为供应商==>大概率没有WAF）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IAhWCw7hRsjHpje25qhWYMzvo5fSPQdDDSnsk6e0JmGhu2U4lAlex9Tw/640?wx_fmt=png&from=appmsg)

通过企查查平台能更快找到企业旗下小程序，通过抓包可以尝试对小程序进行渗透测试。

同样，因为小程序架构的原因，基本不存在WAF，可以尝试通过联动Xray的联动自动挖掘漏洞：https://docs.xray.cool/tools/xray/advanced/burp。

**03**

**针对隐形IP资产的收集**

**3.1 常规测绘语句**

* 通过HTML正文包含的ICP备案号进行查询：body="京ICP备0\*\*\*\*\*\*\*号" && country="CN"；
* 通过企业的Icon图标进行资产测绘。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IA74cuy1zrJvY4sVANRl5JDJ5TLFUbCSqF5s2ibazYI4HD54QwqS2WqEQ/640?wx_fmt=png&from=appmsg)

**3.2 非常规测绘语句**

【关键点】林业局、工商局、农业农村局、学校？怎么测绘边缘资产？

重点在于，要根据目标的具体业务熟悉，联想关键词进行Fuzz测绘：林业管理、树木管理、城市规划、招商平台、融资平台、智慧农村、智慧基建、智慧城市、交通管控、智慧交通、智慧校园、智慧课堂、学习平台、学生管理、党建平台、宣发平台、入学系统、学业平台、智慧入学、校园卡、学院系统、智慧就业、智慧社区、社区管理。

**重点：**首先要打哪个地方的资产，要限定资产的省份/城市。因为一般除了云上资产（CDN等），资产所属IP都在该省/市的范围内。

根据关键词进行省份内测绘：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXEtmUAicCajdk3nMhDWHeTZIibrC6fhfEmGJWVHzM1xObzunWEV0JRv4w/640?wx_fmt=png&from=appmsg)

根据关键词进行管理平台测绘（适合想不到合适业务关键词）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXSltRnib8nuXwG50p3PTSBqsMwm2qicQ3johLuWnv6qp9RVlrsicGjhMvQ/640?wx_fmt=png&from=appmsg)

根据关键词进行文件上传接口测绘：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXV2L1lLzxFuKg9NKIwNpq5UlJe04mKXMJFNA07VLqf9kWEsTjOdJHdw/640?wx_fmt=png&from=appmsg)

批量导出==>查看相关的网页Title==>筛选出一批比较符合的资产==>手动验证

如果这项技能熟能生巧，会有很大的威胁性，想学习或者有疑问的师傅可以私下找作者咨询。

**04**

**针对隐形C段资产的收集**

**4.1 真实源站C段测绘**

备案域名==>IP指向C段==>确定是否为CDN（微步查询）==>不是CDN，直接打C段（确认是否为公司资产）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IAYgE30n0RGo12wXjgjiaJmlLiaIHAYwNVGeTjHKo0MC1kQIeNQTBo2J7A/640?wx_fmt=png&from=appmsg)

通过ARL的C段功能，可以点击IP降序排列，能很清晰看到域名解析IP有多少指向同一个C段，该C段涉及多少个域名，如果涉及IP和涉及域名都很多，就是重点C段资产

如果想要部署ARL的师傅可以看这个项目：https://github.com/Aabyss-Team/ARL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IAwSHBvRDnwCEt8jwvJSXahVY6ZX7Al9Bd1NBGR11d9ue4EZSo5F8jyA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmX8fZ22RWxR5hmRQ5KHfs3YYhA1sVgDJ8HGy235WRpRgmL9vhblcKXttkCWCkbPYaJxwvjVnkzSSKw/640?wx_fmt=png&from=appmsg)

可以看到，目标IP存在有效合法证书，可以用于验证该IP归属具有强关联性

通过这个方法，基本确定该C段为该目标企业的真实C段，可以直接去测试该C段开放的服务是否存在漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IAj87iaBNIjQEYsXq13JlN4gCtC9qU6d9vVAZ6CNBhPowaU9EI0guic7Yw/640?wx_fmt=png&from=appmsg)

**4.2 历史源站C段测绘**

对于一个网站的开发，特别是大型网站的制作，其实需要很长的一个过程。在一些网站刚开始搭建的时候，为了调试方便和测试选项，是不会套CDN和负载均衡进行上线测试的，这个时候可能就会被记录到历史解析IP，我们就能通过查询历史解析IP看看是否为真实源站IP或者业务公网IP。

工具地址（需要代理才能访问）：https://securitytrails.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IA7hl55kNyA9Bm5yqRVyuibYPicqEK8VQEGHWeqyB7cGj4hVqbFPc2ZRDg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IAbcTUaicGLt55fnbia5I1hJTaicBpnFia9YU5h0WPykny8ddSZDBPUD700g/640?wx_fmt=png&from=appmsg)

当然，对于这个测绘的操作，一定要认真验证，因为很有可能找到的IP及C段可能目标已经不再用了，要结合Fofa测绘结果来做综合研判处理！

**05**

**针对敏感信息泄露的搜集**

**5.1 Github开源项目信息泄露**

针对这点的公开资料较多，这里就不再赘述。

**5.2 网页敏感信息泄露**

通过搜索引擎进行搜索：目标域名/名称 默认密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IALD762y3OXpSAia2lkzV7EBGZvviafyWgSwmzIUgc60XjOwkGt7UZHCmw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmX8fZ22RWxR5hmRQ5KHfs3YYTg1ibzSAmWXLicrRKGrpu3FseKxzS8GKDwibZy0ujotL4C16gicE8mnmEA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXicBwUGzREuqzqOO0tdfA2IA9icFupL0fWibn9npN2joLm6JO9xYUWqmBicrCDEDwPibeP7MGAoahUTbsQ/640?wx_fmt=png&from=appmsg)

通过这些方法，可以通过开源情报（OSINT）找到许多学号、工号和默认密码。

**5.3 历史账号密码泄露**

历史账号密码泄露是由许多原因造成的，如历史上遭遇黑客攻击导致数据泄露，又如遭到病毒、木马攻击导致浏览器内凭据被窃取等等。

可以在海外频道获得一些泄露，也有许多频道已经被封禁：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXnJXBibN5Cgcp0PG0mweIiczQ6BwNxAic3yaAYSnA12EeQK9MMom9qcdeQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibDFwJ9QSB1LFMVOoMVD0YXsicKLiaTmvfiaTmh7icNOYicm5iciaLibUQia2iblaQBqRRfR2iatXdH6LLuqmIQg/640?wx_fmt=png&from=appmsg)

里面基本是一行一条，包含网站URL，账号及密码，还有许多其他渠道可以获得质量较高的泄露，欢迎在文末评论区分享交流！

**-END-**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibiaMN9FTPWAS1TQMIhBskub3h6JDA6eRQVElKiccYfkLq8UNjNRSx9XVJBy8ucZGfgicrRq04dCeDCA/0?wx_fmt=png)

国家网络空间安全云社区

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/JthAicibVjmXibiaMN9FTPWAS1TQMIhBskub3h6JDA6eRQVElKiccYfkLq8UNjNRSx9XVJBy8ucZGfgicrRq04dCeDCA/0?wx_fmt=png)

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