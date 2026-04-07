---
title: 开源免费！国内最强AIoT物联网视频管理平台，Python开发基于ZLMediakit框架，支持GB/T 28181新国标，适配海康、大华、宇视
url: https://mp.weixin.qq.com/s/pGt7vhlqUzAmj_l8ZOPIlQ
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:26:35.712246
---

# 开源免费！国内最强AIoT物联网视频管理平台，Python开发基于ZLMediakit框架，支持GB/T 28181新国标，适配海康、大华、宇视

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUgIx7CiaS8aFZK95WNBpX09scpWuUuWjNiaGv5eTmQvjLv5cZkgWicYUF3iby6IZZZVye6R3OyNEOKicEl61Q5MfDxC0dJlCYI5JaXk/0?wx_fmt=jpeg)

# 开源免费！国内最强AIoT物联网视频管理平台，Python开发基于ZLMediakit框架，支持GB/T 28181新国标，适配海康、大华、宇视

原创

.
.

IoT物联网技术

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhZ3L8szMtntVqbJPQMjCtHxY9FEVMJPLHxzDwOhydzDk0OznKiapxw8fuFr9yCB5L5c38qhMOzqNU19kP3MaXWKQPyAoBT6ewM/640?wx_fmt=png&from=appmsg)

> 文末联系小编，获取项目源码

👁[5万元，一网统飞，无人机智能AI巡检交付（附架构图）](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

PyMKUI 视频管理平台是基于ZLMediakit框架采用Python语言开发的适配GB/T 28181 新国标协议的视频监控平台，兼容GB/T28181-2016、GB/T28181-2022版本，实现设备与用户端到端打通、闭环信令服务、流媒体服务，实现了视频流媒体的接入、转发与管理功能，可满足安防监控、智能交通等场景下的视频业务需求，提供设备管理、实时预览、录像回放等核心功能，是构建国标视频平台的完整解决方案。

PyMKUI视频管理平台兼容海康、大华、宇视、水星等主流品牌IPC/NVR/ONVIF物联网设备，IoT物联网项目交付中能充分利旧。包含如下功能：

🎬 视频流管理 — 查看、播放、停止流，获取截图

📡 拉流代理 — 多备用地址、按需/立即模式、自动故障切换、持久化恢复、在线编辑

🔄 转协议预设 — 保存多套转协议参数，拉流时一键加载，支持加载服务器默认值

👥 观众列表 — 实时查看每路流的在线观众及连接信息

📊 服务器监控 — CPU、内存、磁盘、网络实时图表

⚙️ 服务配置 — 在线读写 ZLMediaKit 配置项

🌐 在线推流 — 基于 WHIP 协议的浏览器端直播推流

🔗 网络连接 — 查看和管理当前所有 TCP/UDP 会话

PyMKUI视频管理平台支持原生 HTML5 视频播放，FLV 播放，WebRTC 播放。

## 🚀 平台架构和部署

项目结构

```
pymkui/
├─ frontend/          # 静态前端页面
├─ backend/           # Python 插件与 FastAPI 接口
│  ├─ mk_plugin.py    # ZLMediaKit Python 插件入口
│  ├─ py_http_api.py  # FastAPI HTTP API
│  ├─ database.py     # SQLite 数据库
│  ├─ config.py       # 路径配置
│  ├─ mk_logger.py    # 日志封装
│  └─ shared_loop.py  # asyncio 事件循环共享
├─ data/              # 运行时自动生成
│  └─ pymkui.db       # ⚠️ 升级时请删除
└─ README.md
```

安装部署

PyMKUI视频管理平台采用Python开发，编译依赖 ZLMediaKit 框架

```
# 克隆项目
git clone https://github.com/ZLMediaKit/pymkui.git

# 进入后端目录
cd pymkui/backend

# 安装依赖
pip install -r requirements.txt
```

Docker 镜像部署

```
docker run -id \
  -p 1935:1935 \
  -p 80:80 \
  -p 443:443 \
  -p 554:554 \
  -p 10000:10000 \
  -p 10000:10000/udp \
  -p 8000:8000/udp \
  -p 9000:9000/udp \
  zlmediakit/zlmediakit-pro:feature_all
```

## 🌟 平台演示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhjLic86d0ZY7NLWSn9wB9kDOCrQv93Ogw08d7BsFjf4cBIzX5kIvF09ze0WYevFo03hnZmBYRric8ibxnaIGD1897SicnUaeW6cZ8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaeECQGoP9hSFwT34YnfEkO5Lg60hx5zh6ub1Z0LDicJAOicDo1CsbPDFicdSoXOCTuQT9kE2icHeOu5AuDF46jfXJho4bARV3POXE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjojSIeMAVsPau8ictrF2czfwj4fc2qoniaMBhTHTN6NR0xVrRa63wDF9UNcxAhcNMXX6XaHLiaS5dicgSfnSQeKnYPBicljuV2gXias/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUjy5fI8EkIy9fDicMSIbfOq01ZSToqRQvxDAiaHogjNq6vTGiaoGSoDUuNTqz9vxqTaABbtUvm0txmPzO2NWn2ibXl4f7dPicNkXYMI/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgb1ZekWwgQS4Eic2f17PM4R0HFjTEJ7C3K2kRR9B6Ttib7QtdzvHNl8tm4nqZjtZjtZQXcFvYqvETd0Sm5DfxvTxxFknRqLWeY8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUj5vlcfzQ1iaX4zQ8XiafiaUgOEX6Tp3jeGIgFBkVWRkx1DiaxdAPxBAoNVDUiaahREQicLtHSvMgwtIicjPOrqatpTia3LMX4hZtYibMDo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUhYD52Jd5e4nG2pe1BKCsB3iahu1tBwxqYM6DE30RecUha3qkaEYegbtpicQT9jCJXuqakCzDfticicG4eiaIiadX7Q9sovfGtysqaQY/640?wx_fmt=png&from=appmsg)

🔥 AIoT 视频平台应用场景

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5eLNa8HJKyEF4BC5SBvLQiblLdFJsdxPqxGvm4kn7zLiaWEp7Rsox45NbkkPRFocVcuGSPUrlscYOLA/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

智慧安防与园区管理

* 场景：小区、写字楼、工厂园区。
* 价值：统一接入门禁、停车、消防及视频监控子系统。通过分屏监控与云台控制，实现保安室对多区域的实时巡查；结合电子围栏与入侵检测算法，实现异常事件的秒级告警与联动响应。

智慧城市与交通治理

* 场景：城市治安监控、交通卡口、路灯监测。
* 价值：支持大规模视频流并发接入，融合GB/T 28181与ONVIF协议，打破数据孤岛。结合AI车牌识别与行为分析，辅助交通流量统计、事故预警及违章取证，提升城市治理精细化水平。

能源与工业巡检

* 场景：变电站、化工厂、矿山作业区。
* 价值：接入工业防爆摄像头，实时监控设备运行参数与环境状态。通过定时抓拍与录像计划，留存作业过程证据，结合AI算法识别未戴安全帽、烟火等安全隐患，筑牢安全生产防线。

低空经济与无人机巡检

* 场景：县域无人机巡查、电力线路巡检。
* 价值：适配无人机图传协议，实现航拍视频的实时回传与云端存储。支持地理围栏与轨迹追踪，为低空经济发展提供强有力的视频底座支撑。

🌳 写在最后

随着AI大模型与边缘计算的飞速发展，AIoT视频管理平台将持续演进，不仅是一套视频管理软件，更是连接物理世界与数字世界的桥梁。以开源之名，行创新之实，为每一位开发者、每一家企业提供了一套自主可控、高性能、易扩展的AIoT视频管理基座。

Github项目地址：

https://github.com/ZLMediaKit/pymkui

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiammPZaNSh2HzseQoJ9bNzUSCR9jaK8eBlwD7hS4Qc7LH5ZWOb8IrvxwhaqLcic14VbJIiaWQk4ffEylWbhyeMiaM2q1SaV1EmX40/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgskq8VzxckmN9998ALu5rS2oztQH1K25Dg9soia2ia0gkd7x2AYelfa9HLv70n6ppiaoLbq1n0qSQ6TNoAjof2ibkVoryffJO0gibk/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454939032&idx=1&sn=5679fa0132dd03f96b7854e02250f5bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4nJPPZIh6azfSNld68R6DUJneWzEdAm0vHbaGxD8KIQe6hsIV3gRK9Q/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938828&idx=1&sn=c23447c25873fe4f344373b3b2f5303e&scene=21#wechat_redirect)

**往期推荐**

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[4万元，国产信创私有化部署，破解县域无人机AI巡检平台落地难题](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941157&idx=1&sn=b63f67eb0f573b247f47059347b9e407&scene=21#wechat_redirect)

☞[上班摸鱼， 智能 AI 监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请告知我们，我们将尽快处理。主理人微信: beacon0418

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

IoT物联网技术

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