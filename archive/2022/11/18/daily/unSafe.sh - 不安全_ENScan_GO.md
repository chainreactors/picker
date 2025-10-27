---
title: ENScan_GO
url: https://buaq.net/go-136112.html
source: unSafe.sh - 不安全
date: 2022-11-18
fetch_date: 2025-10-03T23:05:18.723911
---

# ENScan_GO

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2b18f0d99e5de500491f090944e2f3d7.jpg)

ENScan\_GO

ENScan Go 功能列表使用程序可能导致账号被封，仅用于信息收集用途，请勿用于非法用途使用支持以下API，并支持合并数据导出
*2022-11-17 21:57:48
Author: [github.com(查看原文)](/jump-136112.htm)
阅读量:115
收藏*

---

[![Logo](https://github.com/y35uishere/ENScan_GO/raw/master/README/logo.png)](https://github.com/wgpsec/ENScan_GO)

### ENScan Go

## 功能列表

**使用程序可能导致账号被封，仅用于信息收集用途，请勿用于非法用途**

[![ENScanGo](https://github.com/y35uishere/ENScan_GO/raw/master/README/ENScanGo.png)](https://github.com/y35uishere/ENScan_GO/blob/master/README/ENScanGo.png)

* 使用支持以下API，并支持合并数据导出
  + 爱企查 (未登陆信息带\*)
  + 天眼查
  + 阿拉丁
  + 酷安市场
  + 七麦数据
  + 站长之家
  + veryvp
* 查询信息
  + ICP备案
  + APP
  + 微博
  + 微信公众号
  + 控股公司
  + 供应商
  + 客户信息
  + 小程序
  + 控股X的公司的以上所有信息
  + ...
* 通过APK市场收集使用信息

## 使用指南

ENScanGo在第一次使用时需要使用 -v 命令 生成配置文件信息

Cookie信息请勿直接 `document.cookie`，可能因为http-only 选项无法复制全导致登陆失败

[![image-20221028223835307](https://github.com/y35uishere/ENScan_GO/raw/master/README/image-20221028223835307.png)](https://github.com/y35uishere/ENScan_GO/blob/master/README/image-20221028223835307.png)

### 快速使用

**默认公司信息** (网站备案, 微博, 微信公众号, app)

**对外投资占股100%的公司 获取孙公司（深度2）**

```
./enscan -n 小米 -invest 100 -deep 2
```

**组合筛选**

大于51%控股公司、供应商、分支机构，只要ICP备案信息，并且批量获取邮箱信息

```
./enscan -n 小米 -field icp --hold --supplier --branch --email
```

**使用不同渠道**

使用天眼查数据源（或可设定为 all 组合多个数据源）

使用多数据源一起收集（暂不支持多渠道+筛选）

```
./enscan -n 小米 -type aqc,chinaz,qimai,coolapk
```

### 选项说明

#### **field 获取字段**

使用参数 `field`指定需要查询的信息，可指定多参数一起查询，方便快速收集

支持以下参数

* `icp` 网站备案信息
* `weibo` 微博
* `wechat` 微信公众号
* `app` 应用信息
* `job` 招聘信息
* `wx_app` 微信小程序
* `copyright` 软件著作权
* `supplier` 供应商信息（通过招标书确定）

#### **type 获取字段**

使用参数 `type`可以指定需要API数据源

* `aqc` 爱企查
* `tyc` 天眼查
* `all` 全部查询
* `aldzs` 阿拉丁 （仅小程序）
* `coolapk` 酷安市场 （仅APP）
* `qimai` 七麦数据（仅APP）
* `chinaz` 站长之家（仅ICP备案）

#### 完整参数

| 参数 | 样例 | 说明 |
| --- | --- | --- |
| -n | 小米 | 关键词 |
| -i | 29453261288626 | 公司PID（自动识别类型） |
| -f | file.txt | 批量查询，文本按行分隔（可选PID模式） |
| -type | aqc | API类型 |
| -o |  | 结果输出的文件夹位置(可选) |
| -is-merge |  | 合并导出 |
| -invest |  | 投资比例 |
| -field | icp | 获取字段信息 |
| -deep | 1 | 递归搜索n层公司 |
| -hold |  | 是否查询控股公司 |
| -supplier |  | 是否查询供应商信息 |
| -branch |  | 查询分支机构（分公司）信息 |
| -is-branch |  | 深度查询分支机构信息（数量巨大） |
| -api |  | 是否API模式 |
| -client |  | 客户端模式通道 |
| -debug |  | 是否显示debug详细信息 |
| -is-show |  | 是否展示信息输出 |
| -uncertain-invest |  | 包括未公示投资公司（无法确定占股比例） |
| -is-group |  | 查询关键词为集团 |
| -is-pid |  | 批量查询文件是否为公司PID |
| -delay |  | 每个请求延迟（S）-1为随机延迟1-5S |
| -proxy |  | 设置代理 |
| -timeout |  | 每个请求默认1（分钟）超时 |
| -no-merge |  | 批量查询【取消】合并导出 |
| -v |  | 版本信息 |
| -email |  | 获取email信息 |

### API模式

ENScanGo可使用API模式进行分布式部署，搭建API服务构建资产处理

使用`rmq`作为任务队列组件，在redis存入任务信息，可分部署部署。数据可存储至mongodb进行调用分析。

**api调用效果（前端开发中）**

[![image-20221028231744940](https://github.com/y35uishere/ENScan_GO/raw/master/README/image-20221028231744940.png)](https://github.com/y35uishere/ENScan_GO/blob/master/README/image-20221028231744940.png)

[![image-20221028231815437](https://github.com/y35uishere/ENScan_GO/raw/master/README/image-20221028231815437.png)](https://github.com/y35uishere/ENScan_GO/blob/master/README/image-20221028231815437.png)

[![image-20221028231831102](https://github.com/y35uishere/ENScan_GO/raw/master/README/image-20221028231831102.png)](https://github.com/y35uishere/ENScan_GO/blob/master/README/image-20221028231831102.png)

[![image-20221028232013627](https://github.com/y35uishere/ENScan_GO/raw/master/README/image-20221028232013627.png)](https://github.com/y35uishere/ENScan_GO/blob/master/README/image-20221028232013627.png)

#### API说明

在获取信息的内容在数据库内不存在时，会自动添加队列任务收集相关信息

**状态信息**

返回当前系统状态信息

**获取信息**

```
GET /api/info?search=小米&invest=100&branch=true
```

| 参数 | 参数 | 说明 |
| --- | --- | --- |
| orgname | 文本 | 完整公司名称（二选一） |
| search | 文本 | 模糊匹配公司名称（二选一） |
| type | 文本，与命令参数一致 | 数据源 |
| field | 文本，与命令参数一致 | 筛选指定信息 |
| duplicate | true | 加上参数去重 |
| depth | 数字 | 爬取几层公司 如 2 为孙公司 |
| invest | 数字 | 筛选投资比例 |
| holds | true | 筛选控股公司 |
| supplier | true | 筛选供应商信息 |
| branch | true | 筛选分支信息 |
| output | true | 为true导出excel表格 |

**股权穿透**

返回投资、股东关联信息

| 参数 | 参数 | 说明 |
| --- | --- | --- |
| orgname | 文本 | 完整公司名称 |
| search | 文本 | 模糊匹配公司信息 |
| duplicate | true | 是否去重 |

**添加获取任务**

添加新的任务信息

| 参数 | 参数 | 说明 |
| --- | --- | --- |
| orgname | 文本 | 完整公司名称 |
| update | true | 是否更新 |
| type | 文本，与命令参数一致 | 数据源 |
| invest\_rd | true | 不确定投资 |
| branch | true | 获取分支信息 |
| field | 文本，与命令参数一致 | 筛选字段 |
| invest | 数字 | 投资信息 |

#### 启动部署

首先我们需要对配置文件进行修改，加入数据库连接信息，与common同级加入以下配置

```
api:
  server: "127.0.0.1" # redis地址
  mongodb: "mongodb://user:[email protected]:27017" # mongodb 连接信息
  redis: "redis_password" # redis 密码
  port: "8080" # 启动API端口
```

**API模式**

启动API模式将在配置端口监听，并启动api服务，可通过api服务进行调用读取数据

在此场景下无需配置cookie信息

**客户端模式**

可作为部署节点，读取任务队列自动读取信息写入数据库

## 交流&反馈

关注公众号 `WgpSec狼组安全团队` 回复`加群`一起交流~

[![](https://camo.githubusercontent.com/37de137e218f4975cd0c9c5882d2fb5e90f3a79bb3d8cc2c4931755c77619f9a/68747470733a2f2f6173736574732e7767707365632e6f72672f7777772f696d616765732f7765636861742e706e67)](https://camo.githubusercontent.com/37de137e218f4975cd0c9c5882d2fb5e90f3a79bb3d8cc2c4931755c77619f9a/68747470733a2f2f6173736574732e7767707365632e6f72672f7777772f696d616765732f7765636861742e706e67)

[![Stargazers over time](https://camo.githubusercontent.com/0c2e53408721a1d54dfc90c2a824ef93b6a693f8ea260a7a04a350a949937cae/68747470733a2f2f7374617263686172742e63632f7767707365632f454e5363616e5f474f2e737667)](https://starchart.cc/wgpsec/ENScan_GO)

## 404星链计划

[![](https://github.com/knownsec/404StarLink/raw/master/Images/logo.png)](https://github.com/knownsec/404StarLink/raw/master/Images/logo.png)

ENScanGo 现已加入 [404星链计划](https://github.com/knownsec/404StarLink)

## JetBrains OS licenses

`ENScanGo` had been being developed with `GoLand` IDE under the **free JetBrains Open Source license(s)** granted by JetBrains s.r.o., hence I would like to express my thanks here.

[![](https://raw.githubusercontent.com/wgpsec/.github/master/jetbrains/jetbrains-variant-4.png)](https://www.jetbrains.com/?from=wgpsec)

文章来源: https://github.com/y35uishere/ENScan\_GO
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)