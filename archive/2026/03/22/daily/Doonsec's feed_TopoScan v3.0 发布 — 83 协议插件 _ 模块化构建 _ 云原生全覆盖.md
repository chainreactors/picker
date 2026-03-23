---
title: TopoScan v3.0 发布 — 83 协议插件 / 模块化构建 / 云原生全覆盖
url: https://mp.weixin.qq.com/s/l5TdyHbqsyvatOc-TU4CCA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:23:12.972511
---

# TopoScan v3.0 发布 — 83 协议插件 / 模块化构建 / 云原生全覆盖

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/op0UsH3vuJ30BNHibT3ibfUDRUd5B6CScK4IlZJrHvQ7mtUwoVsO50z7VLWQwVrltIeQBxRFsUQvicHayQ3sQkD1tQt6KJSibs2RuOtU5Bw0we8/0?wx_fmt=jpeg)

# TopoScan v3.0 发布 — 83 协议插件 / 模块化构建 / 云原生全覆盖

原创

meeyou
meeyou

three安全之路

![]()

在小说阅读器中沉浸阅读

本公众号（three安全之路）所发布的技术文章、工具及研究内容均仅供参考，所提供的信息仅面向网络安全从业者、授权安全测试人员，用于其负责的网络资产、信息系统及相关设备的安全防护工作。任何使用者利用本公众号提供的技术信息、工具或方案，所造成的直接或间接后果、经济损失及法律责任，均由使用者本人自行承担，本公众号及作者不承担任何连带责任。

##

|  |  |
| --- | --- |
|  | **前言** |

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/op0UsH3vuJ00Cvt6ef7ic1Qibq71BZ5iceI0oCGImgh0vAoOcyL21icLQg26H90lxwZ2ZtBp1qVcwoszJYgh2XHcMVr6ddpf681bB1BibDIgbINc/640?wx_fmt=png&from=appmsg)

距离上次 v1.2 发布已经过了一段时间。这段时间里我们对 TopoScan 做了大量工作 —— 从 46 个协议插件扩展到 **83 个**，新增 **37 个插件**，修复了 **64 个 Bug**，重写了构建体系。

v3.0 不是小版本迭代，而是从扫描能力、代码质量到工程化全面升级的大版本。下面逐一说明。

---

|  |  |
| --- | --- |
| **1** | **扫描能力：从 46 到 83 个插件** |

### **1.1 Web 安全扫描 (+12)**

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ1EvcG1TpvV7yic2HVndIHkFhW4Ll1ib40VnyfE2TuhibmcGjn532vFhje5nibaMDqFbtTJia7O1coib4rktwyc4MhSR2XOtWic3HXV10/640?wx_fmt=png&from=appmsg)

###

### **1.2 Active Directory 攻击 (+6)**

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ0CMZn67Gr6YNMIsVNbXgM7KGPdhaMpGfel7hepTXJIUX6CNl0WEjWrXH1uJN2YibtaMBHudibklygtLjvB5IaCMhy1OKNENmmz4/640?wx_fmt=png&from=appmsg)

### **1.3 认证攻击 (+2)**

* **Pass-the-Hash**: NTLM 哈希传递，无需明文密码
* **密码喷洒 (Password Spray)**: 跨协议密码喷洒 — SMB/SSH/RDP/WinRM/LDAP/MSSQL/MySQL/FTP

### **1.4 网络与基础设施 (+5)**

* Docker Remote API 未授权访问 (2375/2376)
* NFS 共享枚举
* DNS 域传送检测 (AXFR)
* IPMI 哈希泄露 (CVE-2013-4786)
* LLMNR/NBT-NS 名称解析投毒检测

### **1.5 云原生与中间件 (+6，v3.0 新增)**

这是 v3.0 的重点方向之一 —— 覆盖主流云原生和中间件组件：

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ0j2Fr2jcHd1OazAUa6j9xLVric4NpSgOUyKsavCD8mWKYW4b373jGh2Z5iaJtw3NN3Tohoogj4iaHBEdIkxSicC2EaVIiblmicHib4AY/640?wx_fmt=png&from=appmsg)

### **1.6 物联网与消息协议 (+3，v3.0 新增）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/op0UsH3vuJ2ibbl2h0SGqJHnRxshL7Jysjen9fwoSNVCMPXCQbibtT0h3vcyQJhCDTuG6xZbQKktThexWTkTpcs1ZRY1NuQWaG52MY2ECJrNw/640?wx_fmt=png&from=appmsg)

###

### **1.7 其他新增**

* **WebSocket 端点探测**: RFC 6455 握手验证 + Socket.IO/SignalR/SockJS 等框架检测
* **NTLM 信息泄露**: 从 NTLM 认证响应提取域名、主机名、OS 版本
* **TLS 证书信息提取**: 证书主体、SAN、有效期、颁发者
* **打印机自动跳过**: 识别打印机设备（端口 9100/515/631 + Banner 指纹 + MAC 厂商），自动跳过扫描避免中断打印服务

---

|  |  |
| --- | --- |
| **2** | **已有插件增强** |

不只是加新插件，我们对多个已有插件做了深度增强：

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ3BI8ayoib2RzjaZ1gBAtxgj3lVCicWcLk9862Y1CTcv5I8c25GTp61oae1T2oaAQiaPCtRVU7ZFAjlF7wYLmbTkJ1d0ODbsm1GGU/640?wx_fmt=png&from=appmsg)

---

|  |  |
| --- | --- |
| **3** | **扫描引擎增强** |

### **3.0 隐蔽扫描**

实战中经常遇到 IDS/WAF 检测的问题。v3.0 提供了完整的隐蔽扫描支持：

```
# stealth 预设 — 一键低冲击配置
toposcan -h192.168.1.0/24 -preset stealth

# 精细控制
toposcan -h192.168.1.0/24 -rate100-jitter200-host-rate5
```

* `-host-rate`: 单主机最大并发数（防止触发目标告警）
* `-preset stealth`: 低线程 + 限速 + 随机抖动 + 单主机限制
* 默认线程从 600 降到 200

### **3.2 UDP 协议探测 (v3.0 新增)**

新增 NTP/SSDP/mDNS 协议特定探测，不再是简单的 UDP 端口扫描：

```
toposcan -h192.168.1.0/24 -sU-pu123      # NTP
toposcan -h192.168.1.0/24 -sU-pu1900     # SSDP/UPnP
toposcan -h192.168.1.0/24 -sU-pu5353     # mDNS
```

### **3.3 断点续扫 + 优雅中断**

* `-resume`: 保存/恢复扫描进度
* 第一次 Ctrl+C 保存进度，第二次强制退出
* 适合大规模扫描中断后继续

### **3.4 网络保护**

* 代理环境主机发现误报自动修复
* 本地 IP 自动排除
* 漏洞扫描限速（防止 POC 打挂服务）
* **打印机自动跳过** — 识别到打印机后自动跳过爆破和 POC，避免触发打印

### **3.5 其他**

* `-source-ip`: 源 IP 绑定（多网卡环境指定出口）
* `-fpfile`: 自定义 YAML 指纹文件导入
* `-ef`: 从文件读取排除的 IP/CIDR（适合大规模扫描排除敏感资产）

---

|  |  |
| --- | --- |
| **4** | **场景预设** |

v1.2 有 3 个预设 (quick/full/pentest)，v3.0扩展到 **8 个**：

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ0yLKgCaSlq1t6H2eVsibmW8wGd7mfuluqqfpibqtBSwI3iayvichufuEoxpZicsmWicrIqh13ricH2ibyiavvotekLKTsIibVDCdLgLuQ4s/640?wx_fmt=png&from=appmsg)

```
# AD 域渗透
toposcan -h10.0.0.0/24 -preset ad -domain corp.local

# IoT 设备扫描
toposcan -h192.168.0.0/16 -preset iot

# 云原生基础设施评估
toposcan -h10.0.0.0/24 -preset infra
```

---

|  |  |
| --- | --- |
| **5** | **模块化构建** |

这是 v3.0在工程化方面的重要改进。

### **5.1 三种发布版本**

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ3K8IZy076ht2cwHwWDNAwnrbaEpCMm3JGOz8kcpJ8Inp7dBwkupm4eNia4oJkjmY3esOlfTW7pBQaSleGspkAiapkGhL0FxFvCo/640?wx_fmt=png&from=appmsg)

### **5.2 模块化裁剪**

引入 11 个 `no_*` 排除标签，可以按需裁剪：

```
# 不需要 AD 攻击和邮件插件？排除掉
go build -tags"no_ad,no_mail"-o toposcan_custom.exe .

# 极致精简 — 排除全部可选模块
go build -tags"no_sqlite,no_tui,no_excel,no_screenshot,no_report,no_license,no_ad,no_webext,no_extradb,no_mail,no_misc" \
  -trimpath-ldflags"-s -w"-o toposcan_mini.exe .
```

插件模块划分：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/op0UsH3vuJ29PNP6Wn68TEhicjh6eWPBl8aa2AsH074Med0psnvFibXExOSkjoT48kZQ3oPbA49DwarU96kuj9XQ3l7yiaK3hU48cDQScEX2NM/640?wx_fmt=png&from=appmsg)

### **5.3 交叉编译**

支持 Windows/Linux/macOS 一键交叉编译：

```
make all       # 构建 3 平台 × 3 版本 = 9 个二进制
make linux     # 仅 Linux
make lite      # 仅精简版 (3 平台)
```

---

|  |  |
| --- | --- |
| 6 | **稳定性：64 个 Bug 修复** |

代码质量是这个版本投入最多精力的地方之一：

### **6.1 并发安全 (8 项)**

* 修复 `OutputMutex` 死锁（关键修复）
* 修复 ICMP 模块竞态
* 修复多处 `atomic` 混合访问

### **6.2 插件 Bug (25 项)**

* 修复 25 个插件的 `break`/`select` 并发 Bug
* 修复 MS17010 并发数据竞争
* 修复 Redis 全局状态污染
* 修复 8 处 HTTP 响应体未关闭导致的连接泄漏

### **6.3 代码质量**

* **31 项**`go vet` 警告清零
* **15 个**无用函数移除
* **5 组**重复函数合并
* **32 个**单元测试

---

|  |  |
| --- | --- |
| **7** | **新增参数汇总** |

![](https://mmbiz.qpic.cn/mmbiz_png/op0UsH3vuJ0MZIicYmIaqUqLku0fR1JHsvMAHa2qaapFBzrAd823yPzWS7PMaDONRXh7TlibEjYQLJtNVwrVISs8GYeEh9Iib9OZRtkeybbXb0/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **8** | **升级说明** |

v3.0 完全向后兼容 v1.2 的所有命令行参数。直接替换二进制文件即可升级。

```
# 和以前一样用
toposcan -h192.168.1.0/24

# 试试新功能
toposcan -h192.168.1.0/24 -preset stealth              # 隐蔽扫描
toposcan -h192.168.1.0/24 -m pth -hash <NTLM>          # Pass-the-Hash
toposcan -h192.168.1.0/24 -m spray                      # 密码喷洒
toposcan -h192.168.1.0/24 -webpath                      # 敏感路径
toposcan -h192.168.1.0/24 -preset ad -domain corp.local # AD 域评估
toposcan -h10.0.0.0/24 -m kubernetes,mqtt,couchdb       # 云原生
toposcan -h192.168.1.0/24 -ef exclude.txt               # 排除敏感 IP
```

---

|  |  |
| --- | --- |
| **9** | **后续计划** |

* 更多协议插件持续扩展
* 性能优化与大规模网络场景支持
* 社区反馈的 Bug 修复和功能需求

更多功能详情请参考 TopoScanV3.0 使用说明书，公众号后台回复“toposcan”即可获取工具下载链接，可加入群聊探讨功能

---

*TopoScan v3.0| 83 协议插件 | 模块化构建 | 3 平台交叉编译*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/a0a57o0RVEalyLvktrfycvia9iahgHmHJsOp1d9iaicZ1tRYM5fL5RiclgBEztK88zfvAeVvcWSsLlZiagIGNZXjHgjA/0?wx_fmt=png)

three安全之路

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/a0a57o0RVEalyLvktrfycvia9iahgHmHJsOp1d9iaicZ1tRYM5fL5RiclgBEztK88zfvAeVvcWSsLlZiagIGNZXjHgjA/0?wx_fmt=png)

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