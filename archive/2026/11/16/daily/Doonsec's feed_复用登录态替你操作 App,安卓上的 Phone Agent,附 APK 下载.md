---
title: 复用登录态替你操作 App,安卓上的 Phone Agent,附 APK 下载
url: https://mp.weixin.qq.com/s/eRQzxoiR0Dx-mYC7n5g0bw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:14.700977
---

# 复用登录态替你操作 App,安卓上的 Phone Agent,附 APK 下载

# 复用登录态替你操作 App,安卓上的 Phone Agent,附 APK 下载

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OJ2dyibgszmtvxSqOypenkoBp4sQGoMdSaicFfIqvt8QZ9CaGSkwYN3qjGYEnEiaf58A5POxhzzSDsmWVtj08FLhWunwxMtVEgYs/640?from=appmsg)
> **导语**：一句话交给它,它就能在你手机上把事办完,关键是它不抢你的屏幕。Mika 是刚开源的 Android Phone Agent,已有 1300 多赞。三十小时内连发 14 个版本,星标过千。热闹归热闹,权限边界那一栏,值得单独拎出来看。

---

## 一、这是什么,以及它有多新

推文来自 @wangzan101(王赞)。仓库是 `wangzan101/Mika`,Apache-2.0,Kotlin 加 Jetpack Compose 写的。

下午建仓,当晚就发了 v0.1.0,到 30 日晚一共 14 个版本,累计下载约 2300 次。最新 v0.1.13 的 APK 87,093,167 字节,约 83MB。抓取时星标 1157、fork 191、issue 11。

作者定位是"你手机上的私人 AI 助理":一句话交代一件事,它自己去办。

## 二、能力盘点

**后台屏干活,前台不占你**。Mika 在一块后台屏上打开 App、读界面、点击输入、滚动,你照常刷手机,小窗口显示它在做什么。技术核心是靠无线调试配对启动内置手机助手,再用无障碍做点按。界面读不出来的 App 也不怵,有文字识别兜底,配了看图模型也能看图找按钮。

**内置浏览器**默认按电脑版网页打开,能读正文和页面数据,登录过的网站保持登录。翻页有节奏,认得出风控拦截页,交给你处理而不硬闯。

**此刻的屏幕**:你在别的 App 里时,屏幕边上有颗悬浮胶囊,显示进展和结果,双击就把这一屏发给 Mika。

**定时任务、记忆、Linux 沙箱**也都在。沙箱是 Alpine Linux 3.22 加 PRoot,能跑 Python 和 shell,默认断网,仅 arm64。

**内置知识**是它"稳"的原因:28 个 App、17 个网站另写了使用知识,入口在哪、要注意什么,用到时自动查阅。没写到也能干。

![内置浏览器读 Hacker News 页面](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NiayUJtvr4sxNcwyG54XaOwcxBDTDN9AmXY0CoZW1Lj0tD76hoLQn9ia9mLiazBnskxxuZCicakViaICnRPUHjpXoUAr7RbGw9XZhk/640?from=appmsg "内置浏览器读 Hacker News 页面")

![在美团上凑满减、点外卖,付款前先问你](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6POTTbduLsAR76xAonOJwXIZkjZiaGWMP6yUKXCZticq2puut0ibL00hxVbkXHFnmQwJfRHGvLUQ3YE6icQ6VdGdJ5BEMNbnvDkSBE/640?from=appmsg "在美团上凑满减、点外卖,付款前先问你")

## 三、下载与安装

* 仓库源码:https://github.com/wangzan101/Mika
* 版本页(选最新版):https://github.com/wangzan101/Mika/releases/latest
* 安装包直链(当前 v0.1.13):https://github.com/wangzan101/Mika/releases/download/v0.1.13/Mika-v0.1.13.apk
* 手机操作设置指南:https://github.com/wangzan101/Mika/blob/main/docs/setup-guide.md
* 让电脑上的 AI 助手帮你装:https://github.com/wangzan101/Mika/blob/main/docs/install-with-agent.md

装完四步要走:开发者选项、USB 调试、无线调试,用 6 位配对码配对一次,之后长期有效。不想折腾配对也行,插着数据线在电脑上跑 `adb shell sh /sdcard/Android/data/com.wangzan101.mika/files/usb-start.sh` 启动手机助手,代价是每次重启都得再跑。

系统要求:安装 Android 11 起,执行任务要 Android 13 起,推荐 Android 14 起(后台屏有独立焦点,不占你在主屏打字)。模型要支持工具调用,README 内置二十来家服务商预设,也支持 OpenAI 兼容、Anthropic、Gemini、OpenAI Responses 接口,还能直接用 ChatGPT 登录。

## 四、紫队复盘:复用登录态是把双刃剑

Mika 的卖点是"复用你现有的登录态,不用额外授权"。评论区有人翻译得更直白:权限边界全靠 App 自觉。

**询问模式只拦花钱那一步**。默认模式里,只有下单、提交订单、页面显示应付金额时先问你,发消息、发帖、提交表单、删除、改设置都不问,付款由你亲手完成。切到自主模式,连付款也不问。

**v0.1.13 还加了"像人"的操作节奏**。打字改成一段一段输入,动作之间有长短不一的停顿,小红书、微信、抖音这类容易风控的 App 节奏更慢,一个任务里浏览的屏数还有上限。设置里三档:快、标准、像人。从防守视角看,规避风控识别和批量自动化连在一起,挺微妙。

**官方免责声明写得很实在**:用自动化操作第三方 App 和网站可能违反用户协议,被限制功能、封号风险自担;重要的事用询问模式并检查结果。评论区也有人问:拿它自动化 X 和 LinkedIn,会不会触发 bot 检测导致账号被封。

**权限组合**:无障碍加无线调试加"自动打开无线调试"(默认开)。Mika 会在需要时自己把无线调试重新打开,"替我打开无障碍"也是默认开的。这是会把自己扶起来的配置,别的手机 Agent 也一样。

**数据面**没有藏着掖着:没有 Mika 的服务器,你的话、屏幕内容、截图只发给你自己配的模型服务商;API Key、记忆和用户画像用安卓密钥库加密存本机;更新只访问 GitHub;沙箱默认断网。README 对自定义地址也提醒过,不加密又不在局域网里的地址,API Key 和对话内容可能被同一网络里的人看到。

![在 BOSS 直聘网页上批量打招呼后的结果](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PAWjrHrTzXFvrVscSNQQEPmVenibzN1wxuJicYibBibCzJaDmenqQFXyoYpTAKg5rByjncoKKVT24Wm7Lys9t6hZFtNmfJmA4nibsY/640?from=appmsg "在 BOSS 直聘网页上批量打招呼后的结果")

## 五、上手建议

评论区有条评论值得抄下来:先从只读汇总类任务开始,验证识别准确率;再跑单应用内操作,跑通了再试跨应用;最后才碰多步确认的任务,每一步都让它停下来等确认,别一开始就放全自动。还有一条容易忽略:先把任务边界定好,哪些 App 能碰、哪些操作必须先问你,边界定晚了,省下的时间都花在收拾残局上。

微信这种没有结构化界面的应用纯看图会慢不少,先拿界面清晰的 App 练手,成功率高一些。

## 六、结语

Mika 把 Phone Agent 最有争议的那一步,复用登录态、免额外授权,做成了主卖点,比要 root 要电脑的前辈省事。代价是权限边界从系统手里挪到了 App 自己手里,作者用三档确认和免责声明把风险摊开说了,同类项目里算少见。

但反过来看:一个能读屏、能点按、能自己开无线调试、还内置了"像人"节奏的 agent,能力边界由模型和任务定义决定,不由开关决定。能替你干活的,也能替别人干活。

**版权声明**:本文由华盟网原创发布,保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MicjL2WkVnJkMcdKww5n8psYeYkekHFQqK6Z6CNTGaBKCwQrDz6rCKA7lliaciadmyicZkaepfwOWxpjJ0cchXDRmibnmR1gDz4A2Y/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6ODh4Uct19KhocibR1sfLaZJAzh2zbMPmLwYNHLhjGPOt3E8Wsncs65A4algB7vTf77UEXfsG5ZdQe7MVlKURoBgKQTtQvwhIkc/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MPIuHKbMNZHDB4JAJmgYgdlhsP8cc2jeqW8ztAPomDckqiavQfiaJcribjAjgIX519cK826ia6BqU9EFH753mWIicMtvnzj9Gpt9Pg/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NpLxBc8nicrA09lECb8pBKs6I6c4aZ5UsmGkzdEADxp0CW3icEC5krq4G2WRicAa78PR9XmUomDicrsM5QCeneianmGgbCv98SFHd8/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过