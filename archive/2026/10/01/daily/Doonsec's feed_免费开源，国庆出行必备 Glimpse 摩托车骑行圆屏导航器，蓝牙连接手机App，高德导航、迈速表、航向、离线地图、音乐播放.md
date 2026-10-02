---
title: 免费开源，国庆出行必备 Glimpse 摩托车骑行圆屏导航器，蓝牙连接手机App，高德导航、迈速表、航向、离线地图、音乐播放
url: https://mp.weixin.qq.com/s/lT2fKgiAf-dOoWV-zxG9mA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:35.896093
---

# 免费开源，国庆出行必备 Glimpse 摩托车骑行圆屏导航器，蓝牙连接手机App，高德导航、迈速表、航向、离线地图、音乐播放

# 免费开源，国庆出行必备 Glimpse 摩托车骑行圆屏导航器，蓝牙连接手机App，高德导航、迈速表、航向、离线地图、音乐播放

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhshE2nzWfFAicRUiaQSvoibc03KGqw4YwwFbwdz9icx5EgicbVnibwCn91ccDWehD2vZf1g1U1LU9hH3dGG4D0mw3EFfJQVRmlrSwcU/640?wx_fmt=png&from=appmsg)

> 高德导航、迈速表、航向指引、音乐播放

Glimpse 是一款软硬件全开源的摩托车极简导航与仪表设备，基于乐鑫ESP32-S3主控，1.75 英寸圆形 AMOLED 屏幕，通过蓝牙连接 iPhone 手机的高德导航，实现实时定位、地点搜索、路线规划等功能，小圆屏专注绘制最简洁的导航画面，包含迈速表，下一个路口行驶方向、目的地距离，同时可以遥控手机音乐软件，播放音乐。

骑行出发前，你可以在手机 App 里搜索目的地，对比路线的时间和距离。开始导航后，转向提示会同步到圆屏。

* 导航规划：手机承担 GPS 定位、高德地点搜索、路线规划与离线地图缓存，最多对比三条候选路线，选定线路数据通过蓝牙传输到 Glimpse 。
* 开始导航：Glimpse 设备端负责导航、速度、行进航向，专注绘制当前路段，不存储整城地图，默认缓存上限 128 MB、可手动调整到 512 MB。
* 屏幕操作：左右滑动，可切换页面，控制音乐播放。侧键长按 3 秒可由 AXP2101 PMIC 执行电源关机。
* 蓝牙通信：自带分片重组、CRC 校验、加密配对；已通过 9 组 C++ 原生测试、60 项后端测试、12 项 Swift 核心测试。

**圆屏导航**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaib4AyGSgvXC3OAQQiaDhkosCuk2iczWdnfNOl9ZcdTO84YekypTWu58kvrl9FicvL1SkV2FxRODMtstqTib1lFxiavWGCj8LxIaIF8/640?wx_fmt=png&from=appmsg)

导航信息显示在466×466 像素的圆形显示屏中，以黑色为底，白色路线和转向提示是画面的重点， 每种元素都有明确含义：

| 画面元素 | 表达的信息 |
| --- | --- |
| 固定车头箭头 | 当前行进位置的视觉锚点，指向屏幕前方 |
| 白色粗线 | 当前导航路线在附近的走向 |
| 灰色细线 | 周围道路的实际几何形状，帮助辨认路口、支路和道路关系 |
| 灰色建筑块 | OSM 中收录的建筑轮廓，提供街区和园区参照 |
| 左下动作图标 | 下一个路口的直行、左转、右转、掉头等动作 |
| 动作旁的大号距离 | 距离这个动作还有多远，按距离切换 `m` / `km` |
| 限速牌 | 已有显示结构，但真实道路限速尚未接通；缺少数据时隐藏 |
| 底部圆弧 | 路线完成进度，颜色随当前路况状态变化 |

例如屏幕显示右转箭头和 `300 m`，意思就是沿当前路线行驶约 300 米后右转。 接近路口时，距离逐渐减少；通过路口后，图标和数字更新为下一项指引。

行驶和转弯时，路线、周边道路和建筑使用同一组位置、航向和缩放参数。 车头箭头保持固定，地图在它下面平移、旋转，便于连续观察前方道路。 圆屏聚焦当前路段，出发前的全程路线由 iPhone 的预览地图展示。

导航程序根据连续定位更新路线进度、下一动作距离、剩余路程和预计剩余时间。 手机App导航页同时显示目的地、圆屏连接状态、定位状态与当前路况。

偏航判断结合偏离距离与连续定位确认，定位质量、请求编号、路线版本都参与状态更新。

红绿灯倒计时和当前道路限速数据尚未接通。

**地点搜索与路线选择**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjXZuNicGQqTqQibadKVFQrtw4jTjkIIn1M9NKCVNJ6kjy3mVUCll8m2p4ZFfLk7w7BxQ2JSakRpLxPgfHIyH82pDlmWC3bMw3Wc/640?wx_fmt=png&from=appmsg)

### iPhone App 使用高德地点搜索与普通驾车路线服务。搜索时会带上手机当前位置， 优先呈现附近、相关度较高的地点。在济南输入“奥体中心”这样的关键词即可开始检索， 也可以输入带城市名的外地地点。 当前是普通驾车路线，不保证避开摩托车禁限行道路。

搜索与选路流程包括：

* 输入至少两个字开始搜索，连续输入时合并请求，按最新关键词更新结果。
* 搜索结果显示地点名称、地址或所在区域；有当前位置时可展示距离。
* 选择地点后保存到最近地点列表，按使用顺序保留 **8 条**，重启 App 后继续保留。
* 点击最近地点可重新规划前往该处的路线，也可以一键清空历史。
* 规划前刷新起点位置，再向网关请求候选路线。
* 按高德实际返回结果提供 **最多 3 条路线**，以推荐路线、备选路线展示。

路线确认页会显示起点、终点和整条路线。选中的路线高亮，其余候选以浅色显示。 下方卡片列出各条路线的距离、预计时间和分段路况摘要，例如“路况顺畅”“部分路段缓行”。 点击卡片切换方案，确认后再点击“开始导航”。

开始时会将选中的路线交给导航核心；如果预览后起点已经明显移动，程序会从当前位置 重新规划。路线确认与真机显示的一致性是当前持续回归测试的项目之一。

**马表与航向页**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjejhB6IQ8fa2PluBH2wnE2euL9c41a6mQib1RnKSI4VwuMhIDxAvkVdBuxF2HnqR0kQJcVAw4J7VpsCiaibLjecIDZBc5nVjvFTI/640?wx_fmt=png&from=appmsg)

### 马表页以大号数字显示当前速度，单位为 `km/h`，外圈刻度和圆弧随速度变化。 页面围绕实时速度设计，适合在圆屏上快速读取。

航向页显示角度、方位字母、旋转刻度和当前速度。手机定位提供行驶方向， 圆屏上的 QMI8658 六轴传感器提供短时角速度，用于补偿转动过程中的显示变化。

**音乐播放控制**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhvBx86XJJOoL1bic1XHM1XLuECFxRagNPicLQWdulUzNrVJpRlTdYttJKfYW33j43xtEOmZGjgxIuMlKOhJqYJcia72R8KvCUfHg/640?wx_fmt=png&from=appmsg)

### 音乐页通过 iPhone 的系统音乐播放器控制 Apple Music，显示音乐来源、曲目标题、 歌手和播放状态。圆屏提供上一首、播放/暂停、下一首三个操作按钮。

声音继续沿用 iPhone 当前的音频输出，例如头盔蓝牙耳机。圆屏承担显示与遥控， 适合与手机现有的音乐播放方式搭配使用。

**开发调试**

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaPpmFVSWc7upKycDWy4jNo1NDQUQqt2fdsXHE1o3KMQd78Jb60eolju0LIib0ul3d0XVOJboPpnS0Jqiclne7Ef788iaicaWapaIc/640?wx_fmt=png&from=appmsg)

硬件配置： Waveshare 1.75C 开发板 + iPhone iOS 17+ ；编译须 Mac（Xcode 16+ / Swift 6）；固件基于乐鑫 ESP-IDF 5.5.5，网关基于 Node.js 20+

软件编译：推荐 git clone --recurse-submodules，若直接下载 ZIP 源码，需手动补齐 third\_party/lvgl/ 子模块代码。

运行 xcodegen generate 前，必须先在 project.yml 中配置自建网关 URL、Bundle ID 和 Team ID。

授权Key：导航需自行申请高德 Web Key 并部署 HTTPS 网关

```
hardware/
  pcb/
    moto-gps-rev-a.kicad_pro
    moto-gps-rev-a.kicad_sch
    moto-gps-rev-a.kicad_pcb
  libraries/       经复核的自建符号、封装与 3D 模型
  mechanical/      参数化外壳、STEP、STL 与 2D 加工图
  manufacturing/   Gerber、钻孔、BOM、CPL 和装配说明
  validation/      上电、RF、GNSS、罗盘、功耗和环境测试记录
```

关键接口：

* 屏幕与触摸 FPC 接口：电气映射已整理，连接器接触面、Pin 1 与 FPC 厚度仍须用原装屏实物确认。
* LC76G 与 GNSS RF 接口：裸模组、低噪声供电、UART/PPS、U.FL 有源天线基线和塑料 RF 窗约束。
* 电源架构冻结条件：主方案已改为 BQ25628E + TPS63070 + TUSB320LAI，完整主板前须先通过独立电源测试券。
* Rev A0 参数化外壳：铝前框、塑料后壳、独立 RF 舱和可替换车把卡口概念件。

Github 开源项目：mx3353672833-debug/moto-gps-waveshare

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiammPZaNSh2HzseQoJ9bNzUSCR9jaK8eBlwD7hS4Qc7LH5ZWOb8IrvxwhaqLcic14VbJIiaWQk4ffEylWbhyeMiaM2q1SaV1EmX40/640?wx_fmt=png&from=appmsg)

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

☞[上班摸鱼， 树莓派DIY智能 AI 视频算法监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

☞[一站式AIoT视频聚合平台，适配国标28181和国密35114协议](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946211&idx=1&sn=0072cf454ac83d98adb64c5767e58901&scene=21#wechat_redirect)

☞[“空中奇兵”无人机多光谱罂粟巡查平台，识别出苗期、花期、果期](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946024&idx=1&sn=6b7d30937351bcce27a0d930c5727726&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请及时告知，我们将尽快处理。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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