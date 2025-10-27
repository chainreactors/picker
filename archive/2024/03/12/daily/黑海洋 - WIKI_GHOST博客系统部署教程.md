---
title: GHOST博客系统部署教程
url: https://blog.upx8.com/4102
source: 黑海洋 - WIKI
date: 2024-03-12
fetch_date: 2025-10-04T12:12:34.381405
---

# GHOST博客系统部署教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# GHOST博客系统部署教程

发布时间:
2024-03-11

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
14017

## 前言

本教程不仅会介绍Ghost的安装与配置，更会针对我在搭建过程中所遇到的各种问题进行详细的解答。从域名购买到服务器搭建，再到主题选择和插件优化，我将全面详细的写出教程。无论你是技术上的小白，还是有一定经验的用户，都希望本教程能够对你有所启发。

> 在开始构建你的 GHOST 博客之旅之前，请务必心怀耐心和热情。技术世界中的探索与发现永无止境，并且建立自己的博客也是一段愉快而神奇的过程。

如果您在阅读过程中有任何疑问或困惑，请随时向我提问。

---

## 关于Ghost，为什么选择Ghost？

关于Ghost：[https://zh.wikipedia.org/zh-cn/Ghost\_(博客平台)](https://blog.upx8.com/go/aHR0cHM6Ly96aC53aWtpcGVkaWEub3JnL3poLWNuL0dob3N0XyglRTUlOEQlOUElRTUlQUUlQTIlRTUlQjklQjMlRTUlOEYlQjApP3JlZj1ob3N0ZXllLm5ldA)

> 我认为 GHOST 适合那些想要专注于创作内容的人。

它的设置非常简单，Ghost内置了针对SEO（加载速度等）的全面优化，可以让启动博客之前的学习和折腾个人的成本降低到最低。就我而言，我发现WordPress有点庞大……这很可能是我的问题，但（其中）Ghost 没有这样的问题。WP 最大的优点是有太多东西可以优化了，但这也是它最大的缺点。

对于没有搭建过博客的寻求者来说，使用Ghost搭建一个简洁的观看的博客，立刻就可以在这里面记录自己的学习和折腾过的各种事情。如果你想要控制完全能够调整网站的设计和功能，而且此时你已经对相关知识熟悉到一定程度，那么 Ghost 也提供了导出 JSON 的功能。后续将内容迁移到 wp 的时候，采用 RSS 路由或者 GhostJSON-to-WPXML 工具等方法也**非常**的**方便**。

至于Ghost内置的创建会员站点的功能，重点说一下。如果你有途径可以搞到Stripe账户，那么Ghost建立一个付费会员订阅系统非常的简单，几乎是一键式傻瓜操作。如果没有Stripe账户，那么在盈利方面，Ghost 没有那么强大的选择。

## 部署前的准备与选择

> Ghost提供了***托管***与***自托管***两种方案。

如果你对Linux有一定的了解，也花时间去学习折腾，最重要的是，手里有很多闲置的不知道愿意用来搞砸小鸡，那么我建议你选择自托管***。***对了，Ghost 支持 AMD和ARM。所以，闲置的甲骨文可以用来发光发热了。

此外我总结对比了自托管和托管方案的特点，如下：

| 特点 | 自托管 | 托管 |
| --- | --- | --- |
| 技术自由度 | 需要较高的技术知识，可以自定义设置和优化 | 相对较少技术要求，依赖托管服务提供商 |
| 成本控制 | 可以根据需求选择合适的服务器和套餐 | 套餐价格固定，可能相对较贵 |
| 技术挑战 | 需要处理服务器的安装、更新、备份等任务 | 免去繁琐的服务器管理，专注于内容创作 |
| 稳定性和可靠性 | 取决于自己服务器和配置的稳定性 | 由Ghost官方或可靠托管服务商提供稳定性和可靠性 |

这里我也展示一下官方做的对比图

![GHOST博客系统部署教程](https://www.nbmao.com/wp-content/uploads/replace/125f4faf30768aba2559165db7ca1f98.png)
> 面向群体及服务器选择

* **如果你是面向国内的博客，请优先选择 阿里云/腾讯云 等大厂的国内机器。**
* 不想要域名备案，可以选择 第三方商家位于香港、东京、圣何塞、法兰克福等有CN2 GIA/4837/9929 *国内优化的线路*的服务器。
* **如果你不考虑面向国内用户，**套上Cloudflare众生平等，那么你可以专注于性能和稳定性去选择合适的商家。

---

## 部署 - 托管方案

### 准备

* 域名一个（非必须）
* 可以支付外币的支付方式

### 云托管服务商选择

它不可以像静态博客一样使用 Vercel/Railway/Netfily 这类云平台托管，以下列出了一些支持的云平台。

* [Ghost (PRO](https://blog.upx8.com/go/aHR0cHM6Ly9naG9zdC5vcmcvcHJpY2luZy8_cmVmPWhvc3RleWUubmV0))
* **Digital Ocean**
* **Google Cloud**
* **PikaPods**
* …

详细的搭建步骤，等我有空更新。我们先把重点放到自托管方案。

## 部署 - 自托管方案

aa

### 准备

* 至少有 1GB 内存的服务器一台（荐使用全新的系统环境操作）
* 域名一个，并且已经提前设置一个有效的 DNS **A 记录**，指向服务器的 IP 地址。**必须提前完成此操作**
* SSH工具，例如 [Xshell](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubmV0c2FyYW5nLmNvbS9lbi94c2hlbGwvP3JlZj1ob3N0ZXllLm5ldA)、[FinalShell](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaG9zdGJ1Zi5jb20vP3JlZj1ob3N0ZXllLm5ldA)、[Termius](https://blog.upx8.com/go/aHR0cHM6Ly90ZXJtaXVzLmNvbS8_cmVmPWhvc3RleWUubmV0) 等

### 开始部署

如果你对 Docker相关命令已经了解，那么我推荐你使用 Docker 安装。缺点是如果你想在容器内使用现代化的编辑器来编辑文件会比较麻烦，最方便的是vim 等命令进行编辑、添加文件的操作。

如果你直接在服务器上搭建，就可以避免这个问题。我们可以非常方便的使用VScode 编辑文件内容。使用Termius的SFTP功能直接添加删除文件。

我将基于官方推荐的搭载了 `Ubuntu` 20.04 LTS 系统的服务器开始教程。

本教程将确保满足安装 Ghost-CLI 的所有先决条件。

### 1. 更新软件包

```
sudo apt update && apt upgrade -y
```

JAVASCRIPT

Copy

```
1.通过终端/软件连接SSH

2.更新系统软件包

sudo apt update && apt upgrade -y
```

JAVASCRIPT

Copy

### 2. 创建新用户

💡

**注意：用户名使用***`ghost`***会导致与Ghost-CLI冲突，你可以使用除***`ghost`***以外的任何名称**

```
1. 创建一个新用户，用户名需自行替换

adduser <user>
New password:
# 看到这个提示后，输入你想设置的密码。这里要注意，输入的密码是隐藏 不可见的，输入完毕后回车即可

Retype new password:
# 重新输入上一步的密码

Enter the new value, or press ENTER for the default
# 这里按回车默认
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:

Is the information correct? [Y/n]
# 这里确认信息输入正确后输入 y 并按下回车

2. 为新增用户添加 sudo 权限

usermod -aG sudo <user>
# 将<user>替换成你最开始设置的用户名

su - <user>
# 切换到这个用户
```

JAVASCRIPT

Copy

完整操作示例：

```
root@ns348668:~# adduser hosteye
Adding user `hosteye' ...
Adding new group `hosteye' (1001) ...
Adding new user `hosteye' (1001) with group `hosteye' ...
Creating home directory `/home/hosteye' ...
Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for hosteye
Enter the new value, or press ENTER for the default
Full Name []:
Room Number []:
Work Phone []:
Home Phone []:
Other []:
Is the information correct? [Y/n] y
root@ns348668:~# usermod -aG sudo hosteye
root@ns348668:~# su - hosteye
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
```

### 3.安装NGINX

💡

Ghost 使用 NGINX 服务器，SSL 配置需要 NGINX 1.9.5 或更高版本。

```
# 安装nginx
sudo apt-get install nginx
```

💡

如果`ufw`激活，防火墙应允许 HTTP 和 HTTPS 连接。

```
# 检查防火墙是否开启
sudo ufw status
```

```
# 如果防火墙开启，输入此命令允许 HTTP 和 HTTPS 连接。
sudo ufw allow 'Nginx Full'
```

```
Rules updated
Rules updated (v6)
# 开启成功后会输出此信息
```

### 4.安装MySQL

```
# 安装MySQL
sudo apt-get install mysql-server

# 进入mysql
sudo mysql

# 重置mysql root 密码
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<password>';

# 退出mysql
quit;
```

### 5.安装Node.js

![GHOST博客系统部署教程](https://www.nbmao.com/wp-content/uploads/replace/07098c0da4a6bd2e7ad0e8dcc0a6dd33.png)

💡

注意 Ghost 仅支持Node.js 16.x、18.x 两个大版本（推荐安装Node 18.x)

我这里选择安装18.x。

```
# 从 NodeSource 添加 Node.js 18 下载源
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash

# 安装 Node.js
sudo apt-get install -y nodejs
```

### 6.安装 Ghost-CLI

[Ghost-CLI](https://blog.upx8.com/go/aHR0cHM6Ly9naG9zdC5vcmcvZG9jcy9naG9zdC1jbGkvP3JlZj1ob3N0ZXllLm5ldA)是一个命令行工具，可帮助您快速、轻松地安装和配置 Ghost 以供使用。可以使用`npm`或`yarn`安装。

```
# 使用npm安装 Ghost-CLI
sudo npm install ghost-cli@latest -g

# 如果出现以下提示，这是 npm 存在新版本可升级的提示。这里可以自行选择是否需要升级。
npm notice
npm notice New minor version of npm available! 9.6.7 -> 9.8.1
npm notice Changelog: https://github.com/npm/cli/releases/tag/v9.8.1
npm notice Run npm install -g npm@9.8.1 to update!
npm notice
```

### 7.安装Ghost

一旦你的服务器正确设置并且`ghost-cli`安装完毕，就可以安装 Ghost 了。以下步骤是推荐的设置。如果您需要更精细的控制，请参考[Ghost-CLI](https://blog.upx8.com/go/aHR0cHM6Ly9naG9zdC5vcmcvZG9jcy9naG9zdC1jbGkvP3JlZj1ob3N0ZXllLm5ldA) 。

```
# 创建目录： 将 `sitename` 更改为站点名，或其他
sudo mkdir -p /var/www/sitename

# 设置目录所有者： 将 <user> 替换为一开始设置的用户名。 ！注意区分站点名和用户名
sudo chown <user>:<user> /var/www/sitename

# 设置正确的权限
sudo chmod 775 /var/www/sitename

# 然后进入
cd /var/www/sitename
```

现在我们用最后一个命令行安装 Ghost。

```
ghost install
```

```
# 以下是安装示例，请参考。
hosteye@ns348668:/var/www/hosteye$ ghost install

Love open source? We’re hiring JavaScript Engineers to work on Ghost full-time.
https://careers.ghost.org

# 检查系统环境
✔ Checking system Node.js version - found v18.17.0
✔ Checking current folder permissions
✔ Checking memory availability
✔ Checking free space
✔ Checking for latest Ghost version
✔ Setting up install directory
✔ Downloading and installing Ghost v5.55.1
✔ Finishing install process

# 输入你希望绑定的确切 URL，包括 HTTP 或 HTTPS 协议。例如，https://example.com. 如果使用 HTTPS，Ghost-CLI 将会设置 SSL。使用 IP 地址会导致错误。
? Enter your blog URL: https://hosteye.net

# 输入MySQL主机名。如果MySQL安装在其他服务器上，请手动输入对应主机名。
? Enter your MySQL hostname: localhost

# 输入 root ，然后输入 root 用户的密码。如果你已经有一个 MySQL 数据库，请输入对应的用户名和密码。
? Enter your MySQL username: root
? Enter your MySQL password: [hidden]

# 如果还没有创建过数据库，可以直接使用默认值： db_ghost 或者输入想要设置的数据库名。随后系统会开始自动设置。如果在上一步中使用的是非 root 的 MySQL用户名/密码，需要确保该数据库已经存在，并且具有正确的权限。
? Enter your Ghost database name: db_hosteye

✔ Configuring Ghost
✔ Setting up instance
+ sudo useradd --system --user-group ghost
+ sudo chown -R ghost:ghost /var/www/hosteye/content
✔ Setting up "ghost" system user

# 如果在此前提供了 root MySQL 用户，Ghost-CLI 可以自动创建一个属于 Ghost 数据库的自定义 MySQL 用户，该用户只能访问/编辑新的 Ghost 数据库，而不能执行其他操作。
# 输入y确定创建
? Do you wish to set up "ghost" mysql user? Yes
✔ Setting up "ghost" mysql user

# 自动设置NGINX
? Do you wish to set up Nginx? Yes
+ sudo mv /tmp/hosteye-net/hosteye.net.conf /etc/nginx/sites-available/hosteye.net.conf
+ sudo ln -sf /etc/nginx/sites-available/hosteye.net.conf /etc/nginx/sites-enabled/hosteye.net.conf
+ sudo nginx -s reload
✔ Setting up Nginx

# 自动设置SSL。要注意在第一步要输入带 https 的地址作为URL，并且正确配置了记录
? Do you wish to set up SSL? Yes

# SSL 认证设置需要一个电子邮件地址，以便你可以在证书出现任何问题（包括续订期间）时收到通知。
? Enter your email (For SSL Certificate) xxxxx@gmail.com
+ sudo mkdir -p /etc/letsencrypt
+ sudo ./acme.sh --install --home /etc...