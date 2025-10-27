---
title: Docker快速搭建ChatGPT网页版
url: https://buaq.net/go-153264.html
source: unSafe.sh - 不安全
date: 2023-03-14
fetch_date: 2025-10-04T09:27:58.957016
---

# Docker快速搭建ChatGPT网页版

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

![](https://8aqnet.cdn.bcebos.com/ca17fcfa5e5b5f6af4e9dd802c4a7873.jpg)

Docker快速搭建ChatGPT网页版

GitHub地址：https://github.com/Chanzhaoyu/chatgpt-web支持双模型，提供了两种非官方 ChatGPT AP
*2023-3-13 22:29:0
Author: [blog.upx8.com(查看原文)](/jump-153264.htm)
阅读量:186
收藏*

---

[![cover](https://github.com/Chanzhaoyu/chatgpt-web/raw/main/docs/c1.png)](https://github.com/Chanzhaoyu/chatgpt-web/blob/main/docs/c1.png) [![cover2](https://github.com/Chanzhaoyu/chatgpt-web/raw/main/docs/c2.png)](https://github.com/Chanzhaoyu/chatgpt-web/blob/main/docs/c2.png)

## **GitHub地址：**<https://github.com/Chanzhaoyu/chatgpt-web>

支持双模型，提供了两种非官方 `ChatGPT API` 方法

| 方式 | 免费？ | 可靠性 | 质量 |
| --- | --- | --- | --- |
| `ChatGPTAPI(gpt-3.5-turbo-0301)` | 否 | 可靠 | 相对较笨 |
| `ChatGPTUnofficialProxyAPI(网页 accessToken)` | 是 | 相对不可靠 | 聪明 |

对比：

1. `ChatGPTAPI` 使用 `gpt-3.5-turbo-0301` 通过官方`OpenAI`补全`API`模拟`ChatGPT`（最稳健的方法，但它不是免费的，并且没有使用针对聊天进行微调的模型）
2. `ChatGPTUnofficialProxyAPI` 使用非官方代理服务器访问 `ChatGPT` 的后端`API`，绕过`Cloudflare`（使用真实的的`ChatGPT`，非常轻量级，但依赖于第三方服务器，并且有速率限制）

警告：

1. 你应该首先使用 `API` 方式
2. 使用 `API` 时，如果网络不通，那是国内被墙了，你需要自建代理，绝对不要使用别人的公开代理，那是危险的。
3. 使用 `accessToken` 方式时反向代理将向第三方暴露您的访问令牌，这样做应该不会产生任何不良影响，但在使用这种方法之前请考虑风险。
4. 使用 `accessToken` 时，不管你是国内还是国外的机器，都会使用代理。默认代理为 [acheong08](https://github.com/acheong08) 大佬的 `https://bypass.duti.tech/api/conversation`，这不是后门也不是监听，除非你有能力自己翻过 `CF` 验证，用前请知悉。[社区代理](https://github.com/transitive-bullshit/chatgpt-api#reverse-proxy)（注意：只有这两个是推荐，其他第三方来源，请自行甄别）
5. 把项目发布到公共网络时，你应该设置 `AUTH_SECRET_KEY` 变量添加你的密码访问权限，你也应该修改 `index.html` 中的 `title`，防止被关键词搜索到。

切换方式：

1. 进入 `service/.env.example` 文件，复制内容到 `service/.env` 文件
2. 使用 `OpenAI API Key` 请填写 `OPENAI_API_KEY` 字段 [(获取 apiKey)](https://platform.openai.com/overview)
3. 使用 `Web API` 请填写 `OPENAI_ACCESS_TOKEN` 字段 [(获取 accessToken)](https://chat.openai.com/api/auth/session)
4. 同时存在时以 `OpenAI API Key` 优先

**获取自己的OPENAI的APIkey：**<https://platform.openai.com/account/api-keys>

**更新环境**

**安装 Docker**

**创建GPT目录，创建配置文件**

**compose配置代码**

version: '3.8'

**运行指令**

**创建nginx目录结构**

**进入目录编辑文件**

**反向代理配置，代理指定IP加端口**

**部署容器**

**查看运行状态**

**开机自启动**

文章来源: https://blog.upx8.com/3264
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)