---
title: 警惕“NFC欺诈幽灵”：针对中国区用户的NFC中继攻击及恶意软件深度分析
url: https://mp.weixin.qq.com/s/KiLkjQNhFI_M-yugxO-jXw
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:26:44.539417
---

# 警惕“NFC欺诈幽灵”：针对中国区用户的NFC中继攻击及恶意软件深度分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VuRGkncX57NM7lfK0CxooU454InRFDxwR2gbuYGl2Taz6I6baHVibPdoUia1OZQAsDVmWltQoVyJhItYuZyXydlQ/0?wx_fmt=jpeg)

# 警惕“NFC欺诈幽灵”：针对中国区用户的NFC中继攻击及恶意软件深度分析

启明星辰
启明星辰

ADLab

![]()

在小说阅读器中沉浸阅读

更多安全资讯和分析文章请关注启明星辰ADLab微信公众号及官方网站（adlab.venustech.com.cn）

**第一章**

概述

2026年1月21日，启明星辰ADLab在威胁狩猎中捕获到一款针对中国用户定制的NFC中继攻击样本。通过溯源分析，我们发现该样本是一款基于臭名昭著的NFU Pay（恶意软件即服务MaaS）生态而定制的恶意代码，其攻击目标聚焦于中国境内用户群体。与传统银行木马依赖钓鱼页面窃取账户凭证或拦截短信验证码的攻击模式不同，NFC中继攻击利用了近场通信技术的物理特性，使攻击者能够即时获取被盗资金，有效绕过了银行转账延迟到账等传统风控措施。

该攻击样本通过"读取端"设备(受害者设备)近场窃取受害者银行卡APDU指令，经C2服务器实时路由至"接收端"设备；接收端利用HCE功能模拟银行卡与POS机交互，完成毫秒级双向中继。全程POS机无法察觉交易响应实际来自远程真实卡片，导致非接触式盗刷。为了便于后续威胁追踪和情报共享，我们将新发现的恶意软件命名为“NFC欺诈幽灵(NFC-Ghost)”。该恶意软件除了被黑客用于隐秘盗取受害者钱财外，还常被电信诈骗分子用于骗刷银行卡、信用卡等近场交易环节，并且还常常被用于国际间的洗钱活动。

“NFC欺诈幽灵”的开发目标具有明显针对性和目的性，比如其应用界面、提示信息、日志输出均采用简体中文；客户端模式标识从英文“POS\_terminal/Card\_reader”改为中文“接收端/发送端”；API路径使用品牌拼音缩写“/zj/”（中际）；样本品牌名称“中际”及版本标识“Card-2.0/Card-2.3”等都表明其开始了针对中国市场的侵入。

在深度溯源过程中，我们发现NFU Pay平台已衍生出多个定制品牌，除本次分析的“NFC欺诈幽灵”样本外，还包括PhantomCard、Lightning NFC等变种。当前NFC中继攻击领域已形成多个相互竞争的MaaS生态：SuperCard X是另一个由黑客运营的独立平台，其代码架构与NGate恶意软件存在相似性，两者均基于德国达姆施塔特工业大学发布的NFCGate开源项目演化而来。值得关注的是，SuperCard X同样被国内电信诈骗团伙用于实施盗刷、洗钱等非法活动。

“NFC欺诈幽灵”通过安卓系统的NFC HCE（Host Card Emulation，主机卡模拟）功能，实现银行卡APDU指令的实时中继转发。该恶意软件将发送端和接收端功能集成于同一应用中，攻击者在两台手机上安装同一应用后，通过登录界面分别选择“发送端”或“接收端”模式进行配合作业：发送端负责诱导受害者将银行卡贴近手机以读取NFC数据，接收端则在远程POS机或ATM机前模拟该银行卡完成支付或取现操作。整个攻击过程中，受害者的银行卡无需离开其视线范围，攻击行为具有极高的隐蔽性。

为深入了解该威胁的技术细节和攻击手法，启明星辰ADLab对捕获的样本进行了全面的逆向分析工作，涵盖追踪溯源和代码深度剖析等多个维度。本报告旨在为安全研究人员提供详尽的技术参考，同时为普通用户提升安全防范意识提供指导。后续章节将详细阐述我们的分析过程、技术发现以及相应的安全建议。

**第二章**

追踪溯源

在本次分析过程中，我们对捕获的恶意软件样本进行了全面的逆向分析和关联追踪。该恶意软件将发送端和接收端功能集成于同一应用中，用户通过登录界面选择运行模式，软件启动的主界面如图2-1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwODBtnMRqDxG37qoqhD8ibATzAAU5aibD3peL8ficU4G4LeNmccEIGUVPg/640?wx_fmt=png&from=appmsg)

图2-1 恶意软件登录界面及模式选择

在分析过程中，我们发现该恶意软件的后台管理系统仍处于活跃状态。后台登录界面采用中文设计，支持用户名密码、手机短信验证以及企业微信等多种登录方式，如图2-2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwFZCDpLWfXpUHJYU9PTykjTY33ciaQKOU5U5QmcT0ECuriao0m4QJGvIA/640?wx_fmt=png&from=appmsg)

图2-2 后台登录界面

通过审查网站源码，我们注意到页面描述显示为“bluewind-boot后台权限管理系统”。经GitHub检索确认，攻击者直接复用了开源项目bluewind-boot（https://github.com/llllllxy/bluewind-boot）作为后端框架，因此后台界面本身未能提供有效的攻击者溯源线索。

为进一步扩展样本集，我们以主Activity特征字符串“nfc.share.nfcshare.”作为关联查询条件，在多个样本库中进行检索，最终收集到该恶意软件家族的76个样本。通过对这些样本的证书签名信息、包名特征、应用名称等多个维度进行系统性分析，我们得以勾勒出该恶意软件家族的技术演进脉络和攻击者的运营特征。

2.1 样本证书与签名分析

数字证书是Android应用的重要身份标识，通过对收集到的76个样本进行证书信息提取和统计分析，我们发现该恶意软件家族在证书使用上呈现出明显的规律性特征，这些特征为追踪攻击者活动轨迹和评估威胁规模提供了重要依据。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwiaecHNJlfslLd3FXyqSD4EIGaVqht4stxpI60uJf4xLIGiaJuMHmMFOQ/640?wx_fmt=png&from=appmsg)

**图**2-3 签名证书时间线

证书签名时间能够反映样本的生成时间节点，是追踪恶意软件家族活动周期的重要指标。如图2-3所示，我们对76个样本的证书签名时间进行了统计分析，发现样本的时间分布呈现出明显的分层特征。

在早期样本方面，有8个样本使用了2008年签发的Android SDK默认调试证书，另有2个样本使用了2021年4月签发的证书。这些样本可能为早期开发测试版本，或是攻击者为追求快速分发而跳过正式签名流程的临时版本。

从正式运营时间来看，最早的正式样本签名时间可追溯至2024年11月，共有6个样本在该月被签名，这一时间节点与该家族在野外被首次发现的时间基本吻合。进入2025年后，样本签名活动呈现明显的增长态势：3月有5个样本、6月有3个样本、8月有11个样本。值得关注的是，2025年9月成为样本产出的绝对高峰期，单月签名样本数量达到22个，占总样本量的28.9%。随后的10月份仍保持较高活跃度，有12个样本被签名；11月和12月分别有5个和1个样本。进入2026年1月，我们又捕获到1个最新样本，表明该家族仍在持续活跃运营。

这一时间分布特征表明，该恶意软件家族背后的威胁行为者具备持续的开发和运营能力，且在2025年下半年明显加大了攻击投放力度——仅8月至10月三个月内就产出45个样本，占总量的59.2%。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxw324Y5FzMIR1f7STdCsiauicMeyJEtgcm4sqMUtOE5niaR9TLFaAV9OyFA/640?wx_fmt=png&from=appmsg)

图2-4 证书颁发者类型分布

除签名时间外，证书颁发者信息同样是追踪恶意软件家族的重要维度。如图2-4所示，我们对76个样本的证书颁发者信息进行了分类统计，识别出8种典型的证书使用模式。

“xinjiang”自签名证书是该家族使用最广泛的证书类型，共有37个样本采用，占总量的48.7%。这类证书的显著特征是在地理位置字段中统一使用“xinjiang”作为标识，证书主题中的国家（C）、省份（ST）、城市（L）字段均设置为“xinjiang”。更值得关注的是，其组织名称（O）和组织单位（OU）字段采用“两位随机字母+Unix时间戳”的命名格式，如“O=yf1755531900072”。通过对时间戳的解析，我们发现这些数值与样本实际签名时间高度吻合，强烈暗示攻击者使用了自动化工具批量生成签名证书。

简单数字证书是第二大类，共15个样本使用，占比19.7%。这类证书的特点是主题极为简化，通常仅包含一个简单数字作为CN字段值，如“CN=1”、“CN=8789789”等。这种配置通常出现在早期开发版本或需要快速分发的定制版本中，反映出攻击者在某些场景下优先考虑分发效率。

Android调试证书共8个样本使用，占比10.5%。这类样本使用Android SDK自带的默认调试证书，签名起始时间为2008年。在正常开发流程中，调试证书仅用于测试阶段，该家族中存在此类样本表明这些可能是开发测试版本，或攻击者为快速分发而跳过正式签名步骤。

其他自签名证书共5个样本，占比6.6%。这类证书格式各异，包括使用中文字符（如“CN=的撒娇好”）、地区标识（如“C=中国, ST=江苏”）或随机字符串等，反映了样本来源的分散性，可能涉及多个分发渠道或定制客户。

RC/852证书共4个样本，占比5.3%。这类证书在国家代码字段使用“852”（香港国际电话区号），可能是攻击者试图伪装成香港开发者。使用此类证书的样本主要是早期版本，签名时间集中在2025年3月。

“admin”自定义证书共4个样本，占比5.3%。这类证书所有字段均使用“admin”加随机字符串格式，与xinjiang证书类似显示出批量自动化生成特征，但采用不同命名模板。使用此类证书的样本签名时间集中在2025年11月至12月，可能代表攻击者后期采用的新签名策略。

“NFC/Dubai”证书共2个样本，占比2.6%。这类证书使用阿联酋（ARE）作为国家代码，迪拜作为城市标识，暗示可能是针对中东地区定制的版本。

伪造企业证书仅1个样本，占比1.3%。该样本使用“Innovation Hub”作为组织名称，混合使用新加坡和巴西的地理标识，意图通过正规企业名称提升可信度，规避安全检测。

综合来看，证书颁发者的多样性反映了该恶意软件家族的MaaS运营特点：核心开发团队使用自动化工具批量生成xinjiang系列证书用于主要分发，同时为不同地区的定制客户提供差异化的证书配置方案。

2.2 家族归属确认

通过对样本证书的统计分析，我们已初步勾勒出该恶意软件家族的运营规模和活动周期。然而，证书信息仅能反映样本的签名特征，要准确确认家族归属，还需要从代码层面寻找直接证据。为此，我们采用代码比对分析方法，将”NFC欺诈幽灵“与已确认归属于NFU Pay平台的样本进行对比，从代码结构、核心类实现、通信协议等多个维度验证其同源性。

### 2.2.1 参照样本选取

在收集到的76个样本中，我们注意到一个包名为“nfc.share.nfcshare”的样本，其包名与我们用于关联检索的主Activity特征字符串完全一致。该样本的应用名称为“NFU”，应用图标中同样包含NFU字样。通过对该样本的逆向分析，我们在其登录失败处理逻辑的Toast提示信息中发现了明确的归属证据——“遇到问题联系：@nfupay666”，如图2-5所示。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxw3ibZPjYHs5EGD1DFfYldhUB9YJnooaSZU75rzKabmeGzZnpIHtnXAAQ/640?wx_fmt=png&from=appmsg)

图2-5 NFU Pay的联系方式

@nfupay666是NFU Pay在Telegram平台的官方客服账号，如图2-6所示，这一发现直接证实该样本为NFU Pay平台官方分发的版本。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwqbicHmWQ4ojxx3LnsBe6oTkEVb9HhcoUZ9Fw8MRxStWDhOB1DL4ibIZw/640?wx_fmt=png&from=appmsg)

图2-6 NFU Pay的联系方式

因此我们选取该样本（MD5: 07a8dcccfc3c5496423923a0033dbe11）作为参照样本，与“NFC欺诈幽灵”样本进行代码比对。

### 2.2.2 代码对比分析

通过GDA反编译工具对两个样本进行代码目录结构对比分析，我们发现两者的核心代码均位于“nfc.share.nfcshare”包路径下，具有高度一致的模块化组织结构，如图2-7所示。

两个样本均包含相同的service和model子包结构。在service子包中，核心服务类EmulationService.java（NFC HCE卡模拟服务）和MqttService.java（WebSocket通信服务）的类名和包路径完全一致。在model子包中，数据模型类MqttChannel.java（通道类型枚举）、NfcInfo.java（NFC数据封装）、WSMessage.java（WebSocket消息格式）、CardInfo.java（卡片信息）同样保持一致。

两者的主要差异在于混淆程度不同。“NFC欺诈幽灵”经过了更强的代码混淆处理，部分辅助类被重命名为单字母类名（如a.java、b.java、c.java等），而参照样本（“NFU”）保留了原始的类名（如ApiService.java、NetworkUtils.java等）。但值得注意的是，两个样本的核心功能类命名均保持不变，这表明它们共享相同的代码基础框架。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwFx4lbPMIyRiap7fDib8jpoHasHdWkicMpTZzSIjRl6ibErxDwu1GJrE9Yg/640?wx_fmt=png&from=appmsg)

图2-7 样本代码目录结构

在代码结构一致的基础上，我们进一步对比了两个样本的核心功能实现代码。

EmulationService是NFC中继攻击的核心服务类，负责接收POS机的APDU指令并转发至C2服务器。如图2-8所示，两个样本的EmulationService实现逻辑完全一致：均继承自Android系统的HostApduService类。onDeactivated函数内的打印日志的TAG都相同，唯一的差异是分析样本对日志字符串进行了NPStringFog加密处理，而参照样本保留了明文日志。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwMouF0ms281QWTmuBECgVCKmOr7jBia4CUAR22A8qq3MNSG8QAGM3E7A/640?wx_fmt=png&from=appmsg)

图2-8 EmulationService核心代码对比

MqttChannel枚举类定义了WebSocket通信的通道类型。如图2-9所示，两个样本的MqttChannel定义完全相同，均包含FETCH\_CHANNEL、SEND\_CHANNEL、LOG\_CHANNEL、CARD\_INFO\_CHANNEL、CARD\_REMOVED、NOTIFICATION\_CHANNEL、ANSWER\_CHANNEL、OFFLINE\_CHANNEL共8种通道类型，枚举值的名称和顺序完全一致。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwFoNGDfziaiaPudb1hE4icc35wgMoSJiblmicmeor06wVhczwiaKhaVumfR5g/640?wx_fmt=png&from=appmsg)

图2-9 MqttChannel枚举定义对比

综合以上代码层面的直接证据，我们可以确认本次分析的**“NFC欺诈幽灵”属于**NFU Pay MaaS生态系统的定制产品。这种为不同客户定制独立品牌的做法符合MaaS平台的典型商业运营模式——核心开发团队提供基础恶意软件框架，下游客户可根据需求定制品牌名称、界面风格和目标地区。在我们收集的样本中，除“中际”外还发现了“NFU”、“T4”、“鲲鹏支付”、“云联”、“EQUIPE GHOST”等多个品牌名称，这些均为NFU Pay平台为不同客户定制的产品变种。

### 2.2.3 基础设施关联分析

除代码层面的同源性证据外，我们还通过C2基础设施的关联分析进一步验证了家族归属关系。

在“NFC欺诈幽灵”样本的逆向分析中，我们提取到其C2服务器域名www.zjshare.xyz。通过查询该域名的WHOIS注册信息，如图2-10所示，该域名注册时间为2025年11月27日。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxwgCnhRqjLVX4ltt2UAZhSGCaeXnvwVcfla9BEicvGGw26cC1Fj564RMQ/640?wx_fmt=png&from=appmsg)

图2-10 域名www.zjshare.xyz的WHOIS信息

对该域名进行DNS解析，得到其指向的服务器IP地址为185.106.176.32。值得注意的是，该IP地址在另一个“中际”样本（MD5: 45902fa3f8879a18c97b12fbb186e196）中以硬编码形式直接出现，该样本的证书签名时间为2025年12月1日，仅比域名注册时间晚4天。这一时间关联印证了前文证书签名时间溯源的准确性，同时表明攻击者在2025年11月底至12月初期间完成了C2基础设施的部署和样本的签名分发。

通过威胁情报平台对该IP地址进行关联查询，我们发现它还被其他NFU Pay家族变种所使用，其中包括品牌名为“鲲鹏NFC”的样本，如图2-11所示。

![](https://mmbiz.qpic.cn/mmbiz_png/VuRGkncX57NM7lfK0CxooU454InRFDxw...