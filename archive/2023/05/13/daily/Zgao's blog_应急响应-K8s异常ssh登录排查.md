---
title: 应急响应-K8s异常ssh登录排查
url: https://zgao.top/%e5%ba%94%e6%80%a5%e5%93%8d%e5%ba%94-k8s%e5%bc%82%e5%b8%b8ssh%e7%99%bb%e5%bd%95%e6%8e%92%e6%9f%a5/
source: Zgao's blog
date: 2023-05-13
fetch_date: 2025-10-04T11:36:36.189782
---

# 应急响应-K8s异常ssh登录排查

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 应急响应-K8s异常ssh登录排查

* [首页](https://zgao.top)
* [应急响应-K8s异常ssh登录排查](https://zgao.top:443/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-k8s%E5%BC%82%E5%B8%B8ssh%E7%99%BB%E5%BD%95%E6%8E%92%E6%9F%A5/)

[5月 12, 2023](https://zgao.top/2023/05/)

### 应急响应-K8s异常ssh登录排查

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-k8s%E5%BC%82%E5%B8%B8ssh%E7%99%BB%E5%BD%95%E6%8E%92%E6%9F%A5/)

> 某内网k8s集群主机安全告警存在ssh爆破成功的记录，上机排查发现该主机存在长达几个月的异常ssh登录，每天固定凌晨0点-4点出现ssh登录记录，并且同一个ip的ssh登录失败和成功的记录交叉出现。

初步判定这是一起非入侵导致的应急事件，但是该如何定位k8s容器出现异常ssh登录的原因呢？

文章目录

[ ]

* [定位异常记录最早出现时间](#%E5%AE%9A%E4%BD%8D%E5%BC%82%E5%B8%B8%E8%AE%B0%E5%BD%95%E6%9C%80%E6%97%A9%E5%87%BA%E7%8E%B0%E6%97%B6%E9%97%B4 "定位异常记录最早出现时间")
* [查找对应时间新创建的容器和文件变动](#%E6%9F%A5%E6%89%BE%E5%AF%B9%E5%BA%94%E6%97%B6%E9%97%B4%E6%96%B0%E5%88%9B%E5%BB%BA%E7%9A%84%E5%AE%B9%E5%99%A8%E5%92%8C%E6%96%87%E4%BB%B6%E5%8F%98%E5%8A%A8 "查找对应时间新创建的容器和文件变动")
* [auditd审计网络请求和命令](#auditd%E5%AE%A1%E8%AE%A1%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82%E5%92%8C%E5%91%BD%E4%BB%A4 "auditd审计网络请求和命令")

## 定位异常记录最早出现时间

![](https://zgao.top/wp-content/uploads/2023/05/iShot_2023-05-11_11.29.32-1024x571.png)

通过查询日志找到最早的异常ip的ssh登录失败的记录，定位到第一次出现时间为3月29日0点。对应的ip是一台k8s集群的node节点，上面运行全部的是容器服务。因此排查的方向从 主机 –> 容器 。

## 查找对应时间新创建的容器和文件变动

查找3月29号k8s主机上的文件变动。

```
find / -newermt "2023-03-28" ! -newermt "2023-03-30" -type f -exec ls -lh {} \;
```

![](https://zgao.top/wp-content/uploads/2023/05/image-10-1024x384.png)

可以看到确实是有文件变动，很有可能是在3月29号这天，新起的容器服务导致ssh登录异常。查找3月29号创建的容器。

```
 docker ps -a --no-trunc -q | xargs docker inspect --format '{{ .Name }}: Created {{ .Created }}' | grep "2023-03"
```

![](https://zgao.top/wp-content/uploads/2023/05/image-11-1024x233.png)

需要注意，docker的时间通常是utc时间转换cst时间还需要+8小时。

这里与猜测不符，所以并非是在3月29号附近的新创建的容器导致的异常。

## auditd审计网络请求和命令

![](https://zgao.top/wp-content/uploads/2023/05/image-6-1024x315.png)

k8s的容器数量众多，一台主机运行几百个容器，逐个排查效率太低。既然确定异常ssh的登录记录在每天凌晨会固定出现。所以直接开启auditd进行网络请求和命令的审计。命令如下：

```
auditctl -a always,exit -F arch=b64 -S connect,execve -F key=MYCONNECT
```

然后就是等第二天收审计的结果。

![](https://zgao.top/wp-content/uploads/2023/05/image-7-1024x633.png)

但正常情况下，audit必定能抓取到网络请求的进程，但是在audit审计的日志中未能发现在0点-4点之间异常的ssh网络请求信息。

因此，推测在0点前必定有容器异常退出或者容器服务挂掉了。

![](https://zgao.top/wp-content/uploads/2023/05/image-8-1024x267.png)

查看所有退出的容器，从异常退出的容器信息可推断只有k8s\_ocloud-osppro-remote-executor\_ocloud-osppro-remote-executor 容器符合时间要求。

从容器的命令可判断是一台远程执行命令的容器，重新启动该容器并进入查看容器的日志信息。

![](https://zgao.top/wp-content/uploads/2023/05/image-9-1024x730.png)

进入该容器查找服务器日志，发现下发命令的时间与ssh报错的时间和次数完全一致，确实是该容器的服务下发命令导致ssh登录异常。

Post Views: 1,004

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-k8s%E5%BC%82%E5%B8%B8ssh%E7%99%BB%E5%BD%95%E6%8E%92%E6%9F%A5/#respond)

Δ

版权©2020 Author By : Zgao