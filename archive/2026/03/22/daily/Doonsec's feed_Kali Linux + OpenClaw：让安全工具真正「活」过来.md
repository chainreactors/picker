---
title: Kali Linux + OpenClaw：让安全工具真正「活」过来
url: https://mp.weixin.qq.com/s/-Spq-8oBekwFgQ4jb06VpA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:19:51.625345
---

# Kali Linux + OpenClaw：让安全工具真正「活」过来

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2mDF1cR59TMiaLY0oFiaTRnLcHeGwVaiaqxYv3wpzZW62Picnyo6w4SKloTUL16sfabkCoxSCpMwKvPZeU1DoibBEjibsNGXl7nLKDac/0?wx_fmt=jpeg)

# Kali Linux + OpenClaw：让安全工具真正「活」过来

原创

xiejava
xiejava

fullbug

![]()

在小说阅读器中沉浸阅读

作为一个混迹安全圈多年的博主，我用过不少工具：Nmap 跑端口、Metasploit 打漏洞、Burp Suite 抓包... 但说真的，**命令行敲久了真的会腻**。

直到我给 Kali Linux 装上了一个 AI 大脑——**OpenClaw**。

今天不聊理论，直接上硬菜：**Kali + OpenClaw 能碰撞出什么火花？**

---

## 一、你还在手敲 Nmap 吗？

想象这样一个场景：

老板："把我们内网的资产理一下，明天汇报。"

你："好的... "（内心：一百多台机器，手动扫要到猴年马月？）

以前你可能这样：

```
nmap -sn 192.168.0.0/24 -oG - | grep "Up"
```

然后对着几十行 IP 地址开始手动整理，复制到 Excel，再一条条查端口...

**现在，你只需要说一句话：**

```
"帮我扫描 192.168.0.0/24 网段，把在线主机记录到飞书表格"
```

然后你就去泡咖啡了 ☕，OpenClaw 自动完成：

* ✅ 调用 Nmap 扫描
* ✅ 提取在线主机
* ✅ 写入飞书多维表格
* ✅ 标记新发现/离线设备

**3 分钟？你连咖啡还没泡好。**

---

## 二、OpenClaw 是什么？

简单说：**OpenClaw 是一个运行在本地的 AI 助手框架**，类似给电脑装了一个 ChatGPT，但它是**任务导向**的——不只会聊天，真的能帮你干活。

核心能力：

| 能力 | 说明 |
| --- | --- |
| 🤖 AI 对话 | 支持多种大模型（MiniMax、Claude 等） |
| 🔧 工具调用 | 可以调用系统命令、读写文件、操作飞书/邮件等 |
| 🔄 自动化 | 把重复工作编排成自动化流程 |
| 🧠 记忆 | 跨 Session 记住你的偏好和上下文 |

而它最让我惊喜的是：**它在 Kali 上简直是天作之合。**

---

## 三、Kali + OpenClaw = 安全研究员外挂

### 场景 1：一句话生成渗透测试报告

以前：

```
手动扫描 → 记录结果 → 整理报告 → 导出 PDF
一套流程下来 2 小时起步
```

现在：

```
"对 192.168.0.0/24 做一次安全评估，重点关注 Web 服务和开放端口"
```

OpenClaw 会：

1. 调用 Nmap 扫描端口
2. 使用 nikto 检测 Web 漏洞
3. 识别服务版本
4. **自动生成中文报告**
5. 推送到飞书/邮件

---

### 场景 2：社交工程自动化

```
"帮我收集 target.com 的子域名和邮箱"
```

OpenClaw 调用：

* `theHarvester`

  - 邮箱收集
* `amass`

  / `dig` - 子域名枚举
* `whois`

  - 注册信息

结果自动整理成表格。

---

### 场景 3：漏洞优先级排序

```
"扫描内网 Web 服务器，列出所有发现，按风险等级排序"
```

配合 `nmap --script vuln`，结果自动入库，飞书收到高危告警：

> 🔴 **高危**：192.168.0.50 - Apache Struts2 CVE-2023-xxxx
> 🟡 **中危**：192.168.0.101 - 心脏出血漏洞

---

## 四、安装与配置（手把手）

### 1. 安装 OpenClaw

```
# 一键安装（Linux/macOS）
curl -fsSL https://get.openclaw.ai | bash

# 启动网关
openclaw gateway start
```

### 2. 连接 Kali

OpenClaw 支持多种平台，在 Kali 上直接安装即可：

```
sudo apt install openclaw
openclaw config set channel feishu  # 对接飞书（可选）
```

### 3. 开始对话

```
openclaw chat
```

然后就像聊天一样指挥它干活。

---

## 五、实际效果展示

这是我今天的截图：

**Ask:** *“请对内网进行扫描，并将扫描结果发邮件给我”*

**OpenClaw 回复：**
如下图：

**![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2mAUuFLCu2vP5voHN1BaibhJ4YgzbHa1lPAkXAe2HlNGibrtDyic9deXvVv66SgTImdWSiau409v2ibAibgQp9ia5w3qkvLB2iaunn0XKM/640?wx_fmt=png&from=appmsg)**

---

**已经帮你分析好了，不是让你自己看数据。**

这是OpenClaw发的邮件的内容。

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2n4ygD58icY8fVK82Gicon7O3ljsFRDLvot37NRgic0icNRvJV3iaiaCTvbyiaIjiaaGe21B485W4T11HTOmQjHG7oXOZtC6vA5o5kDWYE/640?wx_fmt=png&from=appmsg)

## 也可以让OpenClaw将具体的数据整理到飞书多维表格了，当然也可以帮你写到数据库。

## ![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2mpl5ztc5XMVMUYAYrSKFzicNbAib60LjWn5eRDmGq2cvyhcAE0g3f6mBWk0HbcSIgk8SaVSTWBHdbL4gsZeXkvzZ69BcibJ0mars/640?wx_fmt=png&from=appmsg)

相关的skill已经写好放到了github上，可以让openclaw直接安装
github地址：

https://github.com/xiejava1018/myopenclaw-skills/tree/master/network-scan

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2kc108PXFIgRxv8OYUZddzwSxmCQiaTYt4WbXBahnicb3VPNYoCbXnicwH9bGINiacticZqtxBdDjC6FPImHEW6CUJLmW48cAbSSsHc/640?wx_fmt=png&from=appmsg)

## 六、适合人群

| 群体 | 为什么需要 |
| --- | --- |
| 🔒 安全研究员 | 自动化渗透测试流程，省时省力 |
| 🏢 企业安全团队 | 资产管理、巡检报告、告警响应 |
| 🎓 CTF 选手 | 快速信息收集、漏洞验证 |
| 👨‍💻 运维工程师 | 基线检查、合规扫描 |

---

## 七、局限性与注意事项

说实话，不能光吹不黑：

1. **AI 会出错：模型可能误判漏洞风险，需要人工复核**
2. **工具依赖：OpenClaw 本身不创造工具，得 Kali 有的它才能用**
3. **安全边界：处理敏感数据时注意脱敏，不要把密码交给 AI**
4. **授权原则：扫描需授权，不要动别人的系统**

---

## 结语

Kali 是安全研究员的瑞士军刀，OpenClaw 则是它的**智能引擎**。

以前我们说"工具是死的，人是活的"——现在 AI 时代，这句话该改改了：**工具 + AI = 你多了个 24 小时不睡觉的安全助手。**

如果你也想让 Kali 开口说话，也可以像我一样给他装上OpenClaw随时召唤它干活。

---

**彩蛋**：博主已经用这套组合管理内网资产 1个月，巡检效率提升 **80%**，报告生成从 2 小时压缩到 **5 分钟**。真香定律，亲测有效。

---

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6cNzMD9ovmPQDhxzubx0Hbicg3tUKoQSdEX1ZsXHCL3QBrKaPlbvPK0boZA7WH0KJrxWWUsDAwq7GJOfF0lBq1Q/0?wx_fmt=png)

fullbug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6cNzMD9ovmPQDhxzubx0Hbicg3tUKoQSdEX1ZsXHCL3QBrKaPlbvPK0boZA7WH0KJrxWWUsDAwq7GJOfF0lBq1Q/0?wx_fmt=png)

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