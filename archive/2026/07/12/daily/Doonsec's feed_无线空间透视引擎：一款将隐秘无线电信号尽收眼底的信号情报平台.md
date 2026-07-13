---
title: 无线空间透视引擎：一款将隐秘无线电信号尽收眼底的信号情报平台
url: https://mp.weixin.qq.com/s/3oZ3AO8Fa833Cq1s3iNX4Q
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:29:31.487496
---

# 无线空间透视引擎：一款将隐秘无线电信号尽收眼底的信号情报平台

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UpS7xo7cfic1Edsppuibk0Tj9p0LTdMujt43UEEic4WwdoHqjSjgiadB9yJIl91XmJib1UVPxTVZ5UGgCsoOmc6ia1BBEfNicoib6X5XUE/0?wx_fmt=jpeg)

# 无线空间透视引擎：一款将隐秘无线电信号尽收眼底的信号情报平台

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：本工具仅供安全研究、教育及授权渗透测试使用。使用者须遵守当地法律法规，违规使用由操作者自行承担全部责任。

---

## 重点导读概述

WireTapper 是一款无线 OSINT 与信号情报（SIGINT）平台，专注于被动发现、映射并分析周边无线电环境中的设备信号。平台通过监听 Wi-Fi、Bluetooth、BLE、无线摄像头、车辆 RF 信号、IoT 设备及移动基站广播等常见无线协议，实现对周边电磁空间的全面可视化。核心能力包括：发现隐藏无线设备、识别设备类型与厂商、关联网络归属、定位信号源区域，以及基于 k-Anonymity 查询scheme 检测泄漏的 Wi-Fi 凭证。

![主界面](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrPicPElRlXoa4LZMxWxDKCIPiaA34GzrYiazkjgcwvToCjyzX0MlaOl7ANrzpx6vlrtED9gDmzoDOc9ZXnECEKuwCvN8k1NKelE8/640?from=appmsg)

主界面

---

## 重点导读核心技术架构

### PART 01信号感知层

平台支持多协议并发感知，涵盖：

* Wi-Fi：AP 与客户端发现、MAC 地址厂商溯源、SSID 枚举
* Bluetooth / BLE：经典蓝牙与低功耗蓝牙设备扫描
* 无线 CCTV / IP 摄像头：基于设备指纹识别
* 车辆 RF 信号：信息娱乐系统、远程诊断、免钥匙系统信号识别
* 耳机、可穿戴设备及智能硬件
* Smart TV 与 IoT 家电
* 蜂窝基站与移动网络信标

### PART 02数据关联与情报层

收集到原始信号数据后，平台将其与外部情报源关联：

* **Wigle.net**：无线网络映射与历史发现数据
* **OpenCellID**：全球蜂窝基站位置数据库
* **Shodan**：联网设备深度情报（需 Premium API Key）
* **wpa-sec**：分布式 WPA-PSK 审计数据库

![设备分类界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrbEsoX5f9wLoqW8Y7Oc6SNiafn4QA1m7mvorBk7E9HBfn1hyS2Hr1s2s9orvzBXbicDusrLDBaBSbZH67DhOy0qX3Jfb2aYtFA8/640?from=appmsg)

设备分类界面

---

## 重点导读凭证泄漏检测

平台实现基于隐私保护的 k-Anonymity 查询 scheme，通过该机制识别在公共热点或嗅探场景中泄漏的 Wi-Fi 网络凭证。过程中不暴露用户真实查询标识，兼顾情报采集与隐私合规。

---

## 重点导读设备分类引擎

平台内置智能设备分类引擎，通过设备名称或信号特征中的关键字匹配，将检测到的信号源自动归类为以下类型：

* 路由器（router）
* 车辆（car）
* 电视（tv）
* 摄像头（camera）
* 行车记录仪（dashcam）
* 耳机 / 音响（headphone）
* IoT 设备（iot）
* 蜂窝基站（cell\_tower）

![信号地图](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UpwtPlDy0NMjazj6UrleV3y35ubPEzQCNwORTyBsMcqIYLtpJsV7Q2Gus0jiaOoDCFjSgJ2ITj2ZHfc733w6WNbO8R7ZzZQbDrE/640?from=appmsg)

信号地图

---

## 重点导读部署与运行

### PART 03环境准备

```
bashgit clone https://github.com/h9zdev/WireTapper.git
cd WireTapper
pip install -r WireTapper.txt
```

### PART 04API 密钥配置

支持两种配置方式：

**方式一：直接编辑 `app.py`**

```
pythonWIGLE_API_NAME = "your_wigle_api_name"
WIGLE_API_TOKEN = "your_wigle_api_token"
OPENCELLID_API_KEY = "your_opencellid_api_key"
SHODAN_API_KEY = "your_shodan_api_key"
```

**方式二：环境变量或 `.env` 文件（推荐）**

```
bashexport WIGLE_API_NAME="your_wigle_api_name"
export WIGLE_API_TOKEN="your_wigle_api_token"
export OPENCELLID_API_KEY="your_opencellid_api_key"
export SHODAN_API_KEY="your_shodan_api_key"
```

启动服务：

```
bash# 方式一
python app.py

# 方式二
python app-env.py
```

访问 `http://localhost:8080/map-w` 进入信号地图界面。

![地图可视化](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UpjV2icV2so3js88w71azWELEvgqEfGjdcicwoww5VFc3M7Zjm1ciajnFwwhyQ3PsBzHYyPzT9lRAibhiaibC6Roib2O5oCJPBlicHuj1E/640?from=appmsg)

地图可视化

---

## 重点导读技术栈

* **Python**：核心逻辑与 Web 服务
* **Flask**：轻量级 Web 框架，承载地图可视化前端
* **HTML / JavaScript**：前端交互与地图渲染
* **外部 REST API**：Wigle.net、OpenCellID、Shodan、wpa-sec

---

## 重点导读界面预览

![设备列表](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uq6pRN0maiava6ttUr0TutBXXWxA8u8AFaGoSOlamDoHrG8VictohueuvFaeQBdibn2UzP2f2j5aTEWKDCJoIbVzibSZRC1UXpRAjw/640?from=appmsg)

设备列表

---

## 重点导读合规说明

本项目采用 Creative Commons Attribution-NonCommercial 4.0 International（CC BY-NC 4.0）许可证。**禁止将本工具用于任何未经授权的探测、拦截或分析活动。**

---

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/h9zdev/WireTapper
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UpaxTs4SJ43UPlhDhrKdE3bTWykzr32h906JLkqXwlvnlxR3iauOpKFSCRWWfDBISDpv4P74T4DEU4UnzRh7HPDBcguAb2XndOU/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uq9lFZEcRXQl1yJeahmMia5o3uxr5hOZrdjEMWVuHlBJuqwlMXBYcnRyZoP5RvDA5wOlaQrIfm6PyXOmKGSU0v1loLJrRloRB8g/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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