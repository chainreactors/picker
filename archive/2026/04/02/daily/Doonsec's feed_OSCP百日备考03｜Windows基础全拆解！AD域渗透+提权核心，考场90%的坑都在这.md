---
title: OSCP百日备考03｜Windows基础全拆解！AD域渗透+提权核心，考场90%的坑都在这
url: https://mp.weixin.qq.com/s/1D3df-ILs_Z-cMTihz-ATA
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:21:54.697055
---

# OSCP百日备考03｜Windows基础全拆解！AD域渗透+提权核心，考场90%的坑都在这

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydWaicGCCJxDhnxQ0VGF4VEAVpdfwialm3DjCcVm6N9C1ibcXVMku7n865Od2puWHA0sKhVP4ymNe5OwDLTsiav5nlR3nGJIz7LmPxM/0?wx_fmt=jpeg)

# OSCP百日备考03｜Windows基础全拆解！AD域渗透+提权核心，考场90%的坑都在这

泷羽Sec-陌离

![]()

在小说阅读器中沉浸阅读

# OSCP百日备考03｜Windows基础全拆解！AD域渗透+提权核心，考场90%的坑都在这

## 别只死磕Linux了！OSCP考试40分AD域全靠它，零基础也能吃透

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydVnY5TKkE2Im45n7HoLOPH3qWg7Yv1ic2vRXpyGr1Lc3UHeCEQ3dzEpUOsF0lIDSbSx85onoPwSBk5IWS0sKg6fKYibNYsqVQDs0/640?wx_fmt=webp&from=appmsg)

大家好，这里是[泷羽Sec—陌离]，OSCP百日备考系列第三期准时更新。

上一期我们把OSCP备考的Linux核心基础讲透了，后台收到很多宝子的留言，说终于搞懂了Linux该学什么、怎么练，但同时也问了一个高频问题： 「学长，我是不是把Linux学明白就够了？Windows平时用的少，渗透里是不是用不上？」

今天必须给所有备考OSCP的人敲一个警钟：**绝对不是！Windows基础不仅要学，还要学透，它直接决定了你能不能拿下OSCP考试里占40分的AD域环境，能不能跨过70分的及格线**。

我见过太多备考的人踩了这个大坑：上来就死磕Kali Linux，把Linux命令、提权玩的滚瓜烂熟，结果一遇到Windows靶机直接懵了——连找个flag文件都要查半天命令，拿到低权限shell不知道该查什么信息，更别说提权、内网横向移动了。

要知道，OSCP考试里，AD域环境固定占40分，而AD域的底层，全是Windows服务器和终端；企业真实内网里，90%以上的办公终端、业务服务器，也都是Windows系统。说白了，**Linux是你的攻击武器，而Windows是你最常面对的攻击目标**。

今天这篇，我们不讲没用的理论堆砌，只讲OSCP考场100%会用到的Windows核心基础，每一个知识点、每一条命令，都给你讲清楚「考场里什么时候用、为什么重要」。哪怕你平时很少用Windows，看完也能搞懂渗透测试里的Windows核心逻辑，直接落地到靶场练习里。

---

## 一、先搞懂：为什么OSCP备考，Windows基础绝对不能跳过？

很多人觉得，渗透测试用Kali Linux就够了，Windows学不学无所谓，这是OSCP备考里最致命的误区。

给大家算一笔账，你就知道它有多重要：

1. **考试核心分值绑定**：OSCP考试里，AD域环境固定占40分，而AD域完全基于Windows系统搭建，域内的所有主机、服务器、权限体系，全是Windows的底层逻辑。不懂Windows基础，域渗透根本无从下手，相当于直接放弃了近一半的分值。
2. **渗透实战高频目标**：不管是考试靶机，还是真实的企业内网渗透，Windows都是最常见的目标。从边界打点后的Windows提权，到内网横向移动、权限维持，全靠Windows基础撑着。
3. **提权核心考点全覆盖**：OSCP里Windows靶机的提权，90%都围绕着Windows的权限系统、服务配置、计划任务、注册表这些基础内容。不懂这些，哪怕你拿到了shell，也找不到提权的突破口。
4. **考场丢分重灾区**：太多人Linux学的很扎实，遇到Windows靶机就抓瞎，连最基础的查系统信息、看用户权限都要查资料，白白浪费考场时间，甚至明明有清晰的攻击路径，却栽在基础操作上。

一句话总结：**Windows基础，是OSCP备考里躲不开、绕不过的核心内容，更是你从「会用工具的脚本小子」，变成「能实战的渗透测试工程师」的关键一步**。

---

## 二、Windows文件系统：搞懂结构，靶机里不迷路

和Linux一切皆文件的根目录结构不同，Windows以盘符为核心，用字母区分驱动器（比如最常见的C:、D:），系统默认安装在C盘，绝大多数渗透操作，也都围绕C盘展开。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydWKyxgL7kb9IfhpfwEQHKhmydP3CD8oOGMcotCyCJdxW915iaiaaXb8IUX5BicUPSYCwBPhQPhSHQasnQuibI7Oa3Vkibmx3L49ib3lk/640?wx_fmt=jpeg&from=appmsg)

1. 渗透必记的核心目录

不用记全所有目录，把这些考场里必翻的目录记牢，找flag、找敏感信息、找提权线索就不会迷路：

| 目录路径 | 核心作用 | 渗透实战场景 |
| --- | --- | --- |
| `C:\Windows\` | Windows系统核心目录，存放系统文件 | 系统配置、内置工具、漏洞相关的系统文件都在这，提权必翻 |
| `C:\Windows\System32\` | 系统核心DLL、可执行文件存放目录 | 系统自带的CMD、PowerShell、各类系统工具都在这里，拿到shell后执行系统命令的核心路径 |
| `C:\Windows\Temp\` | 系统临时文件目录 | 【渗透首选目录】和Linux的/tmp一样，默认所有用户都有读写权限，用来传exp、写脚本、放工具，不会有权限问题 |
| `C:\Program Files\` 、`C:\Program Files (x86)\` | 64位/32位程序的默认安装目录 | 找第三方软件的漏洞、配置文件、敏感信息，很多服务提权的突破口都在这里 |
| `C:\Users\[用户名]\` | 用户配置文件目录，每个用户对应一个子目录 | 【找flag核心目录】用户的桌面、文档、下载文件夹都在这里，用户级的flag基本都放在桌面/文档里 |
| `C:\Users\[用户名]\AppData\` | 应用程序数据目录，分Local、Roaming、LocalLow三个子目录 | 存放软件的配置文件、缓存、历史记录，浏览器密码、用户凭证、敏感配置全在这，信息收集必翻 |
| `C:\ProgramData\` | 所有用户共享的程序数据目录 | 很多服务、软件的公共配置文件放在这里，默认权限配置经常出问题，是提权的高频突破口 |

2. 渗透必知的NTFS文件系统特性

Windows主流的文件系统是NTFS，它的几个特性，是OSCP里的高频考点：

* **细粒度NTFS权限**：和Linux的ugo权限不同，NTFS可以给不同用户、不同组设置更精细的访问权限，很多Windows提权，都是利用了文件/目录的权限配置错误；
* **交替数据流（ADS）**：可以在文件里隐藏数据，是Windows里最常用的文件隐藏手法，不管是找靶机里的隐藏flag，还是后期做权限维持留后门，都会用到；
* **符号链接/硬链接**：和Linux的链接文件类似，经常被用来做权限绕过、文件读取的提权操作；
* **文件属性**：只读、隐藏、系统、归档等，用`dir /a`才能看到隐藏文件，找flag的时候必用。

---

## 三、Windows核心命令：OSCP考场必用，分场景全整理

Windows的命令行工具主要分两种：传统的CMD命令行，和功能更强大的PowerShell。OSCP考试里，很多场景CMD会被限制，PowerShell是主流，所以两者都要掌握。

我们不罗列冷门命令，只按渗透场景，整理考场里100%会用到的高频命令，每一条都给你讲清楚实战用途。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydWJqzPXrXbd5A7SYtaTB3sXSpbic3ljvcWpDXD50bicX6aSS6rmiaWiaIbwRPadAbsmwP3icqQpOMjlCia0Vb3a6pMpj8whiaGIkVXK5I/640?wx_fmt=jpeg&from=appmsg)

1. 文件操作命令（找flag、传文件必用）

这是你拿到Windows shell后，做的最多的操作，找flag、看配置、传exp全靠它：

```
:: 【考场必敲】列出当前目录所有文件，包括隐藏文件、系统文件
dir /a

:: 递归显示当前目录及所有子目录的文件，找flag的时候全盘遍历用
dir /s

:: 切换目录，和Linux的cd用法基本一致
cd 目录名
:: 切换到当前盘符的根目录
cd \
:: 返回上一级目录
cd..

:: 复制文件
copy 源文件 目标文件
:: 递归复制整个目录及子目录，复制文件夹用
xcopy /s /e 源目录 目标目录

:: 移动/重命名文件
move 原文件 目标路径/新文件名

:: 【谨慎使用】强制安静删除文件，不会弹出确认提示
del /f /q 文件名

:: 创建目录
mkdir 目录名
md 目录名

:: 【谨慎使用】递归强制删除目录及所有内容，误删会直接破坏靶机
rmdir /s /q 目录名

:: 查看文件内容，对应Linux的cat命令
type 文件名

:: 分页查看大文件内容，对应Linux的more命令
more 文件名

:: 在文件中搜索字符串，对应Linux的grep命令，找敏感关键词必用
findstr /i "关键词" 文件名
:: /i 表示忽略大小写，搜索的时候必加
```

2. 系统信息&权限命令（提权第一步必敲）

拿到Windows低权限shell后，第一件事就是收集系统信息、查看当前用户权限，找提权的突破口，这些命令每一台Windows靶机都要敲一遍：

```
:: 【必敲】显示系统详细信息，包括系统版本、内核版本、补丁情况、主机名、域信息
:: 系统补丁号直接决定了能用什么内核漏洞提权，必看
systeminfo

:: 【提权核心】查看当前用户名
whoami
:: 【重中之重】查看当前用户拥有的特权，比如SeImpersonatePrivilege这类提权必备的特权，每台靶机必敲
whoami /priv
:: 查看当前用户所属的组，比如是不是在管理员组、远程桌面组里
whoami /groups

:: 查看系统所有用户账户
net user
:: 查看指定用户的详细信息，包括用户权限、所属组、密码过期时间
net user 用户名

:: 查看系统所有本地组
net localgroup
:: 查看管理员组的成员，找域内/本地管理员账号
net localgroup Administrators

:: 【提权常用】把用户添加到管理员组，拿到管理员权限后创建后门用户用
net localgroup Administrators 用户名 /add

:: 查看系统所有运行的进程，对应Linux的ps命令
tasklist
:: 查看进程和对应的服务、PID，找以system权限运行的服务，提权突破口
tasklist /svc

:: 【谨慎使用】强制终止指定PID的进程，杀杀毒软件、卡死的进程用
taskkill /f /pid 进程PID
:: 按进程名强制终止进程
taskkill /f /im 进程名.exe

:: 查看系统所有计划任务，找提权用的定时任务，很多靶机的提权点都在这
schtasks /query
```

3. 网络命令（内网渗透、横向移动必用）

信息收集、反弹shell、内网横向移动、端口扫描，全靠这些命令，尤其是AD域渗透的时候，高频使用：

```
:: 【必敲】查看本机IP地址、子网掩码、网关、DNS等网络配置
ipconfig
:: 查看详细的网络配置，包括MAC地址、主机名、DHCP信息、网卡信息
ipconfig /all
:: 清除本地DNS缓存，域名解析出问题的时候用
ipconfig /flushdns

:: 【信息收集核心】查看所有网络连接、监听端口、对应的进程PID，对应Linux的netstat -ano
:: 找靶机开放的内网端口、和域内其他主机的连接，必用
netstat -ano

:: 测试和目标主机的网络连通性，对应Linux的ping
ping 目标IP/域名

:: 跟踪到目标的网络路径，对应Linux的tracert
tracert 目标IP/域名

:: DNS查询，对应Linux的nslookup/dig
nslookup 域名

:: 查看局域网内的计算机共享资源
net view
:: 查看指定主机的共享文件夹，找域内共享的敏感文件
net view \\目标主机名/IP

:: 查看本机的共享文件夹
net share
:: 创建共享文件夹，内网传文件用
net share 共享名=文件夹路径
:: 删除共享
net share 共享名 /delete

:: 【横向移动常用】把远程主机的共享文件夹映射为本地Z盘
net use Z: \\目标主机IP\共享名
:: 删除映射的网络驱动器
net use Z: /delete

:: 查看Windows防火墙状态
netsh advfirewall show allprofiles
:: 【考场常用】关闭所有防火墙配置文件，反弹shell被防火墙拦的时候用
netsh advfirewall set allprofiles state off
:: 添加入站规则，放行指定端口
netsh advfirewall firewall add rule name="Allow Port" dir=in action=allow protocol=TCP localport=端口号
```

4. 服务管理命令（Windows服务提权核心）

Windows服务提权，是OSCP里最常见的Windows提权方式，没有之一。这些命令，就是你找服务提权漏洞的核心工具：

```
:: 【必敲】列出系统所有服务的状态、名称、PID
sc query
:: 查看指定服务的详细配置，包括可执行文件路径、启动类型、运行用户
:: 【重中之重】服务的binpath路径，是服务提权的核心，必查
sc qc 服务名

:: 启动/停止指定服务
sc start 服务名
sc stop 服务名

:: 【提权核心】修改服务的可执行文件路径，服务路径劫持提权必用
sc config 服务名 binpath= "要执行的恶意程序路径"

:: 用net命令启动/停止服务，和sc命令效果一致
net start 服务名
net stop 服务名
```

5. 注册表操作命令（信息收集、权限维持必用）

Windows注册表存放着系统、软件的所有配置信息，不管是找开机启动项、系统配置，还是后期做权限维持留后门，都会用到注册表操作：

```
:: 查询指定注册表项的值，比如查开机启动项
reg query 注册表路径
:: 示例：查询本地机器的开机启动项
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
:: 示例：查询当前用户的开机启动项
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

:: 添加注册表项和键值，留开机启动后门常用
reg add 注册表路径 /v 键名 /t 数据类型 /d 数据
:: 示例：添加一个开机启动项
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "backdoor" /t REG_SZ /d "C:\Windows\Temp\backdoor.exe"

:: 删除注册表项/键值
reg delete 注册表路径 /v 键名
```

---

## 四、Windows权限系统：OSCP提权的灵魂考点

毫不夸张地说，OSCP里90%的Windows提权，都围绕着Windows权限系统的漏洞和配置错误展开。和Linux的ugo权限体系不同，Windows的权限系统更复杂，也更精细，我们只讲渗透里最核心的内容。

1. 核心用户与内置组

Windows的用户分为三类，渗透里重点关注前两类：

* **管理员（Administrator）**：系统最高权限用户，完全控制系统，我们提权的最终目标，就是拿到管理员权限；
* **标准用户**：普通用户，只有有限的系统访问权限，也是我们拿到shell后最常见的用户权限；
* **访客（Guest）**：最小权限用户，实战里很少遇到。

而内置组，决定了用户的权限范围，渗透里必记的几个核心组：

* **Administrators**：管理员组，组内的所有用户都拥有系统完全控制权限，提权的核心目标就是把自己的用户加进这个组；
* **Users**：标准用户组，普通用户默认在这个组里，只有基础的权限；
* **Remote Desktop Users**：远程桌面用户组，组内的用户可以通过RDP远程登录主机，横向移动的时候常用；
* **Backup Operators**：备份操作员组，组内用户可以备份/恢复系统里的所有文件，哪怕没有读取权限，也是提权的常用突破口。

2. 用户账户控制（UAC）

UAC是Windows的安全机制，简单来说，哪怕你用管理员账户登录系统，执行高权限操作的时候，也会弹出确认窗口，防止恶意程序静默获取高权限。

对渗透测试来说，UAC是我们从本地管理员到系统完全控制的一道坎，很多时候我们拿到了管理员组的用户shell，却因为UAC的限制，执行不了高权限操作，这时候就需要用到UAC绕过技术，也是OSCP里的高频考点。

3. 访问控制列表（ACL）

ACL是Windows权限系统的核心，它定义了不同用户、不同组，对一个文件、目录、注册表项、服务等对象的访问权限，比如读取、写入、执行、完全控制等。

很多Windows提权，都是利用了ACL的配置错误：比如一个以System权限运行的服务，它的可执行文件，普通用户居然有写入权限；或者一个系统关键目录，普通用户有完全控制权限。这些配置错误，都是我们提权的绝佳突破口。

查看和修改ACL的核心命令是`icacls`：

```
:: 查看指定文件/目录的ACL权限配置，找权限配置错误必用
icacls 文件/目录路径

:: 给指定用户授予文件的读写权限
icacls 文件路径 /grant 用户名:(R,W)

:: 拒绝指定用户对文件的完全控制权限
icacls 文件路径 /deny 用户名:(F)
``...