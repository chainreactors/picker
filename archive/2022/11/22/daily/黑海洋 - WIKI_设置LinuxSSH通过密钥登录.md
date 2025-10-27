---
title: 设置LinuxSSH通过密钥登录
url: https://blog.upx8.com/3103
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:15.138578
---

# 设置LinuxSSH通过密钥登录

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 设置LinuxSSH通过密钥登录

发布时间:
2022-11-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
11951

## 一、制作密钥对

首先在服务器上制作密钥对。用密码登录到你打算使用密钥登录的账户，然后执行以下命令：

```
[root@host ~]$ ssh-keygen       //建立密钥对
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): //按Enter
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase):     //输入密钥锁码，或直接按 Enter 留空
Enter same passphrase again:    //再输入一遍密钥锁码
Your identification has been saved in /root/.ssh/id_rsa   //私钥
Your public key has been saved in /root/.ssh/id_rsa.pub   //公钥
The key fingerprint is:
0f:d3:e7:1a:1c:bd:5c:03:f1:19:f1:22:df:9b:cc:08 root@host
```

密钥锁码在使用私钥时必须输入，这样就可以保护私钥不被盗用。当然，也可以留空，实现无密码登录。
现在，在 root 用户的家目录中生成了一个 .ssh 的隐藏目录，内含两个密钥文件。id\_rsa 为私钥，id\_rsa.pub 为公钥。

## 二、在服务器上安装公钥

* 使用ssh-copy-id安装：
  `ssh-copy-id -i 公钥文件 用户名@主机 -p 端口`
  如：`ssh-copy-id -i .ssh/id_rsa.pub root@192.168.10.100`
* 手动安装：
  键入以下命令，在服务器上安装公钥：

  ```
  [root@host ~]$ cd .ssh
  [root@host .ssh]$ cat id_rsa.pub >> authorized_keys
  ```

  如此便完成了公钥的安装。为了确保连接成功，请保证以下文件权限正确：

  ```
  [root@host .ssh]$ chmod 600 authorized_keys
  [root@host .ssh]$ chmod 700 ~/.ssh
  ```

## 三、设置SSH打开密钥登录功能

编辑 /etc/ssh/sshd\_config 文件，进行如下设置：

```
RSAAuthentication yes
PubkeyAuthentication yes
```

另外，请留意 root 用户能否通过 SSH 登录：`PermitRootLogin yes`
当你完成全部设置，并以密钥方式登录成功后，再禁用密码登录：`PasswordAuthentication no`
最后，重启 SSH 服务：`[root@host .ssh]$ service sshd restart`

## 四、使用密钥登录

将私钥下载到客户端，然后转换为 PuTTY 能使用的格式
使用 WinSCP、SFTP 等工具将私钥文件 id\_rsa 下载到客户端机器上。然后打开 PuTTYGen，单击 Actions 中的 Load 按钮，载入你刚才下载到的私钥文件。如果你刚才设置了密钥锁码，这时则需要输入。
载入成功后，PuTTYGen 会显示密钥相关的信息。在 Key comment 中键入对密钥的说明信息，然后单击 Save private key 按钮即可将私钥文件存放为 PuTTY 能使用的格式。
以后当你使用 PuTTY 登录时，可以在左侧的 Connection -> SSH -> Auth 中的 Private key file for authentication:处选择你的私钥文件，然后即可登录了，过程中只需输入密钥锁码即可。

[取消回复](https://blog.upx8.com/3103#respond-post-3103)

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