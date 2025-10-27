---
title: Django 打包为 docker 镜像
url: https://h4ck.org.cn/2024/11/18624
source: obaby@mars
date: 2024-11-26
fetch_date: 2025-10-06T19:17:17.433865
---

# Django 打包为 docker 镜像

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[程序设计『Programing』](https://h4ck.org.cn/cats/cxsj)

# Django 打包为 docker 镜像

2024年11月25日
[33 条评论](https://h4ck.org.cn/2024/11/18624#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/12081732512632_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/12081732512632_.pic_.jpg)

之前也想过将 django 项目打包成 docker 部署，但是由于之前的项目过于庞大，用到了系统的定时任务等各种系统服务，不知道打包成 docker 之后相关的服务是否依然能够启动，所以并未实施。

前几天做的我的足迹地图，项目相对来说比较独立，没有其他的依赖项，正好可以尝试一下。

首先在项目下创建 Dockerfile，写入以下内容：

```
# 使用官方Python运行时作为父镜像
FROM python:3.8.18-slim

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于/app中的容器中
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露端口8000，与Django的默认运行端口一致
EXPOSE 10086

# 定义环境变量
ENV NAME=Django

# 在容器启动时运行Django的manage.py命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:10086"]
```

网上代码来回抄，第二行都是FROM python:3.8-slim 如果这么写会导致下面的错误：

```
PS E:\Pycharm_Projects\BabyFootprintV2> docker build -t baby-footprint:1.0 .
[+] Building 21.2s (2/2) FINISHED docker:desktop-linux
 => [internal] load build definition from Dockerfile 0.0s
 => => transferring dockerfile: 568B 0.0s
 => ERROR [internal] load metadata for docker.io/library/python:3.8-slim 21.1s
------
 > [internal] load metadata for docker.io/library/python:3.8-slim:
------
Dockerfile:2
--------------------
   1 | # 使用官方Python运行时作为父镜像
   2 | >>> FROM python:3.8-slim
   3 |
   4 | # 设置工作目录
--------------------
ERROR: failed to solve: python:3.8-slim: failed to resolve source metadata for docker.io/library/python:3.8-slim: failed to do request: Head "https://registry-1.docker.io/v2/library/python/manifests/3.8-slim": dialing registry-1.docker.io:443 container via direct connection because has no HTTPS proxy: connecting to registry-1.docker.io:443: dial tcp 69.63.186.31:443: connectex: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.
```

直接访问上面的网址docker.io/library/python:3.8-slim会发现根本没这么东西，所以要改成FROM python:3.8.18-slim

搜索一下，会有教程提示先下载 python3.8的 docker：

```
PS E:\Pycharm_Projects\BabyFootprintV2> docker pull python:3.8.18-slim
3.8.18-slim: Pulling from library/python
8a1e25ce7c4f: Pull complete
1103112ebfc4: Pull complete
b7d41b19b655: Pull complete
6a1ad0671ce8: Pull complete
de92c59aadaa: Pull complete
Digest: sha256:e796941013b10bb53a0924d8705485a1afe654bbbc6fe71d32509101e44b6414
Status: Downloaded newer image for python:3.8.18-slim
docker.io/library/python:3.8.18-slim
```

3.8.18是 ok 的，此时重新 build 即可：

```
PS E:\Pycharm_Projects\BabyFootprintV2> docker build -t baby-footprint:1.0 .
[+] Building 214.6s (9/9) FINISHED docker:desktop-linux
 => [internal] load build definition from Dockerfile 0.0s
 => => transferring dockerfile: 571B 0.0s
 => [internal] load metadata for docker.io/library/python:3.8.18-slim 0.0s
 => [internal] load .dockerignore 0.0s
 => => transferring context: 2B 0.0s
 => [1/4] FROM docker.io/library/python:3.8.18-slim 0.1s
 => [internal] load build context 0.9s
 => => transferring context: 43.30MB 0.8s
 => [2/4] WORKDIR /app 0.1s
 => [3/4] COPY . /app 0.2s
 => [4/4] RUN pip install --no-cache-dir -r requirements.pip -i https://pypi.tuna.tsinghua.edu.cn/simple 212.0s
 => exporting to image 1.4s
 => => exporting layers 1.4s
 => => writing image sha256:cba073b574f88f19be7487b29612e19b9826ab99e7b54ea748bd5df22e83e1a0 0.0s
 => => naming to docker.io/library/baby-footprint:1.0 0.0s
```

编译变成，就可以像 docker hub 推送镜像了，不过首先需要设置 tag,如果直接推送会提示下面的错误：

```
PS E:\Pycharm_Projects\BabyFootprintV2> docker push baby-footprint:1.0
The push refers to repository [docker.io/library/baby-footprint]
04013169f44d: Preparing
f7c443286fad: Retrying in 5 seconds
fd749af069d5: Retrying in 5 seconds
3482d4cd60de: Retrying in 5 seconds
370c0e78e3ea: Retrying in 5 seconds
a74bee0a48a5: Waiting
c8f253aef560: Waiting
a483da8ab3e9: Waiting
denied: requested access to the resource is denied
```

这个提示也比较坑人，由于 docker 被屏蔽，我一直以为是网络连接问题，直到后来才发现是路径问题。

通过下面的命令设置 tag 后 push：

```
docker tag baby-footprint:1.0 obaby/baby-footprint:1.0
```

```
PS E:\Pycharm_Projects\BabyFootprintV2> docker push obaby/baby-footprint:1.0
The push refers to repository [docker.io/obaby/baby-footprint]
04013169f44d: Pushed
f7c443286fad: Pushed
fd749af069d5: Pushed
3482d4cd60de: Pushed
370c0e78e3ea: Layer already exists
a74bee0a48a5: Pushed
c8f253aef560: Pushed
a483da8ab3e9: Layer already exists
1.0: digest: sha256:0d0c0989a64cc3f3e192e5c8e7bc4931676d49ab66d810061a1daec6b1a6af58 size: 2000
```

受限于网络问题，可能会 push 失败，多重试几次就 ok 了。

最后就可以直接 docker 安装运行啦:

```
docker push obaby/baby-footprint:tagname

```

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241125-134859-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241125-134859.jpg)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Django 打包为 docker 镜像》](https://h4ck.org.cn/2024/11/18624)
\* 本文链接：<https://h4ck.org.cn/2024/11/18624>
\* 短链接：<https://oba.by/?p=18624>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Django](https://h4ck.org.cn/tags/django)[docker](https://h4ck.org.cn/tags/docker)[Python](https://h4ck.org.cn/tags/python)

[Previous Post](https://h4ck.org.cn/2024/11/18629)
[Next Post](https://h4ck.org.cn/2024/11/18592)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2021年9月21日

#### [秀人集爬虫 【21.9.21】【Windows】](https://h4ck.org.cn/2021/09/9036)

2024年7月31日

#### [也谈 cf 的 npm 代理 以及 uniapp vendor.js 压缩](https://h4ck.org.cn/2024/07/17750)

2019年11月8日

#### [jupyter notebook 调整字体 以及matplotlib显示中文](https://h4ck.org.cn/2019/11/6583)

### 33 comments

1. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r) **爱看**说道：

   [2024年11月25日 14:02](https://h4ck.org.cn/2024/11/18624#comment-121458)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   强势沙发

   [回复](#comment-121458)
2. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r)

   [2024年11月25日 14:03](https://h4ck.org.cn/2024/11/18624#comment-121459)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   评论框顶端没边框线条，强迫症表示不可忍

   灵妹妹换成什么路由器...