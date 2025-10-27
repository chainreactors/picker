---
title: 在Linux上使用GoogleAuthenticator登陆SSH
url: https://blog.upx8.com/3108
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:13.913277
---

# 在Linux上使用GoogleAuthenticator登陆SSH

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 在Linux上使用GoogleAuthenticator登陆SSH

发布时间:
2022-11-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
14070

## 一、简介

谷歌验证（Google Authenticator）通过两个验证步骤，在登录时为用户的谷歌帐号提供一层额外的安全保护。使用谷歌验证可以直接在用户的设备上生成动态密码，无需网络连接。特点：自动生成QR码；支持多帐户；支持通过time-based和counter-based生成。

## 二、安装

在CentOS上安装Google身份验证器服务器端组件(需先启用EPEL软件库)：

```
yum install google-authenticator
```

在 Ubuntu 上安装Google身份验证器服务器端组件：

```
sudo apt-get install libpam-google-authenticator
```

在 Fedora 上安装Google身份验证器服务器端组件：

```
dnf install google-authenticator
```

编译安装：
从 GitHub 下载源代码手动编译，具体编译方法请参照 GitHub 上的说明。
项目地址：`https://github.com/google/google-authenticator-libpam`

```
git clone https://github.com/google/google-authenticator.git
cd google-authenticator/libpam/
./bootstrap.sh
./configure
make && make install
cp .libs/pam_google_authenticator.so /lib64/security/
```

## 三、配置

1. 添加谷歌身份验证器PAM模块
   在/etc/pam.d/sshd文件最后添加谷歌身份验证器PAM模块配置：
   `auth required pam_google_authenticator.so`
   或使用如下命令在/etc/pam.d/sshd文件添加认证模块：
   `echo "auth required pam_google_authenticator.so" >>/etc/pam.d/sshd`
2. 配置挑战式密码认证
   在/etc/ssh/sshd\_config文件中添加以下行，如果已配置则将参数更改为“yes”：
   `ChallengeResponseAuthentication yes`
   或使用命令更改：
   `sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config`
3. 重启sshd服务

   ```
   #CentOS7
   systemctl restart sshd.service
   #CentOS6
   service sshd restart
   ```

## 三、使用两步验证登陆

新开一个会话测试SSH登陆：
服务器会提示首先输入服务器的密码，接着会让输入Google验证器生成的密钥，当两者都正确时才能成功登录服务器。

注意事项：
1.验证器时间必须和服务器时间同步。
2.如果你是远程登录到服务器上配置，切勿退出当前的SSH 会话，而应该另外开一个会话去测试SSH登录，重启不会中断当前的 SSH 会话。

[安装脚本下载](https://blog.upx8.com/go/aHR0cHM6Ly93d3dmY3d5cy5vc3MtY24tc2hlbnpoZW4uYWxpeXVuY3MuY29tL3R5cGVjaG8vMjAxOC8wNi8yNC9nb29nbGUtYXV0aC1pbnN0YWxsLnppcA)

## 附、小程序版OTP验证器

灵动验证器是一款方便快捷的动态密码小程序。离线计算动态口令无需联网，本地备份动态口令，支持启动密码等功能。扫描下方小程序码即可使用。
[![灵动验证器](https://s2.ax1x.com/2020/01/18/1pMgNn.jpg)](https://s2.ax1x.com/2020/01/18/1pMgNn.jpg)

[取消回复](https://blog.upx8.com/3108#respond-post-3108)

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