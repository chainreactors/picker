---
title: 巴基斯坦移动网络基础设施数据集泄露分析
url: https://mp.weixin.qq.com/s/_lHt3ZnpkpqvoDVcQpaPfQ
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:03:20.946560
---

# 巴基斯坦移动网络基础设施数据集泄露分析

# 巴基斯坦移动网络基础设施数据集泄露分析

原创

NightTeam
NightTeam

夜组OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 事件摘要

2026 年 10 月 24 日，黑客声称出售巴基斯坦移动网络数据，内含约 9.2 万条基站记录。经对分析本报告得出以下核心结论：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/es3jUghv8r8c7yXP71kLDr7gly4W0ymaibobBE3XcF5FicA7keGxFPyvOiakxeBVOWD3DaRXY6HRcr0Za8dAAoTzOoumpsgRLqiaVWPCPuWLTPc/640?wx_fmt=png&from=appmsg)

1. **数据为真，且与黑客描述同源。** 黑客在 Telegram 截图中列出的三组数字——27,929、27,027、37,184——与包内三份 Ufone（PTML）文件 2G 工作表的行数**逐一精确吻合**（合计 92,140，即其"约 92K"），可确认传播样本就是其所售数据，而非"图文不符"的诈骗帖。
2. **黑客严重低估了数据体量与敏感度。** 全包有效数据行实为 **503,628 行**（含重复副本 610,575 行），是其声称的 5 倍以上；"92K"仅统计了三份文件的 2G 单表，且 92K 是**小区/扇区记录数**，并非基站数（Ufone 物理站址约 **9,609** 个）。
3. **包内隐藏了本次事件最敏感的部分。**`BTS SET QRY.accdb` 并非普通"Access 数据库"，而是 **2021 年 5 月 27 日拉瓦尔品第 Westridge / Chuhar Chowk 一带、四家运营商的单日 BTS 集合查询结果**：**125,891 条 CDR**，涉及 **26,570 个唯一手机号码、25,557 个唯一 IMEI**，并附 12 个小区的 LAC/CID 与部分经纬度。帖文对此只字未提。
4. **泄露路径不是核心网入侵。** 包内没有 SIM 鉴权密钥、HLR/HSS 签约、通话内容、计费账单或核心网配置；相反，Access 文件带有 `Paste Errors`、`Test_ABIMEI` 等人工草稿表，Telenor 的 IMEI 被截断为 14 位，Jazz 的小区/位置列以占位符 `CID`/`LOC` 填充。这些特征共同指向**一台用于 CDR 分析的工作终端**，最可能是执法/情报分析侧工作目录（或其二手流转）外流，其次是运营商内部人员。
5. **风险等级：高。** 9,609 个站址及天线方位、下倾、频点、CGI 等参数构成巴基斯坦电信网络的"测绘底图"，覆盖旁遮普、信德、开普、俾路支、AJK、GB、FATA 等全部省区；CDR 则将 2.6 万余名特定时间出现在特定街区的个人暴露于可识别风险，并可能反向暴露 2021 年一次具体调查行动的时间与空间范围。

## 数据包结构与内容核验

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8ricaibVppJWqgG1CbHtr4WLjUFmI0CRPa6NJm4OSqMcEI49oVIRqYcYialE7x7bMgmJMicXvIcFz15VzB9sy4VbelB2icweyWg4fPn8/640?wx_fmt=webp&from=appmsg)

### 数据分类

| 类别 | 内容 | 性质 | 敏感度 |
| --- | --- | --- | --- |
| A. 运营商工程规划数据 | PTML 2020/2021 站点表、LAC/Cell ID 报表 | Ufone 内部网络规划与在网清单 | 高 |
| B. 跨运营商 Cell ID 参考库 | 2013 年六家运营商小区坐标汇编 | 半公开/灰色流通的分析参考数据 | 中 |
| C. 通信元数据（CDR） | 2021-05-27 四运营商 BTS 集合查询结果 | 执法/情报级个人通信记录 | **极高** |

### Ufone（PTML）工程数据

| 数据集 | 2G | 3G | 4G | 物理站址 | 关键字段 |
| --- | --- | --- | --- | --- | --- |
| PTML 2020 | 27,027 | 36,113 | 8,648 | 9,292（2G/3G 并集） | Region、SiteID、CGI、LAC、BSIC、BCCH ARFCN、天线高度/方位/下倾/波束、上下行频段、MSC/BSC |
| PTML 2021 | 27,929 | 39,426 | — | 9,584 | Region、SiteID、Cell、LAC、CGI、City、Covered Area、经纬度 |
| LAC CELL ID Report | 37,184 | 74,380 | 20,083 | 13,140 站点代码（含停用/室内） | Vendor、BSC/RNC、Site Code、Cell Name、激活状态、ADDRESS、CITY、PROVINCE、Coverage Type |

* **站址规模**：2020 与 2021 规划表并集 **9,609 个物理站址**；2021 年新增 317 个、退网 25 个。
* **厂商结构**：华为占比 2G 64.2%、3G 67.3%、4G 79.4%，其余为中兴；即 Ufone 无线接入网 **100% 为中国厂商设备**。
* **省份分布（2G，37,184 条）**：旁遮普 60.1%、信德 22.2%、开普 9.1%、俾路支 2.9%、联邦首都区 2.5%、AJK 1.9%、FATA 1.1%、GB 0.3%。
* **网络元件命名**：BSC（如 `PSH001H__KohatRd_MGW_1`）、RNC（如 `UISB208H__RNC_I-10 Building ISB_3`）、MME、MSC ID 等内部命名规则完整暴露，可用于推断网元拓扑与厂商版本。
* **数据质量线索**：xlsb 含 4,860 个 3G 停用小区、350 个 2G 停用小区，说明其为"全量台账"而非在网清单；这也解释了其站点代码数（13,140）高于规划表站址数（9,609）。

### 2013 年跨运营商参考库

| 工作表 | 记录数 | 独立站点 | 坐标覆盖 | 备注 |
| --- | --- | --- | --- | --- |
| Ufone | 22,062 | 7,675 | 99.98% | LAC 58806 等与 2021 年规划表一致 |
| Telenor | 22,925 | —（无站点列） | 99.85% | 含 RAC/SGSN/天线/BCCH/BSIC 等 30 列 |
| Warid | 4,573 | 4,568 | 99.87% | Warid 已于 2017 年并入 Jazz |
| Zong | 27,919 | 6,822 | **0%** | 仅有 SITE ID、CI、LAC、地址，无经纬度 |
| Vfone | 285 | 228 | **0%** | 小型/区域运营商 |
| Mobilink | 29,183 | 9,260 | 100% | 现 Jazz |
| 合计 | 106,947 | ≈28,553 | 73.6% | 2011 年创建、2013 年定稿 |

该库是 CDR 地理化分析的典型"民用底图"，长期在分析圈内流通；本次样本中它被完整打包两份，且**恰恰是给 Jazz、Telenor 等非 Ufone 记录定位的关键**。

### BTS SET QRY.accdb：被隐藏的 CDR

数据库共 8 张表，其中 4 张为运营商 CDR，另有 `CallType` 映射表、`Paste Errors` 粘贴错误表、`Test_ABIMEI` 测试表（空）与空的 `BWarid` 表。

| 运营商 | 表名 | 记录 | 唯一号码 | IMEI | IMSI | 小区 | 位置线索 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jazz | BjazzNew | 28,901 | 6,981 | 6,996 | — | 0（CID/LOC 为占位符） | 无 |
| Telenor | BTelenor | 67,940 | 7,826 | 8,029 | 7,837 | 3 组 LAC-CID（2 个物理站） | Westridge Bazar Road、RV Arcade Peshawar Road |
| Ufone | BUfone | 21,705 | 7,306 | 7,313 | 7,306 | 6（3 个物理站） | Malik Plaza Chuhar Chowk、Allahabad、Zaman Plaza Westridge |
| Zong | BZONG | 7,345 | 4,633 | 3,234 | — | 3 | LAC 30201 / 7700 |
| **合计** | — | **125,891** | **26,570（去重）** | **25,557（去重）** | **15,143** | **12** | — |

**时间窗口**：全部记录日期为 2021-05-27；Jazz、Zong 集中在 06:00–17:59（12 小时），Telenor、Ufone 覆盖 00:00–23:59。各运营商交付窗口不一致，符合"按请求分头导出、再人工汇总"的特征。

**地理范围**：Ufone 的 6 个小区经反查全部落在拉瓦尔品第 Westridge / Chuhar Chowk 一带，最远两点直线距离约 1.3 km；Telenor 的 2 个站址同样位于 Westridge 与 Peshawar Road。即这是一次**约 1.5 平方公里范围内的"人-机-号"筛查**，而非全网导出。

**业务构成**：Telenor 侧 SMS 38,618 条、语音 19,973 条、GPRS 9,349 条；Jazz 侧主叫 6,469、被叫 5,245、短信 17,187；Zong 主叫/被叫基本对半。整体以短信与信令为主，符合"以基站集合筛选在场用户"的查询目的。

**真实网络特征**：Telenor IMSI 中 67,931 条为 410-06（巴基斯坦 Telenor），另有 9 条境外 IMSI（424-03 阿联酋、242-01 挪威、262-02 德国、505-02 澳大利亚），与真实国际漫游一致；Ufone IMSI 以 410-03 系列为主。此类细节难以伪造。

**数据质量异常（重要线索）**：

1. Jazz 表的 `CID`、`LOC` 两列全部为字面值 `CID`、`LOC`，即表头被当作数据粘贴，实际小区与位置缺失；
2. Jazz 的 B 方号码混入十六进制业务标识（如 `4A415A5A` 即 ASCII "JAZZ"），说明数据经过二次编码/清洗；
3. Telenor 的 IMEI 全部为 14 位（8,029 个），较标准 IMEI 少一位，符合 Excel 数值处理导致的截断；
4. 存在 `Paste Errors`、`Test_ABIMEI` 等临时表，以及空的 `BWarid` 表（Warid 2017 年已并入 Jazz，说明沿用了旧模板）。

上述异常共同说明：**这是一份由分析人员在终端上手工汇总的工作文件，而非运营商核心系统直接导出的原始文件**。

## 敏感性与影响分析

### 敏感度分级

| 数据类别 | 敏感度 | 主要滥用场景 |
| --- | --- | --- |
| 站址坐标 + 天线方位/下倾/挂高 | 高 | 覆盖建模、干扰/伪基站部署、物理接近与破坏 |
| CGI/LAC/BSIC/BCCH/PSC/PCI | 高 | 小区级定位、终端指纹、网络拓扑推断 |
| 网元命名与厂商信息 | 中高 | 供应链画像、漏洞利用面推断 |
| MSISDN + IMEI + IMSI + 时间 + 小区 | **极高** | 目标识别、轨迹还原、跟踪骚扰、勒索 |
| 2013 参考库 | 中 | 作为"底图"放大上述风险 |

### 网络与国土安全影响

* **测绘价值**：9,609 个站址 + 全量小区参数，可构建巴基斯坦主要城市的射频覆盖模型；对电子战、通信压制、无人机链路规划均具直接价值。
* **战略敏感区**：2G 小区中 AJK 699 个、GB 94 个、FATA 402 个、开普 3,368 个；4G 在 AJK 亦有 104 个。这些区域涉及克什米尔实际控制线、北部边境与部落区，基站坐标属典型军事情报要素。
* **时效性折损**：数据为 2020–2021 年，LAC/CID 与部分站址可能已调整，但**物理站址、铁塔位置、机房地址在 5 年内变动有限**，坐标与天线参数仍高度可用；2013 参考库与 2021 数据的一致性（8 年未变）进一步说明其长期有效性。
* **对 2026 年合并的影响**：Telenor Pakistan 已于 2026 年 7 月并入 PTML（Ufone 5G），本包中的 Telenor 站址与 CDR 现已归同一法律主体，事件影响面与通知义务相应扩大。

### 执法与情报行动的次生风险

* 单日 + 单区域 + 四运营商同时取数，本身即暴露了**2021 年 5 月 27 日拉瓦尔品第某次调查行动的时间与空间范围**。
* 对立方可通过比对自身成员当日的通信记录，反推被监控的小区集合，进而推断行动目的、目标画像与信息来源。
* 若原始工作目录中还存有其他案件材料，本次泄露可能只是"冰山一角"。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8ribaNRAk0IhcelDQicza0IgnlWx3oRVJicXfV5JibdalmxQztDf1icWFCHibEqHibhKibYXic4yQSHOekVfKjs5ibUCwy96amAYibxrcxhNJc/640?wx_fmt=webp&from=appmsg)

## AI暗网威胁情报全球监控系统

暗网全球威胁情报监控系统（dark.libaisec.com） 7\*24实时监控数据泄露情报、网络攻击情报**（融合数据泄露、勒索软件、DDoS攻击、恶意软件、访问权限售卖、网页篡改、日志泄露、网络钓鱼、漏洞情报、政治舆情等威胁事件，为政企用户提供可落地的威胁预警与响应建议。）**，包括市场、论坛、黑客组织、博客、拍卖行等全部情报。

**实时预警全球暗网威胁情报和您所关注国家和地区的数据泄露及其它威胁线索。**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8r91cuGbOFfUMrwej00LhRaHJBfzIzGibUvRsLwah5NGu1S6SuTK6vPmpoeI3michMiaU9cODHHialW1xbWmb3I4UHbpenIDicymmCn4/640?wx_fmt=jpeg)

【重磅】AI暗网全球威胁情报监控系统7\*24实时监控数据泄露情报、网络攻击情报](https://mp.weixin.qq.com/s?__biz=MzU5MjgwMDg1Mg==&mid=2247492349&idx=1&sn=1119db2bf839e3292d5b9511f3fa76bf&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A1AjQiarwFHPJibeWbc1nhED6yPPhcfplNAzMjXJx106p9J3HaRZUNyBAhECfklMPvyOsReia0qaVV8A/0?wx_fmt=png)

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