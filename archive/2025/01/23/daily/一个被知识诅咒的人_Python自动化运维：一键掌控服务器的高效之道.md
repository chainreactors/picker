---
title: Python自动化运维：一键掌控服务器的高效之道
url: https://blog.csdn.net/nokiaguy/article/details/145305263
source: 一个被知识诅咒的人
date: 2025-01-23
fetch_date: 2025-10-06T20:09:26.790531
---

# Python自动化运维：一键掌控服务器的高效之道

# Python自动化运维：一键掌控服务器的高效之道

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2025-01-22 15:55:28 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.4k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

14

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
24

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[自动化](https://so.csdn.net/so/search/s.do?q=%E8%87%AA%E5%8A%A8%E5%8C%96&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/145305263>

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在互联网和云计算高速发展的今天，服务器数量的指数增长使得手动运维和管理变得异常繁琐。Python凭借其强大的可读性和丰富的生态系统，成为实现自动化运维的理想语言。本文以“Python自动化运维：编写自动化脚本进行服务器管理”为主题，深入探讨了如何利用Python在批量处理、定时任务和日志清理等方面解放运维人员的双手。文章从SSH连接、批量部署脚本到日志归档、自动化报警等多个角度进行了详细阐述与代码示例，并分享了常见的最佳实践和性能优化思路。通过阅读本文，读者可以快速掌握Python自动化运维的核心技能，进一步提升运维效率与系统稳定性。

---

### 引言

在服务器数量较少的时候，运维人员往往可以手动登录每台服务器，执行更新、重启、日志查看等操作。然而，随着业务的快速扩张以及云计算、容器化技术的普及，服务器规模迅速增大，手动操作带来的效率问题、出错风险、可重复性低等缺点变得非常突出。为了满足大规模集群管理的需求，自动化运维成为越来越多企业的必然选择。

Python在自动化运维领域优势明显：

1. **语法简洁**：低门槛、易上手，有利于快速编写脚本。
2. **生态完善**：拥有丰富的第三方库，如Paramiko、Fabric、psutil等，为远程连接、资源监控、批量操作提供便利。
3. **可扩展性强**：可以与其他编程语言或系统工具结合，构建灵活的运维平台。

在本篇文章中，我们将围绕“Python自动化运维：编写自动化脚本进行服务器管理”这一主题，系统介绍如何借助Python进行批量操作、定时任务和日志清理等自动化运维任务。文章不仅会给出大量的示例代码，还会对每段代码进行详尽的中文注释和解释，以帮助读者更好地掌握Python自动化运维的相关技术，并在实际生产环境中得以落地实施。

> **提示**：如果您对并发编程、网络协议或系统管理有一定的了解，将更有助于理解本篇内容；但即使是初学者，也能通过示例代码和详细解说，逐步掌握自动化运维脚本的编写方法。

---

### 一、Python在运维自动化中的角色

在企业日常运维工作中，常见的自动化需求包括：

1. **批量操作**：例如同时对多台服务器安装软件、更新配置文件或执行重启操作。
2. **定时任务**：使用脚本替代手动排查和处理，如定期清理日志、备份数据等。
3. **监控和报警**：获取CPU、内存等资源使用情况，或者收集异常日志后发送报警通知。
4. **日志管理**：定期清理过期日志并将重要日志进行归档或备份。
5. **自动化部署**：在持续集成和持续交付（CI/CD）流程中，实现一键部署和回滚。

Python可以通过第三方库或原生功能，轻松完成以上任务，并且可扩展为一整套自动化运维平台。例如，通过**Paramiko**或**Fabric**库实现SSH远程操作，通过**crontab**或**schedule**库实现定时任务，通过**logging**模块实现日志的管理与归档，配合**psutil**库监控系统资源等。

---

### 二、批量处理：提升大规模服务器管理效率

#### 2.1 Paramiko与Fabric：SSH自动化利器

##### 2.1.1 Paramiko简介

**Paramiko**是一个纯Python实现的SSHv2协议库，支持加密与验证，可以用来远程执行命令、文件上传下载等。使用Paramiko时，典型的流程如下：

* 创建`SSHClient`对象
* 设置自定义的服务器主机密钥策略
* 调用`connect`方法连接到目标服务器
* 使用`exec_command`执行远程命令
* 通过标准输入/输出通道获取执行结果
* 关闭连接

以下是一个使用Paramiko连接到远程服务器并执行命令的示例脚本：

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko

def execute_remote_command(host, port, username, password, command):
    """
    在远程服务器上执行命令并返回输出结果
    :param host: 服务器IP或域名
    :param port: SSH端口，一般为22
    :param username: 登录用户名
    :param password: 登录密码
    :param command: 要执行的命令
    :return: 执行结果字符串
    """
    # 创建SSHClient对象
    ssh_client = paramiko.SSHClient()
    # 自动添加目标服务器的主机密钥（不安全，仅供测试使用）
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # 执行命令
    stdin, stdout, stderr = ssh_client.exec_command(command)
    # 获取执行结果
    result_out = stdout.read().decode('utf-8')
    result_err = stderr.read().decode('utf-8')

    # 关闭连接
    ssh_client.close()

    if result_err:
        return f"Error: {

     result_err}"
    else:
        return result_out

if __name__ == "__main__":
    # 测试连接
    host = "192.168.0.100"
    port = 22
    username = "root"
    password = "123456"
    command = "uname -a"  # 查看操作系统信息

    output = execute_remote_command(host, port, username, password, command)
    print("远程执行结果:\n", output)
```

###### 代码解释

1. **Paramiko库的使用**：先创建`SSHClient`对象，然后使用`set_missing_host_key_policy`设置为自动添加服务器指纹。
2. **连接服务器**：通过`connect`方法传入服务器IP、端口、用户名和密码。
3. **命令执行**：使用`exec_command`，可获取标准输入、标准输出和标准错误。
4. **结果处理**：将输出和错误消息分别读取并转换为UTF-8字符串。
5. **连接关闭**：操作完成后调用`close`，释放连接资源。

##### 2.1.2 Fabric简介

**Fabric**基于Paramiko开发，简化了多服务器批量操作的流程，尤其适用于自动化部署和批量命令执行。它提供了更高层次的API，例如`fab`命令行工具，可以在`fabfile.py`中定义一系列任务，然后在命令行中通过`fab 任务名`执行。下面展示一个简单的Fabric示例，用于批量获取服务器的操作系统信息。

先安装Fabric：

```
pip install fabric==2.6.0
```

> **注意**：Fabric 2.x和1.x版本API差异较大，示例基于2.x版本。

在项目目录下创建`fabfile.py`，示例如下：

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fabric import Connection

# 定义服务器列表
servers = [
    {

   "host": "192.168.0.101", "user": "root", "connect_kwargs": {

   "password": "123456"}},
    {

   "host": "192.168.0.102", "user": "root", "connect_kwargs": {

   "password": "123456"}},
]

def get_os_info():
    """
    获取服务器操作系统信息
    """
    for srv in servers:
        # 创建连接
        conn = Connection(**srv)
        print(f"连接到服务器: {

     srv['host']}")
        result = conn.run("uname -a", hide=True)
        print(f"操作系统信息: {

     result.stdout.strip()}")
        conn.close()
```

然后在命令行中执行：

```
fab get_os_info
```

###### 代码解释

1. **服务器列表**：定义一个Python列表，存储多台服务器的连接信息，包括主机名、用户及密码。
2. **`Connection`对象**：Fabric提供了`Connection`对象，用于建立SSH会话。
3. **批量执行**：循环服务器列表，每次创建`Connection`，执行命令并打印结果。
4. **关闭连接**：完成操作后调用`close`，避免资源泄漏。

无论是Paramiko还是Fabric，都能极大地方便批量处理任务。后文中，我们还会进一步结合定时任务与日志管理进行综合示例。

---

#### 2.2 并发批量处理

在大规模集群环境下，依次连接每台服务器的方式效率不高。为提高批量处理速度，可以使用并发或多线程方式，同时连接多台服务器并执行操作。

以下示例基于`paramiko`和Python的`ThreadPoolExecutor`实现多线程并发批量管理：

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko
import concurrent.futures

def execute_command(host, username, password, command):
    """
    在单台服务器上执行命令
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command(command)
    result_out = stdout.read().decode('utf-8')
    result_err = stderr.read().decode('utf-8')
    ssh_client.close()
    return
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

  24

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  14

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![]...