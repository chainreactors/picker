---
title: 【安全圈】飞牛 fnOS 漏洞被批量利用
url: https://mp.weixin.qq.com/s/G4IxQITuWEKoyry7fBOiXw
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:10.372789
---

# 【安全圈】飞牛 fnOS 漏洞被批量利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGhaia4kBCtgbSbnSgGichw1VdfZDhXhwADmF30QVvaOgH11qrqiccOMIKegYicROQ5dCcdDgyAdPuibDGOrKa35tCcRSGnicQUGr3KA/0?wx_fmt=jpeg)

# 【安全圈】飞牛 fnOS 漏洞被批量利用

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyEHjicOfF9mccer1tLWaBvx9QOrRuTUjK1sJTrHibp67iazN7bMKE1QicS5OEoQeT38T9QWx1EJ2PRejtVyKTFn9icwQEY6Co7efEXw/640?wx_fmt=png&from=appmsg)

2026 年 2 月，运行飞牛私有云系统 fnOS 的 NAS 设备被大规模卷入 Netdragon 僵尸网络。攻击者利用长期未彻底封堵的越权访问、路径穿越与验证绕过漏洞，将原本用于家庭和中小企业数据存储的设备，转化为分布式拒绝服务攻击的基础设施。从样本分析与 C2 侧遥测数据来看，感染规模在 1 月底已扩展至约 1500 台节点，峰值同时在线超过 1100 台，且感染对象高度集中于飞牛设备，未见其他厂商大规模波及。这起事件的严重性不仅在于漏洞本身，更在于恶意程序所展现出的成熟持久化与对抗能力。

攻击链条的第一步，是在公网暴露的设备上建立 HTTP 后门。早期样本监听 57132 端口，通过对 `/api` 路径构造特定 GET 请求即可远程执行系统命令。研究人员通过该后门的流量指纹与资产测绘数据比对，确认大量 IP 存在一致行为特征。后续变种则将后门端口迁移至 57199，并更新 C2 基础设施，以规避已有检测规则。

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyGLbmibhic1JW3hn6QfZFeWy2ZtibEaMia5npju70eU5JNtuyiaPMMptTicvEcHvFXia5ibM2TbJFCh0MN6uKRO7495CnOy1JJdck4PykQ/640?wx_fmt=png&from=appmsg)

在成功植入后，Netdragon 首先进行“环境清洗”。加载器会批量删除 `/var/log/*.log`、`/var/log/messages*`、`/var/log/audit/audit.log*` 以及 systemd 日志，抹除入侵和横向行为痕迹。同时篡改 `/etc/hosts`，将官方更新域名如 `apiv2-liveupdate.fnnas.com` 指向 0.0.0.0，切断固件更新与安全补丁通道。它还会终止 `sysrestore_service`、`backup_service` 等恢复相关服务，并删除升级与还原组件，使在线修复与回滚几乎失效。

持久化机制体现出明显的双层设计。用户态层面，恶意程序向 `system_startup.sh` 追加启动命令，从攻击者控制的 IP 下载并执行二阶段载荷，在 `/sbin/gots`、`/usr/bin/<botid>` 等路径下部署副本，并注册 systemd 服务实现自启动。内核态层面，则加载伪装模块（例如 `async_memcpys.ko`），形成重启后依旧存活的内核级落脚点。后续版本还新增伪装为 `/etc/systemd/system/dockers.service` 的服务，用于刷新持久化与对抗清理脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyFasiamK5CWj0td9YJuiaf5NIZDW6QyibiarJlice795IInb7ETNRRRicRfcNMMfv29kmibTTzzvmAXCMR8RHlE9r2WYFsacRDicEruj7Y/640?wx_fmt=png&from=appmsg)

样本内部采用硬编码密钥与 nonce 解密字符串表，其中包含 “PWNED FROM NETDRAG” 标记、C2 域名如 `aura.kabot[.]icu` 以及一系列系统路径。通信层使用自定义二进制协议，支持登录、心跳、命令执行与 DDoS 指令等多种帧类型。会话密钥通过分层 XOR 与 ChaCha20 保护，分别使用不同 nonce 处理双向流量，并在握手阶段完成身份校验。C2 地址随机选择，常见于 45.95.*.* 网段或相关域名，端口包括 3489、5098、6608、7489 等。

在接收到 DDoS 指令后，Bot 进程会进一步压制本地可观测性，例如重命名 `/usr/bin/cat`，终止 `network_service` 与 `resmon_service` 等监控组件，使管理员难以及时察觉异常流量。遥测数据显示，攻击指令可通过 Telegram Bot 与 HTTP API 下发，目标覆盖中国、美国、新加坡、澳大利亚等多个国家的 IT 服务、制造业及公共管理机构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyG3lsOaLibUK01vJNwicwgBLCHic4Eu40IomeTWT7mWOGnPk9eju67jlNoAzHzyosCl7fqhxia6mGDWUm1LEiaaIoFNJicj7VGVf5y6Q/640?wx_fmt=png&from=appmsg)

随着防御方发布检测规则与清理脚本，攻击者迅速迭代。1 月 31 日的新构建版本会自动删除标记为 “C2IP” 的 iptables 与 nftables 规则，恢复与控制端的外联能力；DDoS 模块采用 ChaCha20 加密字符串与配置；并引入动态 8 字节密钥封装机制，提升静态分析难度。2 月 1 日，C2 下发指令要求所有 Bot 删除 `rsa_private_key.pem` 文件，这一行为可能破坏设备加密服务或恢复机制，显著增加数据丢失风险。

部分受害用户反馈，感染设备无法完成固件升级或运行官方安全工具，长期处于“半失控”状态并持续参与僵尸网络。结合漏洞存在时间、感染规模与对抗强度来看，这已不再是单点入侵，而是一次典型的物联网基础设施劫持事件。

从厂商层面来看，飞牛在 2 月 12 日发布了《近期安全事件的完整说明与深刻反思》，承认漏洞属于基础安全缺陷，并披露了修复版本发布、关闭未升级设备中转服务、强化默认配置、引入 SDL 流程与定期审计等整改措施。声明中强调“先修复、后通告”的决策是出于风险控制考虑，同时表示将建立漏洞分级响应与高危漏洞 24 小时内通告机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGfYxWaKaiaqhON3rhnNib630eGv6m07iaulPBDgdFX1OKpYB6AEJ8XKugPMcX1mMkJnqpBUv8UCsHYC469RLzjmqp3ibVs8ia7Ra6s/640?wx_fmt=png&from=appmsg)

但从安全治理角度审视，本次事件暴露出的问题不只是某几个漏洞，而是安全基建与响应机制的系统性缺失。漏洞在较早版本中已存在，论坛亦曾出现相关反馈，却未被识别为高风险问题；攻击发生后，用户在一段时间内未获得充分预警；感染规模、数据外泄情况与溯源细节仍缺乏透明数据支撑。对于存储大量私密数据的 NAS 产品而言，安全能力应当优先于功能迭代，这是基本共识。

我们的态度很明确：一方面，应客观看待厂商在事件发生后的修复与整改动作，推动其落实公开承诺；另一方面，也必须坚持透明、可验证的安全披露原则。感染规模、数据外传评估、攻击溯源进展以及长期审计结果，都应以技术报告形式持续公开，而非止步于公关层面的反思。

只有建立清晰的漏洞分级、强制代码审计、默认最小暴露策略以及离线应急修复能力，类似事件才可能真正画上句号。否则，随着攻击工具链不断演化，Netdragon 这样的僵尸网络仍会把每一台疏于防护的设备，变成下一个攻击节点。

***END***

阅读推荐

[【安全圈】“本地回环”成突破口：Clawdbot 默认配置漏洞导致上千实例暴露公网](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=1&sn=9b1a9c993553c060ba4ff0723b80d66f&scene=21#wechat_redirect)

[【安全圈】7zip.com 并非官方：钓鱼站分发恶意程序](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=2&sn=9be4e7b66acf43666e3f3384a184941e&scene=21#wechat_redirect)

[【安全圈】Apple 紧急修复在野零日漏洞：dyld 组件被用于“高度复杂”定向攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=3&sn=56d3b7691413517a4c4f08c06962d8c9&scene=21#wechat_redirect)

[【安全圈】UEFI 安全启动证书 2026 年 6 月到期，微软已启动轮替更新](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074123&idx=4&sn=46229fdaa0f74e089f4e426e295916b2&scene=21#wechat_redirect)

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