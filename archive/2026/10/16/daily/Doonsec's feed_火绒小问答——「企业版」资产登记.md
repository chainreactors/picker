---
title: 火绒小问答——「企业版」资产登记
url: https://mp.weixin.qq.com/s/wcGHZLA1nG3TBcKZPS-_mw
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:31:42.889952
---

# 火绒小问答——「企业版」资产登记

# 火绒小问答——「企业版」资产登记

火绒安全
火绒安全

火绒安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz6h5nbHLqtyUeLADJt7ewgFh6AbCAxQeO9D2y9CcDK7liaJDD5PZGwbqURKywb0SqKeiaCUIgyLTVkw/640?wx_fmt=gif&from=appmsg#imgIndex=0)

**尊敬的用户，您好！**

资产登记是火绒终端安全管理系统2.0资产管理模块下的核心功能，用于向终端下发登记任务，收集终端用户信息，同时中心自动统计终端的软件、硬件及操作系统信息，便于管理员对全网资产进行统一管理。下面为您详细介绍该功能的具体使用方法及相关注意事项：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01SqOLsEahJy6gquXhn3XnVQlujpc4VeHwP7vAXMQxKlTPiby3M5I8jxx5bTJ7Yic5u5ZmDwLMB6hPQL4DGQH2wt38oIRQWbSjb4As/640?wx_fmt=gif&from=appmsg)

![企业版1.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpJ4fcwBfTPazosg09dPiaJQc6TBN4aiaHKp1fBu7opLlbjARhIy5SoL2yPVJ0FalAXEbrbSKjNDNeWRhT3M6CWpsRNBlNQ4tyhE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01Spcs16qcicxHP2L0viabZ3GDKre7KWNHAKzRHVKxlnh9vzBEDNS41mvM0QyaPUjDibqKoduIHKV5icA3uriaNuBh73qG8GibnR30oyVI/640?wx_fmt=gif&from=appmsg)

**一、功能入口**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SoDzib3gAicWJzsAyZLcgT6T0jP56tia0aB2pVibLky70fEDnomThV3bBFn3xI22qgRQOJcUZIibFB7dW3vVBmI2HmBDbfrrDazgn80/640?wx_fmt=gif&from=appmsg)

【资产管理】→【资产登记】，包含两个子页面：

|  |  |
| --- | --- |
| **子页面** | **功能** |
| **资产登记管理** | 管理终端资产登记任务，查看/编辑终端登记信息 |
| **登记信息管理** | 自定义需要登记的信息项（名称、必填/选填、输入类型） |

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Soibdv1EPyYLlckorAtpRMWvIObJqgdVsvgkRIyouINaLQrNUxxW1a7980G9RB7KJSOanyzFaFgibrz17JTtYFqwVV8ObefoMC3I/640?wx_fmt=gif&from=appmsg)

**二、使用步骤**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SpiaqlcM3H3gicz8MVQK78eibRDBeA1RLq0EjQB261V1pRIcDd0dfekEMVAWiaQiasL3DbpOOKK7SicTU34ga7Z0R3mib2zqDbapeCc70/640?wx_fmt=gif&from=appmsg)

**步骤一：配置登记信息（登记信息管理）**

进入**【资产管理】→【资产登记】→【登记信息管理】**，点击**【新增】**按钮，填写登记信息：

![企业版2.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sr94zdaY2mibIpgdYgxYQksTRT81ribBvBSFBvFTfajLWxKskmK6ukUHjoicatpdUJmbsc3EscNeIF0VQvnwiahx1Z1NOcdO5wd954/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **配置项** | **说明** |
| **登记信息** | 填写此登记信息项的名称（如：姓名、工号、部门、位置等），不超过10个字 |
| **是否必填** | 选择【必填项】或【非必填项】 |
| **输入类型** | 支持三种类型：**文本输入框、数字输入框、下拉列表**（选择下拉列表时需要添加列表项） |
| **引导提示信息设置** | 可选，设置提示语，如"请按照以下格式输入：A分组-张三" |

登记信息列默认显示"终端名称"，点击【设置】可开启终端名称登记并设置引导提示。登记后用户填写的终端名称会自动同步至中心，并将当前终端的终端名称修改为登记上报的信息，此功能可配合分组规则一起使用实现快速分组。

**步骤二：下发资产登记任务（资产登记管理）**
进入**【资产管理】→【资产登记】→【资产登记管理】**，选中需要下发登记任务的终端，点击**【重新登记】**按钮：

* 可设置是否强制登记（终端是否必须填写）。
* 可设置终端页面上是否可查看已填写信息。
* 点击【确定】后，中心将对选中的终端重新下发资产登记任务

终端收到任务后，需填写登记信息并上报至中心。

**步骤三：查看与管理登记结果**

在**【资产管理】→【资产登记】→【资产登记管理】**页面查看所有终端的登记信息：

* 编辑信息：选中终端，点击【编辑信息】按钮，可对终端当前登记的信息进行编辑修改 。
* 导入：支持导入xlsx或csv格式的登记信息，以MAC地址作为索引替换对应终端的登记信息（导入前请确保中心已创建对应的登记信息字段）。
* 导出：将当前登记的终端信息导出为xlsx格式数据表 。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Soibdv1EPyYLlckorAtpRMWvIObJqgdVsvgkRIyouINaLQrNUxxW1a7980G9RB7KJSOanyzFaFgibrz17JTtYFqwVV8ObefoMC3I/640?wx_fmt=gif&from=appmsg)

**三、 进阶设置（登记设置）**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SpiaqlcM3H3gicz8MVQK78eibRDBeA1RLq0EjQB261V1pRIcDd0dfekEMVAWiaQiasL3DbpOOKK7SicTU34ga7Z0R3mib2zqDbapeCc70/640?wx_fmt=gif&from=appmsg)

在资产登记管理页面点击**【设置】**按钮，可进行以下配置：

![企业版3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Spich5BY9CBBm5I19T0KKMxTbDBj0Km9hceIibWcXniczibW9VaJ4wEAZG3zSyIloj2Zq1IEic21EvlZnXPmkQia0egRyEtfgw6W1lGU/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **设置项** | **说明** |
| **开启终端安装资产登记** | 开启后，终端在安装时需先进行资产登记，登记后信息同步至控制中心，未登记无法完成安装 |
| **开启终端分组登记** | 需先开启终端安装资产登记，开启后终端登记信息中增加"终端分组"登记项 |
| **终端重新上报资产信息在终端离线（30）天** | 启用后，当终端离线达到设置的天数时，终端会弹出登记页面提醒用户重新登记 |
| **开启用户自助登记** | 开启后，终端用户可在火绒安全终端主面板打开自助登记，自行上报登记信息 |

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Soibdv1EPyYLlckorAtpRMWvIObJqgdVsvgkRIyouINaLQrNUxxW1a7980G9RB7KJSOanyzFaFgibrz17JTtYFqwVV8ObefoMC3I/640?wx_fmt=gif&from=appmsg)

**四、 配套的资产统计功能（自动采集）**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SpiaqlcM3H3gicz8MVQK78eibRDBeA1RLq0EjQB261V1pRIcDd0dfekEMVAWiaQiasL3DbpOOKK7SicTU34ga7Z0R3mib2zqDbapeCc70/640?wx_fmt=gif&from=appmsg)

除了主动登记外，中心会自动统计全网终端的以下信息，无需额外配置：

|  |  |
| --- | --- |
| **功能** | **说明** |
| **软件管理** | 按全网统计软件安装情况（名称、发布者、版本号、安装率），可推送卸载任务并导出软件清单 |
| **系统管理** | 统计全网操作系统版本信息、安装时间、激活状态，提供操作系统占比可视化数据图 |
| **硬件管理** | 统计全网终端CPU、内存、硬盘、网卡、显卡、主板等硬件信息，支持硬件清单导出，并记录硬件变更历史 |

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Soibdv1EPyYLlckorAtpRMWvIObJqgdVsvgkRIyouINaLQrNUxxW1a7980G9RB7KJSOanyzFaFgibrz17JTtYFqwVV8ObefoMC3I/640?wx_fmt=gif&from=appmsg)

**五、 注意事项**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SpiaqlcM3H3gicz8MVQK78eibRDBeA1RLq0EjQB261V1pRIcDd0dfekEMVAWiaQiasL3DbpOOKK7SicTU34ga7Z0R3mib2zqDbapeCc70/640?wx_fmt=gif&from=appmsg)

1.**导入数据前**，需先在【登记信息管理】中创建对应的登记信息字段，否则导入会失败。

2.登记信息名称**不超过10个字**。

3.资产登记任务需要通过**终端管理→终端概况**勾选终端后下发，终端需在线才能收到任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

尊敬的用户：

若您有其他产品使用问题，可通过以下方式联系我们~

****微信公众号******：**主界面---常见问题---人工客服

****火绒官方论坛：****https://bbs.huorong.cn/

****火绒官方服务热线：****400-998-3555（法定工作日8:30-20:30，法定节假日9:30-18:30）

**关于公司**

火绒安全成立于2011年，是一家专注、纯粹的安全公司，致力于在终端安全领域为用户提供专业的产品和专注的服务，并持续对外赋能反病毒引擎等相关自主研发技术。多年来，火绒安全产品凭借“专业、干净、轻巧”的特点收获了广大用户的良好口碑。火绒企业版产品更是针对企业内外网脆弱的环节，拓展了企业对于终端管理的范围和方式，提升了产品的兼容性、易用性，最终实现更直观的将威胁可视化、让管理轻便化，充分达到保护企业信息安全的目的。

![2d3f91dee3e0747ac5c5fde2bd0de26d.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrJGjzAFJIoicNgkceY4J2RUrwX3qeMkpKttIZKCic0GsicH8YgyDIsT4l75HvsOBMYI6Jds3vMc4gns2u8CmFkO7clQYmfs9icD90/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Sq255bgLyhw0PsXalANTTDdm5ONEHiaT98hYFbmG2cIQaOibibv3GmkxXc6b2bYEOibFfydxp2Wte24MtianbEVCtIwWxlQpMibNHAiao/640?wx_fmt=gif&from=appmsg)

**点点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01SoytWicazjuKgzGlQjA6TrwAticUVAZtbSkednAjDcDG4ma9faBsIbA232JH8sveEQRSlRicPmicNjDrO34zd7Cv15iaIR2iaVK1lDCs/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SodkUzg3jjaL8UVInPOGBQOukRdyVm2gGRRpGQhFB1z7DIIU22icSjiaQsasicNFqGJXzuRUKYuUk3hLbq40RuCaia8zRp8GHzsL7Q/640?wx_fmt=gif&from=appmsg)

**点喜欢**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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