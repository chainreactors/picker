---
title: 在看 | 周报：物业公司因个人信息保护履职不到位被行政处罚；工信部通报Claude Code存在安全后门隐患
url: https://mp.weixin.qq.com/s/9vOaMrajCWN_EfAbXu3YOg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:57.435773
---

# 在看 | 周报：物业公司因个人信息保护履职不到位被行政处罚；工信部通报Claude Code存在安全后门隐患

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38nTRvKLpoqoXqeVic62ibaIJvtgiankmicl8nIYognnwqRFj8RPC3e7XouV01BHHd2k9ppdWcbEqlrUw/0?wx_fmt=jpeg)

# 在看 | 周报：物业公司因个人信息保护履职不到位被行政处罚；工信部通报Claude Code存在安全后门隐患

原创

管窥蠡测
管窥蠡测

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT39x3nndZanlbZOk0K8ibhGOS3mskN8Bwx0bJ9KgpRsYSJ106ib1991xicajm3DeAcXdpEVl2icku02jBg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**[导读]**

本期周报覆盖数据安全及个人信息保护、AI安全、网络安全三大板块。数据安全层面包含违规App通报、物业信息保护失职处罚、多起企业数据泄露与勒索事件；AI安全层面涉及Claude Code安全隐患、多类新型AI攻击手段及全球首例端到端AI勒索攻击等动态；网络安全层面收录多款系统与商用软件高危漏洞、黑产刷量等风险事件，集中呈现行业风险态势与监管动向。

**数据安全及个人信息保护**

[1、国家计算机病毒应急处理中心通报72款违规App](https://mp.weixin.qq.com/s?__biz=MzU1MTE1MjU5Nw==&mid=2247485891&idx=1&sn=c042e9f5d2ba01c0a150bc07729a2340&scene=21#wechat_redirect)

国家计算机病毒应急处理中心经检测发现，72款移动应用存在违法违规收集使用个人信息的情况。这些问题涵盖多个方面：部分App首次运行时未以明显方式提示用户阅读隐私政策，或以默认同意等非明示方式征求用户同意；不少应用的隐私政策未逐一列出收集使用个人信息的目的、方式和范围；一些App向第三方提供个人信息时未告知用户且未取得单独同意；另有应用在未征得用户同意时便开始收集个人信息。

[2、物业公司因个人信息保护履职不到位被行政处罚](https://mp.weixin.qq.com/s?__biz=MzIyNjUxOTQ0MQ==&mid=2247586026&idx=1&sn=f70d14f6afd71f2267fdb8ee6b5b3707&scene=21#wechat_redirect)

重庆市南川区网信办对辖区一家物业管理公司依法作出行政处罚。该公司运营的停车场扫码缴费系统设置诱导性入口，要求用户提供非必要敏感个人信息，相关协议默认勾选，且未以显著方式告知信息收集的目的与范围。该公司委托第三方开发运营系统，却未建立个人信息保护内部制度，日常监管缺失。网信部门责令其限期整改并给予警告，要求删除违规收集的信息，将缴费码整改为纯净模式，并完善内部管理制度。

[3、GitLost攻击可借公开GitHub Issue诱导AI泄露私有仓库数据](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342223&idx=1&sn=81701698d2244e88fb746d9f92c1b9c5&scene=21#wechat_redirect)

Noma Security发现名为GitLost的攻击手段，该攻击针对GitHub Agentic Workflows功能，依托间接提示注入实现破坏。攻击者仅需在公开仓库创建普通外观的issue，就能诱导拥有跨仓库读取权限的AI Agent，把私有仓库信息输出到公开评论区，只需添加特定词汇即可绕过平台自带防护。该攻击满足AI数据泄露的致命三要素，且属于架构层面缺陷，无法依靠补丁完成修复。

[4、埃森哲35GB内部机密数据遭窃取并在黑产论坛售卖](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516244&idx=1&sn=7d6c39a33e787ae14b5757237538b5a7&scene=21#wechat_redirect)

一名威胁攻击者宣称窃取埃森哲超35GB内部数据，并于地下犯罪论坛公开兜售，被盗资料涵盖源代码、各类加密密钥与云平台访问凭证，攻击者还放出克隆企业代码仓库的截图佐证说辞。埃森哲已证实本次安全事件并封堵入侵源头，但未核实泄露数据范围与客户受影响情况，这类泄露信息可被黑客挖掘漏洞用于后续攻击，该攻击者此前也曾倒卖过埃森哲相关数据。

[5、希腊电网电表遭大规模非法篡改，电力盗窃损失超七千万元](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516222&idx=1&sn=1ba8470675ce0f6fe343f0b9a3bec2f0&scene=21#wechat_redirect)

希腊唯一电网运营商HEDNO旗下的模拟电表与数字电表遭犯罪组织大规模篡改，被用于实施电力盗窃，目前已确认六百多起非法篡改案件，预计造成的经济损失超七千万元人民币。该组织对模拟电表采用物理干涉手段压低用电读数，对数字电表则植入非法固件篡改上报数据，还具备远程监控供电数据的能力，以订阅制模式持续非法获利。目前已有五名涉案核心成员被捕，另有百余名个人及法人被立案调查。

[6、Google Dialogflow CX高危漏洞可被利用劫持AI对话窃取数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077769&idx=1&sn=2447f8dbc1a865899ccce5be2120c0a3&scene=21#wechat_redirect)

安全企业Varonis披露Google Cloud旗下企业级对话AI平台Dialogflow CX存在名为Rogue Agent的漏洞，该平台依靠共享Cloud Run环境运行自定义代码模块。攻击者凭借不当权限篡改核心执行文件，注入恶意Python代码，便能掌控同项目全部AI代理，查看对话、操纵会话并窃取隐私，还能搭建对外通信通道绕过数据边界管控，攻击行为不会留存日志难以察觉，相关漏洞已分阶段完成修复部署。

[7、皇家山大学遭遇网络勒索攻击，大量师生数据失窃损毁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077769&idx=3&sn=9d723a7a65246a803e37792374f382ab&scene=21#wechat_redirect)

加拿大皇家山大学遭到黑客入侵，校内多套线上与内部系统陷入瘫痪，黑客盗取存放师生信息的H盘数据并清除原件，还完整删除存有部门资料的J盘数据，J盘数据暂未发现外泄痕迹且难以完整恢复。勒索组织CMD Organization认领此次攻击，放出被盗敏感文件样本并索要比特币赎金，还计划公开拍卖数据，校方已上报监管与执法机构，同时为相关人员提供信用监控保护服务。

[8、PamStealer恶意软件伪装macOS剪贴板工具窃取用户数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077722&idx=1&sn=bdaa7e14cde52df5111a1a50052adb7b&scene=21#wechat_redirect)

一款名为PamStealer的恶意软件正面向macOS设备传播，它外观和热门剪贴板管理工具Maccy高度相似，具备多重数据窃取能力。该恶意程序会盗取浏览器存储的各类密码，读取剪贴板留存的验证码、银行卡号、API密钥等隐私信息，再将收集到的全部用户数据传输至黑客的远程服务器。日常复制粘贴各类敏感信息的操作，会让剪贴板成为极易被恶意程序利用的泄露渠道。

**AI安全**

[1、工信部：Claude Code存在安全后门隐患](https://mp.weixin.qq.com/s?__biz=MzIyNjUxOTQ0MQ==&mid=2247585999&idx=1&sn=da558a91e431fbc32d25f02962ea5367&scene=21#wechat_redirect)

工业和信息化部网络安全威胁和漏洞信息共享平台监测发现，AI编程工具Claude Code存在安全后门隐患且危害严重。该工具由美国Anthropic公司开发，可根据文字需求自主完成代码编写与修复工作。由于其内置了监控机制，未经用户同意便向远程服务器回传用户地域、身份标识等敏感信息，受影响的版本为2.1.91至2.1.196。对此，建议相关单位立即开展排查，对安装上述版本的开发终端进行卸载或升级，同时加强核心业务网段内开发工具外联权限管控与流量监测。

[2、黑客滥用OpenAI组织邀请功能实施数据窃取攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077722&idx=2&sn=33b61b01688826fdeecceb7fbd165d52&scene=21#wechat_redirect)

安全研究人员发现黑客会借助OpenAI的组织邀请功能开展名为“投毒租户”的新型攻击，攻击者先自行搭建OpenAI组织，再向目标用户发送加入邀请。只要用户同意邀请，攻击者便可查看该用户存于组织中的提示词与API调用记录，用户和AI对话的全部内容、接口调用信息都会被对方获取，不少企业与开发者常会向AI输入代码、业务资料等商业机密，这类信息一旦泄露会造成严重损失。

[3、黑客利用SEO投毒与隐藏HTML代码诱骗AI Agent执行恶意指令](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341890&idx=2&sn=a71f7a2617cfed3b32697a6b8d3aee53&scene=21#wechat_redirect)

攻击者借助SEO投毒和隐藏HTML代码的手段，对AI Agent发起间接提示注入攻击。恶意指令被嵌入网页代码，人类用户无法察觉，但扫描页面的AI Agent会将其识别为合法指令。现已发现两起相关攻击活动，一起伪装成Python库文档页面，诱导AI Agent向攻击者账户完成支付；另一起仿冒加密货币平台，诱使AI将其判定为官方认证站点。测试显示部分主流AI模型易受此类攻击欺骗，安全机构建议相关组织部署多层安全管控来检测这类注入风险。

[4、全球首例端到端AI驱动勒索攻击JADEPUFFER曝光](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341828&idx=1&sn=9462121d0d04233a4048cbac30e3b423&scene=21#wechat_redirect)

Sysdig团队监测到全球首例由大语言模型全程自主驱动的JADEPUFFER勒索攻击，全程无需人工干预。攻击者利用Langflow认证缺失漏洞入侵，窃取各类API密钥、云凭证与数据库信息，借助MinIO对象存储完成横向移动，还可自主诊断并修正攻击代码。最终攻击锁定生产服务器，攻破Nacos配置服务后加密千余条配置数据，删除数据库表并留下勒索信息。该攻击颠覆了勒索软件依赖高阶技术人员的传统认知。

[5、AI双Agent攻击可借助Claude桌面版实现远程代码执行](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342284&idx=3&sn=5296e57b8214ad7b324f933d325665d6&scene=21#wechat_redirect)

Pentera实验室研究人员发现新型攻击手段，攻击者先借助认证漏洞获取受害者邮箱权限，再横向侵入其Claude账户，向可跨设备同步的个人偏好字段注入编码恶意提示词。用户启动软件后，程序会静默执行恶意指令，依托本地扩展完成远程代码执行，缺少对应扩展时还会诱导用户安装工具。另有多家机构披露Claude桌面扩展、连接器存在高危漏洞，厂商却认定该攻击利用的功能为产品原生设计。

[6、中学生借助ChatGPT编写工具攻击动漫平台致其长期关停](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516236&idx=1&sn=d311be2c282f45241900bc5b61d9ff2b&scene=21#wechat_redirect)

日本一名初中生凭借编程基础，在监测平台流量时找到万代频道系统漏洞，同时借助ChatGPT生成恶意工具，批量取消近四万七千个用户会员订阅。平台察觉异常后封锁其访问，嫌疑人便多次更换IP持续发起攻击，平台只能紧急关停服务长达六周，还存在上百万条用户个人信息泄露风险，该少年最终因妨害业务、非法访问计算机被警方逮捕。

[7、孤狼黑客借助AI三天攻破跨国企业AWS云环境实施勒索](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516248&idx=1&sn=f593ae42b73f230b52441d760fdf1742&scene=21#wechat_redirect)

安全公司Sygnia的研究披露，一名以牟利为目的的独立威胁行为者，借助AI智能体工作流加速侦察、攻击工具开发与目标环境动态适配，仅用72小时就攻破某全球性企业的复杂AWS云环境并实施勒索。攻击者先从面向互联网开放的应用中获取AWS访问密钥，再通过多条工作流串联云环境多处薄弱环节，完成凭据窃取、后门部署与业务服务干扰等一系列操作，以此向受害者施压索要赎金。

**网络安全**

[1、必应搜索“收款码”下拉联想词遭黑灰产批量刷量](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077739&idx=1&sn=1ba5203e265cf9584e7ff221c4c889e0&scene=21#wechat_redirect)

有网友反映在必应搜索“收款码”时，搜索框下拉联想词出现大量几乎相同的平台广告词，因而怀疑自身电脑中毒或浏览器被劫持。经实测验证，该现象并非用户端问题，而是必应搜索的联想词遭到黑灰产平台批量刷量，即便更换其他浏览器访问必应也能复现相同情况。刷搜索下拉关键词是搜索行业长期存在的顽疾，近年必应依托系统预装实现市场份额大幅增长，随之成为黑灰产盯上的新目标。

[2、Linux内核Bad Epoll高危本地权限提升漏洞曝光](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077708&idx=3&sn=864b0445b461bd238e8f78e65a4e38ec&scene=21#wechat_redirect)

Linux内核epoll子系统被发现名为Bad Epoll的本地权限提升漏洞，编号为CVE-2026-46242，CVSS评分7.8分。该漏洞根因是epoll实现中的竞态条件引发释放后重用问题，攻击者可借此将普通用户进程提升为root权限。漏洞影响内核6.4及以上版本的Linux发行版与部分Android设备，因epoll无法禁用暂无简易缓解方案，目前补丁已合入内核主线，各发行版需完成回溯移植。同期还披露了更高危的DirtyClone提权漏洞，二者叠加可被快速利用完成提权。

[3、微软SharePoint高危远程代码执行漏洞正遭积极利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077654&idx=2&sn=1ab239e93225350d7a4fd85eaf6f1aa2&scene=21#wechat_redirect)

编号为CVE-2026-45659的微软SharePoint高危远程代码执行漏洞正被攻击者积极利用，该漏洞CVSS评分达8.8分，无需管理员权限，任何拥有最低“站点成员”权限的用户都可触发，攻击者可借此远程执行任意代码并直接接管目标服务器。微软最初曾评估该漏洞“不太可能被利用”，但事实证明这一判断出现失误。相关安全机构已要求相关主体限期修复，用户可通过安装官方安全更新、审计账户权限等方式开展防护。

[4、FortiBleed凭证窃取活动证实与INC及Lynx勒索软件相关](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077654&idx=3&sn=1364c56512bff2a13e2fe37aa40b0f27&scene=21#wechat_redirect)

大规模FortiBleed凭证窃取活动已被证实与INC和Lynx勒索软件组织存在关联，攻击者借助自定义数据包嗅探工具，从受感染的FortiGate防火墙中拦截VPN凭证与各类认证数据，窃取的信息将为后续网络入侵提供支撑。研究人员通过攻击基础设施服务器确认，该活动运营者可直接访问勒索软件的谈判管理面板，且受害者信息与勒索软件泄露站点名单存在重叠。该行动实际规模远超最初预估，攻击者还疑似利用未公开的Nextcloud零日漏洞扩大权限，并在失陷设备留存后门账户。

[5、Linux内核Bad Epoll漏洞可实现本地提权并影响Android设备](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341828&idx=2&sn=44a94d63bf1fb8dc5ff30864104ee0b4&scene=21#wechat_redirect)

Linux内核epoll子系统曝出Bad Epoll漏洞，编号CVE-2026-46242，属于释放后重用类型的竞态条件漏洞。攻击者可构造时序扩大攻击窗口，将普通用户权限提升至root，测试中提权成功率接近99%。该漏洞可从Chrome渲染器沙箱内部触发，影响内核6.4及以上版本的Linux设备与部分Android机型。它与AI模型Mythos发现的另一epoll漏洞同源，由研究人员Jaeyoung Chung发现，目前官方补丁已发布，暂未出现实际野外利用案例。

[6、首个一键式Android 17漏洞利用链可实现设备完全控制](https://...