---
title: 荐读丨AI编程默认不安全：知名AI公司发生重大数据泄露
url: https://mp.weixin.qq.com/s/FR26TQqYhnewtcilfXqWFg
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:51.209087
---

# 荐读丨AI编程默认不安全：知名AI公司发生重大数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kdBgUloeCuibtOG2gLichfnln1r4FKcXKspCkcFlwpqE6ibuA15FVhICP0I7JicKThzQEBNbeHAgM7t4vkqPsfxcxa4BTwuCYlaOuR6tLicTIjBo/0?wx_fmt=jpeg)

# 荐读丨AI编程默认不安全：知名AI公司发生重大数据泄露

工业安全产业联盟平台

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Lovable、Vercel、Anthropic等多家知名AI公司近期均发生重大影响的数据泄露事件，前两家涉及大规模暴露/泄露用户数据，后者则是将明星产品的源代码公开暴露；

上述几起事件的原因不一，有默认设计暴露所有用户数据，有员工权限遭供应链投毒劫持，还有员工操作不当等。

4月23日消息，国际知名AI编程工具Lovable近期发生的安全问题，为专业软件工程师提供了又一个对氛围编程保持警惕的理由。

周一，X用户Impulsive点名Lovable，称这家瑞典AI编程初创公司发生了大规模数据泄露，“影响了2025年11月之前创建的每一个项目”。

该用户表示，仅通过自己的免费Lovable账号，就能够访问另一名用户的代码、AI聊天记录以及客户数据。

该用户称：“英伟达、微软、优步和Spotify的员工都有账号。这个漏洞在48天前就已被报告，但至今仍未修复。他们将其标记为重复问题，并一直未予处理。”

***0****1***

**Lovable承认权限设置不当，暴露所有用户聊天和构建内容**

对此，Lovable否认发生了数据泄露，并表示用户可以查看公共项目代码，是其有意为之的设计决策。

然而，这一声明在X上引发了争议。由于表述不够清晰，以及用户不清楚未来应如何保护自身数据，Lovable随后发布了第二份声明。

公司解释称，允许他人查看“公共”项目，是“为了方便用户探索他人正在构建的内容”。同时补充，自去年12月起，所有订阅层级已默认关闭公共可见性。

在第二份声明中，Lovable也承认了最初X帖子所指出的安全问题。

Lovable写道：“不幸的是，在2月我们对后端权限进行统一时，意外重新启用了对公共项目聊天内容的访问权限。一经发现该问题，我们立即回滚更改，使所有公共项目的聊天再次恢复为私密。我们感谢发现这一问题的研究人员。”

***0****2***

**AI编程产品没有在设计时就嵌入安全**

部分用户对Lovable的透明度表示赞赏，但也有用户认为，公司最初的声明是在推卸责任。

安全公司Hacker Minded创始人Tom Van de Wiele表示，这一事件“再次说明，在缺乏安全默认设置的情况下，又未能针对自动化与AI时代进行威胁建模，问题终将暴露”。

他补充称，让用户自行判断哪些内容是公开的、哪些不是，“最终往往会失败”。

ESET全球网络安全顾问Jake Moore表示，围绕该事件是否构成数据泄露的争论，可能掩盖了更深层的问题。

他在接受采访时说：“这并不属于传统意义上的数据泄露，但也绝非无关紧要。从本质上看，这更像是设计缺陷，因为数据是被暴露出来的，而非通过黑客入侵获取。”

他进一步指出：“当一家公司纠结于语义而非实际影响时，往往意味着安全并未从一开始就被纳入设计之中，这正是导致此次事件的现实原因。”

***0****3***

**易用和安全是一次权衡取舍**

总体来看，专业开发人员并不鼓励过度依赖AI，因为其可能生成混乱且未经充分测试的代码。他们认为，氛围编程还会带来信息安全方面的隐患，包括公司数据被意外暴露。

Van de Wiele表示，开发此类工具的公司通常面临取舍，需要在提升易用性与确保安全之间找到平衡，但这并不能成为防护不足的理由。

他说：“公司往往处于两难境地，一方面希望降低新用户的使用门槛，另一方面又要防范数据抓取者。”他补充称，对于可能被抓取并转售数据的用户来说，这确实会带来现实影响。

Moore表示，如果用户未能充分理解哪些内容会被暴露，氛围编程工具可能进一步放大这些风险。

他说：“氛围编程正在不断加速不良默认设置的传播，用户必须对此保持清醒认识，并建立必要的故障保护与备份机制。”

他认为，这种趋势可能使类似事件变得更加频繁。

Moore表示：“如果用户因AI编程工具的默认设置而意外暴露敏感数据，攻击者甚至无需发起任何黑客攻击。”

***0****4***

**接连发生数据安全事件**

在Lovable出错前的几周内，AI领域已接连发生两起重大数据泄露事件。

3月下旬，Anthropic错误泄露了一个包含近2000个文件和50万行代码的档案。当时Anthropic表示，“未涉及或暴露任何敏感客户数据或凭证”。

本周早些时候，网站托管平台Vercel表示，其发现一起安全事件，导致未授权用户能够访问部分内部系统。

Vercel称，该事件源于其员工使用的第三方工具Context.ai被攻破。攻击者借此接管了该员工的谷歌Workspace账号，从而进一步获得了对部分Vercel环境的访问权限。

Vercel在周一发布声明称：“我们正在积极调查此事，并已聘请事件响应专家协助调查与修复。我们已通知执法部门，并将在调查推进过程中持续更新相关信息。”

在2月的一期播客中，Andreessen Horowitz普通合伙人Anish Acharya表示，公司不应在业务的每个环节都使用AI辅助编程，因为相关风险并不值得承担。他同时指出，依赖AI编写代码本身就存在潜在风险。

参考资料：businessinsider.com

**· end ·**

来源 | 安全内参

责任编辑 | 赫敏

声明：本文由工业安全产业联盟平台微信公众号（微信号：ICSISIA）转发，如有版权问题，请联系删除。

![](https://mmbiz.qpic.cn/mmbiz_png/4FpQm8QaW5kiaicHTUwSf9sId0er1ytR3D1Sc1RPfDpmk8FiciciadlBic9jSUbt1ciaE3G3aKiaicickE5ficq81KuYplgow/640?wx_fmt=png)

**如需合作或咨询，请联系工业安全产业联盟平台小秘书微信号：ICSISIA20140417**

**往期荐读**

# **重磅 | [《自动化博览》2026年第二期暨《工业控制系统信息安全专刊（第十二辑）》上线](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247538207&idx=1&sn=b6029b0c433c25c3fefb43e5213e8167&scene=21#wechat_redirect)**

# **征求意见稿丨**[网络安全技术 工业控制系统网络安全防护能力成熟度模型（附下载）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247534222&idx=1&sn=d68a32374971e527f09613e27be69e7e&scene=21#wechat_redirect)

# **工信部丨**[关于防范针对DeepSeek本地化部署实施网络攻击的风险提示](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247532396&idx=2&sn=60d0742822974a8d649ef771a671fcae&scene=21#wechat_redirect)

# **干货丨**[长输油气管网工控安全防护：策略、实践与展望](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247532389&idx=1&sn=3369308f4696e8b953678a13d59bfa71&scene=21#wechat_redirect)

**DeepSeek分析丨**[零信任安全架构在工业领域的发展现状与未来展望](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247532379&idx=1&sn=1603721f3f669d1fe6c5773b5fb55489&scene=21#wechat_redirect)

# **数字化安全丨**[工信部印发《高标准数字园区建设指南》（附全文+图解）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247536123&idx=1&sn=5f062ee2b518557bce3d117e14135ab9&scene=21#wechat_redirect)

# **AI安全丨**[人工智能安全治理框架2.0版（附下载）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247534922&idx=2&sn=2e8770ce10818f912137a9be36d4359e&scene=21#wechat_redirect)

# **干货丨**[工业可编程控制系统加密技术研究](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247531456&idx=1&sn=847458b642638a1a1a849e4bf4916407&scene=21#wechat_redirect)

# **荐读 |**[安全人视角的DeepSeek洞察与思考](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247531456&idx=2&sn=32075f2a360b824080569155dd6929de&scene=21#wechat_redirect)

# **可信数据丨**[中国城市可信数据空间行业研究报告（附全文）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247535945&idx=2&sn=748a35cd2b21d11be2183522b875fd73&scene=21#wechat_redirect)

# **关注丨**[网络关键设备安全检测结果（第19批）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247531380&idx=2&sn=f2148e66d4e29457b7af1e644e232161&scene=21#wechat_redirect)

# **数据安全｜**[国家标准支撑《网络数据安全管理条例》生效施行（v1.0）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247535879&idx=1&sn=d8bb3dd7a37bc6a7f8e157fdc1f5866d&scene=21#wechat_redirect)

# **工信部、国家标准委联合印发丨**[云计算综合标准化体系建设指南（2025版）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247535167&idx=1&sn=f73612b1cd769b542520001fd9bb051b&scene=21#wechat_redirect)

# **国家标准丨**[数据安全国家标准体系（2025版），附下载](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247534784&idx=1&sn=a6bba24ce93af1ad70d4372d9cd411e2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpyKsyPqcbQnzEqbmYSDib90bZicWWGDc7kFPbaRiaVzC16MXUp4T0FY8cA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpMs8tAvMDjxib9jwveZic6lrGG8K5iaoRIibBzbMEOZ1iay9MmF0aJtvicHmQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpQrnsLdgPsjvdBHkvnibporOYKicPv4aBgHkEw0tLgNnDuOTOOAia2tPug/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpgJgfShwDlZNGBxX5EkH8XMYawAfotAVmiaoD9icCOE7l306nqjCsuibCw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdp1IQNNBb9Hm4vRAiaKFBY2gMMDZB2IBvpkaCEetNoQvPFnwv2Tb13PuA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5m076ZlbiboUbvLF6NlQdgP5sIgcKu4LiajXajBhNx9r9tkzBcU4snLHa9hUSZp0AO3Nicrz3FiaDp3ibw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4FpQm8QaW5mEU31mWUSZmGicwwT1Uib60NRHysYs82ggViaSvTIFolS7YLNhzOrphBrAZfUweSeLUKsjib1bynaAqw/0?wx_fmt=png)

工业安全产业联盟平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4FpQm8QaW5mEU31mWUSZmGicwwT1Uib60NRHysYs82ggViaSvTIFolS7YLNhzOrphBrAZfUweSeLUKsjib1bynaAqw/0?wx_fmt=png)

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