---
title: 基于默认配置的 Dify 沙箱 RCE 利用链分析与加固探讨
url: https://xz.aliyun.com/news/93260
source: 先知安全技术社区
date: 2026-11-11
fetch_date: 2026-11-12T09:00:33.824243
---

# 基于默认配置的 Dify 沙箱 RCE 利用链分析与加固探讨

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# 基于默认配置的 Dify 沙箱 RCE 利用链分析与加固探讨

[![](/images/default-avatar.png)二三W杠八H](/users/179967)·2026-11-12 02:02·4 分钟·36·中国·AI专栏

本文分析了Dify沙箱模块因硬编码默认API密钥导致的RCE漏洞利用链。攻击者通过X-Api-Key:dify绕过鉴权，利用ctypes调用底层C库实现任意Python代码执行并穿透沙箱。该问题可导致内网零信任防线崩塌及容器底层情报泄露。

本文记录了针对开源 LLM 应用平台 Dify 沙箱模块的一次安全测试过程。在研究其网络架构与源码时，发现由于默认配置中存在硬编码的通信凭证，在特定部署条件下（如端口暴露于公网），可能存在未经授权执行代码的风险。

文章详细复现了从鉴权绕过到获取底层系统信息的完整链路。针对此问题，官方团队基于开发者体验（DX）的考量，认为该设计属于预设功能并无缺陷。本文不针对此定性做过多主观评价，仅从客观的技术视角还原漏洞细节，并从企业自托管运维的视角，给出了一套切实可行的纵深防御建议，以供安全同仁交流探讨。

### **摘要**

`dify`该服务中存在硬编码的默认 API 密钥（ ） `dify-sandbox`。能够访问 Dify 内部网络的攻击者可以`middleware.Auth()`通过`X-Api-Key: dify`请求头绕过该密钥，从而执行任意 Python 代码。本报告详细描述了完整的攻击链，从代码来源到实际验证，包括深度防御边界映射和业务级拒绝服务风险评估。

### **1. 问题起源：硬编码配置与路由分析**

**（对应附件： 2\_Docker\_Key\_Config.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0031/4b3f320f-fa3.png)

在 Dify 官方代码的 中，沙箱服务配置了 。这意味着只要运维人员未显式配置强密码，沙箱将默认回退使用 作为出厂密钥。`docker/docker-compose.ymlAPI_KEY: ${CODE_EXECUTION_API_KEY:-dify}dify`

**（对应附件： 3\_Router\_Auth.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0155/ad7b5d18-bad.png)![](https://xzfile.aliyuncs.com/2026/11/12/0155/ad7b5d18-bad.png)

沙箱的入口路由定义在 中，将所有 路径挂载了 鉴权中间件。但攻击者只需携带 ，即可瞬间突破 的防御，直接进入内部处理流程。`dify-sandbox/internal/controller/router.go/v1/sandbox/middleware.Auth()X-Api-Key: dify401`

### **2. 攻击链：从解析到任意代码执行**

**（对应附件： 4\_Run\_Controller.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0034/24b8b067-ecd.png)

在 Go 语言控制层 的 中，HTTP 请求体里的 字段被 强制接收，并通过 原封不动传递给底层，无任何过滤或消毒。`internal/controller/run.goRunSandboxControllerCodebinding:"required"service.RunPython3Code`

**（对应附件： 5\_Prescript\_Exec.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0034/f6105cac-f59.png)

代码最终落入沙箱核心的 Python 执行器 中。该脚本通过文件描述符（管道）读取载荷，并在最后一行执行了极其危险的底层代码：。攻击者的任意 Python 载荷在此处被底层加载并触发。`internal/core/runner/python/prescript.pyexec(compile(code, "<fds>", "exec"))`

### **3. 实弹验证：从 RCE 到底层 C 库穿透**

**（对应附件： 6\_RCE\_Verified.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0034/50008e8f-a19.png)

成功绕过鉴权后，发起 ，沙箱成功回显自定义字符串，证明已完全获得任意 Python 代码执行权。`print("RCE_VERIFIED_BY_HHC")`

**（对应附件： 7\_Exec\_File\_Path.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0153/c2ac485a-04e.png)

通过 变形成功获取沙箱内部临时文件的绝对路径，证明执行环境可控。`exec`

**（对应附件： 8\_Ctypes\_Module\_Found.png， 9\_Sys\_Modules\_Full.png， 10\_Builtins\_List.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0034/c162a3be-fba.png)![](https://xzfile.aliyuncs.com/2026/11/12/0035/558df170-697.png)![](https://xzfile.aliyuncs.com/2026/11/12/0035/7e3a4ee3-e74.png)![](https://xzfile.aliyuncs.com/2026/11/12/0035/ff2aae17-816.png)

通过 Python 自省机制，成功探测到沙箱底层不仅加载了 模块，还保留了 ， ， 等核心内置函数。这为突破 Python 层防御提供了致命情报。`ctypesevalexecopen`

**（对应附件： 11\_Base64\_Hidden\_Backdoor.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0157/c4265554-f2b.png)

攻击者使用 动态混淆载荷，沙箱完美解码并回显中文标记 。这证明攻击者完全可以通过动态编码绕过日志的静态流量审计，实现无文件持久化攻击。`exec(base64.b64decode(...))"我是你的后门"`

**（对应附件： 12\_Ctypes\_Timestamp.png， 13\_Ctypes\_PID.png， 14\_Sys\_Executable\_Path.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0035/d3b2b2b7-d7a.png)![](https://xzfile.aliyuncs.com/2026/11/12/0159/0be51456-a9e.png)![](https://xzfile.aliyuncs.com/2026/11/12/0200/7dc7e859-fc0.png)

借助 调用底层 C 语言库 ，攻击者成功穿透 Python 层封锁，直接触碰到了 Linux 容器底层：`ctypeslibc`

* 成功获取宿主机底层系统时间戳：。`1786588842`
* 成功获取沙箱容器内的真实进程 PID：。`51883`
* 成功获取沙箱内部 Python 二进制绝对路径：。
  这是本报告最具核心价值的底层指纹情报，证明了沙箱对攻击者来说已完全透明。`/opt/python/bin/python3`

**（对应附件： 15\_Path\_Exist\_Check.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0036/e9184fe2-68d.png)

通过纯 Python 验证文件是否存在（返回 ），侧面印证了代码执行逻辑的绝对通畅。`False`

### **4. 资源耗尽推演与业务级 DoS 风险**

**（对应附件： 16\_Resource\_Exhaustion\_Test.png）**

![](https://xzfile.aliyuncs.com/2026/11/12/0200/5babae8b-34c.png)

攻击者成功向沙箱发送大规模纯 Python 计算载荷（如列表推导式 ），沙箱返回 。尽管底层的 及时限制了单核 CPU 的占用，但这证明了攻击者完全可以在实战中通过多线程并发发送大量此类载荷，引发沙箱处理 AI 业务请求的严重延迟，直接威胁 Dify 核心业务的可用性。`[i**2 for i in range(10**6)]successcgroup`

### **5. 防御边界深度测绘**

在 RCE 与底层情报获取成功后，本报告还记录了通过发送各类特定的恶意载荷进行的防御边界推演：

* **文件系统封锁验证：** 尝试读取 和 ，被精准拦截返回 。`/proc/self/status/proc/self/cgroupoperation not permitted`
* **内网横向移动验证：** 尝试从沙箱内部通过 探测 Dify 主 API 容器，连接被底层 规则拦截。`requests.get("http://dify-api-1:5001/health")seccomp`
* **DNS 外带验证：** 尝试通过 发送 DNS 请求，同样被彻底封死。
  这些失败的测试精确绘制出了沙箱的 与 防御极限。`socket.gethostbyname_exseccompcgroup`

### **6. 危害评估与修复建议**

尽管沙箱避免了攻击者逃逸到宿主机，但这绝不能掩盖漏洞在微服务架构下的致命性：

1. **内网零信任防线彻底崩塌：** 一把 的出厂钥匙，让所有内网隔离防御形同虚设。任何触达内网的攻击者都能瞬间获得一个完整的沙箱控制权。`dify`
2. **核心底层情报严重泄露：** 容器底层真实 、绝对路径及 C 库时间戳的获取，为攻击者提供了精确定位宿主机 Linux 内核版本的瞄准镜，为后续组合攻击提供了精确的情报支撑。`PID`
3. **修复建议：** 强烈建议官方移除 中 的默认回退配置，并强制要求用户在 中显式配置高强度随机字符串作为 。`docker-compose.yml:-dify.envCODE_EXECUTION_API_KEY`

---

---

## **7.得到的相关回复**

![](https://xzfile.aliyuncs.com/2026/11/12/0102/9ea8faad-2b2.png)![](https://xzfile.aliyuncs.com/2026/11/12/0103/7a70cfff-64e.png)

## **8.给Dify使用者的建议**

1.立即修改默认秘钥（底线防御）

切勿直接使用官方默认的`docker-compose.yml`上生产环境。

修改`.env`文件中的`CODE_EXECUTION_API_KEY`，使用 `openssl rand -base -32` 生成高强度随机字符串替换`Dify`。

2.坚决实施网络隔离（核心防线）

禁止将Sandbox端口（默认`8194`）和API端口（默认`5001`）直接暴露在公网

必须使用Nginx等反向代理，仅对外暴露Web访问所需的80/443端口。Sandbox应仅在内部Docker网络或内网通信。

3.收紧沙箱权限限制（防横向移动）

在.env中确保配置`SANDBOX_ENABLE_NETWORK=false`，防止攻击者利用沙箱发起内网探测（SSRF）或DNS数据外带。

严禁以 `--privileged` 特权模式运行容器，务必使用非root用户运行，防止底层容器被直接突破。

4.建立异常监控与拦截

在网关或WAF层增加规则，拦截包含`exec`、`__subclasses__`、`base64.b64decode`等危险特征的恶意请求。

监控Sandbox容器的CPU与内存使用率，防止被恶意利用执行死循环代码导致算力耗尽（DOS）。

END

[![](/images/default-avatar.png)

二三W杠八H](/users/179967)

0文章

0粉丝

+ 关注[私信](/notifications)

© 2026 先知社区 · xz.aliyun.com

问墨白

### 评论

[登录后参与评论 →](/auth)

还没有评论，来抢沙发

### 相关阅读

[#### 基于机器学习的jsp/jspx webshell检测

前言
在上文《基于AST的Webshell检测》中，笔者已经提出了基于抽象语法树是可以用来检测Webshell的，那么如何将这种思想应用在jsp/jspx的webshell检测便是本文讨论的重点。
简单回顾下抽象语法树的检测原来，由于webshell和正常文件在语法结构上会有比较明显的出入，比如说一句话木马普遍流程就是传参然后执行命令，转化为语法结构上其实是比较单一的，正常文件的语法结构会比这复杂

ADog16K01](/news/5607)[#### 恶意样本家族分类实践

前记
最近有一个项目需求，需要将恶意样本的厂商描述给汇聚成一组统一的标签，然后后续需要对恶意样本的流量及行为进行特征提取和机器学习来实现恶意样本的检测。
简单点来讲所做的恶意样本家族分类其实就是一个数据清洗和打标签的过程。
数据样本量有90000多条，主要采集于virusshare，这里就以virustotal为例，实际效果其实是一样的
这里大概有大概几十家厂商，但是各家厂商的标签都不一样，甚至

ADog16K13](/news/5279)[#### 深度学习在恶意软件检测中的应用

事实证明，机器学习在网络和安全相关领域的应用非常有效。深度学习在语音识别、目标检测、自然语言处理等许多机器学习任务上的性能更佳。本文介绍深度学习在安全领域的一些应用。
Tobiyama提出一种基于进程行为进行恶意进程检测到方法，研究人员利用LSTM（Long Short-Term Memory，长短期记忆网络）进行特征提取，用CNN（Convolutional Neural Networks，卷积

angel01016K00](/news/2129)[#### 基于AST的Webshell检测

前言
想了好久的题目，不知道该用什么样的标题去吸引人，webshell的检测研究已经有很多文章披露了，在兜哥的机器学习书中也被反复作为案例提及，这里Webshell检测都是基于文件特征的，并不是基于流量特征的检测。
个人思考
在查阅了大量论文研究和实际案例后发现国内在webshell检测上的思路似乎没有什么新的突破，总结下来Webshell检测其实无外乎统计学检测、基于黑白名单的检测、基于opco

ADog15K05](/news/5461)[#### 基于机器学习的家用物联网设备DDoS检测

Rohan Doshi, Noah Apthorpe, Nick Feamster
Princeton University
来源：https://arxiv.org/abs/1804.04159
0x00 摘要
尽管越来越多的物联网（IoT）设备连接到互联网，但其中许多设备并不安全，进一步恶化了互联网环境。利用不安全的家用物联网设备，一些僵尸网络（如Mirai）对关键基础设施进行分布式拒绝服务

pingch15K20](/news/1969)