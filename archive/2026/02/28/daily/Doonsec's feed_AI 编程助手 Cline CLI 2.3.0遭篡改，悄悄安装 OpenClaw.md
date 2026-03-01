---
title: AI 编程助手 Cline CLI 2.3.0遭篡改，悄悄安装 OpenClaw
url: https://mp.weixin.qq.com/s/1nG1XHCWN7GOIFfEuj1eKw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:17:17.557803
---

# AI 编程助手 Cline CLI 2.3.0遭篡改，悄悄安装 OpenClaw

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# AI 编程助手 Cline CLI 2.3.0遭篡改，悄悄安装 OpenClaw

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

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

**开源AI编程助手Cline CLI遭篡改，被用于静默安装近期极受欢迎的自托管自主AI代理OpenClaw。**

Cline软件包维护人员发布公告称："太平洋时间2026年2月17日凌晨3点26分，未经授权方利用被盗的npm发布令牌，在NPM注册表上发布了Cline CLI的更新版本：cline@2.3.0。该发布包包含一个被修改的package.json文件，其中新增了postinstall脚本：'postinstall": "npm install -g openclaw@latest'。"开发者安装Cline 2.3.0版本时，此脚本会导致OpenClaw被安装到其机器上。Cline表示，软件包未引入其它修改，也未观察到恶意行为，不过明确指出安装OpenClaw既未授权也非预期行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWVVr0Bm7Jugj8t3nDic7AGnbtKahibJgYyMUfLXZLm6hzOEbYvmvtWpN1Zf7rwKq6LZDsLzR9nW7Z5RzvPpia3BRglmmvCGldGXU/640?wx_fmt=gif&from=appmsg)

**已发布新版本**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfU3sGNr2vLic0ZAP8icEGEbvZ5xTgPPhyTpkHobkrEicxuTB28p2tRM3FLjV58QRdmzCWSk0O2wicPw5UNB8dmV40sZFCGFp2BibepU/640?wx_fmt=gif&from=appmsg)

此次供应链攻击影响了在太平洋时间2月17日凌晨3点26分至上午11点30分约8小时窗口期内，安装npm上发布的Cline CLI软件包2.3.0版本的所有用户。该事件不影响Cline的Visual Studio Code扩展和JetBrains插件。

为消除未经授权发布的影响，Cline维护人员已发布2.4.0版本。2.3.0版本已被弃用，被盗用的令牌也已撤销。Cline同时表示，npm发布机制已更新，现通过GitHub Actions支持OpenID Connect。

微软威胁情报团队在X平台上发文称，在2026年2月17日，观察到由Cline CLI软件包供应链遭入侵导致OpenClaw的安装量出现了"虽小但值得注意的增长"。StepSecurity的数据显示，被入侵的Cline软件包在这八小时内被下载了约4000次。建议用户更新至最新版本，检查自己的环境是否有任何意外安装的OpenClaw，并在不需要时将其移除。

Endor Labs研究员Henrik Plate表示："尽管下载量很高，但总体影响较低：OpenClaw本身并非恶意软件，且该安装过程并不包含Gateway守护进程的安装或启动。然而，这一事件表明软件包维护者不仅需要启用可信发布，还需要通过传统令牌禁用发布——并且软件包用户需要关注相应证明的存在（或突然缺失）。"

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWjq6GA9SOQYYzZZaWJEGicQKQSLxb9m5Q8NssiaraYNOenJSwWbbXT32Y7O8g33LIDgNhafeZicQfapQCd7Zdx1DjWicFd345Bib3E/640?wx_fmt=gif&from=appmsg)

**利用Clinejection窃取发布密钥**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWYL5cxUeNbicQpZGqZvPVWgjZ4ibescbo0hpukP3Oy3cZTzylrU1gdGIibD5N2UkIwYaZoDsLwlicsWX5iaVKibO9iaocBxThtJRsLJI/640?wx_fmt=gif&from=appmsg)

虽然目前尚不清楚谁在背后操纵了这次npm包入侵事件及其最终目的，但在此之前，安全研究员Adnan Khan发现，攻击者可以通过提示注入窃取仓库的身份验证令牌。攻击者利用的是该仓库被配置为自动分类处理GitHub上提出的任何新议题这一情况。

Khan解释说："当新议题被创建时，工作流会启动Claude，并赋予其访问仓库的权限和一套工具来分析和回应这个议题。其意图是自动化初步响应，以减少维护人员的负担。"

但工作流中的一个错误配置授予了Claude过高的权限，使其能够在默认分支内实现任意代码执行。再加上嵌入在GitHub议题标题中的提示注入，可被拥有GitHub账户的攻击者用于诱骗AI代理运行任意命令，进而破坏生产环境的发布版本。

这一基于PromptPwnd技术构建的漏洞被命名为Clinejection。它是在2025年12月21日的一次源代码提交中被引入的。攻击链概述如下：

* 在议题分类工作流中提示Claude运行任意代码。
* 通过向缓存填充超过10GB的垃圾数据来驱逐合法的缓存条目，从而触发GitHub的最近使用最少的（LRU）缓存驱逐策略。
* 设置与夜间发布工作流缓存键相匹配的污染缓存条目。
* 等待大约在协调世界时凌晨2点运行的夜间发布任务触发，并使用被污染的缓存条目。

Khan 指出，"这将使攻击者能够在夜间工作流中获得代码执行权限，并窃取发布密钥。如果威胁行为者获取了生产环境的发布令牌，结果将是一场毁灭性的供应链攻击。通过被盗用的发布凭据推送的恶意更新，将在每个已安装该扩展并将其设置为自动更新的开发者的上下文中执行。"换句话说，该攻击序列利用GitHub Actions缓存投毒，从议题分类工作流横向移动到高权限工作流，例如"发布夜间版"和"发布NPM夜间版"工作流，并窃取夜间发布，这些凭据拥有与生产环境发布所用凭据相同的访问权限。事实证明，这正是所发生的情况——身份不明的威胁行为者利用一个活跃的npm发布令牌（称为NPM\_RELEASE\_TOKEN或NPM\_TOKEN）来验证Node.js注册表并发布Cline 2.3.0版本。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXEaThwwQYwkdhlBOpUPj7OUHaEMKLHxnibAg5vhwcq5kBYWGNkMl04iccibjmnzPb3Up5uYYMsibkf8ibR9djnPFicWYUMw5HUImic4s/640?wx_fmt=gif&from=appmsg)

**AI供应链攻击已成现实**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVT1L4JqqE9mg6Rx22iaFM58Lb02NSPV3KBTGytBHfq91eDl798zsPicBRyc4VEbam9bZdFmj57hXsbamkDltKSRibqkvicMZ1u6hA/640?wx_fmt=gif&from=appmsg)

Zenity公司的安全策略副总裁Chris Hughes提到，"长期以来，我们一直在理论上讨论AI供应链安全，而这周它已成为运营现实。当一个单一的议题标题就能影响自动化构建管道并影响已发布版本时，风险就不再是理论上的了。整个行业需要开始认识到这一点：AI代理是需要治理的特权角色。"

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

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

[PyPI恶意包利用依赖引入恶意行为，发动软件供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523844&idx=2&sn=08c8962eead61fe76467a9196b3da3e5&scene=21#we...