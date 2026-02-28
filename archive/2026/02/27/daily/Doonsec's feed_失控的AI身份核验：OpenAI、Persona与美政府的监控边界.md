---
title: 失控的AI身份核验：OpenAI、Persona与美政府的监控边界
url: https://mp.weixin.qq.com/s/-a9ZCtEorTSjOJzo4nalFg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:00.947235
---

# 失控的AI身份核验：OpenAI、Persona与美政府的监控边界

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrn0zmTDib2ic6bZPuzibnltpw5YyfIWA3AiaVQ1iaQGYJ7NPPUXibCaWQfl2GdiaKJ02eUhwB0Fg8CfrfhuDbomvDafHicwVX1IfZ9AZY/0?wx_fmt=jpeg)

# 失控的AI身份核验：OpenAI、Persona与美政府的监控边界

安全内参

![]()

在小说阅读器中沉浸阅读

编者荐语：

为了使用 ChatGPT 等 AI 工具上传的身份证、自拍、个人信息，不仅会被一套不透明的系统全方位筛查，甚至可能通过一条隐秘通道，直接上报给美国联邦执法部门。

以下文章来源于黑鸟
，作者黑鸟

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

2026 年 2 月，一场由海外安全研究团队发起的调查，撕开了 AI 时代用户隐私保护的巨大口子：

为了使用 ChatGPT 等 AI 工具上传的身份证、自拍、个人信息，不仅会被一套不透明的系统全方位筛查，甚至可能通过一条隐秘通道，直接上报给美国联邦执法部门。

这场调查的核心，牵扯到了全球 AI 巨头 OpenAI、美国头部身份验证公司 Persona，以及美国联邦政府的监管体系。

Persona 全称Persona Identities, Inc.，是美国头部的企业级身份验证与身份治理解决方案服务商，核心为企业提供全流程 KYC（了解你的客户）、身份核验、反欺诈、合规风控相关的产品与服务，也是 OpenAI、Discord 等全球知名科技企业的核心身份验证合作方。

两篇来自vmfunc的调查报告，完整还原了这套 “身份监控机器” 的搭建逻辑、运作方式，以及事件曝光后的官方回应与未解争议。

## 事件起因：一次常规研究，挖出了不该存在的监控数据库

##

这件事的开端，本是一场再普通不过的安全研究。研究团队最初只是想研究身份验证（KYC）流程的绕过方法，目标是 Persona 这家为 OpenAI、Discord 等众多平台提供身份核验服务的公司。

他们用网络空间搜索引擎 Shodan 扫描互联网上的公开服务器时，一个特殊的 IP 地址引起了注意：`34.49.93[.]177`。这个部署在谷歌云的服务器，绑定了两个让所有人意外的域名：

* `openai-watchlistdb.withpersona[.]com`
* `openai-watchlistdb-testing.withpersona[.]com`

翻译过来，就是**OpenAI 监控名单数据库**。

这不是普通的身份核验域名，既不叫 “openai-verify（验证）”，也不叫 “openai-kyc（身份认证）”，而是直白地标注了 “watchlistdb（监控名单数据库）”。更关键的是，证书透明日志显示，这套系统早在**2023 年 11 月**就已经上线运行。

而 OpenAI 直到 2025 年年中，才公布了 “组织认证” 的相关要求，直到 GPT-5 发布，才公开要求普通用户完成身份核验才能使用高级功能。也就是说，在公开告知用户需要身份验证的**18 个月前**，OpenAI 就已经搭好了这套用户监控筛查系统，在用户毫不知情的情况下，完成了对海量用户的背景筛查。

顺着这条线索深挖，研究团队有了更惊人的发现：Persona 为美国联邦政府搭建的专属身份平台`withpersona-gov[.]com`，出现了严重的配置失误 ，53MB 的完整源代码被无防护地暴露在公网上，任何人都能下载查看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDopsgUgyic11c0w7zUOOYJ1X8VSW93UicxzQIibkebqrWB57wGR6ib1IvxEUbcJ3WF8e6kZjDoJPtHTXOVkAeqqvQNqSs5t5HMJDpc/640?wx_fmt=png&from=appmsg)

这份包含 2456 个源码文件的资料，完整揭开了这套系统的全部功能：它不仅能做身份核验，还内置了向美国财政部金融犯罪执法网络（FinCEN）一键提交可疑报告的功能、覆盖全球的制裁名单筛查、面部识别比对、生物特征数据库，甚至能对接加拿大的金融情报系统，给报告打上美国情报项目的专属代号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqFibE9Vfe8ICFHk91mvsAFdAp3zAXzBecgCytk906AoF1aecNZBqiadqrKvbiaIDD1WStJQAWHOKfzQpLjpMPVEjHYKRCrUTVR3w/640?wx_fmt=png&from=appmsg)

研究团队全程没有入侵任何系统、没有使用任何账号密码、没有修改任何数据，所有信息都来自互联网上公开可访问的资源，完全符合美国的相关法律规定。而正是这些 “光明正大” 暴露的信息，让这套本应藏在暗处的 “身份监控机器”，彻底暴露在阳光下。

## 核心真相：为了用 ChatGPT，你正在接受怎样的筛查？

##

很多人以为，上传身份证和自拍给 OpenAI，只是为了 “证明你是真人，不是机器人”。但源码和基础设施信息显示，这套系统的筛查维度，早已超出了 “身份核验” 的范畴，形成了一套全维度的用户画像与风险标记体系。

### 269 项检查，你的一切都被系统扫描

Persona 的系统里，针对用户的验证检查足足有 269 项，覆盖 14 个大类，小到自拍的拍照姿势、背景画面，大到你的社保记录、证件真伪，全都会被逐一核验。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrjxkQTRO4dWs8yywZfECI8S1EkAYNtMDTlbpUqU1SB1Lj63vkQyln5GgMia3dnoFFYgNib9RxndF1Z3axf7l5Qm0LqjQ6sQ6D3g/640?wx_fmt=png&from=appmsg)

* **自拍相关检查 23 项**

  不仅会检测你是不是真人、有没有用照片/视频伪造，还会判断你的脸 “是否像公众人物”“是否属于可疑实体”，甚至会检测你有没有戴口罩、戴眼镜，拍照姿势是不是和其他用户重复，背景是不是和别人雷同；
* **证件检查 43 项**

  除了验证身份证、护照的真伪，还会对接美国驾照数据库、印度的身份系统、巴西的人脸比对库，甚至能检测证件有没有被篡改、PDF 文件有没有被编辑过；
* **数据库与设备检查**

  会核对你是否在死亡人员名单里、手机号对应的运营商信息，还会通过浏览器指纹、设备指纹，给你使用的设备打上唯一标记，实现跨平台追踪。

最让人不安的，是一项名为`SelfieSuspiciousEntityDetection`（自拍可疑实体检测）的功能。系统会通过 AI 判断你的脸 “是否可疑”，但源码里完全没有公开判定标准，用户既不会被告知自己被标记，更不知道自己为什么会被判定为 “可疑”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoNu0m3SCrbVQdXrRT1ic7nPggxM42CyuTIy59X54A9dSdMtmWpia2QyibiaSZUPicTAia0SFzasnAPYOEXbcMaM7FwlSO4bcoiciadACY/640?wx_fmt=png&from=appmsg)

### 你的自拍，正在和全球政要、制裁名单做面部比对

源码证实，这套系统不仅会核对你的姓名和制裁名单，还会用面部识别技术，把你上传的自拍，和数据库里的人物照片做相似度比对，分为低、中、高三个风险等级。

比对的对象，不仅包括美国 OFAC（海外资产控制办公室）制裁清单上的人员，还覆盖了全球各国的政治公众人物（PEP），从国家元首、政府高官，到他们的家人、密切关联人员，全都在比对范围内。

简单来说，你为了用 ChatGPT 拍的一张自拍，会被 AI 拿去和全球数千名政要、被制裁人员的照片挨个比对，算出你和他们的面部相似度。一旦被标记为高匹配，就会被系统重点标注，而这一切，用户全程毫不知情。

### 直通美国政府的 “可疑报告” 一键提交通道

Persona 的这套系统，最核心的敏感功能，是直接打通了和美国、加拿大官方金融情报机构的上报通道。

* 针对美国市场，系统内置了完整的**可疑活动报告（SAR）** 模块，操作人员可以直接在后台生成符合美国财政部 FinCEN 规范的报告，点击按钮就能直接提交给美国联邦政府，系统会全程跟踪报告的受理、审核、驳回全流程；

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDroaqms4LwDLsp6LSvtdF9Z9kxp3LibkheGpcQT61UP1RomFBqRYPwOMJk5zicVJ5gWKu0b76BSB2D7AaTBvV0KxTZd58bxuUa6Y/640?wx_fmt=png&from=appmsg)
* 针对加拿大市场，系统支持提交**可疑交易报告（STR）**，还能给报告打上加拿大情报项目的代号，包括 Project SHADOW、Project LEGION 等真实存在的公私合作情报项目。

Persona 的商业案例显示，它为 OpenAI “每月筛查数百万用户”，其中 99% 的用户都在后台被自动筛查。而这套能直接给联邦政府提交报告的系统，和 OpenAI 用户身份核验用的，是同一套代码库、同一个数据模型，只是部署在不同的服务器上。

### 你的生物信息，留存时间远超公开承诺

OpenAI 曾对外公开，用户的生物特征数据最多只会留存 1 年。但源码里的信息却和这个说法完全矛盾：系统里的人脸数据库，单条数据的最长留存期设置为 3 年，也就是 1095 天，到期后才会自动删除。

更关键的是，用户如果身份核验被拒绝，不仅不会收到任何拒绝理由，没有任何申诉渠道，系统还会留存你的相关数据。而这些被留存的信息，能否被执法部门调取、通过什么流程调取，全程没有任何公开说明。

## 引发轩然大波的 “ONYX” 疑云：和移民监控工具同名的神秘部署

##

在调查过程中，研究团队还发现了一个时间点和名字都极度敏感的神秘部署：`onyx.withpersona-gov[.]com`。

这个子域名在 2026 年 2 月 4 日才刚刚上线，距离研究报告发布只有 12 天，拥有独立的谷歌云服务器、专属的证书和 Kubernetes 集群，后台加载了面部识别的相关代码。

而 “ONYX” 这个名字，恰好和美国移民与海关执法局（ICE）斥资 420 万美元采购的 AI 监控工具**Fivecast ONYX**完全同名。这款工具被 ICE 用于社交媒体监控、人物数字足迹追踪、风险评分判定，是美国移民执法部门的核心监控工具之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDribMIz9Bt0icljibzhvRLGV9udrN336b1f0WO2uicdfUMsa4w0apLQyaT7tWjuSRSZFtolFswLDqnFRLuHM1IQ4gk8p8RW1Stic6ibo/640?wx_fmt=png&from=appmsg)

尽管源码里没有找到 Persona 的 ONYX 部署和 ICE、Fivecast 的直接关联，也没有任何移民执法、驱逐相关的功能代码，但这个巧合的名字、上线时间，以及部署在 Persona 的政府专属平台上，还是引发了外界的强烈担忧：这套身份验证系统，是否会被用于美国的移民监控与执法？

## 官方回应：Persona CEO 的主动沟通，与仍未解开的核心疑问

##

事件曝光后，行业内普遍预测 Persona 会走常规的 “发律师函、要求删帖、DMCA 下架” 流程。

但让人意外的是，报告发布不到 24 小时，Persona 的联合创始人兼 CEO Rick Song 就主动给研究人员发了邮件，全程以个人身份沟通，没有让法务团队介入，还承诺会书面回答报告里提出的 18 个核心问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpgibQNC8r6wultTJ7OEJWfuQ29AenQiczjWYvuTYHDlPg3K6QSU3icZk2rvUUj5IdrQe9cjO4pgzKypqRO49ebxqLyROOoLjbz3Q/640?wx_fmt=png&from=appmsg)

最终，双方在 4 天里往来了 10 封邮件，研究团队完整公开了全部沟通内容，而 Persona 的核心回应，集中在这几个关键问题上：

1. **关于 OpenAI 的监控名单数据库**Rick Song 明确表示，`openai-watchlistdb`只是为 OpenAI 单独搭建的单租户制裁筛查工具，**只做一件事**：通过姓名、生日、国籍三个信息，比对美国 OFAC 的公开制裁名单，没有任何生物识别、面部比对的代码，也不存储任何用户数据，是完全无状态的服务。独立部署只是为了应对 OpenAI 的海量用户流量，解决网络适配问题，并非为了数据隔离保密。他还强调，绝对没有通过 Persona 系统，把 OpenAI 的任何用户数据提交给 FinCEN 或其他政府部门。这套上报功能只有金融机构客户才能使用，且必须使用客户自己的官方报备资质，Persona 本身没有任何向政府提交报告的权限和资质。
2. **关于 ONYX 命名争议**Rick Song 解释，ONYX 这个名字，只是因为团队里一位员工最喜欢的宝可梦是 ONYX（大岩蛇），和 ICE 的监控工具没有任何关联，团队在报告发布前，甚至都不知道 ICE 有同名的工具。他还表示，Persona 目前没有和任何美国联邦机构签订有效合同，正在洽谈的潜在合作，也只是为联邦政府远程办公的雇员做账号身份认证，和监控完全无关。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq2asQAALFicKKRBw5UthV1MzXQOsGreiaJ7IYZRtdQaXXkluibMaTq2Uicv3CeYKEktfTqQj0AeKqfyQTYZib8P7kxNbnbRDqzPJIw/640?wx_fmt=png&from=appmsg)
3. **关于源代码泄露**他承认源代码暴露是团队的配置失误，但强调泄露的集群是还在开发中的迁移环境，并非通过了美国 FedRAMP 安全认证的正式生产环境，这套开发环境还没经过完整的安全评估和渗透测试，事发后已经紧急修复了相关问题。
4. **关于数据留存**Rick Song 表示，Persona 的全球数据最长留存上限是 3 年，客户可以自行设置更短的留存期，OpenAI 设置的 1 年留存期完全符合要求，会优先执行；而年龄验证这类敏感场景的数据，会在核验完成后立刻脱敏删除。
5. **关于生物识别功能**他解释，平台的面部比对功能，只有客户主动开通、用户明确授权同意、且姓名等基础信息已经匹配到制裁名单的前提下，才会启动，唯一的用途是**排除误报**—— 因为行业内 99% 的制裁名单匹配都是误报，前 20 个高频同名人员，造成了全行业 40% 以上的误判，面部比对只是为了避免无辜用户被误伤。而 OpenAI 完全没有开通这项功能，也没有使用 PEP 政治人物筛查服务。

### 仍未得到回答的 9 个核心问题

###

尽管 Persona CEO 回应了部分质疑，但研究团队提出的 18 个问题中，只有 6 个得到了完整回答，还有 9 个关乎用户核心权益的问题，至今没有得到明确回应：

1. 到底有哪些美国联邦机构，正在使用`withpersona-gov[.]com`这套平台？
2. “自拍可疑实体检测” 的判定标准到底是什么？哪些面部特征会被标记为 “可疑”？
3. 源码里提到的 “实验性面部检测模型”，到底有什么用途？
4. 针对美国伊利诺伊州严格的生物信息隐私法，Persona 是否完成了合规评估？
5. 乌克兰并未被美国 OFAC 制裁，为什么会和伊朗、朝鲜等被制裁国家一起，被 OpenAI 屏蔽服务？
6. 身份核验被拒绝的用户数据，执法部门能否调取？需要通过什么法律流程？
7. 用户是否被明确告知，自己的自拍会被拿去和全球政治人物做面部相似度比对？
8. 系统里标记 “高风险” 并建议自动拒绝的活体检测功能，是谁授权上线的？误判率有多高？
9. 源码里提到 AES 加密密钥 “依赖混淆处理”，这一问题是否通过了 FedRAMP 的安全评估？

## 事件影响与本质：AI 时代，我们的隐私正在被谁掌控？

##

这份调查报告发布后，立刻在全球科技圈引发了地震：

* 社交平台 Discord 直接宣布终止和 Persona 的年龄验证合作；
* 美国电子前哨基金会（EFF）、全球多家科技媒体纷纷跟进报道，聚焦 AI 时代的用户隐私风险；
* 大量普通用户开始质疑，自己为了使用 AI 工具交出的身份信息，到底流向了哪里。

这件事最值得我们关注的，是它揭开了一个 AI 时代的核心真相，**当我们把自己的身份信息、生物特征交给 AI 公司时，我们根本不知道这些数据会被用于什么场景，会和哪些机构共享，会被纳入怎样的监控体系。**

OpenAI 对外宣传的 “安全与合规”，Persona 标榜的 “便捷身份验证”，背后是一套不透明、无申诉、全程对用户保密的筛查与标记体系。

所谓的 “防止坏人滥用 AI”，最终变成了对所有用户的无差别监控；用户为了使用 AI 工具让渡的隐私，成为了商业公司与政府监管之间打通的数据桥梁。

研究团队在报告的结尾写下了这样一句话：“如果有人让你拍一张自拍来证明你是人类，你应该问问自己，镜头的另一端是谁，而你又刚刚登上了哪一份名单。”

而这场关于 AI、隐私与监控的讨论，显然不会随着 Persona 的回应而结束。

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7...