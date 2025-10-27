---
title: Smartbi 最新漏洞+后利用打入内存马(手把手叫你如何仅仅从漏洞消息到分析 0day)
url: https://forum.butian.net/share/4537
source: 奇安信攻防社区
date: 2025-08-30
fetch_date: 2025-10-07T00:12:37.508353
---

# Smartbi 最新漏洞+后利用打入内存马(手把手叫你如何仅仅从漏洞消息到分析 0day)

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

### Smartbi 最新漏洞+后利用打入内存马(手把手叫你如何仅仅从漏洞消息到分析 0day)

* [漏洞分析](https://forum.butian.net/topic/48)

又一个前台未授权漏洞爆了出来，而且纵观 Smartbi 的历史漏洞，都是未授权漏洞，看到各个乙方公司的公众号都发了这个漏洞，但是没有一个有分析过程的，也只是一个calc就下播，于是前来分析一手

Smartbi 最新漏洞+后利用打入内存马(手把手叫你如何仅仅从漏洞消息到分析 0day)
=============================================
前言
--
\*\*文章中涉及的敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担\*\*
又一个前台未授权漏洞爆了出来，而且纵观 Smartbi 的历史漏洞，都是未授权漏洞，看到各个乙方公司的公众号都发了这个漏洞
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820150803.png "null")
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820150822.png "null")
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820150834.png "null")
但是没有一个是有 POC 的
那咋办嘛，只能自己分析咯
环境搭建
----
没有源码的可以去访问官网
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820151138.png "null")
直接申请使用，可以免费体验一个月，不过分析这个漏洞完全够用了
下载下来启动
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820151721.png "null")
启动成功后访问环境即可，这个就很爽，无脑起飞，如果需要调试的话，可以在启动里面加参数，不过也不需要
启动后访问 config.jsp
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820152117.png "null")
配置后检测一下成功后就去访问 index
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820152153.png "null")
登录后如图，代表访问成功
但是这个是最新版本的，我们只需要把去加载老版本的 patch，把新的给替代了就 ok
在系统监控那里
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820160803.png "null")
分析思路
----
当然没有思路，只能从几家的漏洞描述+补丁分析了
先去搞一手补丁
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820152613.png "null")
就是这个最新的补丁，早就修复了，但是现在才爆出来
但是这种补丁一般都会加密的
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820152729.png "null")
读不了一点
因为打补丁就是使用的这个文件，所以肯定有解密的流程，去寻找一下
参考<https://zone.huoxian.cn/d/2825-smartbi>
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820155616.png "null")
解密得到一个 zip 文件，解压后得到明文的 patch 文件和一些更新后的 class 文件
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820155642.png "null")
然后我们得到解密的结果
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820154930.png "null")
然后加上我们的 class 文件，大概都去看一下
然后加上乙方的一些描述，之后定位到代码
漏洞的根本原因在于系统权限验证机制存在缺陷，攻击者可以通过特定的资源 ID 绕过身份验证，获取公共用户权限。
然后这时候因为对这个系统不了解，直接去搜索
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820160348.png "null")
参考[https://wiki.smartbi.com.cn/pages/viewpage.action?smt\\_poid=43&amp;pageId=51942608](https://wiki.smartbi.com.cn/pages/viewpage.action?smt\_poid=43&pageId=51942608)
然后找到了资源 ID 就是这玩意
```php
http://localhost:18080/smartbi/vision/createresource.jsp?restype=themewizard&resid=THEME.demo2019.CSAC
```
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820160447.png "null")
结合我们的补丁
发现漏洞应该是出现在 share.jsp 文件了
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820160606.png "null")
代码中也接收 resid 这个参数
然后尝试能不能未授权访问这个接口
先退出登录
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820160857.png "null")
然后访问接口
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820161058.png "null")
访问成功了
然后看到
漏洞分析与利用
-------
### 未授权获取 cookie
然后根据漏洞的描述，有默认的 id，可以返回 cookie，于是接下来的任务就是去寻找 resid
但是这个数据库是内置的，表的结构我们都不太清楚
所以需要先去尝试插入一个 id，看看到哪里去了
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820161317.png "null")
成功后查看属性
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250821110036.png "null")
得到 ID
然后去数据库找这个 ID 是在哪里
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250821172639.png "null")
发现了这个字段，然后就把其中的 resid 全部提取出来，然后去遍历
遍历后无一例外显示全是
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820161649.png "null")
找不到分享记录
如果不熟悉细怎么办？
当然是去翻我们的官方文档了
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820161956.png "null")
然后来到界面是空的，反应过来应该是每个资源都可以分享，于是回到自己创建的资源
然后点击分享
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820162052.png "null")
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250820162101.png "null")
这里我没有找到默认的资源 ID
分享成功后我再次使用我的接口去访问
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250821171726.png "null")
访问成功后我们拿着返回的 cookie 后就可以去访问接口了
### 代码原理分析
为什么这个 cookie 有效果呢
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250822101103.png "null")
可以看到只要我们成功访问资源，就会把当前用户切换为 public 用户
跟进 autoLoginByPublicUser
```php
public boolean autoLoginByPublicUser() {
String userName = "public";
if (this.getUserByName(userName) == null) {
return false;
} else {
if (this.stateModule.getSystemId() == null) {
this.stateModule.setSystemId("DEFAULT\_SYS");
}
IUser serviceUser = this.getUserById("SERVICE");
if (serviceUser == null) {
throw (new SmartbiException(UserManagerErrorCode.NOT\_EXIST\_USER)).setDetail("SERVICE");
} else if (this.stateModule.getCurrentUser() != null && this.stateModule.getCurrentUser().getId() == "PUBLIC") {
return true;
} else {
this.stateModule.setCurrentUser(serviceUser);
this.stateModule.removeSessionAttribute("SMARTBIX\_STATE");
return this.switchUser(userName);
}
}
}
```
这里就直接设定用户了，然后跟进 setCurrentUser
```php
public void setCurrentUser(IUser user) {
this.getState().setUser(user);
this.setSessionAttribute("user", user == null ? null : user.getName());
this.updateSessionLocale(user);
}
```
很明显了
```php
private void updateSessionLocale(IUser user) {
String key = "BOF\_Locale";
HttpServletRequest req = this.getRequest();
if (user != null && req != null) {
if (CommonUtil.getInstance().getLocaleByRequestParameter(req) == null && CommonUtil.getInstance().getLocaleByCookie(req) == null) {
String userLocale = null;
try {
userLocale = CommonUtil.getConfigValue("USER\_LOCALE");
} catch (Exception var6) {
}
if (!StringUtil.isNullOrEmpty(userLocale)) {
Locale locale = CommonUtil.getLocaleType(userLocale);
if (locale != null && !locale.toString().equals(this.getSessionAttribute(key))) {
this.setSessionAttribute(key, locale.toString());
}
}
}
}
}
```
这里会直接设置我们有效的 cookie
这就是我们有效的 cookie 呢
### 进入后台 RCE
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-f08414bc3c6ccb930db94f1563bcca60a65acd6f.png)
这个就是一个历史后台 RCE漏洞
后渗透利用
-----
### 回显构造
当然如果目标不出网怎么办？
所以就需要后渗透的利用了，直接去对应后台的地方
第一想法就是利用 scanner 回显
就是直接把我们命令执行的输出然后放入 scanner 对象，最后输出
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-c24279adba81505d2681fab60f47b02b7b8eb612.png)
但是发现回显的话只会显示这种提示信息，于是想到了使用 header 回显
但是个人觉得这样太麻烦了，思考了一下，我直接让这个页面报错不就完事了吗
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-089d4d842a545e5eab8128e12e48c065d917649a.png)
可以发现回显虽然没有我们的命令执行结果
但是思考一个问题，如果我们把这个 asdsd 换成我们的命令执行结果不就可以回显了吗
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250821182524.png "null")
### 注入内存马
当然一个简单的回显并不如内存马方便了，这里直接打上渗透测试最爱的内存马
借助 spring 的工具类的反射功能，首先获取到我们的关键的类，也就是当前线程的 loader，准备去加载我们的字节码，但是字节码传入的话是二进制，所以我们需要使用 base64，方便传入
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250822095532.png "null")
![](https://gitee.com/nn0nkey/picture/raw/master/img/20250822095549.png "null")
最后
--
\*\*文章中涉及的敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担\*\*

* 发表于 2025-08-29 14:28:02
* 阅读 ( 3332 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

2 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![nn0nkeyk1n9](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/35515)

[nn0nkeyk1n9](https://forum.butian.net/people/35515)

7 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2...