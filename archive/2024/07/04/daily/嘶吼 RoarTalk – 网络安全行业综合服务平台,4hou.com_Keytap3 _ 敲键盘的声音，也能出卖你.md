---
title: Keytap3 | 敲键盘的声音，也能出卖你
url: https://www.4hou.com/posts/7yNy
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-04
fetch_date: 2025-10-06T17:40:50.005017
---

# Keytap3 | 敲键盘的声音，也能出卖你

Keytap3 | 敲键盘的声音，也能出卖你 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Keytap3 | 敲键盘的声音，也能出卖你

RC2反窃密实验室
[行业](https://www.4hou.com/category/industry)
2024-07-03 15:50:08

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)100232

收藏

导语：信息的窃取方式多种多样，但有一种方法可能尤为出乎意料。

![1.1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357263402894.jpg "1718356827265593.jpg")

声明：以下内容符合OSINT国际开源情报搜集定义，不涉及任何非法行为，仅供交流与参考。

**01 技术原理**

你永远想不到，你敲键盘的声音，也可以悄悄出卖你。

程序员Georgi Gerganov给出了一种不通过任何蓝牙、WiFi或其它射频信号，仅仅通过普通的麦克风，就可以窃听键盘输入的方法。

**其原理是**：先捕获键盘敲击的音频，然后生成敲击音的集群图，再通过对相关字母在假定的文本语言中出现频率的统计信息来分析这些集群。

和猜测密码类似，该算法中已经定义了在某些语言（如英语）中使用频率较高的一些字母组合，这样就可以开展猜测推导。

**02 实际测试**

杨叔直接上手体验，进行了测试。

**开始测试前的注意事项：**

**·**在安静的房间里

**·**在手机或PC上打开测试页并将键盘放麦克风旁

**·**使用小写字母和空格，在键盘上键入一些英文

**·**尽量不要以超过 250 CPM 的速度输入

**·**仅适用于机械键盘，因为敲击声更大

不需将键盘连接电脑，或者给键盘安装电池，下图这样就好

![1.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357264458493.jpg "1718356915165933.jpg")

录制足够的音频后，程序将开始分析录音并尝试恢复键入的文本内容。

![1.3.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357264145486.gif "1718356950213070.gif")

杨叔准备了4~5款不同品牌的机械键盘，PS：刚好用到之前KCON黑客大会送的键盘礼

![1.4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357265671855.jpg "1718356976159213.jpg")

可以看到，在杨叔敲击键盘的时候，Keytap3通过电脑的麦克风，捕捉到并记录了机械键盘的敲击声。

![1.5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357266202814.png "1718357031151237.png")

GUI图形版看起来比较清晰，不像下图这个Shell版本，只能看到命令执行效果：

通过测试，杨叔个人怎么觉得还是老版本的Keytap2更直观好用，准确率更高些

![1.6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357266103015.png "1718357075103431.png")

通过测试，杨叔个人怎么觉得还是老版本的Keytap2更直观好用，准确率更高些

![1.7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357267984184.png "1718357120569786.png")

感兴趣的朋友，可以前往 Gerganov 的网站亲自尝试一下，网址如下：

代码地址：https://github.com/ggerganov/kbd-audio

Demo体验：https://keytap3.ggerganov.com/

最好先准备一个**声音响亮的机械键盘**，配合**准确的英语书写**，才能获得最佳结果。

换句话说，你若是下图这样敲键盘，那估计没啥效果。

![1.8.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357267126663.gif "1718357155111012.gif")

有个评论是这么说的：

虽然并不能说这个漏洞已经100% 完美无缺，但它确实能够猜测正在输入的内容，甚至可能会令人惊讶乃至担忧般地准确。

当然，仅仅通过录音，目前的版本可能无法完美地逐字提取冗长的文字，比如邮件内容等。

但它成功提取的单词中可能包括**用户名、密码**，甚至是你不希望与他人共享的**网站URL**

![1.9.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357268337290.gif "1718357180123147.gif")

**03 如何防范**

到底该如何防范呢？

既然我们已经知道了原理，那防范就很简单了

**方法1**：在键盘上加软垫，减少机械键盘声音。

**方法2**：更换机械键盘为静音键盘，减小音量。

网上有人提出了上述两种方法，想来应该都是些不理解机械键盘买家心情的家伙吧？

为什么有人偏爱机械键盘？

就是因为机械键盘“敲”起来爽啊！！

![1.10.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357268940021.gif "1718357203178529.gif")

那些说什么“爱德华·斯诺登在输入密码时会在笔记本电脑上盖毯子”的，杨叔专门查了下，那只是一句关于斯诺登平时很重视安全的玩笑梗，没想到有人当真了

**方法3**：干扰键盘敲击声，如放音乐增加背景噪音、增加一些小动作、减少手指敏感度等等。

![1.11.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357269127660.gif "1718357224127596.gif")

嗯，这个思路可以自行拓展下，上图仅供参考

**方法4**：使用高科技虚拟键盘，比如三星出的SelfieType镭射投影式键盘，移动设备用户能随时在任何平面上，通过虚拟键盘录入。

这个技术虽然缺乏打字的回馈手感，但对于Keytap3来说，显然是有效的。

![1.12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240614/1718357269942338.jpg "1718357246702408.jpg")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TCQptjGk)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/182735b0219b1d7a63869aa0c554f245.png)

# [RC2反窃密实验室](https://www.4hou.com/member/33jn)

专注TSCM，物理安全和隐私保护~

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/33jn)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)