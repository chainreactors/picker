---
title: 下载微信公众号的视频
url: https://zhongxiaojie.cn/2026/04/778/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-04-02
fetch_date: 2026-04-03T04:27:20.257700
---

# 下载微信公众号的视频

[![obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/wp-content/uploads/2026/01/new-logo-27.png)](https://zhongxiaojie.cn)

程序媛 / 独立开发者 / 智商不稳定的女神经

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

 [Menu](#mobilemenu)

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

[程序媛](https://zhongxiaojie.cn/category/code-girl/)

# 下载微信公众号的视频

2026年4月2日 16:46
[35 条评论](https://zhongxiaojie.cn/2026/04/778/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/30A1758-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/30A1758.jpg)

作为一个专业的程序媛，前端时间折腾龙虾转发公众号的文章到闺蜜圈wiki，之前已经处理了图片和文章的问题，今天转发的时候发现另外一个问题：文章里面的视频无法正常播放。

刚开始的时候想着直接去chrome的缓存里面找，但是试了下chrome://cache发现无效，又不想去找插件来干这件事情。直接去调试工具找对应的视频地址：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161705-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161705.jpg)

然而直接贴到地址栏，直接报403了。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161653-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161653.jpg)

唉，好尴尬，既然有本地缓存文件了。那么直接尝试将接收到的数据流写入到文件呗。找了半天没发现怎么直接把请求到的数据写入到文件，点击开始播放等待缓冲结束。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161721-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161721.jpg)

加载完了右下角的数据也就有了，直接切换成base64，复制粘贴：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161959-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-161959.jpg)

然而，尝试decode 之后，播放不了，缺少mp4的头文件，这就挺奇怪的。文件头哪里去了？my\_video为通过代码下载的mp4，video为通过base64 处理的图片。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-163158.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-163158.jpg) [![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-163245.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260402-163245.jpg)

文章测试地址：<https://mp.weixin.qq.com/s/heoer_zm4SFwFKsk4tRecQ>

看了下是video标签实现的：

```
<div data-v-c66e8e28="" class="js_inner inner not_fullscreen"><div data-v-c66e8e28="" class="js_video_poster video_poster"><div data-v-c66e8e28="" class="video_mask"></div><video data-v-c66e8e28="" src="https://mpvideo.qpic.cn/0bc3pidsgaahauamxiglsruvo6wden5aoiya.f10002.mp4?dis_k=247900efb8791f0718998ea0813793c9&amp;dis_t=1775118363&amp;play_scene=10120&amp;auth_info=d9/5u/dlYUBWn6qY0Sp2SXM9PUdEOj5CZmQ3H2k2TzNOXXtjTwYQen0+WTMXEzdWIDNuS0hkIHgTMSlENWAcfUpBcQ==&amp;auth_key=ed4a91866522f27b4b89c5e71e04d115&amp;vid=wxv_4453415887525888005&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" poster="http://mmbiz.qpic.cn/sz_mmbiz_jpg/GAVxEAgJstytcf0uF3dpdZKia9G96C3loxCNaBrbFLHCiak3GvJDfASC7uYqNjjAZ5e2OHSmHoBQrONRJ8UIq6icJjjFXMfUBtdhy7VWlfb3MM/0?wx_fmt=jpeg&amp;wxfrom=16" webkit-playsinline="isiPhoneShowPlaysinline" playsinline="isiPhoneShowPlaysinline" preload="metadata" crossorigin="anonymous" controlslist="nodownload" class="" style="display: block; width: 655px; height: 492px;"> 您的浏览器不支持 video 标签 </video></div><div data-v-f4ee5450="" data-v-c66e8e28="" class="video_poster__info__play" style="display: none;"><i data-v-f4ee5450="" data-v-c66e8e28="" class=""></i></div><div data-v-f4ee5450="" data-v-c66e8e28="" class="video_poster__info" style="display: none;"><p data-v-f4ee5450="" data-v-c66e8e28="" class="video_poster__info__title" style="font-size: 17px;">继续观看</p><p data-v-f4ee5450="" data-v-c66e8e28="" class="video_poster__info__desc" style="font-size: 12px;"> 孤独症，就是不爱说话吗？ </p></div><div data-v-f4ee5450="" data-v-c66e8e28="" class="video_poster__info__mask" style="width: 100%; display: none;"></div></div>
```

还是说着这个东西还有另外的处理逻辑？哪位大神知道原因还望不吝赐教。

既然decode不行，那就直接上代码吧：

```
#!/usr/bin/env python3
"""
下载 mpvideo.qpic.cn 等需 Referer 的 MP4（微信视频 CDN）。

Author: obaby
  https://zhongxiaojie.cn
  https://oba.by
"""

import argparse
import sys
import urllib.error
import urllib.request

# 与常见微信内嵌页一致，避免 403
DEFAULT_REFERER = "https://mp.weixin.qq.com/"
DEFAULT_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 "
    "MicroMessenger/7.0.20"
)

def main() -> None:
    p = argparse.ArgumentParser(description="带 Referer 下载 mpvideo MP4")
    p.add_argument("url", help="完整 mp4 URL（含查询参数）")
    p.add_argument(
        "-o",
        "--output",
        default="downloaded.mp4",
        help="保存路径（默认 downloaded.mp4）",
    )
    p.add_argument("--referer", default=DEFAULT_REFERER, help="Referer 头")
    p.add_argument("--user-agent", default=DEFAULT_UA, help="User-Agent")
    args = p.parse_args()

    req = urllib.request.Request(
        args.url,
        headers={
            "User-Agent": args.user_agent,
            "Referer": args.referer,
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)

    out = open(args.output, "wb") if args.output != "-" else sys.stdout.buffer
    try:
        out.write(data)
    finally:
        if out is not sys.stdout.buffer:
            out.close()
            print(f"已写入 {args.output}，{len(data)} 字节")
            if len(data) >= 8 and data[4:8] == b"ftyp":
                print("魔数检测：疑似标准 MP4（含 ftyp）")

if __name__ == "__main__":
    main()
```

现在就可以下载之后，上传了，发布的文章地址：

https://wiki.guimiquan.cn/archives/1514

---

[![闺蜜圈APP](/support/guimiquan-ads2.jpg)](https://guimiquan.cn "闺蜜圈APP")

**博客：** [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/)

**地址：** <https://zhongxiaojie.cn/>

**文章：** [《下载微信公众号的视频》](https://zhongxiaojie.cn/2026/04/778/)

[公众号](https://zhongxiaojie.cn/tag/%E5%85%AC%E4%BC%97%E5%8F%B7/)[微信](https://zhongxiaojie.cn/tag/%E5%BE%AE%E4%BF%A1/)[爬虫](https://zhongxiaojie.cn/tag/%E7%88%AC%E8%99%AB/)[视频](https://zhongxiaojie.cn/tag/%E8%A7%86%E9%A2%91/)

[Next Post](https://zhongxiaojie.cn/2026/04/768/)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=initials&r=pg&initials=ob)

#### obaby

独立 APP 开发者
偶尔写点东西
希望与过往一刀两断

#### You may also like

2026年2月9日 09:06

#### [WP RSS.Beauty 插件](https://zhongxiaojie.cn/2026/02/416/)

2026年1月27日 20:59

#### [浅谈WordPress静态化](https://zhongxiaojie.cn/2026/01/270/)

2026年3月14日 16:14

#### [开源项目目录📇](https://zhongxiaojie.cn/2026/03/593/)

### 35 comments

1. ![](https://gg.lang.bi/avatar/0b3b8cb95165c8e438337c47068ca52924eb8c720204352f7173082960b42c74?s=64&d=initials&r=pg&initials=%E8%8A%B1%E9%9D%9E) **[花非花](https://www.941741.xyz)**说道：

   [2026年4月2日 5:25 下午](https://zhongxiaojie.cn/2026/04/778/#comment-2185)

   ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Windows 11 x64 Edition](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11 x64 Edition") Windows 11 x64 Edition ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   果然还得是程序员啊，这解决问题的思路

   [回复](#comment-2185)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年4月3日 9:52 上午](https://zhongxiaojie.cn/2026/04/778/#comment-2205)

      ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](h...