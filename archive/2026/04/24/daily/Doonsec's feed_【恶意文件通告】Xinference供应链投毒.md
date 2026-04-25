---
title: 【恶意文件通告】Xinference供应链投毒
url: https://mp.weixin.qq.com/s/i2MfYMhfNwm0NLfE9HMN9w
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:31:02.148984
---

# 【恶意文件通告】Xinference供应链投毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/APc6NwjLsxRZLTgjnLCPkJMRDNqE0ichVtsY0wpvFmD7MRZe73Q233Tc9yTGTdZ4iaV8opYTPqedSSesDDAENIniakNvpZOwSf8kicdxQSyy3lA/0?wx_fmt=jpeg)

# 【恶意文件通告】Xinference供应链投毒

深瞻情报实验室
深瞻情报实验室

深信服千里目安全技术中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSB3CQK3w29POH9Ggq7XQ1m82bAGmpYAYTq77KH1gQz7B3n0C8uO7lOrKnrbGReORRO8Gx87W3up4oYWSPyWiaVshJpo24qW2Wk/640?wx_fmt=gif&from=appmsg)

近期，深信服千里目安全技术中心监测到一起围绕Xinference开源推理框架的PyPI供应链投毒事件。根据xorbitsai/inference项目维护者于2026年4月22日在GitHub公开确认的信息，xinference的2.6.0、2.6.1、2.6.2版本已遭攻击者注入恶意代码并被紧急撤回，攻击起点并非仿冒包名，而是合法PyPI发布线被劫持，属于典型的合法软件供应链投毒事件。

**恶意文件概要**

|  |  |
| --- | --- |
| **事件名称** | 关于Xinference PyPI包的供应链投毒攻击 |
| **发布时间** | 2026年4月24日 |
| **威胁类型** | PyPI发布线劫持、合法包投毒、凭据窃取、AI推理基础设施攻击 |
| **简单描述** | 攻击者通过盗用的维护者/发布凭据向PyPI正式发布线推送xinference 2.6.0、2.6.1、2.6.2三个恶意版本，在xinference/\_\_init\_\_.py中嵌入双层Base64混淆载荷，在import或CLI/服务启动时后台派生子进程实施凭据窃取并外传至C2。 |
| **关键特征** | 合法发布线被劫持；恶意代码位于\_\_init\_\_.py导入即触发；双层Base64 + subprocess.Popen分离执行；重点收集SSH、云IAM、K8s、Docker、包管理器令牌、.env、数据库、TLS和加密钱包等凭据；打包为love.tar.gz经带自定义头X-QT-SR: 14的curl --data-binary外传至whereisitat.lucyatemysuperbox.space；样本含# hacked by teampcp标记，TeamPCP已公开否认负责。 |

**事件详述**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSN1XpibZbnkiaibwPHnE3nIIAG85UKjrWXU2rQwm9IhYNTJQHCfA5ckTkDXYcXbotLcQic74uAnQ8QScDI5iagjISuD5sE4FyS8J0I/640?wx_fmt=gif&from=appmsg)

**攻击背景与起因**

近期，深信服千里目安全技术中心监测到一起围绕Xinference开源推理框架的PyPI供应链投毒事件。

根据xorbitsai/inference项目维护者于2026年4月22日在GitHub Issue #4828中的公开确认，攻击者已取得对合法PyPI发布线的实质控制能力，将xinference 2.6.0、2.6.1、2.6.2三个版本打上恶意载荷后直接通过官方发布通道分发。推断攻击者通过窃取维护者或CI凭据实现了对发布线的接管，但该路径目前尚未被官方完全闭环确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxRSb8t5aqAHYzQS6jvJrqNnKOm8fadpFuCiaahkDfeEiayyNvZdHepnS4dzdg2mO7qbIMGNM9YcLzJI0JV6ibEyNgr5L62eQ1lHia4/640?wx_fmt=gif&from=appmsg)

**影响范围与风险分析**

根据项目官方公告与JFrog、OX Security等第三方研究分析，这次事件的核心影响不在于攻击者是否直接篡改Xinference项目代码仓库，而在于其能够通过合法的PyPI发布线将凭据窃取木马静默植入大量AI推理节点，并由此形成对云平台、代码托管、包仓库和数据库等多类下游资产的级联外泄风险。

* 受影响范围： PyPI上xinference 2.6.0、2.6.1、2.6.2三个版本，上传时间集中在2026年4月22日前后，已由项目方紧急yank；目前PyPI最新安全版本为2.5.0（发布于2026年4月12日前后）。

* 暴露数据： 样本重点收集Linux主机上的SSH私钥与主机密钥、AWS/GCP/Azure云凭据与IMDSv2角色令牌、Kubernetes kubeconfig与service account token、Docker认证、npm/PyPI/Cargo发布令牌、.env与.gitconfig机密、数据库与邮件配置、Terraform状态、WireGuard与Helm数据、TLS私钥及Bitcoin/Ethereum/Solana/Cardano/Monero等加密钱包文件。

* 级联风险： 由于Xinference天然部署在富含云凭据与模型资源的AI基础设施中，一旦导入即可能在极短时间内外传大量高价值凭据，进而引发云账号接管、K8s接管、包仓库二次投毒、源码泄露、数据库外泄与资金类欺诈等级联后果。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxSFibOKdua3dibB12Ite1nvaPIRmSmowHx55lKt1vaqmvlticj2pCpD1F7HdCicr3YzAypOwKn9RIbyAST8iaIbIjlwQe9KwicicEWnXk/640?wx_fmt=gif&from=appmsg)

**受影响场景**

本次事件主要影响在Linux服务器、GPU推理节点、Kubernetes节点、容器构建机、CI Runner或云主机上安装并导入过受影响版本的AI/ML团队、平台运维团队与自托管推理服务运营方，尤其是将以下资产直接置于Xinference部署环境中的场景：

* ~/.ssh/id\_rsa 与 /etc/ssh/ssh\_host\_\*\_key

* ~/.aws/credentials、~/.aws/config 与IMDSv2角色令牌

* ~/.kube/config、

  /var/run/secrets/kubernetes.io/serviceaccount/token

* ~/.docker/config.json、~/.npmrc、~/.pypirc、

  ~/.cargo/credentials.toml

* .env、.env.local、.env.production、.git-credentials

* .pgpass、.my.cnf、redis.conf、postfix sasl\_passwd、terraform.tfvars、terraform.tfstate

* .pem、.key、.p12、.pfx等TLS与证书私钥材料，以及加密货币钱包与keystore

同时公开情报显示本次事件尚未出现针对官方Docker镜像的大规模成功投毒证据，已落地的供应链影响目前主要集中在PyPI发布线。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTZqVwe23kSdL5cGKicjArbau9La65H9CibgqMibWdcLASgwDTBObDYmOzxxVictp1JHIyibu1RzHZY5dG9sLricoudz5UiafrVQ8PMzM/640?wx_fmt=gif&from=appmsg)

**攻击时间线**

|  |  |  |  |
| --- | --- | --- | --- |
| 时间 | 事件 | 详细说明 |  |
| 2025/10 | 维护者关联机器人异常 | XprobeBot机器人账号开始出现异常活动，随后被怀疑是未经授权上传PyPI包的关键切入点。 |
| 2025/12 | CI/CD风险披露期 | JFrog研究员报告xorbitsai/inference仓库GitHub Actions存在pull\_request\_target命令注入风险，可理论上导致PYPI\_PASSWORD、DOCKERHUB\_PASSWORD等机密泄露并形成供应链后果。 |
| 2026/1/25 | GitHub公开披露CI/CD漏洞 | xorbitsai/inference仓库Issue #4528公开说明该命令注入与仓库接管风险，影响可延伸至PyPI和DockerHub发布链，随后被标记为通过PR修复，但与本次4月投毒的直接因果关系尚未被官方闭环。 |
| 2026/4/12 | 正版2.5.0发布 | 维护者按正常流程在PyPI发布xinference 2.5.0（目前仍为推荐安全版本）。 |
| 2026/4/22 | 恶意版本上传 | XprobeBot账号将Base64混淆恶意载荷写入xinference/\_\_init\_\_.py，并以2.6.0、2.6.1、2.6.2三个版本推送至PyPI，GitHub侧无对应标签或提交。 |
| 2026/4/22 | 社区发现异常行为 | 用户在安装xinference 2.6.2后发现服务出现异常行为，包括在服务器上执行与密码相关的grep动作，并在GitHub Issue #4828告警。 |
| 2026/4/22 | 官方确认遭攻击并撤回 | 项目维护者在Issue #4828明确回复"Yes, we are under attack, we have just yanked those versions."。JFrog当日发布详细分析并纳入Xray (XRAY-96896)，OX Security发布独立确认。 |
| 2026/4/22 | TeamPCP公开否认 | TeamPCP通过X账号@pcpcats公开否认参与本次事件 |

**技术特征与攻击行为分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQ8lx6P5goRN4KJK41cGh8FJrghT4tAt9z30KSLMfYdCPlLsYNiaPuhh3Xp0nDjakql9VMhKLDH4F3hdjxY69FXJbS9LIIr9iads/640?wx_fmt=gif&from=appmsg)

**投毒载体与进入方式**

本次事件并非攻击者在Xinference官方源码仓库、提交历史或构建流水线中植入恶意代码，而是典型的"合法PyPI发布线劫持"。

恶意代码仅被注入在xinference/\_\_init\_\_.py中，这意味着只要用户执行import xinference、通过CLI启动服务，载荷就会自动执行。根据JFrog分析，第一阶段为高度混淆的Base64字节串，运行时解码并通过subprocess.Popen派生一个独立的后台Python解释器，将stdout/stderr全部压制；第一阶段再解码第二阶段采集器并通过标准输入喂给子进程，把采集结果写入临时文件、压缩为love.tar.gz后外传，随即清理临时痕迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxTgYercjtGeeib5f4npPQDBdKkcLbW0Kc4EP90l9ms31Z6Kwibn5kh1bP337goLo1jUZV1Nom9dqupXjfzv3kicJsSQ1ITFzwUYz8/640?wx_fmt=gif&from=appmsg)

**信息收集目标**

潜在暴露对象包括：

* 主机画像信息： hostname, pwd, whoami, uname -a, ip addr / ifconfig, ip route, printenv

* SSH密钥与主机密钥： ~/.ssh/id\_rsa, /etc/ssh/ssh\_host\_\*\_key

* 云平台凭据： ~/.aws/credentials, ~/.aws/config, GCP配置, IMDSv2角色令牌, AWS Secrets Manager ListSecrets 与 SSM DescribeParameters枚举

* Kubernetes凭据： ~/.kube/config, /var/run/secrets/kubernetes.io/serviceaccount/token

* 容器与包管理凭据： ~/.docker/config.json, ~/.npmrc, ~/.pypirc, ~/.cargo/credentials.toml

* Git与源码凭据： ~/.git-credentials, ~/.gitconfig

* 环境变量与机密文件： .env, .env.local, .env.production

* 基础设施配置： terraform.tfvars, terraform.tfstate, WireGuard, Helm

* 证书与TLS材料： .pem, .key, .p12, .pfx

* 加密货币钱包： 比特币、以太坊keystore、Solana validator keypair、Cardano、Monero等

* Shell历史与系统账号信息： .bash\_history, .zsh\_history, /etc/passwd, /etc/shadow

* 应用类Webhook与API密钥： Slack/Discord Webhook, JSON/配置文件中的各类API Key

这些凭据一旦外泄，可能被用于数据窃取、会话伪造、云资源接管、Kubernetes接管、包仓库二次投毒、源代码泄露、数据库外泄、资金类欺诈和加密货币盗取，甚至进一步实施真正的下游软件供应链投毒。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxRLR5f3TkDb8h64gPJwpxjkNhpalKD1iaCpx3kpPGARbgawCU9ab6GOsNRwYjfxKIA3Jqsw1Uhme25fsRFSbFWcBXW0kd3dQCMI/640?wx_fmt=gif&from=appmsg)

**持久化与横向移动能力**

由于AI推理环境通常持有跨云、跨项目的高权限凭据，样本外泄的数据具备天然的横向移动潜力：一份被窃的AWS IAM密钥可能直接打开云账号；一份被窃的K8s service account token可能直接接管集群；一份被窃的PyPI/npm/Cargo令牌则可能被攻击者用于对下游其它开源项目再次实施供应链投毒，形成链式放大。

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQnQPFKgia84BPmTEh2ic7JtxHh3t67ibupVfFe4FqpGmWjLHvI6ABpibxZhHwnLzoJwVJxX2Wq9QJrh05DFBm63vIdUsW6rBSeDqE/640?wx_fmt=gif&from=appmsg)

**建议处置流程**

1. 识别影响主机：梳理所有安装或运行过xinference 2.6.0/2.6.1/2.6.2的主机、容器与CI环境。

2. 保全取证证据： 处置前先保留日志、pip缓存、site-packages目录与DNS/代理审计记录。

3. 按优先级轮换凭据： 立即轮换SSH密钥、云IAM凭据、K8s令牌、Docker/PyPI/npm/Cargo令牌、数据库密码与.env机密。

4. 核查下游访问日志：回溯云平台、代码托管与包仓库的访问记录，排查异常登录、令牌滥用与可疑外连。

5. 审计CI/CD与发布凭据： 清理xorbitsai/inference相关GitHub Actions权限、PYPI\_PASSWORD等机密与不再使用的机器人账号。

6. 强化安全配置： 在PyPI、GitHub及维护者账号启用MFA，使用依赖锁定与SBOM工具持续扫描。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxSVmkId4WibNibxtwnJwoOC8GsAE3NdM3zZWt85iaibuicPG0l1JrvKaUOuLgib89YKiat8Wel03lgd5aQBEL6CyvicLicVL713eOjSZiaAk/640?wx_fmt=gif&from=appmsg)

**IOC**

e1e007ce4eab7774785617179d1c01a9381ae83abfd431aae8dba6f82d3ac127

077d49fa708f498969d7cdffe701eb64675baaa4968ded9bd97a4936dd56c21c

fe17e2ea4012d07d90ecb7793c1b0593a6138d25a9393192263e751660ec3cd0

whereisitat.lucyatemysuperbox.space

hxxps://whereisitat.lucyatemysuperbox.space/

MITRE ATT&CK:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tactic** | **Technique** | **ID** | **Application** |  |
| Initial Access | Supply Chain Compromise: Compromise Software Supply Chain | T1195.002 | 恶意代码通过合法PyPI发布线推送至xinference 2.6.0/2.6.1/2.6.2 |
| Execution | Command and Scripting Interpreter: Python | T1059.006 | \_\_init\_\_.py中双层Base64载荷导入即执行 |
| Defense Evasion | Obfuscated Files or Information | T1027 | 双层Base64混淆 + subprocess.Pop...