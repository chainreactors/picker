---
title: ChatGPT热，一大波 ChatGPT 开源项目诞生了！
url: https://www.uedbox.com/post/68725/
source: 体验盒子
date: 2023-02-12
fetch_date: 2025-10-04T06:26:14.563058
---

# ChatGPT热，一大波 ChatGPT 开源项目诞生了！

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# ChatGPT热，一大波 ChatGPT 开源项目诞生了！

* 发表于 2023年02月11日
* [人工智能](https://www.uedbox.com/ai/)

本月初 ChatGPT 问世，犹如平地惊雷般，在技术圈中引起了广泛讨论。

作为全球最大的开发者社区，GitHub 平台也在近期诞生了多个 ChatGPT 相关的开源项目，其数量之多，可谓是见所未见，闻所未闻。说是 ChatGPT 以其一己之力，霸榜了大半个 GitHub Trending 也毫不为过。

它究竟有何魅力，竟让诸多开发者如此激动不已呢？别急，且听我娓娓道来。

ChatGPT 是由 OpenAI 于近期推出的一款智能聊天机器人应用，通过人机交互、线上一对一交流的方式，完成需要大量人工才能处理的工作。

而该项目背后的研发团队：OpenAI，这个坐落于旧金山的人工智能研究机构，已然不是第一次凭借其出色的 AI 能力火出圈了。

早在去年，便有用户借助 OpenAI 所提供的 GPT-3，将其已逝去的妻子成功在互联网上 "复活"，并实现了完整对话，把诸多网友看的瞠目结舌。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/640.png)

虽然该用途已因潜在风险被 OpenAI 禁用，但其模型的强大之处，还是由此可见一斑。

近日诞生的 ChatGPT，则是由更进一步的 GPT 3.5 提供底层技术支持，它所具备的能力，更让人感到头皮发麻。

经过这两天的尝试体验，不少用户发现 ChatGPT 已经可以实现诸如智能聊天、写作、编程、批作业、改 Bug、撰写周报、砍价、作诗等工作。更有甚者，还把它直接当虚拟机使用。

下面是我让 ChatGPT 创作的一则短篇小说，大家可以感受下：

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/911.png)

虽说部分故事情节还需润色，但大体框架已颇为完善。

那 ChatGPT 能不能接着帮你润色故事呢？当然可以！

只需要像我这么操作即可：

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/908.png)

不吹不黑，单单把它拿来创作写故事这块，这东西我就能玩一年。

现在，网上关于 ChatGPT 的技术解析与使用教程已有不少，这里便不多做赘述。

下面主要聊聊，GitHub 上与此相关的开源项目，以便大家后续的进阶使用。

目录表

Toggle

* [浏览器插件](#%E6%B5%8F%E8%A7%88%E5%99%A8%E6%8F%92%E4%BB%B6)
  + [1. ChatGPT for Google](#1_ChatGPT_for_Google)
  + [2. ChatGPT Chrome Extension](#2_ChatGPT_Chrome_Extension)
* [逆向工程](#%E9%80%86%E5%90%91%E5%B7%A5%E7%A8%8B)
* [Mac 插件](#Mac_%E6%8F%92%E4%BB%B6)
* [Node.js API 接口](#Nodejs_API_%E6%8E%A5%E5%8F%A3)
* [微信聊天助手](#%E5%BE%AE%E4%BF%A1%E8%81%8A%E5%A4%A9%E5%8A%A9%E6%89%8B)
  + [1. WeChat GPT](#1_WeChat_GPT)
  + [2. ChatGPT WeChat Bot](#2_ChatGPT_WeChat_Bot)

## **浏览器插件**

### **1. ChatGPT for Google**

这款插件支持 Chrome / Edge / Firefox 等浏览器。

在安装之后，除了会在浏览器正常展示 Google 搜索内容，还会在右侧展示 ChatGPT 反馈结果，进一步提升搜索效率。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/001.png)

GitHub：https://github.com/wong2/chat-gpt-google-extension

### **2. ChatGPT Chrome Extension**

这是专为 Chrome 用户开发的一款 ChatGPT 插件。

安装之后，在任意页面文本框中点击右键，即可弹出「Ask ChatGPT」的选项。

选中后，ChatGPT 会根据当前文本框中的内容，执行具体任务。利用这些特性，可以快速完成撰写推文、修改邮件、修复 Bug 等工作，非常方便。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/640.gif)

GitHub：https://github.com/gragland/chatgpt-chrome-extension

## **逆向工程**

任何让工程师充满好奇心的项目，都逃不过逆向，在这一点上，ChatGPT 也不例外。

GitHub 上一位来自马来西亚的开发者 Antonio Cheong，在 ChatGPT 发布没多久后，便对其进行了逆向，成功提取了 API。

有了这些 API，我们便可以自行开发一款好玩的聊天机器人、AI 智能助手、代码辅助工具等应用。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/901.png)

GitHub：https://github.com/acheong08/ChatGPT

## **Mac 插件**

为了让 ChatGPT 的使用更为简便，GitHub 上有开发者为 Mac 用户量身定制了一款小工具：ChatGPT for desktop。

安装之后，可通过 Cmd+Shift+G 快捷键，快速在系统菜单栏启动 ChatGPT。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/002.jpeg)

该工具其实也支持 Windows 系统，只不过需要开发者运行 npm install electron-forge 命令自行编译。

GitHub：https://github.com/vincelwt/chatgpt-mac

## **Node.js API 接口**

平时习惯用 Node.js 开发的同学，建议你关注下「ChatGPT API」这个项目。

它将 ChatGPT 的 API 进行了二次封装，让定制开发流程变得更加轻松。

通过 npm 扩展包进行安装，即可快速使用。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/003.gif)

GitHub：https://github.com/transitive-bullshit/chatgpt-api

## **微信聊天助手**

像 ChatGPT 如此有趣且前卫的黑科技项目，与微信搭配使用，岂不是如虎添翼？

跟我有一样想法的同学，这里给你推荐两个开源项目。

### **1. WeChat GPT**

该项目基于 wechaty 来建立微信与 ChatGPT 的桥梁，让你快速通过微信聊天窗口，发起与 ChatGPT 的对话。

在使用之前，需先配置 OpenAI 的用户信息，以及对应的「关键词」触发。

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/004.png)

GitHub：https://github.com/fuergaosi233/wechat-chatgpt

### **2. ChatGPT WeChat Bot**

这个项目基于 NodeJS 和 webchaty 开发，同上面项目一样，用 Docker 部署，配置完用户信息后，即可快速使用。

你可以在群里拉入机器人，@它并发起一个问题，便能得到响应。

这是实际使用效果：

![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/uploads/2023/02/005.png)

GitHub：https://github.com/AutumnWhj/ChatGPT-wechat-bot

点赞(0)

打赏

分享

标签：[AI](https://www.uedbox.com/post/tag/ai/) , [ChatGPT](https://www.uedbox.com/post/tag/chatgpt/) , [OpenAI](https://www.uedbox.com/post/tag/openai/) , [人工智能](https://www.uedbox.com/post/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/)  原文连接：**[ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/post/68725/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/post/68717/ "了解Nearby Interaction探索与第三方硬件的近距离交互") [解决Error: php@7.4 has been disabled because it is a versioned formula](https://www.uedbox.com/post/68765/ "解决Error: php@7.4 has been disabled because it is a versioned formula")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/post/69717/ "cursor, 一款基于 vscode 的 AI IDE")

[![ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/post/68799/ "ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事")

[![两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/post/69909/ "两个生成式AI 平台推荐，生产力亲测")

[![ChatGPT 的 12 个主要用例](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT 的 12 个主要用例](https://www.uedbox.com/post/68804/ "ChatGPT 的 12 个主要用例")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

[![ChatGPT推荐30岁女人必看的20部电影 ](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT推荐30岁女人必看的20部电影](https://www.uedbox.com/post/68807/ "ChatGPT推荐30岁女人必看的20部电影 ")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南](https://www.uedbox.com/post/68815/ "如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![肌理解剖师：中年人的小确幸](https://www.ued...