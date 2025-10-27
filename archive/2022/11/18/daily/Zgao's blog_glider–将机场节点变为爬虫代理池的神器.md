---
title: glider–将机场节点变为爬虫代理池的神器
url: https://zgao.top/glider-%e5%b0%86%e6%9c%ba%e5%9c%ba%e8%8a%82%e7%82%b9%e5%8f%98%e4%b8%ba%e7%88%ac%e8%99%ab%e4%bb%a3%e7%90%86%e6%b1%a0%e7%9a%84%e7%a5%9e%e5%99%a8/
source: Zgao's blog
date: 2022-11-18
fetch_date: 2025-10-03T23:05:59.226025
---

# glider–将机场节点变为爬虫代理池的神器

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# glider–将机场节点变为爬虫代理池的神器

* [首页](https://zgao.top)
* [glider–将机场节点变为爬虫代理池的神器](https://zgao.top:443/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/)

[11月 17, 2022](https://zgao.top/2022/11/)

### glider–将机场节点变为爬虫代理池的神器

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/)

> 手里有大量的机场节点，由于渗透、攻防、爬虫等需要，想要把这些机场的ip作为代理池使用。这时候就需要一个上游代理把这些机场节点汇总在一起。
>
> 大家可能遇到过这样一种场景

**glider** 完全满足这类场景，而且可以定期对ip进行健康检测，自动轮询等功能，可作为系统服务稳定运行。glider 对于 trojan、v2ray、ss、ssr这几类常见的机场协议都是支持的，同时还支持很多其他的协议。

![](https://zgao.top/wp-content/uploads/2022/11/image-3-1024x491.png)

可参考：<https://github.com/nadoo/glider#protocols>

| Protocol | Listen/TCP | Listen/UDP | Forward/TCP | Forward/UDP | Description |
| --- | --- | --- | --- | --- | --- |
| HTTP | √ |  | √ |  | client & server |
| SOCKS5 | √ | √ | √ | √ | client & server |
| SS | √ | √ | √ | √ | client & server |
| Trojan | √ | √ | √ | √ | client & server |
| VLESS | √ | √ | √ | √ | client & server |
| VMess |  |  | √ | √ | client only |
| SSR |  |  | √ |  | client only |

文章目录

[ ]

* [安装部署](#%E5%AE%89%E8%A3%85%E9%83%A8%E7%BD%B2 "安装部署")
* [配置机场订阅节点](#%E9%85%8D%E7%BD%AE%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E8%8A%82%E7%82%B9 "配置机场订阅节点")
* [screen 后台运行 glider](#screen_%E5%90%8E%E5%8F%B0%E8%BF%90%E8%A1%8C_glider "screen 后台运行 glider")
* [其他问题](#%E5%85%B6%E4%BB%96%E9%97%AE%E9%A2%98 "其他问题")
  + [vmess协议不识别？](#vmess%E5%8D%8F%E8%AE%AE%E4%B8%8D%E8%AF%86%E5%88%AB%EF%BC%9F "vmess协议不识别？")
  + [节点内容报错？](#%E8%8A%82%E7%82%B9%E5%86%85%E5%AE%B9%E6%8A%A5%E9%94%99%EF%BC%9F "节点内容报错？")
  + [限制公网访问](#%E9%99%90%E5%88%B6%E5%85%AC%E7%BD%91%E8%AE%BF%E9%97%AE "限制公网访问")

## 安装部署

<https://github.com/nadoo/glider/releases>

下载对应的版本进行安装。

```
wget https://github.com/nadoo/glider/releases/download/v0.16.0/glider_0.16.0_linux_amd64.tar.gz
tar xvf glider_0.16.0_linux_amd64.tar.gz
cd glider_0.16.0_linux_amd64/
cp config/examples/4.multiple_forwarders/glider.conf ./
cat glider.conf
```

## 配置机场订阅节点

我们通过glider提供的模板配置文件进行修改。

添加✈️机场订阅的节点。因为机场订阅内容通常是用base64编码过的，所以需要解码拿到原始的节点内容。

这里我用trojan的机场节点做演示。

```
curl -s http://你的机场订阅链接 | base64 -d | sed 's/^/forward=&/g'
```

![](https://zgao.top/wp-content/uploads/2022/11/image-1.png)

将上面的节点内容放在配置文件中。

```
# Verbose mode, print logs
verbose=True

listen=:8443

# 机场节点放在这里
forward=trojan://password@domain
forward=trojan://password@domain
forward=trojan://password@domain

# Round Robin mode: rr
# High Availability mode: ha
strategy=rr

# forwarder health check
check=http://www.msftconnecttest.com/connecttest.txt#expect=200

# check interval(seconds)
checkinterval=3000
```

修改配置文件后运行

```
./glider -config ./glider.conf
```

最终效果如下：

直接将机场订阅节点转换为了爬虫代理池，每次访问自动轮询ip。

![](https://zgao.top/wp-content/uploads/2022/11/image.png)

## screen 后台运行 glider

要作为爬虫代理池肯定是要将其作为系统服务稳定运行。这里用screen后台运行，当然也可以写成service，用systemctl调用。

```
[root@zgao glider_0.16.0_linux_amd64]#
screen -dmS glider ./glider -config ./glider.conf
screen -ls
screen -r glider
```

## 其他问题

### vmess协议不识别？

用v2ray的机场订阅发现报错，查看官方源码发现，glider还不支持常规的base64内容。

![](https://zgao.top/wp-content/uploads/2022/11/image-2-1024x571.png)

需要改写成这种形式，大家可以自行批量转换。

### 节点内容报错？

通常是节点中的密码带有特殊字符，glider支持还不是很完善，把报错的节点删除掉即可。

### 限制公网访问

将代理直接暴露在公网很容易被扫到，所以可以直接用iptables限制指定ip访问该端口。

```
iptables -I INPUT -p tcp --dport 8443 -j DROP
iptables -I INPUT -s 127.0.0.1 -p tcp --dport 8443 -j ACCEPT
iptables -I INPUT -s your_ip -p tcp --dport 8443 -j ACCEPT
```

Post Views: 8,450

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 6条评论

###### 匿名 发布于12:00 上午 - 11月 20, 2022

报错辣，FAILED. error: x509: certificate is not valid for any names, but wanted to match xxx.xxx.com

[回复](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/?replytocom=4270#respond)

###### 匿名 发布于3:00 下午 - 11月 20, 2022

服务器证书的问题

[回复](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/?replytocom=4272#respond)

###### 匿名 发布于6:18 下午 - 11月 20, 2022

大佬有解决方法吗，我在windows和wsl上试了也这样

[回复](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/?replytocom=4273#respond)

###### 匿名 发布于2:05 下午 - 3月 18, 2025

我也是这个问题。同问

[回复](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/?replytocom=9416#respond)

###### musl 发布于4:57 下午 - 11月 18, 2022

you should encode special characters in scheme url. e.g., @->%40
<https://www.w3schools.com/tags/ref_urlencode.asp>

[回复](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/?replytocom=4264#respond)

###### Jojo 发布于9:11 下午 - 11月 17, 2022

P站插件需要更新 NEED HELP！

[回复](https://zgao.top/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/?replytocom=4262#respond)

### 发表评论 [取消回复](/glider-%E5%B0%86%E6%9C%BA%E5%9C%BA%E8%8A%82%E7%82%B9%E5%8F%98%E4%B8%BA%E7%88%AC%E8%99%AB%E4%BB%A3%E7%90%86%E6%B1%A0%E7%9A%84%E7%A5%9E%E5%99%A8/#respond)

Δ

版权©2020 Author By : Zgao