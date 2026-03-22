---
title: 工具|JS_URL_Extractor_Pro_v2.0发布
url: https://mp.weixin.qq.com/s/SzeSU_ICJnFbNM3DgVxSMw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:16:22.360747
---

# 工具|JS_URL_Extractor_Pro_v2.0发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IGws6hSXN0y8s5Vk4kEia1GSqwqevC9MJ8mpKtNeNoUgZU4SAbQUD7VAs9Iuq7DTyIDI9Zr1nZeSAxBj1HsxibKrTDyU7kFYFCibZqEibNyl9D8/0?wx_fmt=jpeg)

# 工具|JS\_URL\_Extractor\_Pro\_v2.0发布

原创

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器中沉浸阅读

说实话，这玩意儿是我被折腾急了才写的，就一个小工具，1.0已经被我丢进回收站了，我想这个工具在你们平时渗透测试项目也许可能大概一定会用到吧，实在找不到水洞的时候也许可以试试......![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_52@2x.png)

前阵子接了个活，要审计一个前端项目，代码是打包过的，乱七八糟的 chunk 文件十几二十个，里面藏着一堆 API 接口和资源路径，客户想要一份完整的接口清单，你总不能让人家一个个文件打开看吧。

最开始我用的老办法——开发者工具 Network 面板，点一遍流程，导出 HAR 文件。但问题很快就来了，有些接口是条件触发的，你不走到特定步骤它根本不请求；还有些资源是动态 import 的，第一次加载根本看不到；然后我试过在 VS Code 里全局搜索，`/api`、`http`、`.js` 来回搜，搜出来几百条，还得手动去重、过滤图片字体、整理格式……搞了两个小时，头都大了。

**我就想，这活凭什么不能自动化？**

## 于是就有了这个脚本

没什么复杂的架构，就是一个 Python 脚本，核心逻辑大概是这样：

```
1.读 JS 文件（本地的或远程的都行）2.用正则把里面像 URL 的字符串都抠出来3.过滤掉图片、字体这些一般不关心的资源4.把相对路径统一补上 5./ 开头，方便后续使用6.输出成两个列表：带域名的和不带域名的
```

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0x9IOTicTD5zPnXhTN42Yw2iciau8arkfQYRhSrDrY3fJwkhNqKlKknicy8eZMHEh4e9Ltbwib9x25qVusibQr98P44730KRKhWhBFVQ/640?wx_fmt=png&from=appmsg)

一、工具介绍

## ✨ 功能特性-

🌐 \*\*网络模式\*\*: 从目标网站下载 JS 文件并提取其中的 URL-

📁 \*\*本地模式\*\*: 扫描本地目录下的 JS 文件提取 URL-

🔗 \*\*智能分类\*\*: 自动区分含域名的完整 URL 和相对路径-

🧹 \*\*去重过滤\*\*: 自动去重并过滤无效 URL-

⚡ \*\*多线程支持\*\*: 可配置并发处理提高效率-

📝 \*\*详细日志\*\*: 彩色日志输出，支持保存到文件-

⚙️ \*\*灵活配置\*\*: YAML 配置文件支持

编辑 `config.yaml` 文件自定义：

* 网络请求超时和重试次数
* 并发工作线程数
* URL 过滤规则
* 正则表达式模式
* 日志级别和输出

二、工具使用

参数说明

| 参数 | 简写 | 说明 |
| --- | --- | --- |
| `--url-file` | `-u` | 包含 JS 文件 URL 的文本文件路径 |
| `--dir` | `-d` | 本地 JS 文件目录路径 |
| `--scan-site` | `-s` | 扫描网站获取 JS 文件 URL |
| `--output` | `-o` | 输出文件路径 |
| `--config` | `-c` | 配置文件路径 |
| `--verbose` | `-v` | 显示详细日志 |

1.从 URL 文件提取

```
# 准备 URL 列表 (input/file.txt)https://example.com/js/app.jshttps://example.com/js/vendor.js# 运行提取python main.py -u input/file.txt -o output/urls.txt
```

2.扫描本地目录

```
python main.py -d ./js_files -o output/urls.txt
```

3.扫描网站

```
python main.py -s https://example.com -o output/urls.txt
```

4.混合模式

```
python main.py -u input/file.txt -d ./js_files -o output/urls.txt
```

5.运行示例

```
# 基础用法python main.py -u input/file.txt -o output/result.txt# 扫描本地目录python main.py -d ./src/js -o output/result.txt# 扫描网站并提取python main.py -s https://target.com -o output/result.txt# 详细日志模式python main.py -u input/file.txt -v
```

三、工具获取

**关注公众号后台回复“****JUEP2.0****”均可获取下载链接**

|  |
| --- |
| **免责声明：**   本文章仅做网络安全技术研究使用！另利用网络安全007公众号所提供的所有信息进行违法犯罪或造成任何后果及损失，均由**使用者自身承担负责**，与网络安全007公众号**无任何关系**，也不为其负任何责任，**请各位自重！**公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！**让我们一起为中国网络安全事业尽一份自己的绵薄之力！** |

**●****推荐阅读**●****

******[应急响应系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2735815599062548484#wechat_redirect)******

**[未授权访问漏洞系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2740221722897186819&scene=126#wechat_redirect)**

**[Nessus漏扫神器之攻防两用](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484603&idx=1&sn=ab7748ce50815e8d9b113a0c047323a5&chksm=ea3b5a27dd4cd331ced13977630dcc1c321f9cba291f28ac17f4108fb0071df964ac5051e670&scene=21#wechat_redirect)**

******[红队如何在攻防演练中一夜暴富？](https://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247485324&idx=1&sn=b63f8d1a5eaf712297402bc2757938e3&scene=21#wechat_redirect)******

# **[浅谈Nacos漏洞之超管权限后续利用](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484671&idx=1&sn=6f268b7dd7e922b7bf7a84e5d4589651&chksm=ea3b5a63dd4cd375f19f69818b1d13a8b0d28775a7ce421673ef25a2f8172e4c83755885d2a6&scene=21#wechat_redirect)**

********[超级弱口令工具+超级字典，攻防必备！](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484816&idx=1&sn=db1111e7c521d4be5c52a373e4a8e228&chksm=ea3b5b0cdd4cd21ab4dfe20b60dbe88c010d376b6cb4be6d993433332e188e24ef6fc77e0d01&scene=21#wechat_redirect)********

********[记某APP服务端渗透测试实战GetShell](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484519&idx=1&sn=8a4322ac773f4147589a0a1b9dc9d3c2&chksm=ea3b5afbdd4cd3edabc9c553bbb5566f2401b9fabc05505c43a7d9a80a9965ec23ea6fbcba96&scene=21#wechat_redirect)********

******[日常实战渗透小技巧，掌握就无需担心漏洞产出为零！](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484957&idx=1&sn=a79f132cc4a21f4776be5550adf273e7&chksm=ea3b5881dd4cd197fea3594bb21397a5a943378eefd251033bacd8ccbaf203847af66117cba7&scene=21#wechat_redirect)******

**********[实战|某网站未授权访问=》数据库权限=》服务器权限](http://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247484547&idx=1&sn=541a371ace13e94aa87cf87f5f2e532b&chksm=ea3b5a1fdd4cd30923c52bcb6ea27c19c502f0eea80e5d84d96c1c6021c7c6f98292d2729148&scene=21#wechat_redirect)**********

****[全方位揭秘：50多种横向渗透提权终极技巧，一篇文章彻底掌握！](https://mp.weixin.qq.com/s?__biz=MzI1NTE2NzQ3NQ==&mid=2247485311&idx=1&sn=3c9c2f5fec222438aec1fcb543bf0c1e&scene=21#wechat_redirect)****

---

写作不易，分享快乐

期待你的 **分享**●**点赞●在看**●关注**●收藏******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

网络安全007

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

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