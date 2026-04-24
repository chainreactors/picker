---
title: 自传播供应链蠕虫劫持 npm 包，窃取开发人员令牌
url: https://mp.weixin.qq.com/s/IYw-_dFMD1taxANPwLQqCA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:52:32.706221
---

# 自传播供应链蠕虫劫持 npm 包，窃取开发人员令牌

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# 自传播供应链蠕虫劫持 npm 包，窃取开发人员令牌

Bill Toulas
Bill Toulas

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)

编译：代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

**Socket****和 StepSecurity 公司的研究人员在 Namastex Labs 的多个软件包中发现，一起针对 npm 生态系统的新型供应链攻击正在窃取开发者凭证，并试图通过来自被入侵账户发布的软件包进行传播。Namastex Labs 是一家提供基于 AI 的智能解决方案以提高盈利能力的公司。**

研究人员提到，该攻击中使用的凭据窃取、数据外泄和自我传播技术与 TeamPCP 的 CanisterWorm 攻击相似，但现有证据无法得出确切的归因结论。

在本文发布时，Socket 列出了在该新型供应链攻击中已被入侵的 16 个 Namastex 软件包中的一组：

* @automagik/genie (4.260421.33–4.260421.39)
* pgserve (1.1.11–1.1.13)
* @fairwords/websocket (1.0.38–1.0.39)
* @fairwords/loopback-connector-es (1.4.3–1.4.4)
* @openwebconcept/theme-owc@1.0.3
* @openwebconcept/design-tokens@1.0.3

这些包用于 AI 代理工具和数据库操作，因此该攻击针对的是高价值终点，而非追求大规模感染。不过，由于该攻击具备类似蠕虫的功能，一旦条件满足，传播速度可能会迅速扩大。

研究人员发现，杯注入的恶意代码会收集与各种密钥相关的敏感数据如令牌、API 密钥、SSH 密钥、云服务凭证、CI/CD 系统、注册表、LLM 平台以及 Kubernetes/Docker 配置。此外，它还会尝试提取存储在 Chrome 和 Firefox 中的敏感数据，包括加密货币钱包（如 MetaMask、Exodus、Atomic Wallet 和 Phantom）。

SetpSecurity 公司的研究人员表示，该恶意软件“是一个供应链蠕虫”，能够找到可用于在 npm 上发布包的令牌，并将自身注入到该令牌有权发布的每个包中，从而进一步扩大入侵范围。研究人员提到，pgserve 的恶意版本首次发布于 4 月 21 日 22:14 UTC，同一天又发布了另外两个恶意版本。

如果发布令牌在受害系统中以环境变量或 ~/.npmrc 配置文件的形式存在，恶意脚本会识别受害者可发布的包，添加恶意负载，然后以递增的版本号将其重新发布到 npm。这些新受感染的包在安装时会执行同样的流程，从而实现递归传播。研究人员指出，如果发现 PyPI 凭据，该恶意软件会使用基于 .pth 文件的负载对 Python 包采用类似的方法，这使得该攻击成为一次多生态系统的攻击。

开发人员应将所有列出的包版本视为恶意版本，立即从系统和 CI/CD 管道中移除，然后更换所有可能已暴露的密钥。Socket 和 StepSecurity 公司均提供了入侵指标，帮助防御者识别受感染的开发环境或针对此次攻击进行防御。在发现受影响包的环境中，建议采取的措施包括：从开发和 CI/CD 系统中移除这些包，更换所有凭证和密钥数据，并检查内部包镜像、构件和缓存。Socket 还建议防御者审计是否存在具有相同的public.pem文件、相同的 webhook 主机或相同 postinstall 模式的相关包。

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[Axios 严重漏洞可导致 RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525768&idx=2&sn=b8967ced3022f4f88a311a652e635650&scene=21#wechat_redirect)

[Trivy供应链攻击触发CanisterWorm 在47个 npm 包中自传播](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525520&idx=2&sn=b3d4dddc586c4b0aa8cefb09c0344cb8&scene=21#wechat_redirect)

[热门包管理器中存在多个漏洞，JavaScript 生态系统易受供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524984&idx=1&sn=19aef4ce8e288278782458e430a710d8&scene=21#wechat_redirect)

[开源自托管平台 Coolify 修复11个严重漏洞，可导致服务器遭完全攻陷](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524828&idx=2&sn=21af241f60f1452013815133745e9a72&scene=21#wechat_redirect)

[得不到就毁掉：第二轮Sha1-Hulud供应链攻击已发起，影响2.5万+仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524487&idx=1&sn=f170d3131122071dec6e419c6cff562c&scene=21#wechat_redirect)

[vLLM 高危漏洞可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524481&idx=3&sn=6d0b161f8add2f6c1ee65e60ef6955d8&scene=21#wechat_redirect)

[开源AI框架 Ray 的0day已用于攻陷服务器和劫持资源](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519162&idx=1&sn=3872fcc82018e2c561d9e4e7574f0c8e&scene=21#wechat_redirect)

[热门 React Native NPM 包中存在严重漏洞，开发人员易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524330&idx=2&sn=bc54e02a8f815ed78b67d3135a9f9607&scene=21#wechat_redirect)

[10个npm包被指窃取 Windows、macOS 和 Linux 系统上的开发者凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524314&idx=2&sn=81cae6998a39f2153ed18d7cc065303b&scene=21#wechat_redirect)

[热门 React Native NPM 包中存在严重漏洞，开发人员易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524330&idx=2&sn=bc54e02a8f815ed78b67d3135a9f9607&scene=21#wechat_redirect)

[热门NPM库 “coa” 和“rc” 接连遭劫持，影响全球的 React 管道](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508946&idx=1&sn=273c58d08a4225306a567cf6a150f40c&scene=21#wechat_redirect)

[开发人员注意：VSCode 应用市场易被滥用于托管恶意扩展](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515219&idx=1&sn=faa32338df1d68e7cd738a80222f3a44&scene=21#wechat_redirect)

[GitHub Copilot 严重漏洞可导致私有仓库源代码被盗](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524163&idx=1&sn=d70a7c55e27a3e179522330a9ce62b0b&scene=21#wechat_redirect)

[受 Salesforce 供应链攻击影响，全球汽车巨头 Stellantis 数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524053&idx=1&sn=2b843932ebd4eeeb17b6935b08be82f8&scene=21#wechat_redirect)

[捷豹路虎数据遭泄露生产仍未恢复，幕后黑手或与 Salesforce-Salesloft 供应链攻击有关](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523990&idx=1&sn=ad9957a5c3d054d4a0bf32250bceb556&scene=21#wechat_redirect)

[十几家安全大厂信息遭泄露，谁是 Salesforce-Salesloft 供应链攻击的下一个受害者？](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523972&idx=1&sn=7b06c31940ea7576d0236d9310886b39&scene=21#wechat_redirect)

[第三方集成应用 Drift OAuth 令牌被用于攻陷 Salesforce 实例，全球700+家企业受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523952&idx=1&sn=2bc84253019e6c2525bcf928eaed696c&scene=21#wechat_redirect)

[黑客发动史上规模最大的 NPM 供应链攻击，影响全球10%的云环境](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523990&idx=2&sn=6e38e1ee8cd69f1375a5be218c02ff97&scene=21#wechat_redirect)

[十几家安全大厂信息遭泄露，谁是 Salesforce-Salesloft 供应链攻击的下一个受害者？](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523972&idx=1&sn=7b06c31940ea7576d0236d9310886b39&scene=21#wechat_redirect)

[第三方集成应用 Drift OAuth 令牌被用于攻陷 Salesforce 实例，全球700+家企业受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523952&idx=1&sn=2bc84253019e6c2525bcf928eaed696c&scene=21#wechat_redirect)

[AI供应链易遭“模型命名空间复用”攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523962&idx=1&sn=2d9b8ca044c242a6ae1f72df93d7acb0&scene=21#wechat_redirect)

[Frostbyte10：威胁全球供应链的10个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523957&idx=2&sn=288b0d14a657b13c7f1a6b14705a44e8&scene=21#wechat_redirect)

[PyPI拦截1800个过期域名邮件，防御供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523850&idx=2&sn=72dc01d9984a720959b312dd0e7cf05e&scene=21#wechat_redirect)

[PyPI恶意包利用依赖引入恶意行为，发动软件供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523844&idx=2&sn=08c8962eead61fe76467a9196b3da3e5&scene=21#wechat_redirect)

[黑客利用虚假 PyPI 站点钓鱼攻击Python 开发人员](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523700&idx=2&sn=463d300bdfd3de129cd5d258ceb67cf4&scene=21#wechat_redirect)

[700多个恶意误植域名库盯上RubyGems 仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492823&idx=2&sn=9c226ff328303e78331451ac5219df07&scene=21#wechat_redirect)

[NPM “意外” 删除 Stylus 合法包 全球流水线和构建被迫中断](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523648&idx=1&sn=d9237c45bf78637d1cdd3bedd1d873e6&scene=21#wechat_redirect)

[固件开发和更新缺陷导致漏洞多年难修，供应链安全深受其害](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523615&idx=1&sn=1df256011200be03dc2afc80016c587e&scene=21#wechat_redirect)

[NPM仓库被植入67个恶意包传播恶意软件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523592&idx=2&sn=5087c0aa841caf3f0def9a1ca6c5ad27&scene=21#wechat_redirect)

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[NPM软件供应链攻击传播恶意软件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523234&idx=2&sn=ac4e0656fd04218349d356761af176dd&scene=21#wechat_redirect)

[隐秘的 npm 供应链攻击：误植域名导致RCE和数据破坏](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523167&idx=2&sn=4249c8e9e0dace01810c665eda52c421&scene=21#wechat_redirect)

[NPM恶意包利用Unicode 隐写术躲避检测](https:/...