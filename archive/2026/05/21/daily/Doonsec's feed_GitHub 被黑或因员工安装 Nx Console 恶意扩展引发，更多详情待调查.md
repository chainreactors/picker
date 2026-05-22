---
title: GitHub 被黑或因员工安装 Nx Console 恶意扩展引发，更多详情待调查
url: https://mp.weixin.qq.com/s/Nyd964qJDIplLdY98vr8Kg
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:04:11.763538
---

# GitHub 被黑或因员工安装 Nx Console 恶意扩展引发，更多详情待调查

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# GitHub 被黑或因员工安装 Nx Console 恶意扩展引发，更多详情待调查

综合编译
综合编译

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

**GitHub****已证实称，一名员工安装了一个恶意的 VS Code 扩展，导致约3800个内部仓库被盗。GitHub 虽然并未提到该扩展的名称，但负责运营 Nx 的公司首席执行官 Jeff Cross已在社交媒体证实称，GitHub 安全事件的初始攻击向量是 Nx Console 扩展。不过 Jeff Cross 在后续更新中表示，“目前仍在等待GitHub 在时候调查报告中确认 Nx Console 就是那个未具名的 VSC 扩展，但我认为是。”**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXShLX2zgB7cWjsDjQOQ7hpJYVTDWiaXGjkSMZ1iaBHywyRdNGpnbaibfJ4OytKjTYJjWFg0lI3r0ibBeicEGfib27DYsc3IZI9VylPE/640?wx_fmt=gif&from=appmsg)

**GitHub 发布最新调查进展**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVfMFFicEk7qoGQVic2s51CQ64hBDkCTmpDhyYgtfMgzQVEPGr6LfypvtIXxHt6icR2bUqgQIDRLevibzZphCJZvwY7IUh1f8UxvqU/640?wx_fmt=gif&from=appmsg)

GitHub 在社交媒体发布调查进展时表示，“昨天，我们检测并阻止了一起因员工设备安装了一个投毒 VS Code 扩展导致的安全事件。我们删除了该恶意扩展版本、隔离了端点并立即启动了事件响应。”

GitHub 还表示，当前评估认为该攻击仅泄露了 GitHub 的内部仓库。目前的调查结果与黑客团伙 TeamPCP 声称攻陷3800+仓库的说法一致。为此，谷歌采取多项措施来减少风险，昨天更换了关键密钥并优先处理影响最大的凭据。目前仍在继续分析日志、验证密钥更换并监控后续活动。

虽然 GitHub 并未说明该扩展的名称，但负责运营 Nx 的公司首席执行官 Jeff Cross 最新发布帖子表示，“目前仍在等待GitHub 在时候调查报告中确认 Nx Console 就是那个未具名的 VSC 扩展，但我认为是。”

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUZg5Zbu7Qb82YDvleJEaCJIWXMgYjvTibZv3MuTevlOc9aEHPXb84sFichubs0OXT976G6WwCaZHsbdvttxBm8MrbOdLvvMxxGE/640?wx_fmt=gif&from=appmsg)

**Nx 回应**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUmf9X9XdQHibfQ2zKWLWGyiccb5Z0FVcNesyJzTQPicAn5RKwnicuaGbtSXS8kUBriaQaYenr8kZbKPuMLkaiaVp7mmx73PxzuTCH9M/640?wx_fmt=gif&from=appmsg)

负责运营 Nx 的Narwhal 技术公司的首席执行官 Jeff Cross 也在社交媒体上表示，“GitHub 今天发布的报告证实称受陷 Nx Console 扩展是本次攻击的初始访问向量。作为 Nx 的首席执行官读到这个结论，难以接受，不过还是希望直接说明：我们为自身软件在本次事件中所扮演的角色担责。” Jeff Cross 感谢 GitHub、微软和其它独立团队迅速调查、遏制并公开共享信息。他指出，“本次事件凸显了我们和其它维护人员需要更加深入和深刻地思考如何保护开发者工具和开源工作。”他提到已经在发布、自动化和扩展安全态势方面进行重大调整，并将在执行后继续公开分享。他指出已经和其它高级别开源维护人员探讨如何合力保护软件供应链的安全，并提到目前的工作重心是支持受影响用户、加固 N 并助力促进更广范围的生态系统采取更强有力的供应链安全实践。

当有人提到，为何Nx 通过恰当的管道并以经过证明的方式发布 Nx，但一名开发人员仍然能够通过官方渠道提交恶意 commit。也有人提到去年8月就发生了类似事件，质疑本次响应是否做出改变，从而发挥作用。Jeff Cross 表示后续将发布完整详情，复盘整个事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXq9ShibPund3eADVvhbfYrde7T1wYd0Ab7ThdGrt7icQGVNPrkqI6oymUTMO72LIqibdhibqwr7ObLTHCjdicictruo9uYkteetQ2gU/640?wx_fmt=gif&from=appmsg)

**受影响 Nx 版本**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUHGcY8Ia8IicGYdS41Teibxzsq2m4AZhoNDujpP3x48Ltds3eZ3iams7WYcibog7B96K6zHykvPm9ueI25TicBkqxoBvibxWMnFK3icE/640?wx_fmt=gif&from=appmsg)

Jeff Cross 表示，目前仍然和微软以及 GitHub 协同调查 Nx Console 18.95.0 恶意版本造成的影响。最初微软表示该恶意版本的安装次数为28次，但根据Nx自身的调查，受感染的用户数量应当远超这个数字，安装量可能超过6000次。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUvxKOamyAY2NfJvuOZEK59SEibiajmRKCicDAeTzQtXvZiav3iaCTy3axgj4ia275V425uL5VVLdQc0uiaUfibna2o5JPxGu6SwBeQBxA/640?wx_fmt=gif&from=appmsg)

**TeamPCP 团伙要价至少5万美元**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUjCMNoSK2dMiaJcmLia9SKIrjoejz6R3NBIBaMicTfIT11GML2HxFEzaLibV7sh1JZKI2icicuuOiaYBiboghJFLUG4WQv1lib8ZHqRDW8/640?wx_fmt=gif&from=appmsg)

TeamPCP 在地下论坛发布帖子称，这些被盗数据的要价至少5万美元。

该团伙此前多次针对开发者代码平台发动大规模供应链攻击，攻击对象包括 GitHub、PyPI、NPM、Docker，更有近期影响两名 OpenAI 员工的 Mini Shai-Hulud 供应链攻击事件。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfW6iavUkL8OCqWicxwEY1DfIXnwGENMy1BJzdScuyFfdzKn3G3wRg56mK2EiaWlO9TO0Mlaj4Ygia1iaF5v1lTvLdnE9fzfRjiaXdOSQ/640?wx_fmt=gif&from=appmsg)

**VS Code 扩展常遭利用**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVGuaZN9ic3ITJbOyUdktxZVLGxOIYV3mQqZufKI1BdjK9N8sQXDotWQWBmGgOduHvGwO5TWQEfEw2CaicQWOGS8DlzSFa511HDo/640?wx_fmt=gif&from=appmsg)

这也并非 VS Code 扩展被木马化。除了 Nx 扩展外，其它扩展的恶意版本也被安装数百万次，窃取用户凭据和其它敏感数据。如去年，下载量达到900万次的 VSCode 扩展就制造多起安全风险事件，伪装成合法的开发工具导致用户感染 XMRig 密币矿机。

GitHub 基于云的平台目前用于400多家组织机构，其中90%是财富100强企业，超过1.8亿开发人员为超过4.2亿代码仓库贡献力量。

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[奇安信Qcode Agents重磅升级，正式解锁操作系统级漏洞挖掘能力](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526048&idx=1&sn=0cc70737a4725595d2a468599e295579&scene=21#wechat_redirect)

[Grafana 令牌被盗，GitHub 环境可遭访问且代码库被下载](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526043&idx=2&sn=ef8599cf70e02716369d0205be9be468&scene=21#wechat_redirect)

[TeamPCP再发动供应链攻击；数百个恶意包被上传，RubyGems 暂停新账号注册](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525995&idx=3&sn=e59f7d088b3f4113b18c149ac6e505c3&scene=21#wechat_redirect)

[Checkmarx 再遭攻击，Jenkins AST 插件受陷](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525972&idx=1&sn=b93bcffc7c3ad4c106fbd39a4ee2218e&scene=21#wechat_redirect)

[Go 流行库 fsnotify 的维护人员访问权限变更，拉响供应链攻击警报](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525972&idx=2&sn=26ec27a2c831c25b913ce2dfb5658469&scene=21#wechat_redirect)

[Gemini CLI 严重漏洞可触发 RCE 攻击和软件供应链风险](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525887&idx=1&sn=294cc8c49080c6239db19c1f8525457e&scene=21#wechat_redirect)

[自传播供应链蠕虫劫持 npm 包，窃取开发人员令牌](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525844&idx=2&sn=3f396c2336c086719e62350cd61cd2bb&scene=21#wechat_redirect)

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

[受 Salesforce 供应链攻击影响，全...