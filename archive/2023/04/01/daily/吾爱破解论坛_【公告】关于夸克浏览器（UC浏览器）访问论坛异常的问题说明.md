---
title: 【公告】关于夸克浏览器（UC浏览器）访问论坛异常的问题说明
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651139215&idx=1&sn=5e680c6bd3318548e733d411da2a612b&chksm=bd50bcdb8a2735cd342cc4a413678fcdb4ba87ed00cae4133791dca9ced78b1b669b78c19492&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2023-04-01
fetch_date: 2025-10-04T11:22:28.148030
---

# 【公告】关于夸克浏览器（UC浏览器）访问论坛异常的问题说明

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZLaHZdP3Ic58wiaxzoibQwS5u8iaQiaasTXibWAUoTwcjAjwzhMEbjQVheibDibIDia0OpnY9ekJ4ibibafTB7g/0?wx_fmt=jpeg)

# 【公告】关于夸克浏览器（UC浏览器）访问论坛异常的问题说明

原创

吾爱pojie

吾爱破解论坛

近期收到大量用户反馈，访问论坛出现491拦截，通过用户反馈和服务器访问日志还有安域WAF平台诊断，出现问题的用户全是夸克浏览器（UC浏览器），随即我们进行了深入的分析发现了原因。

一：现象
使用夸克浏览器（UC浏览器）访问论坛会出现各种各样的问题，如：
1、输入账号密码信息后点登录无反应，刷新后已经登录，退出登录无任何反应，刷新也无效。
2、之前开放注册很多同学反馈点注册没反应或者提示IP已经被注册应该也是同一个问题。（这个锅我们和运营商背了很久。。。）
3、在发帖页或者回帖页点击发帖或者回帖无反应。（搜索等其他有交互的功能可能都会有问题）
4、验证码怎么输入都不对，或者提交无反应。
5、访问论坛很容易被防火墙拦截，出现491错误。

二：分析过程
1、既然是WAF拦截了，我们就联系安域WAF平台的小伙伴，联合进行了分析发现拦截的原因是用户访问的时候产生了大量的404请求，被判断可能存在扫描行为，所以进行了短暂的拦截，这就很奇怪了，正常用户为什么会产生404了，并且通过日志UA发现基本都来自夸克浏览器和UC浏览器，两家都是阿里系的，而且产生的404请求的URL和来源IP看起来就是个功能导致BUG。（后面详述）

2、我们先来看看404用户的请求内容：

```
[31/Mar/2023:14:43:08 +0800] "GET /thread-1766332-1-1.html HTTP/1.1" 200 40209 "https://www.52pojie.cn/" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X; zh-cn) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/20E247 Quark/6.2.2.1622 Mobile" "211.94.109.52"[31/Mar/2023:14:43:08 +0800] "GET /https://www.52pojie.cn/source/plugin/zxsq_markdown/css/markdown.css HTTP/1.1" 404 1367 "https://www.52pojie.cn/thread-1766332-1-1.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X; zh-cn) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/20E247 Quark/6.2.2.1622 Mobile" "211.94.109.52"[31/Mar/2023:14:43:08 +0800] "GET /https://www.52pojie.cn/source/plugin/zxsq_code/css/code.css HTTP/1.1" 404 1367 "https://www.52pojie.cn/thread-1766332-1-1.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X; zh-cn) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/20E247 Quark/6.2.2.1622 Mobile" "211.94.109.52"[31/Mar/2023:14:43:08 +0800] "GET /https://www.52pojie.cn/source/plugin/zxsq_markdown/js/code-tools.js HTTP/1.1" 404 1367 "https://www.52pojie.cn/thread-1766332-1-1.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X; zh-cn) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/20E247 Quark/6.2.2.1622 Mobile" "211.94.109.52"
```

正常访问一个贴子以后，出现了3条404请求，很明显可以看出来URL这里出问题了，居然多是“/https://www.52pojie.cn”，这个问题是怎么产生的了？
我们随即看了下贴子的源代码，先找到markdown.css的信息：
<link rel="stylesheet" href="source/plugin/zxsq\_markdown/css/markdown.css" /><

很明显页面这里的请求被再次追加一个域名导致的问题。

3、既然大概找到了原因，并且所有信息都指向了夸克，那我们就来验证一下，可以通过UA看出来是iPhone上的Quark浏览器，我们去安装了最新版（版本号：6.2.2.1622 app-230323143317），开始复现并没有出现问题，因为之前都是用户邮件反馈，基本都是注册用户，所以随即我们进行了登录账号测试，这时候异常的问题开始接踵而至，首先输入账号密码信息后点登录无反应，验证码通过刷新后又让输入，多次失败后无奈只能刷新页面，这时候显示已经登录了，经验告诉我，不出意外肯定是什么云加速功能导致的问题。

登录后我们去访问上面的贴子，很容易复现了问题，和出问题的用户一样，产生了多个404请求，并且从访问IP看并不是我们自己的IP，通过纯真IP查询211.94.109.52来自数字北京大厦IDC机房，好家伙，明显是走了一层代理，因为早年UC云加速功能就出过验证码异常的问题，当年通过关闭就解决问题了，随即我们去找到夸克浏览器 设置--网页智能保护--智能云加速，将其功能关闭并重启浏览器，好家伙，现实再次打败了我们，关闭后依然还有问题，我们通过服务器发现，访问的IP还是来自代理服务器，并不是我们自己的IP，所以这个智能云加速开关真的有效吗？？？看了所有的功能只有设置--通用--智能预加载网页 还可能和这个有关我们也关闭了，还有刚刚网页智能保护功能全部关闭进行测试，依然被现实打败，是无效的。。。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZLaHZdP3Ic58wiaxzoibQwS5uQdeyC7qvjibxMmqmfzWpx9dvFlkzsAAawnJkHxQjTpuASUCGicXXGlrw/640?wx_fmt=jpeg)

既然无能为力，那我们就决定退出登录吧，现实依然残酷，不管你怎么退出都会提示你退出成功，但跳转回来以后还是登录状态，不知道我现在访问的页面是之前云加速代理服务器的缓存（那串号很太容易了），还是因为登录后的Cookie又有了，到底存在了本地没清理成功还是存在云加速代理服务器上，我们没有再进一步测试，太无能为力了。。。

三：临时措施：
1、由于无法通过浏览器开关解决问题，所以无奈我们在WAF上拦截了夸克浏览器云加速代理服务器IP，让代理功能失效，并添加明显的说明引导更换其它浏览器。

四：建议用户：
1、在厂商没修复问题之前，请更换其他浏览器进行访问。
2、不建议使用浏览器或者插件提供的预读或者翻页功能，短时间发出大量请求很可能会被防火墙判为扫描行为被拦截。
3、不建议使用各种代理加速功能。

五：建议厂商：
1、请修复云加速功能，我们测试开关无效，所以这是被迫选择拦截你们服务器的原因。
2、请修复代理服务器造成的URL请求BUG，理论上肯定不止我们站点，其他站点可能也会受到影响。
3、建议互动类的站点请勿开启云加速功能，特别请求贵方把我们的域名从云加速列表中删除，因为即使修复了URL的BUG，其他缓存导致的登录、发帖等问题依然无法解决。
4、如果修复了或者有什么需要沟通的可以邮件沟通Service@52pojie.cn，新的进展我们会更新到贴子中。

六：安全隐患
这种第三方代理很危险，很容易产生串号风险，导致账号被盗或者被他人滥用，还可能被劫持插入非法内容，谨慎起见最好不要使用，特别是浏览器厂商做这些事情，SSL加密都无法保证安全，中间篡改以后本地客户端可以做证书信任。

****-官方论坛****

www.52pojie.cn

**--推荐给朋友**

公众微信号：吾爱破解论坛

或搜微信号：pojie\_52

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

吾爱破解论坛

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过