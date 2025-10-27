---
title: 【Python】用Python和Paramiko实现远程服务器自动化管理
url: https://blog.csdn.net/nokiaguy/article/details/144238330
source: 一个被知识诅咒的人
date: 2024-12-05
fetch_date: 2025-10-06T19:37:07.929763
---

# 【Python】用Python和Paramiko实现远程服务器自动化管理

# 【Python】用Python和Paramiko实现远程服务器自动化管理

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-12-04 13:38:56 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量908
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

12

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
33

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
[运维](https://blog.csdn.net/nokiaguy/category_11917999.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[服务器](https://so.csdn.net/so/search/s.do?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[自动化](https://so.csdn.net/so/search/s.do?q=%E8%87%AA%E5%8A%A8%E5%8C%96&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/144238330>

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在现代IT环境中，远程服务器管理已成为运维工作的常态。随着自动化运维的需求不断增加，如何高效地管理远程服务器，提升操作的灵活性和效率，成为了运维人员的核心课题。本文将介绍如何使用Python的Paramiko库来实现远程服务器的管理与自动化脚本编写。文章将详细讲解Paramiko的安装与配置，如何通过SSH协议与远程服务器进行通信，以及如何编写自动化脚本来执行命令、传输文件、批量管理服务器等操作。通过大量的代码示例和详细解释，读者可以快速掌握如何使用Python进行远程管理，提升运维效率和可靠性。

---

#### 1. 引言

随着云计算和虚拟化技术的广泛应用，越来越多的服务器被部署在远程数据中心或云平台中。传统的人工操作已经无法满足大规模服务器管理的需求，因此，自动化运维成为了提升工作效率的关键。Python作为一种强大的脚本语言，其丰富的库和良好的扩展性使得它成为自动化运维中的首选工具。

在众多用于远程管理的库中，**Paramiko**是一个非常流行的选择，它支持通过SSH协议连接远程服务器，执行命令，传输文件等操作。本篇文章将通过详细的实例，介绍如何使用Python和Paramiko库来实现远程服务器管理和自动化操作。

---

#### 2. Paramiko简介

**Paramiko**是一个用于在Python中处理SSH2协议的库。通过Paramiko，用户可以通过SSH连接到远程服务器，执行命令，传输文件等操作。Paramiko主要提供以下功能：

* **SSH客户端功能**：可以通过SSH协议连接远程服务器，执行命令，并获取执行结果。
* **SFTP功能**：支持文件传输，可以通过SFTP协议上传、下载文件。
* **密钥认证**：支持公钥和私钥认证，提供比密码认证更安全的连接方式。

#### 3. 安装Paramiko

首先，我们需要安装Paramiko库。可以使用`pip`命令进行安装：

```
pip install paramiko
```

安装完成后，便可以在Python中导入并使用Paramiko库进行远程服务器管理。

#### 4. 使用Paramiko连接远程服务器

在使用Paramiko之前，我们需要了解如何通过SSH连接到远程服务器。以下是一个基本的示例，展示了如何使用Paramiko通过SSH连接到远程服务器，并执行命令。

```
import paramiko

# 创建SSH客户端实例
client = paramiko.SSHClient()

# 自动添加SSH主机密钥
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程服务器
hostname = 'your_server_ip'
port = 22  # SSH默认端口为22
username = 'your_username'
password = 'your_password'

client.connect(hostname, port, username, password)

# 执行命令
stdin, stdout, stderr = client.exec_command('uptime')

# 获取命令输出
print(stdout.read().decode())

# 关闭连接
client.close()
```

在这段代码中，首先创建了一个`SSHClient`实例，用于与远程服务器建立连接。接着，使用`set_missing_host_key_policy(paramiko.AutoAddPolicy())`方法来自动添加SSH主机密钥，这样即使是第一次连接该服务器也不会出现验证错误。然后，我们通过`client.connect()`方法连接远程服务器，并使用`exec_command()`方法执行远程命令，最后获取命令的输出并打印。

#### 5. 使用SSH密钥认证

除了使用用户名和密码进行认证外，SSH密钥认证是一种更安全的认证方式。使用密钥认证时，远程服务器会存储用户的公钥，而客户端则使用对应的私钥进行身份验证。

##### 5.1 配置密钥认证

首先，生成一对SSH密钥对（公钥和私钥）。可以使用`ssh-keygen`命令生成密钥对：

```
ssh-keygen -t rsa -b 2048
```

该命令会在`~/.ssh/`目录下生成`id_rsa`（私钥）和`id_rsa.pub`（公钥）两个文件。将公钥`id_rsa.pub`复制到远程服务器的`~/.ssh/authorized_keys`文件中：

```
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

##### 5.2 使用密钥认证连接

在Python中使用Paramiko连接远程服务器时，可以通过`paramiko.RSAKey`来加载私钥进行认证。

```
import paramiko

# 创建SSH客户端实例
client = paramiko.SSHClient()

# 自动添加SSH主机密钥
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 加载私钥
private_key_path = '/path/to/your/private/key/id_rsa'
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# 连接远程服务器
hostname = 'your_server_ip'
port = 22
username = 'your_username'

client.connect(hostname, port, username, pkey=private_key)

# 执行命令
stdin, stdout, stderr = client.exec_command('uptime')

# 获取命令输出
print(stdout.read().decode())

# 关闭连接
client.close()
```

在此示例中，我们使用`paramiko.RSAKey.from_private_key_file()`方法加载私钥，随后通过密钥认证连接远程服务器。

#### 6. 使用SFTP上传下载文件

Paramiko还提供了SFTP功能，可以用来上传和下载文件。以下是一个简单的SFTP文件传输示例：

##### 6.1 上传文件

```
import paramiko

# 创建SSH客户端实例
client = paramiko.SSHClient()

# 自动添
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/2ccacbf1fc8347338ede60bde7fb2eec_nokiaguy.jpg!1)

蒙娜丽宁](https://unitymarvel.blog.csdn.net)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  33

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  12

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

参与评论
您还未登录，请先
登录
后发表或查看评论

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[AIGC撕裂劳动力市场：技术狂潮下，人类将走向乌托邦还是深渊？](https://unitymarvel.blog.csdn.net/article/details/145234235)

01-18
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2558

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2251

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3140

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csd...