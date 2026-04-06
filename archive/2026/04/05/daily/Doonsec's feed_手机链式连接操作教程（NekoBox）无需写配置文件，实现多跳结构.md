---
title: 手机链式连接操作教程（NekoBox）无需写配置文件，实现多跳结构
url: https://mp.weixin.qq.com/s/L-lYock8-EbjXeNa7T_y0g
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:49.502465
---

# 手机链式连接操作教程（NekoBox）无需写配置文件，实现多跳结构

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjXAibT9fia8kyD58DXZDMv8IF6SDuiaibS2OfOH8R4iafj72tdGlbqgb65Ghe0Nm6ZZF1V2tiaiakC2Sfcs13fZBdQppat4ibiaKgSiagMqs/0?wx_fmt=jpeg)

# 手机链式连接操作教程（NekoBox）无需写配置文件，实现多跳结构

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器中沉浸阅读

在移动端使用代理时，默认都是单线路出站：设备 → 线路 → 目标。这种结构简单，但在需要控制出口路径或组合不同线路时，会明显受限。

链式操作的核心作用，是把“单一出站”拆分成“多跳路径”。也就是将入口线路与最终出口解耦，通过顺序串联，实现：设备 → 线路A → 线路B → 目标。

问题在于，大多数客户端依赖配置文件才能实现这一结构，对用户来说门槛较高。

本文基于安卓端客户端，通过可视化操作完成链式的搭建，不涉及复杂配置，直接实现多跳连接。

📦 一、下载安装

首先安装客户端：NekoBox for Android

下载方式：

在 GitHub 搜索：

```
MatsuriDayo/NekoBoxForAndroid
```

📱 安装包选择说明

|  |  |
| --- | --- |
| 版本 | 适用设备 |
| arm64-v8a | 大部分安卓手机 |
| armeabi-v7a | 老旧设备 |
| x86 | 模拟器 |
| x86\_64 | 模拟器/PC |

👉一般直接选 **arm64-v8a**

## ➕ 二、导入普通代理

##

打开软件后：

1. 点击右上角 **➕**
2. **选择：**

```
从剪切板导入
```

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXj5PDDRKUuhzCvNQXmb9rmINvdtFib2b5SdQicoOGGvXuPzLBhlVAMLmlMdp0YZ8fQ7UlZlZeZiaY87xBZ02sDsRmec2EV8ybQ94/640?wx_fmt=png&from=appmsg)

**👉 导入你的普通代理（第一跳）**

**🗂️ 三、新建分组（用于第二跳）**

1. **点击左上角 **≡****
2. ****进入：**分组******
3. ******点击右上角 **≡+********

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXNaGpokn0MJrva6hJDvzYtqycWvnOvuYGD5Sh3iaibyZYKZjicg4X14o5icqflBhyH5D3NH1QuINYz2FOVetxBVtu7JzhP7LDwhAU/640?wx_fmt=png&from=appmsg)
4. ****新建分组（例如命名为：住宅IP）****
5. ****保存****

********🌐 四、添加第二跳线路********

1. ****回到配置页面****
2. ****进入刚创建的分组（住宅IP）****
3. ********点击右上角 **➕**********
4. ****选择：****

   ```
   手动输入 → Socks
   ```
5. ****填写你的第二跳信息（IP + 端口 + 用户名 + 密码）****
6. ****保存****

**********🔗 五、设置链式连接（关键步骤）**********

1. ****再次进入 **分组界面******
2. ******找到“住宅IP”分组******
3. ******点击 ✏️（编辑）******

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXj6rIteJ8qPgGSXQCgqqTwXH4evl1WHbVf0xQctmGwr3bsEPkJibqyyPfge06DIauibZ6G1zjWjDH07D2RptwdkVribP0wzwIMU8/640?wx_fmt=png&from=appmsg)

****设置前置连接：****

```
前置代理 → 选择配置
```

****👉 选择你刚刚导入的普通线路****

****🔁 此时结构为：****

```
设备 → 基础节点 → 住宅IP
```

****👉 链式完成****

****▶️ 六、启动并测试****

1. ******回到配置界面******
2. ******选中“住宅IP”线路******
3. ******点击下方飞机图标启动。******

****✅ 验证方法：****

* ******查看是否有延迟显示******
* ******打开浏览器查看当前地址******

****👉 如果显示为第二跳的IP，说明链式成功****

****🌍 七、（可选）开启全局模式****

****如果你需要所有流量统一走该路径：****

****进入：****

```
设置 → TUN 实现
```

****修改为：****

```
System
```

****⚠️ 八、注意事项****

****1️⃣ 顺序不要搞反****

```
入口线路 → 出口线路
```

****2️⃣ 第二跳必须可用****

****否则会出现：****

* ******无法连接******
* ******无延迟******
* ******无法使用******

****3️⃣ 多一跳会增加延迟（正常现象）****

****到这里整个链式操作就结束了，通过NekoBox，可以用比较直观的方式完成这一套操作，不需要手写复杂配置文件。****

****本期内容到此结束。****

三连加关注，追文不迷路。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_02.png)

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