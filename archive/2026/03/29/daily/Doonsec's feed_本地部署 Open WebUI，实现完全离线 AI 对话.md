---
title: 本地部署 Open WebUI，实现完全离线 AI 对话
url: https://mp.weixin.qq.com/s/FRjMdJSdMgvwjak7eHUFOQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:43:28.049175
---

# 本地部署 Open WebUI，实现完全离线 AI 对话

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/06rXhwxBPYblpj8uK3A8zkGfkaYqM6JNiaATicibtRYxKaDggu9A8bMN7FP1ZMjr5Nea83ylZokmIKic6MdKhWCWxRZH40pkMK6dic6icEulGQIh4/0?wx_fmt=jpeg)

# 本地部署 Open WebUI，实现完全离线 AI 对话

原创

TP微客
TP微客

技术分享交流

![]()

在小说阅读器中沉浸阅读

1 前言

    Open WebUI（原 Ollama WebUI）是一款开源、可自托管、支持完全离线的大语言模型（LLM）交互 Web 平台，主打私有化部署与隐私安全，提供跟AI大模型的流畅对话体验。

2 搭建过程

(1)本地部署

在centos上通过如下命令启动docker：

```
 systemctl start docker
```

 该命令用于启动系统中的 Docker 服务，执行完成后，可通过 systemctl status docker 查看运行状态，确认服务启动成功。如果 Docker 未设置开机自启，也可以使用 systemctl enable docker 命令配置开机自动启动，避免服务器重启后需要手动再次启动服务。

配置镜像源

```
vi /etc/docker/daemon.json {  "registry-mirrors": ["https://mirror.tuna.tsinghua.edu.cn/"]}
```

 添加国内镜像源可以显著提升容器镜像拉取速度，避免因网络问题导致下载缓慢或失败。配置完成后，需要执行 systemctl daemon-reload 和 systemctl restart docker 使配置生效。

下载open-webui

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/06rXhwxBPYY3lXHwj7au7Y3SOWI8dNLc9sR8fx1pKkVfA41vibGFqwfy2OycogPWiaw7U45KoDaRic7fjgx8V45dCs5VnL9griaxxqibzc6wHfNY/640?wx_fmt=png)

 这条命令会以后台模式启动 Open WebUI 容器，将本地 3000 端口映射到容器内部 8080 端口，方便外部访问。同时挂载数据卷，保证配置、对话记录等数据持久化存储，容器重启后不会丢失。`--restart always` 确保容器异常退出或服务器重启时能够自动恢复。执行后等待镜像拉取完成，容器启动成功即可进入下一步。

(2)访问页面

打开open-webui的网址，使用如下网址和端口访问：

```
http://x.x.x.x:3000/
```

![](https://mmbiz.qpic.cn/mmbiz_png/06rXhwxBPYZH2tmTnRHNGlxtw9WJumZTBUf5jOyUTJp2UM4X8MdhaibcBf8ia3NH53qWMToK2Ju9HYHvJVzef7dr2BeRmlG6CNwF4FxMd3Aes/640?wx_fmt=png)

填写名称、电子邮箱、密码等信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/06rXhwxBPYYQQiciaB1SjTfZh1BzG53F7hhxib70ogPeCmCAic9l7HicqkBLb7Od9V2heTQnp4OjfibUllKqcXdxkF1wFRZwfZpAl0Efxpo57v6IQ/640?wx_fmt=png)

 首次访问会自动进入注册界面，这是系统的管理员账号创建流程。电子邮箱可以使用任意有效格式，无需真实验证，主要用于账号标识和后续登录管理。密码建议设置复杂度较高的组合，提升平台安全性，防止未授权访问。

点击确认，开始使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/06rXhwxBPYZLh65kQDLXdOibHuicgFxGDXU0ic5K0jR9fOHEYia25JI7nGseREicEbgpl2q2NdMpDdGWhicTlvvhXSNzZOcOibDWcib1fQzUw8XW0Vs/640?wx_fmt=png)

(3)配置

点击配置，填写ollama相关的连接地址和端口

![](https://mmbiz.qpic.cn/mmbiz_png/06rXhwxBPYYrLDBqcodjcs966CAiaoNuJg4btySrOa1Q4ZuAFXT3yDibq9LfU4KwJ2QXmB7tt6LwN1mLDZDicN9S5tRh5JaJ6FU8DM04NDFx9Q/640?wx_fmt=png)

在ollma中下载你想要的模型

![](https://mmbiz.qpic.cn/mmbiz_png/06rXhwxBPYYKgHw4fcSicJXiazibZNibLicMFCu6B95d17XTyn93DrhbuGe8ytwMCjkUOqahNxuBurGS9PFXV4gBkym9b5WydRjcG2HsZiaoU5NTE/640?wx_fmt=png)

在open-webui中查看，就能看到你下载的大模型

![](https://mmbiz.qpic.cn/mmbiz_png/06rXhwxBPYbMOnMH3HGCXZxfaDRZLickg0gPlTRhcXTNZY2jtYFzice0nvOnSB9rIx4prnEE96mz9y8olK0iaibVibgybPzVYibDY2yX4eTqcdQHk/640?wx_fmt=png)

(4)开始使用

通过直接输入你想要做的事情

```
例如：帮我写一个烟花绽放的html脚本，烟花自动升向空中，并绽放开来，烟花是五颜六色的，要考虑色彩搭配
```

 输入指令后，系统会调用已加载的大模型进行推理生成，响应速度取决于模型大小和服务器性能。生成的内容支持复制、导出，同时支持多轮对话上下文记忆，可连续追问和补充需求，满足代码编写、文案生成、问题解答等多种场景使用。

![](https://mmbiz.qpic.cn/mmbiz_png/06rXhwxBPYaea5Pbho30M3RhD9RCibLj12VyPXosTnkRe1tPBmfrnFiakTwx1seLyLOiccv9brzjXG1VGCAfibgk8TmAOlUkYjhCTR7PHJoW6rk/640?wx_fmt=png)

其实这就是一个ollama大模型的使用页面，不过这个我感觉挺好用的，接下来，我将继续研究用这个搭建一个属于自己的AI Agent。

---

欢迎关注「技术分享交流」公众号 ，如果有建议或者疑问的话，欢迎大家评论留言，如果喜欢公众号文章的话可以点【在看】，您的鼓励就是我的动力哈！！！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EwzDib7ziaFFNMI0QlbZ0mAxbu30RhkgibUng33sibDErYLDvZRhNUzQrexStu7SsJ29cuyPsjkNUgA18ibibJ8Mdxaw/0?wx_fmt=png)

技术分享交流

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EwzDib7ziaFFNMI0QlbZ0mAxbu30RhkgibUng33sibDErYLDvZRhNUzQrexStu7SsJ29cuyPsjkNUgA18ibibJ8Mdxaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过