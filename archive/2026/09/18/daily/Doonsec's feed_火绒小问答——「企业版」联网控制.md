---
title: 火绒小问答——「企业版」联网控制
url: https://mp.weixin.qq.com/s/STX8Xg6POLmOQ7aIB91WNw
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:55:05.548687
---

# 火绒小问答——「企业版」联网控制

# 火绒小问答——「企业版」联网控制

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

火绒终端安全管理系统2.0的联网控制功能可管控电脑程序的联网行为，支持阻止指定程序联网，或仅允许指定程序联网。该功能默认不启用，开启后每当有任意程序进行联网被阻止时，联网控制都会有弹窗提示，建议根据需要决定是否开启。下面为您详细介绍该功能的具体使用方法及相关注意事项：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01SqOLsEahJy6gquXhn3XnVQlujpc4VeHwP7vAXMQxKlTPiby3M5I8jxx5bTJ7Yic5u5ZmDwLMB6hPQL4DGQH2wt38oIRQWbSjb4As/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01Spcs16qcicxHP2L0viabZ3GDKre7KWNHAKzRHVKxlnh9vzBEDNS41mvM0QyaPUjDibqKoduIHKV5icA3uriaNuBh73qG8GibnR30oyVI/640?wx_fmt=gif&from=appmsg)

**一、使用场景**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SoDzib3gAicWJzsAyZLcgT6T0jP56tia0aB2pVibLky70fEDnomThV3bBFn3xI22qgRQOJcUZIibFB7dW3vVBmI2HmBDbfrrDazgn80/640?wx_fmt=gif&from=appmsg)

若您有下列需求，可开启联网控制并建立属于自己的联网控制规则：

* 指定电脑中一些程序不允许联网（如聊天软件），其他程序都可以联网。
* 电脑不经过允许的程序都不允许联网。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Soibdv1EPyYLlckorAtpRMWvIObJqgdVsvgkRIyouINaLQrNUxxW1a7980G9RB7KJSOanyzFaFgibrz17JTtYFqwVV8ObefoMC3I/640?wx_fmt=gif&from=appmsg)

**二、使用前提**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SpiaqlcM3H3gicz8MVQK78eibRDBeA1RLq0EjQB261V1pRIcDd0dfekEMVAWiaQiasL3DbpOOKK7SicTU34ga7Z0R3mib2zqDbapeCc70/640?wx_fmt=gif&from=appmsg)

1.**中心开启联网控制**：进入【策略管理】→【访问控制】→【联网控制】。

2.**保证策略同步到终端**：配置完成后需要将策略同步到终端（终端显示"已连接中心"且是策略同步状态）。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01Soibdv1EPyYLlckorAtpRMWvIObJqgdVsvgkRIyouINaLQrNUxxW1a7980G9RB7KJSOanyzFaFgibrz17JTtYFqwVV8ObefoMC3I/640?wx_fmt=gif&from=appmsg)

**三、 中心设置（推荐方式）**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SpiaqlcM3H3gicz8MVQK78eibRDBeA1RLq0EjQB261V1pRIcDd0dfekEMVAWiaQiasL3DbpOOKK7SicTU34ga7Z0R3mib2zqDbapeCc70/640?wx_fmt=gif&from=appmsg)

进入**【防护策略】→【策略管理】→策略详情→【访问控制】→【联网控制】**，开启"联网控制"开关。

![企业版1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrdFpaeQianmDyMIp4SS4dNVrd2JfticwbNEnyaBf9QKu9KTbBicI6CzIiaU4icEeeVSnUfVtOaMhdY2dgRQTRSdaj0ELuAAYbLQErc/640?wx_fmt=png&from=appmsg)

功能页包含以下三个配置区域：

**1. 规则外程序联网**

可设置规则之外的程序的联网动作，有两个选项：

|  |  |
| --- | --- |
| **选项** | **说明** |
| **允许联网** | 所有软件都能联网。如果只想禁止某一个或几个软件联网，选中【允许联网】后，点击【添加规则】，选择目标软件并保存，然后将该规则操作方式设为"阻止联网"，即可实现需求。 |
| **阻止联网** | 阻止所有软件联网。也可以在规则里添加目标软件，特别设置为"允许联网"。 |

**2. 自动放行设置**

可设置自动放行的范围：

|  |  |
| --- | --- |
| **选项** | **说明** |
| **自动放行带有数字签名的程序** | 在"阻止联网"模式下，选中此项会放行带有数字签名的程序（如微信、Microsoft Edge 浏览器）；没有数字签名的程序触碰联网控制规则会被自动拦截并弹窗。点击"详情"可跳转安全日志。 |
| **自动放行系统核心程序** | 放行系统核心程序。 |

**3. 联网控制规则**

点击**【添加规则】**可手动新增规则，也可对已有规则进行编辑或删除、导入、导出。

添加规则时可配置以下字段：

|  |  |
| --- | --- |
| **字段** | **说明** |
| **规则名称** | 自己设置的规则名称 |
| **规则类型** | 支持 文件信息 和 SHA1 两种类型 |
| **文件路径** | 目标程序路径（文件信息类型下），支持通配符 |
| **数字签名** | 按数字签名维度配置 |
| **版本信息** | 版本信息包含内容：文件说明、产品名称、版权、原始文件名 |
| **操作方式** | 阻止联网 或 允许联网 |

终端功能实际展示效果如下：

![企业版2.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SrsxG1hoHFXGZkg2lWGf30mXODWz0jiaOlib9FhicG9mDlibVgdLG1Qn0rez35dVXKu31K2sjuVIhriae83oklwLzGhDgguPpaNgzZw/640?wx_fmt=png&from=appmsg)

![企业版3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sqc5ic1xuB8QK74Dz9GFbJJGgmPH3K9jnwm5y0KadJIYKSToWARQH5ibkDvfk5bic6fjD0kPoqL4AOJ7DwH1vJXDCLSibPZfKdURWQ/640?wx_fmt=png&from=appmsg)

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