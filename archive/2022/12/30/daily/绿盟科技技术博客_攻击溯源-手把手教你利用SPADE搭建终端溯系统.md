---
title: 攻击溯源-手把手教你利用SPADE搭建终端溯系统
url: http://blog.nsfocus.net/spade/
source: 绿盟科技技术博客
date: 2022-12-30
fetch_date: 2025-10-04T02:44:50.494505
---

# 攻击溯源-手把手教你利用SPADE搭建终端溯系统

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 攻击溯源-手把手教你利用SPADE搭建终端溯系统

### 攻击溯源-手把手教你利用SPADE搭建终端溯系统

[2022-12-29](https://blog.nsfocus.net/spade/ "攻击溯源-手把手教你利用SPADE搭建终端溯系统")[薛见新](https://blog.nsfocus.net/author/xuejianxin/ "View all posts by 薛见新")[攻击溯源](https://blog.nsfocus.net/tag/%E6%94%BB%E5%87%BB%E6%BA%AF%E6%BA%90/)

阅读： 2,426

## ****一、终端溯源背景介绍****

攻击溯源图是描述攻击者攻击行为相关的上下文信息，利用攻击溯源信息来挖掘攻击相关的线索是当前研究的热点。研究人员发现依靠系统监控日志数据构造具有较强抽象表达能力的溯源图进行因果关系分析，能有效表达威胁事件的起因、攻击路径和攻击影响，为威胁发现和取证分析提供较高的检测效率和稳健性。

关于终端溯源的工作学术上已有不少研究工作[1]，这里基于SPADE[2]工具以及相关的终端采集工具（windows系统的ProcMon[3]，linux系统下的audit[4],camflow[5]）搭建一个简单的终端溯源图系统，来实现攻击溯源。

## ****二、S********PADE********工具简介****

SPADE是一个开源的系统，可以实现溯源数据的推理、存储与查询功能。该系统是一种跨平台的溯源系统，可以应用到区块链、在线社交网络与APT溯源调查中。SPADE可以看成一个分布式的溯源调查工具，以溯源图的形式组织系统日志，溯源攻击过程。该工具支持多种操作系统。SPADE系统支持多种应用，本文只专注其在溯源调查上的应用。该团队基于该系统有多篇顶会顶刊的研究成果，同时该工具声称支持了darpa TC项目，即darpa TC数据集有他们的贡献。

SPADE的特性包括：

* ****跨平台****

SPADE提供了一种跨平台的数据****收集、过滤、存储和查询****服务，支持Linux, Mac OS X, and Windows操作系统，使用操作系统各自的审计功能透明地记录所有数据的溯源信息。

* ****易于部署****

SPADE收集系统审计日志并自动生成溯源图，且不需要对操作系统和应用程序做任何修改。SAPDE主要针对采集器的日志整理得到进行的操作、文件操作等信息。

* ****灵活查询****

SPADE支持使用变量、约束、lineage、路径和集合操作符查询本地的provenance记录，同时支持图和关系 (SQL) 查询，并可以使用第三方工具 (如Neoclipse 和SQL Workbench)进行管理。

SPADE的功能架构如图1所示。下面介绍一下SPADE的核心模块。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_96c81f83-323e-4824-a95c-d23c5cc2e623-260x300.png)

图1 SPADE系统架构

* 数据输入

SPADE支持多种类型的数据，针对windows其支持ProcMon工具采集的日志，linux系统下支持audit、camflow工具采集的日志，同时支持文本数据输入，但输入的格式需要满足其定义的模式要求。

* reporter模块

reporter模块是SPADE的核心模块，它接收来自不同源的数据。从数据中提取有效的实体关推断实体之间的关系，构建有效的溯源图。同时也支持按用户自定义的模式构建溯源图。

* filter模块

Filter模块主要用于对reporter构建的溯源图进行剪枝，通过分析可以看到终端日志非常庞大，存在明显的依赖爆炸问题。但是具体的Filter的原理在其发表的论文中并没有特别详细的介绍。

* 存储模块

SPADE内置了neo4j图数据，也支持关系型数据的存储，同时也支持前面提到的文本格式的存储。

* 查询模块

支持针对溯源图的查询，查询语文是其自定义的。

## ****三、终端溯源系统搭建****

### 3.1 SPADE安装

Linux系统下的SPADE支持audit工具与camflow工具，其中关于audit日志的方法博客[6]有相关的介绍。本文介绍一下windows10下SPADE系统的安装部署。

由于windows主要是基于ProcMon采集的数据进行处理的，因此需要安装process monitor。SPADE在windows上有两种安装方式基于WSL与cygwin。WSL安装参考[1]。具体情况具体分析，有可能碰到安装问题，windows操作系统上安装WSL的教程比较多这里就不详细介绍。

cywin是一个在windows平台上运行的类UNIX模拟环境。它的安装比较简单直接下载相应的安装包即可，参考博客[7]。在安装的时候需要预安装一些包：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_cfd0c614-4351-4fef-9fac-ba8abc0d6673-300x69.png)

打开cygwin，下载SPADE源代码：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_f69ec226-84e6-4a6b-a43b-82366b31e4cd-300x23.png)

这里需要把java加入到PATH变量中，需要安装JDK，JDK的版本必须是11，12 ，13。最新的JDK版本不支持。

* export PATH=$PATH:/cygdrive/c/Program\ Files/Java/jdkXXX/bin

接下来编译安装SPADE:

* cd SPADE
* ./configure
* make

有的时候会失败，失败的话查看相关日志。

启动SPADE服务（需要在SPADE/bin目录下）：

* ./spade start

启动成功并不代表安装成功。

开启controler来配置SPADE:

* ./spade control

结果如图2所示，则表示SPADE安装成功：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_e2e671be-326d-414e-9e63-a98bc1e59507-300x97.jpg)

图2 SPADE 控制器启动成功

经常会碰到SPADE is not running的问题，具体可以查看相关日志，这里碰到的问题基本是java运行内存不足，如图3所示。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_4109fb8a-4858-4b41-adb0-860c4258cbb6-300x125.png)

图3 SPADE 运行问题日志

**3.2 S****PADE****与P****rocMon****联调**

SPADE reporter支持ProcMon，该模块是对接微软的ProcMon工具的。Process Monitor一款微软的系统监视软件，下载即可用。打开ProcMon自动会采集相关数据，数据量非常大十多分钟就9个G的文档。当然该工具功能比较强大可以加一些过滤。

SPADE与ProcMon联动过程：

* 启动ProcMon采集相关数据（这里可以执行相关模拟攻击的操作）
* 关闭ProcMon
* 保存ProcMon的日志，这里只能手动保存，同时SPADE只支持XML格式。
* 在SPADE 控制器中配置ProMon reporter的路径：
* Add reporter ProcMon input=xxx(ProcMon日志的路径)

对ProcMon的支持并不是很友好，但是SPADE还支持DSL管道数据，Graphviz与JSON格式配置。

### **3.3 效果展示**

SPADE支持多种输出形式，支持neo4j图数据，关系数据、文本，文本类型有Graphviz、Prov以及JSON。

SPADE的安装包里已内置了neo4j图数据。

首先需要配置SPADE的存储方式：

* spade start
* spade control

-> add storage Neo4j database****=****spade.graph

进入SPADE目录：

* sudo vim lib/neo4j-community-4.1.1/conf/neo4j.conf
* directories.data ****=****spade.graph
* connector.http.listen\_address****=****0.0.0.0:7474
* connector.bolt.listen\_address****=****0.0.0.0:7687

为了方便启动neo4j，我们同样为neo4j设置环境变量：

* sudo vim /etc/profile
* ExportPATH****=****$PATH:/home/alston/SPADE/lib/neo4j-community-4.1.1/bin
* source/etc/profile
* 启动neo4j：
* spade stop
* alston@ubuntu-vm:~/SPADE/lib/neo4j-community-4.1.1$ neo4j start

这里只能先关闭SPADE才能启动neu4j，其他输出类似必须得先关闭SPADE才能有输出结果。最终的效果如下图所示。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_66aab95f-4497-45bb-bcfb-0e3e627ecac4-300x158.png)

图4 neo4j的终端示例

终端溯源调查系统基本搭建完成，用户可以利用neo4j的查询Cypher进行调查，也可以通过接口取图数据进行分析。

## ****四、结论****

SPADE工具是一相对已经成熟。其优势是可以继承多种终端采集工具，如ProcMon，camflow，以及audit等。其部署灵活，有强大的数据压缩机制能把海量的终端数据压缩到能接受的量级，但是中间的数据损失无法评估。同时图的模式是固定，使用者无法进行修改，这降低了该工具的扩展性。此外，该工具无法实现终端实时监控分析功能。

### 参考文献

1 https://mp.weixin.qq.com/s/cPrgQaTtrZNhe3Iaz6ZN5g

2 <https://github.com/ashish-gehani/SPADE>

3 <https://docs.microsoft.com/en-us/sysinternals/downloads/procmon>

4 <https://zhuanlan.zhihu.com/p/337289840>

5 <https://camflow.org/>

6 <https://zhuanlan.zhihu.com/p/524145892>

7 <https://blog.csdn.net/xiaojin21cen/article/details/125146944>

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/dns/)

[Next](https://blog.nsfocus.net/exchange-server-owassrfcve-2022-41080-cve-2022-41082/)

### Meet The Author

薛见新

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)