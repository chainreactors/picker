---
title: 使用Nginx反向代理KKFileView遇到问题
url: https://blog.csdn.net/aomandeshangxiao/article/details/140095457
source: 傲慢的上校的专栏
date: 2024-07-02
fetch_date: 2025-10-06T17:41:45.758829
---

# 使用Nginx反向代理KKFileView遇到问题

# 使用Nginx反向代理KKFileView遇到问题

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[傲慢的上校](https://blog.csdn.net/aomandeshangxiao "傲慢的上校")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2024-07-01 12:00:46 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1w
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

7

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
10

CC 4.0 BY-SA版权

分类专栏：
[Java](https://blog.csdn.net/aomandeshangxiao/category_12305060.html)
文章标签：
[nginx](https://so.csdn.net/so/search/s.do?q=nginx&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-07-01 12:00:03 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/lilu_leo/article/details/140095457>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756923.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java
专栏收录该内容](https://blog.csdn.net/aomandeshangxiao/category_12305060.html "Java")

7 篇文章

订阅专栏

### 使用KKFileView 4.0 以上版本

在KKFileView官网上，关于使用Nginx代理，建议配置如下

![](https://i-blog.csdnimg.cn/blog_migrate/93bf5edc0d30cea12252285bfbb02fe1.png)

#### 一、修改Nacos

在Nginx的conf文件夹中修改 nginx.conf ,新加

![](https://i-blog.csdnimg.cn/blog_migrate/51954b72004878e34e73256674e185b3.png)

红框内的IP地址为代理服务器地址（即安装KKFileView的服务器地址）

#### 二、修改KKFileView

在KKFileView的config文件中中，修改application.properties文件

我使用的版本时4.2.1，发现 没有

```
server.context-path = /preview
```

正确的的配置方式是

![](https://i-blog.csdnimg.cn/blog_migrate/50f5073a16a51e313df326cb778ccc70.png)

##### 测试界面

配置完成，保存成功后，启动KKFileView，在打开测试界面时，请注意 `配置nginx后,本机ip:8012端口的方式无法在访问根页面,需使用nginx代理ip:8012/preview的方式访问`

![](https://i-blog.csdnimg.cn/blog_migrate/c8909ca3213d166d54e94f15b9d7d61d.png)

### 跨域访问问题

如果遇到跨域访问问题（Strict-origin-when-cross-origin）

![](https://i-blog.csdnimg.cn/blog_migrate/573a44ca6a37f581c3bcbc3fda0daf85.png)

可能时网络访问关系没有开，也可以在Nginx中加上相关配置

![](https://i-blog.csdnimg.cn/blog_migrate/303b93dc61f0399d6b6ad73940d3033d.png)

然后在sbin下执行

```
./nginx -s reload
```

重新加载配置，然后再进行测试

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/d2d7957684914173b2ea5ac8d23c76be_aomandeshangxiao.jpg!1)

傲慢的上校](https://blog.csdn.net/aomandeshangxiao)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  10

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  7

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

专栏目录

[*Nginx*部署*KkFileView*](https://blog.csdn.net/liwan09/article/details/139318055)

[liwan09的博客](https://blog.csdn.net/liwan09)

05-30
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2631

[*KkFileView*是一款开源的附件在线*预览*工具，基本支持主流文档格式*预览*。详细*使用*说明参见*kkFileView* - 在线文件*预览*。](https://blog.csdn.net/liwan09/article/details/139318055)

[*kkFileView*文档在线*预览*方案及*Nginx*代理方式访问](https://blog.csdn.net/tdcqfyl/article/details/147626133)

[时光清浅处，一步一安然](https://blog.csdn.net/tdcqfyl)

04-30
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1493

[*kkFileView*是一款基于Spring Boot的开源免费在线文件文档*预览*工具，支持多种办公文档和非办公文件格式的在线*预览*。](https://blog.csdn.net/tdcqfyl/article/details/147626133)

参与评论
您还未登录，请先
登录
后发表或查看评论

[Linux部署开源文档*预览*服务*kkfileview*](https://download.csdn.net/download/Aria_Miazzy/87916375)

06-16

[Linux部署开源文档*预览*服务*kkfileview*](https://download.csdn.net/download/Aria_Miazzy/87916375)

[*nginx*代理后刷新显示404](https://devpress.csdn.net/v1/article/detail/122439879)

[qq\_42846807的博客](https://blog.csdn.net/qq_42846807)

01-11
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3559

[1、错误的配置（看看自己是不是这样配置的）
原因：原因是因为web单页面开发模式，只有一个index.html入口，其他路径是前端路由去跳转的，*nginx*没有对应这个路径，当然就是404了。
location / {
alias /home/vue/dist/;
index index.html;
}
2、正确的配置应该是：
location / {
alias /home/vue/dist/;
index index.html;
try](https://devpress.csdn.net/v1/article/detail/122439879)

[KKfile 实现*nginx* 代理Https 访问，config 文件修改

最新发布](https://blog.csdn.net/buguaidejiahuo/article/details/150515618)

[buguaidejiahuo的专栏](https://blog.csdn.net/buguaidejiahuo)

08-19
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
415

[SSL 相关配置。](https://blog.csdn.net/buguaidejiahuo/article/details/150515618)

[kkfile配置https*预览*文件

热门推荐](https://devpress.csdn.net/v1/article/detail/125609996)

[你是我一生的追求](https://blog.csdn.net/onlyoneggp)

07-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1万+

[kkfile配置https*预览*文件](https://devpress.csdn.net/v1/article/detail/125609996)

[*nginx* 代理*kkFileView*不能*预览**问题*解决 413头部过大异常解决](https://blog.csdn.net/oJingJingdeDengDai/article/details/149829365)

[jingjing等待的博客](https://blog.csdn.net/oJingJingdeDengDai)

08-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
351

[我的配置,proxy\_set\_header可自己去掉,加上是不让多余的header加入 导致413头部过大异常。按照官网说明修改 *kkFIleView*的配置文件。](https://blog.csdn.net/oJingJingdeDengDai/article/details/149829365)

[*KKFileview*如何*使用**Nginx*进行*反向代理*实操](https://blog.csdn.net/weixin_39353771/article/details/148867738)

[weixin\_39353771的博客](https://blog.csdn.net/weixin_39353771)

06-24
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
948

[*KKFileView*是一款开源的文件在线*预览*解决方案，支持多种主流办公文档格式（Word、Excel、PPT、PDF、TXT、图片等），底层基于 LibreOffice 转换为 PDF 再渲染成 HTML 页面进行展示。本文围绕 Spring Boot + Vue 前后端分离架构，详细讲解了如何配置 *KKFileView* 的在线*预览*功能，并结合 *Nginx* 实现了不同网络环境下的代理访问机制。通过合理配置，不仅解决了跨域*问题*，还能根据不同网络环境灵活切换*预览*路径，保障系统的可用性与兼容性。](https://blog.csdn.net/weixin_39353771/article/details/148867738)

[项目*使用**kkFileView**预览**问题*](https://blog.csdn.net/qinshi501/article/details/136968130)

[qinshi501的博客](https://blog.csdn.net/qinshi501)

03-23
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
4433

[这个流程是文件的文件地址拼上*预览*服务器地址，app访问的过程中，首先访问*预览*服务器，*预览*服务器会解析fullfilename作为文件名，解析拼接的文件地址访问，下载文件到*预览*服务器，然后返回*预览*信息给app。这里*预览*服务器解析我们的文件地址应该是url\_decode和base64\_decode，那应该是文件地址编码过程中出现了特殊字符，造成解码过程出现*问题*，因此可能是我们原始文件地址有特殊字符或者在编码过程中会出现特殊字符。这个插件的*预览*很简单，只需要部署服务*使用**预览*服务地址拼接自己的真实图片地址即可。](https://blog.csdn.net/qinshi501/article/details/136968130)

[kkviewfile 实现*nginx**反向代理*+https](https://blog.csdn.net/qq_41941256/article/details/126059262)

[qq\_41941256的博客](https://blog.csdn.net/qq_41941256)

07-29
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
7864

[k...