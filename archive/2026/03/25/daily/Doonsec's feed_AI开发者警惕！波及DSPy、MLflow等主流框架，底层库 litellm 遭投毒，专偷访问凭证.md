---
title: AI开发者警惕！波及DSPy、MLflow等主流框架，底层库 litellm 遭投毒，专偷访问凭证
url: https://mp.weixin.qq.com/s/8KYMylFNmMmPJK5ivd-kwA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:29:52.049162
---

# AI开发者警惕！波及DSPy、MLflow等主流框架，底层库 litellm 遭投毒，专偷访问凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dZ7ia5iaWFzz93dzpboubBgKOU8t0JJpNaySyTKTqt7tl2gG0LCiaUXbczicGTWr28h9Bbiagj06SmxvWc5Sv6bHlpNOsBRLMcBZaicDy1fQL2lQg/0?wx_fmt=jpeg)

# AI开发者警惕！波及DSPy、MLflow等主流框架，底层库 litellm 遭投毒，专偷访问凭证

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器中沉浸阅读

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg)

2026年3月24日，Python 生态中应用最广泛的大模型统一调用库 **litellm** 在 PyPI 平台遭到供应链投毒。安全社区将此次攻击归因于 TeamPCP 组织，该组织近期持续针对开源生态系统中的安全工具和 AI 基础设施发起攻击。

攻击者将含有恶意载荷的 **1.82.7** 和 **1.82.8** 两个版本上传至 PyPI，公开约三小时后被隔离下架，**最后安全版本为 1.82.6**。鉴于 litellm 日均下载量约 340 万次，且**作为 DSPy、MLflow、OpenHands、CrewAI 等主流 AI 框架的核心依赖，此次事件波及范围极广**。

**一、核心威胁：****底层 AI 支撑库源头投毒，常规防御失效**

攻击者利用被盗用的合法发布凭证，将含有恶意载荷的安装包直接上传至 PyPI 官方源，导致常规的 pip 哈希校验等安全防御彻底失效。成功投毒后，两个受感染版本在注入机制和触发方式上展现出了隐蔽的递进关系：

**litellm 1.82.7 版本：常规导入触发**

恶意代码以 Base64 编码形式嵌入在 litellm/proxy/proxy\_server.py 文件中（约第 128 行）。值得注意的是，官方 GitHub 仓库的源码中并不存在这段代码，说明恶意注入发生在 wheel 打包环节，攻击者借此绕过了常规的代码审查流程。触发机制上，只有当用户在代码中显式导入该模块时，恶意载荷才会被自动触发执行。

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz8ia86YknD87aXzkNoia9B3CofKGE72vh0ZaDicxZE5cAc2dSgRdjrUnv3HxEDQNKqPjskJWk99mibAmvgpXBpnFqaicM7V2prDh6JQ/640?wx_fmt=png&from=appmsg)

图1：proxy\_server.py恶意代码

**litellm 1.82.8 版本：“零点击”静默执行**

该版本的危险程度急剧上升。攻击者在 wheel 根目录额外植入了一个名为 litellm\_init.pth 的文件（大小约 34KB），且该文件在 RECORD 中被正确声明，能够完美通过哈希校验。触发机制上，由于 Python 的 site 模块在解释器初始化阶段会自动处理所有的 .pth 文件，这意味着**只要安装了该版本，任何启动 Python 解释器的行为：无论是运行 pip、执行 pytest、启动 Django 服务，还是运行 CI/CD 脚本都会静默触发恶意载荷，完全无需用户显式导入 litellm 代码。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz827tWkJIia6Pxm2VdHfyrnkLdEpnLSt0QRI5Sarmo3pJxsEGXicibukf7RKX3v8cWlibfoSC0VUTickUuuWgm3OmiaCtuftj1pl93Ko/640?wx_fmt=png&from=appmsg)

图2：litellm\_init.pth恶意代码

**二、攻击手段：****三阶段组合攻击，凭证窃取覆盖AI开发链全栈**

恶意载荷采用三重 Base64 嵌套混淆，执行三阶段攻击逻辑，实现了从凭证窃取到 Kubernetes 集群渗透，再到长期驻留的完整闭环。

**第一阶段：凭证大规模收割**。恶意代码对宿主机实施系统性扫描，将数据加密打包为 tpcp.tar.gz，通过 HTTPS POST 外传至 models[.]litellm[.]cloud（刻意模仿合法基础设施以迷惑响应人员）。

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz91uwsngp4QjjIL2c6wOCJQ7ayic7ibfttZrLyB7QYmkAnXfw7rUStgPupYNQJGfxib0Jcj7agWdaoBibXEJY9mSLDXUicKSibpHDQ3Q/640?wx_fmt=png&from=appmsg)

图3：凭证扫描窃取

**第二阶段：Kubernetes 横向移动。**若宿主机处于 K8s 环境且存在服务账户令牌，恶意代码将读取全集群所有命名空间的 Secrets，并在每个节点的 kube-system 命名空间部署特权 Pod（命名格式为 node-setup-\*），挂载宿主机根文件系统，实现全集群渗透。

**第三阶段：持久化后门植入。**恶意代码在 ~/.config/sysmon/sysmon.py 安装后门，注册伪装成 "System Telemetry Service" 的 systemd 服务。后门每隔约 50 分钟轮询 checkmarx[.]zone/raw 接口，等待攻击者的后续任意指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz8ObHO4viaz85cV4VGEzGdSJvfLg8lKrRfzQRIX5iap9blaJumljeaS8PqxUiaCibZM0pJKxXLoFT5DHocgnLwQVWyUeBP2JClRvrw/640?wx_fmt=png&from=appmsg)

图4：持久化后门

**三、影响范围：****覆盖AI框架生态全栈，凭证泄露风险涵盖云与K8s全域**

此次攻击收集的数据类型覆盖了信息安全全栈，恶意代码甚至内置了完整的 AWS SigV4 签名逻辑，凭证窃取能力远超常规信息窃取程序。一旦中招，以下资产面临极高的泄露风险：

* **云平台凭证：**AWS/GCP/Azure 凭证（含 IMDS 实例元数据、Secrets Manager 内容、SSM 参数）。
* **基础设施配置：**SSH 私钥与配置、Kubernetes 配置与全命名空间 Secrets、Docker 注册表凭证。
* **开发与数据资产：**数据库密码、CI/CD 配置（Terraform/GitLab CI/Jenkins）、TLS 私钥、.env 环境变量文件、Shell 历史记录。
* **加密货币：**比特币、以太坊、Solana、Cardano 等钱包文件。

**四、排查与清理指南：彻底清除驻留后门与残留文件**

请在所有相关环境（本地开发机、CI/CD Runner、Docker 容器、K8s Pod）中逐一执行以下排查与清理操作。适用系统：Linux / macOS。

1. 版本检测

检查当前安装版本：

```
pip show litellm | grep Version
```

如输出为 1.82.7 或 1.82.8，请先完成后续排查。

针对 1.82.8，额外检查 "零点击" 触发文件是否存在（有输出即说明已植入）：

```
find "$(python3 -c 'import site; print(site.getsitepackages()[0])')" -name "litellm_init.pth"
```

2. 深度自查（IoC 匹配）

检查 sysmon 后门与恶意服务：

```
ls -la ~/.config/sysmon/sysmon.pyls -la /root/.config/sysmon/sysmon.pysystemctl --user status sysmon.service
```

检查外传加密文件残留：

```
ls /tmp/pglog /tmp/.pg_state /tmp/tpcp.tar.gz /tmp/session.key /tmp/payload.enc 2>/dev/null
```

检查 Kubernetes 异常 Pod：

```
kubectl get pods -n kube-system | grep node-setup-
```

3. 阻断与清理

停止并移除持久化后门及残留文件：

```
systemctl --user stop sysmon.servicesystemctl --user disable sysmon.servicerm -f ~/.config/sysmon/sysmon.py ~/.config/systemd/user/sysmon.servicesystemctl --user daemon-reloadrm -f /tmp/pglog /tmp/.pg_state /tmp/tpcp.tar.gz /tmp/session.key /tmp/payload.enc /tmp/session.key.enc
```

在 K8s 集群中删除异常 Pod：

```
kubectl delete pods -n kube-system -l app=node-setup
```

卸载受感染版本，清空缓存并**重新安装****干净版本 (1.82.6)**：

```
pip uninstall litellm -ypip cache purgepip install "litellm<=1.82.6"如使用 uv 包管理器，请执行 rm -rf ~/.cache/uv 后重装
```

**五、应急处置：****防范后续渗透，轮换所有凭证**

如确认安装过受感染版本，立即采取以下措施：

* 轮换所有 SSH 私钥（并在 GitHub/GitLab 及服务器 authorized\_keys 中撤销旧公钥）。
* 轮换 AWS/GCP/Azure 访问密钥，并全面审计 Secrets Manager 及 SSM 参数的访问日志。
* 轮换 Kubernetes kubeconfig 及所有服务账户 Token。
* 重置 Docker 注册表凭证、数据库密码及所有 .env 文件中的 API 密钥（如 OpenAI/Anthropic 密钥）。
* 转移可能受影响的加密货币资产。

参考来源：

**Popular LiteLLM PyPI package backdoored to steal credentials, auth tokens**

https://www.bleepingcomputer.com/news/security/popular-litellm-pypi-package-compromised-in-teampcp-supply-chain-attack/

**TeamPCP Isn't Done: Threat Actor Behind Trivy and KICS Compromises Now Hits LiteLLM's 95 Million Monthly Downloads on PyPI**

https://www.endorlabs.com/learn/teampcp-isnt-done

**Three’s a Crowd: TeamPCP trojanizes LiteLLM in Continuation of Campaign**

https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign

**How a Poisoned Security Scanner Became the Key to Backdooring LiteLLM**

https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/

**Popular litellm Python package is the latest victim of TeamPCP's ongoing supply chain attack**

https://research.jfrog.com/post/litellm-compromised-teampcp/

**“洞”悉网络威胁，守护数字安全**

**关于我们**

360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

360漏洞研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

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