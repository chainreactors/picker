---
title: 看不见的车上乘客：安卓车机正悄悄沦为僵尸网络节点
url: https://mp.weixin.qq.com/s/rOfOALsb6NBCTNqSHJL--w
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:55:53.248638
---

# 看不见的车上乘客：安卓车机正悄悄沦为僵尸网络节点

# 看不见的车上乘客：安卓车机正悄悄沦为僵尸网络节点

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

很多车主都觉得，车机无非就是导航、听歌，就算有点小 bug 也不会闹出多大乱子，但卡巴斯基研究团队在 2026 年 6 月监测安卓威胁样本时，挖到了一个刷新认知的恶意事件，这也是全球首例专门针对车机 head unit（车机中控）设计完整感染链路的恶意软件事件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo3SxLIuExWJe0gGYQAQCsbygxUPhdh4fyeC0fTMMjicpNHjUrWYDXDnlCH6Pqj55TUSyZ2nAK8AsvXME02BgKtAQGfqTHia9ZZQ/640?wx_fmt=png&from=appmsg)

这款新的安卓恶意程序有个很诡异的特征，它以普通应用的形式安装到设备上，却完全没有 UI（用户交互界面），不会弹出图标，不会弹出窗口，普通用户完全感知不到它的存在，研究人员由此判断，它大概率是在用户毫不知情的情况下被部署到设备中，后续完整的溯源分析也证实了这一猜想。

本次威胁的核心结论可以简单概括为，攻击者打造了一套多阶段下载器木马，最终用来完成广告欺诈，同时组建代理僵尸网络，它不走破解、物理入侵的老路子，直接利用安卓车机固件自带的更新模块完成恶意分发，高置信度判定该攻击来自 MoYu Group，这个组织和 BADBOX 僵尸网络存在强关联。securelist.com/android-head-unit-malware/121106/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqzW1hOic0KYaS0ibiaMsd5pAtcAiao5HAwDCxiaCCUEmvAqiaTHUczqmpZ20Via6jmQ9sqhdUsqzuLU1SvfmJQIiaqtHVCtUn002ZDB6E/640?wx_fmt=png&from=appmsg)

head unit 也就是车机中控，既是多媒体娱乐中枢，也承担一部分车辆功能控制，分为原厂预装版本和后期改装的后装版本。

不少厂商会选用安卓作为车机底层系统，安卓开源代码本身就适配车载场景，厂商还能在固件编译阶段内置自研系统应用，用来定制界面、补充硬件适配组件。绝大多数普通安卓 APP 都可以直接在车机上运行，恶意软件自然也不例外。

不过部分手机端常见木马，比如银行木马，在车机上几乎没有利用价值，车机不会运行手机银行，攻击者投入资源去植入这类程序得不偿失。

但大量车机自带 SIM 卡槽，能够长期联网，用来导航、接收固件升级，设备本地几乎没有对黑客有直接价值的隐私数据，这种场景下，把设备拉进 botnet（僵尸网络）就成了攻击者最划算的选择，逻辑和物联网设备被入侵挖矿、做代理是同一套思路。

这次被攻陷的就是 DoFun 品牌的车机固件，固件本身的设计缺陷给攻击者提供了分发通道，研究团队已经把情况同步给厂商，厂商反馈已经修复相关安全隐患。

## 合法更新组件 TWCore，沦为恶意传播通道

##

TWCore 是设备上的正规系统应用，负责收集统计数据，执行车机软件更新，整套更新逻辑依靠托管在 cardoor [.] cn 子域名的 MQTT 消息代理服务完成。

MQTT 会下发消息，消息内包含需要下载安装的 APK 信息，消息字段里有一个布尔类型标记 installNotExists，当这个标记被设置为 true 的时候，TWCore 就可以直接安装设备原本没有的应用，不会校验设备原本是否预装该软件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDr86JNfW4iaiahAiaaRT9e3naCZaIOQu5MGXHNlU8ibOicjOWicE495uJVtBrwcw8tlicuscV2hgnQpKZKvHXkAFZic01EKyXT0oZxiasbA/640?wx_fmt=png&from=appmsg)

APK 文件会被下载到`<TWCore external cache dir>/push/apk/`目录下完成安装，卡巴斯基的遥测数据就在这个路径下捕获到恶意样本，并且所有被观测到的恶意程序，都是由包名为 com.tw.core 也就是 TWCore 本身触发安装，第一个落地的恶意组件就是 JarService dropper（投放器）。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp5WTtmtJBLicZnBnOMzEzic3THZ0QhR7UZYdW8ibESXIpFyYxgx3tX4ESGwUhB3gPRvH2FyxxzibALLazuLbkREb28QpZzpjzoz8w/640?wx_fmt=png&from=appmsg)

## 三段式恶意链路，层层解密加载载荷

### Stage1：JarService 投放器

JarService 本身体积不大，没有任何可视化界面，木马代码内部存放多块加密数据，每一块数据使用单字节密钥做 XOR 加密，不同数据块密钥会线性偏移。解密完成之后，会反序列化得到下一阶段载荷的版本、入口信息，同时取出自身内置的后续加载逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDowyA6shBRSSFlgHmA3B5Etv8YDQR51iaibVyhl7dH6w4EllntWyHIxSCXMEBMMY9S7WEsa5h2PY9b828BhT6v7G8Kdqiaddp6cLo/640?wx_fmt=png&from=appmsg)

本次分析样本中，第二阶段载荷的入口点是 com.c.j.qbh 类下的 wa 方法。

### Stage2：loader 加载器

第二阶段的恶意 loader 内部保存大量加密字符串，这些字符串后续会被当作类名，通过 Java 反射机制执行第三阶段载荷。

loader 会向攻击者的 C2（命令控制服务器）发送 POST 请求上报设备信息，上报内容包含 userId、dexVersion、dexType、channelId、packageName、appVersion、appName 等字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpuSY1dPGGeEfZX4OeDLI10LkznurRRwTwXcGvTdqUT0iaxhvEOmWfwUoBvOHEHodwOnrPicialD2qavxlF7zoA9icicEp15icNHbbO4/640?wx_fmt=png&from=appmsg)

C2 服务器返回 JSON 格式响应，其中 dexUrl 字段给出第三阶段载荷的下载地址，下载回来的数据头部首先是单字节整数，对应解密 loader 内部字符串的密钥，紧随其后四字节浮点数值，用来 XOR 解密真正的 Stage3 载荷。

解密之后 Stage3 程序的入口是 com.ast.sdk.BillingMain 类的 init 方法。

研究人员尝试变换载荷链接里的版本号，一共拿到 7 个不同的 Stage3 变体，最早 3.57 版本使用了完全不一样的解码算法，说明更早的攻击版本中，JarService 和 Stage3 之间使用过另一套 loader 逻辑。

### Stage3：clicker 点击器 / 反向代理加载器

第三阶段程序默认每 90 分钟就向服务端`/cpc/api/task`接口发送 POST 请求，上报设备分辨率、设备型号、Wi‑Fi 的 SSID、MAC 地址还有木马配置版本。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqXUortX8ehxGLV1r4lVMPA2PPJC5hPMhmMMlSDohDGsTD278pianQhhoxRJw5HibVaQBA6luBbw6Gs2bkqON9jTe0FyKibwZLGSU/640?wx_fmt=png&from=appmsg)

如果本地配置已经过时，C2 就返回更新后的配置，包含全新 C2 地址、HTTP 请求路径，研究捕获到的最高配置版本为 3.82。

如果配置无需更新，服务器返回整数 productId 也就是指令编号，木马会把指令编号对应的 JSON 序列化指令存进 SharedPreferencesAPI。一旦收到陌生 productId 或者版本过期的指令编号，木马就会发起 GET 请求访问`/cpc/api/xml`接口拉取完整指令脚本。

每一条指令都带有 tagName 标记，程序根据标记映射到对应执行类，报告发布时攻击者一共实现了 9 套指令，覆盖返回存储数据、修改剪贴板、发起 HTTP 请求、WebView 加载网页执行 JS、deeplink 跳转浏览器、traceroute 网络探测、loadlib2 下载执行任意代码等能力。

真实攻击场景中攻击者主要启用 loadlib2 和 http 两条指令，loadlib2 用来下载名叫 zhima 的模块，这个模块就是反向代理组件。诺基亚 Deepfield 应急响应团队也在电视机顶盒样本中独立发现过 zhima，两边的发现互相印证，攻击者的最终目标就是搭建代理僵尸网络。

zhima 模块同样存在多个版本，研究人员通过版本遍历拿到 8 个变体，最早版本号为 57。

简单解释它的牟利逻辑，被感染车机不会偷取车主的银行卡密码，它会把本机网络对外开放成为代理节点，黑产可以购买这些代理服务，对外发起网络请求，流量看起来就来自普通车主家庭网络，绕过很多风控拦截，同时木马附带的 clicker 能力还可以做广告点击欺诈刷取广告收益，而车主全程几乎感受不到异常，车机表面一切正常，只是后台悄悄跑黑产业务。

## 攻击溯源：MoYu Group 与黑产代理服务

在分析 Stage2 loader 的时候，研究人员发现程序会创建名为 mosdk‑host‑loader 的线程，顺着 mosdk 这个线索，研究人员找到机顶盒恶意样本 com.abc.nexus，样本内部有一个和 JarService 逻辑高度相似的投放组件，它的启动服务命名为 AdmoyuService。

结合线程命名、服务命名，再加上网络基础设施大量重合，卡巴斯基高置信度把本次攻击归属给 MoYu Group，该组织就是 BADBOX 僵尸网络背后的行动方之一，诺基亚团队的独立情报也佐证了基础设施重叠这一事实。

黑鸟：经典BadBox域名特征

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqOJ0S877Mfh7uBMXuxg1M9UITqQjKc7pPByw0j5Rnf6phZGfPdHOSUuIhZ5FsxVXMLuswTRGojx9SywAq7uoibeZLESrB2ln04/640?wx_fmt=png&from=appmsg)

溯源过程中研究人员还发现 zhima 模块 C2 服务器 IP128.14.210 [.] 58，对应域名 admin.uipoxy [.] com，这个地址可以访问 zhima 的管理后台，后台支持带邀请码注册普通操作员账号，页面的用户协议、隐私政策托管在 pxyedge [.] com 域名，该域名属于住宅代理服务商 PXYEDGE，页面还保留版权信息指向另一家代理服务商 ProxyForU。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqrLVicKHYfXtJKba7fs7tL35cUibRCPZtG9LKL6pxsibuO1MMHnn0tpyvqZqXdQfMbYgfDMdh3oz7SNLF1n3se2m3icmcPEZusvsg/640?wx_fmt=png&from=appmsg)

注册登录接口的路径格式高度统一，都是 admin 子域名搭配`/proxy/u/login`登录接口、`/proxy/register?channelKey=`注册接口，多方线索都指向这套代理平台和 MoYu Group 存在关联。

即便安全厂商和执法机构一直在打击 BADBOX 这类僵尸网络，相关黑产团伙依旧在迭代攻击手段，传统感染方式包括预装后门、被篡改的 IPTV 应用，而本次事件展示了更加新颖的攻击路径，直接利用设备原厂合法更新系统下发恶意载荷。

这也是公开记录里，第一次出现专门瞄准车机中控的完整恶意感染链路，意味着汽车中控不再只是一个单纯的多媒体盒子，它和物联网设备、手机一样，已经成为黑产重点盯上的目标。

攻击者并不需要攻破车辆动力控制系统，不需要偷取车主个人隐私，仅仅劫持联网能力，就可以把千千万万台车机变成默默赚钱的僵尸节点，车主很难感知，危害却实实在在存在。

More ⬇️

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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