---
title: 白嫖？知识共享星球
url: https://zgao.top/%e7%99%bd%e5%ab%96%ef%bc%9f%e7%9f%a5%e8%af%86%e5%85%b1%e4%ba%ab%e6%98%9f%e7%90%83/
source: Zgao's blog
date: 2022-12-07
fetch_date: 2025-10-04T00:38:52.479583
---

# 白嫖？知识共享星球

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 白嫖？知识共享星球

* [首页](https://zgao.top)
* [白嫖？知识共享星球](https://zgao.top:443/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/)

[12月 6, 2022](https://zgao.top/2022/12/)

### 白嫖？知识共享星球

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/)

> 很早之前想过知识星球割韭菜的问题？

想了想🤔可以用Nginx反向代理做一个*`知识共享星球`*，其中涉及到很多Nginx配置操作，自然也踩了很多坑。可以当做快速熟悉掌握Nginx配置和制作docker镜像的小项目练手。

项目地址：<https://github.com/zgao264/zsxq-share>

![](https://zgao.top/wp-content/uploads/2022/12/image-13-1024x639.png)

**本项目为业余练习Nginx配置的demo，请勿用于非法途径！！！**

通过Nginx反向代理的方式访问自己账号下的星球👊

文章目录

[ ]

* [docker pull 一键搭建](#docker_pull_%E4%B8%80%E9%94%AE%E6%90%AD%E5%BB%BA "docker pull 一键搭建")
* [docker build 本地搭建](#docker_build_%E6%9C%AC%E5%9C%B0%E6%90%AD%E5%BB%BA "docker build 本地搭建")
  + [默认用户密码为zsxq/zsxq](#%E9%BB%98%E8%AE%A4%E7%94%A8%E6%88%B7%E5%AF%86%E7%A0%81%E4%B8%BAzsxqzsxq "默认用户密码为zsxq/zsxq")
  + [修改默认密码](#%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E5%AF%86%E7%A0%81 "修改默认密码")
  + [如何获取获取知识星球token](#%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96%E8%8E%B7%E5%8F%96%E7%9F%A5%E8%AF%86%E6%98%9F%E7%90%83token "如何获取获取知识星球token")

## docker pull 一键搭建

```
docker run  --name zsxq -d -e YOUR_ACCESS_TOKEN="xxxxx" -e YOUR_IP_OR_DOMAIN="xx.xx.xx.xx:9090" -p 9090:80 zgao/zsxq
```

## docker build 本地搭建

```
git clone https://github.com/zgao264/zsxq-share.git
cd zsxq-share/
docker build -t zsxq .
docker run --name zsxq -d -e YOUR_ACCESS_TOKEN="xxxxx" -e YOUR_IP_OR_DOMAIN="xx.xx.xx.xx:9090" -p 9090:80 zsxq
```

YOUR\_ACCESS\_TOKEN 填你的星球token YOUR\_IP\_OR\_DOMAIN 填vps的域名或者ip，默认映射端口为9090

### 默认用户密码为zsxq/zsxq

### 修改默认密码

按照下面的命令自行修改

```
docker exec zsxq echo 用户名:"$(openssl passwd 密码)" >./htpasswd.txt
```

### 如何获取获取知识星球token

f12打开浏览器控制台

![](https://zgao.top/wp-content/uploads/2022/12/image-14-1024x400.png)

本项目涉及到的知识点都写到了下面这篇文章中。

> [Nginx 反向代理问题汇总](https://zgao.top/nginx-%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB/)

Post Views: 5,959

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 6条评论

###### 匿名 发布于8:45 下午 - 9月 9, 2024

项目隐藏了吗大佬

[回复](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/?replytocom=8802#respond)

###### Zgao 发布于2:31 下午 - 9月 10, 2024

是的

[回复](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/?replytocom=8803#respond)

###### 匿名 发布于9:13 下午 - 12月 1, 2023

能请教一下IP地址填什么吗？我是一个小白

[回复](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/?replytocom=6647#respond)

###### 匿名 发布于11:06 上午 - 12月 5, 2023

就是你vps的公网ip

[回复](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/?replytocom=6656#respond)

###### 匿名 发布于9:19 下午 - 12月 5, 2023

感谢指导，部署成功了，只是发现有些地方点不了，比如右侧的星球优质专栏和别人的头像等，请问这是我部署的问题吗

[回复](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/?replytocom=6658#respond)

###### Zgao 发布于2:43 下午 - 12月 12, 2023

我在Nginx配置文件中限制了接口的请求，可以自行修改重新build

[回复](https://zgao.top/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/?replytocom=6927#respond)

### 发表评论 [取消回复](/%E7%99%BD%E5%AB%96%EF%BC%9F%E7%9F%A5%E8%AF%86%E5%85%B1%E4%BA%AB%E6%98%9F%E7%90%83/#respond)

Δ

版权©2020 Author By : Zgao