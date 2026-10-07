---
title: 求职面试竟是陷阱！ContagiousInterview传染性面试，VSCode打开项目即中招，受害者还会无意识传播恶意仓库
url: https://mp.weixin.qq.com/s/wlo-rdKrsU5mEvRO0sMhYQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:53:36.293505
---

# 求职面试竟是陷阱！ContagiousInterview传染性面试，VSCode打开项目即中招，受害者还会无意识传播恶意仓库

# 求职面试竟是陷阱！ContagiousInterview传染性面试，VSCode打开项目即中招，受害者还会无意识传播恶意仓库

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaiblC3KQPJLRF3F9rXOJS67ibuWFpJniaZ3GEHYxJXpMEGrgMrKM9XQBj5qeEuPeqj2d1Ht2PnabDaeHRybk88MVbPVVv5AoxHqp8A/640?wx_fmt=png&from=appmsg)

导语

正在找开发岗位的小伙伴务必警惕！

你收到一份看起来非常正规的面试邀约，HR丢来GitHub/Bitbucket代码仓库，让你完成带回家编码测试。你克隆仓库、用VSCode打开项目，还没开始写代码，电脑已经被APT黑客攻陷，密钥、钱包、企业凭证全部泄露。

Atlassian官方发布重磅调查报告，深度解析代号 Contagious Interview（传染性面试） 的国家级间谍活动。该团伙伪造公司、伪造LinkedIn猎头账号，投放大量高仿恶意代码仓库。更可怕的一点：被感染的开发者，还会在毫不知情的情况下，把恶意仓库二次上传，变身恶意代码的传播者。攻击者大量滥用VSCode自动化任务，打开项目文件夹瞬间自动执行恶意载荷，全程不需要你手动运行脚本。

一、完整攻击链路：一场精心布置的虚假求职骗局

整个攻击流程分为6步，全部围绕求职技术笔试展开：

1. 诱饵与伪装：黑客搭建虚假企业官网、注册高仿LinkedIn猎头账号，对外发布开发岗位招聘；

2. 虚假面试邀约：向求职者发送面试邀请，分配“带回家编码作业”；

3. 投放恶意代码仓库：给到GitHub / GitLab / Bitbucket仓库链接，仓库拥有完整项目代码，看起来和真实业务项目没有区别，恶意代码隐藏在少数配置文件内；

4. 受害者克隆打开仓库：开发者克隆仓库，使用VSCode打开工作目录，一旦信任工作区，`.vscode/tasks.json`配置借助`runOn:folderOpen`实现打开文件夹就自动执行恶意脚本；

5. 植入BeaverTail加载器：执行第一阶段载荷，从外部站点下载后续后门、窃取浏览器密钥、SSH密钥、加密货币钱包、环境变量；

6. 无意识二次扩散：部分黑客会要求求职者录制代码操作视频、把作业重新上传代码仓库。受害者上传副本，被感染的恶意仓库借助受害者的正常账号继续对外传播。

重点：很多受害者并不是主动传播，完全不知情，自己的合法账号变成黑客分发恶意样本的渠道。

二、恶意仓库五大高频特征

Atlassian对数百个恶意仓库统计分析，归纳出攻击者偏好的仓库主题占比：

1. 开发项目类20.16%：demo、proto、project‑beta，基础设施、IaC、后端模板；

2. 招聘面试类18.01%：assessment、assignment、candidate‑repo、take‑home，面试笔试题；

3. Web3加密类13.44%：crypto、defi、swap、staking、wallet；

4. 游戏博彩类8.47%：game、poker、casino；

5. 房地产、密钥、平台架构类合计约20%。

攻击者会复用大量IP基础设施，不同朝鲜APT团伙之间存在基础设施共享，BeaverTail载荷在多个攻击活动中反复出现。

三、恶意载荷执行手法持续迭代

从2025Q2‑2026Q2，攻击者不断更新触发恶意代码的手段，多种技术会组合使用：

1. 代码内混淆载荷（长期主力，占比接近100%）：JS代码混淆隐藏加载器BeaverTail；

2. VS Code tasks.json自动执行（爆发式增长）：打开文件夹自动运行shell/curl脚本，是当前最危险的手段；

3. 伪造字体文件、被感染NPM依赖包、NPM生命周期脚本、Git Hooks，多种方式轮番上阵。

VSCode的`tasks.json`的`runOn:folderOpen`是高危关键点，不需要你手动敲命令，只要打开项目文件夹就会触发执行。

攻击效果

一旦BeaverTail执行成功：

收集系统信息、进程列表；

搜刮浏览器全部配置、Cookie、加密货币钱包文件；

读取`.ssh`密钥、shell历史记录、各种API Token；

下载第二阶段远控后门，建立C2通道，实现远程命令执行、文件窃取。

四、受害者会无意识成为传播者，这是最容易被忽视的风险

这是本次报告一个颠覆性发现：

黑客在面试流程中，要求求职者完成作业后，把项目推送到自己的Git账号，录制操作过程。

受害者本机已经被入侵，本地仓库包含恶意`.vscode`配置文件，受害者不知情直接push上传。

原本的受害者，变成新的分发节点，用自己可信的账号对外分发恶意仓库。

安全人员发现不少恶意仓库来自普通开发者正常账号，并不是黑客新建的黑号。

五、个人开发者防护实操（求职必看）

1. 外来面试仓库，绝对不要在主力办公电脑打开运行！

使用隔离虚拟机、干净的备用设备做笔试题，主机保存着公司密钥、SSH、钱包，严禁直接运行外来仓库。

2. 关闭VSCode自动任务风险

设置 `task.allowAutomaticTasks` 为 `off`；

遇到陌生项目，弹出“信任此工作区”提示，一律选择不信任。

不信任模式下，tasks.json自动执行功能会被禁用，阻止打开文件夹就执行脚本。

3. 拿到笔试题仓库，先看目录：重点检查`.vscode/tasks.json`文件，警惕`runOn: folderOpen`字段。

4. 拒绝直接执行陌生仓库的 `npm install`、`terraform init`、`setup.sh`等脚本，先通读代码再评估风险。

🛡️如果怀疑本机已经中招，标准处置步骤

1. 立刻断开网络，保存证据：招聘聊天记录、仓库链接、执行过的命令；

2. 在另一台干净设备上，批量吊销所有会话：密码、SSH密钥、Git令牌、云API密钥；

3. 如果接触过加密钱包，把资产迁移到全新干净设备生成的新钱包；

4. ❗仅仅删除仓库、杀毒软件扫描远远不够，需要整机重装镜像。恶意程序会建立多层持久化，删除源码不等于清除后门。

5. 向代码平台举报恶意仓库、举报猎头招聘账号。

六、企业安全团队狩猎检测建议

1. 终端行为告警重点监控

IDE（VSCode/Cursor）启动之后，意外唤起shell、bash、cmd、curl/wget；

进程访问浏览器配置文件、密码库、keychain、`.ssh`目录、环境变量文件，紧接着发生HTTP/websocket外发上传行为。

2. 开发终端管控

禁止开发机直接持有生产环境高权限，开发机与生产网络做隔离；

监控终端磁盘出现包含`runOn:folderOpen`的tasks.json配置文件。

3. 安全意识培训

重点对求职、外包、DevOps开发人员做宣贯：面试带回家编码测试是高风险攻击入口。

4. 事件响应原则

怀疑被入侵，优先隔离终端、全盘吊销凭据，不要寄希望于杀毒清理，建议重装系统，同时横向排查内网是否已经发生横向移动。

七、安全行业深度思考

1. 社工已经深入开发者求职场景

APT不再只靠邮件钓鱼，伪装成正规企业招聘，利用开发者求职的迫切心理，攻击成功率极高。很多开发者天然相信“面试作业是正常业务流程”，降低警惕。

2. 开发工具的自动化能力正在被武器化

VSCode Tasks、NPM生命周期脚本、Git钩子，这些本来用来提升效率的自动化特性，被黑客拿来做恶意代码自动执行，打开文件夹就中招，不需要用户手动运行任何脚本。

3. 供应链风险不再只是大厂商沦陷，普通开发者个人是薄弱环节

攻破一个开发者个人电脑，就能拿到云密钥、源码、生产访问权限，同时还能借受害者账号二次扩散恶意仓库，放大攻击杀伤范围。

提醒所有找工作的程序员：一份看起来无比真实的笔试题仓库，背后有可能就是国家级APT布下的陷阱。

结尾互动

你在求职过程收到过让你克隆Git仓库做笔试题的邀约吗？你们团队有没有针对外来代码仓库做安全管控？欢迎转发给身边的开发朋友，警惕传染性面试攻击。

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibm0l6wIBoUfic1Rxr77k9bUlBJeO2gkADWstEJ1u2JGkNGd6Td2RFTWbUh4PWaibl2jEpIAZnNsBUjCX8D6Xrlmuw44kpnsx1H34/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibnOts86xJKqAicF3fEIc4dnBIEm1bCBvX9PhLYRgIIpzQRnfnkanibo4N4ogOicxz4HEc3rFqIBscWYQdYZpL8Ucu7kbX0aRicnZjk/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkJsTBMez9zJVBx2GkJZX37f7O4FrIibRh5t4A452yETKicDN4YVqlC8IFp7j3rb1FtERwaHNkNFWq93j1mMPnGemzXIv4NGaUSU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkfA9XDdSgS2UFvFl6eje0BXEeKlZScMVtCNVBSqD7DzicMw2yPB4iahzUA3H97RvicGicibqricFoEQQey8l2qRVdeUHoYRcRDMbl8Q/640?wx_fmt=png&from=appmsg)

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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