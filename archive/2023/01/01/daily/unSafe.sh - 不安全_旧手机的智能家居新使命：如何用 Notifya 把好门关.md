---
title: 旧手机的智能家居新使命：如何用 Notifya 把好门关
url: https://buaq.net/go-143559.html
source: unSafe.sh - 不安全
date: 2023-01-01
fetch_date: 2025-10-04T02:50:20.469422
---

# 旧手机的智能家居新使命：如何用 Notifya 把好门关

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/84079cef0fb3f9da15da4b669c9ef006.jpg)

旧手机的智能家居新使命：如何用 Notifya 把好门关

旧手机的智能家居新使命：如何用 Notifya 把好门关 手机厂商们每年都在推出新手机，但消费者的疲软却一年比一年更甚，毕竟换来换去手机能做的事情也就这么多，只要不卡顿不出现问题，用上几年
*2022-12-31 15:0:0
Author: [sspai.com(查看原文)](/jump-143559.htm)
阅读量:28
收藏*

---

旧手机的智能家居新使命：如何用 Notifya 把好门关

手机厂商们每年都在推出新手机，但消费者的疲软却一年比一年更甚，毕竟换来换去手机能做的事情也就这么多，只要不卡顿不出现问题，用上几年已经不再是问题。

比起换新手机来说，如何处理旧手机渐渐成为了一个更值得探讨的问题。服役多年的旧机器送去海鲜市场或爱回收等平台二手转卖是不少人的选择，也有部分人会将它交到长辈手中继续使用。只是对一些更旧的设备而言，二手转卖的价格或许还抵不上一顿海底捞的饭钱。

![](https://cdn.sspai.com/2022/12/30/70e645fe8e768d5754534818cc8731b4.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

所以除了把旧手机交给 Apple 来「免费回收」，给它们充上电、在「力所能及」的场景里继续发光发热也是一个值得思考的方案。比如 Notifya 这款应用就能将它们变成智能家居的组成部分——手机上的传感器数量可比传统的智能家居多多了，而且还具备可以直接操控的屏幕，好好利用起来应该会有非常不错的体验。

![](https://cdn.sspai.com/2022/12/30/2a3622d2cf0dbe7bcd6eb8a79fd6683b.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

## 用手机检测门窗状态，怎么实现的？

传统的门窗传感器都是依靠门磁来实现，通过门上的磁铁和门框上的干簧管来检测门的开启关闭状态，原理和继电器类似。这种当下非常成熟的门窗传感器方案缺点也显而易见：一个门窗传感器只能检测一扇门 / 窗的状态，如果家里的门不是智能门或安装了智能门锁，那么就只能买 N 个来满足需求。

按照目前一个小米门窗传感器 249 元的价格来算，一个三室一厅的家庭要给所有门窗都加上传感器需要一笔不小的投资，如果当下要用上体验更好的 Thread 协议设备，唯一可选的 eve 门窗传感器一个更是需要三百多元，一口气买好几个还真不是普通家庭能负担得起的。其他门窗检测方案（如动静贴）同样也需要将设备安装在门窗上，且依然无法解决上面说到的「一个传感器只能对应一个设备」的问题。

但是 Notifya 却恰恰相反，它不仅能用一台手机检测多个门窗的打开状态，还不需要将设备贴在门窗上。要实现这样的效果，其原理肯定与门磁、动静贴的方案截然不同。那 Notifya 是怎么做到的？

**答案是麦克风**。

根据作者在 Home Assistant 论坛的介绍，Notifya 是通过调用手机麦克风捕捉开关门窗时产生的瞬时空气扰动做到的：当我们开关门窗时，除了会发出开锁声和门框碰撞声外，其实还会对屋内的气压产生影响。尽管这些气压的震动不足以发出声音，但可以被手机麦克风捕捉到，然后转化为电信号被 Notifya 识别。

开发者表示，Notifya 采用了一些深度的音频算法，可以对一些音乐声、人声等噪声进行滤除。根据 Notifya 作者在 YouTube 上发布的一个[视频](https://www.youtube.com/shorts/T6minKNKiUw)显示，同一个房屋内即便是大声播放页音乐，Notifya 依旧能够灵敏地检测到 30 米外的门被打开 —— 当然，具体的检测距离和灵敏度还是要根据设备的情况而定。

![](https://cdn.sspai.com/2022/12/30/e0567a3d47ff98bf0ad9dd7c12ac8591.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

作者这是什么家庭水平啊，30 米了还没出家门 🥹

## 多设备联动

虽然 Notifya 能检测到最远 30 米外的门窗状态，如果一些财力雄厚的家庭有超过 30 米或多层的房子，还是需要 Notifya 的多设备联动来发挥作用。

你可以将一台安装了 Notifya 的设备作为主（接收）设备，将多个子（检测）设备链接到主设备上，这样就可以在一台设备上接收到多个运行 Notifya 手机的警报。有点熟悉对吧？没错，像极了多个 Zigbee 设备和一个网关的通信形式。

但 Notifya 的厉害之处不在此，它甚至还支持更多设备联动。Notify 允许设置多个接收设备，或者将多台手机互相设置成接收端和检测端，实现多台手机同时通知报警。这样一来，Notifya 也就不再有像 Zigbee 网络中类似网关设备的存在，而更像是 Thread 网络的样子：每台手机都可以是 Notifya 的节点设备（End Device），每台手机也都是传递 Notifya 数据的路由器（Router），任何一台手机掉线也能保证其他 Notifya 设备的正常工作 —— 是不是更有那味了？

由于我只一台索尼 Xperia 1 II 和一加 8T，所以只能在两台设备上进行测试。实际体验下来，Notifya 的联动响应非常灵敏，并且可以查看到已配对设备的警戒开关状态、报警的历史记录和强度等信息。

![](https://cdn.sspai.com/2022/12/30/a6b3a1f4e056823bb4c41f49258e21fc.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

不过 Notifya 的多设备联动设置在我看来有些不够直观。进入到「Remotes」页面中，点击「Share this devices」，Notifya 会创建一个分享链接，在另一个设备上用浏览器打开这个链接就可以跳转 Notifya 建立配对。

另外这个链接其实并不是很灵敏，很多时候打开了并不会询问我是否跳转到 Notifya，而是直接停在了空白的网页中，或是要等一会 Notifya 才能识别到设备。

除了打开链接之外，作者还提供了配对码来进行连接。同样在「Remotes」页面下，点击「Monitor new device」，输入配对码后点击「OK 」就能建立配对。但是刚开始我对这个配对码一头雾水，我在两台设备上都点击了「Monitor new device」，Notifya 也并没有给我弹出配对码呀？自己在两台设备随便输入同样的字符也不对。后来才发现，原来配对码在「Share this devices」的链接里……

```
Get Notifya alerts from me by opening the link on your device:

https://links.notifya.app/links/68Mq

You can also enter the identifier code below directly into the Notifya app (the code is Case Sensitive!):

XXXX
```

坦白来说，配对码建立设备连接的速度和稳定性都要比直接打开链接好多了，但是配对码需要找一个能完全显示链接文本的第三方 App 才能看到，而且 Android 割裂的分享生态，你懂的。

所以我觉得，既然作者已经做了这个功能，不妨就直接弹出一张配对码的卡片，让用户直接输入或扫一扫二维码就能快速建立配对，这样的体验会好上不少。

![](https://cdn.sspai.com/2022/12/30/32c2ae6c87c7349ad6b7b0051150b625.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

比如这样，做 UI 我们是专业的

另外，Notifya 并不能对配对的设备进行任何操作，例如我不能在索尼马克兔上调节一加 8T 中 Notifya 的开关或灵敏度。不过这个问题可以通过 Notifya 自带的 Home Assistant 支持来解决 ——

## Home Assistant 集成

作者在 Notifya 的介绍表示自己是 Home Assistant 的铁粉，自然 Notifya 对 Home Assistant 的支持是少不了的。

要开启 Notifya 对 Home Assistant 的支持，首先需要确认自己的 Home Assistant 中开启了 MQTT 服务。以目前 Home Assistant 2022.12.8 版本为例，进入「配置 > 加载项」中，点击右下角的「加载项商店」，搜索并安装「Mosquitto broker」。

![](https://cdn.sspai.com/2022/12/30/a7462934b178545a94d43bbda822c87a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

安装完成后先不要着急启动，点击 Mosquitto broker 的配置页面，在「Logins」页面中设置好用户名和密码：

```
- username: 设置一个用户名
  password: "设置一个密码"
```

![](https://cdn.sspai.com/2022/12/30/4376b1f72dadc3365e308cf195b4b45a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

注意，Mosquitto broker 的账户和密码不能和 Home Assistant 的登录账户密码一样。设定完成后，点击右下角的保存按钮，然后回到信息页面启动 Mosquitto broker 服务。

接着，你可以选择重启一下 Home Assistant 服务，避免一些奇奇怪怪的错误。然后再来到「配置 > 设备与服务」页面，直接在已发现的 MQTT 服务卡片下点击配置，即可添加 MQTT 服务。若 Home Assistant 没有自动发现它，点击右下角的「添加集成」，搜索「MQTT」后添加一个新的 MQTT 集成也能达到相同效果。

![](https://cdn.sspai.com/2022/12/30/0620f77b0b49d386694f76b5ebce967f.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

因为是使用官方提供的 Mosquitto broker 服务和 MQTT 集成，一般不需要修改任何信息，一路默认下一步最后点击保存即可。不过要注意的是，如果你是用 Docker 安装的 Home Assistant，那么在设置中是没有「加载项（Add-ons）」这个选项的，需要自己安装 Supervisor，或是转用 Home Assistant 镜像，具体的教程这里就不表了。

搞定了 Home Assistant 的设置后，再回到 Notifya 应用中，在设置页面打开「Enable Home Assistant」的开关，然后设定 MQTT 服务：

* Host：Home Assistant 服务的 IP 地址；
* Port：如果你没有修改 Mosquitto broker 服务的端口，保持默认即可；
* Username：Mosquitto broker 服务中设定的用户名；
* Password：Mosquitto broker 服务中设定的密码。

![](https://cdn.sspai.com/2022/12/30/d4f36bff36e75d90488c0a7dfc6d8160.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

这时候回到 Home Assistant，你就会发现 MQTT 集成下出现了一个以手机型号命名的新设备，到这步就说明已经成功将 Notifya 接入了 Home Assistant。

Notifya 提供了三个实体，分别是总开关、灵敏度和传感器状态。通过 Home Assistant，你不但可以在任意 Notifya 设备上对其他 Notifya 的设定进行调整，甚至可以将 Notifya 桥接到 HomeKit，或是利用自动化来进行更多自动操作。

玩法有很多种，就看你的需求和脑洞够不够大了。

![](https://cdn.sspai.com/2022/12/30/95f6c10dfe6464cee48acfa0bc06101e.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

## 一些问题

由于 Notifya 是采用空气振动和声音来判断门窗的动作，因此本质上来说它和「动静贴」类似，即便你可以在设置中开启 Notifya 对手机移动的检测，但也依旧不能检测门窗此刻的开关状态。所以如果要做开门或关门对应的自动化，那还是逃不了要用门磁传感器。

其次，虽然 Notifya 提供了灵敏度调整的选项，但误检测的问题还是存在的。最离谱的是我擦鼻涕和咳嗽的时候，由于对手机周围的空气进行了小面积影响，有那么几次都被 Notifya 误判成为了开门。而且为了考虑到检测的准确性，你需要尽量将手机放在空气流通的地方，丢在柜子里肯定是不行的。

而对于推拉门，Notifya 的准确性就要低不少了。如果是中式老人家爱用的铁艺门、栅栏门这些完全镂空的门，那还是乖乖用门磁传感器和动静贴吧，Notifya 无能为力。

最后，既然 Notifya 调用的是手机传感器，那么保持手机有电也是必须的。此外，你也得保证 Notifya 一直在运行，不能被息屏和内存不足等原因被 Android 系统嘎掉。虽然 Notifya 提供了一直亮屏的选项，但这对电量和 OLED 屏幕的设备来说还是不小的考验。

## 总结

尽管 Notifya 还有些缺憾，但它灵敏且相对准确的检测结果也还是有不错的使用体验，加上对 Home Assistant 的良好支持，能衍生出不少奇思妙想的联动玩法。更值得肯定的是，Notifya 是一款免费应用，调试好之后确实还是能省去一些额外购买门窗传感器的钱，给肯德基疯狂星期四留出更多经费。

![](https://cdn.sspai.com/2022/12/30/1c77052f6358738ec15c6cd279de355f.PNG?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

iOS 端出现了 Pro 版的购买选项，Android 端则没有。不过目前点击了会提示无法连接到 App Store

Notifya 支持 Android 和 iOS 系统，Android 端大小约为 35MB，iOS 端大小约 10MB，目前是完全免费的应用，未来很可能会加入 Pro 功能内购。Android 用户可以在 Google Play 商店下载，iOS 用户则需要加入 Notifya 的 [TestFlight](https://testflight.apple.com/join/yXHuJt1y) 来获取测试版。

> 下载 [少数派 2.0 客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，解锁全新阅读体验 📰

> 实用、好用的 [正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

[![宛潼](https://cdn-static.sspai.com/ui/img-placeholder.png)](https://sspai.com/u/Elliana/updates)

以前叫 JohnHarrod。用不停创作来对抗焦虑，欢迎合作或投喂。公众号：约翰斯库

文章来源: https://sspai.com/post/77556
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)