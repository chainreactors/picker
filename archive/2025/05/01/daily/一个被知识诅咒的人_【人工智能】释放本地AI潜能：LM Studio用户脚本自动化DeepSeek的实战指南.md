---
title: 【人工智能】释放本地AI潜能：LM Studio用户脚本自动化DeepSeek的实战指南
url: https://blog.csdn.net/nokiaguy/article/details/147641041
source: 一个被知识诅咒的人
date: 2025-05-01
fetch_date: 2025-10-06T22:24:44.407533
---

# 【人工智能】释放本地AI潜能：LM Studio用户脚本自动化DeepSeek的实战指南

# 【人工智能】释放本地AI潜能：LM Studio用户脚本自动化DeepSeek的实战指南

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2025-04-30 22:24:38 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.2k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

12

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
24

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
[人工智能](https://blog.csdn.net/nokiaguy/category_1260139.html)
文章标签：
[人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[自动化](https://so.csdn.net/so/search/s.do?q=%E8%87%AA%E5%8A%A8%E5%8C%96&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/147641041>

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

随着大型语言模型（LLM）的快速发展，DeepSeek以其高效的性能和开源特性成为开发者关注的焦点。LM Studio作为一款强大的本地AI模型管理工具，为用户提供了便捷的DeepSeek部署方式。本文深入探讨如何通过LM Studio的用户脚本实现DeepSeek的自动化运行，涵盖环境搭建、模型部署、脚本开发以及优化技巧。文章通过大量代码示例和详细注释，分享实战经验，帮助开发者在本地高效利用DeepSeek进行任务自动化。无论是数据隐私保护还是成本控制，本文都将为您提供全面的技术指导，助力解锁本地AI的无限可能。

### 引言

在AI技术飞速发展的今天，大型语言模型（LLM）如DeepSeek以其卓越的性能和开源特性，吸引了众多开发者的目光。然而，依赖云端API的模型运行往往面临数据隐私、API限制和成本问题。LM Studio作为一款开源的本地AI模型管理工具，为开发者提供了在本地运行DeepSeek的理想平台。通过用户脚本，开发者可以进一步自动化DeepSeek的任务执行，极大地提升效率。

本文将从LM Studio的安装与配置开始，逐步深入探讨如何通过用户脚本实现DeepSeek的自动化运行。我们将结合大量代码示例，详细解析每个步骤，并提供优化建议，力求为开发者提供一份实用的技术指南。无论您是AI初学者还是资深开发者，本文都将为您提供清晰的实战路径。

### 一、LM Studio与DeepSeek简介

#### 1.1 LM Studio：本地AI模型的理想平台

LM Studio是一款开源的桌面应用程序，支持在Windows、macOS和Linux上运行大型语言模型。它通过直观的图形界面和API模式，简化了模型的下载、管理和运行流程。LM Studio支持多种模型格式（如GGUF、MLX），并提供本地服务器功能，方便开发者通过脚本或API调用模型。

#### 1.2 DeepSeek：高效开源的LLM

DeepSeek是一系列由DeepSeek公司开发的大型语言模型，涵盖DeepSeek R1（专注于推理）和DeepSeek V3（通用模型）等版本。其开源特性和高效的Mixture-of-Experts（MoE）架构使其在代码生成、数学推理和自然语言处理任务中表现出色。DeepSeek模型支持多种参数规模（如7B、67B），适配不同硬件配置。

#### 1.3 自动化脚本的意义

通过LM Studio的用户脚本，开发者可以实现DeepSeek的自动化任务，如代码生成、数据分析和批量处理。这不仅提高了开发效率，还能确保数据隐私，降低API调用成本。

### 二、环境搭建：LM Studio与DeepSeek的本地部署

#### 2.1 安装LM Studio

首先，访问LM Studio官方网站（https://lmstudio.ai）下载适用于您操作系统的版本。安装过程简单，遵循以下步骤：

1. **下载安装包**：选择Windows、macOS或Linux版本。
2. **运行安装程序**：按照提示完成安装。
3. **验证安装**：启动LM Studio，检查界面是否正常。

```
# 示例：Linux环境下安装LM Studio
wget https://lmstudio.ai/downloads/lmstudio-latest-linux.deb
sudo dpkg -i lmstudio-latest-linux.deb
```

#### 2.2 下载DeepSeek模型

LM Studio内置模型目录，支持从Hugging Face等平台下载DeepSeek模型。以下是下载DeepSeek R1（7B参数）的步骤：

1. 打开LM Studio，进入“Discover”选项卡。
2. 搜索“DeepSeek R1”，选择适合硬件的版本（如GGUF格式）。
3. 点击“Download”开始下载。

```
# 示例：通过LM Studio CLI下载模型
lms download --model deepseek-r1-7b-gguf
```

#### 2.3 配置本地服务器

LM Studio支持通过本地HTTP服务器提供API接口，方便脚本调用。启动服务器的步骤如下：

1. 打开LM Studio，进入“Developer”选项卡。
2. 选择已下载的DeepSeek模型，点击“Start Server”。
3. 默认服务器地址为`http://localhost:1234`。

```
# 示例：检查服务器状态
import requests

url = "http://localhost:1234/v1/models"
response = requests.get(url)
print(response.json())  # 输出可用模型列表
```

### 三、用户脚本开发：自动化DeepSeek任务

#### 3.1 脚本开发环境准备

为实现自动化，我们使用Python开发用户脚本，依赖以下库：

* `requests`：用于与LM Studio本地服务器通信。
* `json`：处理API返回的JSON数据。
* `os`：管理文件和目录。

```
pip install requests
```

#### 3.2 基础脚本：与DeepSeek交互

以下是一个基础脚本，用于向DeepSeek发送提示并获取响应：

```
import requests
import json

# 配置服务器地址和模型
SERVER_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "deepseek-r1"

def query_deepseek(prompt):
    """
    向DeepSeek发送提示并获取响应
    Args:
        prompt (str): 用户输入的提示文本
    Returns:
        str: DeepSeek的响应
    """
    headers = {

   "Content-Type": "application/json"}
    data = {

        "model": MODEL,
        "messages": [
            {

   "role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }

    response = requests.post(SERVER_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"错误: {

     response.status_code}"

# 测试脚本
if __name__ == "__main__":
    prompt = "编写一个Python函数，计算斐波那契数列的前n项"
    result = query_deepseek(prompt)
    print(result)
```

**代码解释**：

* **SERVER\_URL**：LM Studio本地服务器的API端点。
* **MODEL**：指定使用的DeepSeek模型。
* **query\_deepseek**：封装了向DeepSeek发送请求的逻辑，支持自定义提示。
* **temperature**：控制生成文本的随机性，0.7为平衡值。
* **max\_tokens**：限制响应长度，避免过长输出。

运行后，DeepSeek将返回一个计算斐波那契数列的Python函数示例：

```
def fibonacci(n):
    """
    计算斐波那契数列的前n项
    Args:
        n (int): 项数
    Returns:
        list: 斐波那契数列
    """
    if n <= 0:
        return []
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
```

#### 3.3 自动化任务：批量代码生成

假设我们需要为一系列数学问题生成Python代码，可以编写脚本批量处理提示列表：

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
2559

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07...