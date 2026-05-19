---
title: 原创 | ShadowScan 安全扫描器v1.0.1更新
url: https://mp.weixin.qq.com/s/-z9LkP752HHL1WAEDJ9dLw
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:51.678518
---

# 原创 | ShadowScan 安全扫描器v1.0.1更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I2dhkmhKrSbtZ0BJG9GQaQnAMyH087Onon43lfPo14amISbQ5S5kv8HDYibH5Z5zUumOd4ufFiatcPfMYQmrcPmHdvLDO2ozCG25Z0Fyyicguk/0?wx_fmt=jpeg)

# 原创 | ShadowScan 安全扫描器v1.0.1更新

原创

MY0723
MY0723

不秃头的安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# ShadowScan 安全扫描器 v1.0.1

```
前言：本文中涉及到的相关技术或工具仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担，如有侵权请私聊删除。
知识星球和交流群在最下方。
需要cn*d（中高）/c2n*d（高与支撑单位）/安全证书请联系vx咨询
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I2dhkmhKrSamW5snnbbeQ2lc0nPfSGtc3L9pSjoy1mtW5jo9h5UsOSajaiaibmUVNMNgccHicMzSRonnPeWapUt1icR60H9ZfTd9T40Ma1yVAEg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=0)

ShadowScan 是一款面向安全从业人员的自动化信息泄露扫描与资产测绘工具。深度整合多平台搜索引擎，通过自动化 Dork 语法扫描发现暴露在公网的敏感文件，并自动提取身份证号、手机号、学号、邮箱、银行卡号等个人敏感信息（PII）。

支持 **Bing / FoFa / Hunter / Quake / Shodan / Censys / Zoomeye / 0.zone / DayDayMap** 等主流搜索引擎与资产测绘平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSZWvdY9GQQGMSgia8FNXbGMHiaiazibRnIibsoibDQhpVwuHVoTT5xVma44iarjCQib3jmoJdX67XUd6zvAJxBujIZc69PeT1XK93UickdY/640?wx_fmt=png&from=appmsg)

## 1、更新日志

![](https://mmbiz.qpic.cn/mmbiz_png/I2dhkmhKrSYP5eObBA6YiaeiaJrLLmfLbDick2rBElqQkQU1NPETXAWImpoP17RyTwBua83iatwehOZtDTTq1FjudEA6Iicf2jpR8ibhhWYrZx7UQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSbZbicl0aBUHLUBMp5tOFa2aN8uz0eL8nR2GPm5aUTiapZ1R4XibicUEIAAImXSyfO4MfhTK7QyLdSxKt5xWq5S0Vias3vYMaxkvgQ8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSa1uUKq9N4oiaeQTnMyw1wiboTqn17pgPmibGgib13UL8Yibia9nwYibuF7AXhZQpuSdgNibfsTjpib4jXNX392OOiaPv4Jp9UTaAHa4PHCI/640?wx_fmt=png&from=appmsg)

```
### v1.0.1**P0 必修修复（13 项）**| 修复项 | 说明 ||--------|------|| 配置保存不生效 | ApiConfigService 移除启动时静态快照，改为动态 getter；修改 API Key 后无需重启即可生效 || Censys 配置模型 | 支持 LEGACY（API ID+Secret）和 PLATFORM_V3（PAT+Org ID）两种模式，自动识别 PAT 前缀 || Censys 初始化参数 | 修正 Module2Controller 传参，PAT 走 v3 端点 + Bearer Token，Legacy 走 v2 端点 + Basic Auth || Censys Org ID 传递 | 验证与搜索统一使用 `X-Organization-ID` Header + `organization_id` 参数 || 旧 CensysApiClient | v1→v2 接口升级，`apiKey:apiKey`→`apiId:apiSecret`，废弃重复客户端 || CSV 导出列错位 | 手写拼接改为字段数组循环导出，表头与数据列数严格一致 || JSON 嵌套字段 | 新增 `jsonPath()` 方法支持 `a.b.c` 路径读取，证书有效期/CN/Issuer 正常展示 || 资产去重 | 按类型定义去重 Key：资产 `ip:port:protocol`、证书 `fingerprint`、漏洞 `cveId+ip+port` || 来源统计 | `setSourcePlatform()` 自动同步到 `sourcePlatforms` 集合，多平台来源统计准确 || 主键获取 | `prepareStatement` 增加 `RETURN_GENERATED_KEYS`，新增记录后获取真实 scanId || ResultSet 泄漏 | `getResultsByScanId()` 改为返回 `List<ScanResult>`，内部 try-with-resources 自动关闭 || 域名匹配误判 | `contains()`→`equals() || endsWith("."+target)`，避免 `notexample.com` 误命中 || FileDownloader | 最大重试 3 次、50MB 大小限制、流式写文件、共用连接池 HTTP Client |
**P1 应修（11 项）**| 修复项 | 说明 ||--------|------|| DataRepository 线程安全 | `HashMap`→`ConcurrentHashMap`，`ArrayList`→`CopyOnWriteArrayList`，关键路径加 synchronized 锁 || 关系构建性能 | O(n²) 双循环改为先建 IP/domain/org/CIDR 索引再生成关系，千级资产导入不卡 UI || HTTP 请求封装 | 新增 `PlatformHttpClient`，统一 GET/POST、Bearer/Basic/API-KEY 认证、429/401/403 错误处理 || 控制器拆分 | Module2PlatformController、MainController 按职责拆为 Controller/Service/Parser/Exporter || 平台字段 Schema | `PlatformFieldMapper` 统一表格列、CSV 导出、暴露面映射字段定义 || 旧实现清理 | 废弃 `PlatformConfigManager` 独立配置，统一到 `ApiConfigService` || ThreatBook pending | 移除重复 `logClick()`，只保留 `showPendingDialog` 内部一处 || PII 校验器 | 身份证增加校验位验证（`isValidIdCard`）、银行卡增加 Luhn 算法校验 || 敏感信息脱敏 | 新增 `SensitiveValueMasker`（maskIdCard/maskPhone/maskEmail/maskBankCard/maskToken） || PII 输出脱敏 | `buildSampleDescription`、`buildCategorySampleDescription` 所有 PII 显示值统一脱敏 || AppPaths | 新增 `AppPaths` 工具类，配置/数据库/输出/日志统一到 `~/.shadowscan/` 目录 |
**P2 增强（4 项）**| 修复项 | 说明 ||--------|------|| 核心单测 | `SensitiveValueMaskerTest`、`ExposureDataTest`、`ApiConfigServiceTest`、`PlatformFieldMapperTest` || JUnit 5 依赖 | pom.xml 添加 `junit-jupiter 5.10.2` || AppPaths 架构 | 从不同目录启动程序读写同一套用户配置，不再依赖 `user.dir` || Logger 统一 | `PlatformHttpClient`/`AppPaths` 统一错误输出，PII 敏感值不进入日志 |
```

## 工具交流群

工具地址：https://github.com/MY0723/ShadowScan

工具  使用手册：

```
https://github.com/MY0723/ShadowScan/blob/main/README.md
```

有问题或更新会优先在群里说，需要的可以加群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSakqrPwr5CqQSMeXUkibicGyRAS1l039hHKDe2103tI7slY27wiaRlgPmzMBibKICMQZw4ricx4wWCzLPKRl2nC0LJ94GaFPicg2gW9Y/640?wx_fmt=png&from=appmsg)

  如果群满加我拉

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I2dhkmhKrSbiaEZXZpFPtsPhOmKADLPWTvqMgPhbOlvenQZzxpRzojnRSh3gzKpIQesdVyrBC68LQTjv6gXmbJ05DOkXjiaibibB38527AwMhPg/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVZYQ3CLswQeCkia9axLIjSV5hFqM9ouzExlwAsUtDeqEyXE2pLUIRCeDJ0m89GHyibMCFAHXBHmiacg/0?wx_fmt=png)

不秃头的安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVZYQ3CLswQeCkia9axLIjSV5hFqM9ouzExlwAsUtDeqEyXE2pLUIRCeDJ0m89GHyibMCFAHXBHmiacg/0?wx_fmt=png)

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