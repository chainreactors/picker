---
title: 用Python制作数据可视化仪表盘：使用Dash与Plotly构建实时交互式仪表盘
url: https://blog.csdn.net/nokiaguy/article/details/142714119
source: 一个被知识诅咒的人
date: 2024-10-08
fetch_date: 2025-10-06T18:49:41.739029
---

# 用Python制作数据可视化仪表盘：使用Dash与Plotly构建实时交互式仪表盘

# 用Python制作数据可视化仪表盘：使用Dash与Plotly构建实时交互式仪表盘

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-07 10:30:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量2.4k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

10

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
16

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[信息可视化](https://so.csdn.net/so/search/s.do?q=%E4%BF%A1%E6%81%AF%E5%8F%AF%E8%A7%86%E5%8C%96&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[dash](https://so.csdn.net/so/search/s.do?q=dash&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142714119>

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在数据驱动的世界中，可视化是理解和解释复杂数据的关键工具。通过数据可视化，用户能够快速洞察数据趋势，做出明智决策。而**仪表盘**作为一种高度集成的可视化工具，能够将多种数据图表汇总到一个界面上，便于实时跟踪数据的变化。

在本文中，我们将使用Python的**Dash**和**Plotly**库来构建一个交互式数据可视化仪表盘。这两个库结合起来，能够提供强大的交互性，并支持实时数据更新、图表生成等功能。我们将从基础开始，逐步构建一个功能齐全的仪表盘，展示如何通过数据驱动决策和实时监控。

### 一、Dash与Plotly简介

#### 1.1 Dash简介

Dash是基于**Flask**、**Plotly.js**和**React.js**构建的Python框架，专门用于创建交互式、响应式的网络应用，特别适合数据可视化和仪表盘开发。Dash允许用户通过简单的Python代码定义UI组件，并能够与底层数据进行交互，实现动态数据展示。

#### 1.2 Plotly简介

**Plotly**是一个开源的可视化库，它可以用于生成高质量、交互式的图表，如折线图、柱状图、散点图、热力图等。Plotly不仅可以用于静态的图表生成，还可以与Dash结合，轻松地集成到交互式的仪表盘中。

#### 1.3 Dash与Plotly结合的优势

* **高交互性**：用户可以与图表进行交互，如选择、缩放、过滤等操作。
* **实时数据更新**：通过回调函数，仪表盘可以实时更新数据和图表。
* **轻松扩展**：通过简单的Python代码就可以生成复杂的界面和多种图表。

### 二、环境准备

在开始构建仪表盘之前，你需要安装相关库。你可以通过以下命令来安装Dash和Plotly：

```
pip install dash
pip install plotly
```

Dash依赖于Flask，因此它会自动安装Flask框架。

### 三、构建基础的仪表盘结构

#### 3.1 基本的Dash应用

我们首先从一个简单的Dash应用开始，展示如何定义页面布局并嵌入一个基本的Plotly图表。以下是一个包含简单折线图的示例：

```
import dash
from dash import dcc, html
import plotly.express as px

# 创建 Dash 应用
app = dash.Dash(__name__)

# 创建示例数据
df = px.data.gapminder().query("country=='Canada'")

# 创建折线图
fig = px.line(df, x="year", y="gdpPercap", title="加拿大 GDP 变化趋势")

# 定义布局
app.layout = html.Div(children=[
    html.H1(children='简单数据可视化仪表盘'),

    html.Div(children='''
        使用 Dash 和 Plotly 构建的交互式仪表盘。
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
```

##### 代码解析：

* **Dash App**：我们通过 `dash.Dash()` 创建了一个Dash应用。
* **数据源**：使用 `Plotly Express` 提供的 `gapminder` 示例数据集，选择加拿大的数据。
* **Plotly 图表**：使用 `px.line()` 创建一个折线图，展示加拿大在不同年份的GDP变化。
* **布局**：使用 Dash 的 `html` 模块创建HTML元素，`dcc.Graph` 用于嵌入Plotly图表。

运行这个代码后，你会在浏览器中看到一个包含折线图的简单网页应用。

#### 3.2 添加更多组件

接下来，我们将增加一些交互性，例如通过下拉菜单选择不同的国家来动态更新图表。

```
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

# 加载数据集
df = px.data.gapminder()

# 定义布
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

  16

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  10

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

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.bl...