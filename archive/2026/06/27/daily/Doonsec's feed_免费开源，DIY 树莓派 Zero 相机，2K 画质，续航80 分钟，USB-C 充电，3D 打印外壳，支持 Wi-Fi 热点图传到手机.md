---
title: 免费开源，DIY 树莓派 Zero 相机，2K 画质，续航80 分钟，USB-C 充电，3D 打印外壳，支持 Wi-Fi 热点图传到手机
url: https://mp.weixin.qq.com/s/a2B60yXx5_qkSCB-RfdS-Q
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:13:06.588733
---

# 免费开源，DIY 树莓派 Zero 相机，2K 画质，续航80 分钟，USB-C 充电，3D 打印外壳，支持 Wi-Fi 热点图传到手机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUhjgmF9q8DpFcUhxNFqz9sfClsibPeqp643Y7b74Dib7UOFkGAFGmibiaZmyOsPYVgyKZfL5ClIZMhb2rZl6SWyoYwl3ltltAXXYDY/0?wx_fmt=jpeg)

# 免费开源，DIY 树莓派 Zero 相机，2K 画质，续航80 分钟，USB-C 充电，3D 打印外壳，支持 Wi-Fi 热点图传到手机

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUjNUSG4GwQmydhpsSW4z4TNJPXEQVCf7mlEcOicNf9Tmk4YxhCwHXU7VXdowR6tZ8EPCBzeP7GHfkV8cZppfyrkCqKlHtbfBSWY/640?wx_fmt=jpeg)

> 文末获取项目源码和完整3D打印资料

Optocam Zero 是一款软硬件全开源，基于树莓派 Zero  2 W 开发板打造的数码相机，配有1.4 英寸 LCD 显示屏，分辨率为 240×240 像素，可拍摄 2592×2592 像素的 JPEG 图像，支持 GIF 录制和回放，内置14500 型锂离子电池，单次充电可持续使用 70–80 分钟。

Optocam Zero 体积小巧、能随身携带、充满拍照乐趣的相机，所有外壳零件都可以 3D 打印，电子部分也采用成熟的零件组装。黄色半透明外壳，小屏幕，摇杆，背面还有一颗相机模组。

* 可拍摄 2592×2592 像素的 JPEG 图像
* 可录录制和回放 GIF 小视频
* 屏幕预览帧率在 15–20 fps摄像头支持自动对焦模块。
* 系统内置 8 种风格照片滤镜。
* 可通过Wi-Fi热点实现快速、简便的把照片传输到手机和电脑
* 自动息屏，屏幕自动变暗，节省电量。
* LCD 显示屏 1.4 英寸 ，分辨率为 240×240 像素
* 支持 USB-C 充电，14500 型锂离子电池，单次充电续航70–80 分钟，可快速更换电池
* 外壳部件完全采用 3D 打印制作，牢固可靠。
* 配件有 TPU 保护套和挂绳设计。
* 体积非常小巧，外形尺寸 51×71×18 mm可轻松放入口袋随身携带。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjlmPIZLxuNL7YPdgN86t69vIQqxdjtGUmPtibmMoMcBQ7RZkaHouXgk4dia9npcuqbNeaHDYKUlRFCsLCtgzIumE7YDj6GrzwIQ/640?wx_fmt=png&from=appmsg)

## 🤖 快速开始

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiandWFjibz3Sam3z0vwpUicg4rbTPgCxScBXCjjpASThcAXYRE5MZia9AXqZiccqUKCGDY3NfI7nhEHByDD6SvNCZqev1sr93NjZZo/640?wx_fmt=png&from=appmsg)

硬件组装

Optocam Zero 核心电子部分基本都是现成 HAT 和模块，其中树莓派 Zero 2 W 开发板在中间，Camera Module 3 通过 CSI 排线连接，LCD HAT 采用 40pin GPIO串口，供电使用 Waveshare Li-ion Battery HAT，通过拆改电池座、部分连接器和排针把各个模块压缩在较小的体积里，14500 电池触点用 JST 线引出来；LCD HAT 右侧按键拆掉后，最上面的 KEY 焊盘用细线引出，变成快门键。

### ![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhOmpr4cR9YCBsDW1wY8O1HrZcTaoECvaykzyzaGpJgHMnaxYbmTZgZSWAhOl40frM9WzeEgTvPSRnZhJIMhZicbVRyTLhK4my4/640?wx_fmt=png&from=appmsg)

### 软件编程

软件系统采用标准的树莓派框架，先用 Raspberry Pi Imager 刷 Raspberry Pi OS Lite 32-bit Bookworm，打开 SSH，第一次启动后登录进去，默认执行脚本 install.sh。安装过程大概 10-15 分钟，重启后相机程序自动启动。

相机操作界面逻辑不复杂，摇杆左右切色温，上下切滤镜，中键进相册；快门键拍照，长按快门切 GIF/Photo 模式。保存图片时底部有加载圈，打开相机Wi-Fi热点传图后，可在手机浏览器里查看照片和视频、一键下载到手机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiasYAQDsubhZvZjqic1wqIfZx8MtTHa0Vf5dXIHqMc7JlicdHFnLia4ffupgfZjr6PDc9S6TYXiaMONicclmNG0RwcV8sn396IGC6hE/640?wx_fmt=png&from=appmsg)

## 🌟 真机摄影作品展示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh4IAsdibtRx7s453icrvFBicBnCHvrgCms3IgvArf9lx0F7VjQZ2gGskEXNqNBYoic7JktDVyjWogtZic1jJ1CJDgj48GVzHhvThN0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjOZtPq27NJwiaZv91ORJUCC6QOB3JKJJXjVw00WGWNtAZgKNMEHkk5z2nBiaeH5VJFQVeuibo7yvUDicLDLrhCwEmvDEkNOQjBQwM/640?wx_fmt=png&from=appmsg)

🌳 写在最后

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgrnj9sXr2HtbxqZkwlvKD5iapEzdFvJEC8ySP8OIcQvxgo3xjRny2fu6XW0ksLuh7Iia1I3IAUFSccMLwQcmicvkkiaeG3iaoZYNtA/640?wx_fmt=png&from=appmsg)

Optocam Zero 硬件成本大约在 100 到 120 美元之间，项目软硬件100%开源，其中software 文件夹中包含了开发所需的相机软件安装程序、安装指南以及相机控制信息；hardware 文件夹包括物料清单（BOM）、PDF 版组装指南、Bambu Studio 项目文件、相机各部件的独立 STL 文件以及用于定制的 CAD 文件。

如果你对摄影感兴趣，不妨亲自动手攒一台树莓派 Zero 小相机！

🔗 GitHub：dorukkumkumoglu/optocamzero

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