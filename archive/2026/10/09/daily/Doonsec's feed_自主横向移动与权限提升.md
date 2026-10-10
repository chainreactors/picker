---
title: 自主横向移动与权限提升
url: https://mp.weixin.qq.com/s/qxSo2uo8INuk6Hd8yMZbzw
source: Doonsec's feed
date: 2026-10-09
fetch_date: 2026-10-10T07:55:50.992767
---

# 自主横向移动与权限提升

# 自主横向移动与权限提升

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 目录

1. 引言
2. 能力建模
3. 网络拓扑感知与路径规划
4. 自主凭据收集与利用
5. 权限提升决策树
6. 隐蔽性分析
7. 对抗性评估环境
8. 评估框架
9. 前沿挑战
10. 参考文献

---

## 1. 引言

横向移动与权限提升是 MITRE ATT&CK 框架的核心战术。AI 自主完成这些能力直接关系到其作为攻击工具的危害评估与作为红队工具的效用评估。

**核心问题**：给定初始立足点，AI 能否自主规划并执行从初始访问到域控的完整路径？

---

## 2. 能力建模

### 2.1 自主渗透能力形式化

**定义 2.1（自主渗透能力）**：AI Agent  的渗透能力建模为元组 ：

* ：感知能力（网络枚举、服务识别、漏洞扫描）
* ：利用能力（漏洞利用、凭据利用、配置滥用）
* ：决策能力（路径规划、技术选择、风险评估）
* ：适应能力（失败恢复、环境变化适应）

### 2.2 ATT&CK 战术映射

| ATT&CK 战术 | AI 自主能力 | 技术示例 |
| --- | --- | --- |
| 初始访问 | 钓鱼生成、漏洞利用 | LLM 生成钓鱼邮件 |
| 侦察 | 自动枚举、OSINT | 网络扫描、AD 枚举 |
| 横向移动 | 路径规划、凭据利用 | Pass-the-Hash、RDP |
| 权限提升 | 提权决策、漏洞利用 | Kerberoasting、CVE 利用 |
| 防御规避 | 告警规避、日志清理 | 加密通信、进程注入 |
| 持久化 | 自动化后门 | 计划任务、服务安装 |
| 数据外传 | 数据发现、通道建立 | C2 通信、数据压缩 |

---

## 3. 网络拓扑感知与路径规划

### 3.1 自主网络枚举

```
enumerate_network(current_host):
  1. 本地信息收集:
     - ipconfig / ifconfig
     - arp -a
     - netstat -rn
     - 域信息: whoami /groups, net group

  2. 网络发现:
     - ping sweep: nmap -sn subnet
     - 端口扫描: nmap -sV target
     - 服务识别: banner grabbing

  3. Active Directory 枚举:
     - BloodHound 数据收集
     - 用户/组/计算机枚举
     - GPO/OUS 枚举

  4. 构建拓扑图:
     G = (hosts, connections, trust_relations)
```

### 3.2 BloodHound 路径分析

**攻击路径图**：有向图 ：

* ：节点（用户、计算机、组、域）
* ：边（AdminTo、HasSession、MemberOf、GenericAll 等）

**最短攻击路径**：

**AI 增强**：LLM 分析 BloodHound 图，识别非 obvious 路径：

```
prompt: "Given the BloodHound graph, identify attack paths
         from user U to Domain Admin that may be overlooked
         by standard shortest-path analysis.
         Graph: {nodes, edges}
         Consider: ACL abuse, trust relationships,
         constrained delegation, resource-based
         constrained delegation."
```

### 3.3 路径规划算法

**A* 搜索*\*：启发式搜索攻击路径：

* ：从起点到节点  的实际成本（已执行步骤数）
* ：从  到目标的启发式估计（到 DA 的估计距离）

**启发式设计**：

* if  is Domain Admin
* if  has AdminTo to DA's computer
* if  has session on DA's computer
* if no known path

**AI 增强启发式**：LLM 基于经验估计节点到目标的距离，考虑非标准路径。

---

## 4. 自主凭据收集与利用

### 4.1 凭据收集

| 来源 | 技术 | AI 角色 |
| --- | --- | --- |
| 内存 | LSASS dump (Mimikatz) | 判断何时/如何 dump |
| 文件 | 配置文件、.ssh、.aws | 自动搜索并解析 |
| 注册表 | 存储的凭据 | 自动提取 |
| LSASS | Pass-the-Hash | 选择目标与服务 |
| Kerberos | Kerberoasting / AS-REP roasting | 识别可利用账户 |
| NTDS | DCSync | 判断权限是否足够 |
| 浏览器 | 存储的密码/Cookie | 自动提取 |
| 环境变量 | API keys、tokens | 自动搜索 |

### 4.2 凭据利用决策

**决策树**：

```
have_credential(cred):
```

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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