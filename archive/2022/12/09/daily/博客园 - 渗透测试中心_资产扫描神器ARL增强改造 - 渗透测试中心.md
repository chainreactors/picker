---
title: 资产扫描神器ARL增强改造 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16965445.html
source: 博客园 - 渗透测试中心
date: 2022-12-09
fetch_date: 2025-10-04T01:00:29.521386
---

# 资产扫描神器ARL增强改造 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [资产扫描神器ARL增强改造](https://www.cnblogs.com/backlion/p/16965445.html "发布于 2022-12-08 10:39")

### 拉取项目

首先从GitHub克隆到服务器上。

```
git clone https://github.com/ki9mu/ARL-plus-docker/
```

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103841848-669109384.png)

### 修改配置文件

因为ARL在配置文件里设置了黑名单，有时候项目为GOV或者EDU之类的时候无法进行扫描，所以在这里修改一下配置文件就可以解除限制。

```
cd ARL-plus-docker/
vi config-docker.yaml
```

在这里删掉黑名单里的几项就可以了

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103842639-2052392126.png)

修改后：

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103844180-274899402.png)

增加和修改riskiq以及fofa API

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103845056-23542144.png)

再增强版里添加了Oneforall的模块，所以在配置文件里需要打开，因为clone下来的代码里默认是Flase，这里将需要想打开的开关替换为Ttue即可。

```
vi oneforall-config/setting.py
```

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103845731-350217365.png)

修改后：

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103846441-1358167599.png)

修改为配置文件之后就开始启动docker，先添加一个volume，然后docker-compose up -d就可以直接启动，拉取镜像的时候如果很慢可以换一下docker源。

```
docker volume create --name=arl_db
docker-compose up -d
```

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103847142-1298185442.png)

当看到一排done就说明成功了，这时候还需要进容器修改一下python代码，因为在python脚本里也有黑名单。先使用docker ps看一下容器的ID，然后进入这个容器进行修改，使用vi进行编辑。

```
docker ps #查看容器ID
docker exec -it 对应ID bash
vi app/config.py
```

修改前：

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103847909-1022097218.png)

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103848601-1432151023.png)

### 添加指纹

安装成功之后，添加一下指纹，让你的灯塔有更强大的指纹。

地址：[https://vps:5003/![file](http://www.a10ng.top/wp-content/uploads/2022/09/2022090213085544.png](https://vps:5003/%21%5Bfile%5D%28http%3A//www.a10ng.top/wp-content/uploads/2022/09/2022090213085544.png))
默认账密：admin\arlpass

```
git clone https://github.com/loecho-sec/ARL-Finger-ADD
cd ARL-Finger-ADD
python ARL-Finger-ADD.py -O https://vps:5003/  admin arlpassCOPY
```

![file](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221208103849431-733071526.png)

### 安装成功

用默认密码登陆，然后在右上角修改掉默认密码就可以愉快的使用了。

posted @
2022-12-08 10:39
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(3210)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025