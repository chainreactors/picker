---
title: 裸辞已是背水一战，一份高薪offer却险些让我坠入深渊
url: https://mp.weixin.qq.com/s/Bx_-nLv2zU7i1IU8pr4VcA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:59:19.101702
---

# 裸辞已是背水一战，一份高薪offer却险些让我坠入深渊

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe0WY1EbXMh2xflM60fTiaqO9ssRu4Xvib5zCu4fbWicalNZZdJ8RgicdthN3OBPsnmDmrKia7COKIX1FV1Sujh69oPbGzibicPuy8abX8/0?wx_fmt=jpeg)

# 裸辞已是背水一战，一份高薪offer却险些让我坠入深渊

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 裸辞已是背水一战，一份高薪offer却险些让我坠入深渊

## 摘要

薪资腰斩后毅然裸辞，本以为拿到一份月薪过万的高薪offer，就能从职场低谷翻身。谁知这份看似完美的面试邀请，却是一场精心设计的电信诈骗圈套。从“试岗培训”到引导安装“拓途办公”App，背后的恶意软件竟能拦截电话、删除通话记录、窃取隐私。本文以亲身经历揭开骗局全流程，结合专业逆向分析报告，带你看清高薪招聘里的“杀猪盘”套路。

---

## 一、裸辞那一刻，我赌上了所有退路

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0zez0BNMVj1Urw5lVAgq9heqFzHXQ47sPxiavicRJU0Qo8Xl1s0KG7icicjJLEmSv95cHINVUiaShtpiaJpNR7UdYic2meAwjHEK4CfU/640?wx_fmt=png&from=appmsg)

“月薪直接砍半，你接受吗？”领导在会议桌对面问我。

我没犹豫，当天就提了离职。与其被羞辱式降薪困死在工位上，不如背水一战。裸辞后的头两周，我疯狂投简历、刷招聘软件，每一次消息通知都像一根救命稻草。

就在积蓄见底、焦虑达到顶点的时候，一封极其正式的《面试邀请函》跳进了邮箱。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2adDXsJdMhzEia0yyys155hDxfWdqUM9GEcbEsicNBhZrv618hKyteo0XnicFz5hShYRxfBOyJra9cicb3ZXs5RKeyue7Wa3WQcVU/640?wx_fmt=png&from=appmsg)

“项目管理工程师，试用期无责任底薪9000元，转正月薪13000元+，季度绩效最高2万元，首年13薪，五险一金入职就交，公积金按12%顶格缴纳。”

那一刻我甚至有点想哭——终于有人识货了。

## 二、完美得不像话的 offer

发来邀请的是“成都德嘉伟业建筑工程有限公司”，说是某大集团下设子公司，总部在北京，全国几十家分公司，业务覆盖互联网、房地产、电子商务等。面试流程也显得很正规：先线上测试，试岗培训两天，再办理入职。

公司还特意强调福利：每月600元住房补贴、300元全勤奖、包中晚两餐、提供集体宿舍，连生日礼金、结婚礼金、生育礼金都给你安排得明明白白。

唯一让我感到奇怪的是，邀请函末尾说培训全程手机操作，无需电脑，叫作“便携办公培训”。但转念一想，可能现在移动办公是趋势吧，我甚至已经开始盘算第一个月工资怎么花了。

## 三、“请回复：同意+手机系统”

所有疑虑都在高薪面前烟消云散。我按照要求回复了“同意+安卓”。

人事很快发来一张《安卓用户下载指南》。

图片做得还挺像样，要求我先保存二维码，用手机自带浏览器扫码下载，然后注册账号发给HR。App名字叫“拓途办公”，示例账号格式是字母加数字，比如 CYH6688，连邀请码都不用填。

此时我突然闪过一个念头：为什么入职流程要通过一个从没听说过的App进行？为什么不能直接在招聘平台完成？为什么要特意强调用手机浏览器扫码，绕过应用商店？

我决定先搜一搜这个公司的背景信息。一搜吓一跳——几乎查不到任何有效评价，所谓的总部办公地点是个注册地址，并且关联着多个名称不同的空壳公司。

## 四、揭开“拓途办公”的真面目

我把那张下载指南和之前怀疑的细节，发给做网络安全的朋友。

他丢回给我一份深度逆向分析报告，文件名是“TTs388eBG660.apk”，分析工具是 IDA Pro，逐行代码反汇编，看得我冷汗直流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe3oPkB0cWkWetFIwiauCUMhFpxjCfy4WFxhOP2Sdiaekn21R8uHI5WHUGLNWa0VwKVZqf4UUHRVsGoia5ibGJ9GhOC9ibT374WlYFibY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe26gVk3kqNQN92kfdb2Ax0HOyAia06HiaoygBxywMDqA97UwqWvcibiaoZHAiaaTzFXuk7Fh0hHgAQzxogyeUC9OmrBRsUxqOzibEA40/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1U1sGWELZibOvSUT3F4iaJHDNGB1l55s4icw70V6g3agtYpGnayw3bJwIgHH0t5ibbevtNMV1yPOgrJbEbfKBbnWniaAFcpwmD7zpI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe30YtWUvJq8J5TIYBFZ0Qq7L9VKl2wXT6QeBC6am2FRCz1aicWEt4CTTFPa6tWXtbNpXhaTogDiaDmYs2VQVTgCC4VoTjFZF2Jso/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0tvvYKQ80IkGDV29jgzqXCF0wyoB2IibA95icVLUBJPDTBH11ibyCcDtKxoY5KYibmHbAUbpllIuqXr159nBhVMP9eT14s0ePumOo/640?wx_fmt=png&from=appmsg)

报告显示，这个 App 是一个**电话拦截木马+间谍软件**，威胁等级标注为“极高危”。

它的核心恶意功能包括：

* • **来电拦截与自动挂断**：通过监听电话状态，一旦发现特定号码来电，就用系统底层接口自动挂断，让你根本接不到银行的确认电话、反诈中心的预警电话。
* • **删除通话记录**：挂完电话后立即调用 `ContentResolver.delete` 删除通话记录，手法干净利落，被拦截的人甚至不知道电话曾经响过。
* • **窃取隐私并上传**：收集你的IMEI、精确位置、通讯录，打包后通过 AES 加密上传到远程服务器。加密密钥被硬编码在代码里，密钥是 `asdfwetyhjuytrfd`，IV 向量是 `16-Bytes--String`，任何拿到这份报告的人都能解密。
* • **黑名单管理**：骗子可以远程动态更新黑名单号码，比如把银行客服、96110、家人朋友的号码加进去，让你彻底被信息隔离。

朋友说，这个 App 的包名是 `com.ddtx.app1.cailiao`，主服务名叫 `PhoneIntercepterService`，里面还有专门的黑名单管理界面。一旦安装并授予权限，你的手机就完全处于骗子控制之下。

## 五、“试岗培训”其实是洗脑+收割

看到这份报告，我终于明白那个所谓的“两天试岗培训”是什么了。

**第一天“员工测试”**：给你4道测试题，让你花60到90分钟去完成。实际上是让你在他们的App里做任务、垫付资金，小额返利让你尝到甜头，逐步上钩。

**第二天“岗前培训”**：上午让你满勤，下午进行“薪资制度、规章制度”培训。实际上就是进一步对你洗脑，让你相信这是一份正经工作，同时利用已经窃取到的通讯录和位置信息，编织更精准的诈骗剧本。

到这一步，骗子手里的牌已经足够多了：你的身份证信息（入职时提供）、你父母的电话（通讯录窃取）、你的实时位置，还有你被锁死的手机。只要他们愿意，可以随时让你的手机变成一座孤岛，然后冒充你向你的家人要钱，或者直接转走你银行卡里的余额。

## 六、我活下来了，但一定有人正在被骗

我算幸运的。在回复“同意”之后、在下载那个App之前，我犹豫了，选择了去核实。

但如果再往前错一步呢？

如果我已经安装了“拓途办公”，并开始“试岗任务”垫付了几千块钱呢？如果我因为焦虑和侥幸心理，继续往那个无底洞里投钱呢？

骗子的剧本完美拿捏了求职者的心理：你正身处低谷，渴望认可，急需一个翻身机会；他们就用远超市场价的薪资、堆砌到夸张的福利、专业感十足的流程，一步步把你拖进陷阱。

而被骗的往往不是一个人，而是他背后的整个家庭。

## 七、写在最后：天上掉的不是馅饼，是陷阱

如果你也正在求职，请一定记住这几条保命法则：

1. 1. **所有要求下载陌生App、先垫钱“做任务”的工作，100%是诈骗。** 不管它包装得多么正式。
2. 2. **正规公司不会让你绕过应用商店下载软件。** 更不会问你用的是苹果还是安卓，然后给你发奇怪的二维码。
3. 3. **福利好到离谱的岗位，往往就是坑。** 试用期9000、转正13000还包吃住、12%公积金，这些词堆在一起就是为了让你脑子发热。
4. 4. **先查公司背景再心动。** 天眼查、企查查、招聘平台的评价区，花十分钟能救你一整个身家。

薪资腰斩裸辞，是我为尊严做的一赌。但差点被骗子当成“一盘菜”，是我这辈子最惊悚的一课。

幸好，最后的结局不是“我被骗了”，而是“我识破了”。

希望读到这里的你，永远不要成为骗子的下一盘菜。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe1vZxRk8oIewqmmhpzMrbTcvYzicD7ZghaYG3VqRgok2VAeqsyxTpUibtHujmdiaH6doHochr0AApIptibCKnvVibLxBVjywADok4rI/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

利刃信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

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