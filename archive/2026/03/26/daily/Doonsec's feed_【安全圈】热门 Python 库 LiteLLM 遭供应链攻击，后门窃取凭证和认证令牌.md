---
title: 【安全圈】热门 Python 库 LiteLLM 遭供应链攻击，后门窃取凭证和认证令牌
url: https://mp.weixin.qq.com/s/bfMK16gq5lOXpv9k1_QeQQ
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:48.299537
---

# 【安全圈】热门 Python 库 LiteLLM 遭供应链攻击，后门窃取凭证和认证令牌

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHicjUv2e3OR6ECV2GCow3hlpicSVtk5unjyuuia7EvMPPSCwvOWRHk3pNiadRBRkib6DlicuiahMMdJ29LiaDibOLT5TF0icdhGULNxHRCM/0?wx_fmt=jpeg)

# 【安全圈】热门 Python 库 LiteLLM 遭供应链攻击，后门窃取凭证和认证令牌

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

LLM攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyEYYnjCIdicZo6NONCQUib1yhjyph458dx3iaoe7K7WLVO9zevLKribTPVhCOqn6HGzVibtKR8KVCGDyL3GBaur448FyKgDVWiaGPuOU/640?wx_fmt=png&from=appmsg)

TeamPCP黑客组织持续发动供应链攻击，现已入侵广受欢迎的Python库”LiteLLM”，并声称在攻击期间从数十万台设备窃取数据。

LiteLLM是一款开源Python库，作为统一API网关对接多个大语言模型（LLM）提供商。该包极为热门，日均下载量超340万次，过去一个月下载量超9500万次。

据Endor Labs研究，**威胁行为体入侵该项目后，今日向PyPI发布了LiteLLM 1.82.7和1.82.8的恶意版本，部署信息窃取程序收集各类敏感数据。**

**此次攻击由TeamPCP认领，该组织此前高调入侵了Aqua Security的Trivy漏洞扫描器。**那次入侵引发连锁反应，波及Aqua Security Docker镜像、Checkmarx KICS项目，如今又轮到LiteLLM。

该组织还被发现利用恶意脚本攻击Kubernetes集群——当检测到伊朗配置的系统时擦除所有机器，在其他地区设备上则安装新型CanisterWorm后门。

消息人士告诉BleepingComputer，数据外泄数量约50万条，其中大量为重复记录。VX-Underground报告的”感染设备”数量相近。但BleepingComputer未能独立核实这些数字。

**LiteLLM供应链攻击详情**

Endor Labs报告称，威胁行为体今日推送了两个恶意版本，均在包导入时执行隐藏载荷。

恶意代码以base64编码形式注入’litellm/proxy/proxy\_server.py’文件，模块导入时即解码执行。1.82.8版本更进一步，向Python环境安装名为’litellm\_init.pth’的.pth文件。由于Python解释器启动时会自动处理所有.pth文件，即使不专门使用LiteLLM，恶意代码也会在Python运行时执行。

执行后，载荷最终部署”TeamPCP Cloud Stealer”变种及持久化脚本。BleepingComputer分析显示，该载荷与Trivy供应链攻击中使用的凭证窃取逻辑几乎相同。

Endor Labs解释：”载荷触发后执行三阶段攻击：收集凭证（SSH密钥、云令牌、Kubernetes密钥、加密钱包和.env文件），尝试通过向每个节点部署特权Pod在Kubernetes集群内横向移动，并安装持久化systemd后门以轮询额外二进制文件。外泄数据经加密后发送至攻击者控制的域名。”

**窃取范围**

该窃取程序收集广泛的凭证和认证密钥，包括：

* 系统侦察：运行hostname、pwd、whoami、uname -a、ip addr、printenv命令
* SSH密钥和配置文件
* AWS、GCP、Azure云凭证
* Kubernetes服务账户令牌和集群密钥
* .env等环境文件
* 数据库凭证和配置文件
* TLS私钥和CI/CD密钥
* 加密货币钱包数据

云窃取载荷还包含额外的base64编码脚本，伪装为”System Telemetry Service”安装为systemd用户服务，定期连接checkmarx[.]zone远程服务器下载执行额外载荷。

窃取数据打包为名为tpcp.tar.gz的加密档案，发送至攻击者控制的infrastructure models.litellm[.]cloud。

如怀疑已遭入侵，应将受影响系统上的所有凭证视为已暴露并立即轮换。

BleepingComputer多次报道过因企业未及时轮换先前泄露中发现的凭证、密钥和认证令牌而引发的入侵事件。研究人员和威胁行为体均告诉BleepingComputer，虽然轮换密钥困难，但这是防止连锁供应链攻击的最佳手段之一。

***END***

阅读推荐

[【安全圈】上海警方深入推进“涉企网络谣言”打击整治：处置 270 余个违规账号，AI 洗稿编造车企销量下滑等行为被严惩](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=1&sn=13b358d9c7991bf709ee2d720e484439&scene=21#wechat_redirect)

[【安全圈】AI 圈地震：月安装量约 9500 万次的 API 网关 LiteLLM 遭投毒](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=2&sn=7ea915e24da062e25443aebe478f6c60&scene=21#wechat_redirect)

[【安全圈】HackerOne 披露员工数据泄露事件：第三方服务商 Navia 遭入侵](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=3&sn=81030c6344d3eb99b31a0593ace75849&scene=21#wechat_redirect)

[【安全圈】马自达通报安全事件：员工和合作伙伴数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075041&idx=1&sn=ae9e793a53a8639e64c1a2ab362f1677&scene=21#wechat_redirect)

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