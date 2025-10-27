---
title: myeclipse打包项目，报Security alert:integrity check error
url: https://blog.csdn.net/aomandeshangxiao/article/details/127899408
source: 傲慢的上校的专栏
date: 2022-11-18
fetch_date: 2025-10-03T23:05:12.292038
---

# myeclipse打包项目，报Security alert:integrity check error

# myeclipse打包项目，报Security alert:integrity check error

原创
于 2022-11-17 10:47:30 发布
·
1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

0

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

1
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#myeclipse](https://so.csdn.net/so/search/s.do?q=myeclipse&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#ide](https://so.csdn.net/so/search/s.do?q=ide&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Spring
专栏收录该内容](https://blog.csdn.net/aomandeshangxiao/category_12014592.html "Spring")

6 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了解决MyEclipse中com.genuitec.eclipse.export.wizard\_9.0.0.me201211011550.jar导致的导出向导错误的方法，包括备份、替换同名jar包、修改文件后缀等步骤。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/af8e445250189407452052a883da2e41.png)

1、备份 MyEclipse\Common\plugins下面com.genuitec.eclipse.export.wizard\_9.0.0.me201211011550.jar

2、将MyEclipse\Common\plugins下面替换MyEclipse\Common\plugins下面同名jar包

3、重新启动

4、如还报错，把com.genuitec.eclipse.export.wizard\_9.0.0.me201211011550.jar后缀名改为txt，关闭MyEclipse，再重新打开，再关闭，把txt后缀改回jar，打开Myeclipse即可

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

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  1

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

[【*Java*】*Myeclipse* 10*项目*导出war包*报*错 ：*Security* *Alert*：*Integrity* *check* *error*](https://blog.csdn.net/W15732624773/article/details/72901486)

[王璐](https://blog.csdn.net/W15732624773)

06-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
6870

[【前言】
         *Java*web工程一般打成war包来进行发布，小编尝试打war包的过程中遇到了问题，特此记录。希望可以给读者带来帮助。

【解决过程】
         打war包
         第一步：右击需要*打包*的*项目*，选择 Export--导出。
         第二步：选择*Java*EE下的 WAR file，点击下一步。](https://blog.csdn.net/W15732624773/article/details/72901486)

[*myeclipse*10.7破解,解决导出war包时*报*“*SECURITY* *ALERT* INTEGERITY *CHECK* *ERROR*”](https://download.csdn.net/download/dingmao6790229/8517807)

03-20

[本次对于*myeclipse*10 7破解后 导出war包时*报*“*SECURITY* *ALERT**:* INTEGERITY *CHECK* *ERROR*”进行了破解
只要执行完第一步的破解后 将com genuitec eclipse export wizard 9 0 0 me201211011550 jar替换plugins目录下的同名文件即可
替换后 最好将jar文件改成 txt文件结尾 然后重启*myeclipse*10 然后关闭 再将jar改回 jar为扩展名的状态 重启后就可以了 ">本次对于*myeclipse*10 7破解后 导出war包时*报*“*SECURITY* *ALERT**:* INTEGERITY *CHECK* *ERROR*”进行了破解
只要执行完第一步的破解后 将com genuitec eclipse export wizard 9 0 0 me201211011550 jar替换plugins目录下的同名文件即可
替换后 最好将jar文件改 [更多]](https://download.csdn.net/download/dingmao6790229/8517807)

参与评论
您还未登录，请先
登录
后发表或查看评论

[激活*myeclipse*10.7出现的*SECURITY* *ALERT**:**INTEGRITY* *CHECK* *ERROR*](https://download.csdn.net/download/bankibm/8801607)

06-13

[适用*myeclipse*10.1-10.7,亲测10.7有效.其他版本不能用时给我留言,留下邮箱,我给发.](https://download.csdn.net/download/bankibm/8801607)

[*SECURITY* *ALERT**:**INTEGRITY* *CHECK* *ERROR*](https://download.csdn.net/download/lizhao1226/9185429)

10-16

[*myeclipse*2015 ci破解后，*报*错，自动关闭；
解决方法：还原破解前的jar文件。
com.genuitec.eclipse.core\_13.0.2.me201508121459.jar](https://download.csdn.net/download/lizhao1226/9185429)

[解决*myeclipse*导出war时，出现“*security* *alert**:**integrity* *check* *error*”](https://download.csdn.net/download/tammie_kk/10109095)

11-08

[解决*myeclipse*不能正常导出war包问题,出现“*security* *alert**:**integrity* *check* *error*”
替换到目录：*MyEclipse*10.7\Common\plugins\com.genuitec.eclipse.export.wizard\_9.0.0.me201211011550.jar](https://download.csdn.net/download/tammie_kk/10109095)

[解决*myeclipse*10.1导出War包出错：*Security* *Alert*：*Integrity* *check* *error*](https://blog.csdn.net/w995223851/article/details/88350032)

[蕃薯耀的博客](https://blog.csdn.net/w995223851)

01-30
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
450

[eye.com/

一、问题描述：
*myeclipse*10.1破解后导出War包出错，提示“*Security* *Alert*：*Integrity* *check* *error*”。

二、解决方案：
原因是*myeclipse*破解不完整，造成导出War包时提示出错，解决方法就是替换一个Jar文件。

操作如下：
1、进入*myeclipse*安装目录下的：%*myeclipse*安装目录%/Common/plugins/
2、把com.genuitec.eclipse.export.wizard\_](https://blog.csdn.net/w995223851/article/details/88350032)

[用*myeclipse**打包**项目*时，*Security* *alert**:**integrity* *check* *error*。](https://blog.csdn.net/qq_25983579/article/details/102778332)

[qq\_25983579的博客](https://blog.csdn.net/qq_25983579)

10-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
645

[1 问题描述
用*myeclipse*10*打包**项目*时，出现如下图的提示：*Security* *alert**:**integrity* *check* *error*
2 问题原因
主要是由于Jar包不符合所导致的
3 解决方法
3.1下载资源
链接地址*:*https*:*//pan.baidu.com/s/1SbN5YcEJ8R-gmfwqfGJWVw
提取码*:*5oh4
3.2 替换jar
*报*错的时候会有提示目录
1 进...](https://blog.csdn.net/qq_25983579/article/details/102778332)

[*myeclipse*10.1导出War包出错：*Security* *Alert*：*Integrity* *check* *error*](https://download.csdn.net/download/w995223851/10229803)

01-29

[在使用*MyEclipse* 10.1开发*Java* Web*项目*时，有时会遇到这样一个问题：当你尝试将*项目*导出为WAR（Web Archive）包时，系统弹出错误提示“*Security* *Alert*：*Integrity* *check* *error*”。这个错误通常意味着*MyEclipse*在*打包*...](https://download.csdn.net/download/w995223851/10229803)

[轻松解决*Myeclipse*打开后遇到 *SECURITY* *ALERT**:* *INTEGRITY* *CHECK* *ERROR*](https://blog.csdn.net/fearless21/article/details/103375238)

[fearless21的博客](https://blog.csdn.net/fearless21)

12-03
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2684

[好几天没打开软件了，今天打开后突然出现 *SECURITY* *ALERT**:* *INTEGRITY* *CHECK* *ERROR* 这个提示，然后经过几次尝试完美解决，下面就是解决步骤
①将*报*错jar包*:*D*:*\app\*MyEclipse*\plugins\com.genuitec.eclipse.core\_14.0.0.20xxxxxx1000.jar剪切到桌面或其他非D盘的任意位置；
②重启*Myeclipse*程序...](https://blog.csdn.net/fearless21/article/details/103375238)

[解决*myeclipse*破解运行后出现的*security* *alert**:**integrity* *check* *error*](https://blog.csdn.net/weixin_42479134/article/details/88766435)

[weixin\_42479134的博客](https://blog.csdn.net/weixin_42479134)

03-23
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
8575

[解决*myeclipse*破解运行后出现的*security* *alert**:**integrity* *check* *error*
安装完*MyEclipse* 2017 CI破解版本后，...