---
title: Clash Verge开启局域网代理共享，让全设备都能使用
url: https://mp.weixin.qq.com/s/WOEWHjgINQ987syreS1MEw
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:31:40.270904
---

# Clash Verge开启局域网代理共享，让全设备都能使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjVxGU8OzbziaUFic5DPgFkOn6OMJlGgbWfxgnBp5G1gEC8tiazyftSWOLehJnl5ZkgsWF0nH5BfOz7kwglAU63MoAdXkDSTlJluAc/0?wx_fmt=jpeg)

# Clash Verge开启局域网代理共享，让全设备都能使用

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器中沉浸阅读

有时候你会发现一件很烦的事——
电脑代理已经配好了，速度也没问题，但手机、平板、甚至另一台电脑，还得一台一台重复配置。

说白了：
👉 **你已经有“梯子”了，但它只服务你自己。**

那不如，让电脑“多干点活”。

### 💡 这一段操作的本质是：

让你的电脑，从“使用代理的人”，变成“提供代理的人”。

简单理解就是：
👉 **电脑变成局域网里的“代理服务器”**

**注意，这种方式不是直连，而是通过电脑做了一层中转。**

**但因为是在局域网内，这一跳几乎没有损耗，可以忽略不计。**

**如果在clash中进行链式操作，最后设备所使用的流量也会是第二跳的流量，若第二跳是住宅IP，那就很方便的让设备使用住宅IP流量了。**

**这里我本地开启代理，Windows10虚拟机没有开代理，那么我要把本地的代理共享给虚拟机的Windows10。**

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVAzLibA3WDtP9icrwwIFFFxfP1KFtaibpib8VEaMc2wiaicTsibkOjibibiatWrBqQXr72FjVJ4JDl3POcyh0gV1z7XY4FkoW1qaVLclVkI/640?wx_fmt=png&from=appmsg)

🖥️ 第一步：打开局域网共享开关

打开Clash Verge。

找到设置（Settings），你只需要做一件事情：

👉 打开：

```
Allow LAN（局域网连接）
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjU4T6y9aR8M0VjMLyXg6ibEzy3zkMTr2xChlZJZ5JuE0KySNXF13n5JKSaxsJpPcZ26jGttrOzX4vFT1ibqKqUfuWSQviccKfACgA/640?wx_fmt=png&from=appmsg)

这一刻，你的电脑会“说话了”：

> “我不仅自己能用代理，你们也可以来用我的。”

🌐 第二步：确认端口

一般默认就是：

```
混合端口：7897
```

不用改，记住就行。

🧭 第三步：找到你的电脑IP

打开终端，输入：

```
ipconfig
```

找到 无线局域网适配器 WLAN 中的：

```
IPv4 地址 . . . . . . . . . . . . : 192.168.x.x
```

👉 这个 IP，就是你在局域网里的“地址”

可以理解为：

👉 局域网设备**要找你，就靠它**

**🔗 到这里，其实已经完成了**

**你的电脑现在的状态是：**

```
局域网内任何设备 → 连接你的IP:端口 → 使用你的代理
```

## ⚠️ 但有一个关键细节（很多人卡在这）

##

电脑默认是“有点防备心的”。

如果你发现：

👉 别的设备连不上

那大概率是：

👉 **Windows 防火墙把你拦了**

解决也很简单，让它“放行”就行。

📱 局域网设备如何使用？

刚刚那一步，其实电脑已经准备好了。
现在的它，就像在说一句话：

> “我这边已经能翻了，你们要用，直接来找我。”

那设备怎么“找你”？很简单——填一个地址。

📲 手机端设置（通用方法）

以手机连接同一个 WiFi 为前提：

进入：

```
WiFi → 当前网络 → 修改网络
```

找到代理（Proxy），选择：

```
手动（Manual）
```

然后填写：

```
服务器：你的电脑IP端口：7897
```

保存。

这一刻，其实已经完成了。

手机会把所有请求交给电脑处理，就像在说：

> “我不翻了，你帮我翻。”

💻 电脑使用：

逻辑是一样的，只是入口不同：

* Windows：设置 → 网络和internet → 代理 → 手动设置代理
* macOS：网络 → 高级 → 代理

填写同样的：

```
IP + 端口（7890）
```

## 🔍 如何判断有没有成功？

##

不用猜，直接测：

👉 打开浏览器访问：

* Google
* YouTube
* 或任何你之前访问不了的网站

如果能打开，说明这条链路已经打通了。

⚠️ 常见翻车点（帮你提前挡坑）

### ❶ 不在同一个局域网

###

👉 必须满足：

```
手机 和 电脑 在同一个 WiFi
```

否则你填的 IP 根本找不到人。

### ❷ IP 填错

###

很多人会填成：

```
127.0.0.1 ❌
```

👉 这是“自己找自己”，肯定不行

必须填电脑的内网IP。

### ❸ 防火墙没放行

###

表现就是：

👉 连不上 / 超时

解决方法你前面已经做过：放行端口即可。

### ❹ 有些 App 不走代理

###

这是正常的，不是你配置问题。

👉 因为你现在用的是：手动代理（HTTP）

部分 App 会绕过它。

到这里就结束了，只要在同一个局域网；
任何设备填上这个IP和端口，都可以直接使用你电脑的代理；
不需要重复配置，也不需要额外软件；

三连加关注，追文不迷路。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_02.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_80@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_64@2x.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXibu188DgR2icXAYBQtNf01bhpxic7jqf6urQPOCpmib4T38DSJQ1bdm1hkrqeCwSNPWCjicD9GAj5icWHicBWTI9sHU19kFibKaVtJ50/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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