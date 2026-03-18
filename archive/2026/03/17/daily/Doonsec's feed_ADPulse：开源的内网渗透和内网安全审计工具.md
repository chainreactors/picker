---
title: ADPulse：开源的内网渗透和内网安全审计工具
url: https://mp.weixin.qq.com/s/rF2w1rR1L-ZLhFsD5jFEaw
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:17:27.577112
---

# ADPulse：开源的内网渗透和内网安全审计工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicLgrJngUWiaM6K0kN9hBk2uhEIcjp5V1aY0V8b56yqXM3fWMafnEEGvmV7trJrQAgacqzcZjtCWlqZ1WTUjiaOc07atiasnAxzTNA/0?wx_fmt=jpeg)

# ADPulse：开源的内网渗透和内网安全审计工具

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[VulnRadar：集成多模块的Chrome浏览器安全渗透测试扩展](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486780&idx=1&sn=86e51f2d05c04ccb6ecf14104f50f99b&scene=21#wechat_redirect)

·[NetSonar：跨平台多协议的开源网络诊断工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486769&idx=1&sn=1e45bd9e7fa03e5dafa6335010f10e75&scene=21#wechat_redirect)

·[CTF和实战可用-文件上传漏洞检测专业工具：UploadRanger](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486761&idx=1&sn=ad09098ab205e45600339e0aa9dfa836&scene=21#wechat_redirect)

·[SwordfishSuite：多平台抓包分析利器-现代化 Web 安全测试平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486734&idx=1&sn=4e5310b6adb0b5ee09c917b3bbf851d9&scene=21#wechat_redirect)

·[OpenClaw Exposure Watchboard：OpenClaw实例公网暴露安全监控面板](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486703&idx=1&sn=5434a2d90ceed9f066b1ae3f26228655&scene=21#wechat_redirect)

·[HackerMind：三AI架构自集成MCP的链上对话智能渗透系统工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486640&idx=1&sn=19052c6dd7b1d73d9b8395857276042f&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKtvCFHMZ9Pd3pnINeQc1BRAtGPOkZf2IGp0lrcVF5qINwh1U5gch8Iz9UYB5FEibCjTaSFEYLR7taB7j9Qd3E8zCTK842g5Nv8/640?wx_fmt=png&from=appmsg)

`Active Directory`作为企业核心身份域管理组件，存在密码策略配置不当、特权账户管控缺失、`Kerberos`漏洞、`ADCS/PKI`配置风险、域信任权限过高、`ACL`权限滥用等多类安全问题，人工逐项核查效率低且易遗漏，`ADPulse`这款开源工具应运而生，通过`LDAP`(S)连接域控制器执行35项自动化安全检查，以只读方式评估`AD`配置错误与攻击面，输出多格式报告，帮助`IT`管理员、渗透测试人员与安全团队快速发现`AD`核心安全风险。

**安装介绍**

```
地址：https://github.com/dievus/ADPulse
```

`ADPulse`基于`Python`开发，运行前需确保本地已配置`Python`环境，首先需从项目仓库克隆代码或下载源码包，获取工具文件与依赖清单：

```
# 克隆项目仓库（获取完整源码与requirements文件）
git clone https://github.com/dievus/ADPulse.git
# 进入项目目录
cd ADPulse
```

项目提供`requirements.txt`依赖清单文件，需通过`pip`安装所需依赖包，确保工具运行环境完整：

```
# 安装项目依赖（基于requirements.txt）
pip install -r requirements.txt
```

依赖安装完成后，无需额外安装流程，直接通过`Python`命令调用`ADPulse.py`即可启动工具，若启动失败需检查`Python`环境或依赖包是否安装成功。

功能介绍

| 序号 | 检查项 | 功能说明 |
| --- | --- | --- |
| 1 | 密码策略 | 最小长度、密码历史、复杂度、锁定阈值、可逆加密、精细密码策略对象 (PSO) |
| 2 | 特权账户 | 域管理员、企业管理员、架构管理员等敏感组的成员；失效成员、密码永不过期、描述中包含密码、内置管理员状态、krbtgt 账户使用时长 |
| 3 | Kerberos | 可 Kerberoast 攻击的账户（用户对象上的 SPN）、可 AS-REP Roast 攻击的账户、仅使用 DES 加密、同时满足 adminCount=1+SPN+PasswordNeverExpires 的高价值目标 |
| 4 | 无约束委派 | 被信任进行无约束 Kerberos 委派的非域控计算机与用户账户 |
| 5 | 约束委派 | 配置协议转换（S4U2Self）的账户及标准约束委派目标 |
| 6 | ADCS / PKI | ESC1、ESC2、ESC3、ESC6、ESC8、ESC9、ESC10、ESC11、ESC13、ESC15 漏洞、弱密钥长度、注册权限 ACL 枚举 |
| 7 | 域信任关系 | 未启用 SID 过滤的双向信任、林信任、外部信任 |
| 8 | 账户健康度 | 失效用户 / 计算机、从未登录的账户、PASSWD\_NOTREQD 标记、账户级可逆加密、旧密码、重复 SPN |
| 9 | 协议安全 | LDAP 签名 / 通道绑定、域控操作系统版本、域 / 林功能级别、NTLMv1/WDigest 配置 |
| 10 | 组策略对象 | 禁用、孤立、未链接、空的 GPO；过多的 GPO 数量 |
| 11 | LAPS | 旧版 LAPS 与 Windows LAPS 架构检测；未配置 LAPS 密码的计算机 |
| 12 | LAPS 覆盖率 | 所有非域控计算机中配置 LAPS 托管密码的占比 |
| 13 | DNS & 基础架构 | 通配符 DNS 记录、LLMNR/NetBIOS-NS 投毒风险提示 |
| 14 | 域控制器 | 单域控检测、域控上的旧版操作系统、FSMO 角色、RODC 密码复制策略 |
| 15 | ACL / 权限 | ESC4、ESC5、ESC7、非特权主体的 DCSync 权限、受保护用户组、委派 ACL |
| 16 | 可选功能 | AD 回收站、特权访问管理（PAM） |
| 17 | 复制健康 | 站点数量、站点链接复制间隔、nTDSDSA 对象 |
| 18 | 服务账户 | gMSA 部署情况、普通用户类型服务账户、adminCount=1 的服务账户 |
| 19 | 其他加固项 | 计算机账户配额、墓碑生存期、架构管理员 / 企业管理员成员、来宾账户、审计策略提示 |
| 20 | 已弃用操作系统 | 已启用且报告 Windows 已停止支持版本的计算机账户 |
| 21 | 旧版协议 | SMBv1 检测、SMB 签名强制、空会话接受（网络探测） |
| 22 | Exchange | Exchange Windows Permissions 组（PrivExchange/CVE-2019-0686）、Exchange 可信子系统 |
| 23 | 受保护管理员用户 | adminCount=1 清单 —— 孤立、失效（禁用）、过期账户 |
| 24 | 描述中包含密码 | 基于关键词检测用户、管理员、计算机描述字段中存储的凭证 |
| 25 | GPP / cpassword (MS14-025) | 遍历 SYSVOL 中的组策略首选项 XML 文件，使用微软公开 AES 密钥解密 cpassword |
| 26 | AdminSDHolder ACL | 读取 AdminSDHolder 的 DACL，标记拥有写入权限的非特权主体；这些 ACE 会通过 SDProp 每 60 分钟自动同步到所有受保护账户 |
| 27 | SID 历史 | 检测存在 sIDHistory 的账户；若注入的 SID 映射到特权组（域管、企业管等）则标记为严重 |
| 28 | 影子凭证 | 标记用户与计算机对象上的异常 msDS-KeyCredentialLink 条目，可实现无密码证书认证 |
| 29 | RC4 / 旧版 Kerberos 加密 | 检查服务账户、域控、管理员账户，识别仍允许 RC4-HMAC 弱加密类型的对象 |
| 30 | 特权组中的外来安全主体 | 枚举并标记来自受信任域、加入敏感本地组（域管理员、备份操作员等）的外来安全主体 (FSP) |
| 31 | 兼容 Windows 2000 前访问 | 检查 Everyone / 匿名登录是否在此组中，该配置允许网络中任意位置未认证的 SAMR/LSARPC 枚举 |
| 32 | 危险约束委派目标 | 将委派目标与域控主机名对比，标记委派到域控上高价值服务类（ldap/cifs/host/gc/krbtgt 等）的账户 |
| 33 | 孤立 AD 子网 | 查找未分配到站点的子网，会导致客户端随机分配域控，可能跨广域网传输认证流量 |
| 34 | 旧版 FRS SYSVOL 复制 | 检测 SYSVOL 是否仍通过已弃用的文件复制服务 (FRS) 而非 DFSR 复制，标记迁移中断状态 |
| 35 | 域对象 / 域控上的 RBCD | 检查域命名上下文头部与所有域控计算机对象的 msDS-AllowedToActOnBehalfOfOtherIdentity，该配置可通过 S4U2Proxy 获取域管权限 |

`ADPulse`核心功能为连接域控制器执行`AD`安全审计，基础扫描命令可指定域、用户与密码完成35项安全检查，具体命令如下：

```
# 基础AD安全扫描
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!'
```

若需指定特定域控制器执行扫描，可在命令中添加`--dc-ip`参数，精准定位审计目标，命令示例如下：

```
# 指定域控制器IP执行扫描
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!' --dc-ip 10.0.0.1
```

`ADPulse`支持控制台、`JSON`、`HTML`三种报告格式输出，可通过`--report`参数指定单一格式或`all`输出所有格式，命令示例如下：

```
# 指定报告输出格式（控制台/JSON/HTML/all）
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!' --report console/json/html/all
```

如需将报告文件保存至指定目录，可添加`--output-dir`参数自定义输出路径，便于报告归档管理，命令示例如下：

```
# 自定义报告输出目录
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!' --output-dir /tmp/scans
```

若终端环境不支持彩色输出，可添加`--no-color`参数禁用彩色显示，保证报告内容清晰可读，命令示例如下：

```
# 禁用控制台彩色输出
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!' --no-color
```

`ADPulse`的35项安全检查覆盖密码策略、特权账户、`Kerberos`、`ADCS/PKI`、域信任、`ACL`权限、`LAPS`、遗留协议等核心`AD`安全风险点，扫描完成后会以指定格式输出详细报告，包含风险评分与等级划分，仅执行只读操作，不会对`AD`环境产生写入影响，可用于常态化安全巡检与合规评估。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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