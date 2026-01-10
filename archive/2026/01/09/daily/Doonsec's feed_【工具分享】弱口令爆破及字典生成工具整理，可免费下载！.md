---
title: 【工具分享】弱口令爆破及字典生成工具整理，可免费下载！
url: https://mp.weixin.qq.com/s/pYdr-a57MLjhuRpHgmGaMg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:24:37.880962
---

# 【工具分享】弱口令爆破及字典生成工具整理，可免费下载！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAkjeialbL3kxX1De2O47VEPaicYVJMyicUvPjQ4yPlDh2rN2bvtMrOwhv2hPCXcEpH7srkOxV4lUfbnQ/0?wx_fmt=jpeg)

# 【工具分享】弱口令爆破及字典生成工具整理，可免费下载！

点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAk1nlByTOFiahZKGHekfZGC180aw53rHwCE1KXCFEyHULHRFVH3sTdiaibVFgTPic4UWScria3Vocb1TyQ/640?wx_fmt=png&from=appmsg)

PART.01

工具介绍

本文将列举多个常用的弱口令爆破工具和字典生成工具，对比其优缺点，方便读者参考使用。

**弱口令爆破工具：**

**1**

**SNETCracker**

**2**

**zombie**

**3**

**week-passwd**

**4**

**x-crack**

**5**

**Hydra**

**6**

**legba**

**字典生成工具：**

**1**

**白鹿社工字典生成器**

**2**

**GenpAss工具**

**3**

**Crunch**

**4**

**用户名字典生成工具**

**5**

**MaskProcessor**

**6**

**火花字典生成器**

**弱口令爆破工具**

**注：本文所有工具下载地址见文末**

**SNETCracker：**

工具下载地址：*https://github.com/shack2/SNETCracker/releases*

        Windows平台的弱口令审计工具， 工具采用C#开发，需要安装.NET Framework 4.0，工具目前支持SSH、RDP、SMB、MySQL、SQLServer、Oracle、FTP、MongoDB、Memcached、PostgreSQL、Telnet、SMTP、SMTP\_SSL、POP3、POP3\_SSL、IMAP、IMAP\_SSL、SVN、VNC、Redis等服务的弱口令检查工作。

![](https://mmbiz.qpic.cn/mmbiz_png/wGIib2JsfOsxVvuKCPdBrVF7S8icI5qn4VjF7xbvJuYmnyBUs9qcOYtMobdvQzeYZacHnbFgzEcAW1TNXoibo0nqA/640?wx_fmt=png&from=appmsg)

**zombie：**

工具下载地址：

*https://github.com/chainreactors/zombie*

一个轻量级的服务口令爆破工具, 继承了hydra的命令行设计, hashcat的字典生成, 以及红队向的功能设计。

基本使用如下：

```
#使用默认字典爆破ssh的root用户口令zombie -i 1.1.1.1 -u root -s ssh
#使用指定的密码批量喷洒ssh口令zombie -I targets.txt -u root -p password -s ssh
#从gogo结果开始扫描zombie --gogo 1.dat
```

**week-passwd：**

工具下载地址：

*https://github.com/BBD-YZZ/week-passwd*

        支持FTP、SSH、MySQL和MSSQL等多种协议。它能够进行密码暴力破解，支持导入多种IP格式进行爆破，并允许从文本文件导入IP数据。

![](https://mmbiz.qpic.cn/mmbiz_png/wGIib2JsfOsxVvuKCPdBrVF7S8icI5qn4V87m5SayDAYxS75jasNmrWBRwRcOHr6cfg94tBicU4JskA1HhiaIV21vg/640?wx_fmt=png&from=appmsg)

**x-crack：**

工具下载地址：

*https://github.com/netxfly/x-crack*

        使用Go语言开发，支持多种协议的爆破攻击，包括SSH, FTP, Telnet, MySQL, PostgreSQL, Redis, MongoDB, HTTP/HTTPS, SMB, VNC, SNMP, IMAP, POP3, SMTP 等16种协议。

基本使用如下：

```
# 单目标单协议爆破./x-crack -target 192.168.1.100 -protocol ssh -username root -password 123456
# 多用户名密码组合./x-crack -target 192.168.1.100 -protocol ssh -usernames root,admin -passwords 123456,password
# 批量目标扫描./x-crack -l ip.txt -protocols ssh
# 从文件读取目标和凭据./x-crack -target-file targets.txt -user-file users.txt -pass-file passwords.txt -protocol ssh
# 高性能配置（推荐用于生产环境）./x-crack -target 192.168.1.100 -protocol ssh \  -target-concurrent 10 -task-concurrent 5 \  -timeout 10s -retries 2 -delay 200ms
# 高速扫描配置（谨慎使用）./x-crack -target 192.168.1.100 -protocol ssh \  -target-concurrent 20 -task-concurrent 10 \  -timeout 5s -delay 100ms
# 输出到文件并显示详细信息./x-crack -target 192.168.1.100 -protocol ssh \  -output results.json -format json -verbose -show-failed
```

**Hydra：**

开源下载地址（kali自带）：

*https://github.com/vanhauser-thc/thc-hydra*

        又名九头蛇，是一款由著名的黑客组织THC开发的开源暴力破解工具，支持大部分协议的在线密码破解，是网络安全渗透测试必备的一款工具。

基本使用如下：

```
#hydra格式：hydra -l/L 指定用户名 -p/P 指定密码字典 协议hydra -l user -P passlist.txt ftp://192.168.0.1hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAINhydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5hydra -l admin -p password ftp://[192.168.0.0/24]/hydra -L logins.txt -P pws.txt -M targets.txt ssh
```

**legba：**

从docker中安装：

```
#Docker Hub上提供了 Docker 镜像docker run -it evilsocket/legba -h
#如果安装了Cargo，可以从Cargo中安装cargo install legba
```

Legba是一个使用 Rust 和 Tokio 异步运行时构建的多协议可靠性暴力破解器/密码破解器和枚举器，以便实现更好的性能和稳定性，同时消耗比类似工具更少的资源。

基本使用方法：

```
#admin从单词列表加载密码时将始终用作用户名。legba <plugin name> --username admin --password data/passwords.txt
#将从单词列表中加载两者并使用所有组合。legba <plugin name> --username data/users.txt --password data/passwords.txt
#将始终用admin作用户名并尝试 4 到 8 个字符之间的默认可打印 ASCII 字符集的所有排列（这是未传递值时的默认行为）。legba <plugin name> --username admin
#将从单词列表加载用户，同时测试/some/path.legba <plugin name> --username data/users.txt --password '@/some/path/*.key'
#将从单词列表加载用户，同时测试abcdef4 和 5 个字符长的字符的所有排列。legba <plugin name> --username data/users.txt --password '#4-5:abcdef'
#将从单词列表加载用户，同时测试从 10 到 999 的所有数字。legba <plugin name> --username data/users.txt --password '[10-999]'
#将从单词列表加载用户，同时测试数字 1、2、3 和 4。legba <plugin name> --username data/users.txt --password '[1, 2, 3, 4]'
```

**字典生成工具**

**白鹿社工字典生成器：**

工具下载地址：

*https://github.com/HongLuDianXue/BaiLu-SED-Tool/releases*

常用的复杂密码一般分为3项：信息项、符号项、弱字符串项。

比如：Admin@123，其中Admin为信息项、@为符号项、123为弱字符串项。

白鹿社工字典生成器依据以上复杂密码的特点，将上述的信息项、符号项、弱字符串项分别对应A项、B项、C项。

![](https://mmbiz.qpic.cn/mmbiz_png/wGIib2JsfOsxVvuKCPdBrVF7S8icI5qn4VbMSvwa8rAnwdovSibAlCwpK1lqahhPymn5jcJiclKLYicVDPic3xtK0lhA/640?wx_fmt=png&from=appmsg)

基本使用方法：

点击“生成字典文件”，将“A项”、“B项”、“C项”数据按照“字典组合方式”及其他配置生成字典文件。

**GenpAss工具：**

工具下载地址：

*https://github.com/RicterZ/genpAss/tree/master*

中国特色的弱口令生成器，基本使用方法：

假定一个人的信息如下：

|  |  |
| --- | --- |
| 字段 | 信息 |
| 姓名 | 王大锤 |
| 用户名 | dachui,dac |
| QQ | 818271273 |
| 手机 | 13928182828 |
| 邮箱 | wangdac@gmail.com |
| 生日 | 1993-12-21 |
| 公司 | baidu |

可以根据以上信息生成密码：

```
genpass -n 王大锤 -u dachui dac -b 1993-12-21 -c baidu -m 13928182828 -q 818271273 -e wangdac@gmail.com
```

**Crunch：**

工具下载地址：

*https://github.com/crunchsec/crunch*

*https://github.com/jaalto/external-sf--crunch-wordlist*

kali中直接运行以下命令直接安装：

```
apt-get install crunch
```

Crunch是一种创建密码字典工具，按照指定的规则生成密码字典，可以灵活的制定自己的字典文件。使用Crunch工具生成的密码可以输出到屏幕，保存到文件、或另一个程序。知道密码的一部分细节后，可以针对性的生成字典。

基本使用方法：

```
crunch 660123456789 -o start # 生成6位数，由0到9位数字组成的，从小到大排序的字典。
crunch 660123456789 -d 2 # 生成6位数，由0到9位数字组成的，同一字符最多连续出现2次的字典。
crunch 44 -f /usr/share/crunch/charset.lst numeric -o 1.txt # 使用数字的字符集去生成4位数的字典。
crunch 11 -p abc # 生成abc的组合的字典
crunch 550123456789 -s 99990 # 生成的字典中是以99990为初始点的。
crunch 11 -q 1.txt # 以文件中每行内容作为基本字符，以排列组合的方式生成字典，最大最小字符失效但必须有
crunch 66 -t @,%%^^# # 生成6位数的字典，满足【小写字母+大写字母+数字+数字+符号+符号】的形式。
crunch 44 -t @,%^ -o 1.txt -z 7z # 生成四位数的字典，满足【小写字母+大写字母+数字+符号】的形式，输出文件名为1.txt，压缩成7z格式。
```

**用户名字典生成工具：**

工具下载地址：

*https://github.com/abc123info/UserNameDictTools*

用户名字典生成工具，用于将中文汉字姓名转换为拼音格式，支持多达11种拼音格式的转换。

![](https://mmbiz.qpic.cn/mmbiz_png/wGIib2JsfOsxVvuKCPdBrVF7S8icI5qn4Vl7CaAdSFC8Z59PdjtISqncUiaCic4tf5YGw8WS2wL8kdrUqJlicyQXa0w/640?wx_fmt=png&from=appmsg)

**Maskprocessor：**

工具下载地址：

*https://github.com/hashcat/maskprocessor*

Maskprocessor是一个快速单词列表生成器。它枚举给定用户定义的键空间中的所有组合，并输出结果。由于它在生成模板（“掩码”）的不同位置支持不同的字母表（也可以组合），因此这种方法允许比使用“朴素”的强力单词枚举更精细地生成候选字母。使用Hashcat密码恢复实用程序中也使用的描述定义掩码。

**火花字典生成器：**

工具下载地址：

*https://github.com/G0mini/spark*

功能特点包括有社工字典生成、hash碰撞等。

![](https://mmbiz.qpic.cn/mmbiz_png/wGIib2JsfOsxVvuKCPdBrVF7S8icI5qn4VTQ0hd8rIba3pJKnRds7t1YiclhvBSVm5JTYZCf7FuIj6c0icGNTkqBPg/640?wx_fmt=png&from=appmsg)

文章内容转自安全栈，侵删

![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAkmMvIEVFdiaG19OichW7IMqrDC7rMDCXQWeTOvkzUbVDPG6M2icEqCwQfLRKHbo8Z0r9FDdhfuyOXOQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过