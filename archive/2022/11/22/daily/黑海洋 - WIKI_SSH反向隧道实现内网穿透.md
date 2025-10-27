---
title: SSH反向隧道实现内网穿透
url: https://blog.upx8.com/3106
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:14.428783
---

# SSH反向隧道实现内网穿透

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# SSH反向隧道实现内网穿透

发布时间:
2022-11-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
12837

## 一、前言

网络上有很多强大的内网穿透软件，但对于某些很简单的需求来说可以通过SSH来实现更为方便。

## 二、配置

配置思路：在 A 机器上做到 B 机器的反向代理；在 B 机器上做正向代理本地端口转发。

| 主机编号 | IP地址 | 用户名 | 备注 |
| --- | --- | --- | --- |
| A | A.A.A.A | usera | 客户端 |
| B | B.B.B.B | userb | 服务器 |

1. 建立客户端A到服务器B的反向代理(在客户端A上操作)

   ```
   ssh -CNR 8081:localhost:80 userb@B.B.B.B

   # 8081为服务器B端口，用来与客户端A的80端口绑定。
   # 可通过 -f 参数实现后台运行
   ```

   到这里客户端A的80端口已经映射到服务器B的8081端口，可以在通过服务器B的8080端口访问客户端A的80端口，但注意只支持服务器B本地访问。
2. 建立服务器B上的正向代理用作本地转发(在服务器B上操作)
   因为绑定后的端口只支持服务器B本地访问，所以我们需要把已经映射的端口转发出去。

   ```
   ssh -CNL "*:8080:localhost:8081' localhost

   # 8080为本地转发端口,将数据转发到先前已经映射的8081端口，实现外网访问。
   # 其中的*表示接受来自任意机器的访问。
   # 可通过 -f 参数实现后台运行
   ```

   现在可以通过服务器B的8080端口访问到客户端A的80端口。
3. 实现持久化连接和无密码登陆
   我们配置完代理后可以正常使用了，但不幸的是这种ssh反向连接会因为超时而关闭，如果关闭了那从外网连通内网的通道就无法维持了，为此我们需要另外的方法来提供稳定的ssh反向代理隧道。

   * 无密码登陆
     a.通过设置KEY登陆(操作略)
     b.使用sshpass命令(需安装)：
     `sshpass -p "ssh密码" ssh -CNR 8081:localhost:80 userb@B.B.B.B`
     c.使用plink工具连接(windows)：
     `plink.exe -pw "ssh密码" ssh -CNR 8081:localhost:80 userb@B.B.B.B`
   * 用autossh(需安装)建立稳定隧道
     autossh的参数与ssh的参数是一致的，但是不同的是在隧道断开的时候，autossh会自动重新连接而ssh不会；另外不同的是 `-M` 参数，该参数指定一个端口用于外网的主机用来接收内网主机的信息，若隧道不正常则返回给内网主机重新连接。

     ```
     autossh -M 5678 -f -CNR 8081:localhost:80 userb@B.B.B.B
     # 参数 -f 为后台运行
     ```

     可使用sshpass与autossh组合使用：

     ```
     sshpass -p "ssh密码" autossh -M 5678 -CNR 8081:localhost:80 userb@B.B.B.B
     ```

     注：使用sshpass，那么autossh不能加-f参数，因为sshpass需要autossh在前台请求密码才能实现输入(这点和expect差不多)，而加上-f参数放后台后会无效，所以若要使用sshpass请务必不要加-f参数，建议使用autossh然后配合-i参数使用用key认证登陆。 最后可以把命令加入开机启动项实现开机启动。
4. 附 SSH命令参数说明

   ```
   -f 后台运行 -C 允许压缩数据 -N 不执行任何命令 -R 将端口绑定到远程服务器，反向代理 -L 将端口绑定到本地客户端，正向代理
   ```

[取消回复](https://blog.upx8.com/3106#respond-post-3106)

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