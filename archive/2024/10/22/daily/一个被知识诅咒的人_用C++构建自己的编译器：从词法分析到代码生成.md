---
title: 用C++构建自己的编译器：从词法分析到代码生成
url: https://blog.csdn.net/nokiaguy/article/details/142946408
source: 一个被知识诅咒的人
date: 2024-10-22
fetch_date: 2025-10-06T18:50:08.958228
---

# 用C++构建自己的编译器：从词法分析到代码生成

# 用C++构建自己的编译器：从词法分析到代码生成

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2024-10-21 11:00:00 发布
·
1.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

14

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

15
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#c++](https://so.csdn.net/so/search/s.do?q=c%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#数据库](https://so.csdn.net/so/search/s.do?q=%E6%95%B0%E6%8D%AE%E5%BA%93&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

本文将带领读者从零开始构建一个简单的C++编译器。我们将逐步讲解如何进行词法分析、语法分析，以及如何将这些结果转换为目标代码。这篇文章的目标是帮助读者理解编译器的基本构成和工作原理，并提供可扩展的编译器框架，为未来的更复杂编译器开发奠定基础。从基础的正则表达式实现一个词法分析器开始，进而通过递归下降分析实现语法解析，最后生成一个简单的中间代码。文章通过详细的代码示例、技术讲解和图表分析，使读者能够全面掌握从源代码到目标代码的核心流程。

---

### 1. 引言

编译器是现代计算机系统中的关键组成部分，它将高级语言转换为机器能够理解的低级代码。虽然市场上已经有很多强大的编译器（如GCC、Clang），但理解一个编译器的工作原理不仅能增强你的编程技能，还能帮助你更好地优化代码并理解计算机体系结构。

在本文中，我们将从最简单的编译器构建起，逐步讲解编译器的每个组成部分，包括词法分析、语法分析和代码生成。最终，读者将学会如何使用C++编写一个简单的编译器，并且为未来更复杂的编译器开发打下坚实基础。

#### 1.1 编译器的基本工作流程

一个典型的编译器分为以下几个步骤：

* **词法分析（Lexical Analysis）**：将源代码划分为一系列称为“词法单元”（tokens）的基本语法元素。
* **语法分析（Syntax Analysis）**：将词法单元组合成更高级别的语法结构，比如表达式、语句。
* **语义分析（Semantic Analysis）**：检查语法结构是否有意义，主要负责类型检查、作用域解析等。
* **中间代码生成（Intermediate Code Generation）**：生成介于源代码和目标代码之间的中间形式。
* **代码优化（Code Optimization）**：对中间代码进行优化，使得生成的目标代码执行效率更高。
* **目标代码生成（Code Generation）**：将中间代码翻译为机器代码或虚拟机字节码。

在本文中，我们将实现前四个步骤，最终生成简单的中间代码。

---

### 2. 词法分析

#### 2.1 词法分析的概念

词法分析器（Lexer）是编译器的第一个阶段，负责读取源代码并将其分解为一系列“词法单元”（token）。每个词法单元代表一个最小的语言成分，如关键字、标识符、操作符等。词法分析的主要目标是去除源代码中的空白字符和注释，并为语法分析器提供易于处理的输入。

#### 2.2 词法分析器的实现

词法分析器通常通过正则表达式来匹配源代码中的模式。我们可以通过C++中的正则表达式库`<regex>`来实现简单的词法分析器。

##### 2.2.1 词法单元定义

首先，我们定义词法单元的类型。每个词法单元由类型和值组成。

```
#include <string>

enum TokenType {

    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,
    TOKEN_OPERATOR,
    TOKEN_PARENTHESIS,
    TOKEN_KEYWORD,
    TOKEN_EOF // 文件结束
};

struct Token {

    TokenType type;
    std::string value;
};
```

##### 2.2.2 词法分析器类

词法分析器的任务是逐字符读取源代码并匹配相应的词法单元。

```
#include <vector>
#include <regex>
#include <iostream>

class Lexer {

public:
    Lexer(const std::string& source) : sourceCode(source), position(0) {

   }

    std::vector<Token> tokenize() {

        std::vector<Token> tokens;

        while (position < sourceCode.size()) {

            if (std::isspace(sourceCode[position])) {

                position++;
                continue;
            }

            if (std::isdigit(sourceCode[position])) {

                tokens.push_back(tokenizeNumber());
            } else if (std::isalpha(sourceCode[position])) {

                tokens.push_back(tokenizeIdentifier());
            } else if (sourceCode[position] == '+' || sourceCode[position] == '-' ||
                       sourceCode[position] == '*' || sourceCode[position] == '/') {

                tokens.push_back(tokenizeOperator());
            } else if (sourceCode[position] == '(' || sourceCode[position] == ')') {

                tokens.push_back(tokenizeParenthesis());
            } else {

                std
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

  14

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  15

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

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
962

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量...