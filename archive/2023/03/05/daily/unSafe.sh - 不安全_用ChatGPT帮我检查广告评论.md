---
title: 用ChatGPT帮我检查广告评论
url: https://buaq.net/go-151974.html
source: unSafe.sh - 不安全
date: 2023-03-05
fetch_date: 2025-10-04T08:43:09.599796
---

# 用ChatGPT帮我检查广告评论

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/0184db24767da5ec9fad221e703e4141.jpg)

用ChatGPT帮我检查广告评论

最近博客后台经常会出现一些来自国外的留言，基本全是一些广告，以推广SEO、推广博客工具的居多，比如这个：这个情况这几年一直都有
*2023-3-4 22:38:0
Author: [www.leavesongs.com(查看原文)](/jump-151974.htm)
阅读量:36
收藏*

---

最近博客后台经常会出现一些来自国外的留言，基本全是一些广告，以推广SEO、推广博客工具的居多，比如这个：

[![image.png](https://www.leavesongs.com/media/attachment/2023/03/04/3c8a5d8c-55d4-4d96-8c55-e86f880d05d0.045ead4d7b0c.png)](https://www.leavesongs.com/media/attachment/2023/03/04/3c8a5d8c-55d4-4d96-8c55-e86f880d05d0.png)

这个情况这几年一直都有，我也一直在给博客增加许多限制，比如IP黑名单、关键词黑名单、增强验证码等，但总有一些漏网之鱼，而且今年特别严重。

我的博客完全是自己开发的，而非Wordpress这类通用程序，理论上应该不会有传统的通用工具能自动绕过验证码进行留言。所以我想不太通这些工具是怎么做到的，可能有什么自动化分析表单并化填写的机制吧，毕竟近年来AI特别流行，传统的一些技术已已经过时……

诶？AI？既然对方可以用AI，那么我也可以借助AI的力量来帮我检查评论是否包含广告信息。

正好前两日ChatGPT正式开放了其3.5版本的API，本次就来水一篇文章，蹭一蹭热点。

## [注册ChatGPT获得API](#chatgptapi)

OpenAI的账户我其实早在之前[DALL·E](https://openai.com/product/dall-e-2)火的时候就注册了，当时AI帮忙生成图片的功能确实把我惊艳了，这次ChatGPT的推出更是惊艳的平方。

我之前一度认为人类的科技已经停滞，互联网上充斥着各种骗局，什么赛道火资本就蜂拥而入，但实际走入大众生活的还是外卖、打车、买菜。要说完全没有技术含量肯定也不是，但和上世界20年代那些伟大的发现相比，总感觉科学已经被锁死了。

我的这个想法也不是凭空出现的，就以我们这篇文章的主题——评论审核为例，大家以前都说AI已经发展到很高的水平了，自然语言与图片、视频处理都不在话下，但实际很多App的审核仍然是关键词匹配，还出现过“Java“、”黑夜总会过去“、”多口交换机“等笑话，大概和我博客的水平一致，可能就是敏感词库要大一点而已。

OpenAI的出现，特别是其将AI技术以一种特别简单的方式呈现在大众面前，让不懂任何技术的人可以通过一段文字生成艺术画作，可以直接和一个无所不知的AI助手聊天，这是以前没有的。

要说以前没有也不严谨，AI助手其实早已进入了每个人的手机、汽车、音响里，但很多人工智能更像是人工智障，相信在ChatGPT出现以前大家也深有体会。

ChatGPT的出现仿佛是对这些上一代智能助手的降维打击，我感觉OpenAI对于他们家AI模型的调教，不光是让其能够更好的理解接收到的信息，还具备了一定程度的创造力，比如ChatGPT可以写小说、写申请书，DALL·E可以创作绘画。

小时候幻想科技的发展，觉得未来社会很多重复性、没有创造力的工作会被机器人替代，现在真的到了这个时代，突然发现最先被取代的反而是艺术家和文字工作者，想想还是挺讽刺的。

[![image.png](https://www.leavesongs.com/media/attachment/2023/03/04/7dd89f07-c0fb-4ada-84d0-c5f897bd9db8.047c4e40b284.png)](https://www.leavesongs.com/media/attachment/2023/03/04/7dd89f07-c0fb-4ada-84d0-c5f897bd9db8.png)

说远了，回到正题😂。

注册以后官方会送18美元的试用费用，但有效期只有三个月。因为我注册的早，到现在这个额度早过期了，所以需要绑定信用卡才能正常使用。

> 值得注意的是，OpenAI没有对中国大陆、香港、俄罗斯、伊朗等地区开放，所以国内的信用卡是用不了的，如果国内的同学需要使用的话，可以考虑注册一些虚拟卡绕过限制。

绑定信用卡后，我们生成自己的API Key，然后就可以调用API了：

[![image.png](https://www.leavesongs.com/media/attachment/2023/03/04/0d01b1a1-70c8-4224-b238-b3868151be05.fdf3f92a6c4d.png)](https://www.leavesongs.com/media/attachment/2023/03/04/0d01b1a1-70c8-4224-b238-b3868151be05.png)

## [调用gpt-3.5-turbo模型](#gpt-35-turbo)

OpenAI中有很多个AI模型，我们需要使用的是前几天新出的gpt-3.5-turbo模型，这个模型就是我们在网页版中使用ChatGPT3.5。

这个模型相关的介绍可以在[这个文档](https://platform.openai.com/docs/guides/chat)里找到，API调用参数在[这里](https://platform.openai.com/docs/api-reference/chat)。在编写代码前，我们先用Burp发下包看看能否正常使用：

```
POST /v1/chat/completions HTTP/1.1
Host: api.openai.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36
Connection: close
Cache-Control: max-age=0
Content-Type: application/json
Content-Length: 117
Authorization: Bearer your-key

{
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "Hello, please introduce yourself"}]
}
```

完全没有问题：

[![image.png](https://www.leavesongs.com/media/attachment/2023/03/04/7386587c-a6a6-4116-a142-1b00a6a2f38f.84f9cdb59bbb.png)](https://www.leavesongs.com/media/attachment/2023/03/04/7386587c-a6a6-4116-a142-1b00a6a2f38f.png)

我们也使用Python官方库[openai](https://pypi.org/project/openai/)来发送请求：

```
import openai

openai.api_key = "your-key"
openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{
    "role": "user",
    "content":  "Hello, please introduce yourself"
}])
```

## [使用ChatGPT帮我分析评论](#chatgpt)

我博客架构是Django+Celery，Celery主要负责执行一些异步任务，比如评论后发送邮件提醒。

因为ChatGPT也是需要发送HTTP请求，是一个异步任务，我就将评论审核相关的工作放在Celery Task中，大概过程如下：

[![image.png](https://www.leavesongs.com/media/attachment/2023/03/04/6e92c14e-4cbc-47e6-beb5-70b005b9671f.16277076e73b.png)](https://www.leavesongs.com/media/attachment/2023/03/04/6e92c14e-4cbc-47e6-beb5-70b005b9671f.png)

1. 用户发表评论，博客先将评论正常保存进数据库中
2. 添加一个新的Celery任务，用于处理这条评论
3. Celery Worker接收到新任务，利用ChatGPT API检查这条评论是否包含广告
4. 评论包含广告，则在数据库中更新这条评论的属性，将其设置为不可见
5. 评论不包含广告，则发送提醒邮件，结束任务

其中，如何让ChatGPT帮忙分析评论呢？其实很简单，我们只需要问这样一个问题即可：

> This is a blog comment, please help me check if this comment contains advertisement, and answer "Yes" or "No":
>
> [评论内容...]

[![image.png](https://www.leavesongs.com/media/attachment/2023/03/04/dbd2b2d7-0c3b-44ce-9dda-636f7bf06d14.1af6e468a4f3.png)](https://www.leavesongs.com/media/attachment/2023/03/04/dbd2b2d7-0c3b-44ce-9dda-636f7bf06d14.png)

这样，如果我们在回答里发现有“Yes”，则说明ChatGPT认为这是一条广告，我们就将这条评论标记为不显示。

标记成不显示，而不是直接删除的原因，是因为这种广告的检测模式毕竟不成熟，ChatGPT有时候也会犯傻，产生误报，所以会在后台double check，确认是广告再手工删除。

其实代码非常简单，就只有十几行：

```
prefix = 'This is a blog comment, please help me check if this comment contains advertisement, and answer "Yes" or "No":\n\n'

def bad_comment(data: str) -> bool:
    try:
        completion = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{
            "role": "user",
            "content": prefix + data,
        }])
        content = completion.choices[0].message.content
        logger.info("check comment: %r, result is %r", data, content)
        return 'Yes' in content
    except (openai.error.OpenAIError, AttributeError) as e:
        return False
```

最后，本文仅是ChatGPT的娱乐玩法，对于垃圾评论的检查，我们也可以使用[Akismet](https://akismet.com/development/api/#getting-started)的云服务，相对而言会更加专业。

文章来源: https://www.leavesongs.com/THINK/using-chatgpt-for-antispam.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)