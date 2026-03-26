---
title: 专家观点丨信创背景下市政行业工业信息化安全探讨
url: https://mp.weixin.qq.com/s/aGEa2fphUjgrts5pcCcmqA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:28:39.084638
---

# 专家观点丨信创背景下市政行业工业信息化安全探讨

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kdBgUloeCu9wrHsSUcicjaTnPoRI47SjBRjqILnvNBFEs61aE9JN6icUKxagjSZBuHDg5icQZT07nytws1B9qctziat2zKZdPdruibaygQDLmLWg/0?wx_fmt=jpeg)

# 专家观点丨信创背景下市政行业工业信息化安全探讨

原创

刘杰，解存福
刘杰，解存福

工业安全产业联盟平台

![]()

在小说阅读器中沉浸阅读

★ 刘杰，解存福 中国市政工程华北设计研究总院有限公司

**摘要：**市政行业作为城市运行的核心基础设施领域，其工业信息化系统涵盖供水、排水、供热、燃气等关键环节，直接关系公共安全与民生保障。在国家信创战略全面推进的背景下，市政行业工业信息化正经历从核心技术到软硬件产品的国产化替代转型，虽然有效破解了国外技术垄断的“卡脖子”难题，但也面临着技术适配、安全防护、生态协同等新挑战。本文立足信创产业发展趋势，结合市政行业工业信息化的高可靠性、强实时性、广关联性等特性，系统剖析了国产化转型过程中的核心安全问题，并借鉴典型实践案例经验，提出了“技术—管理—生态”三位一体的安全防护体系，为市政行业在信创转型中实现安全与发展的动态平衡提供了理论支撑与实践参考。

**关键词：**信创；市政行业；工业信息化；国产化替代；安全防护体系；等级保护

**1　引言**

“信创”也被称为信息技术应用创新，是我国自主研发、自主可控的信息技术体系构建与应用推广过程，其核心目标是打破国外信息技术产品与服务的垄断格局，保障国家信息安全与产业自主发展。2016年，我国提出了信创“2+8+N”三步走战略。具体来说，“2”指的是首先实现党委、政府机关范围内的国产替代；“8”则是指金融、电信、电力、石油、交通、航空航天、教育、医疗等八大关键行业的国产替代，是推广重点；“N”则代表包括市政行业在内的其他行业，最终实现信创的全面普及。

市政行业作为城市基础设施的核心组成部分，其工业信息化系统的安全稳定直接关系国计民生。当前其正加速融入信创发展大局，因此在国产化替代过程中亟需构建适配行业特性的安全防护体系。

**2　相关政策背景**

信创产业发展已形成“国家统筹+地方深耕”的协同推进格局：国家层面以顶层设计明确战略方向、发展目标与实施路径；地方层面结合区域产业基础，通过财政补贴、场景开放、生态培育等举措推动政策落地。

国家政策聚焦自主可控、安全可靠，构建了“战略引领+专项推进+标准规范+市场驱动”体系。其核心要点如表1所示。

表1 安全类国家政策的核心要点

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kdBgUloeCuicZz15sG9HxLBvoItLOywyJc8rYl2TEUaOibalA3w06wsoibe0g6IS8lkW9m2o0oJXib051icm2tCqn5zg84fs5slCKoO5ILDUrWkI/640?wx_fmt=png&from=appmsg)

同时，网络强国、数字中国等国家战略部署持续推进，其中网络强国战略涵盖网络基础设施建设、信息通信业创新发展、网络信息安全保障三大核心维度，为市政行业信创转型与安全建设提供了根本遵循。

**3　信息系统技术架构**

信创背景下的信息系统技术架构以“自主可控、适配兼容、安全可靠”为核心设计原则，构建了从物理硬件到业务应用的全栈国产化体系。各层级既承担独立技术功能，又通过信创适配标准形成有机协同，共同支撑系统的稳定运行与安全防护。

目前，市政行业工业控制与信息系统已逐步建立起完善的国产信创生态产品体系，其核心软硬件产品如表2所示。

表2 国产信创生态核心软硬件产品

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kdBgUloeCu8lr4NZfnyGIvAv4Z1Mk3Kr33GiaTWuY2U6PJ4fPXic92VoNPic9VNjXdpicjlBkP7bicfEBYEcUPXmbXvFQAzz7eweXjqBO4m8Ixp4/640?wx_fmt=png&from=appmsg)

**4　工业控制与信息系统在市政行业的应用**

**4.1　工业控制系统应用场景**

工业控制系统在市政领域的给水、排水、燃气、供热、环卫等行业的厂、站有着广泛的应用。其具体应用场景如表3所示。厂、站控制系统架构图如图1所示。

表3 工业控制系统的具体应用场景

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kdBgUloeCuiczvViceVELjicAKRia8LNXpU0C1kStAN11QoR2W6o1eYyNCk0XVt5v9YWxDqHEibIicM0OBmtTzShXicYrxcDJSe7SE2kbz5Cr16iaro/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kdBgUloeCu9kbSQHrAEfMDVF5v8iaaSDKUI70xt1lP93YgIib2BTqyMWuJ9QWbLlfxiayqwuqnrQ75qkk1LOR9vLFwaThAnMGiadsCelib5lAJuM/640?wx_fmt=png&from=appmsg)

图1 厂、站控制系统架构图

**4.2　信息系统应用场景**

在智慧城市建设理念的引领下，市政行业信息化、数字化、智慧化转型加速推进，信息系统已从单一厂站控制延伸至城镇/区域级、公司/集团级的厂—站—网联合控制、调度与管理，实现了跨区域、跨层级的资源优化配置与协同运行。

**4.3　系统架构特征**

市政行业工业控制与信息系统架构呈现分布式协同特点，其典型架构包含工业数据中心、厂站中控室、现场控制单元三级架构（如图2所示）：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kdBgUloeCu9kLue6speKQd8jhicKraZOS2Yh1qq0XoEslD67KLQ3CRcsmWVocw3lnfvticfd4LVlbQOlibTH4K84KM4tYSvkOiaY84CZS3Envac/640?wx_fmt=png&from=appmsg)

图2 市政行业工业控制与信息系统架构示意图

核心层：通过1000Mbps核心交换机构建高速工业以太网，连接计算服务器、工业监管平台、操作终端等核心设备；

现场控制层：采用PLC控制器实现设备本地化控制，通过工业防火墙、工业审计等安全设备保障数据传输安全；

通信层：借助VPN网关、路由器等实现远程接入与跨区域通信。

**5　市政行业信息安全技术等级保护设计定级探讨**

**5.1　定级依据**

《中华人民共和国网络安全法》第三十一条：国家对公共通信和信息服务、能源、交通、水利、金融、公共服务、电子政务等重要行业和领域，以及其他一旦遭到破坏、丧失功能或者数据泄露，可能严重危害国家安全、国计民生、公共利益的关键信息基础设施，在网络安全等级保护制度的基础上，实行重点保护。关键信息基础设施的具体范围和安全保护办法由国务院制定。

近年来，工业领域信息安全事件频发，因此信息化系统应考虑适当的软硬件防护措施。信息系统安全防护要求可参照现行国家标准《信息安全技术网络安全等级保护基本要求，GB/T 22239》的有关规定执行。

网络安全等级保护定级需综合考虑受侵害客体及侵害程度，具体定级标准如表4所示。

表4 定级标准

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kdBgUloeCuicSwiaUJuD8UuMzd4icibHX79icDDibP3OOOBL290UbuNPahUr78jq9r8TvewHaDOuLoEfXhbUzbgNE6m39v8el4g1TbFvGU7jfhOhY/640?wx_fmt=png&from=appmsg)

**5.2　市政行业定级对应关系**

结合市政行业设施的重要程度、服务范围及影响规模，网络安全等级保护定级与市政行业设施安全等级对应关系如表5所示。

表5 网络安全等级保护定级与市政行业设施安全等级对应关系

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kdBgUloeCuibmbLWDqGzZibFHuGoCqQjNcia80UnmlkyHwPIiaJiau6pFgSX71OnpUHTNDzsHM8UrE8X3BHgzW6sXd37ysExwpVIib56GOfkRbLlE/640?wx_fmt=png&from=appmsg)

**6　信创背景下市政行业安全等保测评三级配置探讨**

针对市政行业等级保护三级对象，结合信创国产化替代要求，市政行业安全等保测评核心软硬件配置及信创相关指标如表6所示。

表6 市政行业安全等保测评核心软硬件配置及信创相关指标

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kdBgUloeCu9tPe0xZFNicqvHt7ia0DgCBZ0icEiakUDpopRicRibT4EYoMWtkd90vOdSpfOn34w3jJAxbPtnC8ibS66umtic37ulCb3hpqZCSGD6wQI/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kdBgUloeCu9okuXYMcZ5ibjnVyWZlQKqm9T7tWwPYzgNJ3xCGd5QM54QJu57D6rpPEnhtrzPNOVBfQlaLNHicoibtrTTG0YrzRn439OhuWMC0I/640?wx_fmt=png&from=appmsg)

**7　结论与展望**

信创背景下，市政行业工业信息化安全建设是技术自主可控、业务安全稳定与合规管理的有机统一，其核心在于实现国产化替代与安全防护的同步推进。当前，市政行业正面临着信创生态与业务场景融合不足、技术适配存在短板、安全管理体系有待完善等问题，通过构建“技术防护—管理保障—生态协同”三位一体的安全防护体系，坚持自主可控、合规适配、场景化防护原则，能够有效破解转型期的安全难题、实现安全与发展的动态平衡。

未来，信创产业技术成熟度与生态完整性的持续提升，将为市政行业工业信息化安全建设提供更有力的支撑。市政行业需牢牢把握信创战略机遇，持续优化安全防护体系：在技术层面深化国产化软硬件适配与安全技术创新，在管理层面健全安全管理制度与应急响应机制，在生态层面加强产业链协同与行业标准共建，推动工业信息化向“自主可控、安全高效、智能协同”的方向迈进，为城市安全稳定运行与民生保障提供坚实的信息化安全支撑。

参考文献略。

**作者简介**

**刘　杰**（1971-），男，山东莱州人，教授级高级工程师，学士，现就职于中国市政工程华北设计研究总院有限公司，主要从事市政工程电气、自控系统设计方面的研究。

**解存福**（1986-），男，河北邢台人，高级工程师，硕士，现就职于中国市政工程华北设计研究总院有限公司，主要从事市政工程电气、自控系统设计方面的研究。

**· end ·**

来源 | 《自动化博览》2026年第二期暨《工业控制系统信息安全专刊（第十二辑）》

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

![](https://mmbiz.qpic....