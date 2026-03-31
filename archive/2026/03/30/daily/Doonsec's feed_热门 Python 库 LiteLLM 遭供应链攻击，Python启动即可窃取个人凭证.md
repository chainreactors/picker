---
title: 热门 Python 库 LiteLLM 遭供应链攻击，Python启动即可窃取个人凭证
url: https://mp.weixin.qq.com/s/7kLZyE1gqsfaodRgRhiofQ
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:20.795893
---

# 热门 Python 库 LiteLLM 遭供应链攻击，Python启动即可窃取个人凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KZCmibwhia3VV1UzDLic2okJos0LlObCU6GtuwgibE7g18wIKPj6IkEGXrGgDNibibhQFEVic7vvoFvBtZKibWsuUVKRfVFw4uDekYgMibPb5wXcClKY/0?wx_fmt=jpeg)

# 热门 Python 库 LiteLLM 遭供应链攻击，Python启动即可窃取个人凭证

SecHub网络安全社区

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png)

**免责声明**

本文发布的工具和脚本，仅用作测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关内容。

文中所涉及的技术、思路及工具等相关知识仅供安全为目的的学习使用，任何人不得将其应用于非法用途及盈利等目的，间接使用文章中的任何工具、思路及技术，我方对于由此引起的法律后果概不负责。

## 🌟简介

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KZCmibwhia3VXaK008fKShVIY4aSxtO9AhcguMsbVSkZibbaEugYOd65bCnGUdswiaMoBr3xv8A708vlncOmAicBm0PXx46cMaFjEtDfJ45OyGcc/640?wx_fmt=png&from=appmsg)

    TeamPCP黑客组织持续发动供应链攻击，现已入侵广受欢迎的Python库”LiteLLM”，并声称在攻击期间从数十万台设备窃取数据。

    LiteLLM是一款开源Python库，作为统一API网关对接多个大语言模型（LLM）提供商。该包极为热门，日均下载量超340万次，过去一个月下载量超9500万次。

    黑客入侵该项目后，向PyPI发布了LiteLLM 1.82.7和1.82.8的恶意版本，部署信息窃取程序收集各类敏感数据。

影响版本

# 所有<2026.1.29的版本

# 详情     两个恶意版本，均在包导入时执行隐藏载荷。     恶意代码以base64编码形式注入’litellm/proxy/proxy\_server.py’文件，模块导入时即解码执行。1.82.8版本更进一步，向Python环境安装名为’litellm\_init.pth’的.pth文件。由于Python解释器启动时会自动处理所有.pth文件，即使不专门使用LiteLLM，恶意代码也会在Python运行时执行。     执行后，载荷最终部署”TeamPCP Cloud Stealer”变种及持久化脚本。     载荷触发后执行三阶段攻击：收集凭证（SSH密钥、云令牌、Kubernetes密钥、加密钱包和.env文件），尝试通过向每个节点部署特权Pod在Kubernetes集群内横向移动，并安装持久化systemd后门以轮询额外二进制文件。外泄数据经加密后发送至攻击者控制的域名。 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/KZCmibwhia3VWcGOPgQpRJBcCsUEokia4ica3jcZAMO6YpmHKWv8CzLBgHM6YnNOzWDq61VNIicV0lc6KhqkibpbEXiaTBGlXJB2PBewib6Y6mbs3ibI/640?wx_fmt=png&from=appmsg) **窃取范围** 该窃取程序收集广泛的凭证和认证密钥，包括： * 系统侦察：运行hostname、pwd、whoami、uname -a、ip addr、printenv命令 * SSH密钥和配置文件 * AWS、GCP、Azure云凭证 * Kubernetes服务账户令牌和集群密钥 * .env等环境文件 * 数据库凭证和配置文件 * TLS私钥和CI/CD密钥 * 加密货币钱包数据     云窃取载荷还包含额外的base64编码脚本，伪装为”System Telemetry Service”安装为systemd用户服务，定期连接checkmarx[.]zone远程服务器下载执行额外载荷。 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/KZCmibwhia3VURV4PaMpqVofWGW2j0hDTibWWkN2icDLTctJxicjnJ7aXz4ISZRMsFAWkHafRs9sncUbrDicEkvGC5gC3gNNzrS05o5WiaZ40FBomU/640?wx_fmt=png&from=appmsg)     窃取数据打包为名为tpcp.tar.gz的加密档案，发送至攻击者控制的infrastructure models.litellm[.]cloud。 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/KZCmibwhia3VWyjnvuY6GQRJmd2Ff7tcrZS93czDnsTa75ic5wrGSdOJ5uXykEboMSv44nM2RuxC8deDw2GOojxnEIhkAj8BPwot4jic9Rs045o/640?wx_fmt=png&from=appmsg)     如怀疑已遭入侵，应将受影响系统上的所有凭证视为已暴露并立即轮换。 处置措施 这两个恶意 LiteLLM 版本已从 PyPI 中移除，目前 1.82.6 版本是最新干净的发布版本。 使用 LiteLLM 的组织强烈建议立即： * 检查是否存在 1.82.7 或 1.82.8 版本的安装 * 立即旋转所有在受影响设备上使用或在代码中发现的秘密、令牌和凭证。 * 搜索持久化组件，例如'~/.config/sysmon/sysmon.py'及相关 systemd 服务 * 检查系统中是否存在可疑文件，如'/tmp/pglog'和'/tmp/.pg\_state' * 审查 Kubernetes 集群中'kube-system'命名空间中的未授权 Pod * 监控出站流量至已知攻击者域名 如果怀疑系统被入侵，所有受影响系统上的凭证都应被视为泄露并立即轮换。

欢迎关注SecHub网络安全社区，SecHub网络安全社区目前邀请式注册，邀请码获取见公众号菜单【邀请码】

**#**

**企业简介**

**赛克艾威 - **网络安全解决方案提供商****

       北京赛克艾威科技有限公司（简称：赛克艾威），成立于2016年9月，提供全面的安全解决方案和专业的技术服务，帮助客户保护数字资产和网络环境的安全。

安全评估|渗透测试|漏洞扫描|安全巡检

代码审计|钓鱼演练|应急响应|安全运维

重大时刻安保|企业安全培训

![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png)

**联系方式**

电话｜010-86460828

官网｜https://sechub.com.cn

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FW5uwU0BZtn2lmMrLPwpibCeCVbtBFDRkbFb7n7ibhPRxg20spUo9mUIiakmRYABB88Idl81IpGuXfw/640?wx_fmt=gif)

**关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwyhlWCYDVqK38BA5dbjKkH7icWmAew7SYRA7ao1bFibialrMvmQ9ib0TBvw/640?wx_fmt=jpeg)

**公众号：**sechub安全

**哔哩号：**SecHub官方账号

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrtCeJIgBibXtegO5DsycA9TJ6R1iaRJKJjOIphJ6SPVk3HII9J7hoqfX87zIWMEs4adzGvg3qLMicJw/0?wx_fmt=png)

SecHub网络安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrtCeJIgBibXtegO5DsycA9TJ6R1iaRJKJjOIphJ6SPVk3HII9J7hoqfX87zIWMEs4adzGvg3qLMicJw/0?wx_fmt=png)

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