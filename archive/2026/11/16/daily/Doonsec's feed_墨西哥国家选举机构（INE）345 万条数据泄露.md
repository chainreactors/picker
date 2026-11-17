---
title: 墨西哥国家选举机构（INE）345 万条数据泄露
url: https://mp.weixin.qq.com/s/UUa_lKhBJhn_9ghHR5rhkA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:29.488941
---

# 墨西哥国家选举机构（INE）345 万条数据泄露

# 墨西哥国家选举机构（INE）345 万条数据泄露

原创

NightTeam
NightTeam

夜组OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 执行摘要

2026 年 11 月 14 日，黑客宣称在墨西哥国家选举机构（Instituto Nacional Electoral，INE）服务器内取得"2022 年总统罢免公投（Revocación de Mandato 2022）完整数据库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8ribhCcDRpq3LNFOPTtcZTkxg1EOVYU6iazQYcr5mYozmYbXPLeC5G2fb70ktrkWX2LwAYRmvt8wZFVtx1xwP94gzddwYzxwxBWYs/640?wx_fmt=webp&from=appmsg)

**综合判定：**

> 该数据集最可能是**以真实选民名册为骨架、对法定标识符重算并对选举地理重编号后生成的派生/合成数据集**（亦可能为 INE 测试环境或仿真数据被带出），**不宜认定为 INE 生产库原始泄露**。但因姓名、出生日期、住址、邮编、州/市层级具备高度保真度，**无法排除其中包含真实公民信息子集**。

**风险定级：** 数据敏感度**高**；影响主体规模 345 万条；综合风险 **高**。

## 数据字段

| 序号 | 字段 | 含义 | 完整率 | 判读 |
| --- | --- | --- | --- | --- |
| 1 | `VCONSULTAPOPULAR_ID` | 支持签名记录主键 | 100% | 严格连续 1–3,451,843，无空洞 |
| 2 | `CONSULTA_ID` | 咨询批次 | 100% | 恒为 `1`（首次全国公民咨询） |
| 3 | `CAJA` | 纸质表册箱号 | 100% | 633 个取值，`9999` 为电子渠道占位（31.4%） |
| 4 | `PAQUETE` | 包号 | 100% | 与箱号组合定位实体档案 |
| 5 | `FOLIO` | 页号 | 100% | 同上 |
| 6 | `CONSECUTIVO` | 页内序号 | 100% | 与上三者构成四级归档 |
| 7 | `ID_SOLICITUD` | 申请单号 | 100% | 1,836 个，**全部以 `F21031` 开头** |
| 8 | `PROMOVENTE` | 推动人 | 100% | 1,836 人；含 10,164 行系统提示文本污染 |
| 9 | `NOM_ORG_ASOC` | 推动组织 | 59.84% | 11 个组织，40.16% 为空 |
| 10 | `CLAVE_ELECTOR` | 选民证号（18 位） | 100% | 100% 长度合规、全表唯一 |
| 11 | `CURP` | 人口登记唯一码（18 位） | 91.22% | 302,978 行为空 |
| 12–14 | `NOMBRE` / `APELLIDO_PATERNO` / `APELLIDO_MATERNO` | 姓名 | 92.96% | 242,939 行整段缺失 |
| 15 | `FECHA_NACIMIENTO` | 出生日期 | 92.96% | `DD/MM/YYYY` ，1901–2000 |
| 16 | `SEXO` | 性别 | 92.96% | `M` （女性）/`H`（男性），无其他取值 |
| 17–21 | `CALLE` /`INTERNO`/`EXTERNO`/`COLONIA`/`CODIGO_POSTAL` | 住址与邮编 | 85–93% | `INTERNO` 83.19% 为空（正常） |
| 22–26 | `ESTADO_CLAVE` /`MUNICIPIO_CLAVE`/`DISTRITO`/`SECCION`/`LOCALIDAD` | 选举地理 | 92.96% | 32 州全覆盖 + 空值 |
| 27 | `MANZANA` | 街区 | 92.96% | — |
| 28 | `OCR` | 选民证 OCR 条码（13 位） | 92.78% | **前 4 位与 `SECCION` 100% 一致** |

**判读：** 字段命名遵循 INE 西班牙语业务命名法与下划线大写风格，并含纸质档案物理定位字段（箱/包/页/序号）与选民证 OCR 条码，属"签名册数字化登记"业务模型的完整投影，非通用泄露库的典型形态（通用库多为 id/name/email/password）。

### 规模与主体

| 指标 | 值 |
| --- | --- |
| 总行数 | 3,451,843 |
| 推动组织 | 11 个 |
| 推动人 | 1,836 名 |
| 覆盖州 | 32/32 + 空值 |
| 覆盖市镇组合 | 2,474 个（含空值组合；市镇编号取值仅 561 个） |
| 覆盖 SECCION | 6,485 个 |
| 实体页（箱/包/页） | 625,554 页 |

组织分布高度集中：`QUE SIGA LA DEMOCRACIA A. C.` 2,031,450 行（58.85%），其余 10 个组织合计约 4.1 万行，另有 1,386,397 行（40.16%）组织为空——空组织与 `CAJA=9999` 的电子渠道高度相关，符合"个人线上支持"未挂靠组织的业务逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8r9RsxZZwNmInmysF7VS3nH0DPfLSoneJ60ib227jIH3ic8s6DOjvtB2IicjDWE4OoTGicFNiaKpiaCbmfX4yS5R5KcorscIxsjzCcLCA/640?wx_fmt=webp&from=appmsg)

## AI暗网威胁情报全球监控系统

暗网全球威胁情报监控系统（dark.libaisec.com） 7\*24实时监控数据泄露情报、网络攻击情报**（融合数据泄露、勒索软件、DDoS攻击、恶意软件、访问权限售卖、网页篡改、日志泄露、网络钓鱼、漏洞情报、政治舆情等威胁事件，为政企用户提供可落地的威胁预警与响应建议。）**，包括市场、论坛、黑客组织、博客、拍卖行等全部情报。

**实时预警全球暗网威胁情报及您所关注国家和地区的数据泄露及其它威胁线索。**

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过