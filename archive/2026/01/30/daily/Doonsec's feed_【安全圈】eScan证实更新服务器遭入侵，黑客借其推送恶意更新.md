---
title: 【安全圈】eScan证实更新服务器遭入侵，黑客借其推送恶意更新
url: https://mp.weixin.qq.com/s/9DvzxG2fwRMwJuZsCfFnnw
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:02:28.742691
---

# 【安全圈】eScan证实更新服务器遭入侵，黑客借其推送恶意更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48bLwTRicbyHoRpPsicO5TvEaIV4ZyGIqdLjh5EnXuHYQIC5ImbIcqH1xg/0?wx_fmt=jpeg)

# 【安全圈】eScan证实更新服务器遭入侵，黑客借其推送恶意更新

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48GK3kicKpWXk9uZGqgRmLTUnn18PiayPj6dbbJr8HmuTbbwJjEgDpcslA/640?wx_fmt=jpeg&from=appmsg)

eScan 杀毒软件开发商**微世界科技（MicroWorld Technologies）** 已正式证实，其旗下一台更新服务器本月初遭黑客入侵，黑客利用该服务器向一小部分用户推送了未经授权的更新程序，后续分析证实该程序为恶意文件。

2026 年 1 月 20 日，在长达两小时的时间窗口内，从该区域更新服务器集群下载更新的用户均收到了这一恶意文件。

eScan 方面表示，涉事的服务器基础设施已完成隔离与重建，相关身份认证凭证也已完成更换，同时已为受影响用户提供了对应的安全修复方案。

安全厂商**Morphisec**也单独发布了一份技术报告，分析了在客户终端监测到的恶意活动，该机构确认这些活动与同一时间段内从 eScan 更新服务器推送的更新程序直接相关。

Morphisec 称其于 2026 年 1 月 20 日检测到相关恶意活动，随后联系了 eScan。但微世界科技向科技媒体 BleepingComputer 表示，该公司对 Morphisec 宣称**自身为首个发现并上报该事件**的说法存在异议。

eScan 方面给出的说法是，公司已于 1 月 20 日通过系统监控和用户反馈内部发现了该问题，并在数小时内完成了涉事基础设施的隔离，且于 1 月 21 日发布了安全预警公告。eScan 还指出，Morphisec 是在公开发布该事件相关声明后，才联系了公司。

对于 “受影响用户对该事件毫不知情” 的说法，eScan 同样予以否认，称其在安全修复方案敲定期间，已主动向受影响用户发送通知并进行了一对一沟通。

### 更新服务器遭非法入侵

eScan 在其安全预警公告中将该事件定性为**更新基础设施访问入侵事件**，表示黑客通过非法访问某区域更新服务器的配置信息，在更新分发路径中植入了未经授权的文件。

微世界科技向 BleepingComputer 提供的公告中写道：“黑客非法访问了我们某台区域更新服务器的配置，导致一个异常文件（补丁配置二进制文件 / 恶意损坏更新包）被植入更新分发路径。”

“2026 年 1 月 20 日的特定时间段内，从该受影响服务器集群下载更新的用户，均接收到了该文件。”

该公司强调，此次事件**并非因 eScan 杀毒软件自身存在漏洞**所致。

eScan 还明确，仅有从该特定区域服务器集群完成软件更新的用户受到影响，其余所有用户均未波及。

不过 eScan 表示，安装了该恶意更新程序的用户，其设备可能出现以下异常现象：

* 更新服务故障提示
* 系统 hosts 文件被篡改，导致无法连接 eScan 更新服务器
* eScan 更新配置文件被修改
* 无法接收新的病毒库安全定义更新
* 客户端设备弹出更新服务不可用的提示窗口

BleepingComputer 已向 eScan 进一步求证其服务器最初遭入侵的具体时间，若收到回复将第一时间更新相关报道。

### 恶意更新被用于投放恶意软件

Morphisec 在其安全公告中指出，此次黑客推送的恶意更新程序，植入了经篡改的 eScan 更新组件**Reload.exe**。

该公告中写道：“黑客通过 eScan 合法的更新基础设施分发恶意更新程序，导致全球范围内的企业和个人终端设备均被植入了多阶段恶意软件。”

尽管这一经篡改的 Reload.exe 文件，表面上带有看似属于 eScan 的代码签名证书，但 Windows 系统和病毒检测平台 VirusTotal 均判定该签名**无效**。

Morphisec 表示，这款恶意 Reload.exe 文件（可在 VirusTotal 查询）被黑客用于实现**恶意程序持久化驻留**、执行恶意命令、篡改 Windows HOSTS 文件以阻止设备进行远程更新，同时连接黑客的**命令与控制（C2）服务器**，下载更多恶意载荷。

研究人员公布了监测到的以下黑客命令与控制服务器地址：

hxxps [://] vhs [.] delrosal [.] net/i

hxxps [://] tumama [.] hns [.] to

hxxps [://] blackice [.] sol-domain [.] org

hxxps[://]codegiant [.] io/dd/dd/dd [.] git/download/main/middleware [.] ts

504e1a42.host.njalla [.] net

185.241.208 [.] 115

研究人员发现，黑客最终向受感染设备投放的恶意载荷为一个名为**CONSCTLX.exe**的文件（可在 VirusTotal 查询），Morphisec 确认该文件是一款**后门程序**，同时具备持久化下载恶意文件的功能。该机构还表示，这些恶意文件会创建计划任务以实现持久化驻留，任务名称伪装为**CorelDefrag**等正常名称。

目前 eScan 已推出一款修复性更新程序，用户运行后可自动完成以下操作：

1. 自动识别并修正被篡改的系统配置
2. 恢复 eScan 更新服务的正常功能
3. 验证系统是否成功恢复
4. 操作完成后需重启系统（常规重启即可）

eScan 与 Morphisec 均建议用户，为提升设备安全性，**屏蔽上述所有黑客命令与控制服务器地址**。

值得注意的是，2024 年曾有相关监测显示，朝鲜黑客组织曾利用 eScan 杀毒软件的更新机制，在企业网络中植入后门程序。

***END***

阅读推荐

[【安全圈】抖音崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=1&sn=b745a686b245684c9bdd345d1b77afb8&scene=21#wechat_redirect)

[【安全圈】恶意 VS Code 扩展"ClawdBot Agent"伪装AI助手传播木马](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=2&sn=3ed01239d8e66b938f373a2a52c32bc0&scene=21#wechat_redirect)

[【安全圈】PyTorch "安全"模式被严重RCE漏洞攻破，可执行任意代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=3&sn=ad2665e9be5ec05d1f5f1bcdabcfa2d4&scene=21#wechat_redirect)

[【安全圈】Chrome 发布安全更新，修复后台 Fetch API 漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=4&sn=cc70511df2d49f4ff6dd41538bf3b02a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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