---
title: 空 - 三眼乌鸦 - zha0gongz1
url: https://www.cnblogs.com/zha0gongz1/p/17400520.html
source: 博客园 - zha0gongz1
date: 2023-06-25
fetch_date: 2025-10-04T11:44:15.102557
---

# 空 - 三眼乌鸦 - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [空 - 三眼乌鸦](https://www.cnblogs.com/zha0gongz1/p/17400520.html "发布于 2023-06-25 00:44")

一款纯净版内网探测工具，解决某些工具内网探测速率慢、服务爆破误报率高以及socks流量代理出问题且工具落地又被秒的困扰

## Three-EyedRaven

内网渗透初期，我们都希望可以豪无遗漏的尽最大可能打开目标内网攻击面，故，设计该工具的初衷是解决某些工具内网探测速率慢、运行卡死、服务爆破误报率高以及socks流量代理扫描出问题且工具落地被秒的困扰。另外，求人不如求诸己。

该工具内置`Top1000`端口探测同时也支持自定义端口探测，支持最新`nmap_service_probes`规则进行服务指纹识别，支持对`SSH/SMB/Mysql/SqlServer/WinRM/Redis/MongoDB`等服务进行密码喷洒式爆破、支持`Netbios`主机名识别及多网卡探测。运行时不需要指定输出文档，默认扫描结果输出至工具同级目录下`z.log`文件中，报错日志在`z_e.log`文件。
![](https://img2023.cnblogs.com/blog/1449167/202306/1449167-20230624112308845-120818110.png)

## 使用方法

[工具地址](https://github.com/zha0gongz1/Three-EyedRaven)，以下是使用命令示例：

```
Three-EyedRaven all -h         #all模块帮助文档
Three-EyedRaven detect -h      #detect模块帮助文档
Three-EyedRaven brute -h       #brute模块帮助文档

#默认400线程进行all模块探测，，禁用爆破模块及web探测（包括401爆破）
Three-EyedRaven all -H 192.168.0.1/24 --nw --nb

#探测C段主机存活，内置1000端口探测，并对结果中存在的可爆破服务进行暴力枚举（内置字典）
Three-EyedRaven all -H 192.168.0.1/24

#默认线程探测B段主机，内置端口字典探测并进行服务指纹识别，web title及401基础认证爆破（B段扫描建议指定个别端口）
Three-EyedRaven detect -H 192.168.0.1/16

#探测C段存活主机及135-139、445、8000-9000端口的开放情况
Three-EyedRaven detect -H 192.168.0.1/24 -P 135-139,445,8000-9000

# 设定80,445端口进行noping探测B段
Three-EyedRaven detect -H 192.168.233.1/16 -P 80,445 --np

#采用内置ssh用户名密码字典爆破B段主机中所有22端口SSH服务
Three-EyedRaven brute -H 192.168.0.1/16 -S ssh -P 22

#同上，若不指定端口，则先进行服务识别再爆破（较慢）
Three-EyedRaven brute -H 192.168.0.1/24 -S ssh

 #采用内置redis用户名密码字典爆破C段中所有redis服务，默认200线程6379端口
Three-EyedRaven brute -H 192.168.0.1/24 -S redis

#设定50线程使用pass.txt字典爆破主机192.168.0.11的ftp服务端口2121
Three-EyedRaven brute -H 192.168.0.11 -S ftp -P 2121 -t 50 -p pass.txt
```

## ToDo

1. 鉴于微软RDP认证协议过多，该服务的认证爆破正在研发阶段
   ~~2. 当目标管理员更改服务的默认端口时，该工具目前仅支持ssh、ftp协议的服务识别，其他服务的识别方法正在研发阶段~~

**闲言碎语：** 年前写好的部分功能代码，但一直没有组装成模块化工具发布，原本想增加exploit利用模块，但那不就跟某些扫描工具功能撞车了？倘若用到exp模块，我的建议是kill杀软上Ladon或fscan。所以，仅把内网渗透的铺垫工作做到极致也是极好的，该工具的定位是隐蔽且最大化限度掌握目标内网情况，欢迎各位大佬提供实战问题bug情况及合理改进意见。

**致谢：**
[K8gege](http://k8gege.org/)
[ServerScan](https://github.com/Adminisme/ServerScan)

朋友可以背叛你，但技术和身材不会

posted @
2023-06-25 00:44
[zha0gongz1](https://www.cnblogs.com/zha0gongz1)
阅读(645)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025