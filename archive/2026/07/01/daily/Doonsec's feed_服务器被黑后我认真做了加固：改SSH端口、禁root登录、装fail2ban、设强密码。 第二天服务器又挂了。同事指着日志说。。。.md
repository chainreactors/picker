---
title: 服务器被黑后我认真做了加固：改SSH端口、禁root登录、装fail2ban、设强密码。 第二天服务器又挂了。同事指着日志说。。。
url: https://mp.weixin.qq.com/s/A27n9vqs4yJWXvZOD1-5fA
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:08.135126
---

# 服务器被黑后我认真做了加固：改SSH端口、禁root登录、装fail2ban、设强密码。 第二天服务器又挂了。同事指着日志说。。。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Skw2xH7iae22VDKLv2zz6KJXicveKUc18SAHkEJC64YsIJuK4m58NSiaLo6dHGEBk38btPXGPgmwHA0RL1GabzMhEfVibHXnP0MicHCiawd3Rv4dQ/0?wx_fmt=jpeg)

# 服务器被黑后我认真做了加固：改SSH端口、禁root登录、装fail2ban、设强密码。 第二天服务器又挂了。同事指着日志说。。。

原创

权限提升中
权限提升中

黑客技术与网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

某个周五的凌晨3点，监控系统疯狂报警，我被电话叫醒。打开电脑一看，生产环境3台服务器CPU使用率全部飙到100%。当时第一反应是业务量暴增？登上服务器一看，top里面赫然躺着几个从没见过的进程名，占用率高达98%。

![](https://mmbiz.qpic.cn/mmbiz_png/Skw2xH7iae22sfOzDGw0OX5PAq8AgUQRqVBTRuFjAMe6qJ0q4ichHrziamQbZt7w70iaf7liat8DhxF8dcSnYKpibFv9ZhjAu0nPzibCOaSU69wRoU/640?wx_fmt=png&from=appmsg)

说实话，那一刻心里是凉的。服务器被黑了。后来排查发现是挖矿病毒，攻击者通过一个老版本Redis的未授权访问漏洞进来的。这次事件让我们团队彻底重视了安全问题。

前不久，导师实验室的服务器也突然出现异常，CPU持续空转，任务却不见进展。导师找来帮忙处理，第一反应就是：大概率是被挖矿了。果不其然，前后花了近两周时间，才终于把病毒清理干净。这次遇到的挖矿程序非比寻常，隐藏手段相当高明，普通方法很难察觉。

处理过这么多次入侵事件后，总结出5个最常见的入侵信号。

## 信号一：CPU长期100%爆表，空闲时也不降

这个每个人都遇到过。通过SSH远程连接服务器后，使用top和htop查看系统资源占用。尽管没有运行任何计算任务，CPU使用率却始终维持在90%左右——典型的挖矿症状。

```
# 按CPU使用率排序
ps aux --sort=-pcpu | head -20
```

与以往不同的是，这次病毒进程被刻意隐藏，普通命令难以直接发现踪迹。top命令下，CPU占用90%，但是显示没有大型计算程序在运行。

值得注意的是，连像htop这样的第三方工具都无法检测到异常进程，这通常意味着问题已不止于命令替换，而更可能是通过动态库劫持、系统调用挂钩等手段做了隐藏，严重时甚至可能侵入内核层面。

发现进程被隐藏后，查到如下两个命令可以一定程度上发现被隐藏的进程：

```
sysdig -c topprocs_cpu
unhide proc
```

可以看出这个挖矿程序占用了至少54个计算核心。进入挖矿进程的PID目录下，可看出该进程的运行信息。这里显示执行程序已被删除，因为进程正在内存中运行，而磁盘上的原始文件已被删除以消灭证据，所以ls -la /proc/[PID]/exe会显示(deleted)。

## 信号二：出现伪装进程，名字越正常越危险

服务器挖矿攻击（Cryptojacking）本质一句话：你的服务器等于黑客的免费矿机。攻击者入侵服务器后，偷偷运行挖矿程序，持续消耗你的CPU、内存和带宽来赚钱。

常见挖矿程序进程名：xmrig、kworker、sysupdate、watchdog。名字越正常越危险。

查看进程的真实可执行文件路径：

```
# 假设可疑进程PID是12345
ls -la /proc/12345/exe
# 这会显示实际的可执行文件路径，如果路径在/tmp下，基本就是恶意程序

cat /proc/12345/cmdline | tr '\0' ' '
```

重点排查这些目录下的可执行文件：/tmp、/dev/shm、/var/tmp。攻击者最常把木马丢在这几个地方。

至于为什么不要第一时间用kill删掉病毒进程，这是一个惨痛教训。排查时需要先通过cat /proc/[PID]/cmdline查看进程的完整启动命令，再用pstree -p [PID]追溯其父进程，确认是被Cron、Systemd还是其他方式启动的，这样才能找到自启根源。前前后后删了多次挖矿进程，所以每次挖矿进程的可执行程序的名字和PID都不一样，不过名字都是由8位的16进制数字组成。

## 信号三：异常外联，大量连接国外IP和矿池

挖矿程序需要连矿池，反弹shell需要连C2服务器。检查网络连接能发现很多问题：

```
netstat -natp
# 或者
ss -antup
```

发现了一个来自美国的IP和一堆欧洲IP链接，经过分析后，这个美国IP是黑客日常发送指令的位置，欧洲IP是接收挖矿密钥的位置。

常见高危异常端口：4444、9001、31337等常见后门端口。大量陌生IP、矿池域名。本地端口对外建立大量ESTABLISHED长连接——这几个都是明确的中招信号。

知道这些后，可以用防火墙对这些IP进行封禁：

```
# 封禁出站到恶意IP的连接（阻止挖矿程序连接矿池）
iptables -I OUTPUT -d IP -j DROP
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" destination address="IP" reject'
```

但是清理的时候要注意，有的病毒会篡改或清空iptables规则，甚至替换iptables二进制文件来干扰排查，遇到命令异常时可从相同系统环境的正常机器上拷贝原版可执行文件进行恢复。

## 信号四：定时任务里出现了不认识的东西，或者/etc/passwd多了新用户

攻击者入侵后优先创建隐藏特权账号，实现长期控制。UID=0：除root外其他账号均为恶意特权账号，可直接提权root。

```
# 查找UID=0特权账号（除root外全部可疑）
awk -F: '$3==0{print $1}' /etc/passwd

# 检查定时任务
crontab -l
cat /etc/crontab
ls /etc/cron.d/
ls /etc/cron.hourly/ /etc/cron.daily/
ls /var/spool/cron/

# 检查启动项
cat /etc/rc.local
systemctl list-unit-files --type=service | grep enabled
```

恶意Cron特征：每分钟执行wget/curl下载脚本、执行/tmp目录下未知二进制、后台静默运行挖矿程序。排查时发现hacker:x:0:0::/home/hacker:/bin/bash异常账号，UID为0且家目录/home/hacker下存在.bash\_history恶意下载、后门执行命令，判定为黑客创建后门账号。

与通常仅在Crontab中写入定时任务实现自启的病毒不同，有些挖矿程序更为隐蔽——它在系统中注入了Service服务，并对进程与目录进行了隐藏，使得常规排查手段难以发现，其隐藏手法可谓防不胜防。

## 信号五：日志里突然多了一堆境外IP的登录记录

查登录历史，尤其是那些半夜三更的成功登录：

```
# 查看登录历史
last -n 50
lastb -n 50   # 失败的登录尝试

# SSH暴力破解来源TOP20
# 注：CentOS/RHEL 日志路径为 /var/log/secure，Debian/Ubuntu 为 /var/log/auth.log
grep "Failed password" /var/log/secure | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -20
```

在后续日志审计中，也发现大量非常用用户名（例如maxwell等）的尝试登录记录。因此，除了强化密码和认证方式外，也建议尽量避免在服务器中使用知名人物、常见词汇或默认用户名作为账户名称。

## 清理步骤

确认被入侵后的处理顺序很重要，操作前建议先封禁所有已发现的恶意外联IP，必要时临时断开公网，防止攻击持续扩散：

1. 先清理定时任务 crontab -e，停掉恶意服务 systemctl stop xxx; systemctl disable xxx
2. 再结束恶意进程 kill -9 PID
3. 清理启动项
4. 删除恶意文件和目录
5. 删除后门用户
6. 封禁黑客IP

有个坑：有些恶意程序用chattr锁定文件，root都删不掉。系统提示Operation not permitted。解除方法：

```
chattr -i /etc/dns  # 先解锁
rm -rf /etc/dns     # 再删除
```

但是重启电脑之后，被关闭的病毒服务又回来了。需要完整地删除，先用journalctl -u <服务名>查看服务日志确认文件位置，再逐一用chattr解除锁定后删除。最后再利用kill -9将挖矿进程删掉，再次重启之后，挖矿服务才没有再次被启动。

## 预防措施

一方面是ssh远程登录没有禁用root的远程登录，此时需要在/etc/ssh/sshd\_config中添加PermitRootLogin no，保存后对ssh服务进行重启。有条件的用户将SSH登录方式改为RSA密钥认证，并禁用密码登录，这能够有效防范绝大多数爆破攻击。

另一个值得反思的问题是：很多人为了多台服务器之间的便捷通信，直接关闭了防火墙。实际上更安全的做法应是通过配置IP白名单，仅允许可信服务器IP进行连接，而非彻底放开权限。

服务器安全是一个持续的过程，需要我们在预防、检测、响应、恢复各个环节都做好充分准备。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mbeDyxcszeFEuUyG2oNmmc8TXvKs0FX3lwk2EglBrVibMgFQcMPAD6EZpFicPBZ9wesfJxU4rSyjbsQlku5gYb2Q/0?wx_fmt=png)

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