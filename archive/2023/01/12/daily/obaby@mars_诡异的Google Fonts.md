---
title: 诡异的Google Fonts
url: https://h4ck.org.cn/2023/01/%e8%af%a1%e5%bc%82%e7%9a%84google-fonts/
source: obaby@mars
date: 2023-01-12
fetch_date: 2025-10-04T03:36:23.502796
---

# 诡异的Google Fonts

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

# 诡异的Google Fonts

2023年1月11日
[6 条评论](https://h4ck.org.cn/2023/01/10978#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/3fed5730f6ebdea0318d44fd1917b109.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/3fed5730f6ebdea0318d44fd1917b109.jpg)

最近打开博客后台的速度越来约慢了，已经到了让人无法忍受的地步了。之前已经通过litespeed cache插件进行了缓存，并且使用omgf进行了google fonts屏蔽。神奇的地方就在于，前台的加载速度基本不受影响，页面加载速度还可以，但是到加载完成依旧需要很长时间，需要等所有的数据加载之后浏览器的按钮才能重新变回刷新。调试了一下，发现首页的问题和内页的问题基本都是由于google fonts引起的，这就很奇怪了。是插件没生效？还是屏蔽不彻底？

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-164424-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-164424-scaled.jpg)

通过后面的启动器可以看到是由jetpack调用的。通过搜索命令找了一下jetpack里面的地址：

```
root@blog:/h4ck/wp-content/plugins/jetpack# grep -rn fonts.googleapis.com *
jetpack_vendor/automattic/jetpack-google-fonts-provider/src/class-google-fonts-provider.php:148:         *      'https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,200;0,300;0,400;1,400;1,500;1,600&display=fallback'
```

可以发现基本都在这一个文件内class-google-fonts-provider.php，修改之后诡异的事情发生了。依然会加载google fonts。所以最直接的办法就是禁用jet pack，禁用之后基本这个字体的问题就解决了。

但是进入后台依然有错误（由jetpack引发的超时也会影响后台的加载速度），出现了facebook 和twitter的两个js链接：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-171427.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-171427.jpg)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-171402.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-171402.jpg)

这也很让人抑郁，并没有看到facebook和twitter的相关内容啊。直接定位启动器会发现是由 child-theme-generator-admin调用的，编辑文件，注释掉响应代码，清空缓存，问题就解决了：

```
jQuery(document).ready(function( $ ) {

    $( "div#remove" ).click(function() {
        $( "div#remove" ).hide();
        $( "div#confirm").show() ;
    });

    $( "div#confirm" ).click(function() {
        $( "div#confirm" ).hide();
        $( "div#remove").show() ;
    });
    // Facebook 注释掉以下代码
    //(function(d, s, id) {
    //	var js, fjs = d.getElementsByTagName(s)[0];
    //	if (d.getElementById(id)) return;
    //	js = d.createElement(s); js.id = id;
    //	js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.8";
    //	fjs.parentNode.insertBefore(js, fjs);
    //}(document, 'script', 'facebook-jssdk'));
    //// Twitter
    //!function(d,s,id){
    //	var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';
    //	if(!d.getElementById(id)){js=d.createElement(s);
    //		js.id=id;js.src=p+'://platform.twitter.com/widgets.js';
    //		fjs.parentNode.insertBefore(js,fjs);
    //	}}(document, 'script', 'twitter-wjs');
} );
```

这个问题解决以后发现依然有加载的google fonts：

而这个字体来自于all in one seo pack：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-181225.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-181225.jpg)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-181256-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-181256-scaled.jpg)

修改文件chunk-vendors.css使用国内的镜像源替换https://fonts.font.im/ 即可。

虽然通过简单粗暴的方法解决了jetpack的问题，但是并不是自己想用的完美的解决方案，于是继续来查看相关的调用，发现最终字体是由这个文件加载的：

https://widgets.wp.com/notifications/?jetpack=true&v=none&locale=zh-cn，外联的wp的地址，这尼码就尴尬了，这个页面的内容也没法修改啊，虽然就那么几行。用来显示的是用户评论，同时由于要加载用户评论就会导致另外一个问题，访问gravatar官方的服务器，会引入另外的资源加载错误。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-180306-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-180306-scaled.jpg)

转变思路，从直接干掉admin bar的那个按钮开始。搜索grep -rn widgets.wp.com \* 会发现一个文件modules/notes.php:234比较可疑。那就直接拿这个文件开刀吧：

```
/**
 * Adds notifications bubble to the admin bar.
 *
 * @return void
 */
public function admin_bar_menu() {
        global $wp_admin_bar;
        return;
        if ( ! is_object( $wp_admin_bar ) ) {
                return;
        }

        $wpcom_locale = get_locale();

        if ( ! class_exists( 'GP_Locales' ) ) {
                if ( defined( 'JETPACK__GLOTPRESS_LOCALES_PATH' ) && file_exists( JETPACK__GLOTPRESS_LOCALES_PATH ) ) {
                        require JETPACK__GLOTPRESS_LOCALES_PATH;
                }
        }

        if ( class_exists( 'GP_Locales' ) ) {
                $wpcom_locale_object = GP_Locales::by_field( 'wp_locale', $wpcom_locale );
                if ( $wpcom_locale_object instanceof GP_Locale ) {
                        $wpcom_locale = $wpcom_locale_object->slug;
                }
        }
```

修改176行开始的函数，直接返回，不要什么bubble就ok啦。修改之后重新刷新，右上角的那个bubble就没了。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-180902-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/Jietu20230111-180902-scaled.jpg)

加载时间1.48s（对比开始的40.72s），啦啦啦。终于快啦

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/d68781cee6cb24caf26e1c7c076c9557.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/d68781cee6cb24caf26e1c7c076c9557.jpg) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/b44928e3c19e358518773bcc24a7d7fe.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/b44928e3c19e358518773bcc24a7d7fe.jpg)

**模特：[SJA佳爷]Vol.050\_闺蜜视角《影》针织衣美女私房肉丝裤袜配红高跟秀美腿诱惑写真62P**

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《诡异的Google Fonts》](https://h4ck.org.cn/2023/01/10978)
\* 本文链接：<https://h4ck.org.cn/2023/01/10978>
\* 短链接：<https://oba.by/?p=10978>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Google Fonts](https://h4ck.org.cn/tags/google-fonts)[jetpack](https://h4ck.org.cn/tags/jetpack)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2023/01/10995)
[Next Post](https://h4ck.org.cn/2023/01/10971)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年3月26日

#### [php-fpm开启opcache缓存](https://h4ck.org.cn/2023/03/11620)

2023年8月13日

#### [【教程】让WP-UserAgent[增强版 13.01.01]支持IPv6归属地显示](https://h4ck.org.cn/2023/08/12909)

2024年3月14日

[![](https://h4ck.org.cn/wp-content/uploads/2024/03/WechatIMG317-720x471.jpg?v=1710380033)](https://h4ck.org.cn/2024/03/15813)

#### [浅谈 WordPress 的速度优化 — 到底是谁拖垮了姐姐的 blog](https://h4ck.org.cn/2024/03/15813)

### 6 comments

1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r) **[小熊](https://www.saphead.cn)**说道：

   [2023年1月11日 21:39](https://h4ck.org.cn/2023/01/10978#comment-91030)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1.2](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1.2") iPhone iOS 16.1.2 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   啥...