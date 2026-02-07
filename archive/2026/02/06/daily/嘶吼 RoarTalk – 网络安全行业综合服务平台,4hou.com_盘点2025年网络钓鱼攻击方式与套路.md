---
title: 盘点2025年网络钓鱼攻击方式与套路
url: https://www.4hou.com/posts/jBEB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-06
fetch_date: 2026-02-07T04:08:00.914071
---

# 盘点2025年网络钓鱼攻击方式与套路

盘点2025年网络钓鱼攻击方式与套路 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 盘点2025年网络钓鱼攻击方式与套路

山卡拉
[新闻](https://www.4hou.com/category/news)
2026-02-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)13583

收藏

导语：2025年已成为全球网络安全领域的关键分水岭。

2025年，网络钓鱼威胁彻底告别“广撒网”式的大规模随机攻击，全面迈入“精准打击”的工业化猎杀阶段。随着生成式人工智能（Generative AI）、多模态深度伪造（Deepfake）技术的成熟，以及这类技术与供应链体系的深度绑定，企业及组织的安全防御边界正被持续突破，脆弱性达到前所未有的水平。

下面将结合行业权威报告，对2025年度十大高发网络钓鱼套路进行深度拆解，所有案例均源自真实行业事件，供从业者参考规避：

**一、AI深度伪造+超个性化情感围猎**

这是2025年破坏性最强的钓鱼手段。攻击者不再局限于静态文字诈骗，而是通过采集受害者的音频片段、社交媒体视频等素材，实时合成足以以假乱真的虚拟形象，精准突破受害者心理防线。

![莱文斯坦距离解释及应用 (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260129/1769677082206344.png "1769677082206344.png")

**典型案例：**香港曾发生一起标志性案件，一名财务人员参与了一场有多位“公司高管”出席的视频会议后，按会议指令转账2500万美元，事后核查发现，除该财务人员外，会议中所有参与者均为AI生成的深度伪造形象[1]。

**技术支撑：**目前仅需几秒钟的语音样本，就能实现实时音频克隆，这种拟真度极高的方式，能直接绕过人类的理性判断，让人防不胜防。

**二、商务邮件欺诈（BEC）转向供应链渗透**

商务邮件欺诈已从早年的冒充高管发邮件诈骗，升级为更隐蔽的供应商邮件欺诈，攻击目标直指企业供应链结算环节。

**套路特征：**攻击者会先渗透供应商的真实邮箱，潜伏数月之久，详细研究其发票格式、付款周期、沟通话术等细节，完全模仿真实业务场景。

**攻击演进：**借助AI技术修改发票中的银行账户信息，给出的理由多为“年度审计需要临时更换结算账户”。由于发送邮件的地址是真实的，财务人员仅凭常规核对，几乎无法识别真伪。据数据统计，2025年上半年，供应商邮件欺诈攻击在所有BEC案件中的占比已飙升66%[2]。

**三、软件供应链钓鱼与开源生态投毒**

攻击者将目标锁定在GitHub、NPM等开源社区的维护者，通过钓鱼手段窃取其账号权限，进而向开源软件包中植入恶意代码，实现批量攻击。

**典型案例：**2025年9月的NPM平台攻击事件中，攻击者注册了伪域名npmjs.help，发送虚假的紧急更新通知，诱骗维护者泄露令牌，最终导致27个核心软件包被植入针对加密货币转账的恶意代码，影响范围覆盖数百万用户[3]。

**技术支撑：**攻击者利用莱文斯坦距离（Levenshtein distance）计算视觉相似域名，在数十亿次软件下载行为中精准定位目标，悄无声息窃取资产。

**四、跨平台全渠道渗透**

网络钓鱼早已跳出“邮件附件”的单一模式，实现全渠道覆盖。调查数据显示，约三分之一的钓鱼攻击通过LinkedIn、Microsoft Teams、Slack等办公工具，或社交平台私信（DM）发起[3]。

**核心套路：**攻击者先在社交平台养号数周，模拟真实职场身份建立信任关系，再发送看似合法的业务链接。同时针对移动端优化界面，伪造HTTPS锁头标志，让用户误以为是安全链接，从而点击中招。

**五、二维码钓鱼突破防御边界**

二维码的便捷性使其被广泛应用，但也掩盖了底层URL的不可见性，成为攻击者的新突破口。攻击者将恶意二维码嵌入邮件、公共停车场海报、伪造的电费单等场景，诱导用户扫描。

![莱文斯坦距离解释及应用.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260129/1769677136146899.png "1769677136146899.png")

**防御绕过点：**传统的安全邮件网关大多只能解析文本链接，无法识别图像中二维码指向的恶意地址，导致这类钓鱼邮件的投递成功率极高，轻易突破企业前端防御。

**六、短信与语音钓鱼爆发式增长**

2025年第一季度，语音钓鱼攻击量同比飙升1633%，短信与语音钓鱼已成为面向普通用户和职场人士的高发攻击手段[5]。

**技术支撑：**攻击者利用AI拨号器，不仅能克隆目标熟悉的声音，还能实时分析通话者的语气、反应，生成对应的回复话术，实现交互式诈骗。

**套路核心：**借助紧迫感压迫用户，常见名义包括快递丢包、银行卡冻结、欠费等，精准抓住民众的焦虑心理，诱导点击虚假充值页面或泄露个人信息。

![莱文斯坦距离解释及应用 (2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260129/1769677213153603.png "1769677213153603.png")

**七、浏览器原生利用与ClickFix诱导攻击**

这是一种非典型钓鱼模式，攻击者不依赖外部链接或附件，而是伪造浏览器原生提示，如：证书过期、文档显示异常、插件需要更新等，诱导用户点击“修复”按钮。

**套路核心：**用户点击“修复”按钮后，会触发隐藏的恶意脚本，进而诱导通过PowerShell执行攻击代码。由于全程使用系统合法工具，常规安全软件难以拦截，攻击隐蔽性极强。

**八、复合型社会工程学：刷单与投资理财场景融合**

这类套路在国内高发频发，堪称“诈骗之王”，其核心在于通过场景叠加降低用户警惕，实现精准收割[5]。

**套路升级：**已从单一刷单诈骗，演变为刷单+色情诱导、刷单+虚假兼职等复合模式。攻击者先通过小额返利建立信任，再结合金价暴涨、虚拟货币热点等时事，诱导受害者进入虚假理财平台，最终逐步套取资金，实施循环收割。

**结语**

网络钓鱼已正式迈入“工业化精准猎杀”的全新阶段，生成式AI、深度伪造等技术与各类钓鱼套路深度绑定、层层升级，攻击场景无孔不入，其威胁范围已全面覆盖企业核心环节与个人日常生活。面对这场无硝烟的安全博弈，企业亟需筑牢“技术+管理+意识”三位一体的防御坚盾，唯有主动升级防御能力、筑牢安全防线，才能在层出不穷的钓鱼威胁中站稳脚跟，切实守护自身与组织的资产安全。

**参考及来源：**

[1] <https://baijiahao.baidu.com/s?id=1799569751510292083&wfr=spider&for=pc>

[2] <https://hoxhunt.com/blog/business-email-compromise-statistics>

[3] <https://www.armorcode.com/blog/inside-the-september-2025-npm-supply-chain-attack>

[4] <https://pushsecurity.com/blog/2025-top-phishing-trends>

[5] <https://e-bits.com.au/the-2025-phishing-surge/>

[6] <https://www.mps.gov.cn/n2253534/n2253543/c9077933/content.html>

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?XyNDD4bp)

#### 你可能感兴趣的

* [![]()

  盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)
* [![]()

  新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)
* [![]()

  Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
* [![]()

  新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
* [![]()

  豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)
* [![]()

  2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

这个家伙很懒,什么也没说!

#### 最新文章

* [盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)
  2026-02-06 12:00:00
* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)
  2026-02-05 12:00:00
* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
  2026-02-04 12:00:00
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
  2026-02-03 12:00:00

[查看更多](https://www.4hou.com/member/azxO)

# 相关热文

* [盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)

  山卡拉
* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)

  胡金鱼
* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)

  胡金鱼
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)

  胡金鱼
* [豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)

  山卡拉
* [2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)