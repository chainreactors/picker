---
title: 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【6】：使用NumPy创建随机雪花点图像
url: https://blog.csdn.net/nokiaguy/article/details/129250204
source: 一个被知识诅咒的人
date: 2023-02-28
fetch_date: 2025-10-04T08:13:38.361376
---

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【6】：使用NumPy创建随机雪花点图像

# 【计算机视觉】OpenCV 4高级编程与项目实战（Python版）【6】：使用NumPy创建随机雪花点图像

原创
已于 2023-02-27 21:22:05 修改
·
830 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

0

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

0
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#Python](https://so.csdn.net/so/search/s.do?q=Python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#OpenCV](https://so.csdn.net/so/search/s.do?q=OpenCV&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#numpy](https://so.csdn.net/so/search/s.do?q=numpy&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-02-27 21:20:45 首次发布

[![](https://i-blog.csdnimg.cn/blog_column_migrate/56256b7598fb005a8c32c420b606b60c.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

OpenCV高级编程与项目实战（Python版）
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12162950.html "OpenCV高级编程与项目实战（Python版）")

9 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)文章介绍了如何使用Python的NumPy库创建彩色图像。通过构建200x200的三维数组来表示BGR色彩空间，分别设置三个通道（蓝、绿、红）的值以生成纯色图像。此外，还展示了如何生成随机像素值的彩色雪花点图像，利用`np.random.randint`函数为每个像素点赋予0到255之间的随机颜色值。

上一篇文章演示了如何使用二维数组创建黑白图像，如果要创建彩色图像，就需要使用三维数组。例如，在BGR色彩空间创建200 × 200的彩色图像，就需要一个200 ×200 ×3的三维数组存储像素的颜色值，其中第3维可以存储3个通道的颜色值，分别是B通道、G通道和R通道。也就是我们平常说的三原色：蓝（B）、绿（G）和红（R）。

1. #### 创建彩色图像

下面的代码，创建一个三维数组，数组元素初始值都是0，然后将该数组复制3份，将第1个数组的通道1（B通道）设置为255，将第2个数组的通道2（G通道）设置为255，将第3个数组的通道3（R通道）设置为255，这将形成3幅纯色的图像。代码如下：

```
import cv2
import numpy as np

width = 200      # 图像的宽
height = 200      # 图像的高
# 创建指定宽高、3通道、像素值都为0的图像
img = np.zeros((height, width, 3), np.uint8)
blue = img.copy()          # 复制图像
blue[:, :, 0] = 255      # 将通道1中的所有像素都设置为255
green = img.copy()
green[:, :, 1] = 255      # 将通道2中的所有像素都设置为255
red = img.copy()
red[:, :, 2] = 255      # 将通道2中的所有像素都设置为255
cv2.imshow("blue", blue)      # 显示蓝色图像
cv2.imshow("green", green)    # 显示绿色图像
cv2.imshow("red", red)        # 显示红色图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，运行结果如图1、图2和图3所示。

![](https://i-blog.csdnimg.cn/blog_migrate/2529e8cdad362baf2d34d119e7c74d6e.png)

![](https://i-blog.csdnimg.cn/blog_migrate/5b1212896afbf5b1e8276ac27431db74.png)

![](https://i-blog.csdnimg.cn/blog_migrate/b88f9983c8b8d7a02a7bdf2529a1673a.png)

#### 2. 创建彩色雪花点图像

下面的例子使用NumPy提供的random.randint函数创建随机数值的三维数组，并将该数组作为图像源显示。由于每一个像素点的颜色都是随机的，所以整体效果看上去就是彩色的雪花点，代码如下：

```
import cv2
import numpy as np

width = 200  # 图像的宽
height = 200  # 图像的高
# 创建指定宽高、单通道、随机像素值的图像，随机值在0~256之间（不包括256），数字为无符号8位格式
img = np.random.randint(256, size=(height, width,3), dtype=np.uint8)
cv2.imshow("img", img)  # 显示彩色雪花点图像
cv2.waitKey()
cv2.destroyAllWindows()
```

运行程序，会看到如图4所示的效果。

![](https://i-blog.csdnimg.cn/blog_migrate/956342cba2ecad21cb58fba95c7872d3.png)

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

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  0

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
2552

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2244

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3134

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1040

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
955

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.blog.csdn.net/article/details/151067543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸式体验](https://unitymarvel.blog.csdn.net/article/details/150948550)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1076

[在当今游戏行业迅猛发展的时代，AI代理技术正悄然引发一场革命，尤其是动态非玩家角色（NPC）的应用，将传统静态游戏体验提升至全新的沉浸式境界。本文深入探讨AI代理在游戏中的核心作用，从传统NPC的局限性入手，分析AI代理如何通过机器学习、强化学习和自然语言处理等技术实现动态行为响应。文章详细阐述了AI代理的架构设计、实现路径，并提供大量代码示例，包括Python和C#语言的实际实现，辅以中文注释，帮助读者理解从简单状态机到复杂代理系统的构建过程。同时，引入数学模型如Q-learning算法的LaTeX公式，](https://unitymarvel.blog.csdn.net/article/details/150...