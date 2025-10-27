---
title: AirFly-机场订阅链接一键生成ip代理池工具
url: https://zgao.top/airfly-%e6%9c%ba%e5%9c%ba%e8%ae%a2%e9%98%85%e9%93%be%e6%8e%a5%e4%b8%80%e9%94%ae%e7%94%9f%e6%88%90ip%e4%bb%a3%e7%90%86%e6%b1%a0%e5%b7%a5%e5%85%b7/
source: Zgao's blog
date: 2023-08-01
fetch_date: 2025-10-06T16:58:47.020686
---

# AirFly-机场订阅链接一键生成ip代理池工具

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# AirFly-机场订阅链接一键生成ip代理池工具

* [首页](https://zgao.top)
* [AirFly-机场订阅链接一键生成ip代理池工具](https://zgao.top:443/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/)

[7月 31, 2023](https://zgao.top/2023/07/)

### AirFly-机场订阅链接一键生成ip代理池工具

作者 [Zgao](https://zgao.top/author/zgao/)
在[[经验分享](https://zgao.top/category/%E7%BB%8F%E9%AA%8C%E5%88%86%E4%BA%AB/)](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/)

![](https://zgao.top/wp-content/uploads/2023/07/image-8-1024x460.png)

很早之前的一个想法，写一个工具支持各种主流的科学上网协议，通过指定订阅链接的就可以实现自动轮询代理ip，很适合爬虫，渗透，攻防的场景。

最近趁工作之余把这个工具写完了，我取名为 AirFLy（Air[port] Fly），意思是 让机场✈️起飞！

文章目录

[ ]

* [项目链接](#%E9%A1%B9%E7%9B%AE%E9%93%BE%E6%8E%A5 "项目链接")
* [工具参数](#%E5%B7%A5%E5%85%B7%E5%8F%82%E6%95%B0 "工具参数")
* [测试代理ip](#%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%90%86ip "测试代理ip")

## 项目链接

<https://github.com/zgao264/AirFly>

## 工具参数

![](https://zgao.top/wp-content/uploads/2023/08/image-17-705x1024.png)

工具的使用非常简单，指定两个参数即可。

* -l 本地监听的端口，支持三种协议（http、socks5、mixed），mixed是指http和socks5共用一个端口。
* -u 机场的订阅链接 ，可以同时指定多个机场订阅链接。

![](https://zgao.top/wp-content/uploads/2023/07/image-9-1024x717.png)

## 测试代理ip

以curl为例：

```
curl -sx "http://127.0.0.1:6666" https://ip.tool.lu
```

连续请求测试：

```
seq 1 10 | xargs curl -sx "http://127.0.0.1:6666" https://ip.tool.lu
```

Post Views: 5,132

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 10条评论

###### uujiang 发布于5:26 下午 - 1月 20, 2025

项目链接打不开呢

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=9246#respond)

###### ztb 发布于12:24 下午 - 11月 9, 2023

运行 airfly 最后几个节点显示 ”连接失败，错误“ 猜测似乎是又变回了原本的ip？ 感谢

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=6187#respond)

###### ztb 发布于12:02 下午 - 11月 9, 2023

curl -sx “http://127.0.0.1:6666” <https://ip.tool.lu> 这个命令没回显， curl ip.sb 也没有变 开放了6666端口，清除了dns缓存， 梯子也关了，请问还有啥原因导致失败了，感谢。

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=6186#respond)

###### 匿名 发布于5:09 下午 - 10月 18, 2023

小白 表示用不来。。cmd。bat打开一闪而过

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=6089#respond)

###### 匿名 发布于5:22 下午 - 10月 18, 2023

这个是命令行工具，没有gui界面。。

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=6091#respond)

###### 匿名 发布于7:07 下午 - 9月 25, 2023

win11下闪退 打不开

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=5993#respond)

###### 唔璇 发布于11:22 上午 - 9月 2, 2023

很实用

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=5876#respond)

###### 匿名 发布于1:22 下午 - 8月 28, 2023

请问会公布源码吗？

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=5858#respond)

###### 卑微小王 发布于4:17 下午 - 8月 3, 2023

确实很实用

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=5707#respond)

###### AllinProgram 发布于11:43 下午 - 8月 7, 2023

Awesome，这个原来可以做到这么方便

[回复](https://zgao.top/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/?replytocom=5737#respond)

### 发表评论 [取消回复](/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/#respond)

Δ

版权©2020 Author By : Zgao