---
title: Bun 打包独立可执行文件的一些坑
url: https://mp.weixin.qq.com/s/71wexu4ZdsFihkuBp_Z8Yw
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:01:34.638874
---

# Bun 打包独立可执行文件的一些坑

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6N4b2yN3FOJgZzmysBwlMdYIuDAfEiabDGse2zicAiaGXFkXW7nDee5wzlaNyFKDbHUlm34k8NCp8Pjllib6FhwdJg/0?wx_fmt=jpeg)

# Bun 打包独立可执行文件的一些坑

原创

0xcc
0xcc

非尝咸鱼贩

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJgZzmysBwlMdYIuDAfEiabDGzWjYA5yE263yNicwcDvF0WDAgicPUVV5LrZs7Cl8ib8tnJnXtNoIjPog/640?wx_fmt=png&from=appmsg)

Bun 去年年底被 Anthropic 收购的新闻刷屏了一阵，在此之前我已经在个人项目玩了好久了。

简单来说 Bun 是 js 运行时里的新秀，和 Node.js 在开发语言和引擎上都走了不同的路线。Bun 使用 Zig 开发，脚本引擎用的 Safari 的 JavaScriptCore。

其实我并不在乎 Bun 大力宣传的运行速度的提升。对我来说比较吸引人的地方在于 Bun 在努力兼容 node.js 核心库的同时也内置了一些非常实用的功能，不需要额外安装 npm 包。比如前阵子加入了 Bun.Archive API 可以直接读写 tar 格式，在未来还将引入 zip 的支持。今天还新鲜出炉了内置的 markdown 解析和渲染。

![import { markdown } from "bun";  const html = markdown.html("# Hello **world**"); // <h1>Hello <strong>world</strong></h1>  // ANSI terminal output const ansi = markdown.render("# Hello\n\n**bold**", {   heading: (children) =>](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6N4b2yN3FOJgZzmysBwlMdYIuDAfEiabDKPARCVHAXYoo4EJcldfVv1ANKHt3lVoIFhj93MsqwokN0KjVWBzX5w/640?wx_fmt=jpeg&from=appmsg)

来自 bun CEO Jarred Sumner

除了作为 js/ts 运行时之外，Bun 还能做前端打包，测试框架，替代 npm 包管理。Bun 对 node.js 核心库的兼容当然不是 100%，在我的玩具里暂时还没有遇到问题，这就够用了。

去年 Agent 开发话题颇为火热，TypeScript 是不少人首选的开发语言。各种终端界面工具的流行甚至有了一点文艺复兴的味道。最新版的 Node.js 支持通过 Type Stripping 开箱即用运行 ts 项目（无需特定 flag，但不支持部分特定语法），Bun 也类似。现在运行 ts 项目已经可以基本摆脱转译器。

下面开始正题。

两年前的外国贴吧上的一封帖子《我是 GitHub 新手，不吐不快》走红了。楼主飙脏话怒喷开源作者提供的安装构建步骤繁琐，对新手不友好。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJgZzmysBwlMdYIuDAfEiabDsriaIoouyqAahzpgC9RHuogHuXr8U383IlZedGtLUFWTuZyMGqe9ntQ/640?wx_fmt=png&from=appmsg)

有的人嘲笑楼主太菜，GitHub 本来的用途就是开放源代码，不是软件下载站；也有人觉得不无道理，开源软件应该面向最终用户提供友好的部署方式。

而回到 TypeScript / Javascript 构建出来的命令行工具。包管理一条命令就能一键安装，然而在桌面操作系统环境上，打包成独立可执行文件直接让用户下载也不失为一种分发的途径。

当然提供可执行文件下载并不见得比包管理一条命令安装友好多少。首先主流桌面系统的安全机制（Windows 的 SmartScreen 和 macOS 的 GateKeeper）会阻止不带签名的可执行文件直接运行。想要丝滑体验还得去搞一个签名。

Bun 另一个功能，也是写这篇笔记的目的，就是可以把 ts / js 项目打包成一个单独的可执行文件（Single-executable application，简称 SEA），无需安装运行时，而是直接复制到目标机器上部署。目前 claude code 就是这样做的。

这种打包分发对 python 程序员已经轻车熟路了，有 pyinstaller 和 pyexe 等若干方案。Electron 和 tauri 也是打包成单应用，但并不是面向命令行终端程序。

在我之前折腾这个环境的时候 Node.js 的 SEA 的构建步骤还不太友好。前两天 Node.js 25.5.0 发布，总算把构建命令简化了。对比起来，目前 Node.js 的 asset API 反而更合我需求一点。

首先还是 hello world 示例。

首先 cli.ts

```
console.log("Hello world!");
```

然后使用 bun 打包成可执行文件：

```
bun build ./cli.ts --compile --outfile mycli
```

接下来直接运行这个 ./mycli 就可以。默认只会生成当前环境的可执行文件。如果需要交叉构建，例如在 Linux 下生成可供 Windows 运行的 exe，则需要加上 --target 参数。可选的平台如下：

| —target | 系统 | CPU | Libc |
| --- | --- | --- | --- |
| bun-linux-x64 | Linux | x64 | glibc |
| bun-linux-arm64 | Linux | arm64 | glibc |
| bun-windows-x64 | Windows | x64 | - |
| bun-darwin-x64 | macOS | x64 | - |
| bun-darwin-arm64 | macOS | arm64 | - |
| bun-linux-x64-musl | Linux | x64 | musl |
| bun-linux-arm64-musl | Linux | arm64 | musl |

更多选项请参考官方文档，下面讲讲之前遇到的一些坑。

本公众号的老读者肯定一下就猜到我想用这个打包 frida，没错。

在 js 里导入了 frida 库之后，编译打包运行，得到类似如下错误：

```
2614 |         dir = process.cwd();2615 |       }2616 |       if (exists(join2(dir, "package.json")) || exists(join2(dir, "node_modules"))) {2617 |         return dir;2618 |       }2619 |         throw new Error('Could not find module root given file: "' + file + '". Do you have a `package.json` file? ');                     ^error: Could not find module root given file: "/$bunfs/root/igf-darwin-arm64". Do you have a `package.json` file?      at getRoot (/$bunfs/root/igf-darwin-arm64:2619:15)      at bindings (/$bunfs/root/igf-darwin-arm64:2549:41)
```

光看这个错误是比较让人困惑，但大体可以猜到和二进制 npm 包有关。出错的上下文在 bindings 库尝试逐层目录查找 package.json 来定位根目录，然后拼接出需要 process.dlopen 的路径来载入二进制 npm 库。这里有一个对应的 issue：

https://github.com/oven-sh/bun/issues/10964

我一开始以为二进制库不会随着 bun 的构建过程打包，询问 ai 也没有搞出来解决方案。直到有天我关注到这个 issue 下出现了几条神回复，精准地指出了问题的关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJgZzmysBwlMdYIuDAfEiabDeAQvf6YLSQJjnPqcHTTXBtibMaEJhxVSja1gCtfgdQDJYqLnIT4Hxbg/640?wx_fmt=png&from=appmsg)

由于 bun 打包之后会把文件系统路径转换成虚拟的 $bunfs 路径，bindings 按照目录搜索会失败。而 bun 有一个与 Node.js 不同的地方，就是除了 process.dlopen(.so) 之外，还可以直接用 require(.so)。

只要给 node\_modules 下的库（在这里是 frida）打补丁，去掉 bindings 改成 require 就可以了。当然这样一来用 node 就会报错，但我们的目的是生成可执行文件，无所谓。

Bun 还内置了一个功能就是 patch，可以在 bun install 之后自动根据 package.json 里配置的 patchedDependencies，直接修改第三方 npm 包。

如下是能让 frida@17.5.1 正常打包运行的补丁：

```
diff --git a/build/src/frida.js b/build/src/frida.jsindex 0b047472199e9151691c52f03ffd36a85952234c..ee9395ae0a8307d8e5a9a31f8663d5d612683b0e 100644--- a/build/src/frida.js+++ b/build/src/frida.js@@ -1,15 +1,8 @@-import bindings from "bindings";+const binding = require('../../build/frida_binding.node'); import util from "util"; import { Minimatch } from "minimatch"; import { Duplex } from "stream"; const { inspect } = util;-const binding = bindings({-    bindings: "frida_binding",-    try: [-        ["module_root", "build", "bindings"],-        [process.cwd(), "bindings"],-    ]-}); var MessageTypeImpl; (function (MessageTypeImpl) {     MessageTypeImpl["Send"] = "send";
```

下一步就是怎么蹭 GitHub 的持续集成自动构建多个平台的可执行文件。

bun compile 命令在没有制定 target 的情况下只会生成当前平台的文件。但加上 target 参数还没完，同样因为 frida 是一个二进制包，在安装的时候会调用 prebuild（也是一个 npm 包）来下载安装对应平台的 so。

因此在 GitHub Action 的构建脚本当中也需要针对性的，对每一个 target 参数都执行一次 prebuild 命令。

如果看到这有点摸不着头脑，实例代码我放 GitHub 了。

https://github.com/ChiChou/frida-node-portable/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJgZzmysBwlMdYIuDAfEiabDREOqkTzWtWLzF0k8ibcKKMb57j1ibCKQw2Q6IRVEGt4slR9rabmcv3WQ/640?wx_fmt=png&from=appmsg)

反正现在大家都觉得多占点内存和存储多大点事，80M 还好吧（斜眼）

最后一个困扰我的坑就是如何打包一整个文件夹。

嵌入图片等非代码等资源文件，官方的示例是这样的：

```
import icon from "./icon.png" with { type: "file" };import { file } from "bun";// Get file contents as different typesconst bytes = await file(icon).arrayBuffer(); // ArrayBufferconst text = await file(icon).text(); // string (for text files)const blob = file(icon); // Blob
```

因为我要打包一个 webui 进去，而前端用的构建工具并不是 bun。

这就导致我需要编写一个脚本遍历整个文件夹，针对每一个文件生成一个 import 语句。

官网确实给了一个打包目录的示例：

https://bun.com/docs/bundler/executables#embed-directories

但同样地，在引用具体文件的时候只能专门用一条 import 语句指定相对路径。而 import 函数还不能用动态的字符串，因为打包的过程需要确定 import 的路径，否则会导致缺失对应的资源文件。更无语的是别忘了 bun 本身就是一个 js 打包器。按照官网给的示例把 .js 路径传进去，bun 不会原样打包，而是会尝试将这个 js 作为一个入口点进行代码分析，对于前端工具已经生成好的生产代码自然报错满天飞。

所以如果我要打包一整个 assets 文件夹然后调用 serveStatic……不行。

折衷的方案就是用构建脚本把前端目录打成 tar 压缩包，这样只需要 import 一个确定的文件名，然后在主程序初始化过程动态解压出来。Node 的 SEA 似乎也没有简单处理这种场景的办法，而那边甚至没有内置的 tar 解压支持。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJePjhDUn7xMMlhZWpLjDwu3WUia32nGS0LiaB64WpyniauGgN9ibRaG1okaRpxswTPwaEgqTlic3aRJrQ/0?wx_fmt=png)

非尝咸鱼贩

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJePjhDUn7xMMlhZWpLjDwu3WUia32nGS0LiaB64WpyniauGgN9ibRaG1okaRpxswTPwaEgqTlic3aRJrQ/0?wx_fmt=png)

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