---
title: A10C2攻击机HOTAS整理
url: https://mp.weixin.qq.com/s/3ao3jWhhCizx_8mZgBE5FQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:44:22.796204
---

# A10C2攻击机HOTAS整理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kGhLgo0BUA48rZDNphCyzkNYgyqmKrVIJKuaLA47B21icRavrmYzwOwK0lHRCicjtlazBW33ibvVWdDbAlTSLveZpw8BGCT99hhicGoKrXq3lL8/0?wx_fmt=jpeg)

# A10C2攻击机HOTAS整理

原创

crackme.net
crackme.net

crackme安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kGhLgo0BUA5DvDX0Uyrz8t7CzZsQicYFsM9xfQsyOKz5NqNYVUmQfZo1rwKMibruPUB8Yh6zmcWt4JM2tCZV29NQHo9LVacgurRxRx8hBbVOs/640?wx_fmt=jpeg&from=appmsg)

好久没更新了，水一个文章证明我还活着（

A10C2可以说是你游HOTAS最复杂的机型了，还有一个啪啪奇，然而啪啪奇的HOTAS虽然按键多但上下文关联弱，还有乔治辅助（HOTA George这一块），反而没那么复杂，但是A10这种属于是按键又多上下文关联性也强

接下来就准备更新F-16C航电系统完全注解，参考真机飞行手册

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA7LWEygVD7pEzzJLFR0YcpykULByKPL7rD9BH67o3bS3tuB2lKZtcKmzia13fnibabh0iciadwMDUvBCTsGjmNVWU6Q8YXHKnQzaZQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA6vrOThs6RXJ9TS5TpvnCgojFXWU7YbSqeYIRn5NYZmK8Ckx7tC7xiaIlqIRCKuYzHSE0MSEcARjRfkKVq19EGYTboOBkjLV53Y/640?wx_fmt=png&from=appmsg)

# HOTAS

## COOLIE

| 方向 | 操作 | 说明 |
| --- | --- | --- |
| 前 | 短按 | 设置 HUD 为 SOI |
|  | 长按 | 临时显示 MSG 页面 |
| 后 | 短按 | 设置 HMCS 为 SOI |
|  | 长按 | 临时显示 DSMS 页面 |
| 左 | 短按 | 循环切换左 MFCD 页面 |
|  | 长按 | 设置左 MFCD 为 SOI |
| 右 | 短按 | 循环切换右 MFCD 页面 |
|  | 长按 | 设置右 MFCD 为 SOI |

## CMS

| 方向 | 操作 | 说明 |
| --- | --- | --- |
| 前 | 短按 | 打 1 发热焰弹 |
|  | 长按 | 切换下一个干扰程序 |
| 后 | 短按 | 打 1 发箔条 |
|  | 长按 | 切换上一个干扰程序 |
| 左 | 短按 | 打 6 发热焰弹 |
|  | 长按 | （无功能） |
| 右 | 短按 | 打 6 发箔条 |
|  | 长按 | （无功能） |
| 按下 | 短按 | 执行/停止当前干扰程序 |
|  | 长按 | 开关 ECM |

## DMS

| 方向 | 操作 | 说明 |
| --- | --- | --- |
| 前 | 短按/长按 | “放大”：地图放大（仅短按，TAD）；画面放大（TGP）：下一个导航点（HUD）；增加亮度（HMCS）；小牛空间稳定（仅长按，长按 DMS 同时移动 Slew） |
| 后 | 短按/长按 | “缩小”：地图缩小（仅短按，TAD）；画面缩小（TGP）：上一个导航点（HUD）；减少亮度（HMCS） |
| 左 | 短按 | “切换”：切换武器（HUD）；切换机炮瞄具（A/A）；吊舱画面投影到头显（TGP HMCS） |
|  | 长按 | 开关头显 |
| 右 | 短按 | “切换”：切换武器（HUD）；切换机炮瞄具（A/A）；循环切换本机图标位置 居中/靠下（TAD）；循环切换照射模式 激光L/红外P/混合B（TGP）；循环切换头显配置文件（HMCS） |
|  | 长按 | “隶属视频画面到头显”：隶属 TGP 到头显（除小牛外）；隶属小牛到头显（小牛） |

## TMS

| 方向 | 操作 | 说明 |
| --- | --- | --- |
| 前 | 短按 | “锁定”：钩住符号（TAD HMCS）；切换点跟踪/区域跟踪（TGP）；响尾蛇锥形扫描（A/A）；尝试锁定目标（小牛） |
|  | 长按 | “创建 SPI”：将钩住的符号设置为 SPI（HUD HMCS）；将看向的地方设置为 SPI（除 HUD HMCS 外） |
| 后 | 短按 | “解锁定”：解钩（TAD HMCS）；切换惯性跟踪（TGP）；响尾蛇解锁（A/A）；解除锁定/地面稳定（小牛） |
|  | 长按 | 重置 SPI 为导航点 |
| 左 | 短按 | 清除收到的消息 |
|  | 长按 | 通过数据链向友机广播 SPI |
| 右 | 短按 | “创建标记点”：游标位置设置为标记点（TAD HMCS HUD）；视频画面指向的位置设置为标记点（TGP 小牛） |
|  | 长按 | 将最新设置好的标记点设置为 SPI |

## NWS

| 场景 | 功能 |
| --- | --- |
| 地面 | 开关鼻轮转向 |
| 空中 | 手动照射激光 |

## MMCB

| 操作 | 功能 |
| --- | --- |
| 短按 | 切换 HUD 模式 NAV/GUN/CCIP/CCRP |
| 长按 | 进入 A/A 模式 |

## Boat

| 操作 | 功能 |
| --- | --- |
| 前 | 显示黑热 |
| 后 | 显示白热 |
| 中 | 显示电视图像（除小牛外）；强制跟踪/自动（小牛） |

## China

| 方向 | 操作 | 说明 |
| --- | --- | --- |
| 前 | 短按 | “切换 FOV”：切换为 EXP 模式（TAD）；切换吊舱 FOV（TGP HMCS）；切换小牛 FOV（小牛）；解锁响尾蛇导引头（A/A）；切换到小牛页面并设置为 SOI（HUD） |
|  | 长按 | 隶属所有传感器到 SPI |
| 后 | 短按 | “回中”：回中游标（TAD HUD HMCS）；开关激光点搜索 LSS（TGP）；导引头回中（小牛） |
|  | 长按 | 隶属 TGP 到导航点 |

# 挂载配平

## 方案一：空一挂点

携带短电子对抗吊舱 瞄准吊舱 响尾蛇 空一挂点

一侧放短电子对抗吊舱和瞄准吊舱，另一侧放响尾蛇

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA7IiadrpZcBCQjcXFapQzq1k5qfOia7FD9QI7sib4ebTxGgDKuOZLI3rjicgJMfbFuGq4kc1Giboc1ESDQib1xlhjTotQEiaGBC6gCorw/640?wx_fmt=png&from=appmsg)

| 挂载 | 重量（磅） |
| --- | --- |
| 2 x AIM9M | 831 |
|  |  |
| LITENING | 458 |
| ALQ184（短） | 474 |

## 方案二：携带火箭弹

用方案一的空挂点携带火箭弹

一侧放短电子对抗吊舱和瞄准吊舱，另一侧放火箭弹和响尾蛇

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA6ZcBmF29qAEupUNe5ekdXRJkkL2JIgXDyZbiaNRqJZxZUPMk6nUOR2oqzbKmSxZibUic4TWxjaURooMtNiad2iatS2iaVrUpmTshqto/640?wx_fmt=png&from=appmsg)

| 挂载 | 重量（磅） |
| --- | --- |
| LAU131 激光制导高爆 | 297 |
| LAU131 激光制导穿甲 | 328 |
| LAU131 照明 | 238 |
| LAU131 烟雾 | 229 |

## 方案三：携带末敏炸弹

用方案一的空挂点携带末敏炸弹

一侧放短电子对抗吊舱和末敏炸弹，另一侧放瞄准吊舱和响尾蛇

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA4MZ8mcU1SVujeQ2PzrMiajaUic32haRjLJ5PX2W3ibIKEbIkGVrYFuTtex4dSs0vILeKuJTtp2sEicLEvUQibuHcfJjo9ibW60qgmOo/640?wx_fmt=png&from=appmsg)

| 挂载 | 重量（磅） |
| --- | --- |
| CBU-97 | 919 |

## 方案四：携带宝石路

用方案一的空挂点携带宝石路

一侧放短电子对抗吊舱和宝石路，另一侧放瞄准吊舱和响尾蛇

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA7XKJGFDOXq0GiaxpYGMdgcaRTTBGa2E8icjObDArE2VKomaNsWxquAoXxntW5DZcq05I8ANUv4zA7ic2M4QibY2WKsibSToakXuJAY/640?wx_fmt=png&from=appmsg)

| 挂载 | 重量（磅） |
| --- | --- |
| GBU-12 | 610 |

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f2j8DeXVicRQ9KGpr3vDNkdIwyasHFEWCmJibCSicITuAqbVgkygYicev0lUCVEj7B2XfSpnEhs6o7mVylZW5gzorA/0?wx_fmt=png)

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