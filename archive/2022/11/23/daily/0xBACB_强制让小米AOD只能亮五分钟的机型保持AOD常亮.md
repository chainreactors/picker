---
title: 强制让小米AOD只能亮五分钟的机型保持AOD常亮
url: https://blog.binklac.com/2f586df9bdee/
source: 0xBACB
date: 2022-11-23
fetch_date: 2025-10-03T23:29:37.810040
---

# 强制让小米AOD只能亮五分钟的机型保持AOD常亮

[![blog logo](/image/common/apple-touch-icon.png) 0xBACB](/)

[首页](/) [归档](/archives) [标签](/tags) [分类](/categories) [关于](/about) [友链](/links)

![author avatar](/image/common/avatar.png)

VeroFess

一个通过开发安全工具让系统变得不安全的家伙

[5 文章](/archives) [3 分类](/categories) [5 标签](/tags)

目录

分类

[开发笔记 1](/categories/%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0/)[科普 2](/categories/%E7%A7%91%E6%99%AE/)[折腾记录 2](/categories/%E6%8A%98%E8%85%BE%E8%AE%B0%E5%BD%95/)

热门标签

[科普](/tags/%E7%A7%91%E6%99%AE/ "科普")[信息安全](/tags/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8/ "信息安全")[Minecraft](/tags/Minecraft/ "Minecraft")[安卓](/tags/%E5%AE%89%E5%8D%93/ "安卓")[CSharp](/tags/CSharp/ "CSharp")

# 强制让小米AOD只能亮五分钟的机型保持AOD常亮

2022-11-22  [折腾记录](/categories/%E6%8A%98%E8%85%BE%E8%AE%B0%E5%BD%95/)  49 字

[安卓](/tags/%E5%AE%89%E5%8D%93/)

为了轻薄买了个小米的Civi，然后发现AOD五分钟就灭了，你这ADO了个寄吧.jpg

解决方式也很简单，`adb shell` 进去, 执行

```
settings put secure aod_mode_time 2
```

作者： [VeroFess](/about)

文章链接：<https://blog.binklac.com/2f586df9bdee/>

版权声明：本博客所有文章除特别声明外，均采用[CC BY-NC-SA 4.0 协议](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)。转载请注明出处！

[上一篇

一些网络安全方面的基础科普 - P2 操作系统安全从入门到放弃](/27113fa2a38a/)

[下一篇

一些网络安全方面的基础科普 - P1 识别恶意软件](/d4ad30414b22/)

评论

目录

目录

最近文章

2022-11-22

[一些网络安全方面的基础科普 - P2 操作系统安全从入门到放弃](/27113fa2a38a/)

2022-11-22

[强制让小米AOD只能亮五分钟的机型保持AOD常亮](/2f586df9bdee/)

2022-11-21

[一些网络安全方面的基础科普 - P1 识别恶意软件](/d4ad30414b22/)

2022-06-09

[CSharp中实现一个可继承的Singleton基类](/f72f727a78aa/)

Copyright © 2017 - 2022   [0xBACB](/)

Powered by [Hexo](https://hexo.io/)  |  Theme - [Kaze](https://github.com/theme-kaze)

本站总访问量次  |  本站总访客数次