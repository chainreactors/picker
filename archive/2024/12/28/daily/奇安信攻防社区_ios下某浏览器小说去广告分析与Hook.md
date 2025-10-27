---
title: ios下某浏览器小说去广告分析与Hook
url: https://forum.butian.net/share/3954
source: 奇安信攻防社区
date: 2024-12-28
fetch_date: 2025-10-06T19:33:35.097426
---

# ios下某浏览器小说去广告分析与Hook

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### ios下某浏览器小说去广告分析与Hook

* [渗透测试](https://forum.butian.net/topic/47)

支持正版，从我做起，仅供学习！！

0x00 前言
=======
几年前，我在用某浏览器看小说的时候，那会就被那个广告折磨的不要不要的，想着找学（po）习（jie）版本，但是逛了一圈没有找到。那咋办，自己动手呗～～然而，那会太菜了，分析了好久都没研究出来怎么弄。。。
过了几年，我没有变得更厉害，但是我想再试试，于是有了本文。。
&gt; ps：处于学（hai）习（pa）的目的，本文只会给出核心的思路，不是那种一步步的保姆级教程，看的师傅要注意了～
0x01 最终的效果
==========
1. 去开屏广告
2. 去小说阅读广告
3. 去小说下载广告
0x02 用到的工具
==========
- MonkeyDev：<https://github.com/AloneMonkey/MonkeyDev/wiki/%E5%AE%89%E8%A3%85>
- frida：<https://frida.re/docs/examples/ios/>
- Reveal：<https://revealapp.com/>
- 越狱的iPhone
- 目标浏览器IPA，版本是15.1.7（我分析的时候是15.1.7，补图的时候是15.7.0）
0x03 开屏广告
=========
Reveal 分析一下开屏广告，发现跟 `MttSplashWindow` 有关系
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5d70839f97f7b6803a32009ae84ff93ae2ed150b.png)
用`class-dump`导出类、方法和属性，并生成相应的头文件
```bash
class-dump -H mttlite.app -o headers
```
发现了一个方法`canShowSplash`很可疑：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-057f77c448c65cbd063ed5f1905283e5584f3a9d.png)
MonkeyDev 直接hook之，让其返回`false`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a550b9e4d79792e5f5bacb59d6de9b3ee773a535.png)
so easy～～
0x04 阅读广告
=========
在看小说的时候，想要无广告，就得开会员
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fe9d68f172911f09f4fba62a0c36c5530a4c99d5.png)
这里提取到关键词“\*\*悦读卡\*\*”
用vscode，打开刚刚的MonkeyDev项目的，下图的路径
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8dbc01782791ee01e12e33911c03c3457761c306.png)
开搜
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8b46c8a4cc208711d6310a23129b3002ee655280.png)
可以看到大部分跟 `mttlite.app/res/rn/novelReader` 有关，盲猜这玩意就是我们看小说的页面
&gt; 其实测试很简单，随便找个关键词改改，编译运行一下，就知道就是这里了
那接下来的操作其实很简单了，分析一下js代码。我从`2.ios.jsbundle`的第一个地方`悦读卡已生效`出发
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2d7ac74b13246af1d2d9747c764a4bf91ea786a4.png)
往上看看，可以看到`isVipUser`和`expireTime`的变量
![Code 2024-11-19 22.23.33.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1d493197f15c0819e71665973c7ac91a0b8975ce.png)
秉承着大胆猜测小心验证的原则，我把`2.ios.jsbundle`这个文件中，所有涉及这两个变量的地方，都改成如下：
```javascript
{
isVipUser: 1,
expireTime: new Date('2099-01-01T00:00:00Z').getTime(),
}
```
我一共改了三处，第一处：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9b630801018bdc613227b21c56a125c509b353e7.png)
第二处：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-eecde83e28280b17d3513ee100c70c12be141ee6.png)
第三处：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-937232824cc0e70878f51be94f5590ffaca69a3b.png)
改完，保存文件，MonkeyDev项目重新编译到手机上，框框刷小说，没广告了，稳如狗～
0x05 下载广告
=========
从 `clickDownloadButton` 入手
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-747e124c9c82062c6ec3bae6fb2599af9236c056.png)
简单分析一下这个函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e9c62ffce5e3d4193e8951a79758bce8fc55c0bb.png)
那么修改思路也很清晰了，直接把原来的`case 22`注释掉，放到`case 12`上面，如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ac9c872a41e080f7fbcbd44dbc43ac8bce3870b1.png)
改完，保存文件，MonkeyDev项目重新编译到手机上，点击下载，也没有广告了，稳！
0x06 开心的太早了
===========
如题，正当我以为结束的时候，开开心心看小说的时候，好家伙，没过两分钟，广告又出来了。。。
思考一件事情，文件是 jsbundle，然后还能动态更新，百度一下，发现这篇文章：[https://blog.csdn.net/xu\\_song/article/details/53286996](https://blog.csdn.net/xu\_song/article/details/53286996)
开搞，上frida
```bash
frida-trace -U -m "\*[\* \*BundleVersion\*]" -f com.example.QQLiu
```
一直刷小说，直到发现出现了广告，即更新了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1b47fd63099c7faa6e478f850fb5df0e523baf5f.png)
hook之，发现还是不行
直接hook所有跟version有关的
```bash
frida-trace -U -m "\*[\* \*Version\*]" -f com.example.QQLiu
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-255c0162a9b15a5391e4413e76eb73c09c2fe246.png)
看一下头文件，感觉都挺可疑的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-dc5f3f1e183468d777b5635c33ed66832beb1d10.png)
看看是哪个`updateRes`方法
```bash
frida-trace -U -m "\*[\* \*updateRes\*]" -M "-[UIImageView \_updateResolvedImage]" -M " -[\_UINavigationBarLargeTitleViewLayout updateRestingTitleHeight]" -f com.example.QQLiu
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-68fd5bd21aa02d009c0f2236f9b5b357c0d9ef84.png)
掏空它
```ObjectC
// See http://iphonedevwiki.net/index.php/Logos
#import
@interface MttSplashWindow : UIWindow
+ (\_Bool)canShowSplash;
@end
%hook MttSplashWindow
+ (\_Bool)canShowSplash{
%orig;
NSLog(@"[+] hook: canShowSplash 返回false");
return false;
}
%end
%hook ResHubLocalResManager
- (void)updateResWithConfig:(id)arg1 taskId:(id)arg2 mode:(id)arg3{
NSLog(@"[+] hook: updateResWithConfig 掏空");
}
%end
```
掏空之后，书架显示不了了，得看看这三个参数都是啥，方向没问题，关键是不能全hook，得根据参数判断来hook
xcode打个断点， 查看参数，发现 `\_sourceRelativeLocalPath`有点可疑
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3e317186045a1078ff4155e6adc583982ed6bbac.png)
```ObjectC
%hook ResHubLocalResManager
- (void)updateResWithConfig:(id)arg1 taskId:(id)arg2 mode:(id)arg3{
NSString \*sourceRelativeLocalPath = [arg1 valueForKey:@"\_sourceRelativeLocalPath"];
NSLog(@"[+] \_sourceRelativeLocalPath: %@",sourceRelativeLocalPath);
%orig;
}
%end
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-65f95e3742dec37658d6ab3213ed8fbaefb447b7.png)
猜测`novelReader\_1337.zip`有关系，只干掉它试试，因为vip的判断都是这个novelReader关键词
> 最新的版本`15.7.0.6057`，这里已经变成 `novelReader\_1519.zip` 了
> ![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-428c1bcd438f2e7c71135d74146b9022956c6d39.png)
> ![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-af5ab13356bc79aed2bfd200b7e679cdf3972270.png)
```ObjectC
%hook ResHubLocalResManager
- (void)updateResWithConfig:(id)arg1 taskId:(id)arg2 mode:(id)arg3{
// %orig;
NSString \*sourceRelativeLocalPath = [arg1 valueForKey:@"\_sourceRelativeLocalPath"];
if ([sourceRelativeLocalPath containsString:@"novelReader"]) {
NSLog(@"[+] hook: updateResWithConfig 掏空");
NSLog(@"[+] \_sourceRelativeLocalPath: %@", sourceRelativeLocalPath);
} else {
%orig;
}
}
%end
```
编译运行，终于稳了，不容易啊。。
0x07 完整的hook代码
==============
```ObjectC
// See http://iphonedevwiki.net/index.php/Logos
#import
@interface MttSplashWindow : UIWindow
+ (\_Bool)canShowSplash;
@end
%hook MttSplashWindow
+ (\_Bool)canShowSplash{
%orig;
NSLog(@"[+] hook: canShowSplash 返回false");
return false;
}
%end
%hook ResHubLocalResManager
- (void)updateResWithConfig:(id)arg1 taskId:(id)arg2 mode:(id)arg3{
// %orig;
NSString \*sourceRelativeLocalPath = [arg1 valueForKey:@"\_sourceRelativeLocalPath"];
if ([sourceRelativeLocalPath containsString:@"novelReader"]) {
NSLog(@"[+] hook: updateResWithConfig 掏空");
NSLog(@"[+] \_sourceRelativeLocalPath: %@", sourceRelativeLocalPath);
} else {
%orig;
}
}
%end
```
0x08 后言
=======
还是那句话，不会提供成品，仅供学习使用！！！支持正版，从我做起，仅供学习！！

* 发表于 2024-12-27 09:00:02
* 阅读 ( 3029 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

2 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![江小虫儿](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/6722)

[江小虫儿](https://forum.butian.net/people/6722)

2 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitem...