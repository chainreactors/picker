---
title: 【事件分析】DeepSeek遭受大量境外网络攻击详细完整分析
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247535220&idx=2&sn=af665dff821641583006abf1d7d5d6d6&chksm=c14438c9f633b1df4a7d869e4537ed8b2640ac24ce5a777eca1d2ea106e4b6646b518f5a1ad1&scene=58&subscene=0#rd
source: 数世咨询
date: 2025-02-07
fetch_date: 2025-10-06T20:37:48.103752
---

# 【事件分析】DeepSeek遭受大量境外网络攻击详细完整分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqoWIDrMGDaly6HuZDqTel11PB3obJhXjMUEE1AlmlQnFQiaCZVJEMqfo8Ylx1hNpsxFfydWicPXFbEQ/0?wx_fmt=jpeg)

# 【事件分析】DeepSeek遭受大量境外网络攻击详细完整分析

奇安信集团

数世咨询

![](https://mmbiz.qpic.cn/mmbiz_png/QkjvmbC1CD0zJ9hBlrElSv4ZqETGn3otgH8VHW1QuoOec3JMAbUyr0iaurJy4DPHBwUsDXiadJ3aha4CvJwyYVew/640?wx_fmt=png)

1月28日，DeepSeek（深度求索）官网服务状态页面显示：**近期DeepSeek线上服务受到大规模恶意攻击，为持续提供服务，暂时限制了+86手机号以外的注册方式，已注册用户可以正常登录，感谢理解和支持。**

奇安信XLab实验室监测显示，DeepSeek近一个月来一直遭受大量海外攻击，1月27日起手段升级，除了DDos攻击，XLab实验室还发现了大量的密码爆破攻击，DeepSeek的AI服务和数据正在经历前所未有的安全考验。实验室相关专家表示，攻击未来将持续。

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaro9z6zXrX87TzDGlibMowXJuZjXplhicCw9jFGWtzrTW6In0Ko0n09FbA5ngWqFkZmibIdZJsDcTbUA/640?wx_fmt=png&from=appmsg)

“通过我们的持续监测，近期DeepSeek遭到了大规模、持续性的DDoS攻击，攻击可能从1月3日、4日就开始，27日、28日攻击手段升级，导致防御难度显著增加，因此更加有效，甚至对注册访问造成了影响”。奇安信XLab实验室第一时间披露并还原了本次DeepSeek遭DDoS攻击事件的幕后细节。

# 01

**引发硅谷华尔街“巨震”的DeepSeek是何方神圣？**

DeepSeek的爆火冲击了美股。美国芯片巨头英伟达27日一夜市值蒸发约5900 亿美元（约4.3 万亿人民币）。纳斯达克综合指数跌3.07%，台积电、甲骨文等AI明星股也遭遇集体暴跌。

作为国内领先的AI大模型之一，DeepSeek近一周全球爆红，不仅引发了硅谷的震动，更让华尔街陷入了恐慌，在外网被不少人称为“神秘的东方力量”，而国内网友更称其为“国产AI之光”。

苹果App Store美国区免费应用下载榜显示，DeepSeek超越ChatGPT，排名第一。美国总统特朗普表示，DeepSeek的崛起应当为美国企业敲响“警钟”。Meta创始人兼CEO扎克伯格也感叹DeepSeek非常先进，中美之间的AI差距非常小。

Scale AI创始人亚历山大·王（Alexandr Wang）公开表示，DeepSeek的AI大模型性能大致与美国最好的模型相当。“过去十年来，美国可能一直在人工智能竞赛中领先于中国，但DeepSeek的AI大模型发布可能会‘改变一切’。”

# 02

****奇安信：攻击从1月3日开始，27日手段变化，更难防范****

奇安信XLab实验室长期关注了DeepSeek上线以来的网络攻击状况，发现其具有持续时间长、变化快等特点，具体可以分为三个阶段：

**第一阶段，1月3日、4日、6日、7日、13日，出现疑似HTTP代理攻击。**

在该时间段，XLab可以看到大量通过代理去链接DeepSeek的代理请求，很可能也是HTTP代理攻击。

第二阶段，1月20日、22-26日，攻击方法转为SSDP、NTP反射放大。

该时间段，XLab监测发现的主要攻击方式是SSDP、NTP反射放大，少量HTTP代理攻击。通常SSDP、NTP反射放大这种攻击的防御要简单一些，容易清洗。

第三阶段，1月27、28号，攻击数量激增，手段转为应用层攻击。

从27日开始，XLab发现的主要攻击方式换成了HTTP代理攻击，此类应用层攻击模拟正常用户行为，与经典的SSDP、NTP反射放大攻击相比，防御难度显著增加，因此更加有效。

XLab还发现，1月28日攻击峰值出现在北京时间03:00-04:00（UTC+8），对应北美东部时区14:00-15:00（UTC-5）。该时间窗口选择显示攻击存在跨境特征，且不排除针对海外服务可用性的定向打击意图。

攻击指令趋势图：

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaro9z6zXrX87TzDGlibMowXJibXOSPHDWWzbgaibgJyImlhbn1mcJuicsR0NPTFyGBricjjXwDZuHBHr7g/640?wx_fmt=png&from=appmsg)

部分攻击指令如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaro9z6zXrX87TzDGlibMowXJIAHdybr4stRCpZfSm2S8w3JJkxutzX5iazGs7Sswv6A40hF3zqRbArQ/640?wx_fmt=png&from=appmsg)

此外，1月28号03点开始，本次DDoS攻击还伴随着大量的暴力破解攻击。暴力破解攻击IP全部来自美国。XLab的数据能识别这些IP有一半是VPN出口，推测也有可能是因为DeepSeek限制海外手机用户导致的情况。

# 03

****DeepSeek响应及时，将影响降至最低****

面对27日、28日深夜突然升级的大规模DDoS攻击，DeepSeek第一时间进行了响应和处理。XLab基于大网的passivedns数据，看到DeepSeek在28号凌晨00:58分在攻击者发起HTTP代理攻击这种有效且破坏力巨大的攻击时做过一次IP切换，这个切换时间和上面截图Deepseek自己的公告时间线符合，应该是为了更好的安全防御。这也更印证了XLab此前对本次DDoS攻击的判断。

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaro9z6zXrX87TzDGlibMowXJibO0B1XwwKGYQWolrZs0x94pxa0q9kzQtfSvdx2fouNEBX6FfiaxN82Q/640?wx_fmt=png&from=appmsg)

XLab安全专家指出，此次大规模攻击事件并非孤立事件，近年来，针对高科技企业的网络攻击呈现出愈演愈烈的趋势。攻击者动机复杂，既有出于商业竞争目的，也有企图窃取核心技术数据，甚至不乏一些国家背景的黑客组织，试图通过攻击手段遏制我国高科技产业发展。例如2024年12月18日，国家互联网应急中心CNCERT发布公告，发现处置威胁两起美对我大型科技企业机构网络攻击事件，足可见我国高科技产业面临的严峻威胁。

1月30日凌晨，即农历大年初二，奇安信XLab实验室监测发现，针对DeepSeek（深度求索）线上服务的攻击烈度突然升级，其攻击指令较1月28日暴增上百倍。XLab实验室观察到至少有2个僵尸网络参与攻击，共发起了两波次攻击。

“最开始是SSDP、NTP反射放大攻击，1月28日增加了大量HTTP代理攻击，今天凌晨开始僵尸网络（botnet）进场了，针对DeepSeek的网络攻击一直在层层加码，攻击手段越来越多，防范难度越来越大，使得DeepSeek面临的安全考验愈发严峻。”奇安信XLab实验室安全专家表示。

# 04

两个变种僵尸网络加入攻击，

指令激增100多倍

XLab实验室通过对DeepSeek持续近1个月的监测发现：攻击模式从最初的易被清洗的放大攻击，升级至1月28日的HTTP代理攻击（应用层攻击，防御难度提升），现阶段已演变为以僵尸网络为主。攻击者使用多种攻击技术和手段，持续攻击DeepSeek。

1月30日凌晨，XLab观察到2个Mirai变种僵尸网络参与攻击，分别为HailBot和RapperBot。此次攻击共涉及16个C2服务器的118个C2端口，分为2个波次，分别为凌晨1点和凌晨2点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkiafMs5L7TJx8Utqq8nlH1IiawkrNHvtvccGKW4WmSNZy1Z9wXP4aBkfWQ/640?wx_fmt=jpeg)

图：部分攻击指令详情

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkiaKnyd1AuTFnroic6E6Eq12QtGvscTbz91vBW1plVval4CzLGROicpp2sw/640?wx_fmt=jpeg)

图：攻击指令趋势

“僵尸网络的加入，标志着职业打手已经开始下场，这说明DeepSeek面对的攻击方式一直在持续进化和复杂化，防御难度不断增加，网络安全形势愈发复杂严峻。”XLab表示。

# 05

两个僵尸网络的身世揭秘

僵尸网络是由攻击者通过恶意软件感染并控制的设备网络，这些设备被称为“僵尸”或“机器人”。攻击者通过命令与控制（C&C）服务器向这些设备发送指令，执行各种任务，例如向目标服务器同时发起DDoS攻击，持续增加攻击规模和强度，耗尽目标服务器的网络带宽和系统资源，使其无法响应正常业务，最终瘫痪或服务中断。

本次采用的两个僵尸网络分别是HailBot和RapperBot，这两个Botnet常年活跃，攻击目标遍布全球，专业为他人提供DDoS服务。

其中，RapperBot平均每天攻击上百个目标，高峰时期指令上千条，攻击目标分布在巴西、白俄罗斯、俄罗斯、中国、瑞典等地区。具体攻击指令趋势和攻击目标地区分布如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkia5UgFCPL3V0UyiaItvvJUwOd2nm2pKZb1GzKwjCbWwyZltC9nYbIjUfw/640?wx_fmt=jpeg)

HailBot的攻击比RapperBot更加稳定。平均每天攻击指令上千条、攻击上百个目标。攻击目标分布在中国、美国、英国、中国香港、德国等地区。具体攻击指令趋势和攻击目标地区分布如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkiaypmc5K4EHlJyoaau5WuGH0KGsZubhZToDIfL5ZYLMZRHVEE8wtib6Ug/640?wx_fmt=jpeg)

从两张图不难发现，这两个僵尸网络“接单”频繁，符合典型的“职业打手”特征。XLab安全专家认为，僵尸网络攻击虽然是一种很古老的攻击方式，但依然屡试不爽。“很显然，今天凌晨这一波儿，黑客采购的是专业的网络攻击僵尸网络服务”。

# 06

树大招风？

中国明星企业易被攻击者“眷顾”

DeepSeek推出R1模型后不久，就凭借其性价比、开源及推理能力的提升等方面获得了广泛关注。除夕当天，DeepSeek还推出了新模型，其中Janus-Pro-7B在基准测试中击败了OpenAI。在外网被不少人称为“神秘的东方力量”。

DeepSeek的成功不仅引发了硅谷的震动，更让华尔街陷入了恐慌。就在1月28日，美国芯片巨头英伟达一夜市值蒸发5900亿美元，合4.3万亿人民币，纳斯达克综合指数跌3.07%，台积电、博通公司、超微半导体等科技股也遭遇集体暴跌。美国总统特朗普表示， DeepSeek的崛起应当为美国企业敲响“警钟”，美国公司“需要专注于竞争以赢得胜利”。

**关于XLab实验室**

奇安信XLab实验室专注于大规模数据环境下的网络态势感知、威胁分析溯源及安全数据平台建设。实验室拥有业内领先的超大规模多维安全基础数据平台和恶意样本及载荷捕获分析平台，覆盖PassiveDNS、僵尸网络跟踪、高级蜜罐系统等关键技术模块。

XLab实验室不仅为内部安全产品及业务提供海量数据支持，还持续进行威胁分析与情报产出，不断披露重大安全威胁，赢得了业内高度认可。此外，实验室还积极参与国家级科研项目，并与国际组织合作，致力于为全球客户提供高质量的安全服务与技术支持。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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