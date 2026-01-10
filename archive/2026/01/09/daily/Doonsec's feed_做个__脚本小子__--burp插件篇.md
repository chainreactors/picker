---
title: 做个\"脚本小子\"--burp插件篇
url: https://mp.weixin.qq.com/s/3rXnyzJWASvhHP8oD5Rzmw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:07.133108
---

# 做个\"脚本小子\"--burp插件篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XxjRljYHYk2EAwD6sN6luzPSEb2TN1Oeiczah4DzJdLXiad4v3jYwKGdWMle31LbkfE2Tia4mb7xFUyBfODibRpOxQ/0?wx_fmt=jpeg)

# 做个"脚本小子"--burp插件篇

原创

kingman

kingman安全

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OefE3VMj77zzpiajviaurdkew5iaDIZ6w7YCCZ6MkKQbcxEXztPqWzQ9SQw/640?wx_fmt=png&from=appmsg)

“脚本小子”是贬义词？

可打渗透效率就是比你高你怎么说？

如下均为插件分享具体的插件可在github、bp自带的Bapp商店下载

公众号不提供任何不开源的东西

公众号不提供任何不开源的东西

公众号不提供任何不开源的东西

重要的事说三遍

想直接拿插件地址直接拉到最下面

# 0x00

---

实际上burpsuite的插件都做了什么？

大部分插件都是根据，经过burp的流量包通过正则匹配后获取其中的关键内容(例如id、remeberme、key)等等之后走自己的逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OeUyEs4MFahrZkQD9cXAdCckHibcJ8HazBoPT4O7VWqpkNyoxe2kDeF8w/640?wx_fmt=png&from=appmsg)

图中为HAE的配置页可以看到正则匹配后高亮显示

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OeDKpMVjibYn9xFviax9jkb85yYHzu9vsib9lM0W0mKASfOKia2nTGoKTA1g/640?wx_fmt=png&from=appmsg)

图中为xiayue的配置页可以看到正则匹配后将数据包分成三种情况重发

好的插件可以大幅度提升渗透效率、缩短渗透流程

如下是常用的一些插件没有排名先后之分

# 0x01

---

xiayue（快速针对未授权漏洞的挖掘）：

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1Oe1DxqqvfxBLw4ntbqd9aJbMCNVDYTOrnbGF25E4UAPq2eicKc4dN81OQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OeWvicjtonhfT7hvfLBdzY837a8ictluxia0JDvx6ScMKEv89XVCX1QsctQ/640?wx_fmt=png&from=appmsg)

HAE（快速对敏感信息高亮）：

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OeAA2wBFANQ5vxs9KKD7yVCPX4IVE2pic5OzAXSb4j7s5NpnS6ZsgU3Jw/640?wx_fmt=png&from=appmsg)

TsojanScan（漏洞扫描）：

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OevVEZDmGusSibcyl5hCnoDSEsmrmN1jNUFHsZX5MicibgoXX19dib8lI22Q/640?wx_fmt=png&from=appmsg)

Add Custom Header（添加自定义头）：

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1Oe7uVE4H7xCb1DhIOFpovKe2aXiaeMK3ibdSvOsaavjlH2xbRnPgUjM3GA/640?wx_fmt=png&from=appmsg)

autoDecoder（前端加解密对抗）：

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1OeeLjBjmrMXbClI0LjfianXWG5fkA3iblVxmcrHdJDO5xXxFQrcX3I15mA/640?wx_fmt=png&from=appmsg)

# 0x02

---

加载过多插件可能会影响burp性能（java会崩溃）

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1Oe0JBvDMtneyqg8OGwN9GKQvICTpCQsxaKiczeYwMPMiaxCKRLZaqeRKMg/640?wx_fmt=png&from=appmsg)

windows：直接burp设置里搜索memo

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk2EAwD6sN6luzPSEb2TN1Oe1pzpngZvyw3VpYl2cViaSHG4xDhmicqMDeVPp7rrwibGia33bUKIv3kUoA/640?wx_fmt=png&from=appmsg)

网上貌似只有windows的解决方案...这让我Debian很难办

Debian：支持正版由于没有礼物 买不起 只能给大家演示loader

首先想和windows用户一样是不可能的了 设置完根本没用 诀窍在于在启动的时候做手脚

此处拿kali举例子

```
 vi ~/.zshrc 新增如下内容： burpsuite() {  local base="xxx原版burp路径"//（此处默认loader和启动器在同一个位置）  ( cd "$base" || return 1    ./jre/bin/java \      -XX:+IgnoreUnrecognizedVMOptions \      -javaagent:"xxxloader路径"=loader,hanizfy \      --add-opens=java.desktop/javax.swing=ALL-UNNAMED \      -Xmx5G \           // 设置成自己想要的大小      -XX:+UseG1GC \      --add-opens=java.base/java.lang=ALL-UNNAMED \      --add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED \      --add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED \      --add-opens=java.base/jdk.internal.org.objectweb.asm.Opcodes=ALL-UNNAMED \      -jar "$base/burpsuite_pro.jar" "$@"  )}
```

# 0x03

---

xiayue地址：https://github.com/smxiazi/xia\_Yue

TsojanScan地址：https://github.com/Tsojan/TsojanScan

autoDecode地址：https://github.com/f0ng/autoDecoder

HAE（商店获取）

Add Custom Header（商店获取）

更多文章请关注：

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

kingman安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过