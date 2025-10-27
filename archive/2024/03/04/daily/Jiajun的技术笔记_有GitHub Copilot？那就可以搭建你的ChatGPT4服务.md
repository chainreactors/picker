---
title: 有GitHub Copilot？那就可以搭建你的ChatGPT4服务
url: https://jiajunhuang.com/articles/2024_03_03-copilot_as_gpt4.md.html
source: Jiajun的技术笔记
date: 2024-03-04
fetch_date: 2025-10-04T12:08:22.216542
---

# 有GitHub Copilot？那就可以搭建你的ChatGPT4服务

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [有GitHub Copilot？那就可以搭建你的ChatGPT4服务](#%25E6%259C%2589GitHub%2bCopilot%25EF%25BC%259F%25E9%2582%25A3%25E5%25B0%25B1%25E5%258F%25AF%25E4%25BB%25A5%25E6%2590%25AD%25E5%25BB%25BA%25E4%25BD%25A0%25E7%259A%2584ChatGPT4%25E6%259C%258D%25E5%258A%25A1)
* [方案1：直接使用API Key搭建](#%25E6%2596%25B9%25E6%25A1%25881%25EF%25BC%259A%25E7%259B%25B4%25E6%258E%25A5%25E4%25BD%25BF%25E7%2594%25A8API%2bKey%25E6%2590%25AD%25E5%25BB%25BA)
* [方案2：把 Github Copilot 转化成 API](#%25E6%2596%25B9%25E6%25A1%25882%25EF%25BC%259A%25E6%258A%258A%2bGithub%2bCopilot%2b%25E8%25BD%25AC%25E5%258C%2596%25E6%2588%2590%2bAPI)

# 有GitHub Copilot？那就可以搭建你的ChatGPT4服务

我有Github Copilot，也订阅了GPT Plus，GPT Plus 20刀每月，我看了一下其实我用的不是特别多。本着开猿节流，降本增笑的精神，
我停止续订了GPT Plus，并且着手于找到 GPT Plus 的替代方案。

## 方案1：直接使用API Key搭建

如果你有 API Key，那么可以直接使用 API Key来搭建，这个很简单，方案也很多，比如川虎，lobe-chat, ChatGPT-Next-Web，然后
输入你的 API Key就可以。

> 我有 API Key，但是折腾是一种乐趣，所以我选择了方案2。

## 方案2：把 Github Copilot 转化成 API

之前在Hacker News看到过，Github Copilot底层其实就是用的OpenAI，因此有人开发了将 Github 接口转化成 OpenAI API 的服务。
因此我们想要搭建一套自己私有的 ChatGPT Web的话，需要3步：

1. 获取 Github Copilot Token
2. 搭建 Github Copilot 转化为 OpenAI API 的客户端并且配置域名
3. 搭建并配置 ChatGPT-Next-Web 或其他Web客户端

第一步，其实比较难，现在网上很多方案都失效了，但是记住一点，既然 Copilot 要在本地使用，而Copilot服务端是要鉴权的，
本地就必然保存了Token在磁盘上，要不然它下次咋鉴权呢？我用的是 vim-copilot，所以我直接在家目录找：

```
$ find .config -name '*copilot*'
.config/github-copilot
.config/gh-copilot
.config/nvim/plugged/copilot.vim
.config/nvim/plugged/copilot.vim/autoload/copilot
.config/nvim/plugged/copilot.vim/autoload/copilot.vim
.config/nvim/plugged/copilot.vim/lua/_copilot.lua
.config/nvim/plugged/copilot.vim/doc/copilot.txt
.config/nvim/plugged/copilot.vim/plugin/copilot.vim
.config/nvim/plugged/copilot.vim/syntax/copilot.vim
```

然后一个一个翻，果然，配置文件就藏在 `.config/github-copilot/hosts.json` 里，找出来，是一个 `ghu_` 开头的token，保存。

第二步，搭建Copilot 转化为 API 的服务，我直接用Docker：

```
docker run -d \
    -e COPILOT_TOKEN=<刚才找到的Copilot里的token，ghu_ 开头的那个> \
    -e SUPER_TOKEN=<自定义的token，等会儿给 ChatGPT-Next-Web使用> \
    -e ENABLE_SUPER_TOKEN=true \
    --name copilot-gpt4-service \
    --restart always \
    -p 8080:8080 \
    aaamoon/copilot-gpt4-service:latest
```

为了方便，我配置了一个域名，假设为 `https://openai.example.com`。

第三步，搭建 `ChatGPT-Next-Web`，同样，我直接使用 Docker:

```
docker run -d -p 3000:3000 \
    -e BASE_URL=<你配置的域名> \
    -e OPENAI_API_KEY=<刚才设置的 SUPER_TOKEN，也就是自定义的token> \
    -e CODE=<等于一个登录密码，防止 ChatGPT-Next-Web 被他人滥用> \
    yidadaa/chatgpt-next-web
```

同样为了方便，为 ChatGPT-Next-Web 也配置一个域名，然后就可以访问了。

访问以后，在设置里，设置登录密码，将模型改为 `GPT4` 或者 `GPT4-Turbo`，将界面语言改为中文，如果想要同步聊天记录的话，
可以配置上自己的 webdav。

至此，大功告成！注意一点，就是搭建出来的服务，仅限于自己使用，不要到处发，否则使用频率太高，被Github检测出来，那有可能
就被拉黑了以后就无法使用Copilot了💔

---

Refs:

* <https://github.com/aaamoon/copilot-gpt4-service>
* <https://github.com/GaiZhenbiao/ChuanhuChatGPT>
* <https://github.com/lobehub/lobe-chat>
* <https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web>

---

##### 相关文章

* [再读vim help：vim小技巧](/articles/2017_01_24-vim_manual.md.html)
* [再读 Python Language Reference](/articles/2017_01_24-python_language_reference.md.html)
* [设计模式（2）- 深入浅出设计模式 阅读笔记](/articles/2017_01_22-head_first_design_patterns_2.md.html)
* [设计模式（1）- 深入浅出设计模式 阅读笔记](/articles/2017_01_21-head_first_design_patterns.md.html)
* [Cython! Python和C两个世界的交叉点](/articles/2017_01_15-cython_rocks.md.html)
* [socketserver 源码阅读与分析](/articles/2017_01_09-socketserver_source_code.md.html)
* [functools 源码阅读与分析](/articles/2017_01_08-functools_source_code.md.html)
* [contextlib代码阅读](/articles/2017_01_07-contextlib_source_code.md.html)
* [Collections 源码阅读与分析](/articles/2017_01_06-collections_source_code.md.html)
* [Redis通信协议阅读](/articles/2017_01_06-redis_protocol_specification.md.html)
* [2016年就要结束了，2017年就要开始啦！](/articles/2016_12_31-2016_is_over_and_2017_is_coming.md.html)
* [unittest 源代码阅读](/articles/2016_12_29-unittest_source_code.md.html)
* [APUEv3 - 重读笔记](/articles/2016_12_26-apue_v3.md.html)
* [Mock源码阅读与分析](/articles/2016_12_22-mock_source_code.md.html)
* [Thinking in Python](/articles/2016_12_16-thinking_in_python.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。