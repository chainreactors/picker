---
title: 火绒小问答——「企业版」中心地址管理使用方法
url: https://mp.weixin.qq.com/s/3O0rtUHRElO1swzqZ-JjAg
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:41:37.367898
---

# 火绒小问答——「企业版」中心地址管理使用方法

# 火绒小问答——「企业版」中心地址管理使用方法

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

火绒终端安全管理系统2.0的中心地址管理（多中心功能）主要针对有分公司的企业：员工需要在总公司和分公司之间来回办公时，如果只在总公司部署一个控制中心，员工到分公司后终端会脱离管控。配置后，当终端无法连接当前中心时，会自动尝试连接预设的其他控制中心，确保终端持续被管控、策略随之同步。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01SqOLsEahJy6gquXhn3XnVQlujpc4VeHwP7vAXMQxKlTPiby3M5I8jxx5bTJ7Yic5u5ZmDwLMB6hPQL4DGQH2wt38oIRQWbSjb4As/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrqXF4pjedAgFiaZQGn7FTySlC2FNAia17H45zF7icgoJnXMSTDv7Nd3ian30mVgJet3horia1ArcYPXIF4sufYNdVuhlgicu17jibuDc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01Spcs16qcicxHP2L0viabZ3GDKre7KWNHAKzRHVKxlnh9vzBEDNS41mvM0QyaPUjDibqKoduIHKV5icA3uriaNuBh73qG8GibnR30oyVI/640?wx_fmt=gif&from=appmsg)

**使用步骤**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SoDzib3gAicWJzsAyZLcgT6T0jP56tia0aB2pVibLky70fEDnomThV3bBFn3xI22qgRQOJcUZIibFB7dW3vVBmI2HmBDbfrrDazgn80/640?wx_fmt=gif&from=appmsg)

1.登录火绒控制中心，进入**【中心管理】→【中心设置】→【中心地址管理】**。

2.点击【添加】按钮，填写：

* **中心地址**（如127.0.0.1格式的IP或域名）
* **部署端口**（如6080）
* **备注**（可选，如"分公司"，不可超过60个字符数）

3.点击【保存】即可完成配置 。

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01Spcs16qcicxHP2L0viabZ3GDKre7KWNHAKzRHVKxlnh9vzBEDNS41mvM0QyaPUjDibqKoduIHKV5icA3uriaNuBh73qG8GibnR30oyVI/640?wx_fmt=gif&from=appmsg)

**配置生效机制**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SoDzib3gAicWJzsAyZLcgT6T0jP56tia0aB2pVibLky70fEDnomThV3bBFn3xI22qgRQOJcUZIibFB7dW3vVBmI2HmBDbfrrDazgn80/640?wx_fmt=gif&from=appmsg)

* 配置成功后，客户端会在**一个心跳时间内**同步该设置，并将地址写入客户端注册表 。
* 之后当终端连不上当前中心时，会自动尝试连接所添加的中心地址；成功连接新中心后，会同步该中心的策略继续接受管控 。

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01Spcs16qcicxHP2L0viabZ3GDKre7KWNHAKzRHVKxlnh9vzBEDNS41mvM0QyaPUjDibqKoduIHKV5icA3uriaNuBh73qG8GibnR30oyVI/640?wx_fmt=gif&from=appmsg)

**建议**

![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01SoDzib3gAicWJzsAyZLcgT6T0jP56tia0aB2pVibLky70fEDnomThV3bBFn3xI22qgRQOJcUZIibFB7dW3vVBmI2HmBDbfrrDazgn80/640?wx_fmt=gif&from=appmsg)

有分支机构的企业建议提前在【中心地址管理】中添加分公司控制中心的地址与端口，以保障员工跨地点办公时终端持续受控。

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过