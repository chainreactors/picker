---
title: 高效构建与文档生成：用Java、Spring Boot和Swagger打造RESTful API
url: https://blog.csdn.net/nokiaguy/article/details/142902977
source: 一个被知识诅咒的人
date: 2024-10-19
fetch_date: 2025-10-06T18:51:27.858189
---

# 高效构建与文档生成：用Java、Spring Boot和Swagger打造RESTful API

# 高效构建与文档生成：用Java、Spring Boot和Swagger打造RESTful API

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)用Java、Spring Boot和Swagger构建RESTful API

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2024-10-18 10:00:00 发布
·
1.1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

30

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

12
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#spring boot](https://so.csdn.net/so/search/s.do?q=spring+boot&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#restful](https://so.csdn.net/so/search/s.do?q=restful&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

随着微服务架构和现代Web开发的兴起，RESTful API已成为应用程序间通信的主要方式之一。Spring Boot提供了快速构建RESTful API的便捷工具，而Swagger则为API文档的生成和维护提供了强大的支持。本文详细介绍了如何使用Spring Boot创建RESTful API，并通过集成Swagger生成可交互的API文档。文章包含代码示例，逐步讲解从创建基本API到为其添加Swagger注解，实现API的自动化文档生成。最后，文章还介绍了如何通过Swagger UI与API进行交互，以便更好地测试和维护API。

---

### 目录

1. 引言
2. RESTful API概述
   * 什么是REST
   * RESTful API的设计原则
3. 使用Spring Boot构建RESTful API
   * 项目设置与依赖管理
   * 创建基本的控制器
   * 使用DTO和Service分层架构
   * API版本控制
4. 在Spring Boot中集成Swagger
   * Swagger简介
   * 使用Swagger注解描述API
   * 自动生成Swagger API文档
5. 使用Swagger UI测试和交互
   * Swagger UI介绍
   * 与API进行交互
6. 实践：创建完整的RESTful API
   * 构建CRUD API
   * 集成Swagger UI
   * 添加API文档注释
7. 性能优化与最佳实践
8. 总结

---

### 1. 引言

在当今的软件开发中，RESTful API已成为后端服务和前端、移动端应用程序交互的主要方式。REST（Representational State Transfer）通过HTTP协议传输数据，并以其简单、灵活的架构风格广泛应用。与此同时，随着应用程序功能的增长，API文档的维护也变得愈加复杂。Swagger提供了自动生成、维护和测试API文档的解决方案，通过其强大的工具链简化了API文档管理。

本文将详细介绍如何使用Spring Boot创建RESTful API，并集成Swagger自动生成可交互的API文档。通过本教程，读者将能够快速构建功能完善的API并通过Swagger自动化文档，提升开发效率和文档维护能力。

---

### 2. RESTful API概述

#### 什么是REST

REST是由Roy Fielding在2000年提出的一种软件架构风格。它基于HTTP协议，通过URL定位资源，并通过标准的HTTP方法（GET、POST、PUT、DELETE等）对资源进行操作。REST具有以下特征：

* **无状态性**：每个请求都是独立的，服务器不会存储客户端的状态。
* **统一接口**：API通过HTTP动词对资源进行操作，具备统一的接口标准。
* **客户端-服务器分离**：客户端和服务器之间保持分离，方便扩展和维护。

#### RESTful API的设计原则

构建RESTful API时应遵循一些设计原则：

* **资源与URI**：每个资源通过一个URI标识，使用名词表示资源，如`/users`代表用户资源。
* **HTTP方法**：常用的HTTP方法有：
  + `GET`：获取资源。
  + `POST`：创建资源。
  + `PUT`：更新资源。
  + `DELETE`：删除资源。
* **状态码**：使用合适的HTTP状态码表示请求的结果。例如，`200 OK`表示请求成功，`404 Not Found`表示资源不存在，`201 Created`表示创建成功。

---

### 3. 使用Spring Boot构建RESTful API

#### 项目设置与依赖管理

首先，我们需要创建一个Spring Boot项目。可以使用[Spring Initializr](https://start.spring.io/)快速生成项目。

**Maven依赖：**

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-ui</artifactId>
    <version>1.6.9</version>
</dependency>
```

`spring-boot-starter-web`是Spring Boot用于创建Web应用程序的核心依赖，而`springdoc-openapi-ui`是用于集成Swagger的依赖。

#### 创建基本的控制器

在Spring Boot中，控制器用于处理HTTP请求并返回响应。我们可以通过`@RestController`注解定义一个简单的控制器。

**示例：UserController.java**

```
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private List<User> users = new ArrayList<>();

    @GetMapping
    public List<User> getAllUsers() {

        return users;
    }

    @PostMapping
    public User createUser(@RequestBody User user) {

        users.add(user);
        return user;
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable int id) {

        return users.stream()
                .filter(user -> user.getId() == id)
                .findFirst()
                .orElseThrow(() -> new RuntimeException("User not found"));
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable int id) {

        users.removeIf(user -> user.getId()
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

  30

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

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创...