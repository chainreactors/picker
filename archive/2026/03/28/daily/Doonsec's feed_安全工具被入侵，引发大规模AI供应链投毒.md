---
title: 安全工具被入侵，引发大规模AI供应链投毒
url: https://mp.weixin.qq.com/s/71IFxRId7Or_CkoxcaB5hg
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:39:20.603769
---

# 安全工具被入侵，引发大规模AI供应链投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HqolA1dQic6ibwzHuyS50BQvRyz6RG0BngkmZropoOe097skbJMxdtfnfmK8zHr1SwX1iay9UZwgyibmTISYu4yc735nxyOP5EuM1rsJ3QMQIgU/0?wx_fmt=jpeg)

# 安全工具被入侵，引发大规模AI供应链投毒

微步情报局
微步情报局

HACK之道

![]()

在小说阅读器中沉浸阅读

3月24日，微步情报局监测到AI核心组件LiteLLM遭遇大规模供应链投毒，PyPI仓库1.82.7和1.82.8两个版本包含攻击者植入的后门。

尽管46分钟恶意版本就被移除，但鉴于其单日300万+次、单月近亿次的下载量，仍对下游数千个AI项目造成极大影响。公开报道显示，攻击者TeamPCP声称已窃取数十万台设备的数据。此次事件基本脉络如下（UTC时间）：

* 2月底——攻击者入侵开源漏扫工具Trivy，植入恶意代码
* 3月中上旬——LiteLLM CI/CD流水线使用恶意Trivy版本，致使PyPI凭证失窃
* 3月24日10:39——攻击者利用PyPI凭证，上传完成两个包含后门的LiteLLM版本
* 3月24日11:25——恶意版本1.82.7和1.82.8被官方移除，存活46分钟

经过进一步研判，恶意代码主要在Linux平台运行，Windows几乎不受影响。

**一、概述**

|  |  |
| --- | --- |
| 事件概述 | LiteLLM供应链投毒，窃取凭证等高价值数据 |
| 涉及产品 | LiteLLM（月下载量约9700万次） |
| 影响版本 | 1.82.7 和 1.82.8，已被移除，安全版本为 1.82.6 |
| 发现时间 | 2026年3月24日（UTC时间10:39 - 11:25） |
| 攻击者 | 黑客组织 TeamPCP |
| 事件根因 | LiteLLM的CI/CD流水线使用了已被入侵的Trivy工具，导致发布权限泄露 |
| 事件危害 | SSH密钥、云服务凭据（AWS/GCP/Azure）、Kubernetes机密、CI/CD令牌、加密钱包等被窃取 |

**二、供应链分析**

# litellm供应链投毒主要影响1.82.7和1.82.8两个版本。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEPKuKXou9y3XjFVheFuGodwSNoGovIzaHVxqM416JnrL7Zm4ncaRiabE5qqQhmJBQd9lYmcuv0icsqqibG5x9gQhFXOqL3ibC7QdsA/640?wx_fmt=png#imgIndex=0)

在1.82.7版本中，恶意攻击者将一段base64编码后的恶意代码加入到proxy\proxy\_server.py文件中，一旦导入litellm项目中的proxy库，便启动执行该恶意代码。在proxy\_server.py文件中存在三个版本，后面两个被注释的恶意编码经过分析后，与非注释恶意编码功能及通信完全相同，只是在加密方式上略有差异。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEPaWicz2fC4e64OMQeOhX9piavPAibytm0vlL5BbfxzN4uRqZ0RHia2CdicQZpxcvDsG2iaPy6to6LvEibTsJNicXpCCHS4JQzlxgllZ2M/640?wx_fmt=png&from=appmsg#imgIndex=1)

在1.82.8版本中，不但包含这种恶意代码注入，还增加了恶意的litellm\_init.pth，利用 .pth文件在python运行时启动的特性进行隐匿执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdENuictqlpusctTlRJhgsSTdKv8kpCH7u1MLT4icVrsGhCGiabRBpNYIgvRl6cmtG5J2cg0ZfjIkicUPsyuZhUZibCbtxmLSnh2pE1Q0/640?wx_fmt=png#imgIndex=2)

经过代码对比，.pth文件中的恶意编码与proxy\_server.py文件的非注释的恶意编码完全一致，因此主要分析以.pth文件中的恶意编码为主。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEN4SFG0uzwYT5ibTa4z3LE0dnFVbI8WyD2fxbEl0DnibNdZ3gcLsT0HQE8YkZwAicXZBovyQMufia8u4oaEoPKssssWdFysjCEgSpE/640?wx_fmt=png&from=appmsg#imgIndex=3)

恶意编码比较简单，首先会从失陷主机窃取大量敏感数据信息，然后下载持久化脚本维持持久化，然后上传打包的敏感信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEOwC6G78YFujRkkfqULyl7u6N7yMyLvy8py6xiaarWc0KqO5iaXk85hKee83TNYOshfOKt79j1Ql3Kvq538ohZiat5YxOia7l3N3qQ/640?wx_fmt=png#imgIndex=4)

值得注意的是，恶意攻击者将路径设置为Linux常用目录，并未针对Windows。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEMojfuzMa4z5vnLpiaNGkWpWlfDr8AfiaVEPkGl3gvDicA6BmhyXEFBhmHzPbrqjTDkJ3oNNRG5yWrWVnZia3bqyoNrXwOKicC16wFs/640?wx_fmt=png#imgIndex=5)

获取系统信息、printenv环境变量、SSH密钥、Git凭证。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMHIGYldBFwiatRoQZxc59ofGhiaT9zibDEjqB8Gwe1T75Mokia6m38xNaoy9JibTibvmqUibzLXHQUpiaKbngd2weYO3Bcl0hZG0qgFaI/640?wx_fmt=png#imgIndex=6)

获取AWS凭证、GCP凭证、Azure凭据、Kubernetes密钥、GCP凭证、Azure凭据。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMZwicMHJZ4jDXNXIcv06v0PibJ7n7dQRxf25ic21qV51wZ4afDTUWjtScjmXP2z1tHkjqjbZfdwd2AiaQ4GT57QP12tuibQlT12LH0/640?wx_fmt=png#imgIndex=7)

获取Docker配置信息、常见包管理、WireGuard key、CI/CD 密钥、数据库凭证。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOlQibAJl5VwWu2UXPlOJMiaegAIdM7domldUbHfOTsT1YZEQC3LhqHCKHRKU2xWYiaBIazM3gn6HVqDjBPZHNOfibXMfhDajPiaxCI/640?wx_fmt=png#imgIndex=8)

获取Shell历史记录、加密钱包、CI/CD 密钥和Webhook信息。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMOvcB4sia7CfhXZPBTbptQL6QjKhibiczkwyVb2DauUNnWzVPpRs3Qhx26iaXDjoWaSkGpq7q9qic12libXD2fl4nlDkRw73eDOtn98/640?wx_fmt=png#imgIndex=9)

通过通信获取AWS凭证等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPfuic6S4Rz3eb1n48UrTzgiaiahLzzicrCECWSV7mG92Bnv0Qka5ib7dk8WxOfarX6gnDsCHE6ueHm8lYkyZK6bKMdYlF7Fic90tS1U/640?wx_fmt=png#imgIndex=10)

使用kubernetes节点下载恶意脚本保存为sysmon.py。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPS7OggxbUv0DR8yk194ibBaGJ95nhrGl6rq07pqxYTkQ6ibd6nqsKmcCJaIP1kJX0HPdyV0WDAlPhrAuaZNgu4seEMCpL0ACM2Q/640?wx_fmt=png#imgIndex=11)

恶意脚本解码如下，主要访问checkmarx.zone/raw下载文件，读取其中的链接来执行二阶段脚本下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEM1ibaLD2ftu57lVwqe1rHJRmZbyRaNhrhhspUaRes0icpd0OibYL7LYxY8zHx1iaRFJvLej523vFO1O3LkCAK7X9BRsAa1bn81azY/640?wx_fmt=png#imgIndex=12)

但是当前链接已被恶意攻击者导向非恶意网站，无法继续执行下载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPfLkL7q88lc5oXwUMLV9UFK85uYdY6sVWiaoJhVFMWuOibuaB82vAFM0cagCIVrmPTVicLgyFicWDnIDoBUsVFicLwVu14qcy6w2Lo/640?wx_fmt=png#imgIndex=13)

后续会设置增加sysmon.service来持久化运行下载到的脚本，该脚本保存为/host/root/.config/sysmon/sysmon.py

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMH5DDmlxOzAaBMcEEoazFQATmK5IIPEbPkwQwMBL02wJ7F6zklSe055jgpwJ6lXRrFruownUMUNgiciaSythl6X4FenuhpTnLnQ/640?wx_fmt=png#imgIndex=14)

在收集大量敏感信息后写入临时文件后，加密打包生成tpcp.tar.gz文件，然后上传到models.litellm.cloud，官方网站为litellm.ai。可以看出攻击者特地申请相似域名来进行指向性投毒，这种相似域名避免引起流量关注。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdENVD1aTxHULEAvfNpmNmiczg5KsJc3g95FXoia7mnph8tY4OP8YqVP3YCtUsMnqFicsoZWNePoOtTFCctHofID56BLyHNPEUlvIfc/640?wx_fmt=png#imgIndex=15)

其中对数据进行加密的公钥在三个版本一直没有改变。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdENyu2I76D5sEVOwKLEXwc3wwaGXNicEj3iazicgJk3U5LNxDDnxicrUOVGYVbdicDIbhs0iaHewdEIzqIbykaWP0805jtt04Siano3Xj8/640?wx_fmt=png#imgIndex=16)

另外在前两个版本中使用了RC4来加密执行脚本，其中的密钥内容为nigger，说明攻击者带有一定的黑人歧视倾向，可能与种族主义有关。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEPddX3D41TuSgrrk1NWfQkOywQ6q3mbFxdVRGEJNzczrJpDLxoa7Jiblkmf8Cz8TC2EebnEpibY049cfeZks6SsyrdGtP0icDFRhM/640?wx_fmt=png#imgIndex=17)

**三、排查方式**

1.重点在linux环境下通过python命令(pip show litellm)，排查是否安装litellm的1.82.7/1.82.投毒版本,若显示版本为这两种，立即停止该服务并卸载以及对失陷机器进行断网处理。

2.针对网络通信部分，拦截models.litellm.cloud以及checkmarx.zone的域名通信。

3.排查是否存在/tmp/pglog或者/tmp/.pg\_state以及/host/root/.config/sysmon/sysmon.py和tpcp.tar.gz文件以及其他python库中与litellm\_init.pth的sha256一致的pth文件，如果存在，则删除该文件。另外排查是否新增非工作相关的sysmon.service，如果有，则删除该服务。

4.建议交给专业人员进行分析失陷机器是否存在其他未知风险。

**四、检测方案**

微步终端安全管理平台OneSEC已支持对恶意代码的精确检测，建议受影响用户及时关注数据外传和敏感文件访问等终端日志。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOxJbxUmc8pmp0Tn9WagJXdIKdd4E8zVP7MibxYTMBB6CagpUvwSBMwU0RKiadfdvAeaLK63pvwzwY34ydEMAN5ibu2V1yMqUHpbw/640?wx_fmt=png#imgIndex=18)

此外，微威胁感知平台TDP、威胁防御系统OneSIG、互联网安全接入平台OneDNS、云沙箱S、沙箱分析平台OneSandbox等，均支持对相关IOC的检测与拦截。

**五、IOC**

|  |  |
| --- | --- |
| IOC | 说明 |
| d2a0d5f564628773b6af7b9c11f6b86531a875bd2d186d7081ab62748a800ebb | litellm-1.82.8.whl |
| 71e35aef03099cd1f2d6446734273025a163597de93912df321ef118bf135238 | litellm\_init.pth |
| a0d229be8efcb2f9135e2ad55ba275b76ddcfeb55fa4370e0a522a5bdee0120b | proxy\_server.py |
| 8395c3268d5c5dbae1c7c6d4bb3c318c752ba4608cfcd90eb97ffb94a910eac2 | litellm-1.82.7.whl |
| models.litellm.cloud | 敏感信息上传 |
| checkmarx.zone | 下载持久化脚本 |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

HACK之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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