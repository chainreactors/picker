---
title: 瞄准即时通讯：DVRTC 漏洞实验室指南
url: https://mp.weixin.qq.com/s/3WcbmoScxykEVR-jj5VLsw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:25.267715
---

# 瞄准即时通讯：DVRTC 漏洞实验室指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibficPIOpys3EnbL2bmnSI3Jlv9Zbknic11MABsvdiaicospb5EnZHAd9UmFuGsxWGppvTjIzcOqPF3qYN5HYrIgMHZicQLqNm3tAyibY/0?wx_fmt=jpeg)

# 瞄准即时通讯：DVRTC 漏洞实验室指南

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> DVRTC是一个故意设置漏洞的VoIP和WebRTC实战演练平台，专为网络安全培训和研究设计。它打包了一套完整的脆弱系统、攻击场景手册和测试工具，让安全人员能在隔离环境中体验SIP、RTP、TURN等协议的多种攻击手法。

## 01 这是个什么东西？

DVRTC，全称Damn Vulnerable Real-Time Communications，简单来说就是一套“练靶场”。

它不是用来防御的，恰恰相反，它把VoIP和WebRTC通信里可能出的问题都攒到了一起，做成一个开箱即用的模拟环境。这样，安全研究员或者想学习攻防的人，就能在一个封闭、可控的系统里，放心大胆地搞破坏，而不用担心惹上麻烦。

> 玩之前，规矩先说好：**只能在完全隔离的专用机器上部署DVRTC。千万别把它和你正在工作的服务器、存着敏感数据的设备放一块儿。这玩意儿的设计初衷就是“不设防”，弱密码、暴露的服务、各种漏洞行为都是故意的。**

这套靶场不光给了你一个满是窟窿的系统，还配套了现成的攻击场景说明、实操练习和验证工具。你可以按照它的剧本走，一步一步发掘攻击路径，验证漏洞是否存在。虽然练习主要用靶场自带的测试工具，但你完全可以用自己喜欢的任何外部VoIP/RTC安全工具来打它。

## 02 现在能玩什么？

目前，这个项目里只有一个主线剧本，代号叫**pbx1**。

这个剧本里搭建的系统，用到的技术栈挺全乎，都是业内常见的组件：

* Kamailio（SIP代理服务器）
* Asterisk（开源PBX电话交换系统）
* rtpengine（媒体代理）
* coturn（TURN/STUN服务器）
* Nginx（Web服务器）
* MySQL（数据库）

它重点暴露的漏洞，涵盖了实时通信的好几个关键环节：

* SIP信令攻击：伪造、篡改呼叫控制消息。
* 摘要认证泄漏：搞到或者绕过SIP的认证信息。
* 弱密码和默认口令：猜密码这种初级但永恒的漏洞。
* RTP/媒体流滥用：劫持通话内容、发起媒体拒绝服务攻击。
* TURN中继滥用：滥用公共TURN服务器做攻击跳板或消耗资源。
* SIP相关的SQL注入和XSS：从Web管理界面找Web应用的常见漏洞。

这个pbx1剧本目前包含了7个有详细指导的练习，官方已经梳理出12条明确的攻击路径。更多细节和潜在的脆弱行为，都写在场景参考文档里，并且有自动化的回归测试来确保这些“漏洞”一直存在。

为了方便上手，项目直接提供了打包好的Docker镜像。你想自己从头编译也行，但用官方镜像最快。实在想体验又不想自己搭，他们还在公网上跑了一个实例：**pbx1.dvrtc.net**。不过依赖这个公共实例前，最好先看看它是不是还能正常访问。

## 03 怎么把它跑起来？

想自己在本地玩，先看看机器够不够格：

* Docker 20.10或更新版本。
* Docker Compose插件。
* 一个支持宿主机网络的Linux系统（macOS用户得用Colima方案，官方不主推直接用Docker Desktop on Mac/Windows）。
* 硬件建议：至少4核CPU，8GB内存，10GB硬盘空间。

满足条件后，开局几条命令：

./scripts/setup\_networking.sh
./scripts/generate\_passwords.sh
./scripts/init-selfsigned.sh
./scripts/validate\_env.sh
docker compose up -d

跑完，服务就该起来了。接下来就可以去`pbx1 Exercise Index`找练习开练。

不想用自签名的测试证书，想换成正经的Let's Encrypt证书也行。先在`.env`文件里设好`DOMAIN`和`EMAIL`，然后执行`./scripts/init-letsencrypt.sh`替换掉上面的自签名脚本步骤。

启动后怎么确认一切正常？可以看容器状态：

docker compose ps

也可以手动从宿主机访问一下Web页面（先加载环境变量）：

. ./.env
curl "http://${PUBLIC\_IPV4}/"

项目还提供了几个脚本帮你做完整性测试：

./scripts/testing-smoke.sh
./scripts/testing-run-all.sh
./scripts/attacker-run-all.sh

如果只是想快速感受一下SIP呼叫，找个SIP软电话（比如MicroSIP），注册分机号1000，密码1500，然后呼叫1200，应该能听到回声服务。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe4K4oAfiaB0460WdhiadpgeC6NGyWDOuHCaKkAlWM00K1ib7UCNdy5O89kWdwxs1bg8q0ARPEyosuB6DqpSRtu5Nib9ianYZbPlcgo/640?wx_fmt=png&from=appmsg)

## 04 该从哪里看起？

文档挺多，新手建议优先看这几个：

* **pbx1场景概览**

  ：这里有全部默认的账号密码、开放的端口列表、每个组件是干嘛的，以及攻击入口在哪。
* **pbx1练习索引**

  ：手把手的实战练习目录，从这里开始你的“破解”之旅。
* **故障排除**

  ：列了一些常见的启动失败问题和诊断方法。

## 05 这靶场到底怎么样？

说实话，DVRTC的出现，正好填了实时通信安全教学的一块空白。

以前学Web安全，有DVWA、WebGoat这些经典靶场。但VoIP、WebRTC这块，想要一个集成化的、带指导的漏洞环境，选择不多。DVRTC直接把一个接近真实PBX的复杂环境打包，让你能系统性学习，这点做得不错。

它的优点很明显：

* **真实性强**

  ：基于Asterisk、Kamailio等真实生产组件搭建，不是玩具。
* **开箱即用**

  ：Docker Compose一键部署，极大降低了搭建复杂环境的门槛。
* **引导性好**

  ：配套的场景、练习和测试工具，让自学路径很清晰。

当然，也有值得注意的地方：

* **场景单一**

  ：目前主要只有pbx1一个核心场景，花样还不够多。
* **复杂度较高**

  ：对于完全没接触过VoIP的新手来说，里面涉及的概念（SIP、RTP、TURN）比较多，可能需要额外补充基础知识。
* **许可证限制**

  ：采用了PolyForm非商业许可证，意味着你不能拿它去做商业用途的培训或产品。

如果你是一个对VoIP/WebRTC安全感兴趣的安全从业者、学生，或者公司内部想进行相关的安全演练，需要个现成的靶子，那DVRTC绝对值得一试。

它的灵感来源于那些经典的教学平台，但现在，它正在成为实时通信安全领域的“必修课实验室”。

项目是非商业许可，源码和文档都在GitHub上。关注实时通信安全的话，也可以看看他们官网的RTCSec月度通讯。

**获取方式：私信回复"DVRTC"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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