---
title: 【位置技术】不用昂贵工牌，手机+Wi-Fi 也能做1~3米室内定位：Wi-Fi RTT + PDR + 地图约束
url: https://mp.weixin.qq.com/s/78SohTkKzCasO77kaZ_hGw
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:52:07.482011
---

# 【位置技术】不用昂贵工牌，手机+Wi-Fi 也能做1~3米室内定位：Wi-Fi RTT + PDR + 地图约束

# 【位置技术】不用昂贵工牌，手机+Wi-Fi 也能做1~3米室内定位：Wi-Fi RTT + PDR + 地图约束

子午猫
子午猫

网络侦查研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、结论：这套方案适合谁

GPS 一进门就"失明"。仓库、厂房、办公楼若想做员工安全、任务调度与应急响应，又不想配昂贵定位工牌，可直接利用现有 Wi-Fi 与工作手机——但关键不是简单读信号强度。更合适的路线是：**Wi-Fi RTT 测距 + 手机 PDR 行人航位推算 + 楼层地图约束**。三者组合：Wi-Fi 定期给绝对位置，手机传感器还原连续移动，地图避免轨迹穿墙。理想前提是统一配发支持 Wi-Fi RTT 的 Android 工作手机、可部署少量 AP、目标精度 **1～3米**（非厘米级）。

二、Wi-Fi RTT 为何比信号强度靠谱

RTT（Round-Trip Time，往返时间测距）基于 IEEE **802.11mc FTM** 能力，测数据包在手机与 AP 间往返时间估算距离。手机同时测得自身到 **4个** 已知坐标 AP 的距离，即可多边定位解算位置。Android 9.0 起提供 RTT API，3 个以上兼容 AP 典型约 **1～2米** 精度；务实验收目标应设为空旷 **1～3米**、复杂房间 **2～5米**。注意：手机不必连接这些 AP 也能测距，但两端硬件驱动须支持；"Wi-Fi 6 路由器"不等于支持 RTT，须确认 FTM Responder 或 802.11az。

三、为何还要 PDR 与地图匹配

RTT 适合绝对定位却不适合高频更新，人员行走时只靠间歇 RTT 坐标会跳动折线。手机自带加速度计、陀螺仪、磁力计、计步器、气压计，PDR 据步数/步长/方向推算连续移动，但误差随时间累积，RTT 恰好定期拉回。工程上用扩展/无迹卡尔曼滤波或粒子滤波融合，走廊房间明显的建筑用粒子滤波加地图匹配更易表达"不能穿墙、只能从门口进"。手机上传的是轻量位置（匿名 deviceId、坐标、楼层、精度、时间），非原始传感器洪流。

四、落地六步与降级路径

部署六步：①检测手机 FEATURE\_WIFI\_RTT、开权限（Android 13+ 处理 NEARBY\_WIFI\_DEVICES）；②确认 AP 支持 FTM，每区域至少 **4个** AP 分散四周留冗余；③以西南角为原点激光测绘 AP 的 BSSID/楼层/X/Y/高度；④先纯 RTT 静态采 20～30 点各 30～60 秒；⑤加 PDR 与地图匹配（步长按身高估算再校准，磁力计在金属区不可作真值）；⑥最后做多人并发与后台运行（运动时高频、静止低频降耗）。无 RTT AP 时可降级：RTT+PDR → Wi-Fi 指纹（KNN/随机森林）+PDR → 仅 PDR 短时维持 → 入口二维码重初始化。

五、预算与隐私边界

主要成本不是服务器，而是支持 RTT 的 AP、现场测绘与手机适配；最小验证版需 3～4 个 FTM AP、2 部兼容 Android、楼层图、激光测距仪。更推荐从企业工作手机小范围试点起步。员工行踪属敏感个人信息：上线前须明确目的与充分必要性，履行告知、评估与同意；技术上优先用不可直接识别的设备标识、账号与轨迹分离保存、仅必要区域时段启动、地图查看/轨迹导出分级授权并留审计、到期删除。iOS 未向普通第三方 App 开放通用 Wi-Fi 扫描，混合部署需 AP 侧定位、BLE 或 UWB 补充。

低成本室内定位的真义，不是"一个路由器定位整栋楼"，而是承认每种技术边界：RTT 解绝对测距、IMU 解轨迹连续、地图解空间约束、指纹管兼容降级；先在一层楼做最小验证，把95%误差、功耗、房间识别率测出来，再决定是否扩部署。

![](https://mmbiz.qpic.cn/mmbiz_jpg/mQFl6fQOc0qYsibcLKMqWicoxO18ksI2ujiaUoYzddBq3al8mXBEm4cicxruhgeaoQAhKENjTTL39UXVVK370Wz2cjOoLib6JAquRGj2aRWjImiaQ/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mQFl6fQOc0qgGKhYhP9c1JhqkjJVLrnCZdFnOPVwib14GM4xCibvxTjxgwFfBuyqse1G8ibRVP5BJkSI3QxTSWTQPfJKqtWPEOoibhN9hRUFKaM/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2b9Dn5TZppcYVNqtewpGLM6TUkWg29ayK9yWAJbqViaE15Ltf8AprRumW3Lmw3ibHOAsMYMnhNqcfiaA/0?wx_fmt=png)

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