---
title: 又见劫持
url: https://h4ck.org.cn/2022/11/%e5%8f%88%e8%a7%81%e5%8a%ab%e6%8c%81/
source: obaby@mars
date: 2022-11-07
fetch_date: 2025-10-03T21:52:03.789410
---

# 又见劫持

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 又见劫持

2022年11月6日
[一条评论](https://h4ck.org.cn/2022/11/10683#comments)

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/6b3c6999586e7f553c985bc04597a290.jpg)

昨天dujun问我的证书是不是到期了，查看了一下并没有，已经更新到23年一月份了。由于没有自动将http跳转到https之前劫持的事情倒是也见过。

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/63668ddde0cf6.png)

这种劫持也是非常恶心，不知道还以为是网站自己投放的广告（问题是我特喵的没放广告啊）。

上次遇到的是青岛联通劫持的quickconnect.cn。在之前是移动劫持的gravatar.com（https://h4ck.org.cn/2019/10/%E9%9D%92%E5%B2%9B%E7%A7%BB%E5%8A%A8%E5%8A%AB%E6%8C%81%E4%BA%861-gravatar-com-rofl/）。再往前就是青岛的长城直接dns劫持各种广告注入。

于是，今天早上我把http重新定向到https上了。

```
server
    {
        listen 80;
        #listen [::]:80;
        server_name h4ck.org.cn www.h4ck.org.cn;

        return       301 https://h4ck.org.cn$request_uri;
}
```

虽然还是存在被劫持的可能，但是难度还是提升了一些的（劫持的方式很多，参考：https://h4ck.org.cn/?s=%E5%8A%AB%E6%8C%81）。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《又见劫持》](https://h4ck.org.cn/2022/11/10683)
\* 本文链接：<https://h4ck.org.cn/2022/11/10683>
\* 短链接：<https://oba.by/?p=10683>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[DNS劫持](https://h4ck.org.cn/tags/dns%E5%8A%AB%E6%8C%81)[浏览器劫持](https://h4ck.org.cn/tags/%E6%B5%8F%E8%A7%88%E5%99%A8%E5%8A%AB%E6%8C%81)

[Previous Post](https://h4ck.org.cn/2022/11/10691)
[Next Post](https://h4ck.org.cn/2022/11/10677)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年3月11日

#### [再谈评论区亲密度](https://h4ck.org.cn/2024/03/15777)

2009年9月25日

#### [WordPress 正文添加标签选项](https://h4ck.org.cn/2009/09/264)

2020年12月31日

#### [修改WordPress 文章内分页样式](https://h4ck.org.cn/2020/12/7932)

### 1 comment

1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r) **[TeacherDu](https://dusays.com)**说道：

   [2022年11月10日 18:34](https://h4ck.org.cn/2022/11/10683#comment-88783)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   宽带运营商做劫持真是恶心，那点广告能挣到什么钱，但是大大影响了站点的访问体验，通过公共DNS能好些！

   [回复](#comment-88783)

### 发表回复 [取消回复](/2022/11/10683#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

[x] 如果有人回复我的评论，请通过电子邮件通知我。

[x]

Δ

### 标签云[Tag Cloud]

Your browser doesn't support the HTML5 CANVAS tag.

* [心情](https://h4ck.org.cn/tags/myfeeling)
* [PETools](https://h4ck.org.cn/tags/petools)
* [游戏](https://h4ck.org.cn/tags/game)
* [Mac OS](https://h4ck.org.cn/tags/mac-os)
* [CDN](https://h4ck.org.cn/tags/cdn)
* [大姨妈](https://h4ck.org.cn/tags/%E5%A4%A7%E5%A7%A8%E5%A6%88)
* [C/C++](https://h4ck.org.cn/tags/cc)
* [Crack](https://h4ck.org.cn/tags/crack)
* [ASM](https://h4ck.org.cn/tags/asm)
* [Plugin](https://h4ck.org.cn/tags/plugin)
* [无题](https://h4ck.org.cn/tags/nomean)
* [远程控制](https://h4ck.org.cn/tags/remot-control)
* [Python](https://h4ck.org.cn/tags/python)
* [月经](https://h4ck.org.cn/tags/%E6%9C%88%E7%BB%8F)
* [IDA](https://h4ck.org.cn/tags/ida)
* [Linux](https://h4ck.org.cn/tags/linux)
* [Python3](https://h4ck.org.cn/tags/python3)
* [php](https://h4ck.org.cn/tags/php)
* [驱动开发](https://h4ck.org.cn/tags/driver-develop)
* [m3u8](https://h4ck.org.cn/tags/m3u8)
* [Delphi](https://h4ck.org.cn/tags/delphi)
* [美女](https://h4ck.org.cn/tags/beauty)
* [WordPress](https://h4ck.org.cn/tags/wordpress)
* [秀人集](https://h4ck.org.cn/tags/%E7%A7%80%E4%BA%BA%E9%9B%86)
* [PE](https://h4ck.org.cn/tags/pe)
* [Windows](https://h4ck.org.cn/tags/windows)
* [QQ](https://h4ck.org.cn/tags/qq)
* [Android](https://h4ck.org.cn/tags/android)
* [APK](https://h4ck.org.cn/tags/apk)
* [杂谈](https://h4ck.org.cn/tags/zatan)
* [Virus Analysit](https://h4ck.org.cn/tags/virus-analysit)
* [CentOS](https://h4ck.org.cn/tags/centos)
* [Porn](https://h4ck.org.cn/tags/porn)
* [OSX](https://h4ck.org.cn/tags/osx)
* [系统美化](https://h4ck.org.cn/tags/os-diy)
* [Django](https://h4ck.org.cn/tags/django)
* [闺蜜圈](https://h4ck.org.cn/tags/%E9%97%BA%E8%9C%9C%E5%9C%88)
* [Google](https://h4ck.org.cn/tags/google)
* [文本编辑](https://h4ck.org.cn/tags/texteditor)
* [jeb](https://h4ck.org.cn/tags/jeb)
* [UniApp](https://h4ck.org.cn/tags/uniapp)
* [yolov5](https://h4ck.org.cn/tags/yolov5)
* [爬虫](https://h4ck.org.cn/tags/%E7%88%AC%E8%99%AB)
* [Debugger](https://h4ck.org.cn/tags/debugger)
* [spider](https://h4ck.org.cn/tags/spider)
* [iOS](https://h4ck.org.cn/tags/ios)
* [OD](https://h4ck.org.cn/tags/od)
* [妹子图](https://h4ck.org.cn/tags/%E5%A6%B9%E5%AD%90%E5%9B%BE)
* [ubuntu](https://h4ck.org.cn/tags/ubuntu)
* [Unpack](https://h4ck.org.cn/tags/tuoke)

### 搜索[Search]

Search for:

Search

### 简介[Contact]

[![小妖精高P，嘻嘻](/wp-content/uploads/2025/08/IMG_20250807_171128-tuya-scaled.webp)](https://h4ck.org.cn/envira/%E5%86%99%E7%9C%9F2024)

本站所破解的程序仅限于分析研究使用，不可用于非法用途，如果喜欢该软件请购买正版。由于程序所造成的损失本人概不负责。(Findu App由于阿里旺信服务关闭，暂时停止推荐，如果想和我一块开发，请联系我~~)

---

### 分类目录[Category]

分类目录[Category]
选择分类
点点滴滴『Past &Future』  (457)
   个人日记『Diary』  (281)
   临时目录『Temp』  (17)
   发表的文章『Posted ArticleS』  (5)
   手机魔方『Phone』  (23)
   无心呢喃『Feelings』  (17)
   游戏娱乐『Game/Funny』  (27)
   说说『Talk』  (84)
破解/汇编『Crack/Asm』  (306)
   插件『IDA/OD/IMMDbg Plugin』  (62)
   汇编『ASM』  (7)
   病毒分析『Virus Analysis』  (7)
   脱壳『Unpack』  (12)
程序设计『Programing』  (385)
   业余爱好『Favourite』  (111)
   人工智能『AI』  (39)
   前端开发『FrontEnd』  (24)
   后台开发『BackEnd』  (63)
   物联网『IoT』  (9)
系统相关『OS』  (277)
   Linux『Linux』  (36)
   Mac OSX『Mac OS』  (42)
   安卓『Android』  (37)
   微软『Windows』  (85)
   苹果『iOS』  (37)
   远程控制『RemoteCtrl』  (7)
经验总结『Skills Summary』  (135)
   入侵渗透『Expliot/Injection』  (8)
   动画教程『Vidoes』  (2)
   博客相关『Blogger/WordPress』  (97)
   杀毒安全『AntiVirus』  (11)

### 说说[Talk]

* [再也不见，去死吧](https://h4ck.org.cn/microposts/%E5%86%8D%E4%B9%9F%E4%B8%8D%E8%A7%81%EF%BC%8C%E5%8E%BB%E6%AD%BB%E5%90%A7)

  [评论:![](https://h4ck.org.cn/wp-content/plugins/simple-microblogging/bubble-icon.png)×0](https://h4ck.org.cn/microposts/%E5%86%8D%E4%B9%9F%E4%B8%8D%E8%A7%81%EF%BC%8C%E5%8E%BB%E6%AD%BB%E5%90%A7)

  [![](https://h4ck.org.cn/wp-content/uploads/2025/09/VolumesApple图片personalJietu20250928-090043.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/VolumesApple%E5%9B%BE%E7%89%87personalJietu20250928-090043.jpg)

  ☆版权☆

  \* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**

  ---

### 随机文章[Random Posts]

* [![](https://h4ck.org.cn/support/uugai.com-1661691272754.png)](https://h4ck.org.cn/2011/04/2676)

  [破解/汇编『Crack/Asm』](https://h4ck.org.cn/cats/crackasm)

  2011年4月13日
* [![](https://h4ck.org.cn/support/uugai.com-1661691272754.png)](https://h4ck.org.cn/2010/11/2190)

  [破解/汇编『Crack/Asm』](https://h4ck.org.cn/cats/crackasm)

  20...