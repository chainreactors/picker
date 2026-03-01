---
title: 全网首发 | 基于CORS漏洞示例验证的大模型能力Agent Skills能力从0到1全流程开发解析科普讲解，新手小白也能轻松上手
url: https://mp.weixin.qq.com/s/pgrujScra2J6y4X-BG1nWA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:18:36.811960
---

# 全网首发 | 基于CORS漏洞示例验证的大模型能力Agent Skills能力从0到1全流程开发解析科普讲解，新手小白也能轻松上手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vMvqFvNsWMDhTfYia62s0ZX1eYiaumbl6fSFTqOzTPskcEadW5FRutYUicxqaJ3dyZOTkVDf7O4Uia7U7mfLTglerECGUalk3picSzcrHc9Pwicy4/0?wx_fmt=jpeg)

# 全网首发 | 基于CORS漏洞示例验证的大模型能力Agent Skills能力从0到1全流程开发解析科普讲解，新手小白也能轻松上手

原创

KamenRiderDarker
KamenRiderDarker

HexaGoners

![]()

在小说阅读器中沉浸阅读

最近Skill这个概念非常火啊

鄙人在了解了一下之后发现，这个本质上就是一段非常灵活的渐进式披露的提示词机制，采用按需加载的思想，果然计算机行业到最后都是最优概念套娃么？（方法论）

今天就给大家带来一款「基于通用型CORS漏洞扫描的Skill」的全流程解析，不仅覆盖从环境准备、前置检查到无登录态扫描的完整操作，还会同步补充Skill、MCP（模型调用协议）及大模型交互的核心知识点，以及如何去使用，还有Skill的开发思路，过程中遭遇的问题以及解决干货，希望能够帮助到还在和ai焦灼的小伙伴们，Skill格式目前只适配了Trae，其他vibe coding工具厂家未作适配，但是应该也不影响使用，我们先看一下运行效果：

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMDz39fzSicDIsgH0d6Bo468yia3uahRUJXv3EXoxzkD27JjeLZ1UjJxVMnDG2qNdkwzzgycEJycdkMYf9eLEw67k8ZZNQaReibpoQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAbRUCZZUI9qjhKUl855EtLTfianKiahPoCJvRjhecblLtmaNgPrP62ftAvsuJy4vSdU18ibsIt99ZxCvAibKM7m8cdms3lZWgiau78/640?wx_fmt=png&from=appmsg)

感觉还是可以的

好了，话不多说，我们就赶快开始！

先来基础知识补习，你也可以在阅读下列问题之前在自己心里过一遍：

1、什么是prompt？

prompt译为提示符，那中文说法说的顺畅一点，就是提示词了

那很顾名思义了，就是一段带有指导提示的 ”指令/问题/引导语“

* 简单理解：你想让 AI 做什么、怎么做、遵循什么规则，都通过 Prompt 告诉它。
* 核心作用：定义 AI 的任务目标、约束条件、输出格式，引导 AI 生成符合预期的结果。

那么prompt也有下列几种常见类型：

**（1）基础 Prompt（无约束）：**

**”写一篇关于AI Agent的短文“**

**（2）结构化Prompt（带约束）：**

**”任务：写一篇关于AI Agent的短文**

**要求： 1. 字数控制在200字以内 2. 重点讲Skill的作用 3. 语言通俗易懂，避免专业术语 输出格式：纯文本，分段清晰“**

**（3）Agent场景的Prompt：**

**”你是一个智能助手，拥有以下技能：**

**- web\_search：根据关键词搜索网页信息，参数为keywords（必选）、top\_k（可选）**

**- code\_generation：生成指定语言的代码，参数为language（必选）、function\_name（必选）**

**现在用户的问题是：“用Python写一个网页搜索的函数，要求能返回前5条结果”**

**请分析：**

**1. 是否需要调用技能？需要调用哪个/哪些？**

**2. 调用时需要的参数是什么？**

**3. 调用后如何整合结果并回答用户？“**

**——————————————————————————————**

**可以看到第三类提示词的描述复杂度是上升的，并且能够指导处理的问题程度也偏向复杂了，但是复杂度和描述之间是不成正比的，也就是说当你需要进行描述事情过程的复杂度到了超出大模型上下文能力时，就很难支持这种堆积如山的写法了**

2、什么是MCP？

MCP全称 Model Context Protocol（模型上下文协议）

你可以理解为：“AI大模型连接外部具体世界事物的统一万能接口”

也就是这套协议，无论哪个厂家训练出来的具有基础功能的大模型，都可以通过这套协议并输出接近相同的操作，同时，还可以获取外部资源

也就是说：MCP = 大模型和外部工具之间的 “通用翻译官 / 通用语言”：

* 规定：怎么发请求
* 规定：怎么返回结果
* 规定：怎么调用功能、读数据、写文件

不管你是：

* 百度文心
* 阿里通义
* OpenAI GPT
* 字节豆包

只要大家都**说 MCP 这门语言**，就能统一调用外面的工具。

3、什么是Skill？

Skill直接英译就是“技能/能力”的意思，你可以理解为：**AI 会做的 “具体本事”**。

它是**封装好的一套做事流程**：比如 “查天气”，是不是应该先访问对应咨询的数据应用渠道，比如什么天气查询网站，或者手机的某个界面，然后点击进入，然后就看到了。

一个完整 Skill 通常包含：

（1）做什么（功能描述）

（2）要什么输入（参数）

（3）怎么一步步做（逻辑 / 流程）

* （4）最终/每一步之间，返回什么结果（格式）

说白了就是一本带目录的说明书

4、那Skill和MCP之间的关联是什么？

### 核心区别：一句话分清

###

* **MCP 管 “连接”**

：解决 “AI 能不能连上外部工具 / 数据” 的问题。

* **Skill 管 “做事”**

  ：解决 “AI 怎么规范、高效地完成任务” 的问题。

#### 再举个目前就可以实现的例子：AI 帮你订机票

####

1. **Skill（订机票技能）：**

查出发地 / 目的地 / 日期

比价

选航班

生成订单

1. **MCP（连接协议）：**

帮 AI 连上外面的资源

航空公司 API（查航班）

连支付系统（付款）

* 连你的日历（写入行程）

**流程：**AI 调用「订机票 Skill」→ Skill 按流程走 → 每一步需要外部数据时，就通过 **MCP** 去调用对应服务 → 拿到结果后，Skill 继续处理 → 最后给你订单。

—————————————我是分隔线————————————

好了，在有了这些基础知识后，我们来看看如果要将Skill的思想结合到安全实践活动中，我们应该怎么做？

这里我使用的是一个较为简单的漏洞——CORS啊

那还是按照学术文章的惯例，我们先来复习一下这个漏洞的知识：

CORS （Cross-Origin Resource Sharing）跨域资源共享，这本身是浏览器的一个机制，是一种基于 HTTP 头的，通过在返回给浏览器客户端的响应报文中，通过配置相应字段，允许服务器声明哪些外部源（协议、域名、端口组合）有权访问其资源。它解决了浏览器同源策略（Same-Origin Policy）对跨域请求的限制，使前端应用能安全地与不同源的后端 API 通信。

举例子：

在浏览器默认情况下，网站A不能读取网站B的数据，比如，张三正在观摩恶意不良网站，但是这时，张三电脑的浏览器内还缓存了其他网站的一些凭证信息数据，那么如果恶意不良网站的恶意js想要获取这些数据时，浏览器便会进行阻断

那什么情况下，CORS漏洞会产生，还是这个场景，其他网站中的一个后台网站不小心配置了不当的CORS头字段返回到浏览器，那么此时，不良恶意网站便可以通过CORS这种跨域资源共享机制，获取到后台网站中保存的张三的一些个人凭证，以造成凭证等重要敏感信息窃取。

那了解完了漏洞成因，我们还需要了解一下CORS的一些玩法和漏洞类型：

CORS 请求分为两类，由浏览器自动处理：

1. ‌**简单请求（Simple Request）**‌

* HTTP 方法为 `GET`、`POST` 或 `HEAD`。
* 请求头仅包含 `Accept`、`Accept-Language`、`Content-Language`、`Content-Type`（且值仅限 `text/plain`、`multipart/form-data`、`application/x-www-form-urlencoded`）。

* ‌**条件**‌：同时满足以下三点：
* ‌**流程**‌：浏览器直接发送请求，并自动添加 `Origin` 头。服务器需在响应中包含 `Access-Control-Allow-Origin` 头，浏览器才允许前端接收响应。

2. ‌**预检请求（Preflight Request）**‌

* 使用 `PUT`、`DELETE`、`PATCH` 等方法。
* 自定义请求头（如 `Authorization`、`X-Custom-Header`）。
* `Content-Type`

  为 `application/json`。

* ‌**触发条件**‌：请求为非简单请求，例如：
* ‌**流程**‌：

1. 浏览器先发送一个 `OPTIONS` 请求（预检请求），包含 `Access-Control-Request-Method` 和 `Access-Control-Request-Headers` 头。
2. 服务器响应预检请求，返回 `Access-Control-Allow-Methods`、`Access-Control-Allow-Headers` 等头，确认允许跨域。
3. 浏览器收到允许响应后，才发送真正的请求。

漏洞类型：

1、完全宽松型

特征：

后端响应头中出现CORS配置字段，并且出现：

Access-Control-Allow-Origin: \*

Access-Control-Allow-Credentials: true

* `*`

  表示允许**全世界任何域名**跨域访问
* `Allow-Credentials: true`

  表示允许携带 Cookie / 登录态

危害性评估：高

2、反射型Origin

特征：

后端会**直接把前端请求头里的 Origin 值，原样返回**到 `Access-Control-Allow-Origin` 里：

* 前端发起构成的最终请求报文中： `Origin: https://evil.com`
* 后端有CORS字段，且字段 `Access-Control-Allow-Origin值为: https://evil.com`

危害性评估：中

3、弱正则匹配（校验缺陷）

特征：

后端用**写得很烂的正则表达式**校验 Origin，比如：

* 想只允许 `https://xxx.com`，但正则写的是 `.*xxx.com`
* 黑客只需要构造 `https://evilxxx.com`，就能匹配上，被允许访问

### 常见绕过方式

* 正则漏写开头 / 结尾：`xxx.com` → 绕过为 `hackxxx.com`、`xxx.com.hack.com`
* 大小写绕过：`Xxx.Com`
* 子域名滥用：`hack.xxx.com`（如果正则没限制子域名）

危害评估：中

4、宽泛根域名白名单配置

和Access-Control-Allow-Origin: \* 同理，只不过变成了Access-Control-Allow-Origin: \*.com

5、预请求配置不当

特征：

对于CORS 机制的预请求（OPTIONS 请求）报文，后端响应报文中返回：

Access-Control-Allow-Methods: \*  # 允许所有HTTP方法（GET/POST/DELETE等） `Access-Control-Allow-Headers: *  # 允许所有请求头
Access-Control-Max-Age: 86400    # 预检结果缓存时间过长`

### 危害评估：低

好了，那么，关于CORS漏洞的大概知识，我们也复习了解完了，你坚持看到了这里，辛苦了，离成功还差2/3了

—————————————我是分隔线————————————

那么在了解完Skill和CORS的概念后，我们便可以来着手开始尝试写一下我们的Skill了

我这里使用的是Trae CN版

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMBRvm3SEibXFne5CnG9FO5mWF6yhPAId4ibwJIStTVibBHIoQRUA7tricSUf8EuO73D2hefg6Nt9Y0VkfMWum84bRQZ2EMbWpic0aF4/640?wx_fmt=png&from=appmsg)

先来了解一下Trae对Skill的支持：

切换到Solo模式，注意，Skill只有在Solo模式才支持Skill等一系列功能特性，没有Solo版本的小伙伴赶紧去申请吧，一般1-2天就可以申请到了

来到右边页面右上角的齿轮，设置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMDpXfp2UPjPsljicwqOKAsZd5nOJOqWLm4gxa6KbibCWoWwzezHokjjzzjCDBeYRGk0Uqe1N1VtBb2ukF9kR5L1rVDCxKLhaTj4I/640?wx_fmt=png&from=appmsg)

点击 “规则和技能”

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMCgGV9ibcflfvpiaicJjUBToA6IuoNVbeaEJlsJqAfkW9u0Mdt4ykFYOQ9ZN9RwvWaA6utvALJduu5vkROkREd7831ia6uw7eM69os/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMAwTxtpcz0DKtNN9WBLGrZlmvJTAtxH8ERbSeqxwDDqkibrmPmUe3P1nQHtNakXSjxpZlEywYBqOh9csYecSj6dogVt7c1iaxXls/640?wx_fmt=png&from=appmsg)

来到技能功能板块

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMBcicSFqib4l8g8bKzgYR3VS5icfVT9dGupUoeRxJiauSAnkoHneIOiaIj5DGIQldNSpYcLbSVXw8iaWUpZkGGygylTQPptlRotyBwH4/640?wx_fmt=png&from=appmsg)

首先来讲一下全局技能和项目技能的区别

全局技能，意思是你使用Trae打开的任意项目都具备的初始技能，那么该功能所在的文件夹路径在：

C盘/用户名/.trae-cn/skills下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMA2OwHFHzuzlY8MCfOBpULhzrOnx4useu0SyBMPVv4tiaW1ykcO4snG5DfyOsjibLzLuavMCfuJArvRvFl96juw0nbLxepas2iaRc/640?wx_fmt=png&from=appmsg)

而项目技能则在当前项目工程主文件夹的.trae-cn/skills下

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMC3uksmm5etPzek43l7cLzy67Fw5DfBnDXRLzXb4bx6iaoj3QqbSUUWYC2kGe2GcVdDcmXHK5KiaWYGibicBxQcxKXnyBx7icZKHhibk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMA8q3qMCH94M4ZH97nhk7nrwGwibFWUpfaxwPpnFKQOQE3MO9wbRFle7yg4SYslRugDchicvs5DGxujPAAeIIWs6DeBPvBtwszRE/640?wx_fmt=png&from=appmsg)

项目技能跟随项目走，那当然你重新创建一个项目之后，便没有咯，但是你可以重新复制过来，甚至也可以复制到全局技能的文件夹路径中作为一个全局技能

我们继续看如何创建技能，点击“创建”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMC7MgMibJq6tqMy7fVBGhAnEvDDIVGNnHK2U7dBSSMkU4p8IxYB1D7icXRbW9LVicPmn8HsnPpco8kP4xsjYUwkOdw5k4qtsdvaDs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMDAmK32ibM6zkKH1Njxf7I0Tdw1Wtrz8dvgic1LeXavYJbmC8VIicp6T1lrwdHykjLkwibLf9icbx8gNtXb5BD2hT1ibdVLyrwiajFh8E/640?wx_fmt=png&from=appmsg)

可以看到这里的界面其实支持两种创建方式，一种是直接上传技能压缩包，Trae会自动解压缩并且将技能放入对应的全局还是项目文件夹中，还有一种就是手动创建，输入技能名称，描述，和指令，例如下面的形式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMBnZ2GVI2zf5j7UK7SZp3hObthsUbdJgG313beOpgYIh263vyCiaOvJics6nD44HyKsLsbu1t7yIx3HZP4dLJVQovo6yAibyqJ1T8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAribKxzTziaFI7yjGN2GSiaJWseGAAX7s9kXQQ9T6GYwXxiaNVaYuIO4tyLGI6DOg6ZGLrUp60U4iaNuAgE9RpIgGdLscttr2gkl8A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_m...