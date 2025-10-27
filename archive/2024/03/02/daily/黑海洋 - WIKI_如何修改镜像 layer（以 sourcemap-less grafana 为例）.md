---
title: 如何修改镜像 layer（以 sourcemap-less grafana 为例）
url: https://blog.upx8.com/4084
source: 黑海洋 - WIKI
date: 2024-03-02
fetch_date: 2025-10-04T12:11:42.195262
---

# 如何修改镜像 layer（以 sourcemap-less grafana 为例）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 如何修改镜像 layer（以 sourcemap-less grafana 为例）

发布时间:
2024-03-01

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
10768

## 前言

前段时间一个项目里面，对方用扫描器扫出来 grafana 有 sourcemap 文件，其实这原本是无风险的，有瑕疵还是处理一下。

本文会简单介绍一下修改镜像 layer 的方法。

## 开始

首先要明确一个概念，镜像是由一层层的 layer 叠加起来的，所以直接在 Dockerfile 当中 `from image` `RUN rm -rf file` 是没有意义的，前面的 layer 当中的文件依然可以被提取出来。所以需要直接对 layer 进行操作。

然后要读懂 image 的格式，我喜欢 oci format，所以以下均为 oci format 的操作。

先把镜像拉下来

```
crane pull --format=oci grafana:grafana:8.5.27 ./grafana
```

oci format 为一个文件夹，目录树为

index.json
oci-layout
blobs/sha256/\*

所有 manifest 里面的 sha256 都是对应 blobs/sha256/ 底下的文件

所以就一层一层找

index.json [> multi\_platform\_manifest ]> single\_platform\_manifest > special\_layer
这样的路径向下找要修改的文件，找到目标 layer（layer 会是一个 gzip tarball）修改完内容之后对内容进行 sha256sum，把内容重命名为 sha256value，然后修改上一层 manifest 里面的 digest 和 size，然后继续向上修改 manifest，不断重复这件事。

这是 layer 部分的修改，除此之外，还需要修改 image config。

special\_layer 是一个 tar.gz。我们解压出来修改完内容之后（这会是一个 tar），此时也需要计算一次 sha256，这个值需要被填充到 image config 的 `.rootfs.diff_ids[layer_index]`。然后再进行 gzip 生成 tar.gz。要是不进行 config diff\_ids 的修改，会出现 `layers from manifest don't match image configuration.` 的报错。

大体流程就是如此。

## 具体 layer 的修改

针对本次目标（删除 grafana 里面的 sourcemap），找了了 layer 之后，只需要

```
cd blobs/sha256
target=layer_filename
mv "$target" "$target.tar.gz"
gunzip "$target.tar.gz"
tar --wildcards --delete '*.js.map' -f "$target.tar"
# 此处需要 sha256sum "$target.tar"，填充到 diff_ids 对应位置
gzip "$target.tar"
# 这样就得到了修改完的 tar.gz layer，sha256 重命名一下就行
```

完整的过程我写成了一个 bash 脚本，放在了 [hunshcn/grafana-sourcemap-less](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2h1bnNoY24vZ3JhZmFuYS1zb3VyY2VtYXAtbGVzcw)，可以自行制作 sourcemap less 镜像，寻找 target layer 的规则是 layer 倒序找到第一个 size > 1000000 的 layer，理论上如果有其他镜像需要移除 sourcemap 只需要修改这个逻辑即可。

手改的和脚本改的会有一点点差异。

因为脚本改的会把 manifest 的缩进扔掉，因为用了 yq –inplace， size 可能会因此出现变化。

然后手改的缩进自然是不会变的，但是 size 一样会变，用 vim 修改会比原来多一个字节（比如 2203 把 sha256 替换了会变成 2204），应该是多了一个控制字符，我没有过多探究。

[取消回复](https://blog.upx8.com/4084#respond-post-4084)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")