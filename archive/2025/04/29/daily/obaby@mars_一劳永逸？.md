---
title: 一劳永逸？
url: https://h4ck.org.cn/2025/04/20308
source: obaby@mars
date: 2025-04-29
fetch_date: 2025-10-06T22:04:37.373368
---

# 一劳永逸？

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj), [人工智能『AI』](https://h4ck.org.cn/cats/cxsj/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E3%80%8Eai%E3%80%8F)

# 一劳永逸？

2025年4月28日
[63 条评论](https://h4ck.org.cn/2025/04/20308#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1500.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1500.jpg)

忘了是周几了，在[杜郎](https://dujun.io)![杜郎](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=mm&r=r)那里看到[《Coze扣子空间邀请码》](https://dujun.io/e91e5b25-4091-52a4-8c24-8fcf5f33ac67.html)，取了一枚邀请码注册了一下。

刚拿到的时候试了一下，发现生成效率有点低。昨天又   尝试了一下，让 coze 根据上传的图片还原生成 ui。上传的图片：

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1497-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1497.jpg)

输入的指令：

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/2A168A4494943045FFE7FBA8CB25FD71.png)](https://h4ck.org.cn/wp-content/uploads/2025/04/2A168A4494943045FFE7FBA8CB25FD71.png)

静态页面有了，那么是不是同样能够生成后端工程，然而让尝试生成后端项目的时候。表示无法生成项目，不过通过尝试创建目录和文件的方式是可以的。

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250428-095458-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250428-095458.jpg)

不过后端代码的整体效果就比较一般了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250428-095617.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250428-095617.jpg)

导入了序列化的类，但是却没有把数据序列化返回。

相对来说，前端的还原度和代码质量就要高很多，实际效果：

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/2025-04-28-09.57.45-space.coze_.cn-c3e498b4a49b-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/2025-04-28-09.57.45-space.coze_.cn-c3e498b4a49b.jpg)

页面访问地址：<https://space.coze.cn/web?uri=7497853897668313142%2F%E6%9B%B4%E6%96%B0%E5%90%8E%E7%9A%84uniapp%E8%BF%90%E5%8A%A8%E6%95%B0%E6%8D%AE%E9%A1%B5%E9%9D%A2-1d16562ed0.jsx>

整体来说扣子空间前端代码能力还是不错的，包括图片识别，页面设计等等，体验还算不错。但是对于 django 框架，实际的体验就比较一般，当然也有可能是这个框架太小众了。

附几个邀请码：

小妖精 邀请你体验扣子空间，快来和 Agent 一起开始你的工作吧！
~~https://www.coze.cn/space-preview?invite\_code=QL9FGUG1~~

~~https://www.coze.cn/space-preview?invite\_code=8UQSUMXW~~

~~https://www.coze.cn/space-preview?invite\_code=B13LD82P~~

~~https://www.coze.cn/space-preview?invite\_code=1QP96OUJ~~

~~https://www.coze.cn/space-preview?invite\_code=Y1V1I0YB~~

昨天收到联通发的消息，说要升级设备。

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1501-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1501.jpg)

不出意外，今天早上家里服务都无法访问了，看下了报了个错误。这个错误，应该是 cdn 升级之后导致的，接口变了。

```
[E] 发生错误： 请求参数错误: username为必填字段
[T] 获取到 token: None
Traceback (most recent call last):
  File "/home/obaby/dnspod-ddns/ddns.py", line 346, in <module>
    loop.run_until_complete(main())
  File "/home/obaby/dnspod-ddns/ddns.py", line 235, in main
    update_ipv4_record(current_ip)
  File "/home/obaby/dnspod-ddns/ddns.py", line 109, in update_ipv4_record
    update_domain_source(domain_list_v2, new_ip_address)
  File "/home/obaby/dnspod-ddns/baby_dunyun.py", line 248, in update_domain_source
    site_list = get_site_list(token)
  File "/home/obaby/dnspod-ddns/baby_dunyun.py", line 54, in get_site_list
    'authorization': 'Bearer ' + token,
TypeError: can only concatenate str (not "NoneType") to str
```

对于这种错误，其实没什么好的预见手段，只能出了问题再去改。

上午把错误修复了，同事改了下更新 ipv6 地址的逻辑。

就在刚刚，收到华为应用商店的短信，提示 app 被下架了了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1369.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1369.jpg)

果然跟自己预料的差不多，至于举报只是其中一部分，关键的一部分在于实名认证。但是这个实名认证真的是不怎么好办，不管哪种认证方式，都非自己所愿。就是个记录大姨妈的 app，干嘛非得实名认证，而至于 ai 生成的内容，实名认证了就不会生成敏感内容了吗？这个不应该是 ai 服务提供商来解决 ai 的问题吗？为什么要把问题转嫁给用户？

之前还说永不投降，其实啊，哪里有什么骨气？我不想收集那些用户敏感信息，对此也没兴趣。所以，对于实名认证这件事情我投降了。

至于一劳永逸？那就更不存在了，唯一的就是跟着不断的折腾，折腾，折腾。

天底下没什么免费的午餐，更没什么永葆青春的秘诀。

哪怕是再遥遥领先的高潮针，也解决不了时间的鞭挞。

**补充邀请码：**

小妖精 邀请你体验扣子空间，快来和 Agent 一起开始你的工作吧！
https://www.coze.cn/space-preview?invite\_code=O0RDW20W

https://www.coze.cn/space-preview?invite\_code=6WXD0SC0

https://www.coze.cn/space-preview?invite\_code=WLCJH5LK

https://www.coze.cn/space-preview?invite\_code=RESH9SKJ

https://www.coze.cn/space-preview?invite\_code=DLKZFGTF

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《一劳永逸？》](https://h4ck.org.cn/2025/04/20308)
\* 本文链接：<https://h4ck.org.cn/2025/04/20308>
\* 短链接：<https://oba.by/?p=20308>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[COZE](https://h4ck.org.cn/tags/coze)[扣子空间](https://h4ck.org.cn/tags/%E6%89%A3%E5%AD%90%E7%A9%BA%E9%97%B4)

[Previous Post](https://h4ck.org.cn/2025/04/20324)
[Next Post](https://h4ck.org.cn/2025/04/20289)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年11月13日

#### [从《POI》说起](https://h4ck.org.cn/2024/11/18518)

2024年11月25日

#### [莫名其妙](https://h4ck.org.cn/2024/11/18629)

2025年8月8日

#### [挣得太少](https://h4ck.org.cn/2025/08/21207)

### 63 comments

1. ![](https://gg.lang.bi/avatar/a3187abab7f61b0c43efc6d88384d1c643d359defed5874a2a3b60e979effc83?s=64&d=identicon&r=r) **[梦之源泉](http://www.mzyq.com)**说道：

   [2025年4月28日 10:53](https://h4ck.org.cn/2025/04/20308#comment-125930)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   哪怕是再遥遥领先的高潮针，也解决不了\*\*的鞭挞。

   大师，我悟了

   [回复](#comment-125930)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年4月28日 11:02](https://h4ck.org.cn/2025/04/20308#comment-125931)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      啊 这么长 你就读最后一句🤣

      [回复](#comment-125931)

      1. ![](https://gg.lang.bi/avatar/a3187abab7f61b0c43efc6d88384d1c643d359defed5874a2a3b60e979effc83?s=64&d=identicon&r=r)

         [2025年4月30日 09:31](https://h4ck.org.cn/2025/04/20308#comment-126004)

         ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

         ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-userage...