---
title: 篇 03：美国能源公司CenterPoint Energy 数据泄露分析报告
url: https://mp.weixin.qq.com/s/0h7R_PPWO1TW5Br4Guzaeg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:57:20.622009
---

# 篇 03：美国能源公司CenterPoint Energy 数据泄露分析报告

# 篇 03：美国能源公司CenterPoint Energy 数据泄露分析报告

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAjxRayA5mVOpfcBhb3luflYv56ejnda4IyNCtDWA92Khymzh01A8d1IfdvMmKSUmaBiaSpUwrrsqBE8zAlVzJzyic2lQmI3ibAfM8/640?wx_fmt=webp&from=appmsg)

2026年9月14日，美国公用事业公司 CenterPoint Energy 披露，未经授权的第三方通过对外系统取得了部分客户个人信息，供电和供气未受影响。公司总部位于休斯敦，服务覆盖得克萨斯、印第安纳、明尼苏达和俄亥俄四州，计量客户超过700万。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAiawMicymT5gUunFqpq2Qr4nPuhRH4W7IrwicaF79lNOXlsoibBsYJickUpta0sPAfD9USpjibnAeK8E3zjmuFbT9Io25KaPjYojjLeg/640?wx_fmt=webp&from=appmsg)

通过分析泄露数据，`full_db`包含7个CSV、7个JSONL及辅助目录，总量约52.40 GB。数据涉及账户、联系方式、地址、账单和身份核验字段。

| 文件组（各含CSV、JSONL） | 两文件合计GB | JSONL响应条数 | 结果码000条数 | CSV数据记录 |
| --- | --- | --- | --- | --- |
| mn\_1 | 7.898 | 1,128,275 | 974,522 | 974,517 |
| mn\_2 | 7.071 | 1,002,842 | 892,190 | 892,181 |
| tx\_1 | 15.741 | 2,263,118 | 2,078,744 | 2,078,213 |
| tx\_2 | 4.329 | 608,331 | 597,562 | 597,534 |
| tx\_3 | 5.414 | 772,547 | 691,796 | 691,756 |
| tx\_4 | 7.459 | 1,059,907 | 955,157 | 955,113 |
| tx\_5 | 4.485 | 652,504 | 529,022 | 528,947 |
| 合计 | 52.396 | 7,487,524 | 6,718,993 | 6,718,261 |

两种格式是7组对应材料，行数不能相加。JSONL全部可解析，其中694,172条为`999`，包括375,172条「No Data Found」和319,000条「No active contract」；另有74,359条缺少结果码。

`000`响应的外层账户编号未检出重复，内层账号有值的为6,711,033条，另有7,960条为空。CSV包含5,493,097个不同的非空合同编号、2,914,269个不同的服务地点编号；JSONL仅1,606,092条标记账户活跃。账户、合同、地点和人数不能混用，也不能把全库称为当前客户清单。

在140,000条配对样本中，124,008条`000`响应的五个身份及联系字段与CSV同序记录一致，但CSV总计少732条。CSV账号及账单州列全部为空；配对样本中，自动付款和无纸化账单的`false`与`null`均转为空值，说明转换存在信息损失。46,718条CSV内容完全重复，并不代表原始账户重复；另有16,633个空白行及1条含NUL的记录。

| 信息字段 | 有值记录数 | 占CSV数据记录 |
| --- | --- | --- |
| 账户持有人名称（`holderName`） | 6,708,900 | 99.86% |
| 业务伙伴地址（`bpAddress`） | 6,711,009 | 99.89% |
| 电话（`phone`） | 5,210,159 | 77.55% |
| 邮箱（`email`） | 2,812,945 | 41.87% |
| 驾驶证号码字段（`dlNo`） | 1,845,256 | 27.47% |
| 社会安全号码末四位字段（`lastFourSSN`） | 2,898,789 | 43.15% |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgXRic9RtibiacWmphsuSkETtkmkibFTiaicUjRicLp9YGLqc3eOj4WvaqmlalxlwwkJV7vOxueRlwBBFAw7L0z98KTDjXcIn75WpLib4g/0?wx_fmt=png)

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