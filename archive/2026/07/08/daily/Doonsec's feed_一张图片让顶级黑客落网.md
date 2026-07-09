---
title: 一张图片让顶级黑客落网
url: https://mp.weixin.qq.com/s/r21jVxC2HJNis3DJelBeow
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:59:51.262813
---

# 一张图片让顶级黑客落网

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PwKqX7Pibn2EnnulrbsQP4XEmaYTYQJgfRemkeEoricku0QwQbUmZWicXcECus27t0MwsFL0Mp58L9CAyjSUFoufZteDVwATpQUA/0?wx_fmt=jpeg)

# 一张图片让顶级黑客落网

原创

Ben Chen
Ben Chen

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PEtrnib92D2oK87RibXnQvpZCZAkK3atZrcptiahK7489EsepicU8jY03gBQqJmM9H50cKQRKIY72vFj6hjQLAHDmMSOQic6mQ150A/640?wx_fmt=png)
> **导语**：2026年4月10日，19岁的彼得·斯托克斯在芬兰机场准备登机飞往日本，兜里揣着两块2TB硬盘。他以为自己用了VPN、换了MAC地址、请了"私人助理"接打电话，社会工程学玩得滴水不漏——FBI却早已在他Windows电脑里那个从不公开的设备标识符上，静静等着他露出马脚。

---

## 一、机场抓人，硬盘里有什么？

2026年4月10日，芬兰赫尔辛基机场。一个19岁的美国和爱沙尼亚双重国籍青年正准备登上飞往日本的航班，被当地警方当场拦下。他叫**彼得·斯托克斯**（Peter Stokes），这个名字在网络安全圈并不陌生——他被指控是黑客组织**分散蜘蛛**（Scattered Spider，又名Octo Tempest）的核心成员。

美国伊利诺伊州北区地方法院随后解封了一份**35页的刑事起诉书**，内容之详尽，让所有安全研究员倒吸一口凉气。这不是一份泛泛的指控文件——这是一份由FBI电子取证专家亲笔写就的**完整攻击复盘报告**，每一步操作、每一个时间戳、每一条日志，全部记录在案。

起诉书显示，分散蜘蛛被指控涉嫌**100多起网络入侵**，与超过**1亿美元赎金支付**直接相关。

---

## 二、一通电话打穿价值数十亿美元的零售防线

### 2.1 攻击起点：社工电话，而非恶意软件

2025年5月12日，分散蜘蛛对一家**奢侈品珠宝零售商**（起诉书将其匿名为"公司F"）发动了攻击。攻击链的起点出人意料——不是漏洞利用，不是钓鱼邮件，而是一通电话。

攻击者使用两个**Google Voice号码**打给公司F的IT服务台，冒充员工要求重置凭证：密码和用于多因素认证的移动设备。**2到3小时后，三个用户账户沦陷，其中包括两个IT管理员账户。**

这就是社会工程学的可怕之处：**没有恶意代码，没有漏洞利用，每一道门打开时，拿的都是合法钥匙。** 认证成功了，安全日志 wave them through。

![分散蜘蛛攻击链](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N9nupugNaGqza2eV8u1PibrrOF72X3wWWtOuD91ObiczgrtCC2xIbyH10HmiaPMPhCw1lk60V9w7eFg39PeNia3A74KgXuKGY3dXo/640?wx_fmt=png "分散蜘蛛攻击链")

### 2.2 横向移动：用合法工具干脏活

拿下管理员账户后，攻击者没有停下来。他们用这些合法凭证进一步提权，获取了公司F虚拟服务器和云计算平台的控制权。

然后，他们安装了两样东西：

* **ngrok**：一个合法的开发者工具，可以从私有网络内部建立到互联网的安全隧道，正规安全产品，完美穿透边界防御
* **Teleport.sh**：另一个合法远程访问工具，结合**Amazon S3**存储进行数据外泄

三天时间，外泄数据量：**至少77GB**。

### 2.3 勒索未遂

攻击者试图在最后阶段投放勒索软件，但公司F的安全团队及时发现并驱逐了他们。数据已经被拿走了。5月15日，攻击者从一个已攻陷的邮箱发出勒索函，主题："IMPORTANT: WE STOLE THE DATA, CONTACT UMMEDIATELY"（大意：我们偷了数据，立即联系我们）。赎金开价：**800万美元**。公司F拒绝支付。实际的业务中断和修复损失约**200万美元**。

---

## 三、分散蜘蛛：一个品牌，多个运营商

### 3.1 真实成员档案

斯托克斯只是这个组织曝光的冰山一角。这份起诉书里还有更多名字：

* **诺亚·乌尔班**（Noah Urban），代号"Sosa"和"King Bob"：因SIM卡交换攻击被判处**120个月**监禁
* **塔尔哈·朱拜尔**（Thalha Jubair）和**欧文·弗劳尔斯**（Owen Flowers）：2026年6月在伦敦当庭认罪，涉及2024年8月对伦敦交通系统的攻击，导致交通瘫痪
* **泰勒·布坎南**（Tyler "Tylerb" Buchanan）：2026年4月认罪

### 3.2 DragonForce：勒索软件即服务生态

调查人员在斯托克斯的服务器上还发现了**DragonForce**的聊天记录——这是一个勒索软件即服务（RaaS）品牌， affiliates可以租用代码和基础设施来运营自己的攻击。起诉书中记载了这样一段对话：一个affiliates抱怨被收取500美元新登录费，并反驳"我们给你们创造了超过100万美元的收益"。

**品牌年年换，行为模式不变。**

---

## 四、真正让黑客落网的：那个Windows从不告诉你的GDID

### 4.1 什么是GDID？

这是整个故事最硬核的部分。

**GDID（Global Device Identifier，全局设备标识符）** 是微软在Windows生态中设计的一个持久性设备级标识符，用于唯一标识一台Windows设备——无论物理机还是虚拟机——在特定微软服务和场景下的身份。

根据起诉书陈述，微软代表如此定义：

> "Windows生态中的全局设备标识符，是一种持久性、设备级别的标识符，旨在跨特定微软服务唯一定位一台Windows操作系统安装实例。"

翻译成人话：**你每次联网，微软就知道是你。**

**![图像](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PJoJvtKFGhm90sSkpls22jLQicOTU8Ihpm8YLuadickxDDmyw41ibLfwbtkQcLPX2dcCcaAEf7pKT1ibDgkcfiaUplOVYZvfzLeVicM/640?wx_fmt=jpeg&from=appmsg)**

### 4.2 为什么换了VPN和MAC地址还是没用？

斯托克斯在攻击时使用了**Tzulo托管服务商的代理IP**，以为自己万无一失。确实，VPN隐藏了单一连接——但FBI的思路根本不是追单一IP。

他们的方法是：**把微软手里的GDID活动记录，与已经关联到斯托克斯本人的其他账号IP历史进行交叉比对。**

![FBI跨平台取证分析：GDID与社交账号IP交叉碰撞](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MaAFvlvWnhfJq3VvV2AjERjf73lL2aaU7SZMCibJYsvVhbRu9EOV6gI6hXavHSRQF9mRen3I3C3x4btyd2D16LrA8lBsRlrGFs/640?wx_fmt=png "FBI跨平台取证分析：GDID与社交账号IP交叉碰撞")

具体来说，FBI已经通过以下渠道关联到斯托克斯本人：

* **Snapchat和Facebook照片**：定位到他在巴黎、纽约、曼谷、迪拜的行程，入住豪华酒店，手持现金和名表，脖子上戴着一条写有"HACK THE PLANET"字样的钻石项链
* **生日消息**：他在生日当天发消息吹嘘自己刚拉了一个包含电汇数据的数据库，而这条消息的发送日期与他在美国国务院记录中的出生日期完全一致
* **游戏账号**：2025年1月8日，同一IP地址在两分钟内先后访问了他的Apple账户、Ubisoft账户和游戏Growtopia账号

这些信号单独看都是噪音。**但当它们在时间、空间、行为上反复交叉重合，就形成了一张无法抵赖的画像。**

### 4.3 关键铁证：GDID编号6755467234350028

起诉书第9页披露了最核心的技术细节。2025年5月12日19:21 UTC，那台绑定了GDID **6755467234350028**的电脑除了入侵公司F系统外，还访问了ngrok的注册页面：

> "https://dashboard.ngrok.com/signup"（ngrok账户注册页面）

此外，微软日志还显示该GDID从Tzulo服务器访问了"多个站点"，与攻击基础设施相关联。

**一个数字，串起攻击行为和真实身份。**

---

## 五、GDID暴露的隐私陷阱：Windows是监控软件？

### 5.1 DiagTrack：永不断线的回传链路

GDID的幕后是Windows的**DiagTrack服务**（即"连接的用户体验和遥测"服务）。正是这个后台进程，源源不断地将设备唯一标识符日志回传给微软云端。用户毫不知情，也无处可逃。

安全专家**马修·希科**直接在推特上开炮：**"Microsoft Windows就是监控软件。"**

### 5.2 重装系统能摆脱GDID吗？

根据微软官方文档，GDID在系统更新后保持一致，但重新安装Windows后会生成新的唯一GDID。然而问题来了：

> "因此，一个微软用户可能有多个GDID。"

但安全社区已经指出：微软完全有能力通过其他标识符——如**微软账户登录、IP地址**——将新GDID与旧GDID进行关联。重新安装系统不过是换了个马甲，背后的数据画像早已成型。

### 5.3 苹果是否同样存在这个问题？

安全研究员**科斯汀·劳**在"三好友问题"播客中提出：

> "我想问的是：苹果设备上有同样级别的情况吗？是否更严重——它们是否绑定到硬件层面，以至于你重装系统也没用，因为它基于硬件？很可能不只是微软一家。但如果你想真正匿名，可能最终需要用Linux、FreeBSD之类，然后通过代理、VPN、Tor传输所有流量。"

---

## 六、红队视角：这个案子的真正警示

### 6.1 攻击者视角

分散蜘蛛的战术代表了一种成熟的攻击范式：

1. **社工电话开局**：绕过所有技术防线，用人性弱点直接撬门
2. **MFA重置接管身份**：即使是企业级安全环境，客服重置流程依然是软肋
3. **合法工具隐蔽渗透**：ngrok、Teleport、S3，这些工具不触发任何告警
4. **VPN+代理基础设施**：单点来看完全无法追溯

但这个案子的真正教训是：**就算每一步都做对了，操作系统层面的遥测数据会在你不知情的情况下，把你所有数字身份关联在一起。**

### 6.2 防御者视角

对于防守方，这个案子有几处值得深思：

* **MFA重置流程是致命盲区**：攻击者拿到的不只是密码，而是一枚全新的合法MFA令牌。传统的MFA控制在这个环节完全失效
* **行为基线比签名更重要**：ngrok隧道、S3大量上传，这些行为单独看都"正常"，但第一次出现时\_CONTEXT才是一切
* **隐私和安全的双刃剑**：GDID既是对抗网络犯罪的利器，也是悬在所有Windows用户头顶的隐私隐患——微软从未公开宣传过这个标识符的存在

---

## 七、总结

彼得·斯托克斯案是网络安全史上一个标志性节点。它证明了两件事：

**第一，社会工程学依然是入侵企业最有效的路径。** 一通电话、两次重置、三小时内拿到管理员权限——不需要零日，不需要恶意软件。

**第二，操作系统层面的遥测数据，已经成为数字取证的核心战场。** GDID这类隐藏标识符，让执法机构具备了绕过传统网络追踪手段的能力。而当这种能力曝光，也在安全社区引发了一场关于隐私边界的激烈争论。

对于普通用户，结论很残酷：**你对自己的设备没有你想象的那么多隐私权。** 对于安全从业者，这个案子的启示同样清晰——攻击者已经足够了解防守方的盲区，而防守方也必须开始关注那些自己从未留意的系统底层数据。

**条条大路通shell，但在你通往目标的每一步路上，可能都有一条你根本不知道存在的遥测链路，在同时记录着你。**

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Puc8HNiaVFMibMWyXuRCjam9iat0x1rCpsp1iatD7HveaKn7X0FMG8AlYEYZQbWQjAzjbYJjgdDQYTxLsn3W66vehH9V8LV2z9XnE/640?wx_fmt=jpeg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NJaWlOgGNt6DbZUibIWJ1CIhPX5Be64ePAYnHxT3Q4ThVqTKzMNiaQAYEjNaDlY9AthbLcIsrN4kPU1dqTEyiaAr3nialmYqMQh9o/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618755&idx=1&sn=48e0a85464fb20c73b6f338928a8f850&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PKBzibJnbda0CMK3x60eudMe9sX2keic0hP6ibj4r1vchm8wLibbC2LvvlTBXKJbfDqhJQQKCpqDeWnsEoxndVribgNu4ZZGlZ5KEw/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618776&idx=2&sn=a8fc65fd2a71822830022fc52d967bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M31JAE8U9E4F6SwkHX5V8dmziavPTqVQc7JdOHLa6PRExE28VUOIRk770kATgFwwvMibngxp6OBwXhjHATN3lVheGl5dVrSiaVa4/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618496&idx=1&sn=96ecdff99136258a4bf2cb156542311e&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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