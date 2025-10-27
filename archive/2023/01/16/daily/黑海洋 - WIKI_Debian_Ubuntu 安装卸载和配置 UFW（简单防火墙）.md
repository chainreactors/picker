---
title: Debian/Ubuntu 安装卸载和配置 UFW（简单防火墙）
url: https://blog.upx8.com/3180
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:51.608089
---

# Debian/Ubuntu 安装卸载和配置 UFW（简单防火墙）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Debian/Ubuntu 安装卸载和配置 UFW（简单防火墙）

发布时间:
2023-01-15

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
54078

## 前言

UFW 是一个 Arch Linux、De­bian 或 Ubuntu 中管理防火墙规则的前端，可大大简化防火墙的配置过程。

## 安装 UFW

如还没有安装，可以使用 apt 命令来安装

**1、更新软件包**

```
sudo apt update
```

**2、安装 UFW**

```
sudo apt install ufw
```

**3、如果你在远程位置连接你的服务器，在启用 UFW 防火墙之前，你必须显式允许进来的 SSH 连接。否则，你将永远都无法连接到机器上。**

```
sudo ufw allow 22/tcp
```

> 如果 SSH 运行在非标准端口，你需要将上述命令中的 22 端口替换为对应的 SSH 端口。

**4、启动 UFW**

```
sudo ufw enable
```

在使用前，你应该检查下 UFW 是否已经在运行。

```
ufw status        #查看防火墙状态
ps -ef|grep xxxx  #查看服务状态
```

如果你发现状态是 `inactive` ，意思是没有被激活或不起作用。

## 启用/禁用（重启防火墙）

```
ufw enable   #启用
ufw disable  #禁用
```

**#防火墙解除（甲骨文云）**

```
开放所有端口
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -F

Ubuntu镜像默认设置了Iptable规则，关闭它
apt-get purge netfilter-persistent
reboot
或者强制删除
rm -rf /etc/iptables && reboot
```

## 使用与配置

### 列出当前UFW规则

```
ufw status verbose
```

### 添加规则

#### 允许入站（allow）

默认情况，没有允许就是拒绝（入站），使用 `ufw allow <端口>` 来添加允许访问的端口或协议。

```
ufw allow smtp　             #允许所有的外部IP访问本机的25/tcp (smtp)端口
ufw deny smtp 　             #禁止外部访问smtp服务
ufw allow 22/tcp 　          #允许所有的外部IP访问本机的22/tcp (ssh)端口
ufw allow 2333/tcp 　        #添加2333端口，仅TCP协议
ufw allow 6666/udp 　        #添加6666端口，仅UDP协议
ufw allow 8888:9999 　       #添加8888到9999之间的端口
ufw delete allow smtp 　     #删除上面建立的某条规则
ufw allow ssh 　             #添加22端口
ufw allow http 　            #添加80端口
ufw allow https 　           #添加443端口
ufw allow 53 　              #允许外部访问53端口(tcp/udp)
ufw allow from 192.168.1.100 　 #允许此IP访问所有的本机端口
ufw allow proto udp 192.168.0.1 port 53 to 192.168.0.2 port 53
sudo ufw deny from 192.168.1.100                  #要封禁 IP 地址 192.168.1.100
sudo ufw deny from 192.168.1.100 to any port 22   #限制某个特定IP和端口的访问
sudo ufw delete deny from 192.168.1.100           #删除指定限制的IP
```

#### 拒绝访问（deny）

使用 `ufw deny <端口>` 来添加拒绝入站的端和协议，与添加允许的类似。

### 删除规则

先使用 `ufw status` 查看规则，再使用 `ufw delete [规则] <端口>` 来删除规则。

```
ufw delete allow 2333/tcp
```

如果你有很多条规则，使用 `numbered` 参数，可以在每条规则上加个序号数字。

然后使用 `ufw delete <序号>` 来删除规则。

```
root@p3terx:~# ufw status numbered  #列出规则，并加上序号。
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 20,21,22,80,888,8888/tcp   ALLOW IN    Anywhere
[ 2] 39000:40000/tcp            ALLOW IN    Anywhere
[ 3] 8896/tcp                   ALLOW IN    Anywhere
[ 4] 8896/udp                   ALLOW IN    Anywhere
[ 5] 443/tcp                    ALLOW IN    Anywhere
[ 6] 20,21,22,80,888,8888/tcp (v6) ALLOW IN    Anywhere (v6)
[ 7] 39000:40000/tcp (v6)       ALLOW IN    Anywhere (v6)
[ 8] 8896/tcp (v6)              ALLOW IN    Anywhere (v6)
[ 9] 8896/udp (v6)              ALLOW IN    Anywhere (v6)
[10] 443/tcp (v6)               ALLOW IN    Anywhere (v6)

root@p3terx:~# ufw delete 4  #删除上面的第4条规则
Deleting:
 allow 8896/udp
Proceed with operation (y|n)? y  #最后会询问你是否进行操作
```

# Ubuntu卸载firewalld防火墙

使用root权限卸载firewalld，先禁用防火墙，然后卸载firewalld，命令依次如下：

**1.查找防火墙的全称：**

```
dpkg --list|grep "fire*"
```

**2.禁用防火墙firewalld：**

```
systemctl disable firewalld
systemctl stop firewalld
```

**禁用ufw：**

```
ufw disable
```

**3.卸载防火墙：**

```
sudo apt-get --purge remove firewalld
```

# 使用 UFW 禁止 ICMP 协议访问（禁 ping）

## 打开 UFW 配置文件

```
vim /etc/ufw/before.rules
```

## 修改配置

允许 ping

```
-A ufw-before-input -p icmp --icmp-type echo-request -j ACCEPT
```

禁止 ping

```
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP
```

## 让配置生效

```
ufw reload
```

---

以上都是一些简单常用的一些命令，想要深入了解，可以输入 `man ufw` 查看 ufw 用户手册。

1. **[Ubuntu和Debian 初始化](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudXB4OC5jb20vMzEyMA)**

   2024-08-17 23:35:00

   [回复](https://blog.upx8.com/3180/comment-page-1?replyTo=30071#respond-post-3180)

   [...]最近来来回回折腾了上百次服务器，每次折腾总要做一些重复的操作，挺麻烦，干脆记录一些常用操作，方便日后复制粘贴。一键网络DD脚本重装系统组件：apt-get install -y xz-utils openssl gawk file wget screen && screen -S os一键DD脚本：wget --no-check-certificate -O NewReinstal[...]
2. **[Ubuntu和Debian 初始化](https://blog.upx8.com/3120)**

   2024-06-06 13:59:13

   [回复](https://blog.upx8.com/3180/comment-page-1?replyTo=29703#respond-post-3180)

   [...]最近来来回回折腾了上百次服务器，每次折腾总要做一些重复的操作，挺麻烦，干脆记录一些常用操作，方便日后复制粘贴。一键网络DD脚本重装系统组件：apt-get install -y xz-utils openssl gawk file wget screen && screen -S os一键DD脚本：wget --no-check-certificate -O NewReinstal[...]

[取消回复](https://blog.upx8.com/3180#respond-post-3180)

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