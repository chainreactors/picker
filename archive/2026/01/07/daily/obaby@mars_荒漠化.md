---
title: 荒漠化
url: https://h4ck.org.cn/2026/01/22345
source: obaby@mars
date: 2026-01-07
fetch_date: 2026-01-08T03:29:07.613390
---

# 荒漠化

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

黑客程序媛 / 逆向工程师 / 人工智能学徒 / 用爱发电的独立开发者

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 荒漠化

2026年1月7日
[46 条评论](https://h4ck.org.cn/2026/01/22345#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/微信图片_20260107100836_522_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260107100836_522_42.jpg)

昨晚下班之后，依然跑步回家。今天的天气有些差，路上笼罩着一层雾气，路灯在迷雾中也变得有些朦胧。气温还是徘徊在零度多一点，一阵凉风吹来还是能感受到深深的寒意。

跑步的时候，难免也会想一些乱七八糟的事情，不禁就想到了最近关于 cursor 的各种行为问题。自从某天 cursor 的背景插件更新之后，编辑器在打开文件之后就开始频繁卡顿。正常情况下 cursor 插件都开了自动更新，也就是这次更新，让 cursor 直接到了崩溃的边缘。

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-101534.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-101534.jpg)

让 cursor 解决 ide 卡顿的问题，给推荐一个更加轻量化的插件 backgroud-cover,但是安装的时候是 3.0 版本，提示使用了什么后台服务，balalbalabal。刚开始使用一切顺利，然鹅，这几天更新几次后就又出现了卡顿的问题。

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-101753.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-101753.jpg)

只好回滚到了 3.0 版本，相对来说就稳定可靠多了。所以哦，并不是每次更新带来的都是优化，也可能是退化。

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-100708-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-100708.jpg)

退化的可能不仅仅是这些东西，ai 虽然也在不断的迭代，整体来说能力越来越强，但是针对特殊问题的解决能力却鲜有进步。集成百度 asr 语音识别之后，出现一个诡异的 bug，那就是在 安卓手机上正常，但是在 ios 系统上出错了。让 cursor 解决问题，给出的方案就是方法论的那一堆，包括定位错误，调整配置等等。当然，cursor 也不是一无是处，对于权限的处理还是有价值的：

```
"NSMicrophoneUsageDescription" : "To use the AI voice assistant's speech recognition feature",
"NSSpeechRecognitionUsageDescription" : "To use the AI voice assistant's speech recognition feature",
```

然而，对于具体的错误处理：

```
{
    "code": 2225220,
    "message": "Error Domain=33 Code=2225220 \"asr authentication failed[info:-3004] [(-3004)] \" UserInfo={NSLocalizedDescription=asr authentication failed[info:-3004] [(-3004)] , NSHelpAnchor=7697EC65-0C8F-4640-8993-699C90797ACC},https://ask.dcloud.net.cn/article/282"
}
```

cursor 给出的建议：

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-103848.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-103848.jpg)

说的的确是问题，但是实际上并不是问题的根本。哪怕去百度的后台看也是一切正常的，

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-104108-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-104108.jpg)

包括 ios 的包名也设置了，网上搜索，能看到的唯一的一篇相关的文章是官方论坛的：<https://ask.dcloud.net.cn/question/182917>

里面提到了注入权限，直接修改源文件，重新打包，申请资源包等等。然而，在我这里问题的关键在于开通按量付费里面的短语音识别、实时语音识别。

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-104516.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-104516.jpg)

虽然提示的是asr authentication failed，然而，在通过 cursor 一通折腾没有任何的效果之后。我就开始怀疑这个明显不是认证问题，因为目前能做的都做了，并且安卓可以，ios 不行，大概率还是百度平台的设置问题。而至于给出的错误码，这个充其量是个参考，之前对接百度原生的 asr 和 tts 的时候就出现过错误码毫无任何价值的情况。并且，更神奇的是，同样是语音识别，ios 走的是不同的接口，这也挺神奇的。而调用的接口，就是 uni 官方给出的：

```
var options = {
    engine: 'baidu'
};
text.value = '';
console.log('开始语音识别：');
plus.speech.startRecognize(options, function(s){
    console.log(s);
    text.value += s;
}, function(e){
    console.log('语音识别失败：'+JSON.stringify(e));
} );
```

<https://uniapp.dcloud.net.cn/tutorial/app-speech.html#%E9%85%8D%E7%BD%AE%E7%99%BE%E5%BA%A6%E8%AF%AD%E9%9F%B3%E8%AF%86%E5%88%AB>

对于这种问题，目前网上相关的资料少的可怜。可能也有人遇到过，可能解决了再也没人发文章了。

自从有了各种开发助理之后，现在网上的新的技术文章已经肉眼可见的少了。解决问题的文章也少了，不知道是大家都不在遇到问题了，还是真的让 ai 全部给解决了。

现在看到一篇文章，在不确定是真人写的情况下，第一认知，应该判定这个东西是 ai 生成的。现在要判断 ai 生成的内容，成本也越来越高了。

昨天下午博客有段时间卡死了，登录服务器发现 php进程跑满了。看了下实时流量的 ua 竟然有个 gptbot。日志文件分析之后，发现各种 bot 真的不少：

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-092218-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-092218.jpg)

而 umami 统计的流量，也属实有些离谱了：

[![](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-105501.jpg)](https://h4ck.org.cn/wp-content/uploads/2026/01/Jietu20260107-105501.jpg)

这种 ai 对于这种真人输出的内容的依赖性从来不低，毕竟 ai 生成的内容反复投喂给 ai，最后 ai 就会变成智障，这个和近亲繁殖有着异曲同工之效。太多的人依赖于 ai，ai 解决问题之后，也很少有人会在写这些问题的解决过程。只要 ai 还需要人类生成的内容进行 feed，那么哪怕是再拙劣的文字也有重大的价值，直到那天 ai 能自己进化，那时候就不需要人类的。

互联网的荒漠化进程依然会继续，珍惜那些愿意打字的博主们吧，他们才是这个时代的宝藏，让 ai 不会快速沦落为智障。

---

[![闺蜜圈 APP](/wp-content/uploads/2025/11/guimiquan-ads2.jpg)](https://sj.qq.com/appdetail/ma.dayi.app?&from_wxz=1)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《荒漠化》](https://h4ck.org.cn/2026/01/22345)
\* 本文链接：<https://h4ck.org.cn/2026/01/22345>
\* 短链接：<https://oba.by/?p=22345>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[AI](https://h4ck.org.cn/tags/ai)[UniApp](https://h4ck.org.cn/tags/uniapp)[博主](https://h4ck.org.cn/tags/%E5%8D%9A%E4%B8%BB)[百度](https://h4ck.org.cn/tags/%E7%99%BE%E5%BA%A6)

[Next Post](https://h4ck.org.cn/2026/01/22320)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年9月4日

#### [明月•山海间](https://h4ck.org.cn/2023/09/13180)

2013年4月9日

#### [Happy Birthday To Myself](https://h4ck.org.cn/2013/04/5082)

2024年7月25日

#### [华为 Pura 70 Pro — 不完美的 GMS 体验](https://h4ck.org.cn/2024/07/17727)

### 46 comments

1. ![](https://gg.lang.bi/avatar/290428aed24c54dab10263c1cf04ac4f9a7e20889aeaecb89529e426f0f51348?s=64&d=identicon&r=r) **[满心](https://zhoutian.com)**说道：

   [2026年1月7日 11:39](https://h4ck.org.cn/2026/01/22345#comment-131150)

   ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 5](https://badgen.h4ck.org.cn/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 143](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 143") Google Chrome 143 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   cursor的能力还是可以的，不过时不时轴的厉害，只能换其他AI，一起搭配着用

   [回复](#comment-131150)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2026年1月7日 13:01](https://h4ck.org.cn/2026/01/22345#comment-131157)

      ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 142](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 142") Google Chrome 142 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      有时候也挺弱智的，他是在搞不动了，我就自己搞。
      全靠 ai 行不通

      [回复](#comment-131157)
2. ![](https://gg.lang.bi/avatar/0c4f0308fe2d14897705367e365ec1eddde54de4957b3a6ec9e9562919983f38?s=64&d=identicon&r=r)

   [2026年1月7日 11:39](https://h4ck.org.cn/2026/01/22345#comment-131151)

   ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 143](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 143") Google Chrome 143 ![Windows 11](https://h4ck.org.cn/wp-cont...