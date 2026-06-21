---
title: 黑客滥用 NinjaOne RMM 代理远程访问巴西组织
url: https://mp.weixin.qq.com/s/VTWt5DGrQNZpE0S69tDIbg
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:49:30.388735
---

# 黑客滥用 NinjaOne RMM 代理远程访问巴西组织

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb0xReKZN1l0F7U5rFLl07StVhyVcHKvkhVRfjNxJn7VXUDOS3tCOPSvkmefBRx0hvCjKC1mtXwdsp9xBf6p3vjxK9tXWw7msIQ/0?wx_fmt=jpeg)

# 黑客滥用 NinjaOne RMM 代理远程访问巴西组织

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一场活跃的网络钓鱼活动，利用合法的 NinjaOne 远程监控和管理 (RMM) 代理程序来获取对巴西组织的持久远程访问权限。

攻击者并没有依赖定制的恶意软件，而是利用熟悉的业务流程和葡萄牙语社交工程，诱骗财务、采购、会计和行政人员安装一个经过数字签名的 NinjaOne 代理，该代理会连接到攻击者控制的基础设施。

这种对主流远程监控工具的滥用行为未被记录在案，凸显了一个令人担忧的趋势：对手越来越多地利用受信任的企业工具来最大限度地减少检测并最大限度地提高行动自由。

该活动以精心设计的钓鱼邮件开始，这些邮件通过 Googleusercontent 重定向链将受害者引导至葡萄牙语着陆页。

这些门户网站模仿巴西可识别的流程，例如与 SEFAZ 相关的财政文件、模仿 Reclame Aqui 风格的投诉管理网站以及使用“Documento Fiscal”、“Download Seguro”和“Verificação de Segurança”等本地化语言的安全文件递送服务，以建立信任。

Cato CTRL 的研究人员最近发现了一起未记录在案的、活跃的网络钓鱼活动，该活动以伪造的商业文件为诱饵，针对巴西的组织。

在模拟验证流程之后，受害者点击下载按钮，该按钮不会返回文档，而是提供一个合法的 NinjaOne 安装程序，该安装程序配置为向攻击者控制的管理端点注册。

文件名通过嵌入财政文件标识符和网站上下文来加强欺骗，例如：NinjaOne-Agent-DocumentoFiscal21782856920262001238-Sede-Auto-x86-64。

网络钓鱼基础设施中的技术控制措施展现了操作人员明显的成熟度。他们采用地理围栏技术限制有效载荷的发送范围，使其仅限于巴西的IP地址段；利用浏览器指纹识别技术检测自动化框架和沙箱（例如Selenium、Puppeteer、Playwright、WebDriver、PhantomJS等）；并通过行为检查（例如鼠标移动、滚动和触摸事件）来验证攻击者是否为真人。

JavaScript 中的蜜罐字段和开发者注释揭示了蓄意的反分析意图；一条葡萄牙语注释翻译过来是“机器人填满了蜜罐”。

Cloudflare 的前端服务进一步隐藏了后端主机，而简单的下载机制（?download=1）表明，社交工程攻击比复杂的有效载荷交付逻辑更为重要。这些保护措施降低了研究人员的风险，并延长了基础设施的使用寿命。

滥用 NinjaOne 平台会造成特别严重的后果，因为该平台的合法管理功能与攻击者的目标直接对应。

作为企业级远程监控管理 (RMM) 工具，NinjaOne 支持端点监控、远程 shell 访问、文件传输、软件部署、补丁和自动化功能。当这些功能被攻击者控制时，便可在受害者网络内部提供侦察、持久远程访问、工具部署和横向移动的机会。

该活动与 CISA、NSA 和 MS-ISAC 发布的更广泛的警告相一致，这些警告旨在防范恶意 RMM 滥用。

Cato CTRL 的分析重点关注了化学品和先进材料行业的受害者，但这种诱骗模板广泛适用于处理财务文件和供应商沟通的各个行业。

通过操作工件（尤其是重复使用的地球主题壁纸）发现的基础设施转移扩大了对相关领域的可见性，这表明微不足道的重复使用资产可以揭示攻击者生态系统的大部分内容。

调查人员还发现，这与之前在巴西与 Venon RAT 活动相关的基础设施存在重叠，但归因仍是初步的，需要更多证据。

截至报告发布之时（2026年6月3日），尽管已采取负责任的披露措施，但部分钓鱼基础设施仍然可以访问。各组织应警惕任何意外的文档下载提示，直接核实分发渠道，并对远程监控管理 (RMM) 安装实施严格的终端控制和白名单机制。

### 相关IOC

r64[.]org

hairdb[.]com

lazybearpottery[.]net

rectalmania[.]com

sefaz[.]services

reclameaqui[.]services

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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