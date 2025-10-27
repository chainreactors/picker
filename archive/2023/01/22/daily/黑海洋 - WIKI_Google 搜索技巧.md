---
title: Google 搜索技巧
url: https://blog.upx8.com/3198
source: 黑海洋 - WIKI
date: 2023-01-22
fetch_date: 2025-10-04T04:33:36.923534
---

# Google 搜索技巧

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Google 搜索技巧

发布时间:
2023-01-22

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
15782

# 前言

我们获取资源的方式通常是通过搜索引擎来获得，但是搜索引擎对于不会使用一些技巧的人来说，搜索出来的内容和自己预期的不符，往往需要话大量的时间来搜索才能找到需要的内容，今天我们来看看有哪些技巧或者是语法帮我们快速找到需要的资源！以下语法是来源于Google Hacking，我只在Google上使用过，其他搜索引擎不保证有效果！！！

# 基础

* ## 并且【AND】

> AND的意思的“和”的意思，那么我们在搜索的时候就可以在AND的前后加上我们想要搜索的内容，满足两个条件的内容将显示出来。
>
> 语法【**AND的前后要有空格】**：xxx AND xxx

* ## 或者【OR】

> OR的话和AND就恰恰相反了，只要满足其中一个条件的内容就能展示出来。
>
> 语法【**OR的前后要有空格】**：xxx OR xxx

* ## 精确匹配【”关键字”】

>  将需要的关键字用英文的双引号括起来，这样就能保证搜索出来的结果必定包含该关键字。
>
> 语法【**注意是英文的双引号**】：”xxx”

* ## 过滤【-】

> 减号【-】：这个在我们搜索的时候比如不想看某个平台的文章就可以派上用场了。
>
> 语法【**注意减号前面必须加上空格**】： -xxx

* ## 包含【+】

> 加号【+】：和减号相反，如果我们只想看某个平台的文章就使用加号。
>
> 语法【**注意加号前面必须加上空格**】： +xxx

* ## 模糊匹配单个字符【?】

> 问号【?】：这个可以帮助我们匹配单个字，比如我们只记得某明星的两个字，还有一个字忘记了，这个时候就可以用?代替。
>
> 语法【**注意是英文状态的问号**】：?你太美

* ## 模糊匹配多个字符【\*】

> 星号【*】：这个可以匹配多个字符，比如一首歌的歌词你可能只记得前后，中间部分忘记了，那么这个时候你就可以使用*来代替中间忘记的那部分。
>
> 语法：x\*x

* ## 范围【..】

> 可以搜索某些数值的范围，例如某个时间段等等。
>
> 语法：x..x

![](https://img-blog.csdnimg.cn/115e5b83e5e2493bb092132b57cda76b.png "null")

# 进阶

* ## 标题包含【intitle:】

> 这个可以帮助我们找到网页标题包含的内容，可以看下图片指出的位置，你就知道对应的是哪个位置了。
>
> 语法【**注意intitle后面的冒号是英文状态的**】：intitle:xxxx

![](https://img-blog.csdnimg.cn/ad3d59ab69c5475490deddf52176f230.png "null")

* ## 内容包含【intext:】

> 上面介绍的intitle搜索出来的是网页标题包含关键字的内容，那么intext搜索的就是网页里面包含的内容了，文章都会有标题和内容，这两个关键字的作用也不一样。
>
> 语法【**注意intext后面的冒号是英文状态的**】：intext:xxx

* ## 指定网站【site:】

> site使用来指定某个网站的，当然你也可以用这个关键字来看下搜索引擎有没有将你自己的网站收录进去，用法请看下图！
>
> 语法【**注意site后面的冒号是英文状态的**】：site:域名

![](https://img-blog.csdnimg.cn/a387f4d26897469794ebd9a9fe49e6a6.png "null")

* ## 网站目录【index of /】

> 有些网站可能没有配置目录的访问限制，通过这个关键字可以试着帮我们找到网站允许访问的目录。如图：

![](https://img-blog.csdnimg.cn/ca5775e5f76b4870bffb16680ae60698.png "null")

![](https://img-blog.csdnimg.cn/f1bdae8c64e84a188da040bd85b9def3.png "null")

* ## 指定路径【inurl:】

> 域名之后跟着的就是一些页面的访问路径，我们可以通过该语法快速找到网站的后台管理页面。如图：

![](https://img-blog.csdnimg.cn/6f0297daf31b4722a19231035dce2d16.png "null")

![](https://img-blog.csdnimg.cn/64631cbdc7194c2d86cc6624648ab4c1.png "null")

* ## 文件类型【filetype:】

> 指定文件的类型，比如我可能需要找一些作文，需要word文件，这个时候就可以派上用场了。用法看图：

![](https://img-blog.csdnimg.cn/2d30520b47be44e5b4093613f69ff297.png "null")

* ## 相似网站【similar to】

> 有时候我们可能需要找相似的网站，这个语法就能派上用场了，不过这个未必是百分比能找到，看机缘了！用法如下：

![](https://img-blog.csdnimg.cn/d234b1d5b4614d048724d09d9a495fc4.png "null")

* ## 相似软件【alternative to】

>  该语法可以查找软件的替代品，比如我想找一个Photoshop相似的软件，可以这么查找：

![](https://img-blog.csdnimg.cn/955e17ce30dd47dbbf2607998ee7b3d9.png "null")

* ## 查找外链【link:】

> 这个不是很常用，这个可以用来查找哪些网站引用了你指定的网址。当然这个也未必找得到，随缘~

![](https://img-blog.csdnimg.cn/dc12db93b50d45dd9906fe025972537b.png "null")

>  上面的这些语法不是每次都能记住，我也老是忘记，然后我就写了一个油猴脚本，方便使用，感兴趣的小伙伴可以往下看！

* ## 词的意思【define】

> 这个可以查某个词的意思，比如我不知道”人”是什么意思，可以这么搜索：

![](https://img-blog.csdnimg.cn/d0e08755146a460582287e53781f3ffd.png "null")

* ## 查询天气【weather:】

> 加上城市名即可查看城市天气，语法如下：
>
> weather:城市名

* ## 电影信息【movie:】

> 通过电影名查找相关信息，中文不保证能搜到，语法如下：
>
>  movie:电影名

* ## 查询股票【stocks:】

>  通过股票名查找相关信息，语法如下：
>
> stocks:股票名

* ## 搜种子【torrent:】

> 比如想搜索`奇异博士`种子，输入`奇异博士:torrent`即可。

# 脚本

> 脚本目前只支持谷歌引擎，也是比较简单的，后续我再翻新一下，脚本效果如下图：

![](https://img-blog.csdnimg.cn/b113274d486746bca350ab9ec31789a9.png "null")

比较简陋，但方便是真的方便，不用再记那些语法了！脚本我已经发布到油猴插件的greasyfork平台上了；

## 安装

\*\*目前脚本只支持Google搜索！！！ \*\*

使用前需要安装tampermonkey油猴插件，安装的教程很多，可以自己去找下教程，这里就不提供了，安装好油猴插件之后**点击下面的链接****或者****进入greasyfork搜索GoogleEasySearch**就可以下载使用了！

脚本地址：[用户脚本](https://blog.upx8.com/go/aHR0cHM6Ly9ncmVhc3lmb3JrLm9yZy96aC1DTi9zY3JpcHRzP3E9R29vZ2xlRWFzeVNlYXJjaA "用户脚本")

![](https://img-blog.csdnimg.cn/b7dcd7999af240d7bb0217e6b4a8592a.png "null")

[取消回复](https://blog.upx8.com/3198#respond-post-3198)

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