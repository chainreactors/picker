---
title: cursor, 一款基于 vscode 的 AI IDE
url: https://www.uedbox.com/post/69717/
source: 体验盒子
date: 2024-10-02
fetch_date: 2025-10-06T18:54:47.616724
---

# cursor, 一款基于 vscode 的 AI IDE

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

# cursor, 一款基于 vscode 的 AI IDE

* 发表于 2024年10月01日
* [人工智能](https://www.uedbox.com/ai/)

为大家推荐 cursor， 一款基于 vscode 的 AI IDE

目录表

Toggle

* [优点](#%E4%BC%98%E7%82%B9)
* [规则文件](#%E8%A7%84%E5%88%99%E6%96%87%E4%BB%B6)
* [下载地址](#%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80)
* [便宜强大的国产大模型接口 deepseek](#%E4%BE%BF%E5%AE%9C%E5%BC%BA%E5%A4%A7%E7%9A%84%E5%9B%BD%E4%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%A5%E5%8F%A3_deepseek)
  + [价格](#%E4%BB%B7%E6%A0%BC)
  + [OpenAI 兼容 base url](#OpenAI_%E5%85%BC%E5%AE%B9_base_url)
  + [一些 URL](#%E4%B8%80%E4%BA%9B_URL)
* [如何配置 DeepSeek](#%E5%A6%82%E4%BD%95%E9%85%8D%E7%BD%AE_DeepSeek)
* [🤔 疑问](#%F0%9F%A4%94_%E7%96%91%E9%97%AE)

## 优点

* 能够为整个项目建立索引，生成代码更合逻辑
* 代码生成模式比 Copilot 好
  + 不局限于代码补全
* IDE 基于 vscode 二次开发
  + vscode 插件兼容
  + 如果以前就用 vscode，很快就能熟悉
  + remote 开发功能能够正常使用
* 可以自定义大模型接口 (openai 兼容)
  + 可以使用 便宜强大的国产大模型接口 deepseek
  + 配置简单
  + 无需🪜
  + 按量付费，非常便宜
    - 我每日大概消耗 3万 Token，约合3分钱，充值10元几乎可以用一年
  + 可以用自己跑的大模型

## 规则文件

<https://cursor.directory>

Copy and add a .cursorrules file in the root of your project.

The instructions in the .cursorrules file will be included for features such as Cursor Chat and Ctrl/⌘ K.

The more specific your rules for your project, the better.

此网站还有 cursor 使用教程 <https://cursor.directory/learn>

网站里面的规则 prompt 写的很好，给 AI 事无巨细地阐述技术栈、代码风格等

prompt 里有些部分程序员看了都会有收获

## 下载地址

<https://www.cursor.com>

文档 <https://docs.cursor.com/>

## 便宜强大的国产大模型接口 deepseek

### 价格

<https://platform.deepseek.com/api-docs/zh-cn/pricing>

| 模型 | 上下文长度 | 最大输出长度 | 输入价格（缓存命中） | 输入价格（缓存未命中） | 输出价格 |
| --- | --- | --- | --- | --- | --- |
| deepseek-chat | 128K | 4K (8K Beta (2)) | 0.1 元 / 百万 tokens | 1 元 / 百万 tokens | 2 元 / 百万 tokens |
| deepseek-coder | 128K | 4K (8K Beta (2)) | 0.1 元 / 百万 tokens | 1 元 / 百万 tokens | 2 元 / 百万 tokens |

### OpenAI 兼容 base url

|  |  |
| --- | --- |
| 1 | https://api.deepseek.com/v1 |

|  |  |
| --- | --- |
| 1 | https://api.deepseek.com/beta |

### 一些 URL

<https://chat.deepseek.com>

<https://platform.deepseek.com/usage>

<https://platform.deepseek.com/api-docs/zh-cn/news/news0802>

## 如何配置 DeepSeek

简易版本：

* 打开 cursor， 点击右上角齿轮按钮，打开 cursor settings
* 切换到 Models Tab
* 关掉所有Model Names
* 添加一个 Model Name
  `deepseek-coder`
* 这样可以限制只会以这个model name 调用openai兼容接口
* OpenAI API Key 一栏中
  + 填写自己的 deepseek api key
  + Override OpenAI Base URL 填写
    - `https://api.deepseek.com/v1`
* 点击 Verify 按钮
* 验证成功后，OpenAI API Key 右上角会出现一个开关 ，保持打开即可

![cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/wp-content/uploads/2024/10/pasted-image-313afb33442f00930ca8d46cfa832a4d.png)

原教程： <https://juejin.cn/post/7400945359194210316>

## 🤔 疑问

我每天执行代码补全，最起码有100次 但我看deepseek的接口用量统计中显示只有10次

抓包发现 cursor 在执行代码补全时会发出向
`api[\d].cursor.io`
 host 的请求

只有用 ⌘+k 进行代码生成 或 在Chat侧边栏对话时，才会调用 deepseek 域名

so… 代码补全并没有使用刚刚配置的 deepseek

磊哥曾发出疑问：cursor IDE不收费，又允许自定义大模型接口，那我们都用deepseek，他怎么挣钱？

现在我猜测是卖代码补全接口

再试用一下 等 cursor 的注册账号赠送2周会员到期，看看会不会要求收费

点赞(1)

打赏

分享

标签：[AI](https://www.uedbox.com/post/tag/ai/) , [cursor](https://www.uedbox.com/post/tag/cursor/) , [IDE](https://www.uedbox.com/post/tag/ide/) , [vscode](https://www.uedbox.com/post/tag/vscode/)  原文连接：**[cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/post/69717/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[git 设置和取消代理](https://www.uedbox.com/post/69715/ "git 设置和取消代理") [解决WordPress上传svg/ico/webp，您无权上传此文件类型](https://www.uedbox.com/post/69734/ "解决WordPress上传svg/ico/webp，您无权上传此文件类型")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/post/68799/ "ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

[![ChatGPT 的 12 个主要用例](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT 的 12 个主要用例](https://www.uedbox.com/post/68804/ "ChatGPT 的 12 个主要用例")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![ChatGPT推荐30岁女人必看的20部电影 ](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT推荐30岁女人必看的20部电影](https://www.uedbox.com/post/68807/ "ChatGPT推荐30岁女人必看的20部电影 ")

[![Dart DevTools exited with code 255解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Dart DevTools exited with code 255解决](https://www.uedbox.com/post/66983/ "Dart DevTools exited with code 255解决")

[![如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南](https://www.uedbox.com/post/68815/ "如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南")

[![VSCode技巧：快速生成html模板](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

VSCode技巧：快速生成html模板](https://www.uedbox.com/post/67749/ "VSCode技巧：快速生成html模板")

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

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/post/119352/ "🔥 最新免费域名资源大全 | 永久免费域名获取")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

* [最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")
* [NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")
* [Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

* [2025 BT磁力搜索引擎大全【最新优质】](https://www.uedbox.com/post/54994/ "2025 BT磁力搜索引擎大全【最新优质】")
* [怎么用图片搜索番号？以图搜图AI搜图](https://www.uedbox.com/post/55287/ "怎么用图片搜索番号？以图搜图AI搜图")
* [this channel is blocked because it was used：Telegram群组/频道屏蔽解决方法](https://www.uedbox.com/post/56387/ "this channel is bl...