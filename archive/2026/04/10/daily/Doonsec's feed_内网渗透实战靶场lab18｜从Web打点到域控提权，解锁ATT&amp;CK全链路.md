---
title: 内网渗透实战靶场lab18｜从Web打点到域控提权，解锁ATT&amp;CK全链路
url: https://mp.weixin.qq.com/s/7HzCV7YnDXhK8tpEYyaF2Q
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:15:34.515602
---

# 内网渗透实战靶场lab18｜从Web打点到域控提权，解锁ATT&amp;CK全链路

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/aOXddd8LbRDLwWLF3KUREclicVFNciawYSh4D3o9qbYAYYWaib2ibwtHmX4Xvsa2t33lPNJbtV9eR8nvTmORicx9H35xPULrK4nyrribKibvkXtP0U/0?wx_fmt=jpeg)

# 内网渗透实战靶场lab18｜从Web打点到域控提权，解锁ATT&CK全链路

cslab
cslab

红蓝公鸡队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **真实企业内网模拟 | 10+ 核心攻防技术 | 挑战红队完整杀伤链**

## 🚨 为什么你需要一个真正的内网靶场？

在真实的网络攻防中，**外网突破只是开始，内网横向与提权才是决定成败的关键**。
你是否遇到过以下困境：

* 只会单个漏洞利用，却不懂内网**资产识别**与**信息收集**？
* 拿到WebShell后无从下手，无法进行**UDF提权**或**权限控制**？
* 对**ATT&CK**框架停留在理论，缺乏实战映射环境？

**我们为你打造了一个高度仿真的内网渗透靶场** —— 从Web打点出发，经历RCE、WebShell控制、数据库提权、权限维持，最终拿下内网核心权限。全流程覆盖红队实战技术点。

## 🎯 靶场核心知识点

你将在这个内网环境中亲手操作以下技术模块：

| 阶段 | 技术点 | 实战内容 |
| --- | --- | --- |
| **入口突破** | Web打点 · 资产识别 | 发现暴露的Web应用，指纹识别，寻找脆弱点 |
| **权限获取** | RCE执行 · WebShell控制 | 利用命令注入/反序列化漏洞，上传冰蝎/蚁剑WebShell |
| **信息收集** | 内网扫描 · 服务探测 | 收集主机信息、网络拓扑、敏感配置 |
| **权限提升** | UDF提权 · 权限控制 | MySQL数据库提权，Windows/Linux权限提升 |
| **纵深控制** | 权限维持 · ATT&CK映射 | 创建后门，横向移动，域权限劫持 |

### 🔍 详细技术点拆解

* **Web打点**：SQL注入、文件上传、XXE、SSRF等多入口选择
* **资产识别**：Nmap/Masscan探测内网存活主机、开放端口、服务版本
* **RCE执行**：Struts2、Log4j、ThinkPHP等经典RCE漏洞复现
* **WebShell控制**：流量加密、免杀绕过、内网代理建立
* **UDF提权**：MySQL导出自定义函数，获取系统权限
* **权限控制**：SeBackupPrivilege、SeImpersonate等令牌利用
* **ATT&CK**：覆盖侦察、初始访问、执行、提权、防御绕过、横向移动等12个战术
* **信息收集**：域控定位、用户Hash抓取、Kerberos攻击

## ⚔️ 靶场亮点

✅ **全流程真实模拟** – 从外网暴露点到内网核心，无剧本自由渗透
✅ **多漏洞组合** – 每个靶标至少2~3种利用路径，拒绝死板
✅ **UDF提权专训** – 独立数据库靶机，完整演练MySQL提权技巧
✅ **ATT&CK映射指南** – 每完成一个动作，自动关联MITRE战术编号
✅ **安全沙盒环境** – 隔离部署，支持回滚，随时重置靶机状态
✅ **分步Hint与Writeup** – 新手可看提示，高手直接挑战0辅助

## 🧑‍💻 适合人群

* **渗透测试工程师** – 提升内网实战能力，应对复杂网络环境
* **红队成员** – 演练ATT&CK攻击链路，优化技战术
* **安全专业学生** – 从理论到实战，构建完整的渗透测试知识体系
* **CTF选手** – 突破单一题目限制，体验真实内网攻防
* **企业蓝队** – 用于内部攻防演练，评估防御能力

## 🚀 如何加入靶场？

**在线体验**
👉 点击立即注册，开启你的内网渗透挑战
（周末限时免费）

## 🏁 你的第一个目标

> 已知目标对外开启Web服务，IP段为 `192.168.50.0/24`。
> 请尝试：
>
> 1. 发现Web漏洞，获取初始WebShell
> 2. 对内网进行资产识别，找到数据库服务器
> 3. 利用UDF提权获得系统权限
> 4. 最终控制域控制器并读取flag

## ⚠️ 注意事项

* 靶场仅用于合法安全学习，禁止用于非法攻击
* 所有操作均在隔离环境中进行，不影响真实网络

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibibMpt3IV0Cy5zapTWx0QLTY2mSE1nhWutM7SNNrCJ6mfk84ibPedvuvT8gGu1aQGicUbhQrFvlzNXd2Yav8TWkZA/0?wx_fmt=png)

红蓝公鸡队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibibMpt3IV0Cy5zapTWx0QLTY2mSE1nhWutM7SNNrCJ6mfk84ibPedvuvT8gGu1aQGicUbhQrFvlzNXd2Yav8TWkZA/0?wx_fmt=png)

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