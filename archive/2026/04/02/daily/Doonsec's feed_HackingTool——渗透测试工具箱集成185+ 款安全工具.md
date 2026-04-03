---
title: HackingTool——渗透测试工具箱集成185+ 款安全工具
url: https://mp.weixin.qq.com/s/RXN1jmNqE2f87HG56MGM_Q
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:23:01.301778
---

# HackingTool——渗透测试工具箱集成185+ 款安全工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qqiaD4wiajgFzxeOQltecYOsMarXkVaBoYpyuk3wOlEcMCMUwJ8WJ5X7vysrLCcicYqmMv9EEtEuicgibfE78Ffl2Ruiby9pUlIpDvEex2PMA9o8g/0?wx_fmt=jpeg)

# HackingTool——渗透测试工具箱集成185+ 款安全工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

**项目地址**

https://github.com/Z4nzu/hackingtool

**HackingTool** 是开源一体化渗透测试工具集合，旨在为安全研究人员和渗透测试人员提供便捷的工具管理界面。该项目使用 Python 3.10+ 开发，集成了 **185+ 款安全工具**，涵盖信息收集、漏洞扫描、无线攻击、社会工程学等 20 个主要类别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwQoRuAbj8b4wRKx3mfy5ksPgRchE158lcIQ6j4v8uuchWe6LdZsUHhYEbCeZwCYHFU5q3kWiakT6biaiaTqH4zQBlsG8CnLvOoKw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFxZRA8Y4kLEsoM7wYxyj617dw5YdK6rXIGXnyDwj7VeG2oibCn6D5c3wQU06szOds1ewaOxHg5Hice1uxk88oA1AqUwWMQ9ce4Gw/640?wx_fmt=png&from=appmsg)

> ⚠️ **法律声明**：本工具仅适用于授权的安全测试、渗透测试研究和教育目的。未经授权使用可能违反当地法律法规。

---

## 核心特性 (v2.0.0)

表格

| 特性 | 说明 |
| --- | --- |
| **Python 3.10+** | 全面移除 Python 2 代码，采用现代语法 |
| **智能菜单系统** | 自动识别操作系统，隐藏不兼容的工具 |
| **工具搜索** | 按 `/` 键通过名称、描述或关键词搜索工具 |
| **标签过滤** | 按 `t` 键通过 19 个标签（osint, web, c2, cloud 等）筛选 |
| **智能推荐** | 按 `r` 键输入需求，获取推荐工具 |
| **安装状态追踪** | 每个工具旁显示 ✔/✘ 安装状态 |
| **批量安装** | 选项 `97` 支持一键安装整个类别 |
| **智能更新** | 自动检测 git pull / pip upgrade / go install 更新方式 |
| **Docker 支持** | 本地构建，无需依赖外部镜像 |
| **一键安装** | `curl` 单命令完成全部安装 |

---

## 系统架构

### 技术栈

* **编程语言**: Python 3.10+
* **依赖管理**: pip + requirements.txt
* **容器化**: Docker & Docker Compose
* **支持平台**: Linux (主要), macOS (部分工具)

### 目录结构

```
hackingtool/
├── tools/              # 各类工具模块
│   ├── anonymoussurf.py
│   ├── information_gathering.py
│   ├── wordlist.py
│   ├── wireless.py
│   ├── sql_injection.py
│   ├── phishing.py
│   ├── webattack.py
│   ├── postexploitation.py
│   ├── forensic.py
│   ├── payload.py
│   ├── exploit_framework.py
│   ├── reverse_engineering.py
│   ├── ddos.py
│   ├── rat.py
│   ├── xss.py
│   ├── steganography.py
│   ├── active_directory.py
│   ├── cloud.py
│   ├── mobile.py
│   └── others.py
├── install.py          # 手动安装脚本
├── install.sh          # 一键安装脚本
├── requirements.txt    # Python 依赖
├── Dockerfile          # Docker 构建
├── docker-compose.yml  # Docker Compose 配置
└── hackingtool.py      # 主入口程序
```

---

## 工具分类详解

### 1. 🛡 匿名隐藏 (Anonymously Hiding)

表格

| 工具 | 功能描述 |
| --- | --- |
| Anonymously Surf | 匿名浏览工具 |
| Multitor | 多 Tor 实例管理 |

### 2. 🔍 信息收集 (Information Gathering) - 26 款工具

**核心工具**：

* **nmap** - 网络端口扫描器
* **theHarvester** ★ - 子域名和邮箱收集
* **Amass** ★ - 深度子域名枚举
* **Shodanfy** - Shodan 搜索引擎集成
* **SpiderFoot** ★ - 自动化 OSINT 框架
* **TruffleHog** ★ - Git 仓库敏感信息扫描
* **Gitleaks** ★ - 检测 Git 历史中的密钥泄露

### 3. 📚 密码字典生成 (Wordlist Generator)

* **Cupp** - 自定义用户画像字典生成
* **Hashcat** ★ - GPU 加速密码破解
* **John the Ripper** ★ - 经典密码破解工具

### 4. 📶 无线攻击 (Wireless Attack) - 13 款工具

* **Aircrack-ng 套件** (Airgeddon, Wifite, Wifiphisher)
* **Fluxion** - WiFi 钓鱼攻击框架
* **Bettercap** ★ - 现代网络攻击与监控框架

### 5. 🧩 SQL 注入 (SQL Injection)

* **Sqlmap** - 自动化 SQL 注入与数据库接管
* **NoSqlMap** - NoSQL 注入测试

### 6. 🎣 钓鱼攻击 (Phishing Attack) - 17 款工具

* **SocialFish** - 社交媒体钓鱼框架
* **Evilginx3** ★ - 中间人钓鱼攻击框架
* **Gophish** 替代方案
* **QR Code Jacking** - QR 码劫持攻击

### 7. 🌐 Web 攻击 (Web Attack) - 20 款工具

**现代 Web 安全工具集**：

* **Nuclei** ★ - 基于模板的快速漏洞扫描器
* **ffuf** ★ - 高速 Web Fuzzer
* **Feroxbuster** ★ - 递归内容发现工具
* **OWASP ZAP** ★ - 综合 Web 应用安全扫描器
* **Katana** ★ - 下一代爬虫框架
* **Caido** ★ - 轻量级 Web 代理工具

### 8. 🔧 后渗透 (Post Exploitation) - 10 款工具

* **pwncat-cs** ★ - 升级版 Netcat
* **Sliver** ★ - 跨平台 C2 框架
* **Havoc** ★ - 现代 C2 框架
* **PEASS-ng** ★ - 权限提升脚本套件
* **Ligolo-ng** ★ - 高级隧道工具
* **Chisel** ★ - 快速 TCP/UDP 隧道
* **Evil-WinRM** ★ - Windows 远程管理利用
* **Mythic** ★ - 跨平台红队协作框架

### 9. 🕵 取证分析 (Forensics) - 8 款工具

* **Autopsy** - 数字取证平台
* **Volatility 3** ★ - 内存取证框架
* **Wireshark** - 网络协议分析
* **Binwalk** ★ - 固件分析工具

### 10. 📦 载荷生成 (Payload Creation)

* **The FatRat** - 绕过 AV 的载荷生成器
* **MSFvenom Payload Creator** - Metasploit 载荷封装

### 11. 🧰 漏洞利用框架 (Exploit Framework)

* **RouterSploit** - 路由器漏洞利用
* **WebSploit** - Web 漏洞测试框架

### 12. 🔁 逆向工程 (Reverse Engineering)

* **Ghidra** ★ - NSA 开源逆向工程套件
* **Radare2** ★ - 高级逆向工程框架
* **JadX** - Android APK 反编译

### 13. ⚡ DDoS 攻击 (DDOS Attack)

* **SlowLoris** - 低速 HTTP DoS
* **GoldenEye** - HTTP 压力测试

### 14. 🖥 远程管理工具 (RAT)

* **Pyshell** - Python 远程 Shell

### 15. 💥 XSS 攻击 (XSS Attack) - 9 款工具

* **DalFox** ★ - 现代 XSS 扫描器
* **XSStrike** - 高级 XSS 检测

### 16. 🖼 隐写术 (Steganography)

* **Steganography** - 图像隐写工具

### 17. 🏢 活动目录 (Active Directory) - 6 款工具 ⭐新增

* **BloodHound** ★ - AD 关系可视化与攻击路径分析
* **NetExec (nxc)** ★ - 自动化 AD 评估
* **Impacket** ★ - Python AD 协议套件
* **Responder** ★ - LLMNR/NBT-NS/mDNS 投毒
* **Certipy** ★ - AD CS 攻击工具
* **Kerbrute** ★ - Kerberos 暴力破解

### 18. ☁ 云安全 (Cloud Security) - 4 款工具 ⭐新增

* **Prowler** ★ - AWS/GCP/Azure 安全审计
* **ScoutSuite** ★ - 多云安全态势评估
* **Pacu** ★ - AWS 漏洞利用框架
* **Trivy** ★ - 容器与代码漏洞扫描

### 19. 📱 移动安全 (Mobile Security) - 3 款工具 ⭐新增

* **MobSF** ★ - 移动安全测试框架
* **Frida** ★ - 动态代码插桩工具
* **Objection** ★ - 运行时移动探索

### 20. ✨ 其他工具 (Other Tools) - 24 款

* 社交媒体暴力破解
* Android 黑客工具
* IDN 同形异义攻击 (EvilURL)
* 哈希破解 (Hash Buster)
* WiFi 去认证攻击等

---

## 安装指南

### 方法一：一键安装（推荐）

```
curl -sSL https://raw.githubusercontent.com/Z4nzu/hackingtool/master/install.sh | sudo bash
```

此命令自动完成：

* 系统依赖安装
* 仓库克隆
* Python 虚拟环境配置
* 启动器安装

### 方法二：手动安装

```
# 克隆仓库
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool

# 安装依赖
sudo pip3 install-r requirements.txt

# 运行安装脚本
sudo python3 install.py

# 启动工具
hackingtool
```

### 方法三：Docker 部署

```
# 构建镜像
docker build -t hackingtool .

# 直接运行
docker run -it--rm hackingtool

# 或使用 Docker Compose（推荐）
docker compose up -d
dockerexec-it hackingtool bash

# 开发模式（挂载本地源码）
docker compose --profile dev up
dockerexec-it hackingtool-dev bash

# 停止并清理
docker compose down -v
```

---

## 系统要求

表格

| 依赖 | 版本 | 用途 |
| --- | --- | --- |
| Python | 3.10+ | 核心运行环境 |
| Go | 1.21+ | 现代 Go 工具（nuclei, ffuf, amass 等） |
| Ruby | any | haiti, evil-winrm |
| Docker | any | Mythic, MobSF（可选） |

### Python 依赖

```
# requirements.txt 示例
requests
colorama
pyfiglet
# ... 其他依赖
```

---

## 使用指南

### 快速命令参考

表格

| 命令 | 功能 | 适用场景 |
| --- | --- | --- |
| `/query` | 搜索工具 | 主菜单 |
| `t` | 标签筛选 | 主菜单 |
| `r` | 智能推荐 | 主菜单 |
| `?` | 帮助 | 任意位置 |
| `q` | 退出 | 任意位置 |
| `97` | 批量安装 | 分类菜单 |
| `99` | 返回上级 | 任意位置 |

### 典型工作流程

1. **信息收集阶段**

   **主菜单 → 2 (Information Gathering) → 选择 theHarvester/Amass**

1. **Web 漏洞扫描**

   ```
    主菜单 → 7 (Web Attack) → 选择 Nuclei/ffuf
   ```
2. **AD 渗透测试**

   **主菜单 → 17 (Active Directory) → BloodHound → NetExec**
3. **后渗透阶段**

   **主菜单 → 8 (Post Exploitation) → Ligolo-ng 建立隧道**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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