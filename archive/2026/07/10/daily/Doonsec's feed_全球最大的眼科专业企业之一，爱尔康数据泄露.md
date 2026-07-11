---
title: 全球最大的眼科专业企业之一，爱尔康数据泄露
url: https://mp.weixin.qq.com/s/5hAiXomKyI7sr6vcSj9Z6Q
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:02:13.400758
---

# 全球最大的眼科专业企业之一，爱尔康数据泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaNqLNrWSicIr5NicqDkwXxvkib63ctiaVE0FBheRtZUDSRpWMRZFgKJNwIeYqLro79r2JHIX1ZT8TjLPAOANINhfmlLUZhwchOibTMycFgKN62mw/0?wx_fmt=jpeg)

# 全球最大的眼科专业企业之一，爱尔康数据泄露

原创

暗网哨兵
暗网哨兵

暗网哨兵

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年5月，全球知名眼科医疗企业及医疗器械制造商Alcon（爱尔康）遭遇网络攻击。攻击者声称已获取爱尔康内部大量业务数据，并表示曾与公司进行勒索谈判，但由于双方未能达成交易，最终决定公开部分数据。

攻击者发布的信息显示，泄露数据被打包为 .7z 压缩文件，包含多个业务系统的数据，包括 MARLO 平台用户信息、Salesforce供应商数据、客户资料、订单信息、平台通信记录以及部分源代码等。

根据攻击者公布的样例文件和字段信息，该事件涉及医疗企业客户管理、供应链管理、销售运营以及内部业务系统数据，潜在影响范围覆盖爱尔康客户、合作伙伴及供应商群体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIoNAuw3weXcRD4ad7ibsD0dTUcKHk6GUM9FjCf4XRrIvUWXvT3GcFZNNrQDYibLgpSSqbccLVNOyHD07zbia35kQu28ps4Wohd9ko/640?wx_fmt=png&from=appmsg)

# 事件概况

* **事件时间：**

2026年5月

* **攻击目标：**

爱尔康（Alcon）

* **攻击类型：**

数据泄露 / 勒索攻击

* **攻击者声明：**

攻击者声称已入侵爱尔康内部系统，并获取大量业务数据。

* **攻击过程：**

1. 攻击者表示在攻击后与爱尔康展开谈判；
2. 曾向爱尔康提供部分文件样本，以证明数据真实性；
3. 双方接近达成交易时，爱尔康据称改变决定；
4. 攻击者随后公开泄露数据样本，并威胁进一步披露。

* **攻击者披露内容：**

  > “该压缩文件包含非常丰富的数据，包括MARLO用户数据、Salesforce供应商数据、对话记录、订单编号、文件源代码等。”

#

# 泄露数据详情

攻击者公布的数据压缩包为 `.7z` 格式，包含多个业务系统相关数据。

## 1. MARLO平台用户数据

攻击者声称泄露所有注册 MARLO 平台用户信息。

涉及字段包括：

| 数据类型 | 示例字段 |
| --- | --- |
| 用户身份信息 | 姓名 |
| 联系信息 | 地址、电话号码 |
| 账户信息 | 用户编号 |
| 平台交互数据 | MARLO聊天记录 |
| 业务数据 | 订单编号 |

以上字段是部分。还可能包含其他的。

---

## 2. Salesforce供应商及客户数据

泄露数据包含 Salesforce 相关业务记录。

示例字段：

```
```
cust_num
cust_name
sfdc_cust_id
strt_addr_line1
city
region
country
phone
fax
email
customer_classification
industry_code
credit_limit
account_grp
alcon_cust_nbr
main_sf_id
main_sap_id
```
```

涉及内容包括：客户基础信息、客户编号、客户名称、Salesforce客户ID、SAP客户ID、企业地址、国家/地区、联系方式、邮箱

---

### 企业经营信息：客户分类、行业类别、销售组织、分销渠道、客户等级、信用额度、账户状态

---

## 3. 供应链及销售运营数据

字段示例：

```
```
customer_classification
customer_hrchy_glbl
customer_hrchy_rgnl
order_block
credit_limit
payer_link
direct_account_link
```
```

---

## 4. 内部系统及技术数据

攻击者声称数据包还包含：

* 文件源代码
* 内部业务文件
* 系统配置数据
* 平台通信记录

还可能涉及：

* 企业应用程序代码
* 数据接口信息
* 内部业务流程资料

#

# 泄露主体简介

## 爱尔康（Alcon）是全球最大的眼科专业企业之一，专注于眼部医药品、手术设备与隐形眼镜及护理产品的研发与制造。公司历史逾75年，业务涵盖眼科手术（如白内障设备、人工晶体）和视力保健（隐形眼镜、护理液等）两大核心领域，致力于帮助全球人们改善视觉并看见更清晰的世界。该公司在瑞士日内瓦设有名义上的总部，但其营运总部位于美国德克萨斯州沃斯堡，在当地雇用了约4,500名员工。

##

**爱尔康在国内的情况**：

* **爱尔康（中国）眼科产品有限公司**

  （Alcon (China) Ophthalmic Product Co., Ltd.）成立于**1995年**，为外商独资企业，总部位于**北京**。
* 员工规模：约1000人以上，产品覆盖全国（包括边远地区）。
* **办事处/办公室**

  ：早期资料显示有**9个办事处**。目前主要包括：

+ **北京**

  （总部/主要办公室）
+ 其他城市设有区域办公室或培训中心（如上海、广州等主要城市）。

##

历史文章

[1100 万份详细的美国原始简历（跨越 20 多年，总计 1TB）！](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485825&idx=1&sn=d906eeeb2a38b0b2df346459e71a19d7&scene=21#wechat_redirect)

[意大利国家民航局数据泄露：近9000条用户记录及后台数据库曝光](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485816&idx=1&sn=f4023d8d3d87f7378e5d93f343a59831&scene=21#wechat_redirect)

[近期暗网重大泄露事件概览【20260706】](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485809&idx=1&sn=f838f5ffee79570ddd5b70aebb38254a&scene=21#wechat_redirect)

[苹果iPhone 18 Pro 被“扒光”，630GB 数据暗网曝光！](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485760&idx=1&sn=05672ad9750392031b74656e60a78fff&scene=21#wechat_redirect)

[DarkForums近10万用户档案与42万条IP关联数据遭整合发布：用户画像、历史IP及论坛资料被汇总](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485664&idx=1&sn=16eba98c80ccd85197b7b31ab3085258&scene=21#wechat_redirect)

[近期暗网重大泄露事件概览【20260701】](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485709&idx=1&sn=b8ea623f288f7fd704b2b87cd3319831&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIqToNZA7UgB4vwHbjuHIraY9sQ90LEKr3AXbMcGxtZzJjCTdMvkzuPLR7yxn4OlR8ZXBcqticCYOH1ibSEqialVbcbq3G3r84X840/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=15)

我们的服务

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIqeQnicgjXB2ROIoEBh1zyy1pkWh1TkHclBoGsCZTYf1nh4yrvW1WFeWNA6ocrSx3ibKqTLkN9NDoS4D9mbzw7duicr2XINeLVv3E/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=16)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBOjLcRoq5z6HJGh2YFWNrGpT2OCnicLfK2icJCTPNlutcb2gVia57NfRqrhN8KcI7NI4A16MZyY7zHrIiawZJ032vs7yqLKiapr5fbQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

***01 **暗网监控与风险预警*****

7×24小时持续监控全球暗网论坛、数据交易市场、黑客社区、泄露平台及地下渠道，及时发现与客户相关的数据泄露、账号泄露、敏感信息曝光、勒索软件活动等风险事件，并提供预警通报与分析服务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBMXUKEibMPGptpmTfDG2hHvFy9t5aziaf6ics8ffhLv9uPHWnUKINx7HBD0fFdsMFS4fXb9FEOjWEqyicGEFZQggbnwOa8Pc43ZrPg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)

***02 **定向数据采集服务*****

根据客户业务需求，提供定制化数据收集与整理服务。支持：指定网站数据采集，指定行业数据采集，指定国家地区数据采集，以及其他相关数据采集服务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBOOhYOtiaZoc57SOOribQLoLehLt5UDV9fct4m2zg4SFVmicYCCuJ2Cw99UTFEwBsWHuvWvBxkic7MjOIiavlvUfXXDh9maNib3M6T5o/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

***03 定制化情报服务***

针对客户个性化需求提供专项支撑。例如：舆情监测、目标画像分析，行业情报研究。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIpMOs7hINfzhbq6R8kVziccj9aJ5r7DxVve3RmOgMdFo8UiaXRB2SfwdMf7pHx4icy3XZaC1ibHfXqmJcjC9DkJnFibJ8INBEbEYcE8/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=31)

**内部社区交流群**

**加入方式**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIrAXIfcZdB7Yib7GBnMSibFgMeDJyzr8cYqwq6fXs1QOAT543r1BJbGAuQSiawdpgJFO07Ng3fBl2iaNeXMB3zEokXUfvLFqBVkt9Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/HaJr68L1tTTyCC8O1Oa7QCNiaQwscfJqPCZib6GkcFrg9UiazicTe9PZdDEwZ111UTxdTXXrgeUzibuo6AQiaMuKTpNg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

点点关注不迷路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIrrWGp3fibB8Ya39P5JtKp5ADwdziakKyGLkbVsT6BUht87anj0zvgkFtYt7XPJ7tFsQsQ0AdQnRdqDngo8RAfmTuqTjNicwawvjM/0?wx_fmt=png)

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