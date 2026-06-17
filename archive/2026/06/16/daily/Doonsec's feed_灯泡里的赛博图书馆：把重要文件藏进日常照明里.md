---
title: 灯泡里的赛博图书馆：把重要文件藏进日常照明里
url: https://mp.weixin.qq.com/s/v-Q18NZHzu873RIpnLpKtw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:05.999615
---

# 灯泡里的赛博图书馆：把重要文件藏进日常照明里

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDprghXlKKETKFLBcCyU3IBGqsLicC9JCTGv9VRnuuNiboyqzmBibF6x5j77vh8MIwTQkx9xaenNA1vR9Ef3sPGTrFl4YutCoVdNpQ/0?wx_fmt=jpeg)

# 灯泡里的赛博图书馆：把重要文件藏进日常照明里

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，海外开发者 Richard Osgood 分享了一项硬件改装项目。他将普通 WiFi 智能灯泡改造成可离线共享重要文件的微型数字站点。只要灯泡通电，附近任何人都能通过 WiFi 访问其中存储的资料。设备外形与普通照明灯泡一致，隐蔽性较强且成本低廉。

Richard 的这个想法，最早源自 Ben Brown 的短篇小说图书馆。故事里的角色们维护着一个数字档案馆，存放着创意作品、使用手册、3D 模型等一旦从互联网消失就难以找回的内容。

受这个内容启发，他萌生了对应的开发思路。如果能把重要的数字文件装进智能灯泡，再布置到社区的各个角落，哪怕在网络受限的环境里，人们也能就近获取这些资料。设备本身就是日常照明用具，很难被特意排查，而且单台价格低廉，批量部署也不会产生太高成本。

Richard 最初在本地 DEFCON 爱好者聚会中聊起这个想法，有家庭自动化经验的朋友向他推荐了开源固件 Tasmota。这款固件可以刷入各类智能设备，实现完全本地化控制，摆脱厂商云服务的限制，与项目离线自主的需求高度契合。

经过调研，他找到了一款预装 Tasmota 的商用 WiFi 智能灯泡，主控为 ESP32C3 芯片，自带 4MB 闪存，官方还标注了各个 LED 灯珠对应的 GPIO 引脚，非常适合二次开发。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDonYpDP9CftJa3icKexegicCziaR5tgpcwAps4HYzaZp3ZgSmmWWvJZCLkT7taWCQBWTpicmXueTomUCVYXhPz4hJJhbehcYX3H7cw/640?wx_fmt=webp&from=appmsg)

【预装 Tasmota 的 ESP32 智能灯泡实物外观】

更关键的是，这款灯泡支持 OTA 空中刷机，不需要拆开外壳就能刷入自定义固件，大大降低了改装门槛。为了防止操作失误导致设备损坏，他一次性购买了两台备用。

## 拆解与存储扩展尝试

拿到设备后，Richard 第一步就拆解了灯泡，研究内部结构与改造空间。

撬开灯罩后可以看到两层电路板。上层是 LED 灯板，下层是搭载 ESP32C3 的主控板，中间预留了天线位置，铝制外壳也兼顾了散热与信号优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpjsMF6vNq11y2SXCZa991nFQ1tL5wibhofSYhpNFVWfgby5bVArSHQ45cibThV8LiaEseN9eV5icL8jnkrjZibphUeribeI6ZkVpicw4/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDp85o5Ltqgzib7rDJ82uBZY7LwLJPHIViclpCDIn5SMS9N8se2G9Ks1DsFaedkawS1SveKoTbnibKiapukwJYE5m87x3vGvHiasl4Zs/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDob2oZM4zibZ7xbTTicUy0HH5Y9gN2k2yts4LMXr1zBD8a122CxkLicd7kXlEZKpUd9OKdozzjtko7kjWdSKW8Bjj8ulNEicksQtNM/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDroOyicNcROUXkEEMysRDvxfI6V2Gbiao2pGW8TpeV3JdRDwL5C54miaLBqT1nXJjWIeicIEeA9zxsWup45EffREibI33tTFSXpUwRs/640?wx_fmt=webp&from=appmsg)

【灯泡内部拆解结构图，展示双层电路板布局】

但主控板被大量橡胶灌封胶牢牢固定，想要完整取出主板非常麻烦，而且拆后很难原样复原，还可能带来用电安全隐患。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqaZXlIesULRn0HYlcM5yWY56GAiaRlCE4vBeFic537picNCj8hahkib219c6FK2eDNSW5iatCddnt3Y0KcfW1CWWBsCwdMl4z4sYRs/640?wx_fmt=webp&from=appmsg)

【ESP32 主控板特写，展示芯片引脚与灌封胶去除后细节】

最初他计划加装 microSD 读卡器来扩展存储空间。毕竟 4MB 闪存要同时放下固件、网页和文件，空间格外紧张。但几番尝试后他发现这条路很难走通。灯泡内部空间狭小，没有合适的焊接位置，拆板焊接基本等于毁坏设备。尝试复用 LED 控制引脚失败，硬件设计决定了这些引脚只能输出无法输入。设计 3D 打印夹具接触引脚的方案可靠性太差，无法稳定使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDp8kCgn4IPiaYRSmC1micwer2nWqDJEDbwdnGcqb2icGFBaA0PThxibxz9hqZozEoXWqGNwxJEfTorKkm0aRAIQCbfVO23khwlL2fE/640?wx_fmt=webp&from=appmsg)

【3D 打印夹具设计截图，展示适配 ESP32C3 的接触式夹具模型】

他还测试了飞利浦 WiZ 等其他型号的智能灯泡，要么主控引脚完全不外露，要么结构更难改装。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoK9WNbiamz4hzSqicvHkDPCrYTzBibK5lPCggZZdOyicUtF7icBgHEIBQaWk2IAib7IHmYxtvtyGpg4fscVeRavibicleMW3oQcK7Bdog/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDof3I36KSh0VWVf7LCEBrKwrBpRSu1ohFO7joFMWdmicACuFGtDlZDGUMYbWUIHThmJ4XArYjhDEichGbNUcfaHWfRciaXjSLxzlQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrAmsYy7Hg54iciaULXibibYGEzcgkMN0ISPcers9Z02I1yloJ7EzL4tpUkltyw4sV5aljpKdWfLKgFchhyn2YDDFUwIIjiaLf0Pbics/640?wx_fmt=webp&from=appmsg)

【飞利浦 WiZ 灯泡拆解图，展示内置 ESP32 芯片模块】

几番试错后，Richard 决定放弃外接存储的方案，转而在原厂 4MB 闪存的限制里做空间优化。

## 分区表调整扩容

原厂 Tasmota 固件有一套默认的闪存分区方案。主固件占近 3MB，安全启动分区占近 1MB，留给用户文件的空间只有 320KB，连一份稍大的电子资料都装不下。

Richard 发现，自己的自定义固件功能更精简，不需要这么大的固件分区。于是他打算修改分区表，压缩固件分区的空间，扩大文件存储分区的容量。

这个操作风险很高。分区表一旦出错，设备就无法启动，只能通过串口修复。更棘手的是，Arduino 开发框架默认禁止修改闪存的敏感区域，根本无法写入新的分区表。

为了突破限制，他转而使用官方 ESP-IDF 开发框架，开启了 SPI\_FLASH\_DANGEROUS\_WRITE\_ALLOWED 配置，获得了闪存的完全操作权限。同时引入 Arduino 作为组件的方案，兼顾了上层开发的便利性和底层硬件的控制能力。

最终他重新划分了闪存空间，将文件存储分区扩大到 2MB，足够存放数份精简格式的重要数字资料。

## 固件功能开发

解决了存储问题后，Richard 逐步搭建起完整的固件功能体系。第一，开放 WiFi 热点与异步 Web 服务器。设备启动后自动创建开放 WiFi 网络，搭载异步 Web 服务器，提供文件浏览与访问服务。第二，自定义安全启动分区。原厂 Tasmota 的安全启动会留存 WiFi 明文密码，安全性较差。Richard 专门开发了极简的安全启动固件，不依赖原有配置，同时支持 OTA 更新，最大程度避免设备无法启动。第三，首次启动引导页面。设备首次刷入固件后会展示引导页，指导用户通过 ElegantOTA 工具刷入文件系统镜像和安全启动固件。

## 前端交互设计

为了让普通用户也能无门槛使用，Richard 开发了对应的网页前端，兼顾易用性和空间占用。

### 文件浏览页面

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrr92dB1ofqBZYmia0fAQ6ZRlXE8PxD1ibkA6mVw37QLSSAExbKzOr8OeWnsNoP7sibHE9Oburd7KaNC1qaRLs9ia8kyIOBKoEpUk4/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrwbshbAqdMlz93F3jVTiapQp9Pf5DpV7EkgMfnFR7CsJPe0bG5Ricjwr3mT0LAwIbm01rRXURmOnfOU44aicibdRPgXMtD1m5Z9uY/640?wx_fmt=webp&from=appmsg)

首页设置了欢迎界面，页面内清晰列出所有存储的重要文件，包含标题、说明等信息。所有页面都由纯手写代码完成，尽量压缩体积以节省存储空间。

### 管理后台

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDr2TMXLxEru2rmRpBXB3a2vnYqTTZHraIJf6dzfhswLalV5GHDmibStjm2VwDANljcsNX2AngSlpBXxE235c3icvkS95tCgUdG94/640?wx_fmt=webp&from=appmsg)

【管理后台界面截图，展示灯光控制与固件更新功能选项】

通过 admin 路径可以进入密码保护的管理面板，支持调节灯泡的色温与开关，方便部署时匹配现场原有灯光，降低被察觉的概率。同时后台还集成了固件更新、重启进入安全启动、分区恢复等全套运维功能。

为了让连接热点的用户能直接打开站点，Richard 实现了强制门户功能。搭建 DNS 服务器将所有域名请求指向设备自身 IP，同时适配了 Windows、安卓、iOS、火狐等各大平台的门户检测机制。用户连上 WiFi 后会自动弹出文件站点页面，不需要手动输入任何地址。

受限于 4MB 的存储空间，每个灯泡能承载的文件数量有限。但 Richard 认为这一限制也有其价值。每个部署出去的站点，都会留下部署者的个人选择，承载着他们认为最有价值最值得传播的内容。同一个城市里的不同站点各有不同，让寻找这些站点的过程具备探索的乐趣。

对于项目的未来，他还有不少规划。加入 RGB 全彩调节功能，更精准地匹配环境灯光，进一步提升隐蔽性。实现 Mesh 网状组网，让多个灯泡站点互相连通，接入任意一个就能访问整个网络里的所有文件。探索更多智能设备的改造玩法，挖掘廉价 ESP32 硬件的更多可能性。

往期：[FBI 打造模拟小镇：用于演练真实网络攻击场景](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187043&idx=1&sn=e84cf29c78bc596a6199c9f7a700b67e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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