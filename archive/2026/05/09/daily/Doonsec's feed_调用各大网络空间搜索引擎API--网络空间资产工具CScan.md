---
title: 调用各大网络空间搜索引擎API--网络空间资产工具CScan
url: https://mp.weixin.qq.com/s/n0spZqIStIcKtXjbMDBbTQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:28.577184
---

# 调用各大网络空间搜索引擎API--网络空间资产工具CScan

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZMyIuHTOaapf9YcGjeyiatJuicCXVp9kQDGhBWNqEXpRnLAhp4oiaUWtnRmtaMic3fF2DBiaxib0lPh1fDYUrgAx5IwwpFzicnWTtjsjoApbaMlBiag/0?wx_fmt=jpeg)

# 调用各大网络空间搜索引擎API--网络空间资产工具CScan

原创

kris卢
kris卢

网络安全研习社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在信息收集的时候，经常需要处理大量IP地址、域名和企业名称等资产信息。传统的手动资产搜集方式效率低下且容易出错。CScan旨在通过自动化工具调用各大网络空间搜索引擎的API接口，快速完成资产搜集工作，显著提升工作效率。

CScan主要解决以下痛点：

1.手动搜集资产耗时耗力

2.多个平台API调用繁琐

3.结果格式不统一

4.缺乏统一的速率控制和错误处理机制

一、功能特性

**多引擎支持**：集成Hunter、FOFA、Quake、Zone等多个网络空间搜索引擎

**资产类型**：支持IP、域名两种目标类型

**批量搜索**：支持批量处理目标列表

**结果导出**：自动将搜索结果导出为Excel文件

**速率控制**：内置API调用速率限制，防止触发平台限制

**错误处理**：自动处理API错误，支持指数退避重试

二、安装说明

**方式一：使用预编译二进制文件**

1.根据系统架构下载对应版本：

Windows: cscan\_windows\_amd64.zip

Linux: cscan\_linux\_amd64.tar.gz

macOS: cscan\_darwin\_amd64.tar.gz

2.解压下载的文件

3.运行二进制文件

**方式二：从源码编译**

1.确保已安装Go 1.18+环境

2.克隆项目：

git clone https://github.com/T3nk0/cscan.git

cd cscan

3.安装依赖：

go mod tidy

4.编译项目：

go build -o cscan cmd/main.go

三、使用效果

![](https://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaaqSc4qpj9dEXEicSXYGKB4Dt0o75h7bloruMd1bnw74MT4MiaQ6HPhQb41ibFNykxumbSRZPVpra1AVJ1XibLrqnPMlicib79PeibNmeE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaardQxNo5icia3Zbr4wRQ0H62oMlgjRblphu9poRianljMOr1AsCueicibNjReV2QZeODRoFiazpcvTY7nvOcY3ULmSKcHqicq1ibtjV7b4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaaoWcZCGvYFJZfKLkNlO3a6fIhQmibl0EiaWGricLgCnsfwLQfOuap1vbIc6N06K4ibwj9iaJpDibVy7efcV0ojz8iaeEYOQ55tLSSDATI/640?wx_fmt=png&from=appmsg)

四、使用说明

**基本用法**

|  |
| --- |
| ./cscan -m <module> [options] [submodule] |

**参数说明**

| **参数** | **说明** |
| --- | --- |
| -m | 模块选择 (cse/co) |
| -f | 输入文件路径 (默认: target.txt) |
| -o | 输出文件路径 (默认: results.xlsx) |
| -v | 显示版本信息 |

**模块说明**

**1.****网络空间测绘****(cse)**

|  |  |
| --- | --- |
| # 使用所有引擎搜索  ./cscan -m cse -f targets.txt -o results.xlsx  # 使用指定引擎搜索  ./cscan -m cse hunter -f targets.txt -o hunter\_results.xlsx | |

支持子模块：

* hunter: Hunter引擎
* fofa: FOFA引擎
* quake: Quake引擎

**2.****公司情报****(co)**

|  |
| --- |
| ./cscan -m co -f companies.txt -o company\_assets.xlsx |

支持子模块：

* zone: Zone引擎

五、配置说明

    首次运行程序时，如果当前目录下不存在config.json文件，程序会自动创建配置文件模板。

配置文件config.json需要包含以下内容：

|  |
| --- |
| {   "hunter\_api\_key": "your-hunter-key",   "fofa\_email": "your-fofa-email",   "fofa\_api\_key": "your-fofa-key",   "quake\_api\_key": "your-quake-key",   "zone\_api\_key": "your-zone-key",   "max\_page": 10,   "page\_size": 100  } |

六、示例

**搜索****IP****资产**

1. 创建目标文件targets.txt：

|  |
| --- |
| 192.168.1.1  8.8.8.8 |

执行搜索：

|  |
| --- |
| ./cscan -m cse -f targets.txt -o ip\_results.xlsx |

搜索公司资产

创建公司列表文件companies.txt：

|  |
| --- |
| 阿里巴巴  腾讯 |

执行搜索：

|  |
| --- |
| ./cscan -m co -f companies.txt -o company\_assets.xlsx |

七、注意事项

1. 请确保已获取各平台的API Key并正确配置

2. 建议控制目标数量，避免触发平台限制

3. 输出文件为Excel格式，建议使用Excel或WPS打开

4. 程序内置了API调用间隔，请勿手动调整

最新CScan下载地址

---

点击公众号后台

回复关键字【20260509】获取下载链接

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaarQelXTaickmCYWRMv2UmKTbA7SceBZQ4pjiagPgsiagy6ibYbiajVRxelHcfkviamLYZumX2fKWFndK6uwtEKP5JpJ9hC1kwxYY3y6k/0?wx_fmt=png)

网络安全研习社

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaarQelXTaickmCYWRMv2UmKTbA7SceBZQ4pjiagPgsiagy6ibYbiajVRxelHcfkviamLYZumX2fKWFndK6uwtEKP5JpJ9hC1kwxYY3y6k/0?wx_fmt=png)

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