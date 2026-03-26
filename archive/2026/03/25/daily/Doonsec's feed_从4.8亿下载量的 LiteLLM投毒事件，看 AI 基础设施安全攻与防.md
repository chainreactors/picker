---
title: 从4.8亿下载量的 LiteLLM投毒事件，看 AI 基础设施安全攻与防
url: https://mp.weixin.qq.com/s/ENu39ZiSnfFaLOdIyW2MhQ
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:46.146057
---

# 从4.8亿下载量的 LiteLLM投毒事件，看 AI 基础设施安全攻与防

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9icASLQUQzvYib5MJnSskooBuCGnxQwiccicn7V1StLeO18AYZYN1KicefuUqAqAqs0yzFgzyJlIExQocicBO6GFG3CGhBV78ZrB0tbCXeakdeUS8/0?wx_fmt=jpeg)

# 从4.8亿下载量的 LiteLLM投毒事件，看 AI 基础设施安全攻与防

原创

朱雀实验室
朱雀实验室

腾讯安全应急响应中心

![]()

在小说阅读器中沉浸阅读

近日，知名大模型网关工具 LiteLLM 遭遇供应链投毒，其 1.82.7和1.82.8 版本被植入恶意代码。由于该项目月下载量极高(近1亿月下载量)，且被 DSPy 等众多主流 AI 框架作为底层依赖，此次事件波及范围极广。Andrej Karpathy 也在 X 平台上发帖提示了该漏洞的严重性，甚至用”软件恐怖事件“来形容。

    目前，朱雀实验室开源的 AI 基础设施安全检测工具 A.I.G(AI Infra Guard)已经支持一键安全检测。

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvaY5BSkMKMK1Pz5UnPNCmlK83TdIu69kqASUG0fGlsGlibKreoyG6UDXPrbPBankuOicHVicyzMTiaNJUTfSfiae6a6AibdDGMibM3s5s/640?wx_fmt=png&from=appmsg)

事件：LiteLLM 投毒始末

**第一步：暗度陈仓（攻破上游工具）**

**攻击者首先入侵了LiteLLM的 CI/CD 流水线中依赖的容器漏洞扫描器 Trivy。通过感染安全工具来获取信任，这是典型的上游供应链打击。**

第二步：窃取密钥（获取发版权限）

被篡改的 Trivy 在流水线中暗中提取了存储在环境变量里的 PYPI\_PUBLISH 令牌，从而掌握了向官方仓库发布新包的最高权限。

第三步：投递毒药（发布恶意包）

利用窃取到的令牌，攻击者堂而皇之地向 PyPI 发布了植入恶意文件（litellm\_init.pth）的 1.82.7 和 1.82.8 版本。

第四步：静默触发（利用 .pth 自动执行）

这是整个攻击中最狡猾的一环。Python 的 site 模块在解释器启动时，会自动执行目录下的 .pth 文件。这意味着受害者根本不需要在代码里写 import litellm，只要安装了该包，任何 Python 进程的启动都会瞬间唤醒恶意载荷。

然后，当开发者执行pip install litellm或 pip install dspy 时，恶意代码会被同步下载到本地。该恶意代码的主要行为是窃取本地敏感信息，包括 SSH 密钥、AWS/GCP 云端凭证、Kubernetes 配置以及加密钱包等，并将其发送至攻击者的远程服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvYvrkZTSA1RCLshFEhImMGUhPo9bjAPMZ90iaUSGtKdMk6oKUibdlOMRWKFewWjWpfS7SakZB21xzaH0FLkwyHU7YaKUmJkiah07s/640?wx_fmt=png&from=appmsg)

卡帕西大神对此攻击事件的评价是:恐怖的供应链攻击事件

由于现代软件工程高度依赖第三方包，LiteLLM 作为基础组件，其受污染会导致所有依赖它的上层应用自动中招。这种供应链攻击大幅增加了排查的难度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvaT0KM9UXrHltVu1O6265FugP5bzI3UWYCg0c170Sxm6MXxABnyQtgw2M8XyV9WqbDeLuVpfiaia73bwRosD4ibIqgicKbf9Ba5u7g/640?wx_fmt=png&from=appmsg)

LiteLLM维护者也在Hackernews社区道歉，并表示受影响的版本（v1.82.7、v1.82.8）已从 PyPI 中删除。所有维护者账户均已更改。所有 GitHub、Docker、Circle CI 和 pip 的密钥均已删除。（看起来维护者本人的账号和各种身份凭据也被黑客恶意接管了）

**影响路径：三阶段递进攻击**

恶意代码一旦被触发，将自动在后台静默执行以下三个阶段的攻击：

**1.敏感资产全面收集**

恶意脚本会深度扫描并窃取主机上的核心凭证与配置文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvbNWP6tluSAFIwicJ9RbSAykq0wzljyHGmChcAibRqYibY0fVkFPMwAX3yoWfYTnJ5mlCuTOiaibhZWqn1M9ibrq8Nibuw5G621CUDhE8/640?wx_fmt=png&from=appmsg)

解密后的攻击代码，主要窃取以下目标

● SSH 私钥及配置、.gitconfig、Shell 历史记录。

● .env 文件、数据库密码、加密钱包文件。

● 云服务凭证（AWS/GCP/Azure）及 K8s 配置文件。

● 主动导出系统环境变量，并查询云端元数据接口（如 IMDS、容器凭证）。

**2.加密并泄露这些凭证**

为对抗网络流量审计，窃取的数据会被多重加密：

使用 AES-256-CBC（随机会话密钥）与硬编码的 4096 位 RSA 公钥对数据进行加密并打包为 tar 文件。

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvYyvp2uTdgz3gn5OlNlWbgFqTlnRGFckP9xYTgOCxIab0MQewv5Aibs9ic3W706pylKhuxfeWWynFOawLyj0eerGibjia3qSuiakqmM/640?wx_fmt=png&from=appmsg)

● 最终通过 POST 请求，将数据包发送至攻击者控制的伪造域名（ https://models.litellm [.]cloud/，该域名伪造成官方基础设施，实际是攻击者持有的域名）。

### 3. 横向移动与持久化驻留

攻击者不仅窃取数据，还会试图长期控制基础设施：

● K8s 集群渗透：若环境中存在 K8s 服务账户 Token，恶意软件将跨命名空间读取所有集群 Secret，并尝试在 kube-system 的所有节点上创建特权容器（alpine:latest）。该容器会挂载宿主机目录，并在 /root/.config/sysmon/sysmon.py 植入 systemd 级别的后门。

● 本地机器驻留：在普通受感染设备上，恶意脚本会自动写入~/.config/sysmon/sysmon.py，建立持久化访问权限。

**受影响群体及范围**

本次攻击的破坏模型是二元的：只要在漏洞窗口期安装了 1.82.7 或 1.82.8 版本，该设备上的所有敏感凭证即被视为已全部泄露。

以下环节极易受到影响：

● LLM 代理服务端：将 LiteLLM 作为 OpenAI、Anthropic 等多模型路由网关的生产环境。

● CI/CD 流水线：在受影响期间执行过 pip install litellm 的 Docker 构建、GitHub Actions 或 GitLab CI 任务。

● 开发者本地环境：通过 pip 或 uv 拉取到受感染版本的开发机。

● 下游依赖项目：任何将 LiteLLM 声明为依赖，并在构建时拉取了该版本的第三方软件包。

**风险排查与自查清单**

无论当前是否直接使用 LiteLLM，建议立即执行以下自查步骤。

**1.检查环境感染情况**

在终端运行以下命令，确认是否中招：

```
# 检查当前安装的 LiteLLM 版本pip show litellm 2>/dev/null | grep Version
```

```
# 全局查找是否存在恶意的 .pth 触发文件find $(python3 -c "import site; print(site.getsitepackages()[0])") \-name "litellm_init.pth" 2>/dev/null
```

```
# 检查项目依赖配置文件历史grep -r "litellm" requirements*.txt pyproject.toml setup.py Pipfile 2>/dev/null
```

判定标准：如果发现 litellm\_init.pth 文件，或确认曾安装过 1.82.7 / 1.82.8 版本，必须假设系统已被全面渗透，请立即执行下一步骤。

使用朱雀实验室开源的A.I.G  https://github.com/tencent/AI-Infra-Guard  也可以一键检测：

![](https://mmbiz.qpic.cn/mmbiz_png/9icASLQUQzvad8ialqrTanBQzLLnamn7A6rQuUPcPFeV8PbCBvM1tN7AukELJtmmpYhiaDiap08xUklJzmAibibeRBq8V5lVAkJlp41iboCfX6AQ4U/640?wx_fmt=png&from=appmsg)

**2.凭证全面更换（按风险降序）**

一旦确认受影响，建议立刻更换以下所有密钥与凭证，建议严格按照以下高风险优先的顺序执行：

1.  云服务商凭证：AWS 访问密钥、GCP 服务账户、Azure 服务主体。

2.  包管理器令牌：PyPI、npm 及私有注册表 Token（防止攻击者以您的名义发布恶意包）。

3.  SSH 密钥：重新生成所有密钥对，并同步更新所有服务器的 authorized\_keys。

4.  数据库密码：特别是以环境变量形式存储的明文密码。

5.  API 密钥：所有大模型厂商 Key（OpenAI、Anthropic 等），以及 Stripe、Twilio 等第三方服务 Key。

6.  Kubernetes 配置：轮换所有 K8s Secrets 并重新部署服务。

7.  Git 凭证：重新生成 GitHub/GitLab 的个人访问令牌（PAT）。

**未来思考**

此次 LiteLLM 投毒事件揭示了 AI 基础设施领域一个日益严峻的趋势：隐藏在软件供应链深处的攻击正变得越来越频繁，且极具破坏力。

随着大模型应用的爆发，底层的网关工具、数据处理框架以及各类 AI 代理库已经成为整个技术栈的咽喉。这些基础组件不仅被成千上万的生产环境所依赖，而且通常掌握着极高的系统权限，频繁触碰核心 API 密钥、云端凭证甚至企业私有数据。对于攻击者而言，直接攻破目标企业的防御成本极高，而向这些被广泛使用的开源上游组件投毒，则能以极低的成本引发链式反应，实现大范围的隐蔽攻击。

可以预见，这种利用传递依赖进行的静默渗透，将成为未来网络攻击的核心手段之一。越是处于底层、被视为理所当然的基础设施，其一旦被攻破，所带来的系统性威胁就越是致命。

参考&引用：

1.  https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign

2.  https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/

3.  https://www.endorlabs.com/learn/teampcp-isnt-done

4.  https://github.com/BerriAI/litellm/issues/24518

5.  https://safedep.io/trivy-teampcp-supply-chain-compromise/

6.  https://x.com/karpathy/status/2036487306585268612

7.  https://github.com/tencent/AI-Infra-Guard

点击阅读原文，体验A.I.G一键安全检测

![](https://mmbiz.qpic.cn/mmbiz_gif/9icASLQUQzvZKtXfCibkUiaaVicUoq0eshVlicY3JUSMP3YUdPjoRR105B3TmZibTIPbVPzEO19YkIDpRIAyd4LorBzRcINF8L3wJOTy4uwNibqzI0/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

腾讯安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

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