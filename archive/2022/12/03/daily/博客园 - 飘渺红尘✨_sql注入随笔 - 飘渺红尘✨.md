---
title: sql注入随笔 - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/16945048.html
source: 博客园 - 飘渺红尘✨
date: 2022-12-03
fetch_date: 2025-10-04T00:24:11.991965
---

# sql注入随笔 - 飘渺红尘✨

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [sql注入随笔](https://www.cnblogs.com/piaomiaohongchen/p/16945048.html "发布于 2022-12-02 17:15")

最近挖了一些漏洞，还挺有意思的。这边分享两个需要细节一点才能挖到的sql注入，希望给大家带来一些漏洞挖掘思路。

　　黑盒是很有意思的，有趣的。

**1.搜索功能的隐藏sql注入，post data数据内容如下:**

```
{"product":"","offer":"DIV","variant":"*","search":""}
```

　　探测的时候发现这些参数都不存在注入

![](https://img2023.cnblogs.com/blog/1090320/202212/1090320-20221202170102785-525852483.png)

　　开始第二次尝试,当删除json体中某个参数后，variant参数触发报错注入:

```
{"product":"","variant":"*","search":""}
```

　 结论:测试漏洞的时候，记得删除参数。可能某个参数起到了健全的作用。

**2.搜索功能的order by隐藏注入，post data数据包内容如下:**

```
Origin:
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer:
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8

number=0&size=10&sortField=id*&sortOrder=desc&playerUsername=&uid=
```

 对数据包进行正常发包:

![](https://img2023.cnblogs.com/blog/1090320/202212/1090320-20221202170809618-2140614462.png)

 发包返回当前搜索的所有数据。因为有sortField参数，所以我格外注意测试order by注入。这里我对每个参数进行了sql注入测试，发现并不存在order by和其他类型的sql注入。

 直觉告诉我，可能有漏洞。我想坚持fuzz下，如果我放弃了，那么一个高风险漏洞都没有了。

 fuzz参数发现当post data参数为:

```
Origin:
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer:
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8

number=0&size=10&sortField=id&sortOrder=desc&playerUsername=%25&uid=
```

　这里我为playerUsername赋值%25后，正常发包后，他的返回和上面第一个数据包的返回内容一致。

   但是这个赋值不一般，直接导致了sortField参数可以受到order by注入攻击，直接触发sql语句报错。

![](https://img2023.cnblogs.com/blog/1090320/202212/1090320-20221202171227547-1545269593.png)

  很神奇，这个点真的很神奇。也可以说是意外之喜。然后就是出数据，证明是sql注入:

![](https://img2023.cnblogs.com/blog/1090320/202212/1090320-20221202171333233-719672655.png)

　　结论:遇到敏感的参数，一定要坚持下！不然可能错过高风险安全漏洞。

* 添加到短语集
  + 没有此单词集：英语 → 中文（简体）...
  + 创建新的单词集...
* 拷贝

* 添加到短语集
  + 没有此单词集：英语 → 中文（简体）...
  + 创建新的单词集...
* 拷贝

TRANSLATE with ![]() x

English

|  |  |  |
| --- | --- | --- |
| [Arabic](#ar) | [Hebrew](#he) | [Polish](#pl) |
| [Bulgarian](#bg) | [Hindi](#hi) | [Portuguese](#pt) |
| [Catalan](#ca) | [Hmong Daw](#mww) | [Romanian](#ro) |
| [Chinese Simplified](#zh-CHS) | [Hungarian](#hu) | [Russian](#ru) |
| [Chinese Traditional](#zh-CHT) | [Indonesian](#id) | [Slovak](#sk) |
| [Czech](#cs) | [Italian](#it) | [Slovenian](#sl) |
| [Danish](#da) | [Japanese](#ja) | [Spanish](#es) |
| [Dutch](#nl) | [Klingon](#tlh) | [Swedish](#sv) |
| [English](#en) | [Korean](#ko) | [Thai](#th) |
| [Estonian](#et) | [Latvian](#lv) | [Turkish](#tr) |
| [Finnish](#fi) | [Lithuanian](#lt) | [Ukrainian](#uk) |
| [French](#fr) | [Malay](#ms) | [Urdu](#ur) |
| [German](#de) | [Maltese](#mt) | [Vietnamese](#vi) |
| [Greek](#el) | [Norwegian](#no) | [Welsh](#cy) |
| [Haitian Creole](#ht) | [Persian](#fa) |  |

![]()

[![]()](https://go.microsoft.com/?linkid=9722454 "Help") ![]() ![]()

TRANSLATE with ![]()

COPY THE URL BELOW

![]()

![]() Back

EMBED THE SNIPPET BELOW IN YOUR SITE  ![]()

Enable collaborative features and customize widget: [Bing Webmaster Portal](http://www.bing.com/widget/translator)

Back

posted @
2022-12-02 17:15
[飘渺红尘✨](https://www.cnblogs.com/piaomiaohongchen)
阅读(937)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)

Title