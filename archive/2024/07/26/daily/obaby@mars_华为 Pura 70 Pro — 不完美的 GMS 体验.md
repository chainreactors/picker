---
title: 华为 Pura 70 Pro — 不完美的 GMS 体验
url: https://h4ck.org.cn/2024/07/17727
source: obaby@mars
date: 2024-07-26
fetch_date: 2025-10-06T17:42:01.610857
---

# 华为 Pura 70 Pro — 不完美的 GMS 体验

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 华为 Pura 70 Pro — 不完美的 GMS 体验

2024年7月25日
[71 条评论](https://h4ck.org.cn/2024/07/17727#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG1063.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG1063.jpg)

上周出去旅游的时候，19 年买的华为 p30p 终于坚持不住了。牺牲在了导航的前线上，在到达目的地之后也锁不了车了。之前屡次也想过换手机的问题，但是毕竟它还能用，也没什么理由换啊，也不用手机玩大型游戏。最多就玩个消消乐，当然换华为的另外一个原因跟目前用的华为的手表也有关系。

自从上次过生日买 mac mini 的时候发现，二手东的同城配送也蛮好用的，下单之后两个小时内就送到了，不得不说，这个效率的确杠杠的。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/4721721875232_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/4721721875232_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2024/07/4731721875298_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/4731721875298_.pic_.jpg)

五年时间，价格有提高，当然，配置也有提高。这个至于性价比到底如何，其实我也不知道。选择华为的另外一个原因，就是感觉用着也还行吧，没有那么烂。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/10561721875916_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/10561721875916_.pic_.jpg)  [![](https://h4ck.org.cn/wp-content/uploads/2024/07/10591721875919_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/10591721875919_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2024/07/10601721875920_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/10601721875920_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2024/07/10611721875921_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/10611721875921_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2024/07/10621721875922_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/10621721875922_.pic_.jpg)

不过不得不说这个数据同步并不会同步所有的数据，关键性的 google 的框架 、play store 等都不会同步，这就有点尴尬了。

安装 apkpure 之后，通过 apkpure 安装 gms 框架以及 store 发现并不能用。这就让人有些尴尬了，想着之前 p30 上的商店是好用的。只好通过adb 导出 apk 进行安装。

1.列出 apk 列表

```
adb shell pm list packages
```

2.获取 apk 文件路径

```
D:\HuaWei_STB\adb>adb shell pm path com.google.android.gms
package:/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/base.apk
package:/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/split_config.en.apk
package:/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/split_config.xxhdpi.apk
package:/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/split_config.zh.apk
```

3.拉取 apk

```
D:\HuaWei_STB\adb>adb pull /data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/base.apk D:\HuaWei_STB\adb\base.apk

/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/....apk: 1 file pulled. 40.3 MB/s (140967559 bytes in 3.333s)

D:\HuaWei_STB\adb>adb pull /data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/split_config.en.apk D:\HuaWei_STB\adb\split_config.en.apk
/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/....en.apk: 1 file pulled. 29.2 MB/s (881049 bytes in 0.029s)

D:\HuaWei_STB\adb>adb pull /data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/split_config.xxhdpi.apk D:\HuaWei_STB\adb\split_config.xxhdpi.apk
/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/...pi.apk: 1 file pulled. 34.6 MB/s (1806280 bytes in 0.050s)

D:\HuaWei_STB\adb>adb pull /data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/split_config.zh.apk D:\HuaWei_STB\adb\split_config.zh.apk
/data/app/com.google.android.gms-Ee965jN8xgYRemYmu52cxQ==/...zh.apk: 1 file pulled. 36.3 MB/s (1831321 bytes in 0.048s)

D:\HuaWei_STB\adb>adb shell pm path com.google.android.gsf
package:/system/product/priv-app/GoogleServicesFramework/GoogleServicesFramework.apk
```

4.链接新设备安装：

```
adb install-multiple base.apk split_config.en.apk split_config.xxhdpi.apk split_config.zh.apk
```

基本安装完这个之后，依赖 gms 的 apk 就可以运行了，同样可以尝试安装 play store 等，不过我安装后一直闪退，具体原因也不清楚。

最起码奇妙庄园能运行了，不再提示依赖服务不存在。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG474-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG474.jpg)

google 的一些其他的 app 也可以安装，但是登录google账号的时候还有问题，目前还不知道怎么解决，如果要想更简单的一点，还是直接安装 gbox 吧，简单 粗暴。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/4751721877349_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/4751721877349_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2024/07/4761721877351_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/4761721877351_.pic_.jpg)

apk 下载地址：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《华为 Pura 70 Pro — 不完美的 GMS 体验》](https://h4ck.org.cn/2024/07/17727)
\* 本文链接：<https://h4ck.org.cn/2024/07/17727>
\* 短链接：<https://oba.by/?p=17727>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[gms](https://h4ck.org.cn/tags/gms)[Google](https://h4ck.org.cn/tags/google)[华为 Pura70](https://h4ck.org.cn/tags/%E5%8D%8E%E4%B8%BA-pura70)

[Previous Post](https://h4ck.org.cn/2024/07/17742)
[Next Post](https://h4ck.org.cn/2024/07/17702)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年2月10日

#### [祝大家新年快乐](https://h4ck.org.cn/2024/02/15438)

2009年12月4日

#### [黑鹰安全网 黑客又秀逗了~](https://h4ck.org.cn/2009/12/791)

2025年3月25日

#### [vivaldi 同步失败](https://h4ck.org.cn/2025/03/19944)

### 71 comments

1. ![](https://gg.lang.bi/avatar/c44d885e47f3366e1926898246ecc70fc950b80314f34861521a7bad7b7af49c?s=64&d=identicon&r=r) **[w4j1e](https://hin.cool)**说道：

   [2024年7月25日 11:50](https://h4ck.org.cn/2024/07/17727#comment-117609)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 126") Microsoft Edge 126 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   淘汰的手机不要丢，可以拿到我这换不锈钢盆 ![laugh](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh.gif)

   [回复](#comment-117609)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年7月25日 13:18](https://h4ck.org.cn/2024/07/17727#comment-117611)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      你这盆，保真吗？嘻嘻

      [回复](#comment-117611)

      1. ![](https://gg.lang.bi/avatar/8a012e16bd9362f5813bc8e7dea51352a5f457dbc97c15599931ba3598920472?s=64&d=identicon&r=r)

         [2024年7月26日 09:36](https://h4ck.org.cn/2024/07/17727#comment-117677)

         ![Level 4](https://badgen.net/badge/亲...