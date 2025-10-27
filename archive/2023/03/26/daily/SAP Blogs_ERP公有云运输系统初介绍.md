---
title: ERP公有云运输系统初介绍
url: https://blogs.sap.com/2023/03/25/erp%e5%85%ac%e6%9c%89%e4%ba%91%e8%bf%90%e8%be%93%e7%b3%bb%e7%bb%9f%e5%88%9d%e4%bb%8b%e7%bb%8d/
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:44.226180
---

# ERP公有云运输系统初介绍

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* ERP公有云运输管理初介绍

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51768&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ERP公有云运输管理初介绍](/t5/enterprise-resource-planning-blog-posts-by-sap/erp%E5%85%AC%E6%9C%89%E4%BA%91%E8%BF%90%E8%BE%93%E7%AE%A1%E7%90%86%E5%88%9D%E4%BB%8B%E7%BB%8D/ba-p/13559639)

![Feng_Chen](https://avatars.profile.sap.com/b/5/idb510cba38534353e6e96c15e92188a99b8fc88c9077c6f14b97c3533231e8946_small.jpeg "Feng_Chen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Feng\_Chen](https://community.sap.com/t5/user/viewprofilepage/user-id/132169)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51768)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51768)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559639)

‎2023 Mar 25
9:47 AM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51768/tab/all-users "Click here to see who gave kudos to this post.")

2,374

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sales](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Sales

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

View products (3)

# **Transportation Management****主数据**

### 1.TM货运订单中需要的**组织架构**：

* 公司代码

* 采购组织

* 采购组

![](/legacyfs/online/storage/blog_attachments/2023/03/org1.png)

### **2.****业务伙伴**

承运方是与运输流程最相关的业务伙伴，您将货运订单分包给承运方，并且协商货运协议。

![](/legacyfs/online/storage/blog_attachments/2023/03/partner-2.png)

业务伙伴（常规）保存一些一般信息，如名称、搜索词、公司形式、地址和付款细节；

承运方角色用在货运订单和货运协议中；

供应商和供应商（财务会计）链接到组织架构比如公司代码和采购组织，运行财务流程比如支付运费。

### **3.地点**

每个货运单元必须有一个源地点和目标地点，分别代表运输开始的发货点和客户的交付地址。

![](/legacyfs/online/storage/blog_attachments/2023/03/location1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/location2.png)

### **4.****设备组和设备类型**

设备组和设备类型用来代表运输能力

![](/legacyfs/online/storage/blog_attachments/2023/03/EP1.png)

（CBC：Define Equipment Groups and Equipment Types）

运输工具组STR代表陆运，每个工具类型都可以维护具体的描述，负载重量或者立方容量

![](/legacyfs/online/storage/blog_attachments/2023/03/EP2.png)

# **配置物流集成**

### **1.****货运单元**

货运单元在业务凭证如销售订单，采购订单，STO创建后被创建。货运单元可以是：

* 可以一起输运的一套货物

* 用于合并可以一起运输的项目

* 货物的最小单位

* 用于货运计划

![](/legacyfs/online/storage/blog_attachments/2023/03/FU1.png)

### **创建货运单元**

在销售运输流程中，通过配置销售订单的运输相关性决定是否创建货运单元：

* 销售组织

* 分销渠道

* 产品组

* 销售订单类型

* 发货条件

![](/legacyfs/online/storage/blog_attachments/2023/03/peizhi1-1.png)

（CBC：Define Transportation-Relevance of Sales Documents）

* 控制代码0052定义销售订单与输运相关

* 物流集成参数文件S001: External Planning Outbound、S002: Internal Planning Outbound

![](/legacyfs/online/storage/blog_attachments/2023/03/peizhi2.png)

### **管理货运单元**

作为运输经理，您可以通过APP：管理货运单元跟踪货运单位，并了解任何问题，例如计划积压和延误。

* 根据相关规则（前趋凭证、源地点、目标地点）搜索、过滤、排序和分组货运单元列表。

![](/legacyfs/online/storage/blog_attachments/2023/03/manage_freight_unit.png)

* 选择货运单元浏览详细信息

比如您可以在项目下查看待运输的产品、件数、毛重和总体积等信息。

![](/legacyfs/online/storage/blog_attachments/2023/03/FU2-1.png)

在执行页签，查看运输的所有事件比如检出，装货，启运和送达。

![](/legacyfs/online/storage/blog_attachments/2023/03/FU3.png)

在凭证流中查看前趋和后继业务凭证

![](/legacyfs/online/storage/blog_attachments/2023/03/FU4.png)

### **2.管理货运协议**

运输系统中所有财务数据的锚就是货运协议。货运协议是采购组织和承运方之间关于货物的服务和定价。您可以通过APP：管理货运协议维护货运协议。

在货运协议的抬头部分，您可以维护基本信息比如：

* 采购组织

* 承运方

* 有效起始日期/失效日期

* 凭证货币

* 常规条款（主运输模式、装运类型）

![](/legacyfs/online/storage/blog_attachments/2023/03/FA0.png)

货运协议中最重要的元素就是计算单（Calculation Sheet），计算单定义了货运订单定价逻辑，由多项计算单项组成，每项包含以下：

* 费用类型

费用类型可以为费用分类，比如运输的基本收费或特定处理，危险货物的附加费。

![](/legacyfs/online/storage/blog_attachments/2023/03/FA1.png)

* 费率（固定金额、百分比或者费率表）

![](/legacyfs/online/storage/blog_attachments/2023/03/FA5.png)

* 计算解析基础（ROOT, Product 或者 Stage）

ROOT：货运订单抬头

Stage：利用Stage属性，比如访问地点之间的距离

Product：当产品属性比如产品数量，重量或者体积需要被使用时

![](/legacyfs/online/storage/blog_attachments/2023/03/FA4.png)

费用类型可以指定一个统一费率表或参考费率表，其中包括费率价格。

![](/legacyfs/online/storage/blog_attachments/2023/03/FA2.png)

费率表可以由几个维度组成，这些维度引用了定义费率表结构的各个尺度。您可以通过APP：管理费率表来创建和编辑费率表详细信息，这些费率表对于在多个货运协议中经常需要的运输费用很有用，比如装卸费、保险费、过路费等。

案例1保险费：

设定了基于货物价值与费率的计算方式，当货物价值大于等于0时，费率是1%

![](/legacyfs/online/storage/blog_attachments/2023/03/FA3.png)

在测试中货运订单的货运价值为100000时，那么保险费为100000\*0.007=700。

案例2基础费：

设定了基于源位置+目的地地点+运输工具类型来决定具体固定费用

![](/legacyfs/online/storage/blog_attachments/2023/03/FA6.png)

* 计算方法（Standard, Clipping）

举例如下费率表：

|
 **重量** |
 **费率** |

|
 低于等于100KG |
 2 CNY/KG |

|
 低于等于 200KG |
 1.8 CNY/KG |

|
 低于等于 500KG |
 1.5 CNY/KG |

采用Standard计算方法

* 重量95 KG，费用：95 KG\*2=190 CNY

* 重量 110 KG，费用：110 KG\*1.8=198 CNY

采用Clipping计算方法

* 重量95KG， 费用：95 KG\*2=190 CNY

* 重量 110 KG，费用：100 KG\*2+10 KG\*1.8=218 CNY

# **手动运输计划** **–** **外向（****4MO****）**

### **业务流程**

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO1-1.png)

### **1.创建销售订单**

在销售订单抬头-装运中输入装运条件与装运类型触发TM

![](/legacyfs/online/storage/blog_attachments/2023/03/SO1.png)

### **2.执行手动运输计划**

APP：运输主控室，输入货运单元阶段源位置和目标位置然后执行

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO2.png)

选择货运单元，创建卡车类型并且选择，点击分配选定项目，点击保存生成右屏幕的货运订单

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO3.png)

### **3.执行承运方转包**

APP：管理货运订单，找到之前创建的货运订单，打开编辑在基本信息中输入承运方、采购组织、采购组，然后点击费用：

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO3.5.png)

这里费用类型SF00价格1000 CNY为手工输入，由于费用表设置的条件和该货运订单的条件不匹配，所以没有自动带出金额，需要手工输入，而这也满足客户的实际业务需求，比如每个货运订单的运费都不固定并且没有规则，需要手工输入。

费用类型SO05保险费，是货运价值100000（销售订单不含税价）\*费率0.7%=700 CNY

总运费金额=1000+700=1700 CNY

点击转包更改状态，发送到运输公司，根据实际业务再更改成设置为“运输公司已确认”。

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO4.png)

这时货运订单的转包状态会变成以下：

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO5.png)

### **4.监控货运订单触发交货创建**

APP: 管理货运订单，点击创建交货

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO6.png)

通过凭证流查到交货单凭证号

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO7.png)

### **5.设置货车已在装运点位置到达并已检入**

APP: 管理货运订单，点击执行状态选择设置为“已做好运输执行准备”

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO8.png)

根据实际卡车运输状态，在基本信息页面下的阶段，选择执行状态（源）设置为“已运达”，然后改成设置为“已检入”，保存后会提示费用计算已完成和成本分摊已完成。

![](/legacyfs/online/storage/blog_attachments/2023/03/4MO9.png)

### **6.执行拣配**

由于这步不复杂，详细参考文档最佳业务实践：手动运输计划 – 外向（4MO）

### **7.设置货车已在装运点检出并启运**

在基本信息页面下的阶段，...