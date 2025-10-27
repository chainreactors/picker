---
title: 也谈 cf 的 npm 代理 以及 uniapp vendor.js 压缩
url: https://h4ck.org.cn/2024/07/17750
source: obaby@mars
date: 2024-08-01
fetch_date: 2025-10-06T18:01:55.383088
---

# 也谈 cf 的 npm 代理 以及 uniapp vendor.js 压缩

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

[前端开发『FrontEnd』](https://h4ck.org.cn/cats/cxsj/%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E3%80%8Efrontend%E3%80%8F)

# 也谈 cf 的 npm 代理 以及 uniapp vendor.js 压缩

2024年7月31日
[32 条评论](https://h4ck.org.cn/2024/07/17750#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG479.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/WechatIMG479.jpg)

这两件事情，本质上区别还是蛮大的，一个是小程序的包体积问题，另外一个是 npm 源问题。但是这两件事情却又有千丝万缕的联系，不替换 npm 源就无法愉快的安装压缩插件，所以两件事情就写到了一起。

至于 npm 代理的问题，杜老师写了篇文章已经说的很清楚了，原文点击[这里](https://dusays.com/732/)查看。

主要的就是worker 的那几行代码：

```
addEventListener(
  "fetch", event => {
    let url = new URL(event.request.url);
    url.hostname = "unpkg.com";
    url.protocol = "https";
    let request = new Request(url, event.request);
    event.respondWith(
      fetch(request)
    )
  }
)
```

so easy 对不对？

然鹅，这个 npm 源个人感觉有问题，在指定包的版本号之后就无法安装了，提示下面的错误：

```
zhongling@zhonglingdeMacBook-Pro ~ %  npm config set registry https://npm.obaby.blog
zhongling@zhonglingdeMacBook-Pro ~ % npm install compression-webpack-plugin@6.1.1
npm ERR! code FETCH_ERROR
npm ERR! errno FETCH_ERROR
npm ERR! invalid json response body at https://npm.obaby.blog/compression-webpack-plugin@11.1.0/dist/index.js reason: Unexpected non-whitespace character after JSON at position 12

npm ERR! A complete log of this run can be found in: /Users/zhongling/.npm/_logs/2024-07-31T02_19_03_318Z-debug-0.log
```

刚开始以为是代理代码的问题，尝试换其他代码依然如此。问题是这几行代理的代码是如此简单，凭直觉感觉也不是代码的问题啊。

猜测可能是源的问题，尝试换 npm 的官方源，https://registry.npmjs.org 再次部署之后，就 ok 啦。cf 的速度，个人感觉还是蛮 ok 的。

worker 代码：

```
addEventListener(
  "fetch", event => {
    let url = new URL(event.request.url);
    url.hostname = "registry.npmjs.org";
    url.protocol = "https";
    let request = new Request(url, event.request);
    event.respondWith(
      fetch(request)
    )
  }
)
```

设置npm 源：

```
npm config set registry https://npm.obaby.blog
```

安装插件：

```
zhongling@zhonglingdeMacBook-Pro ~ % npm install compression-webpack-plugin@6.1.1
npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm WARN deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm WARN deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm WARN deprecated @npmcli/move-file@1.1.2: This functionality has been moved to @npmcli/fs

added 53 packages, removed 11 packages, changed 5 packages, and audited 133 packages in 18s

16 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilitiesd
```

到这里 npm 的问题就算是解决了，另外一个问题就是 uniapp 小程序打包的问题，首先来看下包的体积：

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240730-162455.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240730-162455.jpg)

很好，很丰满，一个 vendor.js 已经超过了 2.5M，这尼玛就离谱啊，一个小程序主包体积最大才 2M，这尼玛能上传？

于是想到了之前在 [linyufan](https://www.linyufan.com/content/19/1994-1.html) 那里看到的[《uniapp分包后，打包vendor.js过大的问题解决方案》](https://www.linyufan.com/content/19/1994-1.html)，说实话，虽然想到了可能是在他这里看到的，但是找文章的过程颇为曲折，在他的网站没有搜索，也没有归档之类的，全凭记忆找？太累了。于是从网上搜索 verdor.js 过大的问题的解决方案。

最终看到了几篇文章，感觉应该是说的同一件事情，通过compression-webpack-plugin插件压缩 js 文件。例如这篇文章：https://blog.csdn.net/weixin\_44690156/article/details/123544820

安装插件：

```
npm i compression-webpack-plugin
npm i webpack
```

插件安装好之后，配置压缩。**新建vue.config.js文件**：

```
const CompressionWebpackPlugin = require('compression-webpack-plugin');
const productionGzipExtensions = ['js', 'css']

module.exports = {
    configureWebpack: {
        plugins: [
            new CompressionWebpackPlugin({
                // filename: "[path][base].gz",
                algorithm: 'gzip',
                test: new RegExp('\\.(' + productionGzipExtensions.join('|') + ')$'), //匹配文件名
                threshold: 102400, //对10K以上的数据进行压缩
                minRatio: 0.8,
                deleteOriginalAssets: false, //是否删除源文件
                // deleteOriginalAssets: true, //是否删除源文件
            })
        ]
    }
}
```

但是此时便于运行会报下面的错误：

```
09:18:12.964 正在编译中...
09:18:14.428  ERROR  TypeError: Cannot read properties of undefined (reading 'tapPromise')
09:18:14.436 TypeError: Cannot read properties of undefined (reading 'tapPromise')
09:18:14.437     at /Users/zhongling/node_modules/compression-webpack-plugin/dist/index.js:372:39
09:18:14.447     at SyncHook.eval [as call] (eval at create (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/tapable/lib/HookCodeFactory.js:19:10), <anonymous>:9:1)
09:18:14.454     at SyncHook.lazyCompileHook (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/tapable/lib/Hook.js:154:20)
09:18:14.464     at Compiler.newCompilation (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Compiler.js:630:30)
09:18:14.465     at /Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Compiler.js:667:29
09:18:14.474     at AsyncSeriesHook.eval [as callAsync] (eval at create (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:6:1)
09:18:14.481     at AsyncSeriesHook.lazyCompileHook (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/tapable/lib/Hook.js:154:20)
09:18:14.488     at Compiler.compile (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Compiler.js:662:28)
09:18:14.489     at /Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Watching.js:77:18
09:18:14.497     at AsyncSeriesHook.eval [as callAsync] (eval at create (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:15:1)
09:18:14.504     at AsyncSeriesHook.lazyCompileHook (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/tapable/lib/Hook.js:154:20)
09:18:14.514     at Watching._go (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Watching.js:41:32)
09:18:14.515     at /Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Watching.js:33:9
09:18:14.521     at Compiler.readRecords (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Compiler.js:529:11)
09:18:14.531     at new Watching (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Watching.js:30:17)
09:18:14.537     at Compiler.watch (/Applications/HBuilderX.app/Contents/HBuilderX/plugins/uniapp-cli/node_modules/webpack/lib/Compiler.js:244:10)
```

重新制定版本号安装插件：

```
npm install compression-webpack-plugin@6.1.1
npm i webpack@4.46.0
```

安装之后可能会提示下面的信息：

```
npm WARN deprecated move-concurrently@1.0.1: This package is no longer supported.
npm WARN deprecated source-map-url@0.4.1: See https://github.com/lydell/source-map-url#deprecated
npm WARN deprecated figgy-pudding@3.5.2: This module is no longer supported.
npm WARN deprecated rimraf@2.7.1: Rimraf versions prior to v4 are no longer supported
npm WARN deprecated rimraf@2.7.1: Rimraf versions prior to v4 are no longer...