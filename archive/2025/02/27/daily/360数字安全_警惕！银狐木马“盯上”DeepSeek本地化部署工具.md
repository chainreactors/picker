---
title: 警惕！银狐木马“盯上”DeepSeek本地化部署工具
url: https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247579696&idx=1&sn=ccb1ae52d4d3be31f969d5a2bb0de59b&chksm=9f8d2838a8faa12e0b1e4c3f995748f2dc140dfe191c6cdb07c5d2303f268a7767fe297a7514&scene=58&subscene=0#rd
source: 360数字安全
date: 2025-02-27
fetch_date: 2025-10-06T20:37:09.942954
---

# 警惕！银狐木马“盯上”DeepSeek本地化部署工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVVeP2yODicbsscKR0kebX0UlXc9VHTCqDtVBQiaaNniczYLlaGvPYPxp8g/0?wx_fmt=jpeg)

# 警惕！银狐木马“盯上”DeepSeek本地化部署工具

360数字安全

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

News Today

DeepSeek持续爆火，大量政府、企业和个人开发者纷纷选择进行本地化部署，以获得更好的使用效果，网上迅速涌现出众多与之相关的部署工具和下载资源，然而，攻击者也将矛头对准这一环节。

近期，360安全大模型监测到，通过仿冒DeepSeek进行的钓鱼攻击迅速增多，出现大量虚假本地部署工具，如DeepSeek电脑版、DeepSeek中文版等，诱骗不了解情况的用户充值购买。**在各种钓鱼攻击中，持续猖獗的银狐木马团伙也再次现身，360数字安全集团特别提醒广大用户，务必提高警惕，谨防上当受骗。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVzKicnR5aDfpZSLCCCbQabasEROpibiccHd6mtsNUtZliaRtAqBVYOpMuXw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqV8T1IdK5WD7O4MYX9nxicIpVCR0hZ58TOE4a9uZBSjQzyQ0kibaRAeSmw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVicswmRSwDvnppdkENiaRemuxEWVUJRdB4s5uZnH0ThlicLsrAaiazqt0IA/640?wx_fmt=gif&from=appmsg)

**“简单粗暴”，真实还原银狐攻击始末**

银狐木马主要通过钓鱼网页、即时通讯软件、下载站伪装成常用软件供用户下载等方式进行传播。它通常利用具有诱导性的文件名，如“成绩单”、“转账通知单”等，在QQ、微信等即时通信软件发送钓鱼文件或网站链接，诱导受害者点击。

面对DeepSeek近期的“泼天流量”，银狐木马团伙简单粗暴，直接对其他仿冒DeepSeek工具进行二次打包嵌入木马。或干脆“不装了”，银狐木马团伙利用“DeepSeek”关键词搭建各类钓鱼站点，直接在仿冒网站提供一个木马安装包，诱导用户下载虚假的DeepSeek安装包，最终在用户机器中植入银狐木马。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqV41UIvLaX1u6F1jU6HSAtGHEJXribc6icPEIsMIB9cPlOzZX1hyDKPKXw/640?wx_fmt=png&from=appmsg)

以上图这个银狐木马为例，该木马和过往的银狐木马在执行流程和功能上并未有太大区别。木马运行后会请求黑客服务器获取后续的配置文件，并通过解密配置文件获取其上线模块、杀软对抗模块、驻留模块等功能模块。下图展示木马请求黑客服务器后获取的配置文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVWQeIxZVwjziajCmUKCXVRyvWTPxZzFNCVa8CRXUIDfsGgQKbbzt7nPg/640?wx_fmt=png&from=appmsg)

获取配置后，银狐木马会检测系统中是否存在安全软件，若发现能影响其工作的安全软件，则调用杀软对抗模块与安全软件对抗，主要通过构造RPC数据包、以RPC管道方式创建计划任务绕过安全软件检测，计划任务执行的目标为可结束安全软件进程的合法驱动，即BYOVD。一旦计划任务创建成功，该驱动就会接收木马发出的指令，在环0层结束安全软件进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVb2K26cLqL3R8OHzAOfWBzzb8p2d74o4zZCn2E1zVNuIwZiauK7bdlBg/640?wx_fmt=png&from=appmsg)

成功结束安全软件后，“银狐“的上线模块和驻留模块开始工作。其上线模块是由Ghost木马改造而成的“银狐WinOS 4.0远控”，能实现包括键盘记录、屏幕监控、命令执行、语音监听在内的多种恶意操作。木马窃取用户的微信密钥与聊天记录、企业财税文件、企业工资单等企业财务相关内容，最终将这些信息售卖给诈骗团伙。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVib0FMNXSjX6wpuRH1s59NeG66ibQrbhPLomPGf5EYSicxyGKHukwPEHGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVicswmRSwDvnppdkENiaRemuxEWVUJRdB4s5uZnH0ThlicLsrAaiazqt0IA/640?wx_fmt=gif&from=appmsg)

**构建数字安全防御体系**

**360精准打击银狐威胁**

针对近期再次活跃的银狐木马攻击，360建议广大政企机构应尽快构建更加体系化、实战化、智能化的数字安全防御体系。

**基于多年攻防实战经验和能力，360推出基于安全大模型赋能的银狐病毒防护实战化解决方案**，将云化数据、探针、专家、平台和大模型能力开放给广大客户，构建了有效预警、全面防护、持续监测、智能处置的数字安全能力体系，实现了对入侵病毒的安全检测、安全分析、安全响应处置效率飙升，人效提升可达50%以上，安全运营各项指标效率提高100%以上。

这套方案主要是由360企业安全浏览器、360终端安全管理系统、360安全云组成：

**360企业安全浏览器**

**基于180亿+恶意网址数据库，每日拦截超过7.5亿个恶意网址。**360企业安全浏览器基于安全大模型的深度赋能，可实时通过云端不断更新的恶意网站数据库中查询，自动化判定登录网站是否为钓鱼网站、黑网址等威胁站点，对于银狐等持续变种性木马，及时警告用户访问的目标网站可能存在威胁，避免钓鱼、诈骗、财产损失等安全风险。

**360终端安全管理系统**

**四大立体引擎协作，再高级的变种也难逃法眼。**360终端安全管理系统，针对银狐木马等提供先进的防病毒功能，通过云查杀引擎、鲲鹏引擎、QVM人工智能引擎、QEX脚本检测引擎构建的多维智能检测体系，并配合主动防御，支持对蠕虫病毒、恶意软件、APT、广告软件、勒索软件、引导区病毒的检测查杀。

四大引擎实现后端病毒特征自动分析提取、抽取出病毒与恶意代码共性特征，建立恶意代码不同族系模型，同时，可将变种繁多的宏病毒置入模拟器执行，通过既定输出参数精确判断宏病毒后执行精确查杀。

**360安全云**

**终端安全专家托管服务，大模型赋能云化专家7\*24全天候守护终端安全。**依托超过3000名云化安全专家，提供7×24小时全天候监测、响应和处置服务，每天执行超过560亿+次的云端查杀操作，平均每秒查杀64.8+万次，每日拦截勒索攻击100万+次、挖矿攻击1000万+次、网络电信诈骗6000万+次，为客户终端设备提供有效的安全托管服务，助力客户能够快速发现异常，自动化响应处置。在帮助企业节省人力、资金的前提下，进一步提高安全水平，为银狐病毒防护建立安全屏障。

**IOC**

jdwr.ewdnw.cn

lkij.fiphi.cn

rtgd.gaegh.cn

jdwr.ofjulhz.cn

lkij.hckhxxl.cn

evgh.bgcwwa.cn

lkij.htsvl.cn

vien3h.oss-cn-beijing.aliyuncs.com

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU1icGxibkT5o65u4GaAz54uqVicswmRSwDvnppdkENiaRemuxEWVUJRdB4s5uZnH0ThlicLsrAaiazqt0IA/640?wx_fmt=gif&from=appmsg)

想要了解更多详情

欢迎拨打咨询电话

400-0309-360

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● 周鸿祎：360安全大模型将向“一带一路”友邻国家开放共享 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247577471&idx=1&sn=14be24acd47dba66bd105aa3790e5c53&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ● 满血守护DeepSeek，360率先推出DS大模型安全方案 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247579607&idx=1&sn=df88fe4a67db9d5ccc93fdb826d23d6b&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● 从《哪吒2》解码数字安全新范式：安全大模型重构防御体系 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247579545&idx=1&sn=c08fc0f07b8723bc5bb78c1f6e0c67a6&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 独家|360发布全球高级威胁研究报告：我国14大重点行业面临境外APT威胁 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247579509&idx=1&sn=0b56794720b224bd3af0dd6bead2f1e6&scene=21#wechat_redirect) | |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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