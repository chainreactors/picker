---
title: 新固件才把 root 交出去：拆 Enphase 光伏网关认证注入
url: https://mp.weixin.qq.com/s/-C0IwEqLgy3T6ltQAWq-nw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:33.015067
---

# 新固件才把 root 交出去：拆 Enphase 光伏网关认证注入

# 新固件才把 root 交出去：拆 Enphase 光伏网关认证注入

原创

黑卷
黑卷

黑卷的IoT攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

美国光伏厂商 Enphase 的 IQ Gateway，是屋顶微型逆变器跟云端之间的那台数据采集网关。2026 年 8 月 7 日，研究者 Joseph Charles（j027）公开了一条他在自家设备上走通的链：新固件里的 API Key 认证把用户输入拼进了 shell，未登录就能执行命令；再叠上没被彻底拿掉的公式口令，以及一条给客服用的未认证重启，就能拿到 root SSH。

官方通告是 ENSA-2026-1，发布于 2026 年 5 月 20 日。影响版本写的是 IQ Gateway 8.2.4264 到 8.3.5171，CVSS 3 打了 9.8，CVE 当时还在等待分配。修复版本是 8.3.5562 或更新。通告里点名致谢了 Joseph Charles，并明确建议：这台网关本来就不必直接暴露在公网。

![Enphase 官方 IQ Gateway（ENV-IQ-AM1-240）产品图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84X9NIMbz65VV5o3ohdblBa1l1Y7VyrpKp7iaibyaibPlkaZzLuiaUYUoXxiaEBOPYlBLdRbvKmlicjXXQOItALTS0HA7pYiaqQ2DAA3aQ/640?from=appmsg)

![一张图看完：新固件引入未认证命令执行，再拼上旧口令和未认证重启就能进 root](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84VH53hUQTs3bXFUiaMgNo8ia2TPA9FNdEIBkcuJCuMUWPJTqp9Z4f3bMVfiapIKxlIGlnjB6L466jfrl0TwwX51fS12k4102Qicr5Y/640?from=appmsg)

## 一、这块 4GB 的 eMMC，已经写了 32TB

故事的起点不是挖洞，是自家网关先坏了。设备还在网上，本地接口却没了响应，手机 App 显示离线，机身上四盏灯一起闪红。重启没用，找厂商支持之后走了换货。

研究者后来拿到安装商权限，才把旧机换下来。换之前他在自己这套系统上请厂商侧重启过一次，第二天数据又开始上报，但掉线那一段时间的历史记录没了。之后这台旧机还是会自己掉线，先是夜里一两个小时，后来白天也不稳定，直到换上新机才恢复正常。

他想搞清楚根因，免得新机再走同一条路。按社区里已经公开过的方法进入系统之后，他去看 eMMC 健康状态，数字很直白：这块 4GB 的颗粒已经经历了大约 8000 次擦写，折合写入量大约 32TB。他想换一颗更高耐久的同规格芯片，找不到；转头看见板上有 USB 口，这才动了把高频写入挪出去的念头。

![示意：IQ Gateway 夹在微型逆变器与 Enphase 云之间，经电力线通信采集每块板的数据](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84Xm0KkK44Psvia7QDuNCdr9WXKA0bicRd2GKGdjkajJGgibwicXOO69gYicY2nBD9sPxzLDRc7cPmwcic4wtg6Paygxuic1RRBLdmsbiaY/640?from=appmsg)

![关键数字：4GB eMMC 约 8000 次擦写，折合写入约 32TB](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84XcXoSEy2XVA2E10uZuiaGYbYzd6n4LJyN35HbLApkpErkaTVicKIKSpF6ib5UHw1Cb3OCggE7eBM7DBSRYL9suXh7mP4I3CibVx7Q/640?from=appmsg)

## 二、新固件里，认证手续自己把壳打开了

换货来的新机带着较旧的固件，上面有一些已知问题。他并不想为了做实验再把正在发电的新机重装一遍，于是把目光转到最新固件：安装商 App 里能拿到加密镜像，设备上的 eecrypt 放到 QEMU 里跑，镜像就能解开。

审计最新固件时，API Key 认证处理里出现了一处命令注入。用来校验密钥的步骤，会把用户送来的内容直接拼进一条计算 SHA-512 的 shell 命令。这条路径不必先登录，跑在 Web 服务进程里，子进程的身份是 nobody。也就是说，未认证的请求已经能够在设备上执行命令，只是此时还不是 root。

更值得注意的是时间线：这条未认证的命令执行，是新固件才引入的。旧版本反而没有这个入口。补丁叠上去之后，认证代码自己又开了一扇门。

![Enphase 官方 IQ Gateway 3 产品图，同属 IQ Gateway 产品线](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VowkSgrNuHhcickjd4qwsVR7EAyPpqYOV3smE8qoKGHxZQ6fSeFsHjUy6zAtnJz3S1ZXewEU20xYEYnKKiaxFvnYDk0mJf0Qpico/640?from=appmsg)

![示意：从安装商 App 取出加密镜像，用 eecrypt 在 QEMU 中解密后再做审计](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84Xxm4hFB2xfibibqmY52WVCWtEgCGdwxiavJPib5WiaHrSZgrTnf0fceOj3u2KPR9G37PlFTg4HvSic5pMPRT7XocuGayeR0BEgVQAVY/640?from=appmsg)

![示意：API Key 认证把外部输入拼进计算哈希的 shell，未登录即可在 nobody 身份下执行命令](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84WXibRQXsBIicNs1KAO3dhq6cpXoPVhBWBibz8ibbPJrA17oGkcJXlo58iaBiaeg6zx3cicfwlf8JePmfCByJsV9WBlYwEt5Y3CZE1bm4/640?from=appmsg)

## 三、门口要通行证，后院的进程却是 root

安装商用来排查电力线通信噪声的诊断接口，按设计需要安装商权限。但这层鉴权是在前面的 OpenResty / nginx 上做的。真正干活的 Ruby 后端以 root 运行。

有了前面那处未认证的命令执行，就可以绕过门口的登录，直接跟后端说话。后面两条问题——任意文件删除，以及一次不必登录的重启——因此也能被未认证的请求串起来。

![示意：鉴权在 OpenResty 门口，Ruby 后端以 root 运行，命令执行可绕过登录直达后院](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84XCtBEyshMe3nDO90SYpyOCCx0plibHtb51ugh3n75VrPhkLuVicQysglicXdeGJicib1iaM7757BHuoEAmTLQYZILDiaSYDqLTYoYC48/640?from=appmsg)

## 四、删掉两份配置，旧的公式口令又回来了

固件里有一份额外的 SSH 配置，专门用来关闭密码登录。注释写得很清楚：目的是禁用「可按规则推出来的公式口令」。这类问题早年以 CVE-2020-25754 被公开过。可研究者核对 PAM 之后发现，那套自定义模块还在，而且只挂在 SSH 上。密码登录一旦被重新打开，公式口令就又可用。根因并没有被拿干净。

主机防火墙默认只对所连网络放行 Web 端口。SSH 和其他端口，本来打算只走客服隧道。客服可以让网关去连 VPN，再凭他们自己的密钥登进去。

诊断接口里有一项「删除选中的抓包文件」。后端把用户给出的名字拼在抓包目录后面，再执行删除。写文件的路径有穿越防护，删除这条没有。后端以 root 跑，于是可以删到这份关闭密码登录的配置，也可以删掉防火墙的启动脚本。

改完还需要一次重启才会生效。测试时他只能拉过电闸，随后找到一条给客服调试用的、不必登录的重启入口。这次重启会让设备进入一种故障调试状态，一部分常规服务不再拉起，但 SSH 还在——它本来就是留给客服把机器救回来的。于是前面的删除生效，密码登录和 SSH 端口重新可用，公式口令也能对上 root。

如果这台 IQ Gateway 被直接放到公网，或者攻击者已经在同一局域网里，整条链不需要再借助别的条件。

![示意：关闭密码登录只是多了一份配置，PAM 里的公式口令模块还在](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84UXKDiaPtRNTV2MtYQIuwYmwScYnxibVJQR6b4yxlPzoLgo2foXYFwta9AiaxJCiagrfzSyQ2Dj6O87P3Or5icHMk0efraInXl5GQGk/640?from=appmsg)

![示意：删除接口未防路径穿越，可拿掉 SSH 覆盖配置和防火墙脚本](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84XjaLJUhpYeMLDWYw7ZhLDUiaCa66FYyg99sILFrJGiczhLnZobYT7axK88WGbichrZBwnct4Y4gcfnnRPcqz7NUed1eIJnxSmUIc/640?from=appmsg)

![示意：未认证命令执行、直达后端删除、未认证重启，三步之后回到 root SSH](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84WeDecT7UtTrh8Iyj3BJfahzeznxSOnlG1QdNavzsCbq5LyRlDaILunsUUvJ9Gmh5DCmsIQLJcNGIotjdoJpnjEqYLpx3ANpec/640?from=appmsg)

## 五、公网上能搜到，补丁却没有按期铺完

多数家庭会把网关放在路由器后面，并不直接暴露。研究者在等待协调披露时，用 Shodan 搜索 `enphase-envoy`，还是看到当时有一千多台出现在公网。相对厂商宣传的百万级安装量，这只是一小部分，但已经足够拿来观察升级节奏。

当时至少有 400 台处于「整条链都可以走通」的版本。他认为路径穿越和未认证重启的影响面更宽，几乎覆盖各版本固件；整链之所以只是子集，正是因为那处命令注入只存在于较新的版本。

厂商通过 CERT/CC 的 VINCE 渠道协调，并曾表示会在披露日 2026 年 5 月 21 日之前把设备全部打上补丁。研究者按版本号跟踪公网样本，发现节奏跟不上这份表态。他还能看到，承担升级脚本分发的 Apache 在放量时被请求打满——这台服务器本身也已经十年未升级。加速推送时，升级流程要去同一台服务器拉一份 Ruby 脚本，并发一高就撑不住。撰写原文时，公网上仍有可走整链的设备，只是比高峰时少。他建议厂商通知那些把网关直接放到公网的用户，但没有得到回应。

官方通告对这条注入的修复口径很明确：升到 8.3.5562 或更新，并且不要把网关暴露到公网。2026 年 9 月 1 日，研究者又看了安装商 App 里当时的最新固件：未认证的命令执行和未认证重启已经修好；路径穿越还在，意味着有安装商权限的人仍可删除任意文件；同一套 PAM 公式口令也还在。注入补上了，后院里的旧问题并没有一起收干净。

![示意：研究当时公网暴露超 1000 台，其中至少 400 台处于整链可打的版本](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84XjHuyUvyZPQOYNic9M8W9g29WAxjjmI9YpibSPbNkAI8pnQPBmVEb1OJn6bLeC96gPm1mJ9bBIYNGOywKEBmZwP5nmJxrciaca8s/640?from=appmsg)

![官方通告 ENSA-2026-1：CVSS 9.8，影响 8.2.4264 至 8.3.5171，修复为 8.3.5562 或更新](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84V87yK7TPqSwICl1yDibD8BCskESHn8FkvHyhCiacbb91jgj7qYwrKg7SapSwG3WeOVF6DUOibsv8QDiaUQnaib67qHpibaeQS3mGibyI/640?from=appmsg)

![2026 年 9 月 1 日复核：注入和未认证重启已修，路径穿越与公式口令仍在](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84UxczvwT7yq6kU3mSLwkNBedlbicrGs2yApqlGz3vFibtWzdUpsM4u9EqDyiciaeDh4U6kRn5CaibTnedIgGEMPicKay2ebIqzKfU8bI/640?from=appmsg)

## 六、屋顶上的网关，先别直接对着公网

对已经装了 IQ Gateway 的业主和安装商，公开资料里能立刻做的几件事并不复杂。

把网关放在路由器后面，不要给它公网地址，并限制对管理口的 HTTP / HTTPS 访问。这是厂商通告里的缓解措施，也是这类采集器的常见部署方式。尽快确认嵌入式软件已经升到 8.3.5562 或更新。管理接口不要放到访客网络。路径穿越和公式口令如果仍留在当前版本里，就应当把安装商权限和 SSH 暴露面一并收紧，不要默认认为「认证注入修了就等于 root 链断了」。

![业主与安装商可立即执行的加固清单](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84Xica2w4gasVGXDtWOBMDQKRibicmzlIg4VVDvmWQMhEKicBRrBiaNpiaEmabhhqll3x2YVZEgxs2PRUic9ZNVSvPRXSRyJibNCyx4gVgY/640?from=appmsg)

黑卷点评

这条链最别扭的地方，不是「光伏网关也能进 root」，而是洞出在新固件的认证代码里。旧的公式口令问题已经被讨论过一轮，厂商的修法却是再盖一份关闭密码登录的配置，PAM 模块还留着。新版本为了算一条哈希，又把外部输入送进了 shell。门修了一半，锁却装到了门框外面。

披露过程里，厂商先说过已经修好，后来的推送节奏又对不上自己定的截止日期，承担升级脚本的服务器在放量时直接被打满。通告只覆盖了未认证命令执行这一层；到 9 月初，删除接口和公式口令仍被研究者看到还在。打补丁不是把一条通告贴出去就结束。该核对的是：当前版本号、网关有没有被直接放到公网、安装商接口还能否删到系统文件、SSH 密码登录是不是又被那份覆盖配置单独扛着。

屋顶上的采集器一旦被拿到最高权限，看到的不只是发电曲线，还有这户的用电和网络位置。先把设备从公网收回来，再确认固件已经跟上官方修复版本，比事后再追日志更要紧。

![黑卷点评：新固件把门开在认证里，旧口令还留在 PAM 上](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84WxAMjeRyrr6g2CZibGEO7KrYq2yLYtLHGuIiawaiauFZnReHJYQBJNrTpiblJfVO89qHHkweESsLSNrD0AqnNkD69IDo0OniaOncc0/640?from=appmsg)

---

⚠️ **免责声明**
 本人所有文章均为技术分享，均用于防御为目的的记录，请勿用于其他用途，否则后果自负。

🛰️ 星球「黑卷的IoT攻防日记」

* 🔥 每天一篇一线漏洞拆解与复现思路
* 🚗 整车实测 20+、IoT 组件 100+
* 📚 车联网 / V2X / 固件逆向 资料库
* ⚡ 星球里提问，24 小时内必答

![星球「黑卷的IoT攻防日记」](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84WTHNgwVP7vqWjicjm4YnrsrgpTrRy9tnaB2IEhUrP8TLW4Q7qMH1yKeJQBzR7qKZowZ6S16zorDvexUgpicTAav3tcia41NDDFYA/640?from=appmsg)

**往期推荐**

* [鉴权算法可离线算：拆 Trane Tracer SC+ 到 root SSH](https://mp.weixin.qq.com/s?__biz=Mzg5MjY0MzU0Nw==&mid=2247486905&idx=1&sn=d0bb07a6870e20a94b8e63672a9d9625&scene=21#wechat_redirect)
* [从调试口抽到改固件：Sonoff ZigBee 网关的芯片到云端两条 CVE](https://mp.weixin.qq.com/s?__biz=Mzg5MjY0MzU0Nw==&mid=2247486121&idx=1&sn=fa00d6550883f102a66c5308fc9197e8&scene=21#wechat_redirect)
* [EOL 路由照样打穿：Netgear WGR614v9 UART + Bitdefender Box SPI 降级 RCE](https://mp.weixin.qq.com/s?__biz=Mzg5MjY0MzU0Nw==&mid=2247485429&idx=1&sn=5a4cdfd6982657765522258b8310892d&scene=21#wechat_redirect)
* [嫌我不配坐超跑？最后车主亲自递钥匙｜第03集](https://mp.weixin.qq.com/s?__biz=Mzg5MjY0MzU0Nw==&mid=2247486892&idx=1&sn=b65fe7abf239e42c3914139d20db195a&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84U36giciazNDB6JcNOyOCiculsulnuSgJMLiaGLmb0JRFlsbATVibtic0zhk2luY1tUia6ibMkaCvMPWMqzfI0ibKKicbFXFIciazZibqJTY08/0?wx_fmt=png)

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
...