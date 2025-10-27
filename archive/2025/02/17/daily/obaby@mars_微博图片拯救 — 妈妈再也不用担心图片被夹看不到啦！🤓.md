---
title: 微博图片拯救 — 妈妈再也不用担心图片被夹看不到啦！🤓
url: https://h4ck.org.cn/2025/02/19296
source: obaby@mars
date: 2025-02-17
fetch_date: 2025-10-06T20:33:24.183749
---

# 微博图片拯救 — 妈妈再也不用担心图片被夹看不到啦！🤓

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

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [破解/汇编『Crack/Asm』](https://h4ck.org.cn/cats/crackasm)

# 微博图片拯救 — 妈妈再也不用担心图片被夹看不到啦！🤓

2025年2月16日
[30 条评论](https://h4ck.org.cn/2025/02/19296#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/A2I2387_extend-tuya-scaled.webp)](https://h4ck.org.cn/wp-content/uploads/2025/02/A2I2387_extend-tuya.webp)

过了这好几年之后，总感觉自己已经从一个技术博主，变成了一个生活博主。

年龄越来越大了之后，探索能力，学习能力逐渐的下降。接受新事物的能力也日渐式微，总感觉想做一些东西而力不从心。

很多东西多年以前就知道了，但是想自己去做的时候却总感觉没什么头绪，不知道该从哪里开始。

今天又看到教主转的微博，同样原内容图片被夹了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-184919.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-184919.png)

教主发的那个这就发挥作用了，是一张截图：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/微信图片_20250216184251.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250216184251.png)

这么个东西。

至于原理，很久之前教主就大概提过，说出来也简单，就是利用cdn的缓存删除时间差，在节点未删除之前遍历所有的cdn节点去搜索图片。知道原理之后，要实现也简单，目前微博图片主要有四个域名+两个alias：

```
weibo_cdn_domain_list = [
    'wx1.sinaimg.cn',
    'wx2.sinaimg.cn',
    'wx3.sinaimg.cn',
    'wx4.sinaimg.cn',
    'weiboimgwx.gslb.sinaedge.com',
    'weiboimgwx.grid.sinaedge.com'
]
```

既然有了域名，那么也简单，通过python库直接解析所有的地址即可：

```
def get_ipv4_ips(domain_name):
    try:
        ipv4_addresses = []
        answers = dr.resolve(domain_name, "A")
        for rdata in answers:
            if str(rdata).startswith("192."):
                continue
            else:
                ipv4_addresses.append(str(rdata))
        return ipv4_addresses
    except Exception as e:
        print(e)
        return None

def get_ipv6_ips(domain_name):
    try:
        ipv6_addresses = []
        answers = dr.resolve(domain_name, "AAAA")
        for rdata in answers:
            if str(rdata).startswith("::"):
                continue
            else:
                ipv6_addresses.append(str(rdata))
        return ipv6_addresses
    except Exception as e:
        print(e)
        return None

def get_all_ips():
    ip_dict_list = []

    for domain in weibo_cdn_domain_list:
        ips = get_ipv4_ips(domain)
        v6_ips = get_ipv6_ips(domain)
        print(domain, ips)
        domain_ips = {
            'domain': domain,
            'ipv4': ips,
            'ipv6': v6_ips
        }
        ip_dict_list.append(domain_ips)
    return ip_dict_list
```

然而，这么高却也存在问题，就是拿到的ip地址都是国内解析到的，与命令查询到的一致：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-185216.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-185216.png)

四个域名加起来不多几十个ip地址，然而，仔细观察教主的图片会发现，解析出来的ip大约有2000+按照图片进度猜测。

即使加上ipv6的也远远少于教主的ip地址数量。

并且尝试下载的时候全部失败了，无法遍历到删除的文件，再次查看教主的图片，搜了下ip地址，并不是国内的：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-204342.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-204342.png)

那么，可能的原因在于，教主拿到了所有的ip地址，包括海外的，并且海外节点的删除时间会更晚，这样能找到被夹的图片的概率自然也越大。

那么直接去itdog.cn拉取所有的ip地址列表：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-204534.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-204534.png)

一个域名对应800+ip地址，那么这么看来基本跟教主的数量就能对上了。剩下的就简单了，告知思路，剩下的大家可以自由发挥了，主要代码可以暂停录像看屏幕代码：

```
1.将所有的域名解析为ip
2.讲ip与域名组装为：
domain_ips = {
            'domain': domain,
            'ipv4': ips,
            'ipv6': v6_ips
        }
格式。
3.遍历域名下的所有ip地址，拼接请求链接指定host。
4.针对请求数据进行处理，目前已知默认的占位符图片长度为：6067, 8308, 8844这几个，对于返回长度10000以下的，可以直接抛弃掉。
5.请求到数据之后保存为文件即可。
```

效果图：

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-193604.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/Screenshot-2025-02-16-193604.png)

视频演示：
﻿

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《微博图片拯救 — 妈妈再也不用担心图片被夹看不到啦！🤓》](https://h4ck.org.cn/2025/02/19296)
\* 本文链接：<https://h4ck.org.cn/2025/02/19296>
\* 短链接：<https://oba.by/?p=19296>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Python](https://h4ck.org.cn/tags/python)[Python3](https://h4ck.org.cn/tags/python3)[图片](https://h4ck.org.cn/tags/%E5%9B%BE%E7%89%87)[微博](https://h4ck.org.cn/tags/%E5%BE%AE%E5%8D%9A)

[Previous Post](https://h4ck.org.cn/2025/02/19307)
[Next Post](https://h4ck.org.cn/2025/02/19271)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年1月7日

#### [DeIDA Package 1.4](https://h4ck.org.cn/2013/01/4907)

2023年4月16日

#### [requests SSLCertVerificationError](https://h4ck.org.cn/2023/04/11847)

2025年8月8日

#### [数独求解工具](https://h4ck.org.cn/2025/08/21136)

### 30 comments

1. ![](https://gg.lang.bi/avatar/e82222af6a5616ec24ae02e0eaa8ceacadef6fd83873a62c639eefd4cf7be8b6?s=64&d=identicon&r=r) **[沉沦](https://kkn.me)**说道：

   [2025年2月16日 21:35](https://h4ck.org.cn/2025/02/19296#comment-123767)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Safari 18](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 18") Safari 18 ![iPad iOS 18.3.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/ipad.png "iPad iOS 18.3.1") iPad iOS 18.3.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   有文字，有图，又有视频。就是看不懂😂

   [回复](#comment-123767)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年2月16日 21:36](https://h4ck.org.cn/2025/02/19296#comment-123768)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      为了解决之前念叨了很久的事情。

      [回复](#comment-123768)
2. ![](https://gg.lang.bi/avatar/c9b84eca89169750a7bb00740aea5786adbd48bcaaeed2393f4bef6a5adc1857?s=64&d=identicon&r=r)

   [2025年2月16日 22:52](https://h4ck.org.cn/2025/02/19296#comment-123769)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![QQbrowser 13](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/qqbrowser.png "QQbrowser 13") QQbrowser 13 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   已经很多年没碰微博了，现在大部分时间都被小说、短视频和内耗占据，剩下的10%用来睡觉。 ![sad](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/sad.gif)

   [回复](#comment-123769)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年2月17日 08:42](https://h4ck.org.cn/2025/02/19296#comment-123774)...