---
title: 半途而废的机顶盒刷机
url: https://h4ck.org.cn/2023/01/%e5%8d%8a%e9%80%94%e8%80%8c%e5%ba%9f%e7%9a%84%e6%9c%ba%e9%a1%b6%e7%9b%92%e5%88%b7%e6%9c%ba/
source: obaby@mars
date: 2023-01-31
fetch_date: 2025-10-04T05:13:15.372873
---

# 半途而废的机顶盒刷机

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

[破解/汇编『Crack/Asm』](https://h4ck.org.cn/cats/crackasm)

# 半途而废的机顶盒刷机

2023年1月30日
[22 条评论](https://h4ck.org.cn/2023/01/11099#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

最开始想给华为的那个iptv盒子刷机还是好几年前，不过尝试了好多次，包括进入恢复模式之类的。最终也没刷成功，那时候想装app主要是原来的55寸的那个海信电视变得非常卡了。就想着用iptv的机顶盒替代一下。不过最终还是失败了，这台电视后来搬到了昌乐的家里用，结果初五的那天早上忽然开不了机了。完了，芭比Q了。给海信的400打电话，初六去看了一下，表示要带回去拆机才能知道是哪里的问题。由于初七就要回青岛，早上修不好就得一直扔在那里，于是就放弃了。甚至我都开始看新的电视了。

昨天晚上又在看iptv的设置界面发现一个远程链接的选项：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/IMG_20230129_205433-tuya-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/IMG_20230129_205433-tuya-scaled.jpg)

搜索了一下发现使用一个华为的HuaWei\_STB工具就可以连接到iptv的盒子上了（切换到同一个网络内）。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230130201902.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230130201902.jpg)

输入ip地址和密码点击链接即可获取到机顶盒的各种参数。

后面就是开启adb链接，点击启用远程登录，选择开之后点击提交，现在就可以使用adb链接机顶盒安装apk了

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230129210750-1.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230129210750-1.jpg)

如果链接失败可以多长时间几次，任务管理器挂掉adb的进程。 install的时候要注意把apk放到adb的目录下，可以简化操作命令。提示安装成功之后去box上并找不到这个应用，需要在安装个第三方桌面，例如沙发桌面、当贝桌面之类的。我就在这个地方放弃了，因为现在机顶盒是连得联通的iptv的专用百兆端口，不确定这个端口是不是能够访问互联网的其他资源。另外，换了电视之后也没那么卡了，现在没有强需求需要使用那个iptv盒子，不过海信电视比较蛋疼的一点就是，安装几个应用之后就会提示内存不足。删除应用释放空间之后也没什么大的效果，最终恢复出厂设置解决了这个问题。

使用的工具从这里获取：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

**模特**：[IMISS爱蜜社]Vol.710\_模特合集女神Lavinia肉肉私房性感姐妹花情趣内衣撩人诱惑写真41P

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《半途而废的机顶盒刷机》](https://h4ck.org.cn/2023/01/11099)
\* 本文链接：<https://h4ck.org.cn/2023/01/11099>
\* 短链接：<https://oba.by/?p=11099>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[adb](https://h4ck.org.cn/tags/adb)[HuaweSTB](https://h4ck.org.cn/tags/huawestb)[IPTV](https://h4ck.org.cn/tags/iptv)[安卓](https://h4ck.org.cn/tags/%E5%AE%89%E5%8D%93)

[Previous Post](https://h4ck.org.cn/2023/02/11131)
[Next Post](https://h4ck.org.cn/2023/01/11094)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2011年3月22日

#### [.NET Reflector 7.0 Cracked](https://h4ck.org.cn/2011/03/2578)

2012年12月21日

#### [也谈《Linux脚本自动备份网站数据到Dropbox》](https://h4ck.org.cn/2012/12/4867)

2011年7月15日

#### [SQL Pretty Printer 2.8.1 Cracked by obaby](https://h4ck.org.cn/2011/07/2946)

### 22 comments

1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r) **[TeacherDu](https://dusays.com)**说道：

   [2023年1月31日 00:30](https://h4ck.org.cn/2023/01/11099#comment-91722)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 109") Microsoft Edge 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   现在的机顶盒都是越用越卡，他们不做优化的吗？

   [回复](#comment-91722)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年1月31日 08:53](https://h4ck.org.cn/2023/01/11099#comment-91734)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      基本没啥优化，系统倒是更新了好几个版本。关键是现在的电视带的系统也很智障存储空间装5个app就提示空间不足了。当然，也可能和我买的配置不是很高也有关系，但是整体体验会下降很多。

      [回复](#comment-91734)

      1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

         [2023年1月31日 10:19](https://h4ck.org.cn/2023/01/11099#comment-91736)

         ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

         ![Microsoft Edge 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 109") Microsoft Edge 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         我之前尝试过使用树莓派来安装盒子系统，然后作为电视盒子使用，想着树莓派的性能至少在那，肯定没有问题。
         但是使用一段时间，发现还是会有卡顿。
         现在怀疑是不是盒子的系统都有问题，越用越卡！

         [回复](#comment-91736)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2023年1月31日 14:06](https://h4ck.org.cn/2023/01/11099#comment-91748)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            盒子用过好几个品牌，最开始的大迈box，用了三年。后面就不大好用了，再后来就一直用的联通送的华为的这款盒子。如果不刷机就用系统自带的那个电视功能倒是卡顿没那么明显，但是一旦装第三方应用，慢慢的就废了。老家各种盒子我数了一下大概有七八个，基本都废掉了。现在从淘宝买个刷好的盒子百十块钱倒是也不贵。但是寿命整体来说都很一般，很快就各种问题了。

            [回复](#comment-91748)

            1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

               [2023年2月1日 14:13](https://h4ck.org.cn/2023/01/11099#comment-91788)

               ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

               ![Microsoft Edge 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 109") Microsoft Edge 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

               我只用过小米这么一个牌子，几乎每次更新换代，都会购买新款。
               不知道是不是我的心理作用，总感觉新款发布后，老款就开始卡。

               [回复](#comment-91788)

               1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740...