---
title: 一个人开发的冷门App 有人用智能眼镜对着你手机会先叫
url: https://mp.weixin.qq.com/s/8pKreixPxCcKu1TJPjxZMA
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:02:06.801758
---

# 一个人开发的冷门App 有人用智能眼镜对着你手机会先叫

# 一个人开发的冷门App 有人用智能眼镜对着你手机会先叫

原创

紫禁
紫禁

紫禁玄科

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

SECURITY · INTELLIGENCE

# 一个人开发的冷门App 有人用智能眼镜对着你手机会先叫

2026年10月09日 · 8 min

#网络安全#开源工具#隐私保护#挖宝日记

01

周四晚上翻仓库，翻到一块被埋没的护身符

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ah5NAr7MJFgNSiaaQo6uBrazuC55vvtFShGq9oLqMybohTJ2ia3Xy4pLCda6slFjKGriavP1KuMYZibUlzKBSZW67icjmvkEao4KCXQbq9S9icVas/640?from=appmsg)

挖到一块被埋没的隐私护身符：会报警的手机哨兵

我有个雷打不动的习惯：睡前刷一遍 GitHub，像逛旧货摊，专挑那些两三千星、不上不下的仓库翻。星太多的都是通货，星太少的多半没打磨完。周四晚上照例翻到一个 2452 颗星的安卓项目，本想划走，结果它的 README 第一屏就把我钉住了——两行全大写的警告，第一行说「有人因为你怀疑他戴了偷录设备就去骚扰他，这本身可能构成犯罪」，第二行只有四个词：永远不要骚扰任何人。

一个教你「防偷拍」的工具，开篇先教你「别去冤枉人」。这行字让我决定把整个仓库挖到底。挖完之后我得说：这是最近三个月我挖到的、最被低估的一块护身符——它叫 **Nearby Glasses**，一个业余开发者写的手机 App，功能只有一件事：**如果附近有人戴着会录像的智能眼镜，你的手机会先叫**。

02

Nearby Glasses：一个人业余写的手机哨兵

先交代这块「宝贝」的来历。作者 Yves Jeanrenaud 在 README 里自述「我不是科班出身的开发者，这些都是业余时间自学着写的」，语气诚恳到有点卑微。项目 2026 年 2 月才建仓，到现在两千四百多颗星，安卓和 iOS 双端都有，Google Play、App Store、IzzyOnDroid、Obtainium 都能装，嫌商店不干净的可以下 APK 自己编译——它是 AGPL 协议开源，代码完全摊开给你看。

它的工作状态非常「金丝雀」：图标是一只小鸟，安静的时候小鸟站在那儿，说明附近没有检测到可疑设备；一旦报警，小鸟缩起翅膀躲起来，配合一条系统通知。所以这个模式就叫金丝雀模式——老矿工下井带金丝雀，鸟不叫就还有气，鸟一叫就得撤。通知冷却默认 10 秒，不会把你震到手麻。界面还带中文，对国内用户几乎没有门槛。

最让我舒服的是它的克制：不收集任何个人信息、没有遥测、没有广告，日志只存在你自己手机里，导不导出全凭自愿，而且日志里只有一串串厂商代码。一个「防隐私侵犯」的工具自己先做到不侵犯隐私，这在同类 App 里是稀有品质。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ah5NAr7MJFjRDOIiaqSg9fCmpibMCIbRLwDHCViaDNFOibdyA5dsrZx8sEdUcSX5Xfkl9ZmutjBVQqkCRtpmf8iaZXKLoXdeJHlrNdUm1iaETlGeI/640?from=appmsg)

挖宝第一课：先分清哪块是真货，哪块是蹭名字的

03

好东西为什么被埋没：名字先被蹭名的盯上了

这么实用的东西，为什么才两千星出头？我翻到 README 里第二处警告时就明白了——**它被蹭名字的盯上了**。作者用一整段红字声明：一个叫 nearby-glasses-alert.pages.dev 的网站跟本项目毫无关系；Google Play 和 App Store 里还有一堆长得像、甚至同名的 App，「它们看起来在劫持这个名字赚快钱」，既不遵守 AGPL 协议，也跟作者没有任何关系。

翻译一下这个局面：真正免费开源、不收集数据的那个，被一群收割流量的仿冒品围在中间。普通用户一搜「nearby glasses」，先跳出来的很可能是山寨货，轻则看广告，重则反过来收集你的位置和蓝牙扫描记录——防偷拍的工具成了偷数据的工具，没有比这更讽刺的了。所以我把「验明正身」做成了本文第一个动手环节，见后文。

被埋没还有两个原因。一是题材微妙：检测「别人的眼镜」天然带着冲突感，作者怕被人拿去当「抓间谍」的令箭，反反复复在文档里劝你冷静；二是他压根没做营销，没有产品官网，没有刷榜，连截图都是自己画的金丝雀。这样的项目就像旧货摊角落里的东西，得蹲下来才看得见。

04

我把它怎么认眼镜的逻辑翻了个底朝天

技术人看到「能检测智能眼镜」的第一反应都是：凭什么？作者没有藏私，README 里把试错过程写得很清楚。难点在于：蓝牙 LE 的 MAC 地址是随机的，服务 UUID 也不稳定，大厂还用私有协议——想稳定认出「这是一副眼镜」，常规路子全堵死。最后能落地的方案来自蓝牙技术联盟的厂商注册表：**每一台蓝牙设备的广播帧里都带一个不可更改的厂商编号**。

比如 Meta 系设备的编号是 0x01AB 和 0x058E，给 Meta 代工雷朋眼镜的陆逊梯卡是 0x0D53，做 Snap 眼镜的 Snapchat 是 0x03C2，还有珠海杰理 0x05D6（不少白牌智能眼镜用它家方案）。App 后台扫到这些编号，再叠加设备名特征（rayban、HeyCyan 这类）和一个固定的服务 UUID，命中且信号够近就报警。默认的「够近」门槛是 RSSI 不高于 -75 dBm，大致相当于中等距离。

顺带说个作者自己承认的短板：同样带这些编号的还有 VR 头显等设备，所以误报不可避免——对面那哥们可能只是戴着 Meta 的 VR 头盔。也因此 App 的每次报警都只是一句「附近可能有」，剩下的判断留给人。这种把不确定性明说的做法，比那些张口就「100% 精准检测」的收费 App 诚实太多。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ah5NAr7MJFjwHHVjjQiabQJ2B7Slhhap0PWpYRMTLQUa8MTnibTj5UDdTpsscIeia24JQnvIaGjKju3EXvtNUibJJ10hbuiadnBn9bqJBhnmk8ic4/640?from=appmsg)

蓝牙广播里的厂商编号，就是它认出眼镜的依据

05

作者自己泼的冷水，比功能更打动我

翻到 README 的「Tech-Solutionism?」一节，我有点意外。作者写道：「我知道这是在用技术方案解决一个由技术放大的社会问题，我不想鼓吹技术万能，也不想给人虚假的安全感。这个方案不完美，可能永远都不完美。」他还列了五篇新闻报道说明自己为什么写这个 App：有执法人员用智能眼镜偷录执法过程，有按摩店员工被眼镜用户拍摄骚扰，录制指示灯厂商说不可关但被人轻松关掉，有人给眼镜装上人脸识别当场「开盒」路人，还有媒体预言厂商要把人脸识别做成出厂功能。

说实话，我见过太多把「保护你」写成营销话术的项目，反而是这种把「我保护不了你全部」写在最前面的，让我愿意信任。

06

动手一：装之前先验明正身，别把山寨货请进门

前面说了山寨横行，所以动手第一步不是安装，是验货。下面这段脚本只读公开信息：核对官方仓库的协议、星标和最近推送时间，再把名字带 nearby glasses 的仓库全搜出来，逐个跟官方对照。我实跑了一遍，结果比预想的还热闹——

verify\_source.py — 仓库验明正身（Python，只读）

# verify\_source.py — 装之前先验明正身（只读，stdlib）

import json, urllib.request, datetime

def now():

　　return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def gh(path):

　　req = urllib.request.Request(

　　　　"https://api.github.com" + path,

　　　　headers={"User-Agent": "verify-script",

　　　　　　　　"Accept": "application/vnd.github+json"})

　　with urllib.request.urlopen(req, timeout=15) as r:

　　　　return json.loads(r.read().decode("utf-8"))

OFFICIAL = "yjeanrenaud/yj\_nearbyglasses"

info = gh("/repos/" + OFFICIAL)

print(f"[{now()}] 官方仓库: {OFFICIAL}")

print(f"[{now()}] 协议 {info['license']['spdx\_id']} | 星标 {info['stargazers\_count']}"

　　　f" | 最近推送 {info['pushed\_at'][:10]}")

data = gh("/search/repositories?q=nearby+glasses+in:name&per\_page=10")

print(f"[{now()}] 名字带 nearby glasses 的仓库共 {data['total\_count']} 个，逐个核对：")

for it in data["items"]:

　　mark = "官方" if it["full\_name"] == OFFICIAL else "!! 疑似蹭名，认准作者 yjeanrenaud"

　　print(f"[{now()}]  {it['full\_name']:<44} {mark}")

print(f"[{now()}] 提醒：应用商店里的同名 App 也要对包名 ch.pocketpc.nearbyglasses")

实测输出（节选）：官方仓库协议 AGPL-3.0、星标 2452、最近推送 2026-09-24；而名字带 nearby glasses 的仓库一共 3 个，除了官方那个，另外两个都会被标成「疑似蹭名」。手机端同理：装之前对一眼包名 **ch.pocketpc.nearbyglasses**，对不上的直接放弃。防偷拍的第一课，是先防住「防偷拍」的骗子。

07

动手二：看懂 RSSI，才知道报警离你多远

报警响不响，取决于一个叫 RSSI 的信号强度值。作者给的经验对照是：-60 dBm 大约 1 到 3 米，-70 约 3 到 10 米，-80 约 10 到 20 米，-90 开始就是 20 米开外了。想自己换算的话，用对数距离模型就能估个量级，下面这段离线脚本把默认报警线前后各档距离都算给你看：

rssi\_dist.py — 信号强度换算距离（Python，离线）

# rssi\_dist.py — 把信号强度换算成大概距离（离线，stdlib）

import math, datetime

def now():

　　return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 对数距离路径损耗模型：RSSI ≈ -10 \* n \* log10(d) + C

# n=2.3、C=-54 为按官方 RSSI 对照表拟合的室内经验值

N, C = 2.3, -54.0

def est(rssi):

　　return 10 \*\* ((C - rssi) / (10 \* N))

print(f"[{now()}] RSSI -> 距离估算（n={N}, C={C}，仅供量级参考）")

for rssi in (-60, -70, -75, -80, -90, -100):

　　note = "默认报警线" if rssi == -75 else ""

　　print(f"[{now()}]  {rssi:5d} dBm  ≈  {est(rssi):6.1f} 米   {note}")

print(f"[{now()}] 墙体、人体、设备朝向都会拉低信号，别拿这个数字去指认谁")

实测输出：-75 dBm（默认报警线）约合 8 米出头，-90 dBm 就退到 36 米开外。这里必须泼一瓢冷水：墙、人体、甚至手机朝向都会让信号衰减，这个数字只能帮你判断「大概在哪个量级」，不能当证据用。真要留证，走正规渠道，别拿一张截图去指认谁。

08

用它的四条边界，和三句大实话

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ah5NAr7MJFhibSx1HywoBOotPgpafcFKSFoZvb6wQ3ibs3icVzbrTMpud89X31NXOOu4n6ZHUY9eicWPNqI3tgtdRZ4NxU5aTrZ4vc4Sw8yb574/640?from=appmsg)

从扫描到冷静处理，一次预警的完整流程

把这款 App 装进手机只是开始，怎么用才不惹祸，我总结了四条边界：

1. **报警只是「可能」**：VR 头显、同厂其他蓝牙设备都会触发，先提醒自己冷静，再观察环境

2. **永远不要上前质问或围堵**：作者在 README 里用全大写强调过，这可能比戴眼镜本身更严重

3. **日志自己留好，别乱传**：导出的记录含周边设备信息，发到群里之前想想给别人留了什么

4. **iOS 用户只有金丝雀模式**：系统限制导致后台常驻扫描不可用，安卓才能收到系统通知

三句大实话收尾。第一句：这是个哨兵，不是保镖，它替你放哨，但替你做不了决定。第二句：真正的安全感来自「知道自己身处什么环境」，一款免费开源、不收你数据的小工具，愿意把误报率和局限性都摊开写，这份坦荡本身就是稀缺品。第三句：如果你常去展会、酒吧、密室这类人多的场合，或者工作内容敏感，装它花不了十分钟，比事后追悔划算得多。

挖宝日记写到这儿。这块护身符两千四百颗星，作者还在提交代码，金丝雀还在笼子里站着。觉得有用，把这篇转给那个常跑线下活动、又爱较真的朋友。我们下期接着挖。

觉得有用？点个「在看」让更多人看到

紫禁玄科

专注网络安全 · 深度分析

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ah5NAr7MJFgsJVJaWtQWT91yiaiamRUadMsnMic0LbgkAdUkYst4Ziaz6lclmn95ickibdZxnp72aTaJuXKjZvMYmeobnPyQpN7LeuZhOHpKqXOV0/0?wx_fmt=png)

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