---
title: 圈内悄悄火了！一年省下数万元，网安都在用的数据分类分级系统
url: https://mp.weixin.qq.com/s/tC7FOG_WMXyXTNFKkC0ukQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:45:59.547386
---

# 圈内悄悄火了！一年省下数万元，网安都在用的数据分类分级系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kRTFoQOJmMCUeyicufEkbc7eH5NicSt0JZd5toEwpyOjvJL9pqzE1gVQ5jnUaHKXfVlEzicdy9dUTDEhj4Fo0ic5pGXBh89IvDowWX9skvj60MY/0?wx_fmt=jpeg)

# 圈内悄悄火了！一年省下数万元，网安都在用的数据分类分级系统

原创

We12
We12

安全info

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/dLdju2RRyOVZCt6JROGL4RbVO3K89gEd9AzQsXcxXJI38Id203kk5cPmcuyZAYGvmXN5hBf2TDKHZc9oOHId2A/640?&random=0.480268147009117&random=0.7852064864757442&random=0.5280121419303507&random=0.31068546178001877&random=0.902996060772371&random=0.6132855098545147&random=0.40915401836935317&random=0.21070276491849915&random=0.4503270954677947&random=0.6633865165883854&random=0.3383815024943708&random=0.614016238623269&random=0.47835475944468886&random=0.8255181334303598&random=0.597781584874417&random=0.296401927007669&random=0.47428619952089&random=0.9176517482624438&random=0.8227814374843445&random=0.5279493323924853&random=0.06914140362382715&random=0.622636740236107&random=0.011911117235720692&wx_fmt=png&random=0.03378163228500641&random=0.7046232470262854&random=0.8907979124545382&random=0.9602293510442985&random=0.3979911640268916&random=0.6016218769058672&random=0.3699423099283994&random=0.7918381136454429&random=0.9438676131218258)

点击上方蓝字关注我们

![](https://mmbiz.qpic.cn/mmbiz_png/ZuN7LNJw9RwRTibaY0K2FdiaA3okcYyjLJibJE4Yw0QGUNL6Cm4dlhKQj26HdY9QbY3SKBUG3Ce5X0icnvLETaSCDA/640?&random=0.4554565008552287&random=0.7978393537713326&random=0.822287961694234&random=0.5747704059519392&random=0.6133036835261836&random=0.07494758186176309&random=0.7737266648829204&random=0.28102668650160956&random=0.6819742914041635&random=0.4800634446861538&random=0.2794350214405745&random=0.489900736917255&random=0.31712309790588766&random=0.9921751386755318&random=0.35232486262848073&random=0.537115210250668&random=0.2877357361451034&random=0.5001228865169085&random=0.3219365869300037&random=0.6270479613876261&random=0.48765407861482735&random=0.49358357077060755&random=0.27318874141377836&wx_fmt=png&random=0.28167317060606956&random=0.8913015973084637&random=0.6760115038064081&random=0.3300148315573701&random=0.9910743512397473&random=0.8583561701414033&random=0.18385734820303945&random=0.02021421063591977&random=0.4761867121674215)

**重要声明**

随着网络安全越来越重要，“**安全info**”将定期分享实用安全技术、最新行业动态、案例分析，实战技巧等。**鉴于网络安全法的基础文章内容仅供学习，不做其他任何用处！**

![](https://mmbiz.qpic.cn/mmbiz_png/6aVaON9Kibf7Ry5PiczY7dDqRLyu8gT5Blh52IibkCBoa128nfqcVPa101OK1u4cxqlv23bShGUxrjKMoYDamIShw/640?&random=0.38460509818288524&random=0.09763661647621547&random=0.35578161837813926&random=0.9659969272914388&random=0.24632283352685214&random=0.1340981186234862&random=0.7044825285430407&random=0.025020224847427164&random=0.47352345756097347&random=0.0021982275525160855&random=0.4735167740766173&random=0.37906030300930027&random=0.3182731269923167&random=0.8627576976506441&random=0.3587178707604215&random=0.059233933647551584&random=0.7717671019227492&random=0.23504659389414861&random=0.37797072873806026&random=0.06895297615021323&random=0.09590530102137707&random=0.10219339876916123&wx_fmt=png&random=0.637403832549521&random=0.04883436709888844&random=0.11325089166784585&random=0.9304571522378458&random=0.22418465116388742&random=0.35201968049483523&random=0.7687049756863031&random=0.8789800622572888&random=0.09261329469851276)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kRTFoQOJmMC38WotzVUWShypVumiaJ0Wzq9XBJwicoBhq2bicdTRTQyu4AymR55ickhbwI8knZGzGagmwribPkfIbSgYtNX8VdwNdxdlUHqryT9g/640?wx_fmt=png&from=appmsg)

## 第一步：接入数据源

项目组在服务器上部署了 MDCGS，前后不到半小时。部署完成后，第一件事是把所有数据库接进来。

系统支持以下数据源类型：

| 类型 | 端口 | 说明 |
| --- | --- | --- |
| MySQL | 3306 | 业务主库 |
| PostgreSQL | 5432 | 数据仓库 |
| Oracle | 1521 | 财务系统 |
| SQL Server | 1433 | ERP系统 |
| DM（达梦） | 5236 | 政务相关 |
| openGauss | 5432 | 新型数据库 |
| PolarDB | 1921 | 云原生数据库 |

填写连接信息，全部接进来，用了不到一天。

![](https://mmbiz.qpic.cn/mmbiz_png/kRTFoQOJmMDx77hxL4LN6T5JG6DtaiafyrnnUkTx54kyJVrNzKN2OXrR4LUSfyYcSdhQia3Kv7JcfatbFsMWG9EwgwNHDxfKczXgxPw2RG5qo/640?wx_fmt=png&from=appmsg)

## 第二步：发起全量扫描

数据源接入完成后，对每个数据库发起"扫描任务"。

这一步，系统自动完成三件事：

1. 1. **读取表结构**
   读出所有表名、字段名、字段类型、注释。
2. 2. **字段内容采样**
   从每张表取若干条样本数据，观察实际存储内容。比如有个字段名叫 c3，注释是空的，采样一看存的是手机号格式。
3. 3. **规则匹配**
   系统内置一套敏感数据识别规则，对字段名和字段内容、注释同时做匹配：

| 敏感类型 | 匹配规则 | 典型字段 |
| --- | --- | --- |
| 手机号 | 正则匹配数据值 + 字段名包含 phone、mobile、tel | - |
| 身份证 | 正则匹配数据值 + 字段名包含 id\_card、cert\_no、person\_id | - |
| 银行卡 | 正则匹配数据值 + 15-字段名包含 bank\_card、card\_no | - |
| 邮箱 | 正则匹配数据值 + @字段名包含 email、mail | - |
| 姓名 | 正则匹配数据值 | real\_name、truename |
| IP地址 | 正则匹配数据值 + 字段名包含 ip、client\_ip | - |

两百多张表，全部扫描完成，用了十分钟。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kRTFoQOJmMB7g7EicKN0av0LEbEgrxic5cUaXqFkS6bTXl7Y8RE9LG2oiau4EG3SKGr8myf50JYAKnNYlFP8QNM0ZEmetq0mOUPDMD1V6Xmeak/640?wx_fmt=png&from=appmsg)

## 第三步：确认分类分级结果

扫描结果出来后，安全团队要做的不是从头梳理，而是审核和确认。

系统把识别结果全部列出来，每条记录包含：

* • 字段所属的数据库、表名、字段名
* • 系统识别的敏感类型（手机号 / 身份证 / 银行卡等）
* • 自动给出的分级建议（L1 至 L4）
* • 建议的保护措施（脱敏 / 加密 / 观察）

安全团队逐条过了一遍。有几条识别有误，比如某个叫 phone\_code 的字段存的其实是邮编，不是手机号，改掉了。大部分识别是准确的，特别是对身份证和银行卡的识别，准确率很高。

审核完成后，系统记录了审核人和审核时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kRTFoQOJmMCiaatBJBCpj3Goib6Ar6boEqX7B1a9zVteSwTTGpHmmfftuAN3chJ0IY838BMoNsXFjA7mOmibricqe0IRc76icASYQYau0GCj84x8/640?wx_fmt=png&from=appmsg)

## 第四步：配置分级保护策略

分级完成后，系统根据分级结果自动给出保护建议：

| 分级 | 含义 | 建议保护措施 |
| --- | --- | --- |
| L1 | 极高敏感，如身份证、银行卡 | 脱敏 + 加密，建议禁止批量导出 |
| L2 | 高度敏感，如手机号、邮箱 | 脱敏，建议审批后访问 |
| L3 | 中度敏感，如姓名、地址 | 视情况脱敏，记录访问日志 |
| L4 | 一般数据 | 正常访问，定期巡检 |

系统内置了常用脱敏规则：星号替换（138\*\*\*\*8000）、部分保留（6222 \*\*\*\* \*\*\*\* 7890）、哈希脱敏等，可以直接选用。

## 第五步：生成合规报告

全部配置完成后，一键生成报告。报告包含以下内容：

* • 数据资产总览：共计多少个数据库、多少张表、多少个字段，其中敏感字段多少个
* • 分类分布：各级别（L1-L4）的字段数量和占比
* • 敏感字段清单：所有识别出的敏感字段明细，注明当前保护状态
* • 合规评分：基于分类覆盖率和敏感字段保护落实情况计算的综合评分
* • 改进建议：还未落实保护的敏感字段，给出处理优先级建议

报告导出为 PDF，直接提交监管部门。

![](https://mmbiz.qpic.cn/mmbiz_png/kRTFoQOJmMDicvFpIibeGnpapQSy25PHRCkGQsMH81HJALkZOwMp4AFJ65m30h8OplHSzHWIy0ch67QTc4awhLNvFRo7iaicyeTbibH7s8exAXHw/640?wx_fmt=png&from=appmsg)

## 第六步：建立持续运营机制

一次性梳理完成后，系统留了一条定时任务：每周自动扫描一次，比对字段变化。

* • 发现了新字段，自动告警，提示安全团队复核
* • 发现已有字段被删除或改名，记录留档
* • 每次扫描结果自动存档，随时可查历史记录

这样，数据资产台账不再是"查一次管一年"，而是持续更新、持续可控。

## 用后的真实感受

安全团队的反馈是几件事有明显改善：

**第一，梳理效率。** 手工梳理两百张表，保守估计两周。MDCGS 扫描加人工复核，三天完成。

**第二，结论有据可查。** 手工梳理的结论靠人记忆，MDCGS 的每条分类结论都有规则依据：字段名命中了哪条规则、数据值符合什么格式，报告中全部列明。监管问起来，答得上来。

**第三，历史可追溯。** 字段变更有记录、审核操作有日志、报告有存档。下次检查，翻出历史报告对比，变化一目了然。

**项目地址**： https://github.com/HaoY-l/mdcgs
**演示地址**： https://mdcgs.hyinfo.cc/ （账号 admin / admin123）

本文仅供技术交流，企业数据安全建设需结合自身实际情况制定分类分级方案。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z8yWOunaWFxsNRiacoONvUDnEia1l81m70IjcKHE5HGAFrWlpZFbvf1nHAGdJCicKsxp5T1ohC2o8w1v9dXLUPhicg/0?wx_fmt=png)

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