---
title: 【Python运维】用Python管理Docker容器：从`docker-py`到自动化部署的全面指南
url: https://blog.csdn.net/nokiaguy/article/details/145227982
source: 一个被知识诅咒的人
date: 2025-01-19
fetch_date: 2025-10-06T20:08:09.290885
---

# 【Python运维】用Python管理Docker容器：从`docker-py`到自动化部署的全面指南

# 【Python运维】用Python管理Docker容器：从`docker-py`到自动化部署的全面指南

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-01-18 15:21:30 发布
·
1.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

14

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

16
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#docker](https://so.csdn.net/so/search/s.do?q=docker&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

在现代软件开发和运维过程中，Docker容器化技术因其高效、轻量和可移植性而被广泛应用。Python作为一种灵活且功能强大的编程语言，通过`docker-py`库为开发者提供了强大的Docker容器管理能力。本文深入探讨了如何使用`docker-py`库来管理Docker容器，涵盖从基础操作到高级自动化部署的各个方面。通过详细的代码示例和中文注释，读者将学习如何通过Python脚本实现容器的创建、启动、停止、删除，以及镜像管理、网络配置和数据卷管理等功能。此外，本文还介绍了如何构建自动化部署流程，利用Python脚本与Docker API集成，实现持续集成和持续部署（CI/CD）的高效管理。通过本文的学习，读者将掌握使用Python优化Docker容器管理和自动化部署的实用技能，提升开发与运维的协作效率，确保应用的高可用性和可维护性。

### 引言

随着微服务架构和持续交付的普及，容器化技术在软件开发和运维中的重要性日益凸显。Docker作为最流行的容器化平台，为开发者提供了打包、分发和运行应用的强大工具。然而，随着应用规模的扩大，手动管理大量的容器变得繁琐且易出错。为了解决这一问题，自动化管理工具和脚本成为必需。

Python因其简洁易用和丰富的生态系统，成为自动化任务的理想选择。`docker-py`，也称为Docker SDK for Python，是一个官方维护的Python库，允许开发者通过Python脚本与Docker引擎进行交互，实现对Docker容器、镜像、网络和卷等资源的管理。

本文将全面介绍如何使用`docker-py`库管理Docker容器，从基础操作到自动化部署，涵盖实际应用中的各种场景。通过丰富的代码示例和详细的解释，帮助读者掌握Python在Docker管理中的实用技巧，提升工作效率。

### Docker及容器管理简介

#### 什么是Docker？

Docker是一种开源的容器化平台，它允许开发者将应用及其依赖项打包到一个称为“容器”的轻量级、可移植的单元中。与虚拟机不同，Docker容器共享主机操作系统的内核，因此启动速度更快，资源消耗更少。

#### 容器管理的重要性

在复杂的应用环境中，容器的数量可能会迅速增加，手动管理容器变得不可行。自动化容器管理不仅可以减少人为错误，还能提高部署效率，确保应用的高可用性和可维护性。

#### Docker API与`docker-py`

Docker提供了丰富的API，允许开发者通过编程方式与Docker引擎进行交互。`docker-py`是Docker官方提供的Python SDK，它封装了Docker API，简化了Docker资源的管理操作，使开发者能够通过Python脚本高效地管理容器、镜像、网络和卷等资源。

### `docker-py`库介绍

#### 什么是`docker-py`？

`docker-py`，全称Docker SDK for Python，是一个官方维护的Python库，提供了与Docker引擎进行交互的接口。它支持Docker的所有核心功能，包括容器管理、镜像管理、网络配置和卷管理等。

#### 安装`docker-py`

在开始使用`docker-py`之前，需要先安装该库。可以使用`pip`进行安装：

```
pip install docker
```

确保Docker引擎已安装并正在运行。`docker-py`通过Docker守护进程与Docker引擎通信，因此需要确保当前用户有权限访问Docker守护进程。

### 基础容器操作

#### 导入必要的模块

```
import docker
from docker.errors import NotFound, APIError
import sys
```

#### 创建Docker客户端

首先，需要创建一个Docker客户端实例，用于与Docker引擎进行通信。

```
# 创建Docker客户端
client = docker.from_env()
```

`docker.from_env()`会自动从环境变量中读取Docker配置，如`DOCKER_HOST`、`DOCKER_TLS_VERIFY`和`DOCKER_CERT_PATH`，并创建一个客户端实例。

#### 创建容器

以下示例演示如何使用`docker-py`创建一个新的容器。

```
def create_container(image_name, container_name, command="echo Hello World"):
    """
    创建一个新的Docker容器
    :param image_name: 镜像名称
    :param container_name: 容器名称
    :param command: 容器运行的命令
    :return: 创建的容器对象
    """
    try:
        container = client.containers.create(
            image=image_name,
            name=container_name,
            command=command,
            detach=True
        )
        print(f"成功创建容器: {

     container_name}")
        return container
    except APIError as e:
        print(f"创建容器失败: {

     e.explanation}")
        sys.exit(1)
```

##### 代码解释

1. **函数定义**：

   * `create_container`函数用于创建一个新的Docker容器，接受镜像名称、容器名称和运行命令作为参数。
2. **创建容器**：

   * 使用`client.containers.create`方法创建容器。
   * 参数说明：
     + `image`：容器使用的镜像名称。
     + `name`：容器的名称。
     + `command`：容器启动时执行的命令。
     + `detach=True`：容器以分离模式运行。
3. **异常处理**：

   * 捕获`APIError`异常，输出错误信息并退出程序。

#### 启动容器

创建容器后，可以启动容器。

```
def start_container(container):
    """
    启动Docker容器
    :param container: 容器对象
    """
    try:
        container.start()
        print(f"成功启动容器: {

     container.name}")
    except APIError as e:
        print(f"启动容器失败: {

     e.explanation}")
        sys.exit(1)
```

##### 代码解释

1. **函数定义**：

   * `start_container`函数用于启动指定的Docker容器。
2. **启动容器**：

   * 使用`container.start()`方法启动容器。
3. **异常处理**：

   * 捕获`APIError`异常，输出错误信息并退出程序。

#### 停止容器

容器运行后，可以根据需要停止容器。

```
def stop_container(container):
    """
    停止Docker容器
    :param container: 容器对象
    """
    try:
        container.stop()
        print(f"成功停止容器: {

     container.name}")
    except APIError as e:
        print(f"停止容器失败: {

     e.explanation}")
        sys.exit(1)
```

##### 代码解释

1. **函数定义**：

   * `stop_container`函数用于停止指定的Docker容器。
2. **停止容器**：

   * 使用`container.stop()`方法停止容器。
3. **异常处理**：

   * 捕获`APIError`异常，输出错误信息并退出程序。

#### 删除容器

当容器不再需要时，可以将其删除。

```
def remove_container(container):
    """
    删除Docker容器
    :param container: 容器对象
    """
    try:
        container.remove()
        print(f"成功删除容器: {

     container.name}")
    except APIError as e:
        print(f"删除容器失败: {

     e.explanation}")
        sys.exit(1)
```

##### 代码解释

1. **函数定义**：

   * `remove_container`函数用于删除指定的Docker容器。
2. **删除容器**：

   * 使用`container.remove()`方法删除容器。
3. **异常处理**：

   * 捕获`APIError`异常，输出错误信息并退出程序。

#### 完整示例

以下是一个完整的示例，展示如何创建、启动、停止和删除一个Docker容器。

```
def main():
    image = "hello-world"  # 使用官方hello-world镜像
    container_name = "test_container"
    command = "echo Hello from Docker"

    # 拉取镜像（如果本地不存在）
    try:
        client.images.get(image)
        print(f"镜像 {

     image} 已存在本地。")
    except NotFound:
        print(f"镜像 {

     image} 不存在，正在拉取...")
        client.images.pull(image)
        print(f"成功拉取镜像: {

     image}")
    except APIError as e:
        print(f"拉取镜像失败: {

     e.explanation}")
        sys.exit(1)

    # 创建容器
    container = create_container(image, container_name, command)

    # 启动容器
    start_container(container)

    # 等待容器完成
    container.wait()
    print(f"容器 {

     container.name} 已完成运行。")

    # 获取容器日志
    logs = container.logs().decode("utf-8")
    print(f"容器日志:\n{

     logs}")

    # 停止容器
    stop_container(container)

    # 删除容器
    remove_container(container)

if __name__ == "__main__":
    main()
```

##### 代码解释

1. **拉取镜像**：

   * 首先检查本地是否存在指定的镜像，如果不存在则拉取镜像。
2. **创建容器**：

   * 调用`create_container`函数创建一个新的容器。
3. **启动容器**：

   * 调用`start_container`函数启动容器。
4. **等待容器完成**：

   * 使用`container.wait()`方法等待容器完成运行。
5. **获取容器日志**：

   * 使用`container.logs()`方法获取容器的输出日志。
6. **停止容器**：

   * 调用`stop_container`函数停止容器。
7. **删除容器**：

   * 调用`remove_container`函数删除容器。

#### 运行示例

将上述代码保存为`manage_container.py`，并在终端中运行：

```
python manage_container.py
```

运行结果将显示容器的创建、启动、运行日志、停止和删除的过程。

### 镜像管理

除了容器管理，`docker-py`还提供了强大的镜像管理功能。以下将介绍如何使用`docker-py`进行镜像的拉取、列出、删除和构建。

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

  14

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/...