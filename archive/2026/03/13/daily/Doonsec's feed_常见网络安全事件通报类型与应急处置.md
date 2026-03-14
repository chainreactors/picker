---
title: 常见网络安全事件通报类型与应急处置
url: https://mp.weixin.qq.com/s/0PznhK3cDHouBwgxD8KRxg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:11:47.834641
---

# 常见网络安全事件通报类型与应急处置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/F9ccIXSyq6SQfg9lial7rjVOniaO9icsZw6LDPsQeP73Gu5mrviaO98MKfGUVgIdIV3BNGheYg7f1hj3FXkjfZFAmgrr5Gy4H9U73wCzVdQHGeA/0?wx_fmt=jpeg)

# 常见网络安全事件通报类型与应急处置

原创

Xc1Ym
Xc1Ym

墨守安全

![]()

在小说阅读器中沉浸阅读

# 常见网络安全事件通报类型与应急处置

## 常见的网络安全事件通报类型

在日常网络安全运营中，信息安全事件频发，已成为各类组织不可回避的风险。为强化风险警示与行业协同，监管机构会对辖区内发生的安全事件进行识别、定级与通报。常见的通报类型包括**勒索病毒、挖矿病毒、银狐木马、⽹⻚内嵌恶意代码、两⾼⼀弱**等，这些事件多属于**有害程序事件（MI）** 与**网络攻击事件（NAI）** 的范畴，其通报不仅推动涉事单位及时处置，也为全行业提供了关键的风险态势与防御参考。

## 勒索病毒

### 特征

勒索病毒（Ransomware）是一种恶意软件，它通过加密用户设备上的文件或锁定系统屏幕来阻止用户正常访问自己的数据或设备，然后向受害者勒索赎金（通常要求以比特币等加密货币支付），并承诺在收到赎金后提供解密密钥或恢复访问权限。这类病毒通常通过钓鱼邮件、恶意附件、漏洞攻击或伪装成正常软件的安装包进行传播，对个人、企业甚至公共机构造成严重危害，包括数据丢失、财务损失、业务中断等。

我们以`baxia`勒索病毒为例进行简单分析

![](https://mmbiz.qpic.cn/mmbiz_png/F9ccIXSyq6QDMLEPTmW28McKOdWbDNmKZmqOEmM7fhicicVkAQvzIcN58R5fCI9ib8OqUaQcHQcu7E33ajRh3xrBI2LWznL9zY6kbdWQuic1ALk/640?wx_fmt=png&from=appmsg)

`baxia`勒索病毒是BeijngCrypt勒索病毒家族的变种，通常通过各类数据库的弱口令进行入侵感染，黑客获取数据库弱口令后通过数据库命令下载、执行勒索病毒，`baxia`病毒一旦运行，就开始针对各类文档、程序(doc、docx、xlsx、xls、pdf、mdf、jpg、png、exe等格式)进行加密操作，并在加密文件夹下创建名为`!_INFO.txt`的勒索信件。同时baxia勒索病毒会针对内网中其他主机的445、3389端口发起攻击，继续扩大勒索范围。

### 处置方法

勒索病毒的处置方法主要以前期巡检、备份为主，大部分的勒索病毒使用AES+RSA加密，如果没有解密密钥，几乎无法使用常规手段解密，所以勒索病毒的处置基本上是删除相关的恶意软件、检查主机薄弱点并修复、部署相应的终端防护设备。

对于已经感染勒索病毒的主机，首先要立刻切断主机的网络，防止主机攻击其他内网机器感染更多的设备，同时也阻止主机上传解密密钥到黑客的服务器。Windows操作系统的主机可以使用命令`netsh interface set interface "以太网" disable`、Linux操作系统使用`sudo ip link set eth0 down`或者直接拔掉主机网线来禁用主机网络。

接下来需要识别勒索病毒的类型，我们可以通过观察已经被加密的文件后缀识别勒索软件的类型，以前图为例，勒索软件加密文件后后缀为`baxia`，则该勒索软件为`baxia`。我们可以访问360勒索病毒解密或者奇安信勒索病毒搜索这两个网站，查找可能可以解密的勒索病毒后缀，部分勒索病毒可能可以解密。如果不能解密，那就祈祷这台主机启用了备份功能，可以恢复到勒索前的状态吧。

紧接着就是立即关闭勒索软件，Windows主机通过`tasklist /v`检查异常进程、`netstat -ano`检查异常的网络连接，Linux主机可以使用`ps auxf`、`top -b -n 1`检查异常进程、`netstat -tulpn`和`ss -tulpn`检查异常的网络连接。一般情况下，在加密还未结束时，勒索病毒的加密操作会大量占用CPU资源，所以可以使用`KILL`命令关闭CPU资源占用较高的进程。Windows操作系统还需要检查`任务计划程序`、`注册表`、`启动文件夹`、`Windows服务`、`DLL劫持与侧加载`等等。

常见的注册表自启动键：

```
# 标准自启动键
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
# 扩展自启动位置
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit
# 登录相关键
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell
HKEY_CURRENT_USER\Environment\UserInitMprLogonScript
# 特定扩展名关联键
HKEY_CLASSES_ROOT\.txt\shell\open\command
HKEY_CLASSES_ROOT\txtfile\shell\open\command
# COM对象键
HKEY_CLASSES_ROOT\CLSID\{GUID}\InprocServer32
```

常见的启动文件夹目录

```
# 用户启动文件夹
C:\Users\<用户名>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# 所有用户启动文件夹
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```

检查要点包含：

```
# 检查服务
sc query state= all | findstr "SERVICE_NAME"
# 检查计划任务
schtasks /query /fo list
# 检查网络连接
netstat -ano | findstr "ESTABLISHED"
# 检查WMI事件
Get-WmiObject -Namespace root\subscription -Class __EventFilter
# 注册表关键位置检查
$suspectPaths = @(
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
)
foreach ($path in $suspectPaths) {
    if (Test-Path $path) {
        Get-ItemProperty -Path $path | Format-List
    }
}
```

针对Linux操作系统的勒索病毒，我们还应检查`定时任务`、`Systemd服务与定时器`、`Shell配置文件`、`动态链接库劫持`、`Init系统脚本`等。

Linux检查要点包含：

```
# 检查所有cron任务
crontab -l                          # 当前用户
crontab -u root -l                  # root用户
ls -la /etc/cron.*/                 # 系统cron目录
cat /etc/crontab                    # 系统crontab
find /etc/cron* -type f -exec cat {} \; 2>/dev/null
# 检查所有服务
systemctl list-unit-files --type=service
systemctl list-units --type=service --all
# 查看服务详情
systemctl status [服务名]
cat /etc/systemd/system/[服务名].service
# 检查定时器
systemctl list-timers --all
# 检查rc.local
cat /etc/rc.d/rc.local
cat /etc/rc.local
# 检查init.d脚本
ls -la /etc/init.d/
grep -r "执行命令" /etc/init.d/
# 检查profile文件
grep -n "可疑命令" /etc/profile ~/.bashrc ~/.bash_profile
# 查找隐藏文件
find / -name ".*" -type f 2>/dev/null | grep -v "/proc/"
find / -name "..*" -type f 2>/dev/null
# 检查/tmp、/var/tmp异常
ls -la /tmp/ /var/tmp/
find /tmp /var/tmp -type f -mtime -1
# 检查不可变文件
lsattr /etc/cron* /etc/systemd/system/*
# 检查LD_PRELOAD
echo$LD_PRELOAD
cat /etc/ld.so.preload 2>/dev/null
```

通过上述的命令排查到勒索软件的进程和守护进程后，即可关闭勒索病毒进程，备份勒索病毒样本，删除勒索病毒。

接下来是要排查勒索软件的入口，判断勒索软件是从主机的哪个脆弱点攻击成功并部署勒索病毒的。

在Windows上，首先应该排查SMB的445端口和RDP的3389端口，这是病毒内网非常常见的传播方式，这些服务能被攻破的主要原因除了未打补丁之外，还可能存在弱口令、空口令的问题，所以还需排查操作系统的登录密码的强弱，如果过于简单则需要更换。在排查的时候，可以通过Windows自带的日志系统来进行分析，在安全日志中，事件编号为4625、4688分别代表着失败登录和进程创建，前者意味着勒索并是通过猜解登录密码在主机上部署勒索病毒的，后者可以获取勒索病毒的进程创建时间，进一步确认系统中毒的时间。

```
# 检查系统补丁状态（特别是MS17-010永恒之蓝）
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
wmic qfe list brief | findstr "KB"
# 检查已知勒索漏洞补丁是否安装
wmic qfe get hotfixid | findstr "KB4012212 KB4012217 KB4012606"
# 检查RDP服务状态和配置
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber
# 检查SMB服务状态（端口445）
sc query lanmanserver
net share  # 查看共享资源
# 检查用户账户和最近登录
net user
net localgroup administrators
wevtutil qe Security /rd:true /f:text | findstr "4624 4625"  # 登录事件
# 检查弱密码或空密码账户
net user [用户名]  # 查看账户状态
wmic useraccount get name,passwordexpires,lockout
# 查看RDP连接历史
query user  # 当前会话
qwinsta     # 会话信息
# 检查安全事件日志中的可疑活动
wevtutil qe Security /rd:true /f:text /q:"*[System[(EventID=4625)]]"  # 失败登录
wevtutil qe Security /rd:true /f:text /q:"*[System[(EventID=4688)]]"  # 进程创建
# 查看应用程序和系统日志
eventvwr.msc  # 图形界面查看
# 或使用命令行筛选
Get-WinEvent -FilterHashtable @{LogName='Application'; StartTime=(Get-Date).AddDays(-7)} | Where-Object {$_.Message -like "*crypt*"}
# 查看最近修改的可执行文件
forfiles /p C:\ /s /m *.exe /d -3 /c "cmd /c echo @path @fdate @ftime"
```

在Linux上，首先要排查SSH、VNC等服务是否存在弱口令，这些服务的配置是否正确。

```
# 检查系统版本和内核
uname -a
cat /etc/os-release
lsb_release -a
# 检查已安装的安全更新（不同发行版）
# Ubuntu/Debian
apt list --installed | grep -i security
# RHEL/CentOS
yum history | grep -i update
rpm -qa --last | head -20
# 检查SSH配置和登录
grep -i "permitrootlogin\|passwordauthentication" /etc/ssh/sshd_config
last -20  # 最近登录
lastb -20 # 失败登录
# 检查RDP/VNC等服务
systemctl status xrdp vncserver 2>/dev/null
ps aux | grep -E "(xrdp|vnc|tightvnc)"
# Linux：检查内存中的可疑内容
strings /dev/mem | grep -i "ransom\|crypt\|bitcoin"
# 检查用户和特权账户
cat /etc/passwd | grep -E "(/bin/bash|/bin/sh)"
cat /etc/sudoers
sudo -l  # 当前用户sudo权限
# 检查空密码或弱密码账户
awk -F: '($2 == "" ) {print}' /etc/shadow
# 检查UID 0账户（除root外）
awk -F: '($3 == 0) {print}' /etc/passwd
# 检查文件权限
find / -perm -4000 -type f 2>/dev/null  # SUID文件
find / -perm -2000 -type f 2>/dev/null  # SGID文件
find / -type f -perm -o+w 2>/dev/null   # 全局可写文件
# 检查敏感配置文件权限
ls -la /etc/passwd /etc/shadow /etc/sudoers
# 检查LD_PRELOAD劫持
echo$LD_PRELOAD
cat /etc/ld.so.preload 2>/dev/null
# 检查bash历史
tail -50 ~/.bash_history
```

如果操作系统上还部署其他服务，比如数据库、Web服务等，那我们还应该检查这些中间件服务对应的日志信息和配置，大多数数据库被攻击、入侵都是因为使用了默认密码、弱口令，或者未授权访问，当然也有可能是Web服务导致的SQL注入。同样的，Web服务也可能存在被黑客攻破的薄弱点：任意文件上传漏洞、远程代码执行漏洞、反序列化漏洞、不安全的配置、供应链攻击、弱口令/默认口令以及前述的SQL注入等等，这些漏洞也会造成黑客的入侵，传播勒索病毒或者下述的其他病毒等。排查这些中间件服务的日志可以更清晰的反应出黑客的入侵路径，在修补薄弱点后防止下次的入侵行为。

```
# Apache日志检查
tail -200 /var/log/apache2/access.log | grep -E "(\.php|\.asp|\.jsp|POST.*\.(php|asp|jsp))"
tail -200 /var/log/apache2/error.log | grep -i "error\|warning"
# Nginx日志检查
tail -200 /var/log/nginx/access.log | grep -E "(union.*select|eval\(|base64_decode|system\(|shell_exec)"
tail -200 /var/log/nginx/error.log
# 查找异常IP访问
cat /var/log/apache2/access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -20
# 检查Web目录下的异常文件
find /var/www -name "*.encrypted" -o -name "*.locked" -o -name "*_readme.txt" 2>/dev/null
find /var/www -na...