---
title: 记一次web登录通杀渗透测试 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16915458.html
source: 博客园 - 渗透测试中心
date: 2022-11-23
fetch_date: 2025-10-03T23:29:55.752351
---

# 记一次web登录通杀渗透测试 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [记一次web登录通杀渗透测试](https://www.cnblogs.com/backlion/p/16915458.html "发布于 2022-11-22 16:12")

在渗透测试过程中，碰见的web登录页面特别多，那么我们应该用什么样的思路去进行一个测试呢，下面看看我的一些测试师思路ba

---

**测试思路**

当看见一个这样的web登录框时，会怎么样进行一个渗透呢

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161144125-937896601.jpg)

**弱口令**

我们可以看见 这个登录时并没有存在一个验证码，就会存在一个爆破问题 那么一般爆破的用户名又会存在那些呢

1.admin
2.test
3.root

这里也可以去查找对应系统的的操作手测，收集管理账号，增加爆破机率

在这里进行了爆破，并没有结果

---

**目录扫描**

我们可以去扫描目录 可能一些被扫描出来的目录未做鉴权 可直接访问

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161144975-43469940.png)

---

**JS文件未授权**

上面方法都无果后，我们接下来去看下JS文件

发现在index.js中存在一个/SystemMng/Index的url

我们尝试拼接访问

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161145762-648547022.jpg)

拼接进来后 发现什么都没有 是不是准备放弃了

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161146563-1851357490.jpg)

别急 我们再看看JS 是不是发现惊喜了

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161147284-1744435551.jpg)

拼接几个危害都挺大的 拿个可以继续利用的给大家

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161147977-1570743273.jpg)

---

**组合拳弱口令爆破**

到这里我们拿到了管理员的账号以及电话了，也可以直接重置他们密码了（拿正确的账号再去尝试爆破）

可以看见 password被加密了 发现为m5 我们利用burp自带的转码爆破即可

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161148870-450547764.jpg)

爆破成功 账号比较复杂 在没前面的操作下拿不到用户名

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161149626-1906501501.jpg)

登录成功

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161150320-470810085.jpg)

---

**登录返回包测试**

随意输入登录的账号密码登录抓包

修改他的鉴权数据后

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161151069-1570905541.jpg)

修改后发现跳转的还无数据 JS中还是存在泄露

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161151786-761786982.jpg)

利用方法一样

---

**越权**

现在已经拿到了普通用户的账号密码了，那我们后面应该去尝试一个越权 垂直越权 或者 平行越权

拿爆破的号进行登录抓包处理，这个地方师傅们在挖掘的时候可以多看几遍数据包以及返回包

开始在构造时 以为是校验ID 后面多测试几轮下来，发现只会去识别code参数

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161152477-1992148335.jpg)

从未授权到拿到网站的所有权限

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221122161153290-648200404.jpg)

原文连接： <https://xz.aliyun.com/t/11612>

posted @
2022-11-22 16:12
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(756)
评论(1)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025