---
title: 如果你有一台闲置 VPS，建议看看这个开源蜜罐 wisp
url: https://mp.weixin.qq.com/s/PQgZzwTOtl6HRR7X35R8uw
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:17.218187
---

# 如果你有一台闲置 VPS，建议看看这个开源蜜罐 wisp

# 如果你有一台闲置 VPS，建议看看这个开源蜜罐 wisp

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**开源地址：**https://github.com/iamwillychen/wisp

如果你手里只有一台普通 VPS，能不能拿它做一个真正有用的蜜罐？

以前我的答案可能会比较谨慎。

因为传统蜜罐并不是“开几个端口，记录一下 SSH 登录”这么简单。要模拟的服务越多，依赖越复杂，日志、告警、数据保存也会跟着上来。像 OpenCanary 这样的成熟方案本身就很好，但部署时涉及 Python、Twisted、Scapy，SMB 场景还会牵扯 Samba 等组件。

最近看到一个比较新的项目 **wisp**，思路倒是挺直接：

**把蜜罐做成一个 Go 编译出来的单体程序，然后直接丢到服务器上运行。**

更有意思的是，它没有只盯着 SSH、FTP、HTTP 这些传统服务，而是开始模拟 Kubernetes、Docker、云元数据、Jenkins、GitLab、Ollama、MCP 等现在更容易暴露出来的服务。

![image-20260926204355191](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfMWYmhW1Ghv3ot5vsv88tLY3UHvTycG7pG7PhN5bFgMrMXHpbo4smqSshicyPA6Gajb3cib5chpia1eYb34jh4yskBa0OwCIx7uHw/640?wx_fmt=other&from=appmsg)

这就让“一台 VPS 做蜜罐”这件事重新变得有意思了。

## 一、wisp 到底是什么？

wisp 的定位很明确：

**Single-binary network honeypot sensor and self-hosted console。**

简单翻译一下，就是：

**一个单二进制的网络蜜罐传感器 + 自托管管理控制台。**

![image-20260926204236354](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfNTnntmuK6cIkJ6zw95owBhMb59R4hC8nuiciaE1nnGX79V4OZEGfdHficqZ5U7icdiaBlwtqF6rKiaPXSd56MxhjnriaGQjAPnSWVQOQ/640?wx_fmt=other&from=appmsg)

目前项目仍然处于 pre-1.0 阶段，所以它并不是一个已经打磨多年的成熟商业产品。项目作者自己也明确把它和 OpenCanary 做了比较，并承认 OpenCanary 更成熟。

但 wisp 有一个很现实的优势：

**部署简单。**

项目提供 Go 二进制运行方式，也提供 Dockerfile 和 Docker Compose；传感器和控制台可以分别运行。

这对于 VPS 用户很重要。

因为很多人不是不会搭蜜罐，而是懒得为了一个蜜罐维护一大串依赖。

一个 Python 环境坏了，要修。

一个系统包版本不兼容，要修。

SMB 又需要额外组件。

最后折腾半天，蜜罐还没开始收集数据。

wisp 的路线则比较粗暴：

```
textVPS
 │
 ├── wispd
 │
 ├── 蜜罐服务
 │
 ├── 日志
 │
 └── 可选 Console
```

编译或者拉镜像之后直接跑。

![image-20260926204456212](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfOV0KD1fL8OoLKcDyAOJv1nibvBmdqCtKDSibTxb945uJ579FUaOrUMBYiaSU9sOyvZJ1hKVlhS9QWdJicSEYemkcSX3WVFmEu6ibWI/640?wx_fmt=other&from=appmsg)

## 二、真正让我觉得它有意思的，不是 SSH 蜜罐

如果 wisp 只是做一个 SSH Honeypot，我其实不会专门写它。

因为 SSH 蜜罐已经不是什么新鲜东西了。

公网 VPS 开一个 SSH 服务，过不了多久通常就会遇到：

```
textroot
admin
test
ubuntu
user
```

之类的用户名尝试。

再往后就是各种密码组合。

这类数据当然有价值，但问题是：

**现在攻击者盯着的已经不只是 SSH。**

尤其是云原生环境越来越普遍以后，攻击面开始往另外几个方向移动。

比如：

```
textKubernetes API
Kubelet
Docker Socket
Cloud IMDS
Jenkins
GitLab
Elasticsearch
Ollama
MCP
```

![image-20260926204530683](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPNSgblJNKJhod2VsDLCEMWIubbic0XBewqybg34MfbJYXUgS2jCDnhNmeX2Sfqws3CJP3eo1GsSAUbefW0SR7DqfvvRiaDHDYwk/640?wx_fmt=other&from=appmsg)

这些服务一旦暴露出来，攻击者感兴趣的东西也和传统 SSH 爆破不太一样。

wisp 的一个核心思路，就是专门针对这些现代基础设施增加“诱饵”。

项目目前列出了 9 类 OpenCanary 没有覆盖的新型 decoy，包括 Kubernetes、kubelet、Docker、云 IMDS、Jenkins、GitLab、Ollama 和 MCP 等。

这才是我觉得它值得关注的地方。

## 三、为什么 Docker、K8s、MCP 都值得做成蜜罐？

因为这些服务背后的信息，可能比一个 SSH 登录失败更加有意思。

举个比较容易理解的例子。

假设攻击者发现了一个疑似 Ollama 服务。

传统蜜罐可能只告诉你：

> 有人连接了这个端口。

但 wisp 的 Ollama decoy 可以记录攻击者发送过来的 prompt。

项目 README 给出的示例里，甚至直接记录了攻击者尝试让模型执行：

```
textcat /etc/shadow
```

这样的请求。

最后日志中会留下模型名称、请求路径和 prompt 等信息。

这就完全是另一种数据了。

你看到的不只是：

> “有人扫我。”

而是：

> “有人发现了我的 AI 服务，并且下一步准备干什么？”

对于研究 AI 基础设施攻击面来说，这种数据明显更有意思。

![image-20260926204553428](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfNHjBbN4mYB4FqKzLoFcBdqIZXWNF1ibgYY99ofNhiam5Mh485AeyIYGLQ71YkGIXv08Nz5GWicQPXJVx2fVkn3NK5IYC2EdfX5K8/640?wx_fmt=other&from=appmsg)

## 四、Docker 蜜罐就更有意思了

Docker 本身已经成为很多服务器上的基础设施。

而 Docker Socket 又是一个很特殊的东西。

如果一个环境错误地把 Docker Socket 暴露给不可信用户，那么攻击者面对的就不只是一个普通 Web 服务。

wisp 针对 Docker 做了对应的 decoy。

项目介绍中提到，它可以捕获攻击者尝试提交的容器规格，例如：

```
textPrivileged: true
```

以及 Host Mount 等信息。

这类数据非常适合拿来做攻击行为分析。

因为你可以开始观察：

**攻击者到底想把什么容器跑起来？**

而不是简单地统计：

**今天来了多少 IP。**

两者的信息价值完全不同。

## 五、云服务器还有一个很容易被忽略的攻击面：IMDS

如果你经常玩云服务器，应该听过 IMDS。

简单来说，云平台实例内部通常存在一个用于获取实例元数据的接口。

正常情况下，这东西应该只被特定服务使用。

但一旦攻击者能够从一个存在 SSRF 等问题的应用访问到云元数据接口，就可能进一步尝试获取实例相关信息。

所以 wisp 把 **IMDS** 也做成了蜜罐诱饵。

这说明它考虑的已经不是：

> “有人正在扫描我的 SSH。”

而是：

**“如果攻击者把一台云服务器当成目标，他接下来会寻找什么？”**

这也是现代蜜罐和传统蜜罐之间比较明显的区别。

## 六、MCP 甚至也被放进来了

这一点可能是 wisp 最“2026”的地方。

现在很多 AI Agent 开始通过 MCP 连接外部工具和数据。

MCP 本身并不是攻击工具，但一旦 Agent、MCP Server、工具权限和敏感数据混在一起，安全问题就会变得复杂。

wisp 直接增加了 MCP decoy。

它甚至支持 MCP 类型的 honeytoken。

也就是说，你可以把一个看起来像 MCP 配置的东西放进环境中。

如果有人或者某个 Agent 加载了这个配置并进行连接，就能够产生对应事件。

项目目前的 token 类型还包括 HTTP、DNS、Word 文档、kubeconfig 和 MCP。

## 七、那一台普通 VPS 到底能不能跑？

答案是：

**可以，而且这恰恰是 wisp 这种项目比较有吸引力的地方。**

因为它不是把整套 SIEM、ELK、几十个容器全部塞进 VPS。

最简单的情况下，一个 `wispd` 就可以作为传感器运行。

项目默认配置甚至可以直接启动：

```
bash./wispd
```

如果想进一步部署管理控制台，则可以再运行：

```
textwispd
   ↓
Sensor
   ↓ HTTPS
wisp-console
   ↓
SQLite
   ↓
事件 / 告警 / 查询
```

控制台本身也是 Go 程序，项目采用 SQLite 保存数据。

所以从架构上来说，它并不要求你一开始就准备一台很夸张的服务器。

## 八、不过，公网 VPS 部署蜜罐有一个原则

**蜜罐和业务服务器最好不要放一起。**

这一点比 CPU、内存配置重要得多。

如果你有一台正在跑网站的 VPS：

```
text网站
数据库
Docker
个人文件
SSH
蜜罐
```

全部放在一起，然后直接把蜜罐暴露到公网。

这不是一个特别好的实验方案。

因为蜜罐的核心工作就是：

**故意让不可信流量接近它。**

而它又需要解析攻击者发送过来的各种输入。

所以更合理的思路是：

```
text业务服务器
      │
      │
      │  隔离
      ▼
蜜罐 VPS
      │
      ├── wisp
      ├── 日志
      └── Console
```

最好再通过防火墙限制管理端口。

真正需要暴露到公网的，是你准备拿来“吸引访问”的那些服务端口。

管理控制台不要因为图省事直接裸奔。

## 九、蜜罐最怕的其实不是攻击，而是“被攻击以后失控”

很多人第一次搭蜜罐会有一个误区：

> “反正是假的，随便开。”

恰恰相反。

蜜罐应该是：

**看起来像真的，但实际上什么都不能真的做。**

wisp 自己也强调这一点。

例如认证请求不会真正放行；容器、服务和系统环境都是诱饵。

项目提供的 Docker 部署还采用了非 root 用户、只读根文件系统、删除能力权限以及 `no-new-privileges` 等限制。

这其实是蜜罐设计里非常关键的一层：

```
text攻击者
  ↓
诱饵服务
  ↓
记录行为
  ↓
告警
  ↓
结束
```

而不是：

```
text攻击者
  ↓
诱饵服务
  ↓
真的执行命令
  ↓
真的访问宿主机
  ↓
寄
```

蜜罐的任务是观察攻击行为，不是给攻击者提供一个免费的 VPS。

## 十、日志比“攻击次数”重要

搭蜜罐最容易犯的第二个错误，是只看：

> 今天有 132 个 IP 扫描。

这个数字看起来挺刺激。

但其实没那么重要。

真正值得分析的是：

```
text谁
 ↓
什么时候
 ↓
访问什么服务
 ↓
发送了什么请求
 ↓
尝试使用什么凭证
 ↓
下一步想干什么
```

wisp 的日志可以输出 JSONL，每条事件包含时间、节点、服务、源 IP、目标端口以及捕获的数据。

而且这些 JSON 日志可以进一步交给 Vector、Filebeat 或 SIEM。

这样一来，一台几十块钱级别的 VPS 就不只是：

> “放一个蜜罐玩玩。”

而可以变成一个小型的攻击情报采集节点。

## 十一、如果只有一台 VPS，我会怎么规划？

如果只是个人学习或者做实验，我反而不会一开始搞得特别复杂。

可以按照这个思路：

```
text公网 VPS
│
├── wisp Sensor
│
├── 日志
│
└── 防火墙
```

先观察一段时间。

等数据量起来之后，再考虑：

```
textVPS 01
└── wisp Sensor

VPS 02
└── wisp Sensor

VPS 03
└── wisp Sensor

        ↓

   wisp Console
        ↓
      SQLite
        ↓
   告警 / 分析
```

这时候就从“个人蜜罐”变成了一个小型蜜罐网络。

而 wisp 的 Console 本身就是为了多个 sensor 集中管理设计的。传感器通过 HTTPS 向 Console 上报事件，并使用独立 token 进行注册。

## 十二、一台 VPS 做蜜罐，最值得玩的其实是这个思路

以前大家搭蜜罐，关注的是：

**SSH、FTP、Telnet、Web。**

现在可以开始换一个思路：

```
text传统服务器
      ↓
SSH / FTP / SMB

云原生服务器
      ↓
Docker
Kubernetes
IMDS
CI/CD

AI 服务器
      ↓
Ollama
LLM API
MCP
Agent

未来的蜜罐
      ↓
传统攻击面
+
云原生攻击面
+
AI 攻击面
```

wisp 的价值就在这里。

它并没有试图证明传统蜜罐已经过时。实际上，项目自己也承认 OpenCanary 更成熟。它做的是另一件事情：

**把蜜罐的诱饵面往现在的云、容器和 AI 基础设施扩了一圈。**

这也是为什么我觉得这个项目值得关注。

![image-20260926204609871](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOGWMZjaS6DpDNWibPdbB3tj0FNCWwLq9mtVOvOUWd57GWcf8fmgjVsXU6Y7oGYn79b338cIwEms1HFcB5Fs2LNCXB6a53Qbr5A/640?wx_fmt=other&from=appmsg)

## 最后：VPS 真的可以成为一个安全研究工具

很多人买 VPS，第一反应都是：

> 建站。

其实服务器本身就是一个很好的安全实验环境。

你可以拿它做：

* 蜜罐
* 日志分析
* 威胁情报采集
* 安全监控
* Docker 安全实验
* AI Agent 实验
* MCP 安全研究
* 内网实验环境

而像 wisp 这种项目，把“部署一个蜜罐”的门槛又往下压了一截。

它现在还年轻，项目本身也明确标注了 **pre-1.0**，所以没必要把它包装成什么“下一代蜜罐终结者”。

更准确的说法应该是：

**它正在尝试回答一个很现实的问题：如果今天重新设计一个蜜罐，除了 SSH 和 Web，我们是不是应该把 Docker、Kubernetes、云服务以及 AI 基础设施也考虑进去？**

至少从 wisp 目前的设计来看，答案已经很明显了。

如果你手里刚好有一台闲置 VPS，拿它做个隔离的蜜罐节点，倒是一个挺有意思的玩法。

## 服务器选择

如果你准备拿 VPS 做蜜罐、安全监控或者 Docker 实验，建议优先考虑**独立服务器环境、稳定公网 IP、足够的磁盘空间以及可控的防火墙策略**。蜜罐本身并不需要一上来就堆很高的配置，先从低成本节点观察真实流量，再根据日志量决定是否扩容，通常更合理。

## 服务器推荐

阿里云全场九折优惠：

```
https://link.aitq.net/RcgjvF
```

![image-20260721194150454](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfMc9o0at10wDoESul8jnSsZIa3HiaPvhUtzrf4QudErvIDFXZibrGHEaVxdeWyWvj4GZoovhTUuwUZHKricEiba9IoAGMadtpoR7vY/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=30)

image-20260721194150454

阿里云2核2g 99计划 99元每年，续费同价

![image-20260721193517630](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfM8NjiaVk5M4vqjg0hnRuBJX5qUS0pMibKC3TS3poLSQHEGUYPD62cDpcR4GC3De6f9tibol1s9iaq8tzs3WZH2iaibR9R0qSmO2BUoM/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=31)

image-20260721193517630

腾讯云2H2G **99** 每年：

```
https://link.aitq.net/mVGWtG
```

![image-20260721194058767](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfPic37uqiapguH8XuRDVlNzLxwJLPl4iaOq5LKc9eAUJuicjcknUmw2h2hllcqxPCRpZ9sJ10EGws1vJPa9gVIGa4EA1nDicBiaG1doQ/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex...