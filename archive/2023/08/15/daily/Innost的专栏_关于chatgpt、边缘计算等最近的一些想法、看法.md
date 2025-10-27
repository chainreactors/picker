---
title: 关于chatgpt、边缘计算等最近的一些想法、看法
url: https://blog.csdn.net/Innost/article/details/132288531
source: Innost的专栏
date: 2023-08-15
fetch_date: 2025-10-04T12:01:06.467853
---

# 关于chatgpt、边缘计算等最近的一些想法、看法

# 关于chatgpt、边缘计算等最近的一些想法、看法

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)ChatGPT与2B业务需求：技术与行业角色的融合

原创
于 2023-08-14 16:41:47 发布
·
2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

5

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

0
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#chatgpt](https://so.csdn.net/so/search/s.do?q=chatgpt&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#边缘计算](https://so.csdn.net/so/search/s.do?q=%E8%BE%B9%E7%BC%98%E8%AE%A1%E7%AE%97&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)作者结合自身经历，探讨了ChatGPT技术如何融入2B业务场景，指出其作为工具可能增强现有产品，但真正的落地关键在于具有行业背景的专家。强调了在乌卡时代，判断能力和数据分析的重要性超过单纯的技术学习。

![76667412566616f8cd94e4c9f2f50448.png](https://i-blog.csdnimg.cn/blog_migrate/51a481e6cd53a8ccfd9a10d41901779d.png)

一些想法

最近一直在忙自己的产品打磨。然后，chatgpt突然就爆火了，一下子冒出来几十个大模型。老板一直劝我们，要转型，大模型是未来的iPhone之类的。

其实我在日常生活，工作里也用了大模型。包括今天还让一个同事去用大模型帮他定义一个数据结构。不过，这种所谓的风口，我已经经历过3次了：

* 2015年，VR，火了一阵，我感觉一年都没到。我还买了几个VR设备。有新鲜感，但体验不太好。设备扔了。
* 2016年，说是AI的元年。我自己还亲自搞了一个项目，基于AI的OCR识别。认识了圈内好多朋友。也确实把AI技术带到了业务场景。包括OCR识别、智能客服、人脸识别等。AI，Machine Learning，我当时还花了半年多时间买了好多材料学习。
* 2017年，区块链。第二年区块链突然就火了。我们行还做了好几个区块链大项目。但是也是没2年就势头下去了。有了AI这经验，区块链我就就看了下以太坊的代码。但始终没搞清楚区块链解决啥问题了。

根据我亲自下场，和亲自下场朋友们的沟通，我说一下我看到的情况：不论是AI还是区块链（尤其是区块链），纯从技术上来说，他们离面向2B端的真正需求还有一个巨大的gap。

AI还好点，AI还能优化、提升原有2B端产品，而区块链完全是另搞了一套。而且，还离不开原有的业务——这话说得很拗口，直白点说，就是原有业务要对接到所谓的区块链平台。

做了一个产品，自己独立干不了活，还要原有业务对接过来，产生的价值也不清楚，用户也没感知，这种东西肯定很难推下去嘛。

回到chatgpt，它是一个技术。但哪个B端需求场景可以借助它提升效果？更好满足业务需求呢？所以，光有gpt还不行，还得有行业专家。我之前做的几个项目，行里都是有专门的业务人员来对接技术提供商的。双方一起做好一个产品。从我个人来看，有行业背景的业务或者产品经理，也是chatgpt真正落地的关键人物。

再举个例子，我自己也用chatgpt写代码。之前让它帮我改动一个makefile文件，把一个executable的编译目标改成编译出一个so文件。它改得确实快，但碰到一个很复杂的问题，就是把静态库编译到so里。

幸好，我之前一个项目里手动改过这个问题。这个问题我之前花了至少半天才解决。这次就很快改完了。这个问题，如果没有一些makefile经验的，恐怕是比较难搞定的。

我一直在想，chatgpt会替代我们这些“性价比低”的人么？我现在感觉反而不会。因为，chatgpt要处理的内容，需要有经验的人才能玩好。它应该起到手和脚的作用——有经验的人，知道自己想要什么，也能很快看出来gpt给的东西对不对，知道怎么调教它。

但没有经验的人，gpt给出了一堆结果，他都很难判断对不对。所以，我判断gpt对我们有丰富经验的人来说，更可能是个帮手，而不是干翻我们的人。

另外 ，关于chatgpt的学习，我没有再去看它的实现，论文。因为我在2016年学习AI的时候发现，这玩意已经不是看代码，加强逻辑训练（例如可以写出极为正确的if/else/while等）的事情了。它是通过数据喂养大的，没有代码里写的那样的逻辑关系。甚至，科学家也搞不清为什么这样或那样才有用。它只是经过测试，经过验证后，发现现在的模型有用，所以就这样了....

所以，在乌卡时代，更重要的可能是判断能力的修炼。判断能力，显然不是严格的代码能写出来的，需要足够多的，好的数据以及数据分析，还要有经验。

工作十六年了，我一直在做强逻辑，强因果关系的事情——如果程序出错，一定是我写错了。现在，我觉得应该从数据分析上看看有什么更有价值的事情了。

最后的最后

* 我期望的结果不是朋友们从我的书、文章、博客后学会了什么知识，干成了什么，而应该是说，神农，我可是踩在你的肩膀上的喔。
* 关于学习方面的问题，我已经讨论完了。后面这个公众号将对一些基础的技术，新技术做一些学习和分享。也欢迎你的投稿。不过，正如我在公众号“联系方式”里说的那样——郑渊洁在童话大王《智齿》里有一句话令我印象深刻，大意是“我有权保持沉默，但你说的每一句话都可能成为我灵感的源泉”。所以，影响不是单向的，很可能我从你那学到的东西更多。

神农和朋友们的杂文集

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/d44f053d55d74bae934e9801dd3bee65_innost.jpg!1)

阿拉神农](https://blog.csdn.net/Innost)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  5

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

参与评论
您还未登录，请先
登录
后发表或查看评论

[![](https://profile-avatar.csdnimg.cn/d44f053d55d74bae934e9801dd3bee65_innost.jpg!1)](https://blog.csdn.net/Innost)

[阿拉神农](https://blog.csdn.net/Innost "阿拉神农")

博客等级
![](https://csdnimg.cn/identity/blog8.png)

码龄19年

![](https://img-home.csdnimg.cn/images/20210412060958.png)
《深入理解Android》 作者

![](https://img-home.csdnimg.cn/images/20210114022826.png)
博客专家认证

[:   229

原创](https://blog.csdn.net/Innost)

:   2726

点赞

:   2896

收藏

:   1万+

粉丝

关注

[私信](https://im.csdn.net/chat/Innost)

[![](https://i-operation.csdnimg.cn/images/8fbfca85f6a1420d8f224438dfe454b1.png)](https://activity.csdn.net/writing?id=10971)

[![](https://i-operation.csdnimg.cn/images/bfc20af708654cc689adbb6361f6dc98.png)](https://mp.csdn.net/edit?utm_source=blog)

### TA的精选

* [新
  读KK《2049：未来10000天的可能》有感](https://blog.csdn.net/Innost/article/details/151060086)

  973 阅读
* [新
  从最近的一件事情再理解智能体](https://blog.csdn.net/Innost/article/details/148461724)

  1490 阅读
* [热
  深入理解Android之Gradle](https://blog.csdn.net/Innost/article/details/48228651)

  190271 阅读
* [热
  Android Wi-Fi Display（Miracast）介绍](https://blog.csdn.net/Innost/article/details/8474683)

  167335 阅读
* [热
  深入理解SELinux SEAndroid（第一部分）](https://blog.csdn.net/Innost/article/details/19299937)

  139172 阅读

[查看更多 ![](https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowRightWhite.png)](https://blog.csdn.net/Innost?type=blog)

[2025年2篇](https://blog.csdn.net/Innost?type=blog&year=2025&month=08)

[2024年7篇](https://blog.csdn.net/Innost?type=blog&year=2024&month=09)

[2023年4篇](https://blog.csdn.net/Innost?type=blog&year=2023&month=08)

[2022年7篇](https://blog.csdn.net/Innost?type=blog&year=2022&month=12)

[2021年20篇](https://blog.csdn.net/Innost?type=blog&year=2021&month=12)

[2020年16篇](https://blog.csdn.net/Innost?type=blog&year=2020&month=12)

[2019年19篇](https://blog.csdn.net/Innost?type=blog&year=2019&month=12)

[2016年2篇](https://blog.csdn.net/Innost?type=blog&year=2016&month=09)

[2015年36篇](https://blog.csdn.net/Innost?type=blog&year=2015&month=12)

[2014年21篇](https://blog.csdn.net/Innost?type=blog&year=2014&month=12)

[2013年10篇](https://blog.csdn.net/Innost?type=blog&year=2013&month=12)

[2012年25篇](https://blog.csdn.net/Innost?type=blog&year=2012&month=12)

[2011年37篇](https://blog.csdn.net/Innost?type=blog&year=2011&month=12)

[2010年26篇](https://blog.csdn.net/Innost?type=blog&year=2010&month=12)

[2009年2篇](https://blog.csdn.net/Innost?type=blog&year=2009&month=03)

### 大家在看

* [【Python进阶】网络爬虫核心技能-第三方IP服务](https://blog.csdn.net/weixin_45221204/article/details/152508327)
* [免费清理C盘垃圾的多种方法
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
  1175](https://blog.csdn.net/2401_87766320/article/details/152327974)
* [高性能队列实现与应用解析](https://blog.csdn.net/ysct_999/article/details/152509181)
* [基于Python的招聘信息可视化分析系统](https://blog.csdn.net/m0_67185565/article/details/152507258)
* [​​PrivaZer (系统清理优化工具) 深度清洁/隐私保护​​](https://blog.csdn.net/KSYWER/article/details/152508936)

### 分类专栏

* [![](https://i-blog.csdnimg.cn/columns/default/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64)

  Android开发系列](https://blog.csdn.net/innost/category_767414...