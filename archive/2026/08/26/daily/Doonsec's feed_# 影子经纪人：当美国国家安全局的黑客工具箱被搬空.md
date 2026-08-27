---
title: # 影子经纪人：当美国国家安全局的黑客工具箱被搬空
url: https://mp.weixin.qq.com/s/8AqE9uAMUTYAJzie9vYc1A
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:10:17.790946
---

# # 影子经纪人：当美国国家安全局的黑客工具箱被搬空

# # 影子经纪人：当美国国家安全局的黑客工具箱被搬空

红客攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AjSHgfLXVrozeN7CNxzx37rBpib2l1icbdiaAb8iaOPqPgmvqk5aqsL0ltY6lbEWWgceGLfTSJAgicU9TsrDFbuCyGlLDLAYy5rAynfd3iaQvrm78/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrrWBM9NsFoOAYpMwvMcWichCKDr8DKKuoibyTpWEjytoNBTGhX2FLoZG41ufZ3T2gDgn7hE6NZ0p9pb3NRdLRWI1sKH8IeLrtBAA/640?wx_fmt=png)

故事得从一份目录讲起。

2013年底，德国《明镜》周刊拿到了一批美国国家安全局（NSA）的内部文件，其中有一份东西看得所有人头皮发麻——ANT目录。ANT，全称"高级网络技术"，说白了，这是NSA的"黑客装备采购手册"。你在NSA上班，需要黑掉某个目标？翻翻这本目录，挑一件武器，打个申请就行。

这本目录里的东西，乍一看像科幻小说的设定，但每一件都是真的：

**COTTONMOUTH（棉口蛇）**

一个看起来普普通通的USB插头，插在目标的鼠标或键盘线路上，就能把所有经过的数据无线发送出去。隔壁房间的人，能看见你敲的每一个字。2008年的技术，到今天市面上都没有同等商用产品。标价：一个两万美元。

**DROPOUTJEEP**

针对iPhone的植入软件，短信、通讯录、语音邮件全部拿走，还能远程开麦克风、开摄像头、定位。

**JETPLOW**

一种固件，让NSA对思科防火墙拥有永久后门。想象一下：一台防火墙还在快递运输途中，被人拆箱、刷入固件、重新封好，等你拆开包装那一刻，它就永远是别人家的了。

**RAGEMASTER**

一个小装置，接在电脑到显示器的VGA线上，直接把你屏幕上的内容无线传出去。你没联网？没关系，人家看的不是你的网，是你的显示器。

这本目录是给谁用的？**TAO**——"定制访问行动"部门，NSA内部的精英黑客部队。别的黑客找漏洞用天、用周计算，TAO有的是预算和时间，一个漏洞可以悄悄打磨好几年。

安全研究圈没法点名道姓说这是谁干的，就给他们起了个代号——**方程式组织（Equation Group）**。所有人都心照不宣：方程式组织，就是NSA的TAO。

记住这个名字。故事的主角之一，就藏在里面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrocYXt6icYgQb71ITsBzib8mx0lhrHjaMI4pxB72gXwz0awiaGMLiavTTQGG3RMzejMcwQLnTfVfUBjXGGdGyrhuz8l71arpUpPb9c/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqHjB4KLjWGcQhInTAF94vlErJX1EBkdOnxIsZ2iczTOLulINyBVmLzBFG9Uic5zjibWAStQNKIEW4RTR8B4XjNCblLn74icnw97Qg/640?wx_fmt=png)

**杰克·威廉姆斯**（Jake Williams），安全公司Rendition InfoSec的创始人，Twitter上叫@MalwareJake，五万粉丝，圈内名人。白天教SANS的安全课程，晚上处理黑客入侵事件，标准的"数字消防员"。

2016年8月，他正带着团队驻扎在一个客户现场处理一起严重的安全事件，会议室改成了"作战室"，连轴转了好几天。

8月13日清晨，六点半到七点之间。他们正要出门，早餐买的是Sonic的早餐卷饼。

就在这时，公司安全运营中心（SOC）的同事在Twitter信息流上刷到了一条东西，赶紧通知他。

发帖的人，账号叫Shadow Brokers——影子经纪人。帖子是这么写的（原文是那种蹩脚的、明显不是英语母语的人写的英文）：

"我们跟踪了方程式组织的流量。我们找到了方程式组织。我们黑了方程式组织。我们发现他们有很多网络武器。看到图片了吗？我们免费送你们一些文件，这是证据。剩下的最好的文件——拍卖。"

影子经纪人声称：他们从NSA（具体说，是TAO）手里偷到了一批黑客武器，现在免费公开其中一件当"验货样品"，其余的拍卖。谁出价达到一百万比特币，全部打包公开。

杰克放下卷饼，下载了文件，看了一眼。

**JK**

JAKE WILLIAMS

*"我的天，这是真的。不是恶作剧，是真家伙。"*

那是一件针对思科和防火墙厂商Fortinet产品的漏洞利用工具——能拿下一台打满补丁、完全更新的防火墙。这意味着什么？意味着这个漏洞连厂商自己都不知道。这是一件 NSA 级别的、此前从未面世的攻击武器。

**JK**

JAKE WILLIAMS

"在不确认或否认的前提下，我只能说到这里——它看起来是合法的。"

思科和Fortinet随后都确认了：这是我们不知道的漏洞。补丁紧急发布。

但真正的问题才刚刚开始：影子经纪人是谁？他们手里还有多少？下一个被公开的，会是什么？

那场"拍卖"相当尴尬——头24小时，总共收到了937美元。离一百万比特币，差得有点远。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrr20pmmibOm8pHWoHsjWHHrhwfBX03cgQn9dvsRWjJQACQ4DrSUnd2N6ibdzPMnw3RJ4H3eBnBRk4HqaxlJzo3eLRBzFe1oC80yw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrpDbqBBPAiajLUfrOydCaTcWZWWtYQhODjTiaJiaTia4L5tb1GGuEvnl1wtZk77gnb0sbQmGSVB9RgFSa11ia89GibA8m4AmlVxmM5Bs/640?wx_fmt=png)

新闻炸开了锅。《卫报》、Wired、《纽约时报》全在报道：NSA的黑客工具被泄露了。

全世界都在猜：影子经纪人到底是谁？有人说是黑了NSA的反向操作；有人说是NSA黑客攻击别人时把工具落在了对方服务器上，被人捡走了；还有人说，是内鬼。

两个月后，2016年10月，美国副总统拜登上了NBC的《与媒体见面》节目，谈俄罗斯涉嫌干预美国大选。主持人问：你们会报复吗？

拜登说了一段意味深长的话：

**JB**

JOE BIDEN · 副总统

*"我们正在传递一个信息。我们有这个能力。会在我们选择的时机、以影响最大的方式进行。"*

**JC**

CHUCK TODD · 主持人

*"公众会知道吗？"*

**JB**

JOE BIDEN

*"我希望不会。"*

话音落下两周后，影子经纪人发了第二次倾倒。开场第一句：

"为什么那个肮脏的老爷爷要用CIA的网络战威胁俄罗斯？"

"肮脏的老爷爷"，指的就是拜登。

不过这第二次倾倒的内容倒不算劲爆——就是一大串IP地址，据称是NSA已经入侵过、或用作跳板的服务器清单。但这东西对安全圈反而是实打实的干货：把自己的网络流量记录翻出来，跟这份名单对一遍——如果对上了，恭喜你，你可能是NSA的目标。

杰克的团队也这么干了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrqAvz0aqBQePccQOH6tX9XSkVRrurZ96QiaOt20d0MibhvzLGiay6JR4GHfZqriaFkBvQLkmXHy0vYicPOFmyJhkuF8BXkwNy5ickBVs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrqQThthIOINCFAZb4nDZSiaUkgYllic2HkjZKcSGz1Y2kSkQOsE9b2o8aEIDibKGQMqAlvtLXT9DuxAriaPx0H3YooETIXh010ibKfs/640?wx_fmt=png)

2016年11月，美国大选，特朗普胜出。关于俄罗斯干预选举的舆论一浪高过一浪。

2017年1月，影子经纪人再次发帖，这次是一篇"告别信"：拍卖没拍到钱，那就算了，我们免费送——他们放出了61个Windows可执行文件、链接库和驱动程序，据称全部出自方程式组织之手，可以攻击Windows电脑。然后宣布：我们要转入暗处了。

这批东西里，藏着一个让整个取证行业脊背发凉的能力——**手术式篡改Windows事件日志**。

干这行的都知道，Windows事件日志相当于电脑的"案发记录"。教科书上写得明明白白：日志可以删，但只能全删，而且删的动作本身还会留下一条"日志被清空"的记录，等于案发现场留下一句"我来过"。想只删掉其中一两条？做不到。这是行业里近乎信仰的常识。

而TAO的这件工具，恰恰就是"手术刀"——想删哪条删哪条，删完不留任何痕迹。关掉日志、做坏事、再打开，中间那段空白干净得像什么都没发生过。

// OVERNIGHT

这个能力一直存在，圈内人也隐约知道谁有，但从来没有人见过实物。一夜之间，全世界都有了。

.

.

.

杰克后来写了博客，说了句分量很重的话：**"这对事件响应是彻头彻尾的游戏规则改变者。注意了。"**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrr1p0c6Aelj6V6Ju0iabFiawZ1RVgmlPcZlPUca4fO7mwcz4gArL6IicBg3L4AX5icJU7MT0eCxX1meDMFKIHFQ61aiaXx0Bj8r6cLk/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVroE4icHruSGmNZEsOuEC36QS3TUaWjZ3GhUnO7AvNOAad6s1okUGtMM9JKkicUa4hvVibQKetDxuLFTdOBncxhb0rib6PXY0YicuEzw/640?wx_fmt=png)

2017年4月，影子经纪人又冒头了，倾倒了更多工具，还给特朗普留了一段话：

"影子经纪人把票投给了你。影子经纪人支持你。但影子经纪人正在对你失去信心，特朗普先生。看起来你正在抛弃你的基本盘，抛弃这场运动，抛弃那些让你当选的人。"

.

.

.

这算什么？影子经纪人是特朗普粉丝？还是故意放的烟雾弹？没人说得清。

但杰克注意到了另一件事，并把它写进了博客：这些倾倒的时机，"太巧了"——每次都精准卡在俄罗斯因黑客行动被媒体围攻的节骨眼上。每次一倾倒，新闻焦点就从"俄罗斯黑客"变成了"天哪，NSA丢了工具"。这不像是为了钱，倒像是一场彻头彻尾的信息战。

这篇博客火了。被大量转发，还有媒体直接围绕他的分析写了报道："Rendition公司的杰克·威廉姆斯认为，这即使不是俄罗斯的行动，也是符合俄罗斯利益的行动。"

博客火了的第二天，杰克正在奥兰多教SANS的高级漏洞利用开发课程。他还发着烧。

早上醒来，手机通知一拉——**99+**。他的第一反应是：完了，我是不是发了什么惹众怒的推文，被网暴了。

然后他看清了内容，血液瞬间凉了半截。

影子经纪人，那个搅动整个安全圈的神秘组织，直接在Twitter上@了他：

@MalwareJake

“你作为一个前方程式组织成员，嘴巴真大。影子经纪人不习惯揭露方程式组织成员，但不得不为你这张大嘴破例。"

— Shadow Brokers

一句话，把杰克藏了将近二十年的身份，钉在了全世界的目光之下。

事实是——这是真的。杰克在政府情报界干了快二十年，其中大约五年，就在TAO。他从来没公开说过。LinkedIn上只写着"曾为国防部工作"，而安全圈里为国防部干过的人一抓一大把。他的朋友、家人、前同事之外，没有任何人知道：这个教课的讲师、发推的网红，是NSA精英黑客部队的前成员。

而影子经纪人不是猜的。杰克后来说：

**JB**

JAKE WILLIAMS

"我可以高度自信地说，他们百分之百不是在猜。他们把这事弄得一清二楚。

"至于他们怎么知道的——"我不能透露原因。"

**JB**

JOE BIDEN · 副总统

*"我们正在传递一个信息。我们有这个能力。会在我们选择的时机、以影响最大的方式进行。"*

更瘆人的是，那条信息还夹枪带棒地提到了一些词：某些"奇怪的任务"、CCI、Windows BITS持久化、Q Group。杰克被问起这些时，只回答了一句：

**JB**

JOE BIDEN · 副总统

*"我对这些无法做出任何安全的评论。"*

那段时间他怎么熬过来的？说来讽刺，是靠教书。SANS的课程从早上九点上到晚上七点，他说那是"被迫的分心"——没有时间反复琢磨，只能埋头干活。对一个刚被神秘组织当众扒皮的人来说，这大概是最好的止痛药。

但代价是真实的。他的商业搭档吓得连夜把那篇博客撤了下来，重写成一段没有任何实质内容的空话。他的威胁模型彻底变了：他给前妻打电话，给这个从没涉足过军队的女人上了一堂"这是俄罗斯情报机构"的速成课，然后问了一个让人心里发酸的问题——

"你还让我见孩子吗？如果你说不，我完全理解。"

之后的几个星期，他和孩子们只能视频通话，不敢见面。因为他不知道，也不可能有任何人知道——接下来会发生什么。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrruH9NPemUicpMWFJahozuvfwL1TD2icJSV7RtdkiaXwq1fmvEueI680kap8t8YicUnRugs0iba00kXynOTF9PS5rebOkNqa2Zlsr7U/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrr9TgDRRjlCib4FM8vHBXYa9vrnuMevMmO7La1NeCcx8YoWpKPAqJGvhic9tatzOy7RQI7TFzictaNhoibiaCicdwia6Gzh6gAqs6wzQE/640?wx_fmt=png)

就在点名杰克的推文几天后，影子经纪人放出了最后一批、也是最致命的一批工具。

里面有件东西，叫EternalBlue（永恒之蓝）。

它利用的是Windows上SMB协议的漏洞——SMB是每一台Windows电脑默认都开着的。换句话说，全世界上亿台Windows电脑，对这件武器门户大开。有人评价：EternalBlue可能会作为历史上最成功的黑客工具之一载入史册。

蹊跷的是，就在影子经纪人公开它的一个月前，微软悄悄发布了对应补丁。坊间传闻，NSA提前给微软递了话："这东西可能要流到街面上了，你们先准备着。"

这批倾倒里还包含了SWIFT银行系统的行动数据。杰克从中读出了更可怕的一层：影子经纪人手里握着的，不只是工具，还有行动数据——NSA实际干过什么的记录。

**JK**

JAKE WILLIAMS

*这告诉我，他们手里握着的，不只是工具，还有行动数据——NSA实际干过什么的记录。*

.

.

.

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrq5PJRQyosWPa9O5Hf9wYrNQKOCWI7ElpMGt4bpnRickcmcBpcNCA8gtzPLDarwGam3km8sZe2tOgSGOiaYpPFeY5Z1a5rJU4fP0/640?wx_fmt=png)

你大概听说过FBI的"十大通缉犯"，但你知道FBI还有一份"网络通缉名单"吗？名单上有11名为俄罗斯政府工作、涉嫌干预2016年大选的黑客，有4名对美国搞间谍活动的伊朗黑客。这些人只要踏上美国领土——甚至是与美国有引渡条约的国家——就可能被逮捕。

而被影子经纪人点名的杰克，现在站在一个前所未有的位置上：他代表美国攻击过谁，他比谁都清楚；而对方手里可能握着他当年行动的完整记录。哪天另一个国家也学美国起诉他国黑客——他会是第一批上名单的人吗？

**JK**

JAKE WILLIAMS

"我不是爱打赌的人，"他说，"但我无法想象我不会以某种方式被卷入其中。"

于是，2017年年中，他取消了去新加坡的行程。后来又陆续放弃了其他国际差事。每次出国前，他都要在脑子里过一遍：这个国家和那些国家有没有引渡条约？我降落之后，会不会直接被带走？

他提到了华为高管在加拿大机场被捕的事——"他们甚至还没过海关。"

**JK**

JAKE WILLIAMS

"我不会把自己扮演成受害者，"他说，"那些是我自己的职业决定，也正是这些决定让我走到了今天。但毫无疑问——他们手里有我的行动数据，那些东西完全可能以最糟糕的角度描绘我。而我，完全任由他们决定发布，或者不发布。"

这就是生活在"影子经纪人"阴影下的日子。

顺便一提：还有个叫哈罗德·马丁三世（Harold Martin III）的人，博思艾伦咨询公司的承包商，曾为NSA工作。此人从NSA的服务器上偷走了50TB的数据，成功带了出来，被抓，判了九年。时间线与影子经纪人的倾倒确实对得上——但始终没有过硬的证据把两者连在一起。没人知道那50TB里到底有什么，也没人知道他给了谁。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AjSHgfLXVrpoWzBtuZscYIBcoJO3FZMZaqMLs00ibaWiaicXpZYiciatbrQN7I32bW1HGAIEDKaTnHzSJxVqNJTbxbU5qpjobT15JDcZYia2ZIutY/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqTNPLWMWtBWXJvlqmvHPDQ160DZW9gGuhT6Kn9yzX8iaicS85Vmn8cBxicoBsodoOL4x8wia1wXy6sdRYhiblrmDDw6enA1yjjBNYs/640?wx_fmt=png)

把整件事摊开看，最值得琢磨的其实是这个问题——

NSA从没承认这些工具是他们造的，但所有证据都指向同一个结论：是真的。这意味着什么？意味着NSA养着一支研究队伍，专门在Windows这类软件里找漏洞，找到了，不告诉厂商，捂在自己手里当武器。

NSA公开说过自己不"囤积零日漏洞"。可影子经纪人的倾倒就是一记响亮的耳光：他们不但囤，而且囤了这么多年。

// THE CORE QUESTION

进攻和防守，NSA选了进攻。如果他们真以防御为先，发现漏洞...