---
title: 伊朗关联组织借虚假招聘和编程测试投放跨平台远控木马，我科技企业海外招聘及开发者终端面临渗透风险
url: https://mp.weixin.qq.com/s/nNcE3ecLK_r8Z-tKk7ULZg
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:00:21.967546
---

# 伊朗关联组织借虚假招聘和编程测试投放跨平台远控木马，我科技企业海外招聘及开发者终端面临渗透风险

# 伊朗关联组织借虚假招聘和编程测试投放跨平台远控木马，我科技企业海外招聘及开发者终端面临渗透风险

FF
FF

情报分析师

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一份看似普通的“限时编程测评”，正在成为进入研发网络的低成本入口。

攻击者不必强攻企业边界，只需让一名开发者在日常终端运行一份招聘代码包，便可能沿着终端、身份、代码仓库和云构建链路持续渗透。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7eVYZd5wxlMUH8AbP0u5QEcXJf2BcusmURFrdKzNEaj40a5SY6PMFREpUeLdwCwZk0J5zic0GogBwzjqhhvibbZUtnutgGqKeDwI/640?wx_fmt=png&from=appmsg)

**招聘作业，正在变成研发网络的隐蔽入口，一次运行操作，可能打开整条开发信任链。**

近期披露的行动显示，伊朗关联威胁集群Mirage Kitten以虚假招聘人员身份，通过LinkedIn等职业平台接触软件工程师，发送“技术挑战”“React项目修复”“限时在线测评”等代码包。

项目外观与正常招聘流程高度相似，底层却嵌入NodeRabbit、PollCat两类跨平台远程控制工具。

目标并不只是求职者个人设备。

真正有价值的是开发者所连接的企业资源：私有代码仓库、云平台令牌、SSH密钥、构建流水线、企业邮箱、协作工具会话，以及合作伙伴网络。

这类攻击把社会信任与技术执行压缩在同一个动作里：下载压缩包、安装依赖、运行项目。

开发者做的每一步都符合工作习惯，攻击者因此不必绕过复杂的边界防护，也不必立刻攻击核心服务器。

卡巴斯基披露，NodeRabbit以Node.js构建，可运行于Windows、Linux和macOS；PollCat则采用混淆JavaScript，并伪装成React代码修复测评。

已确认的受害活动涉及阿富汗、埃及和埃塞俄比亚的金融科技、航空与航天相关组织。

**限时与验证码，不是流程细节而是心理操控**

攻击者对开发场景的理解相当具体。一份伪装项目要求候选人在限定时间内完成修复，并暗示某些核心文件“无需检查”。另一份测评设置六位验证码和倒计时，要求运行 npm i && node index.js 后才能进入题面。

真正的恶意逻辑却可能在应用启动阶段已经执行。

“立即完成”“不得外传题目”“不得使用外部工具”这些要求，表面上是招聘纪律，实际效果是压缩核验时间，降低代码审查概率。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7fPHdCA6RfMm0hPkJSQpatncqSqsic9yvgT0iaobibo9pQwwPeaSibUeHU5qEwicsl7DiaBko3PQoh69sTtAqWG27x05miaTKuUsFHeFk/640?wx_fmt=png&from=appmsg)

越是紧迫、越是强调保密，越可能迫使目标绕开本应存在的安全检查。

这也是传统反钓鱼教育的盲区。开发者不能简单遵循“不要打开陌生附件”，因为其职业活动本就要求下载、编译和运行陌生代码。

风险不在于点击某个链接，而在于把外部代码直接带入了承载企业身份和研发资产的终端。

**Node.js****让恶意活动混入正常开发节奏**

过去，安全团队习惯围绕恶意可执行文件、注册表修改、异常DLL加载和可疑域名开展检测。

如今，攻击者转向Node.js、npm、React、Git和VS Code等开发生态，改变的是隐蔽方式，而非威胁性质。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7dLF1XPm6rvick7dPUnf3yk26nEe2lYAx3khCWia2C7ABjxzM2iaqP2jH3js5FfyL0icOEvZXASlmn0oVKOwrcP2WqcMUW0eicInMuk/640?wx_fmt=png&from=appmsg)

NodeRabbit可执行命令、枚举文件与磁盘、收集网络信息，并扫描Git仓库。后续版本还被发现具有借助Git hook和伪装VS Code扩展维持活动的能力。PollCat同样能够执行脚本、传输文件和识别安全产品环境。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7f3r3DNPeL9WQibG7GJDJJW39msZclgDgEdtOscvwXflcaCrnnjYhFWoB395pWcLJrSiaHWN01fIqS4nSzA7GtQM4ReVYKRlQSWU/640?wx_fmt=png&from=appmsg)

对安全运营而言，难点在于每一个孤立动作都可能正常：Node启动本地服务、npm安装依赖、Git触发脚本、开发工具连接云平台。

真正危险的是一组连续行为——外部压缩包解压后，Node从隐藏缓存或node\_modules目录启动，再拉起Shell或分离进程，并访问此前未出现过的云端地址。

微软已观察到多起滥用Node.js投递恶意载荷、窃取信息和外传数据的行动。

这不是单一组织的偶发现象，而是攻击者正在把通用开发运行时转化为隐蔽执行环境。

**受害地与样本地，必须分开看**

公开信息提示风险扩散，但不能任意外推。已确认受害系统位于阿富汗、埃及和埃塞俄比亚；印度、土耳其、德国、爱尔兰等地出现了相关压缩包的样本提交记录。

两类信息不能混为一谈：样本提交只能说明当地有人获取、分析或上报了文件，不能直接证明当地机构被入侵，更不能据此推断攻击已经针对某一国别或企业。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7eM5DbZyiaFKYjFq5uZrl692GRD0FVlialAPvKhYASICcNXyy9lcwcupzYHxyGv8CK1IaIBqgPxmYPicl5XtnYdWG9N8Xam8pkRCk/640?wx_fmt=png&from=appmsg)

对我科企，目前没有公开、可核查证据表明我境内机构已经遭NodeRabbit或PollCat成功入侵。

但风险条件确实存在：海外研发中心、跨国外包团队、留学开发者个人设备、区域合作伙伴和跨境云构建体系，都是招聘诱饵可能触及的接点。

Google威胁情报团队长期追踪到UNC1549相关活动使用伪造职业门户、招聘诱饵和恶意工具，重点围绕航空、防务、无人系统及相关技术人员展开。

其基础设施中还曾出现冒用无人机制造商等企业信息的招聘材料。

这意味着，不能把“尚未确认受害”误读为“无需处置”。

更准确的判断应当是：攻击能力已经具备，目标条件存在，直接入侵事实仍待企业自身遥测和日志验证。

**防线要前移到招聘与开发环境之间**

外部编程测评应被视为一次“外部代码执行申请”，而不只是个人求职活动。

企业应明确：凡要求下载压缩包、安装依赖、运行脚本、信任IDE工作区、关闭安全工具或在短时间内完成的测评，不得在日常开发终端、生产跳板机或保存企业凭据的个人设备上运行。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7eknW4JA96fnH3Jkz0RxolSfh1sFqDp1y6LMOCA1GYOEBPib4CGMia63Aog5uw0mm559PusQiafsaibtu47Qw5jBAWQAXCGTRK1HM8/640?wx_fmt=png&from=appmsg)

确需参加时，应使用与企业身份隔离的一次性虚拟环境，禁止挂载代码目录、浏览器密码库、SSH Agent、云令牌和企业VPN。

招聘核验也不能依赖对方提供的联系方式。

岗位、招聘人员、测试平台和文件来源，应通过企业官网、官方域名邮箱或其他独立渠道反向确认。

知名云平台托管、HTTPS链接、精致的项目界面，都不能证明代码可信。

更关键的是，把监测能力延伸至开发上下文：关注浏览器或聊天工具下载的压缩包是否触发Node执行，关注node\_modules隐藏目录、Git hook、VS Code扩展、异常出站连接和云凭据访问。

安全团队需要看到Windows、Linux、macOS和WSL上的同类行为，否则攻击者只需转换终端平台，就能绕开防线。

招聘、个人终端、开发工具、代码仓库和云构建，长期由不同部门分别管理。攻击者已经把它们串成一条渗透链。

防御若仍停留在“邮件附件是否报毒”，就很难应对下一份换了名称、换了云存储桶、换了招聘身份的代码测评。

完整版研判涵盖攻击链还原、NodeRabbit与PollCat技术特征、海外研发与外包暴露面、Git hook和云构建风险、分阶段处置方案及可执行排查清单。

欢迎加入**情报读书会知识星球**，下载完整版并获取持续更新的安全情报研判资料。

![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7drFpicRwK9B08IaUEnt94TmWNKmIakzOicK3ibUZf0jtzxBHcZk1eptSFs01Pd4LIUCU2HN1ibwhCZeY32UjibRK91I2FzWbxkJ0ibE/640?wx_fmt=jpeg&from=appmsg)

**【深度研判】伊朗关联组织借虚假招聘和编程测试投放跨平台远控木马，我科技企业海外招聘及开发者终端面临渗透风险****（资料编码2609101030，36页，14778字）**

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7elBBT5VSSsQW62VxibsRX97iaNTQZKfWwarz2PHF5fwwUOov2xYy975fibnOECjQib31kjA7wSoO0qS6WOH4mXwkAbUVU3O4oKdGE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7fHkW3D73ILknUicvXm6lJFZyWYykvUUtm402Yl33BRN9bh1EiceuM4wezJqFINhHC4XDH0CMDnAmrrCbzDxjy79lTLfOiaTqucGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7dnpuf2iayzfsJicJBN9ApKEsiaanTowFYIuWcnZRabXAlGZkXoCxgS47ibslbhcvRyBR5UDsynUVWOPT9wVtzmfUOugmcqUneN3TQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7dQY2YVncWJPv2k3zdDkw9DGYIiaE3gCaUzjz9aUDdfwPia0WEcfibYpazCib8ScxxibtHziahz2a8GSoQFGL03RNQukTRO5fnlePr3M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7fowOyRib6Me2QrW3GqohnbYyveHaSQJic8g2XfTQRIicaZjgCIq6wmc2cdxtVPQUhzaKXeiaYEpAdA3ib3oYwogFeKTBfaXvthO2TI/640?wx_fmt=jpeg&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pBCQrIFuT7dVZwx1BbicibPyx8t3cLfFZiaIkcDxC0Zdew30k5NIwcKl7G9y1QibICrs5DLX8zdEGeFTS4YJW6EnZeiaSWb3FZdoUxXYtbcpTgF0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517630&idx=1&sn=9e3b81a8a102c266955220bb1ea32d51&scene=21#wechat_redirect)

[韩国拟将芯片技术间谍罪最低刑期提高至十年并首次点名外国企业，半导体与人工智能技术竞争加速法律武器化风险研判](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517630&idx=1&sn=9e3b81a8a102c266955220bb1ea32d51&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7c191HJI3wRX6qrNRVkOzMRvXwSx9PJotpQ0ZPYsh1KZjWuXXykBV7EX3zejX1cqv8OAj8IfoiamPnGwtuT8JhuwflOxZyNt4Z8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517600&idx=1&sn=aa13a60bc0ac1f63bbb4346082291a32&scene=21#wechat_redirect)

[美国以防范网络安全“后门”为由宣布国家紧急状态并限制采购外国产电力系统设备，相关供应链安全审查及涉我设备排除风险需关注](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517600&idx=1&sn=aa13a60bc0ac1f63bbb4346082291a32&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7fYPYWYTb0IiccJw4XMQ93ckewWOcJjJ77EibNQI4UIx76kNMLuJ0fZSLGfwQgz46Vgj7ibQzmialMicjOerzWWoib0zEtNMVubnbtjs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517559&idx=1&sn=6c6517f0dc607c61c82555807fcb33bf&scene=21#wechat_redirect)

[鲍曼莫斯科国立技术大学第四系泄密事件暴露俄军网络作战人才培养链路，其与俄军总参谋部情报总局相关单位联系值得关注](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517559&idx=1&sn=6c6517f0dc607c61c82555807fcb33bf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7ciagsJIA0ucY4LibRWB85wjdTuKia3LNyo5FQM8OS6JKllNgvUSDR3QQv16oyqrf8JZMtbKqiabaXibwTvWW6TsJS0ibtic2ujv025E8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517518&idx=1&sn=fbd2c5c982ff1bcd64db4aa5807a2a22&scene=21#wechat_redirect)

[德国联邦情报局借科隆国际游戏展招募网络技术人才，游戏玩家向网络特工转化及德国强化对俄网络攻防对我安全启示](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517518&idx=1&sn=fbd2c5c982ff1bcd64db4aa5807a2a22&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pBCQrIFuT7fkaW5sBS5SQMy6ACuM7B9DufbtyLFRk0IiaOjoJicatICZvW8wMJY6D0F4ZcapYpQZ5Cns1ypj7mZvicDN58BkPEbTNaW1hRicCicE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517505&idx=1&sn=58d921f952260d80dab8e9e15fa2c6dc&scene=21#wechat_redirect)

[2026年首届韩国中亚峰会评估——机制升级、资源竞合与地区秩序影响](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517505&idx=1&sn=58d921f952260d80dab8e9e15fa2c6dc&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUO5dhXictxTG5ooia6EeoxUEWwpdMstx1ibGcNTPKQKdW4lNVR4j8qr8uuWMBNGaGiaRMR0wKXP4hxAw/0?wx_fmt=png)

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