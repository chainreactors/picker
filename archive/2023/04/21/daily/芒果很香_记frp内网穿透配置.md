---
title: 记frp内网穿透配置
url: https://blog.csdn.net/laczff21/article/details/130266717
source: 芒果很香
date: 2023-04-21
fetch_date: 2025-10-04T11:33:38.279078
---

# 记frp内网穿透配置

# 记frp内网穿透配置

原创
已于 2023-04-20 17:26:03 修改
·
3.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

1

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

2
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#frp](https://so.csdn.net/so/search/s.do?q=frp&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#内网穿透](https://so.csdn.net/so/search/s.do?q=%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2023-04-20 17:13:49 首次发布

这两天由于想给客户看一下我们的系统，于是想到用内网穿透，但是怎么办呢，没有用过呀，于是各处找资料，但是搞完以后已经不记得参考了那些文档了，对不起各位大神，就只能写出过程和要被自己蠢死的错误了，以免下次再犯。

首先要准备两台电脑，一台是有公网IP的服务器，一台是发布系统的电脑。一开始看到别人的帖子上写要用公网IP的服务器的时候，作为小白的我理解为了是必须要发布系统的电脑在内网就能访问到的具有公网IP的服务器，后来才明白原来只要是一台有公网IP的服务器即可，各种云服务器都是可以的。作为一个小白也太难了。

其次，下载frp的安装文件，根据自己的系统选择对应的包就可以了，一个包里面包含了服务器端和客户端的程序，下载地址：[https://github.com/fatedier/frp/releases](https://github.com/fatedier/frp/releases "https://github.com/fatedier/frp/releases")

我的公网IP服务器为阿里云的windows系统，内网电脑为centos7的系统，所以对应下载了windows和linux两个版本，正式开始配置

### 第一步：配置公网服务器

把压缩包解压以后，Windows安全中心就提示发现木马，直接就给隔离了，我还心想怎么刚解压完exe就不见了。放心，不是木马，我们给他加入白名单。

#### 开始配置frps.ini

这里frps开头的是服务器程序相关的，frpc开头的是客户端相关的，建议把客户端开头的删掉，以免误操作。

最简单的配置，打开frps.ini，里面默认是这样子的，不用修改可直接使用。

 [common]
 bind\_port = 7000

 从文件夹窗口启动命令行程序（就把光标定位到文件夹路径那一栏，输入cmd，后回车）

![](https://i-blog.csdnimg.cn/blog_migrate/395b671e76d6bad845e8e62e52648b6a.png)

#### 启动frp服务器端

然后输入frps.exe，然而这是我犯的第一个错误，导致后面token验证一直失败，启动命令应该为：

frps.exe -c frps.ini

这个命令才会去调用当前文件夹下的frps.ini中的配置，否则配置就白配了，也是导致我这个小白后来因为这个查找了好久token失败的原因

会出现如下界面，就说明服务器端启动成功了

![](https://i-blog.csdnimg.cn/blog_migrate/1e958e51f4e9f9362cf26133b069bc92.png)

#### 开放监控端口

我用的是阿里云的服务器，所以需要登录阿里云安全管理页面，对端口进行开放，由于阿里云服务器我没有管理，是同事配置的，这里就没有描述了。

### 第二步：配置内网电脑

#### 解压缩文件包

命令：

解压缩：tar -xzvf frp\_0.48.0\_linux\_amd64.tar.gz

移动文件到安装目录：mv frp\_0.48.0\_linux\_amd64 /usr/local/frps

移动到安装目录：cd /usr/local/frps

![](https://i-blog.csdnimg.cn/blog_migrate/1382c9ce85359c9e38e36968b652bf24.png)

#### 编辑配置文件

vim frpc.ini       这个时候注意了不要写错了，毕竟frpc和frps只差一个字

![](https://i-blog.csdnimg.cn/blog_migrate/dab225ef55655d69c6b66b7d3172bb5e.png)

![](https://i-blog.csdnimg.cn/blog_migrate/2a34cbb0833baad7212a2a25df617e47.png)

其中 server\_addr写入公网IP

[ssh]可以是你自己的项目名称

local\_port为本地端口

remote\_port为服务器的端口

如果有多个端口要穿透，则写多个配置即可

![](https://i-blog.csdnimg.cn/blog_migrate/9b98d51a6ca63929becf2d88f01ee68f.png)

#### 启动客户端

命令：./frpc -c ./frpc.ini

也可以使用 nohup  ./frpc -c ./frpc.ini ，但是这个命令为后台运行，配置完第一次不建议采用这种方式启动，因为后台启动不会把错误显示在终端，出现问题也不知道，我因为后台启动后连接不上也找了好久原因。出现下图这样的信息就表示已经成功了。

![](https://i-blog.csdnimg.cn/blog_migrate/6ddcf8db5944c79aace83dc12f570464.png)

### 配置token

一开始的时候我计划加上token，服务器的配置文件为

![](https://i-blog.csdnimg.cn/blog_migrate/59ef11934b853007bea14471f5e967ce.png)

客户端的配置文件为：

![](https://i-blog.csdnimg.cn/blog_migrate/1fe43e71b827e641ac9604d1cde955a7.png)

但是一直提示：token in login doesn't match token from configuration

![](https://i-blog.csdnimg.cn/blog_migrate/a3524e990c51973a90f4cbf2029b6e87.png)

 找了各种资料以后，才发现是因为我服务器端启动时直接调用了frps.exe，用的是默认配置，并没有调用到我写的frps.ini，把命令改成frps.exe -c frps.ini 就可以连接成功了。

### centos后台进程查看和杀死

由于我一开始是nohup运行的，要杀死该进程，于是查找了如下命令

查找进程：ps -e | grep  应用名称

根据端口查找进程： lsof -i:端口号    或者 netstat -ntulp | grep 端口号

杀死进程： kill -9 PID

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/default.jpg!1)

芒果很香](https://blog.csdn.net/laczff21)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  1

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  2

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

[*frp**内网穿透**token*不匹配错误排查全过程 *frp* *内网穿透*、*frp*s、*frp*c、*token* *in* *login* doesn’t *match*、*配置*文件冲突](https://blog.csdn.net/weixin_41961749/article/details/151045805)

[代码简单说 Vue、JAVA、PHP、Node.js 熟练运用，接口、架构、性能全搞定。](https://blog.csdn.net/weixin_41961749)

08-31
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
112

[不要急着改来改去，很可能是因为你用错了*配置*文件。特别是在 L*in*ux 环境下，如果你是通过systemctl或者自启动方式运行的 *frp*s，很可能默认读取的是，而不是你解压目录下的那个*frp*s.*in*i。先通过看一下*frp*s 到底加载的是哪个*配置*文件；确认 *token* 保持一致；再重启服务。这样一来，*token* 报错问题基本都能解决。](https://blog.csdn.net/weixin_41961749/article/details/151045805)

[*Frp**内网穿透*的*配置*与启动-l*in*ux、w*in*dows、Mac](https://blog.csdn.net/hahofe/article/details/117285911)

[韩麸子的博客](https://blog.csdn.net/hahofe)

05-26
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1万+

[目录
一、客户端下载
二、*配置**frp*s.*in*i和*frp*c.*in*i文件(最重要)
一、连接内网w*in*dows远程桌面
二、其他需求
三、启动
四、其他
一、客户端下载
https*:*//github.com/fatedier/*frp*/releases
常用的64位安装包如上图，下载，解压后，得到如下文件（w*in*dows示例）。其中 *frp*s 为服务端，*frp*c为客户端。*frp*s\_full.*in*i为全量*配置*信息，可以自己阅读后，挑选需要的*配置*信息，写入*frp*s.*in*i即可完成*配置*。
.](https://blog.csdn.net/hahofe/article/details/117285911)

参与评论
您还未登录，请先
登录
后发表或查看评论

[*frp*流量代理时*token*的报错问题](https://devpress.csdn.net/v1/article/detail/123536166)

[qq\_15042405的博客](https://blog.csdn.net/qq_15042405)

03-16
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
4065

[2022/03/16 13*:*50*:*31 [E] [service.go*:*316] *token* *in* *login* doesn’t *match* *token* *from* *configuratio*n
2022/03/16 13*:*50*:*31 [W] [service.go*:*105] *login* to server failed*:* *token* *in* *login* doesn’t *match* *token* *from* *configuratio*n
这几天研究cs上传*frp*打域控，结果一直报错。总结了一些解决方法：
1、*token*位](https://devpress.csdn.net/v1/article/detail/123536166)

[*frp* *内网穿透*, 认证*配置*,安全*配置* *TOKEN*](https://devpress.csdn.net/v1/article/detail/122034137)

[BIG.KE的博客](https://blog.csdn.net/weixin_42209307)

12-20
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1万+

[*frp*s *frp*s.*in*i 服务器端*配置*
[common]
b*in*d\_port = 7000
vhost\_http\_port = 17000
dashboard\_port = 17500
dashboard\_user = adm*in* # 控制台用户名
dashboard\_pwd = xxxxxx # 控制台密码
# auth
authentication\_method = *token* # 认证方式, *token*
authenticate\_new\_work\_conns = true #.](https://devpress.csdn.net/v1/article/detail/122034137)

[*frp*c客户端*配置*](https://devpress.csdn.net/v1/article/detail/135767667)

[weixin\_49587492的博客](https://blog.csdn.net/weixin_49587492)

01-23
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3632

[在将*frp*c解压后，w*in*10电脑对*frp*c.exe会识别为存在风险，导致我们无法启动*frp*c，所以需要将*frp*c服务所在文件夹设置为安全，不需要进行检测。在*配置**frp*之前，请先确认需要*配置**frp*的电脑能被其他电脑远程桌面登入，其次最好先将你准备把*frp*解压的目录设置为排除项，排除向设置在第三步有说明。对*frp*c服务进行*配置*主要是，在计算机刚刚启动的时候，*frp*c服务可能启动失败，后续不在启动。*frp*c.*in*i*配置*是*frp*c非...