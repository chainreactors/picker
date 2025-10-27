---
title: aws的ec2如何dd系统到debian11
url: https://blog.upx8.com/3094
source: 黑海洋 - WIKI
date: 2022-11-19
fetch_date: 2025-10-03T23:13:43.527529
---

# aws的ec2如何dd系统到debian11

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# aws的ec2如何dd系统到debian11

发布时间:
2022-11-18

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
13039

前言：dd系统有风险，极易造成机器失联，本教程经实则，可正常ddaws的ec2为Debian11的系统，里面涉及多个重要IP填写，请一定认真核对；**个人不对dd失败造成机器失联负责；个人不对dd失败造成机器失联负责；个人不对dd失败造成机器失联负责。**

## 所要获取的参数

IP
子网掩码
网关

## 1.获取ip地址

ssh输入 `ip addr`
![ip地址](https://cdn.jsdelivr.net/gh/Netflixxp/pic/img/202109062101612.png "ip地址")

## 2.获取子网掩码

ssh输入 `ifconfig`
如果报错，见下图
![报错](https://cdn.jsdelivr.net/gh/Netflixxp/pic/img/202109062102799.png "报错")
那么输入 `apt install -y net-tools`
安装完再输入一次`ifconfig`

## 3.获取网关

`route -n`
![获取网关](https://cdn.jsdelivr.net/gh/Netflixxp/pic/img/202109062104427.png "获取网关")

## 4.执行以下脚本

`wget --no-check-certificate -qO InstallNET.sh 'https://moeclub.org/attachment/LinuxShell/InstallNET.sh' && chmod a+x InstallNET.sh && bash InstallNET.sh -d 11 -v 64 -a --ip-addr 172.31.XX.XXX --ip-gate 172.31.XX.X --ip-mask 255.255.240.0 --mirror 'http://mirror.xtom.com.hk/debian/'`

**代码里面XX的参数根据自己的自行更换**
ip-addr :IP Address/IP地址

ip-gate :Gateway /网关

ip-mask :Netmask /子网掩码

## 5.记得改密码

默认密码为 `MoeClub.org`
十分钟左右就可以完成安装，连接上机器第一件事就是修改默认密码，以免造成不必要的损失
更改密码方式为
输入`passwd`
然后盲输两次一样的新密码。

[取消回复](https://blog.upx8.com/3094#respond-post-3094)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")