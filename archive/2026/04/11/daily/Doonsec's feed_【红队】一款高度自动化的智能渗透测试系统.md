---
title: 【红队】一款高度自动化的智能渗透测试系统
url: https://mp.weixin.qq.com/s/4bbwoKpsWimwBXkbtwgftQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:50.991282
---

# 【红队】一款高度自动化的智能渗透测试系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/k2PJfskYECmvfCF38rUWUEbKiaFjG0NtyMQdf5FMoiahnUV483bmhpJ45kvc0N3Ff0CQEYPVibGic68YXAmCZibdicxPpN8qemQDQL7KW2nKUtf8M/0?wx_fmt=jpeg)

# 【红队】一款高度自动化的智能渗透测试系统

vegetableou
vegetableou

贝雷帽SEC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/HVNK6rZ71oofHnCicjcYq2y5pSeBUgibJg8K4djZgn6iaWb6NGmqxIhX2oPlRmGe6Yk0xBODwnibFF8XCjxhEV3K7w/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

本公众号所提供的文字和信息仅供学习和研究使用，请读者自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具介绍**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

本项目旨在研发一款高度自动化的智能渗透测试系统，其核心目标是实现对安卓设备的无人值守安全评估。与传统的单一漏洞扫描工具不同，本系统是一个集成了情报收集、智能决策与多向量攻击能力的统一调度平台。它能够自动对目标网络进行深度探测，发现Web服务漏洞后，并非简单地给出报告，而是由系统内部的“决策引擎”智能选择最优攻击路径——或利用漏洞在可信服务器上部署陷阱，或通过社会工程学生成高仿真的钓鱼网站，最终目的都是自动化地将定制的诊断程序（伪装成正常应用的APK）投递至目标安卓设备。一旦设备运行该程序，系统便能即时建立远程连接，并自动完成一系列安全数据采集与风险评估任务。

**专业的Android自动化渗透测试与社会工程学攻击框架**

集成多种攻击链、智能决策引擎、一键Docker部署

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k2PJfskYECmDv2DMbbUO9DO39Giaqfrk9OCkbEibCbEM8zUa8iaEXlOaAgwA1PLw2bToeFqUr4cG2jPUCichbxsicP64m42H76gvFZH7LgRN0F3A/640?wx_fmt=png&from=appmsg)

### 集成工具

* metasploit Framework - 载荷生成与会话管理
* **Nmap**

  - 网络扫描与服务识别
* **SQLMap**

  - SQL注入自动化工具
* **ffuf**

  - Web目录爆破
* **Nuclei**

  - 漏洞模板扫描引擎
* **APKTool**

  - APK反编译与重打包
* **GoPhish**

  - 钓鱼邮件平台
* **Ngrok**

  - 内网穿透隧道

攻击链支持

1. **钓鱼攻击链**

   - 邮件钓鱼 → APK下载 → Meterpreter会话
2. **文件上传链**

   - 端点扫描 → 绕过上传 → WebShell/反弹Shell
3. **直接利用链**

   - 漏洞扫描 → CVE匹配 → Exploit执行
4. **SQL注入链**

   - 注入检测 → 数据库枚举 → 数据提取
5. **暴力破解链**

   - 服务识别 → 字典攻击 → 凭证获取

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具使用**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
前置要求Docker 20.10+ 和 Docker Compose 2.0+至少 4GB RAM 和 10GB 磁盘空间Linux/macOS/Windows (WSL2)
# 1. 克隆项目git clone https://github.com/your-repo/android-pentest-framework.gitcd android-pentest-framework
# 2. 配置环境变量cp .env.example .envnano .env  # 编辑配置文件
# 3. 一键启动chmod +x deploy.sh./deploy.sh start
# 4. 访问Web界面# 浏览器打开: http://localhost:5000
```

## 使用指南

### 1️⃣ 初始化配置

首次访问 http://localhost:5000，在首页配置：

* **LHOST**

  : 你的攻击机IP地址（目标设备能访问到的地址）
* **LPORT**

  : Meterpreter监听端口（默认4444）

点击"初始化控制器"按钮。

### 2️⃣ 目标扫描

进入 **目标扫描** 页面：

```
目标: 192.168.1.100
扫描类型: 综合扫描
```

点击 **一键扫描+智能决策**，系统将自动：

* 执行主机发现
* 服务指纹识别
* 漏洞扫描
* Web目录爆破
* 技术栈识别
* 推荐最优攻击链

### 3️⃣ 执行钓鱼攻击

进入 **钓鱼攻击** 页面：

**基础配置：**

* 攻击名称: `Android Security Update`
* 应用名称: `System Update`
* 隐身级别: `高`
* 架构: `ARM`

**高级选项（APK深度伪装）：**

* ✅ 启用apktool深度伪装
* 模板APK: 选择一个正常的APK文件
* 包名伪装: `com.google.android.gms`
* 应用名称: `Google Play Services`
* 自定义图标: 上传Google Play图标

**GoPhish集成：**

* ✅ 使用GoPhish发送钓鱼邮件
* 选择用户组、邮件模板、钓鱼页面

点击 **启动攻击**，系统将：

1. 生成伪装的恶意APK
2. 启动Meterpreter监听器
3. 启动Ngrok公网隧道
4. 启动文件分发服务器
5. （可选）通过GoPhish发送钓鱼邮件

### 4️⃣ 会话管理

目标安装APK后，进入 **会话管理** 页面：

* 查看所有活跃会话
* 执行Shell命令
* 运行Meterpreter模块
* 文件上传/下载
* 截屏、录音、定位

### 5️⃣ 文件上传攻击

进入 **文件上传攻击** 页面：

```
目标URL: http://target.com
架构: ARM
隐身级别: 中
```

点击 **扫描上传端点**，然后 **执行攻击**。

### 6️⃣ SQL注入攻击

进入 **SQL注入** 页面：

```
目标URL: http://target.com/page.php?id=1
请求方法: GET
```

点击 **检测注入点** → **枚举数据库** → **提取数据**。

**下载链接**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
项目地址：https://github.com/vegetableou/Intelligent-Android-Penetration-System
```

End

“点赞、在看与分享都是莫大的支持”

**工具精选**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

[【红队】一款安全测试工具集——Onyx](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494121&idx=1&sn=8675cf1677352620a57d68ff9f0b0686&scene=21#wechat_redirect)

[【红队】一款 AI 原生安全测试平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494139&idx=1&sn=5d8a98e0d0cb700c124aeaecae595d4c&scene=21#wechat_redirect)

[【红队】Webshell 管理与后渗透平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494098&idx=1&sn=cb7bc8f3cc7f59e6f80f4b56e7d4c1f9&scene=21#wechat_redirect)

[【红队】BProxy - 多级 SOCKS5 代理工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494084&idx=1&sn=dbc658a17e6ddc0dcd7c7857c841478a&scene=21#wechat_redirect)

[【红队】攻击面管理平台 (ASM)](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494076&idx=1&sn=e9c2ff60ccd065dc223c71042515268d&scene=21#wechat_redirect)

[【红队】ParrotOS 7.0 正式发布 代号：Echo](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494038&idx=1&sn=243e1105a439eb986fdc34534e6a8d19&scene=21#wechat_redirect)

[【红队】一款专为红队打造的主动资产指纹识别工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493898&idx=1&sn=3e395ade15061739c89f5d0a13645af4&scene=21#wechat_redirect)

[【蓝队】SamWaf开源轻量级网站防火墙](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493939&idx=1&sn=e56702a24dcae461024668aaea6aced3&scene=21#wechat_redirect)

[[蓝队] FastMonitor - 网络流量监控与威胁检测工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493925&idx=1&sn=a952c400c3ee63c8401ff57692745dd1&scene=21#wechat_redirect)

[【蓝队】漏洞全生命周期管理平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493803&idx=1&sn=10daa12b5a3523bf4a1ecc665890f917&scene=21#wechat_redirect)

[【蓝队】蓝队Ark神器 OpenArk v1.5.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493788&idx=1&sn=91a31e2d507cb9e0111c19dac98b315e&scene=21#wechat_redirect)

[【红队】矛·盾 武器库 v3.2](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493701&idx=2&sn=9cf7e304fee21328bac6d9bd97b81183&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/pM2klgicgT5dylTzXyrXBmex6dlAsZ0QJOQdzqcw2HpC49rnL0dTHNsWsOze4QmRYN7fPRoLdVK5MXs0DXtOvZw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

贝雷帽SEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

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