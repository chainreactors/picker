---
title: Oracle 甲骨文云闲置实例资源保活教程
url: https://buaq.net/go-149048.html
source: unSafe.sh - 不安全
date: 2023-02-13
fetch_date: 2025-10-04T06:27:28.539372
---

# Oracle 甲骨文云闲置实例资源保活教程

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

![](https://8aqnet.cdn.bcebos.com/78bcffa96416736ce35c6efaa0d7b7a8.jpg)

Oracle 甲骨文云闲置实例资源保活教程

甲骨文云从最初的AMD服务器，到现在的高配ARM服务器。这一波确实非常良心了！但是由于很多龟友闲置资源，导致甲骨文从去年底开始酝酿清理闲置资源的方式，这
*2023-2-12 17:55:0
Author: [blog.upx8.com(查看原文)](/jump-149048.htm)
阅读量:91
收藏*

---

甲骨文云从最初的AMD服务器，到现在的高配ARM服务器。这一波确实非常良心了！但是由于很多龟友闲置资源，导致甲骨文从去年底开始酝酿清理闲置资源的方式，这次终于出详细规则了！

早在去年2022年11月16日，甲骨文云官方突然新增说明：

> *从 2022 年 11 月 24 日开始，您闲置的 Always Free 计算实例可能会停止。 详细了解此过程以及如何重启您的实例。 您还可以随时升级您的帐户以避免中断。*
>
> *仅限未付费的免费套餐帐户。Idle Always未付费免费套餐帐户的免费资源可以随时回收，恕不另行通知。回收包括停止或终止等操作。*

![](https://cnboy.org/wp-content/uploads/b1dfde9f6f719f2-700x275.jpg "Oracle 甲骨文云闲置实例资源保活教程第1张-CNBoy 四海部落")

但是就在发布的3天后11月19日，该说明突然消失了。

就在2023年1月底，甲骨文云又再次出现类似的说明。

> 空闲计算实例的回收Idle Always Free计算实例可能会被 Oracle 回收。如果在 7 天内满足以下条件，则 Oracle 会将虚拟机和裸机计算实例视为空闲：
>
> * 95%时间CPU利用率低于10%
> * 网络利用率低于10%
> * 内存利用率低于 10% （仅适用于A1 形状）（ARM实例）

这次公告明确了具体回收闲置资源的规则，CPU / 网络 / 内存 都不符合要求会回收计算实例，账号不影响，回收后应该能再开新实例。看来是要玩真的了。

规则一出，众多的大佬也就开始出手，纷纷给出了自己的练龟绝技。下面就整理一下比较不错的几个，提供给龟友们。

### Oracle Keep Alive【Shuaibsport】

这是来自于一个G友帅比大佬的作品，所以博主在这也送它一个更特别的名字 **Shuaibsport 。**脚本同时对CPU、内存（仅`ARM`）、网络三项进行锻炼，使用非常简单。所以就放在第一位向大家介绍下。

**Shuaibsport 2.0**：脚本内已设定每天定时运行6个小时，卸载方式更简单

**复制

```
curl -skLO https://odcf.eu.org/oracle_keepalive.sh && bash oracle_keepalive.sh
或
wget https://github.com/Glory-CNBoy/oracle_keep_alive/raw/main/Shuaibi/keepalive2.sh && bash keepalive2.sh
```

**Shuaibsport 1.0**：脚本持续运行，如需定时，可根据自己需要通过cron设置启动及停止时间

**复制

```
wget https://github.com/Glory-CNBoy/oracle_keep_alive/raw/main/Shuaibi/keepalive.sh && bash keepalive.sh
```

**Shuaibsport-light**：这是博主根据大佬1.0版本修改自用的。CPU、内存设定在甲骨文的标准下限临界值上，网络占用非常低。所以仅适用于已有项目在运行但达不到标准，同时也不想影响到自用项目网络的龟友。

**复制

```
wget https://github.com/Glory-CNBoy/oracle_keep_alive/raw/main/Shuaibi/keepalive-light.sh && bash keepalive-light.sh
```

**复制

```
# 停止：
systemctl stop cpur

# 重启：
systemctl restart cpur

# 释放内存：
umount /ramdisk

# 完全卸载命令【适用于 1.0 及 light 版】：
systemctl disable cpur --now
sed -i '/\/opt\/shuaibi\/mem.sh/d' /etc/crontab
umount /ramdisk &>/dev/null
rm -rf /opt/shuaibi
rm keepalive**

# 2.0 版的卸载非常简单：
传入任意位置变量，比如：bash oracle_keepalive.sh 233 或是 bash keepalive2.sh 233 ，即可
```

### Keepoccupied

出自于Hostloc论坛sesr大佬，原贴地址：《[甲骨文保持占用](https://hostloc.com/thread-1132162-1-1.html)》 。在此博主将其`ARM`命令与`AMD`命令整合到一个脚本中，由脚本自行判断，对CPU、内存（仅`ARM`）、网络三项进行锻炼。

**运行命令**

**复制

```
wget https://github.com/Glory-CNBoy/oracle_keep_alive/raw/main/Sesr/keepoccupied.sh && bash keepoccupied.sh
```

**复制

```
# 停止：
systemctl stop KeepCPUMemory.service KeepNetwork.service
或
reboot   #直接重启也能停掉

# 完全卸载命令：
sudo systemctl stop KeepCPUMemory.service KeepNetwork.service && \
sudo systemctl disable KeepCPUMemory.service KeepNetwork.service && \
sudo rm /etc/systemd/system/KeepCPUMemory.service /etc/systemd/system/KeepNetwork.service && \
sudo rm /etc/systemd/system/multi-user.target.wants/KeepCPUMemory.service /etc/systemd/system/multi-user.target.wants/KeepNetwork.service && \
sudo rm keepoccupied.sh
```

### NeverIdle

龟龟的锻炼量（时间、项目等）均可以根据自己的情况随心调节。

项目地址：<https://github.com/layou233/NeverIdle>

**复制

```
# 服务器安装 wget screen
yum install -y wget screen

# 下载编译后的可执行文件
# AMD服务器
wget https://github.com/layou233/NeverIdle/releases/download/0.1/NeverIdle-linux-amd64 -O NeverIdle
# ARM
wget https://github.com/layou233/NeverIdle/releases/download/0.1/NeverIdle-linux-arm64 -O NeverIdle

# 修改文件权限
chmod 777 NeverIdle

# 使用screen运行程序
screen -R baohuo

# 启动程序
./NeverIdle -c 2h -m 2 -n 4h

# 挂起screen 按 Ctrl+A+D

# 再次进入screen
screen -R baohuo
```

**复制

```
启动程序的命令参数详解：

-c 指启用 CPU 定期浪费，后面跟随每次浪费的间隔时间。
   如每 12 小时 23 分钟 34 秒浪费一次，则为 12h23m34s。按照格式填。

-m 指启用浪费的内存量，后面是一个数字，单位为 GiB。
   启动后会占用对应量的内存，并且保持不会释放，直到手动杀死进程。

-n 指启用网络定期浪费，后面跟随每次浪费的间隔时间。
   格式同 CPU。会定期执行一次 Ookla Speed Test（还会输出结果哦！）

启动该程序后即立刻执行一次你配置的所有功能，可以观察效果。
```

### 计算圆周率

这一个也出自于Hostloc论坛的大佬（[原贴直达](https://hostloc.com/thread-1131769-1-1.html)），但是这个只锻炼CPU。

**复制

```
nohup echo "scale=99999999;4*a(1)" | bc -lq > /dev/null &
nohup cpulimit -l 30 -p 22489 >/dev/null &

scale那个代表小数点后的位数，数越大计算时间越长 -l 那里可以控制cpu使用率0-200 -p 那里写程序的PID，通过 top 命令查找，或者 ps -aux | grep bc

# 直接shell死循环也可以
nohup cpulimit -l 30 bash -c "while :;do a=1;done" > /dev/null 2>&1 &
```

当然，方法还有很多，目的也都是让吃灰的龟龟跑起来，不再“吃灰”！

最后，博主想说的也就是：**再好的保活教程也不如自己真实使用！毕竟现在免费的资源越来越少了，所以还是建议大家别浪费云服务器多多利用起来！**

文章来源: https://blog.upx8.com/3222
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)