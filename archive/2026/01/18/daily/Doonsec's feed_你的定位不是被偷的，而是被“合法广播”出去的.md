---
title: 你的定位不是被偷的，而是被“合法广播”出去的
url: https://mp.weixin.qq.com/s/rrUVEO8TrHxDRUmxCfD1Kg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:43:18.478618
---

# 你的定位不是被偷的，而是被“合法广播”出去的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpMibchcmeNze5icd5Qqsmxnv3yuymYPCk98P0nbBqXYqtft3nHSKbdO9lLcibgE5Hppslyfe9PSN0dQ/0?wx_fmt=jpeg)

# 你的定位不是被偷的，而是被“合法广播”出去的

白帽子

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

黑鸟发的[美国移民及海关执法局（ICE）的监控工具们](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184730&idx=1&sn=ab5c3b4cbbb0db1bf11df0c119d0b9f9&scene=21#wechat_redirect)，里面提到了Penlink公司的两款产品：Tangles和Webloc，在仔细研究后，发现了一些有趣的技术点。

相关资料显示，Webloc 用户可以通过多种方式搜索其手机数据数据库。

用户可以执行单次周界分析，搜索特定区域在特定时间段内的手机数据。

他们可以使用矩形、圆形或多边形绘制目标区域。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpMibchcmeNze5icd5QqsmxnvrHAKGeBsAL2Amfaj01sRQAia1Vo6DtmBruCv7GqZnx5Cp0yAvWKQxPA/640?wx_fmt=png&from=appmsg)

Webloc 用户一旦识别出感兴趣的设备，即可获取该手机的更多信息，进而推断其所有者，例如查看该手机在本地和全国范围内的移动轨迹。

用户可以点击路线功能，查看设备的移动路径。

资料显示，如果用户查看设备夜间的位置，或许可以找到其可能的住所；而白天的位置则可以找到其可能的雇主。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpMibchcmeNze5icd5QqsmxnvMJbxOicLvsG1Epibdgx28JpsgZdZScAHUX4b0ArakgiaXpd9nvIqPwMEQ/640?wx_fmt=jpeg)

该软件还可以同时监控多个位置，以查看哪些设备出现在两个或多个特定位置。

结果页面随后会显示已发现设备的列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpMibchcmeNze5icd5Qqsmxnvsv4bib8dYSzibWNicIzXJu23o6sWtiaDIODNYkvsVVsZeCicpibd4wjh2Q5g/640?wx_fmt=png&from=appmsg)

其中包括手机是安卓设备还是iOS设备；设备访问特定位置的天数；设备在该位置停留的平均时长；以及该手机的位置数据总数。

这份材料并未说明Penlink最初是如何获取智能手机位置数据的。但监控公司和数据经纪商通常通过两种方式收集这些数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpMibchcmeNze5icd5QqsmxnvBgGBtUQY8xiaavdcHyhneBFic3SRInPNmTeSbDy6nLAxyQ5apuhQzmgA/640?wx_fmt=jpeg&from=appmsg)

第一种方式是通过包含在普通应用程序中的小型代码包，即软件开发工具包（SDK）。

SDK所有者会向应用程序开发者付费，例如开发天气或祈祷类应用程序的开发者，以获取用户的位置数据。

接下来，才是正题。

第二种方式是通过实时竞价（RTB）。

在RTB模式下，在线广告行业的公司会进行近乎瞬时的竞价，以使他们的广告能够触达特定人群。

其副作用是，这些公司可以获取用户个人设备的数据，包括其GPS坐标。

间谍公司已经从一些非常流行的智能手机应用程序中获取了这类RTB信息。

Webloc 的资料显示，用户可以通过设备独特的苹果和安卓广告标识符来筛选设备，这些标识符通常会被监控公司收集。

资料还显示，用户可以通过 GPS、WiFi 或 IP 地址来筛选位置数据。

实时竞价广告意义

RTB（Real-Time Bidding）是一种程序化广告的交易方式。核心特征是：
**当用户打开或刷新一个应用/网页时，广告平台会在几十毫秒内把这个用户的设备信息广播给大量广告竞价方进行出价，最高者获得广告展示位。**

RTB 的价值在于即时竞价，但副作用是**海量设备信息会以广播式方式暴露给广告生态中的众多公司**，其中包括合法的广告公司、数据经纪商、甚至第三方“监控/情报公司”。

**RTB 的参与者架构**

典型 RTB 广告链路包含以下角色，下面的文章都直接写缩写：

1. **Publisher（发布者）**
   App 或网站，例如天气类应用、新闻应用、游戏等。
2. **SSP（Supply-Side Platform）**
   发布者使用的广告供应平台，用来把广告位卖出去。
3. **Ad Exchange（广告交易所）**
   负责把广告请求广播给多个 DSP 的中介平台。
4. **DSP（Demand-Side Platform）**
   广告主/广告代理方使用的购买端。
5. **Data Brokers / Data Management Platforms（数据经纪商）**
   在竞价中使用第三方数据增强用户画像。
6. **Advertisers（广告主）**
   最终决定是否出价显示广告的人。

其中关键点是：当一次广告请求发生时，用户数据会被发送给所有参与竞价的 DSP 以及所有接入的第三方数据方。

**RTB 数据流的实际过程**

当用户打开一个含广告的 App（例如天气类 APP）：

### **（1）App 发送广告请求给 SSP**

包含基础设备信息：

* 设备型号（iPhone / Samsung 等）
* OS 版本
* 屏幕尺寸
* App ID
* IP 地址
* **Advertising ID（IDFA/AAID）**
* 本地时间
* Locale / 时区
* 网络类型（WiFi/4G/5G）
* 用户是否付费
* App 使用行为（如页面路径）

### **（2）SSP 将请求发给广告交易所**

SSP 会包装更多数据，包括：

* **精确 GPS（如果 App 有定位权限）**
* 设备唯一标识（IDFV 等）
* 推断的性别、年龄段等（如有）

### **（3）Ad Exchange 将请求广播给所有 DSP**

这里是隐私泄露的核心点：

**每个 DSP、每个数据合作伙伴都能看到这个 bid request 的用户数据(黑鸟解释bid request（竞价请求）=RTB 广播出去的关于你设备的资料。)，不论他们是否出价。**

这意味着：

即使广告未展示给你，你的设备信息已经被几十至数百家公司接收。

### **（4）DSP 结合数据经纪商画像**

DSP 将设备标识符（IDFA/AAID）交给数据经纪商进行用户拼接，例如：

* 过去是否访问过某些地点
* 是否用同样 ID 访问过其他 App
* 是否与某个 WiFi SSID 关联
* 是否可能为某个职业群体
* 是否可能有某类兴趣或风险属性

### **（5）DSP 出价 / 不出价**

但无论是否出价，**数据已经被他们接收**。

所以，**RTB 中会暴露哪些数据呢？**

RTB 的标准数据结构由 IAB（Interactive Advertising Bureau）定义，比如 **OpenRTB 2.x/3.x**。

以下是可包含的数据范围（黑鸟注释：并不需要所有字段，但常见应用会发送大量字段）：

### **设备标识符类**

* **IDFA（Apple Identifier for Advertisers）**
* **AAID（Google Advertising ID）**
* IDFV（Apple vendor ID）
* MD5 / SHA1 hashed email（部分应用也会偷偷上传）
* IP 地址（可用于推断常住地）

### **地理定位类**

* GPS 坐标（精度一般可到 5–20 米）
* 海拔
* 速度（如在车上）
* 开启定位权限的时间戳
* IP 推断出的城市、ISP、基站区域

### **网络信息**

* WiFi / Cellular
* Carrier（运营商）
* 设备是否越狱 / root
* UA 信息（可用于浏览器/设备指纹攻击）

### **行为信息**

* App 当前页面
* App 使用时长
* 匿名用户账号 ID
* App 类别（如天气、健身、孕期管理等——极其敏感）

下面是典型的 **OpenRTB 2.5** 的数据结构片段

```
{  "id": "a7b8c9d0e1f2",  "imp": [{    "id": "1",    "banner": {"w": 320, "h": 50},    "instl": 0  }],  "device": {    "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X)",    "ip": "172.58.230.15",    "ifa": "AEBE52E7-03EE-455A-B3C4-E57283966239",    "geofetch": 1,    "geo": {      "lat": 37.421998333333,      "lon": -122.084000000000,      "accuracy": 10,      "type": 1,     // gps        "country": "USA",      "region": "CA",      "city": "Mountain View"    },    "devicetype": 4, // mobile    "make": "Apple",    "model": "iPhone14,3",    "os": "iOS",    "osv": "16.4",    "carrier": "T-Mobile",    "language": "en",    "connectiontype": 2  // wifi  },  "user": {    "id": "c23c88xx93d9e",    "ext": {      "consent": "BOEFEAyOEFEAyAHABDENAI4AAAB9vABAASA"    }  },  "app": {    "id": "com.weather.sunshine",    "name": "Sunshine Weather",    "bundle": "com.weather.sunshine",    "cat": ["Weather"],    "publisher": {"id": "abc123"}  }}
```

注意：

ifa 就是 IDFA / AAID

geo.lat / geo.lon 精度可达 5~20 米

model + osv 用于设备指纹化

carrier, language, connectiontype 用于用户聚类

即使 DSP 不投这个广告，他们也已经收到整个请求

**为何 RTB 会成为“监控公司”的情报来源？**

因为：

### **(1) RTB 数据是“被动广播式”的**

App 只要触发广告请求，这些数据就被自动发送给所有接入的 DSP。

### **(2) RTB 数据可根据 IDFA/AAID 做设备级追踪**

利用广告标识符，一个设备在多个应用中的行为可以实现：

* **跨 app 追踪**
* **跨网站追踪**
* **跨地理位置追踪**
* **跨数月/数年的轨迹**

### **(3) 数据经纪商会把 RTB 数据“二次销售”**

许多国家的数据经纪商会将 RTB 数据打包出售为：

* “人口流动热力图”
* “兴趣人群分析”
* “国家安全监控解决方案”
* “位置智能数据集”

### **(4) 一些监控公司故意注册为“DSP”或“数据公司”**

例如 Webloc 类似的公司，会：

* 注册为 RTB 生态中的 DSP
* 接收所有 bid request
* 不出价，只收集设备数据
* 按 IDFA/AAID 建立一个大型轨迹数据库

#

# **为什么用户定位会被泄露？**

#

因为在 RTB 请求中：

* 如果 App 有 GPS 权限，会直接上传精准坐标。
* Android/旧版 iOS App 很多会默认传递。
* 用户不知道数据会被广播给 100+ 公司。
* 广告方不需要“用户授权访问定位”，他们只需要 App 授权了。

# **Webloc 等公司如何筛选特定设备？**

#

# **核心实际上就是通过设备独特的苹果和安卓广告标识符来筛选设备。**

#

这是典型的 RTB 数据利用方式：

1. 从 RTB bidstream 中收集 IDFA / AAID
2. 存入数据库
3. 为每个 IDFA / AAID 建立设备行为档案：

* 常出现的地点
* 家庭地址（夜间位置）
* 工作地点（白天位置）
* 定期出入敏感设施（大使馆、政府大楼、军事基地等）
* 使用的 App 种类（如约会 App、孕期 App 等）
* 设备型号、系统版本

4. 外部客户可以输入某个 IDFA/AAID
5. 查询这个设备过去几个月的轨迹与行为

这正是为什么 RTB 被批评为“商业间谍系统”的原因。

**RTB 数据泄露的典型风险**

| 风险类型 | 描述 |
| --- | --- |
| 跟踪个人行踪 | 通过 GPS + 时间戳可还原一天行程 |
| 判定敏感身份 | 如访问医院、X教场所、x治组织 |
| 工作单位识别 | 长期白天出现位置可推断工作地点 |
| 家庭住址识别 | 夜间位置固定点 |
| 行为模式分析 | 访问的应用、使用时长等 |
| 国家级威胁 | 某些政府、情报部门可买到这些数据集 |

如果你想自查设备是否被 RTB 广播数据泄露，可以自行手机抓流量查看。

iOS 防护方式

关闭：
**设置 → 隐私 → Apple 广告 → 关闭个性化广告**

虽然苹果宣称 App Tracking Transparency（ATT）很严格，但只要你点了“允许追踪”，App 就能把 IDFA 广播给所有 DSP。

 同时，老生常谈，把定位改为从“始终允许” → “仅在使用 App 时”

因为天气类应用是最大泄露源。

### **还可以关闭后台刷新，因为RTB 常发生在后台刷新中，但黑鸟用了一段时间，手机切换应用一卡一卡的，很不舒服。**

###

Android 暴露更严重，因为大多数 App 默认会上传 AAID，可以选择定期重置 Advertising ID，例如设置 → Google → Ads → 重置广告 ID

现在你该知道，你浏览一次广告之后，什么样的数据被传走了吧？

更多实时情报：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpMibchcmeNze5icd5QqsmxnvkXial3HBkhdiaOVZuibRImicC3BqadiaOVrly82d5AoI0hdB3mia0y1a1Jzw/640?wx_fmt=jpeg&from=appmsg)

参考文档：

https://iabtechlab.com/standards/openrtb/

部分字段通过ai检索获得，人工已经印证真实性。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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