---
title: 网安秋招警惕“假面试”投毒：已有3万台设备中招
url: https://mp.weixin.qq.com/s/a-B857vyL9EIC_O82Chm9A
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:01:12.487820
---

# 网安秋招警惕“假面试”投毒：已有3万台设备中招

# 网安秋招警惕“假面试”投毒：已有3万台设备中招

原创

小胖快学网络安全
小胖快学网络安全

小胖快学网络安全吧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

假设你刚加上一位招聘负责人。

公司能查到，岗位介绍也挺正规。聊了几句，对方发来一个代码仓库，说这是技术面试题，让你先把项目跑起来，第二天再聊实现思路。

项目运行时报错，对方很快发来一段命令：“复制到终端执行一下就好了。”

这时候，你会照做吗？

秋招节奏快，大家都怕错过机会。对方顶着招聘人员的身份，前面又铺垫了那么多，很少有人会把这一刻和网络攻击联系起来。

问题恰恰出在这里。

你以为自己在做面试题，对方等的可能只是你亲手把陌生代码跑起来。

01 “假面试”已经不是一种猜测

2026年9月18日，日本警察厅、美国FBI、澳大利亚网络安全中心等机构联合发布了一份安全通告。

通告提到，一个被称为WaterPlum的朝鲜攻击团伙，会伪装成雇主、招聘人员或者技术负责人，通过招聘网站、社交平台和自由职业平台接触求职者。

他们提供的岗位通常不差，涉及软件开发、人工智能、区块链、加密货币和Web3等方向。

前面是正常的岗位沟通，后面也可能真的安排视频面试。等求职者逐渐放下戒心，对方才会发来所谓的“编程测试”。

有的是代码仓库，有的是需要安装依赖的项目。还有一种做法，是在视频会议出现“故障”时，让求职者下载文件或者执行修复命令。

恶意程序就混在这些操作里。

官方披露，从2025年12月至2026年7月，该团伙至少影响了100多个国家的3万台设备，超过7000个加密货币钱包的资金或账户凭证遭到窃取，涉及资产约1071万美元。

因为对方盯上的并不是普通消费者，而是软件开发者、Web工程师和IT专业人员。

这群人有一个共同习惯：收到项目后，拉代码、装依赖、运行起来看看。

网安学生参加技术面试时，面对的恰好也是这种环境。

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl2fXnabtYNicXQkGm7fVdNnC41BPcQJbKibKJMdItp8Whp9TvRhow1WIdibmweOzPPoS1icfh934GHUufGtgWofDlCaJBX4VV9ibPTk/640?wx_fmt=png&from=appmsg)

02 项目跑起来了，风险也可能跟着启动

这类攻击最容易让人中招的地方，是它不像传统印象里的“病毒文件”。

对方不会一上来就发一个来历不明的安装包。相反，他会先和你聊技术栈、工作内容和面试流程。等你确认“这应该是一次正常招聘”后，再把有问题的内容塞进项目里。

接下来的事情就顺理成章了：

对方发来代码仓库，催你完成面试任务；你在自己的电脑上安装依赖、运行项目；隐藏在其中的程序开始读取浏览器信息、本地文件和账号凭证。

联合通告提到，可能被获取的内容包括浏览器保存的账号密码、剪贴板、键盘输入、屏幕截图、数字钱包信息，以及电脑和共享目录中的文件。

如果本机还留着GitHub Token、SSH密钥或者云平台密钥，事情会更麻烦。

这些凭证相当于代码仓库和服务器的“备用钥匙”。攻击者拿到以后，影响的可能就不只是你的个人账号，还可能包括项目源码、云主机甚至企业内部系统。

所以，受害者以为自己在接受面试，对方真正想确认的，却是这台电脑里有什么值得拿走。

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl3bdw3NTf7UrjsSNqYC1CI0ibic8V2nr2qkYC0MlpUZ7w6k1YAbmbiclBN13pWPib4icALicLC4d3iaoicvMmGPchQ8aU10x9a3hKdj5qE/640?wx_fmt=png&from=appmsg)

03 遇到这5种情况，先停一下

技术面试要求做代码作业很正常，不能看到陌生项目就一律当成骗局。

但下面这些情况如果同时出现，就别急着运行了。招聘者的身份无法核实

对方只使用私人邮箱或者聊天软件联系你，企业官网查不到相关岗位，邮箱后缀和公司域名也对不上。

头像、职位和公司名称都可以复制，不能只凭一张资料页判断身份。岗位好得有些不真实

没有经过多少技术沟通，对方就给出明显偏高的薪资、完全远程办公或者快速入职的承诺。

条件越诱人，人越容易忽略本来应该做的核实。一直催你马上运行

“今天必须完成。”

“运行成功才能进入下一轮。”

“先别检查了，肯定没问题。”

正常公司不会介意候选人检查项目，更不会把“马上执行”当成进入下一轮的条件。要求关闭安全软件

如果项目必须关闭杀毒软件、防火墙或者系统保护才能运行，基本没有继续冒险的必要。

公司要考察的是技术能力，不是看你愿不愿意关闭安全防护。让你执行看不懂的命令

特别是那些会下载远程文件、修改系统设置或者隐藏执行过程的命令。

看不懂，就不要运行。对方自称面试官，并不会让一段陌生命令变得更安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl2tu7Cgxp6MLbgNxmARhfEibZasvMLYIGwTbgmJUEic72j7qRFPMmIWN3ibHdUE4gGbPnXRTj7ktjlQpeIwnFpc8WmZ9XEaOPdLMc/640?wx_fmt=png&from=appmsg)

04 项目可以做，别在主力机上裸跑

遇到技术面试项目，我更建议先做一个简单的“红黄绿灯”判断。绿灯：身份和项目都能验证

企业官网能查到岗位，招聘人员使用企业邮箱，任务要求说得清楚，也允许候选人先检查代码。

这种项目可以正常查看。不过在运行之前，依赖和自动执行脚本还是要过一遍。黄灯：暂时不能确定有没有问题

招聘者身份无法完全确认，代码仓库比较陌生，项目里又包含大量依赖或者自动执行脚本。

这种情况不一定是骗局，但没有必要拿主力电脑去赌。

可以使用虚拟机、沙箱或者专门的测试电脑。测试环境里不要登录私人邮箱、代码平台、云服务和数字钱包，也别把真实密钥、证件和工作资料放进去。红灯：到这里就该停了

对方要求关闭安全软件、导入钱包或者云平台凭证，又或者坚持让你执行无法解释的命令。

这时候先别考虑会不会错过面试，重新核实岗位和招聘者身份更重要。

面试项目可以做，但求职焦虑不能替你按下“信任并运行”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl0xKaflhxQs6EAhFNjac9CiaUlmq4sbvvtvWSeW7EI4bhSTvdlvk12xUeEcUeibyYY3LexpV0h189pMsK0TzHljzOxJz3XkWVKvo/640?wx_fmt=png&from=appmsg)

05 已经运行了，现在怎么办？

如果你刚刚运行过来源不明的项目，先别只顾着删除文件。

第一件事是断开网络，减少可疑程序继续向外传输数据的机会。

接下来换一台可信设备处理重要账号。修改邮箱、代码平台和云服务的密码，同时注销其他登录会话。

如果电脑里存过GitHub Token、SSH密钥或者云平台访问密钥，还要把旧密钥撤销，再重新生成。只改密码，不一定能让已经泄露的密钥失效。

浏览器保存的密码、Cookie、钱包插件，以及本机存放的个人证件和敏感文件，也要逐项检查。

设备里如果有数字钱包，可以考虑在干净设备上创建新钱包并转移资产。

即使安全软件已经完成查杀，也不能据此判断数据从未被传出去。如果电脑中长期保存着重要凭证，或者后续仍然出现异常进程、弹窗和网络连接，备份必要文件后重装系统会更稳妥。

删除项目，只是删掉了眼前的文件，并不代表风险已经消失。

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl0zsnZxbRrrvibEeJ5EfGarzNIoZKzujiaSBLr6sOVaia4HcxPkkdcIhlia9kNUGAHwbIwRibE45MGjDjoGDdOG02cPPZxtL3osKNcM/640?wx_fmt=png&from=appmsg)

写在最后

这篇文章不是想让大家拒绝所有面试项目。

企业通过代码作业了解候选人的真实水平，很正常。真正值得警惕的，是几件事同时出现：

身份无法验证，岗位好得不真实，不断催促运行，项目来源不明，还要求关闭安全保护。

有时间的话，可以检查一下自己的求职电脑：

浏览器里是不是保存了重要密码？

代码平台和服务器密钥是不是长期留在本机？

个人证件、钱包插件和项目源码，是不是全放在同一台电脑里？

有些人发给你的不是offer，而是一个等着你亲手运行的入口。

你在面试中遇到过要求下载项目、安装依赖或者运行命令的情况吗？当时是怎么判断的？

星球介绍

一个人走的很快，但一群人才能地的更远。吉祥同学学安全这个[星球🔗](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486065&idx=2&sn=b30ade8200e842743339d428f414475e&chksm=c0e4732df793fa3bf39a6eab17cc0ed0fca5f0e4c979ce64bd112762def9ee7cf0112a7e76af&scene=21#wechat_redirect)成立了2年左右，已经有600+的小伙伴了，如果你是网络安全的学生、想转行网络安全行业、需要网安相关的方案、ppt，快加入我们吧。系统性的知识库已经有：[《Java代码审计》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484219&idx=1&sn=73564e316a4c9794019f15dd6b3ba9f6&chksm=c0e47a67f793f371e9f6a4fbc06e7929cb1480b7320fae34c32563307df3a28aca49d1a4addd&scene=21#wechat_redirect)++[《Web安全》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484238&idx=1&sn=ca66551c31e37b8d726f151265fc9211&chksm=c0e47a12f793f3049fefde6e9ebe9ec4e2c7626b8594511bd314783719c216bd9929962a71e6&scene=21#wechat_redirect)++[《应急响应》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484262&idx=1&sn=8500d284ffa923638199071032877536&chksm=c0e47a3af793f32c1c20dcb55c28942b59cbae12ce7169c63d6229d66238fb39a8094a2c13a1&scene=21#wechat_redirect)++[《护网资料库》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484307&idx=1&sn=9e8e24e703e877301d43fcef94e36d0e&chksm=c0e47acff793f3d9a868af859fae561999930ebbe01fcea8a1a5eb99fe84d54655c4e661be53&scene=21#wechat_redirect)++[《网安面试指南》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486695&idx=1&sn=85fefa98f17e6f1f2dd745ef5a498a10&token=1860256701&lang=zh_CN&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl33adFKibqLvAHRJiacH1o1ibbJmV3rfCSs78vNic47eEv0DR7SkbHFoaBX05fQRjoJEtiaIkVssMmnkemnUPMmLSGPwaVYAHWnib4kY/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oh2kiaia4icySDqrNyBCHuYdPugU7RJlWianw9FiaCn6EH2P31ATvZJnibr9IgONEx77AFiaEib2Bnh807WMHcrr9ibqdMA/0?wx_fmt=png)

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