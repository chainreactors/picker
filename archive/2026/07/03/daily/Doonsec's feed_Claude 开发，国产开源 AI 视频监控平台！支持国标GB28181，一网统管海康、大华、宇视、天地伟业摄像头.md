---
title: Claude 开发，国产开源 AI 视频监控平台！支持国标GB28181，一网统管海康、大华、宇视、天地伟业摄像头
url: https://mp.weixin.qq.com/s/LrqOGZpfAAmFThIJ9fClOw
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:39:30.085096
---

# Claude 开发，国产开源 AI 视频监控平台！支持国标GB28181，一网统管海康、大华、宇视、天地伟业摄像头

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUiarX3DMzNHDeUNdfU2cEX4Gd87jbK0T2YAicT1uTZ2iaSzVICBCZu0fWsYXr2x0xBuKca3WBywoHnodkNsiaVhkNGvg976icKo04RA/0?wx_fmt=jpeg)

# Claude 开发，国产开源 AI 视频监控平台！支持国标GB28181，一网统管海康、大华、宇视、天地伟业摄像头

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaAWAlT1iaK8G18poCMkYxHZbRKOib2Jw2vhVWrIZiavBFAuuslDU4Wv19P4S5B2PE6kErD2ppOjeXrVMzCYyX6zI7cjiaOJCx7Ct0/640?wx_fmt=png&from=appmsg)

> 文末获取项目完整方案资料

在物联网视频采集快速发展的当下，Voglander 作为一个Claude Code 开发的，国产开源的企业级视频监控平台，支持国标GB28181协议、交通行业GT1078 协议、国际通用的网络视频接口标准 ONVIF 协议，基于 SpringBoot 构建，核心目标就是解决海康、大华、宇视等厂商协议碎片化、设备兼容性差、媒体流处理复杂是三大核心痛点，实现设备无感切换，二次封装 zlm-spring-boot-starter后，拉流/推流/录制/Hook 回调全链路自动化，提供设备管理的 REST API，摄像头接入完成之后增删改查都可以通过接口自动化处理。

🎯 全协议支持：国标 GB28181、ONVIF、GT1078，兼容海康、大华、宇视、中维等主流厂商

🧪 GB28181 协议验证台：业界少见的「设备端 ⇄ 平台端」可视化验证平台，同进程真实 SIP 自环，注册/PTZ/目录/点播双向闭环一屏可见，零额外部署

📡 SSE 实时事件总线：基于 Server-Sent Events 的单连接全双向事件推送，Redis Pub/Sub 跨节点扇出，15s 心跳保活、断线自动重连，设备上下线/告警/会话状态毫秒级触达前端

⚡ 高并发分片引擎：四层异步事件管线（翻译 → 分片 → 协议路由 → 协议处理），16 槽哈希分片，零锁竞争

🎬 ZLM 二次封装：基于 zlm-spring-boot-starter 封装，实时点播、录像回放、流代理、推流，Hook 驱动状态自动同步

🏗️ 企业级分层架构：Web / Manager / Service / Repository / Integration 五层，Assembler 模式统一数据转换

🛡️ 安全可靠 ：完整的RBAC 权限体系、XSS 过滤、防重复提交、限流切面、Redis 分布式锁

📊 全链路可观测：SkyWalking 链路追踪、结构化日志、JaCoCo 聚合覆盖率报告

🔌 开箱即用：SQLite 零配置启动，平滑迁移 MySQL，Docker 友好

## 🤖 平台技术架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaK1nxBsshmXVCFgdemFNKpic15trnTNwa5urDicf8JEC4UCicIRI8hPECdd7tdKHd3rEibStiaFb3wRXS1qfeXsx3Ysq4jWyfngc3s/640?wx_fmt=png&from=appmsg)

Voglander项目按职责拆成了多个模块：voglander-web 管接口层，voglander-manager 管业务编排，voglander-service 管核心逻辑，voglander-repository 管数据访问。支持集群化部署，高并发场景下可以通过加节点横向扩展，满足企业成百上千路视频接入需求。

| 类别 | 选型 | 版本 |
| --- | --- | --- |
| 语言 & 运行时 | Java | 17 |
| 核心框架 | Spring Boot | 3.5.3 |
| ORM | MyBatis-Plus | 3.5.5 |
| 多数据源 | dynamic-datasource | 4.3.1 |
| 生产数据库 | MySQL | 8.2.0 |
| 开发/测试数据库 | SQLite | 内置 |
| 缓存 & 分布式锁 | Redis | 6.0+ |
| SIP 网关 | sip-gateway-spring-boot-starter | 1.8.0 |
| 媒体服务 | ZLMediaKit-Starter | 1.0.10 |
| JSON | FastJSON2 | latest |
| 链路追踪 | SkyWalking | 9.1.0 |
| API 文档 | SpringDoc OpenAPI | 2.8.9 |
| 测试覆盖率 | JaCoCo 聚合 | 0.8.11 |

### 服务器运行环境要求

> JDK 17+
>
> Maven 3.6+
>
> MySQL 8.0+（默认 SQLite）
>
> Redis 6.0+（多节点部署必须）

一键启动项目

```
# 克隆项目git clone https://github.com/lunasaw/voglander.gitcd voglander# 编译mvn clean compile# 启动（自动创建 app.db，真正开箱即用）mvn spring-boot:run -pl voglander-web
```

| 领域 | 实体 | 表名 |
| --- | --- | --- |
| 设备 | `DeviceDO` | `tb_device` |
| 通道 | `DeviceChannelDO` | `tb_device_channel` |
| 媒体会话 | `MediaSessionDO` | `tb_media_session` |
| 媒体节点 | `MediaNodeDO` | `tb_media_node` |
| 流代理 | `StreamProxyDO` | `tb_stream_proxy` |
| 推流代理 | `PushProxyDO` | `tb_push_proxy` |
| 权限 | `UserDO / RoleDO / MenuDO / DeptDO` | RBAC 主体 |

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUj6QrgKHrRQ8lfK6icYv322e1UGSYPFVtHicF6KV1GDq3Z25bwOsPxnQc77U2QuYrj0OpKYicFvGkL03XsQad5yEBRg5LXGdakRco/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaZEiaRCqL34b1bZDCFcAE3fRaNXE6EqDOaiadfCQjspT1PEGxHKOCWyL4R3Pq1RGgKkGtDHlPEL1QobyJaicObicYLIYYOncqaZUg/640?wx_fmt=png&from=appmsg)

## 🌟 系统演示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiatpibmzfHrpFIwBAe0uibjtz91thqGkDERib2X5vUn5Y7UIkbs7eXDUIGx2mnrP7ibUKqDRfFQHRO47B2G53YqibNRNle0OZWfyicqg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgVhkpz34nZCneohkaVzGNTVtFnWZDekrLO4iaiarFowf2SoVN0icacotukW2tTt42ibiacyIB8hkKsqthpAGnPjmDcg3ib2wHvIt8R0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaD92mSbHYAsY8k347UFMOwvbbOS4kHtj0hr19WgnNiakiabibtVgdqeaPoTXRNnLOmJwviaRf0ZXRHwop1lalxOFwbrDX8KFepKdQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiazIZiaOgq3weHlJ1LB6h1aiaKAwjMzKZS3Ix8NxpLEsNGjHonFPLAFaeibQpJmkpjocbGua0Wiaplqez8uvQ34Toe4qWpY3P0V5Eg/640?wx_fmt=png&from=appmsg)

🌳 写在最后

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiakrXocz5Oic1eCqsjIVOHlAvNQzhQSeyugNIIJoCZgN9iceh2m4qwXoY2IUDfRAHjGHRKn89EfhFsJx03maeOXIKOKZBFuACPSA/640?wx_fmt=png&from=appmsg)

Voglander 基于 MIT 协议开源，代码和结构都比较清晰，二次开发成本不高，非常适合熟悉 SpringBoot 3技术栈的中小企业，承接企业、园区、学校、医院等场景安防监控集成的物联网项目，如果你正在做IoT视频监控管理平台相关的物联网项目需求，不妨一试！

🔗 GitHub：lunasaw/voglander

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