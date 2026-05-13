---
title: 【恶意文件通告】关于Hugging Face平台仿冒OpenAI仓库的供应链投毒事件
url: https://mp.weixin.qq.com/s/1Gz41IktUfVoyT2bzfswxQ
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:46.868700
---

# 【恶意文件通告】关于Hugging Face平台仿冒OpenAI仓库的供应链投毒事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/APc6NwjLsxRK4QJxrQXh0OYem3FKDCf8NlQ407AColXwAzxLdzmn6XLNbCpjlJIibPdsthb3IcyoTGhPic8FcdXnCmWY9d4JAzzf78KSDSD70/0?wx_fmt=jpeg)

# 【恶意文件通告】关于Hugging Face平台仿冒OpenAI仓库的供应链投毒事件

深瞻情报实验室
深瞻情报实验室

深信服千里目安全技术中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQ2FicTTpURJDveiayY3JWuRyjO08FribGd9JPtjtqLsS1Mu3XLvmMNOqVm3ert49K0du4FGt3IBn94r21kibfvZn9h33QichHOujqE/640?wx_fmt=gif&from=appmsg)

近期，深信服千里目安全技术中心监测到一起围绕Hugging Face平台的开源AI供应链投毒事件。

安全研究机构HiddenLayer于2026年5月7日披露，攻击者通过typosquatting技术在Hugging Face仿冒OpenAI官方“Privacy Filter”项目，创建恶意仓库Open-OSS/privacy-filter，借助虚假账户刷star冲上平台趋势榜榜首，在被清除前累计下载量约244,000次，最终向受害者部署基于Rust语言开发的Sefirah窃密木马，是开源AI生态历史上规模最大的恶意分发事件之一。

**恶意文件概要**

|  |  |
| --- | --- |
| **事件名称** | 关于Hugging Face平台仿冒OpenAI仓库的供应链投毒事件 |
| **发布时间** | 2026年5月12日 |
| **威胁类型** | 供应链投毒、信息窃取木马 |
| **简单描述** | 攻击者在Hugging Face注册仿冒OpenAI Privacy Filter的恶意仓库Open-OSS/privacy-filter，通过虚假账户刷star冲上趋势榜首，借助loader.py四阶段感染链投递基于Rust的Sefirah信息窃取木马，窃取受害者的浏览器凭据、加密货币钱包、Discord令牌、SSH/FTP/VPN凭证及系统敏感数据。 |
| **关键特征** | loader.py禁用SSL并解码远程payload；多阶段PowerShell隐藏执行；批处理写入Microsoft Defender排除项；C2域名通过Cloudflare CDN中转隐藏真实基础设施。 |

**事件详述**

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxRm3L7xIqTajcaKiayoAiaLxgzqF5kXq9VYRZ6a8AicIM2Bmm1eEvBsW1DQaK4ShRVIyPBC2zZZCAV4u6sLvOz5YF4Fokd7U2Ygdg/640?wx_fmt=gif&from=appmsg)

**攻击背景与起因**

近期，深信服千里安全技术中心监测到一起 Hugging Face 平台的信任链滥用事件。据 HiddenLayer安全研究团队披露：攻击者在全球最大的开源AI模型托管平台Hugging Face上，创建了名为Open-OSS/privacy-filter的恶意仓库。该仓库利用typosquatting（仿冒拼写/相似命名）技术，冒充OpenAI官方发布的Privacy Filter项目，逐字复制原始项目的Model Card文档，建立高度可信的视觉欺骗。与此同时，攻击者通过自动化脚本批量生成约667个虚假账户对该仓库进行star操作，将其推上Hugging Face平台趋势榜（Trending）榜首位置。

本次事件滥用了开源AI社区中以“项目名称、下载量、点赞数”为核心的隐性信任体系，是一次典型的供应链投毒事件。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTcML2EtG5icyagz63icGCrwUjg2EuVNlJYOCAHRIvdf3bq7bQqTjuoIZaLhT4DwP8S3qu4ickel5dxQicgyicS9YUf1SXAup0P9uiaw/640?wx_fmt=gif&from=appmsg)

**影响范围与风险分析**

根据HiddenLayer与BleepingComputer的联合披露，本次事件的核心风险并不在于Hugging Face平台代码本身遭篡改，而在于攻击者能够借助开源AI生态的高度开放性，对全球AI开发者、模型工程师及企业研发团队执行近乎“广播式”的恶意软件分发。

* **受影响范围：**恶意仓库在被下架前累计下载量约244,000次，研究人员指出该数字部分可能被人为放大，但仍有相当数量的真实开发者主机被入侵。

* **暴露数据：**浏览器Cookie、保存密码、加密密钥与会话令牌（Chromium与Gecko系）、Discord令牌与本地数据库、加密货币钱包及种子短语、SSH/FTP/VPN凭据及FileZilla配置、本地敏感文件、完整系统信息与多屏截图。

* **级联风险：**受害者多为AI开发者与算法工程师，其主机内通常托管有OpenAI/Anthropic API Key、GitHub/GitLab访问令牌、云厂商凭据、AI模型权重与训练数据集等高价值资产，单台主机失陷即可引发企业级密钥外泄、模型权重盗取乃至云资源接管。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSmIfxCjeMQyW0Gym06JuLJtbP2ooXjJVOc0MHmfOVfXuoaEsTFwLsZqQNibMC8Xy9aN5IbuTbiaNgYMHXdf8bq4t6SuGm4cfEQ4/640?wx_fmt=gif&from=appmsg)

**受影响场景**

本次事件主要影响在Hugging Face上拉取/下载第三方模型与脚本、并直接在主机本地环境执行的开发者与企业用户，尤其是以下场景：

* 直接使用git clone或huggingface-cli下载Open-OSS/privacy-filter并在物理机或开发主机执行loader.py；

* 在AI Notebook、Jupyter环境中以root或管理员权限交互式运行未审计的第三方模型加载脚本；

* 在缺少代码签名校验与Sandbox隔离的情况下将Hugging Face模型直接集成进CI/CD流水线；

* 同时在同一主机保存浏览器密码、加密货币钱包、SSH私钥与各类Token的AI开发者；

* 将下载量、趋势榜排名作为模型可信度评估主要依据的团队。

截至披露时，Hugging Face平台本身的基础设施未发现被入侵，OpenAI官方Privacy Filter项目亦未被篡改，本次受害对象集中在主动从仿冒仓库下载并本地执行恶意代码的终端开发者。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxSbyjZ2icb4bhsHRn3OfSoSzo0WicNfzGib5sD7icXTChUsyfeKibhrO1FGgPngR6D7g5CiasWOiaYEwmOiaCwat5UKCbzzTvTicUHq04Ew/640?wx_fmt=gif&from=appmsg)

**攻击时间线**

|  |  |  |
| --- | --- | --- |
| **时间** | **事件** | **详细说明** |
| 2026/2/16 | C2基础设施预置 | 攻击者注册C2域名recargapopular.com，使用TUCOWS.COM作为注册商，并配置Cloudflare名称服务器（deborah/west.ns.cloudflare.com），提前约3个月部署用于后续数据外泄的基础设施。 |
| 2026/2 – 2026/5 | 恶意仓库创建与伪装 | 攻击者在Hugging Face注册Open-OSS/privacy-filter仓库，逐字复制OpenAI官方Privacy Filter的Model Card，植入伪装为AI推理代码的loader.py。 |
| 2026/2 – 2026/5 | 虚假账户刷榜推热 | 通过自动化脚本生成大量虚假账户对仓库执行star操作，约667个账户参与点赞，将恶意仓库人为推上Hugging Face趋势榜榜首位置。 |
| 披露前阶段 | 大规模分发 | 在Trending榜单曝光下，仓库累计下载量约244,000次，多个真实受害者主机被Sefirah窃密木马感染。 |
| 2026/5/7 | 初次披露 | HiddenLayer研究人员公开仿冒仓库、loader.py、PowerShell加载链与最终Sefirah载荷的完整分析。 |
| 2026/5/9 | 媒体技术报道 | BleepingComputer发布配套技术分析，曝光C2域名recargapopular.com及与npm typosquatting活动的关联。 |
| 披露后 | 下架与扩展溯源 | Hugging Face下架Open-OSS/privacy-filter仓库；研究人员进一步发现，该loader基础设施与npm生态中分发WinOS 4.0植入程序的typosquatting活动存在重叠，指向同一跨平台威胁行为体。 |

**技术特征与攻击行为分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQYpibroj2ASzsv54YEMLZwZ23cbocfibIPibjfROGkCu7D4EuOCFfoTWibbpVR4C7AYicE6eO71vWxibW9ychNwfSKH9rTZdsmxOwu8/640?wx_fmt=gif&from=appmsg)

**投毒载体与进入方式**

本次事件是典型的“开源AI生态typosquatting + 信任语义滥用”。攻击者综合运用以下三层手段进入受害者主机：

* 命名仿冒：通过Open-OSS/privacy-filter等高相似度命名仿冒OpenAI官方Privacy Filter项目，欺骗按关键词检索/复制粘贴使用模型的用户；

* 内容仿冒：几乎逐字复制原始项目的Model Card文档与项目描述，使README与示例代码具备与官方近乎一致的视觉与语义可信度；

* 社群信号操纵：用自动化生成的约667个虚假账户进行star操作，借助Hugging Face趋势榜的曝光放大作用，使仓库短时间内冲上榜单榜首；

* 依赖默认行为：受害者按惯例直接执行示例脚本loader.py，攻击链由此打通。

本次攻击充分利用了开源AI生态相较传统软件包生态的两点差异：其一，模型仓库往往包含可执行的预处理/推理脚本，执行边界从“安装”延伸到“加载”；其二，社区对“下载量+点赞数+趋势榜”的依赖远高于代码签名等强校验机制，使得攻击者能够在不投放0day的情况下实现大规模感染。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxS1M7uCIUgCeiatD4ogHxG42CicKFvSSVriaZh1OrlDUZricfia1ftRMBqicPstV3nSpoJ01YibPZa9IkdV3HODh5bvbotkxK0mia46ciaI/640?wx_fmt=gif&from=appmsg)

**多阶段感染链与信息收集目标**

攻击者构建了四阶段感染链：从看似合法的Python脚本起步，逐级隐藏意图，最终落地基于Rust编译的Sefirah窃密木马。

潜在收集对象包括：

* 浏览器数据：Chromium/Gecko系浏览器的Cookie、保存密码、加密密钥、浏览历史、会话令牌；

* 即时通讯：Discord令牌、本地数据库与主密钥；

* 加密资产：本地加密货币钱包文件、浏览器扩展中的钱包、钱包种子短语与私钥；

* 远程访问凭据：SSH、FTP、VPN凭据及配置文件（含FileZilla）；

* 开发者凭据：本地保存的API Key、Access Token、配置文件中的明文密钥；

* 系统信息：完整主机信息、安装软件清单、用户名、多显示器全屏截图。

窃取到的数据经压缩后通过HTTP协议外泄至C2服务器recargapopular[.]com，该域名于2026年2月16日由TUCOWS.COM注册，并通过Cloudflare CDN中转隐藏真实后端。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSl09b53w1HlRibvhr4aibyuqwvemb60MRuia9WCvryZy7RKpgT5Np62TRnxlohNqMRActD0CQgxEptmVk1D8KHhUkWEuq9uJ7LbQ/640?wx_fmt=gif&from=appmsg)

**持久化能力**

Sefirah载荷集成了多层反分析机制，仅在确认运行环境为真实受害者主机时才会触发完整恶意行为，显著提高了沙箱与自动化分析的成本：

* 虚拟化环境检测：识别VMware、VirtualBox、QEMU等虚拟机特征；

* 沙箱检测：识别主流自动化分析沙箱的行为特征与硬件指纹；

* 调试器检测：检测附加调试器与软件断点；

* 分析工具检测：识别Wireshark、Procmon等主机进程。

* 持久化方面：攻击者并未采用经典的注册表Run键或计划任务，而是通过将最终载荷写入Microsoft Defender排除路径，使Sefirah及其后续行为长期免于本机AV扫描，从而在不显著触发用户感知的情况下保留持续执行能力。

**解决方案**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxReosr3zJQQOricfWI6ql17fFC0u3ZDgViaickB33Cq1rTHkc4XUiaBBE5BQr8QAWfgNqI0TCYmibkmLmD28tZnnVzWbXE0BaIzZqMQ/640?wx_fmt=gif&from=appmsg)

**建议处置流程**

针对已下载或执行过Open-OSS/privacy-filter相关代码的开发者及企业用户，建议立即执行如下处置流程：

1. 识别受影响主机：在终端与EDR中检索是否曾从Hugging Face拉取过Open-OSS/privacy-filter，或访问过recargapopular[.]com；

2. 隔离与重装：对疑似受感染主机直接执行重装/重映像，确保loader、PowerShell stager、start.bat与Sefirah主体被彻底清除；

3. 凭据全面轮换：轮换该主机曾保存的浏览器密码、API Key、SSH私钥、云厂商凭据、Git Token、OpenAI/Anthropic等AI服务Key；

4. 会话失效：使所有浏览器会话Token与SSO登录态失效，重置双因素认证种子；

5. 清理本机Defender排除项：检查并删除被start.bat写入的Microsoft Defender排除路径，恢复正常扫描覆盖范围；

6. 日志与外联审计：审查近期出站流量是否存在指向恶意域名；

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTibmkibHtG6ghwjN2Sbol24szvGLShokiaNWdMVcjUb6SrwibOYia8MqbbGO0bN1e9NSDOC2wibKqv59SmJUqbn8xdb9ZejIhCYXg1E/640?wx_fmt=gif&from=appmsg)

**IOC**

recargapopular[.]com

172.67.165.218

104.21.66.235

MITRE ATT&CK:

|  |  |  |  |
| --- | --- | --- | --- |
| **Tactic** | **Technique** | **ID** | **Application** |
| Resource Development | Acquire Infrastructure: Domains | T1583.001 | 攻击前3个月注册recargapopular.com，使用Cloudflare中转隐藏后端。 |
| Initial Access | Supply Chain Compromise | T1195 | 在Hugging Face投放仿冒OpenAI Privacy Filter的恶意仓库。 |
| Initial Access | Phishing | T1566 | 通过命名仿冒与刷榜实施针对AI开发者的社会工程诱导下载。 |
| Execution | Command and Scripting Interpreter: Python | T1059.006 | loader.py作为初始执行入口。 |
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 | 以WindowStyle Hidden隐藏执行下载后阶段命令。 |
| Defense Evasion | Impair Defenses: Disable or Modify Tools | T1562.001 | 禁用SSL校验；写入Microsoft Defender排除项。 |
| Defense Evasion | Virtualization/Sandbox Evasion: System Checks | T1497.001 | VM/沙箱/调试器/分析工具检测，仅在真实主机执行。 |
| Credential Access | Credentials from Password Stores: Web Browsers | T1555.003 | 提取Chromium/Gecko浏览器保存的密码与令牌。 |
| Credential Access | Unsecured Credentials: Private Keys | T1552.004 | 采集SSH/VPN/加密钱包私钥与种子短语。 |
| Collection | Screen Capture | T1113 | 抓取主机多显示器全屏截图。 |
| Exfiltration | Exfiltration Over C2 Channel | T1041 | 通过HTTP将压缩数据外泄至recargapopu...