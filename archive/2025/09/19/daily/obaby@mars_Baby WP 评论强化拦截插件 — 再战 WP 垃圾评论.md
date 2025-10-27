---
title: Baby WP 评论强化拦截插件 — 再战 WP 垃圾评论
url: https://h4ck.org.cn/2025/09/21609
source: obaby@mars
date: 2025-09-19
fetch_date: 2025-10-02T20:21:28.826414
---

# Baby WP 评论强化拦截插件 — 再战 WP 垃圾评论

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

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# Baby WP 评论强化拦截插件 — 再战 WP 垃圾评论

2025年9月18日
[65 条评论](https://h4ck.org.cn/2025/09/21609#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/微信图片_20250918163845_190.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250918163845_190.jpg)

这种生态成熟，或者说受众较大的产品，难免惦记的人就多。之前已经增加了很多方法，来弥补 akismet的不足，包括禁止非中文评论，评论长度限制，是否包含中文等等。

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-164239.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-164239.jpg)

虽然拦截了很多垃圾评论，但是还有一些显而易见的垃圾，却还是要进审核或者回收站，这就让人的确不爽。

至于 wp 自带的评论设置，只能说没什么大用，设置了，还是一样要手工删除，这就 tmd 贼恶心。

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-164449-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-164449.jpg)

设置了关键字之后，还是难以直接屏蔽广西的这个屌毛，天天来发币安的广告，之前已经删了无数次，加到禁止评论关键词里面还是继续发。

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250917-093457-1-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250917-093457-1.jpg)

并且，找到了规律之后，还会带着中文发，这就很 tm 操蛋了。

还有这种来法验证码广告的：

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-111407-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-111407.jpg)

我之所以不加验证码，主要还是觉得这个东西体验太差了。然而为了屏蔽这些傻屌，随之而来的另外一个问题就是需要在 functions.php 中改的次数越来越多了，现在已经变成了下面的样子：

```
/**
 * 检查评论内容是否包含禁用词
 * @param string $content 评论内容
 * @param array $banned_words 禁用词数组
 * @return bool 是否包含禁用词
 */
function has_banned_word($content, $banned_words) {
    foreach ($banned_words as $word) {
        if (stripos($content, $word) !== false) {
            return true;
        }
    }
    return false;
}

/*
 * WordPress控制文章评论最少字数
 */
function custom_comment_length( $commentdata ) {
        $max_length = 1800;
        // 设置最大字数限制
        if ( mb_strlen( $commentdata['comment_content'] ) > $max_length ) {
                wp_die( '额，你评论的内容太多啦，最多可以输入1800个字，不要再评论区写论文啊！' ,'宝贝，出错了哦 - obaby@mars', array( 'back_link'=>true ) );
        }

        if ( ! is_admin() ) {
                $comment_content = $commentdata['comment_content'];
                if ( preg_match( '/[\x{4e00}-\x{9fa5}]/u', $comment_content ) === 0) {
                        //if (strpos($commentdata['comment_author_url'],'http')!==false || strpos($comment_content,'http')!==false){
                        //      wp_die( '不要乱发哦，让姐姐我不开心就不好了嘛！','姐姐我不开心啦！ - obaby@mars', array( 'back_link'=>true ) );
                        //}
                        //if (strpos($commentdata['comment_author_url'],'http')!==false || strpos($comment_content,'http')!==false){
                                wp_die( '不要乱发哦，让姐姐我不开心就不好了嘛！(评论禁止纯英文字符、数字内容)','姐姐我不开心啦！ - obaby@mars', array( 'back_link'=>true ) );
                        //}
                }
                $banned_words = ['binance.info', 'binance.com','xrumersale.site'];
                if (has_banned_word($comment_content, $banned_words)){
                        wp_die( '不要乱发哦，让姐姐我不开心就不好了嘛！(你tmd别发广告了ok？你是傻逼吗？！)','姐姐我不开心啦！ - obaby@mars', array( 'back_link'=>true ) );
                }
        }
        return $commentdata;
}

add_filter( 'preprocess_comment', 'custom_comment_length' );
```

每次要屏蔽一个傻逼，就要修改一次：banned\_words。的确是有些烦人，所以，直接弄了个插件出来，当然还是得感谢 cursor，写了 99% 的代码。哈哈哈。 [![](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-165016.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-165016.jpg)

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-164946.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/Jietu20250918-164946.jpg)

功能页面：

[![](https://h4ck.org.cn/wp-content/uploads/2025/09/UserszhongmingPicturesVivaldi-Captures2025-09-18-16.51.23-h4ck.org_.cn-1b88935cfe3a-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/09/UserszhongmingPicturesVivaldi-Captures2025-09-18-16.51.23-h4ck.org_.cn-1b88935cfe3a.jpg)

代码开源地址：

https://github.com/obaby/baby-wp-comment-filter

插件 zip 下载：

https://github.com/obaby/baby-wp-comment-filter/releases/tag/wp

无法访问的，搭配https://ghproxy.link 食用。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Baby WP 评论强化拦截插件 — 再战 WP 垃圾评论》](https://h4ck.org.cn/2025/09/21609)
\* 本文链接：<https://h4ck.org.cn/2025/09/21609>
\* 短链接：<https://oba.by/?p=21609>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[WordPress](https://h4ck.org.cn/tags/wordpress)[WP](https://h4ck.org.cn/tags/wp)[垃圾评论](https://h4ck.org.cn/tags/%E5%9E%83%E5%9C%BE%E8%AF%84%E8%AE%BA)

[Previous Post](https://h4ck.org.cn/2025/09/21627)
[Next Post](https://h4ck.org.cn/2025/09/21534)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年3月11日

#### [再谈评论区亲密度](https://h4ck.org.cn/2024/03/15777)

2020年9月11日

#### [Porn Data Anaylize — AI换脸 分类数据浅析(github)](https://h4ck.org.cn/2020/09/7426)

2022年12月7日

#### [那些代码托管服务平台](https://h4ck.org.cn/2022/12/10841)

### 65 comments

1. ![](https://gg.lang.bi/avatar/50b181af6dd3b12260967373e0cd3567f27f9399d9e172d2bb40f995024211fc?s=64&d=identicon&r=r) **[西风](https://xifeng.net)**说道：

   [2025年9月18日 18:10](https://h4ck.org.cn/2025/09/21609#comment-128719)

   ![Level 2](https://badgen.net/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![uz](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/uz.svg "uz")

   这个好

   [回复](#comment-128719)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年9月18日 21:57](https://h4ck.org.cn/2025/09/21609#comment-128722)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 138](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 138") Google Chrome 138 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      主要是有些太烦人了

      [回复](#comment-128722)
2. ![](https://gg.lang.bi/avatar/ffc1ac2ecde17b2eb1caff3e94c119fdaea4dc1a947a08a3092b388bf9b454d0?s=64&d=identicon&r=r)

   [2025年9月18日 18:26](https://h4ck.org.cn/2025/09/21609#comment-128720)

   ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 140](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 140") Google Chrome 140 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugin...