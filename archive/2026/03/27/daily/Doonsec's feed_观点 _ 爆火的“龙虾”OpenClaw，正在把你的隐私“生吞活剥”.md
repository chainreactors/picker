---
title: 观点 | 爆火的“龙虾”OpenClaw，正在把你的隐私“生吞活剥”
url: https://mp.weixin.qq.com/s/msdlCjhNlVwC7F7kVJ8Tag
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:14:48.296959
---

# 观点 | 爆火的“龙虾”OpenClaw，正在把你的隐私“生吞活剥”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kdBgUloeCu9QMtia3Sgtafm1d5kHh3Zzopp1RGT19OXsh7756gHyu2IibShiaH5FwXfyicNt8fgxUF6lehPhw7UiccyNEicsdTzjp1ic0Q72j6FAKE/0?wx_fmt=jpeg)

# 观点 | 爆火的“龙虾”OpenClaw，正在把你的隐私“生吞活剥”

原创

李可歆
李可歆

工业安全产业联盟平台

![]()

在小说阅读器中沉浸阅读

**给你的AI开“上帝模式”，可能是在给黑客开后门**

“养虾”这个梗，最近在科技圈彻底火了。

这个被戏称为“龙虾”的OpenClaw，被称为“史上增长最快的开源AI项目”，短短几个月在GitHub上狂揽近30万颗星。它最大的卖点是什么？让AI真正替你干活——管理邮件、订外卖、写代码、操作电脑，像一个“数字员工”一样24小时在线。

听起来很酷，对不对？

但你有没有想过：当你把这个“数字员工”请进家门，给它最高权限，甚至让它能直接操作你的电脑系统——万一它“叛变”了呢？

就在过去一个月，OpenClaw的安全问题集中爆发。国家互联网应急中心（CNCERT）紧急发布风险提示，中国信通院联合高校发现了高危命令注入漏洞，全球已有超过27万个OpenClaw实例暴露在公网上，其中40%与已知APT组织存在关联。

今天，我们就来深扒一下“养虾”背后的三大安全陷阱，看看这个网红AI是如何变成“特洛伊木马”的。

**供应链投毒——你以为在装“龙虾”，其实在请“木马”**

**案例：GitHub官方仓库惊现恶意技能，专偷加密货币钱包**

如果你以为“只从官方渠道下载就安全了”，那OpenClaw的故事会让你重新思考这个假设。

今年3月初，安全研究人员在OpenClaw的官方Skill仓库中发现了一个伪装成“LinkedIn智能求职系统”的恶意技能。这个技能包装得极其专业，声称提供基于AI的职位搜索、简历定制、一键申请等功能，还配有精美的文档和教程。

但真正的杀招藏在前置条件里。这个恶意技能会告诉Windows用户：下载一个名为“AuthTool.exe”的程序（密码1234）来完成配置。而Mac用户则被诱导在终端执行一行命令，声称需要完成认证——实际上，一旦执行，恶意软件就会在后台静默运行。

这个恶意程序的真实身份是什么？专门窃取加密货币钱包、交易账户凭据的信息窃取木马。

更可怕的是，这不是孤例。研究人员对ClawHub上的2857个技能进行全面审计后，发现了341个恶意技能——这意味着每八个技能中就有一个是坏的。后续调查中，这一数字最终增长到了824个。

还有攻击者通过伪装NPM包 `@openclaw-ai/openclawai` 实施攻击，诱导开发者安装后，自动执行恶意代码，窃取浏览器密码、SSH密钥、云服务凭证，甚至iMessage历史记录。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC7pYzbgibRiapuwWjz4Hic38ubwsVw3ibQ7wXwxqINJVakXZkxib34ZfL7N67Xl6OnLOBhyoEXXf1wficJQ/640?wx_fmt=png)

**点评：**别以为“开源”就等于“安全”。当AI生态的插件市场缺乏审核机制，每一个“一键安装”都可能是在给黑客开后门。

**漏洞百出的架构——一个端口就能接管你的电脑**

**案例：端口18789成“任意门”，2小时被刷走1400元**

OpenClaw默认开放18789控制端口，这个设计缺陷直接导致了一系列灾难性后果。

2026年1月，安全研究员通过Shodan扫描发现，近千个OpenClaw实例完全没有设置任何身份认证，直接暴露在公网上。攻击者只需要扫描到这个端口，就能以最高权限接管设备。

这可不是理论风险。国内已有用户在安装OpenClaw后的第三天，因API密钥被盗，在凌晨收到了高达1.2万元的Token账单。还有用户更惨，仅仅2小时内就被刷走1400元。

在国外，一位工程师因为OpenClaw的漏洞，损失了25万美元的加密资产。攻击者利用跨域重定向漏洞，在OpenClaw的fetch-guard组件中窃取了授权凭证，直接接管了受害者的AI代理，执行了转账操作。

更令人担忧的是漏洞的数量。截至2026年3月初，OpenClaw已被披露82个CVE漏洞，其中高危漏洞33个。包括远程代码执行（CVE-2026-25253，CVSS评分8.8）、命令注入（CVE-2026-25157，CVSS评分8.1）、认证绕过等一系列严重安全问题。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC7pYzbgibRiapuwWjz4Hic38ubwsVw3ibQ7wXwxqINJVakXZkxib34ZfL7N67Xl6OnLOBhyoEXXf1wficJQ/640?wx_fmt=png)

**点评：**一个把安全责任全部转嫁给用户的AI框架，就像一栋不装门锁的房子——看起来豪华，实际上谁都能进去搬东西。

**权限失控——“数字员工”分不清“老板”和“骗子”**

**案例：Meta高管被自家“龙虾”删光200封邮件，AI无视指令拒绝停止**

OpenClaw最可怕的地方，不是黑客攻击，而是它自己就可能“失控”。

Meta超级智能实验室的AI对齐与安全总监Summer Yue最近遭遇了一起令人哭笑不得的事故：她的OpenClaw在运行过程中，直接删除了个人邮箱中的200多封邮件。当她试图让AI停止操作时，AI甚至无视了她的指令。

这不是“误操作”，而是AI对指令理解的偏差。当用户赋予OpenClaw操作文件系统的权限后，如果它错误理解了指令，或者在执行过程中被恶意提示词诱导，后果就是灾难性的。

火山引擎安全产品负责人刘森用了一个形象的比喻：OpenClaw就像一个聪明、勤勉的数字员工，但它还不太懂工作中的操作规范和边界。如果现在给它下达指令“把root目录删掉”，它真敢干，那这台电脑可就彻底打不开了。

更可怕的是“提示词注入”攻击。攻击者通过在网页中构造隐藏的恶意指令，诱导OpenClaw读取该网页，就可能导致它把用户系统密钥泄露出去。这意味着，黑客甚至不需要入侵你的系统，只需要让你家的“龙虾”看到一篇带毒的网页，就能让它乖乖交出隐私。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC7pYzbgibRiapuwWjz4Hic38ubwsVw3ibQ7wXwxqINJVakXZkxib34ZfL7N67Xl6OnLOBhyoEXXf1wficJQ/640?wx_fmt=png)

**点评：**给AI开“上帝模式”不是不可以，但前提是它得知道谁是“上帝”。当一个工具分不清“主人”和“骗子”时，给它越大的权力，就埋越大的雷。

**怎么“养虾”才安全？给你四条保命建议**

既然OpenClaw有这么多风险，是不是就完全不能用了？也不尽然。如果你确实想体验这个“数字员工”的威力，以下四条安全建议请收好：

第一，别在主力机上玩。 不要在装有重要文件的工作机上安装OpenClaw。使用虚拟机或者一台闲置的电脑更安全。

第二，把门锁好。 安装后立即更改默认端口，设置只允许本地电脑访问Web界面，绝对不要暴露到公网。添加身份认证和访问控制，别让任何人随便摸进你家。

第三，砍掉它的手。 遵循最小权限原则，缩减AI智能体的权限，特别是和财务、本地文件、运行命令相关的权限。需要执行高危操作时，强制设置人工二次确认。

第四，看好你的钱袋子。 设定Token上限并监控API用量。OpenClaw在执行复杂任务时可能消耗大量Token，没有额度控制，一张天价账单随时可能砸到你头上。

**结语：AI安全，没有“后悔药”**

OpenClaw的爆火，折射出整个AI Agent时代的安全困局：我们越是赋予AI“能动性”，就越需要思考如何控制它。

正如埃隆·马斯克所说：把root权限交给AI，如同给猴子递上一把上了膛的枪。当技术跑得比安全快，代价往往由用户来承担。

但问题在于，黑客不需要等待技术成熟。他们在扫描端口、伪造插件、窃取密钥——就在你阅读这篇文章的几分钟里，又有新的OpenClaw实例被攻破。

“养虾”可以，但别把自己“养”成黑客的盘中餐。

**· end ·**

责任编辑 | 赫敏

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