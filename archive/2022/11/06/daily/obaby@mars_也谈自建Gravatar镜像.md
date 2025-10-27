---
title: 也谈自建Gravatar镜像
url: https://h4ck.org.cn/2022/11/%e4%b9%9f%e8%b0%88%e8%87%aa%e5%bb%bagravatar/
source: obaby@mars
date: 2022-11-06
fetch_date: 2025-10-03T21:49:05.165745
---

# 也谈自建Gravatar镜像

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 也谈自建Gravatar镜像

2022年11月5日
[6 条评论](https://h4ck.org.cn/2022/11/10659#comments)

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/66fbb4d7fa35a3c7788cfbf5537f481b.jpg)

随便搜一下，网上搭建gravatar镜像的文章还是挺多的，基本都是基于cdn溯源来做的。当然，国内也有很多其他的镜像服务器，例如cravatar.cn loli.net等。常用额基本就是下面这几个：

|  |  |
| --- | --- |
| V2EX | [https://cdn.v2ex.com/gravatar/](https://link.zhihu.com/?target=https%3A//cdn.v2ex.com/gravatar/) |
| 极客族 | [https://sdn.geekzu.org/avatar/](https://link.zhihu.com/?target=https%3A//sdn.geekzu.org/avatar/) |
| loli | [https://gravatar.loli.net/avatar/](https://link.zhihu.com/?target=https%3A//gravatar.loli.net/avatar/) |
| inwao | [https://gravatar.inwao.com/avat](https://link.zhihu.com/?target=https%3A//gravatar.inwao.com/avatar/) |

cravatar貌似系统也在不断地更新：

> Cravatar 完美兼容所有 Gravatar 头像 API 接口，同时如果你未在 Cravatar 设置头像，则会先尝试调用 Gravatar 上的头像数据，其后是 QQ 头像，最后会返回我们为你准备的一组默认头像。

> 特别地：我们会对所有头像进行人工审核（也包括来自 Gravatar 和 QQ 的头像），所有包含暴恐、色情、政治等违反中国法律的内容都会被屏蔽，并返回默认头像。

虽然兼容所有的api，但是并没有分级功能。

本来想免费薅羊毛弄一台甲骨文的服务器做nginx代理转发用，但是没成功，提示没有可用资源了。于是就想着用oss来做代理，这个想法其实也是由来已久，不过一直没有实施。最近弄了个nai.dog的域名，于是就在这个域名下面建了个镜像代理（不完美，这个最后说）。

测试头像：https://gravatar.nai.dog/avatar/3a78942c4ddcda86242f20abdacee082?s=50&d=mm&r=g

1.创建一个bucket（区域选择香港），设置为公共读。设置回源选项：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105121439.jpg)

回源地址选择一个gravatar的服务器地址即可。需要说明的是回源参数，如果选择携带请求字符串那么会缓存指定大小的图片。我所我把这个参数给去掉了，默认缓存80\*80的图片。

2.设置生命周期，选择一段时间后自动删除：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105121723.jpg)

目前设置的是2天后自动删除，所以在gravatar更新头像两天之后才能刷新头像。

3.设置域名<https://gravatar.nai.dog/>：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105121856.jpg)

4.设置ssh证书https://yundun.console.aliyun.com/?p=cas#/certExtend/free：

目前阿里云每年有20个免费证书的额度，直接申请审核（大约10分钟）通过之后即可在oss上自动部署：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105122053.jpg)

现在就可以使用自建服务了：

```
https://gravatar.nai.dog/avatar/3a78942c4ddcda86242f20abdacee082?s=50&d=mm&r=g
https://gravatar.nai.dog/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=32&d=mm&r=g
https://cravatar.cn/avatar/81b9805653d1169927583574d835691b?s=32&d=mm&r=g
```

已知问题：

1、标准的gravatar参数无效s=50&d=mm&r=g。oss是根据文件名缓存，所以不会带参数属性

2、返回的图片大小默认为80\*80，所以需要页面设置图像大小。否则会出现问题。

替换wp默认gravatar服务器地址代码：

```
if ( ! function_exists( 'get_cravatar_url' ) ) {
    /**
     * 替换 Gravatar 头像为 Cravatar 头像
     */
    function get_cravatar_url( $url ) {
        $sources = array(
            'www.gravatar.com',
            '0.gravatar.com',
            '1.gravatar.com',
            '2.gravatar.com',
            'secure.gravatar.com',
            'cn.gravatar.com',
            'gravatar.com',
        );
        return str_replace( $sources, 'gravatar.nai.dog', $url );
    }
    add_filter( 'um_user_avatar_url_filter', 'get_cravatar_url', 1 );
    add_filter( 'bp_gravatar_url', 'get_cravatar_url', 1 );
    add_filter( 'get_avatar_url', 'get_cravatar_url', 1 );
}
```

实际效果：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221105122749.jpg)

服务器地址：

https://gravatar.nai.dog/

欢迎测试~~~

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《也谈自建Gravatar镜像》](https://h4ck.org.cn/2022/11/10659)
\* 本文链接：<https://h4ck.org.cn/2022/11/10659>
\* 短链接：<https://oba.by/?p=10659>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Cravatar](https://h4ck.org.cn/tags/cravatar)[Gravatar](https://h4ck.org.cn/tags/gravatar)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2022/11/10671)
[Next Post](https://h4ck.org.cn/2022/11/10651)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年4月6日

#### [博客再次彻底完蛋](https://h4ck.org.cn/2013/04/5073)

2016年5月19日

#### [Apache2 Django {“detail”:”Authentication credentials were not provided.”}](https://h4ck.org.cn/2016/05/5892)

2024年3月16日

#### [再谈 WordPress 的速度优化 — 优化插件真的是提速的吗？](https://h4ck.org.cn/2024/03/15874)

### 6 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月5日 13:41](https://h4ck.org.cn/2022/11/10659#comment-88568)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1") iPhone iOS 16.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这个开放给别人用的话，就是流量扛不住

   [回复](#comment-88568)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月5日 13:42](https://h4ck.org.cn/2022/11/10659#comment-88570)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      还好，本身图片不大。oss费用相对来说也比较低。不过就算是开放了用的人应该也不多吧。

      [回复](#comment-88570)

      1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

         [2022年11月5日 13:45](https://h4ck.org.cn/2022/11/10659#comment-88571)

         ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

         ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1") iPhone iOS 16.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         公开服务了就难说，也可能被刷。aws一个月100G，我也不敢搭这个代理

         [回复](#comment-88571)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2022年11月5日 13:46](https://h4ck.org.cn/2022/11/10659#comment-88572)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 104](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 104") Google Chrome 104 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.or...