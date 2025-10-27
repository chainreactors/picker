---
title: Vite项目使用CDN
url: https://buaq.net/go-167068.html
source: unSafe.sh - 不安全
date: 2023-06-04
fetch_date: 2025-10-04T11:44:34.076723
---

# Vite项目使用CDN

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Vite项目使用CDN

vite如果把全部的文件都给本地打包的话，体积就很大，所以把公共库给打包出来，就能减少很多体积。使用vite插件vite-plugin-cdn-impo
*2023-6-3 15:6:0
Author: [blog.upx8.com(查看原文)](/jump-167068.htm)
阅读量:23
收藏*

---

vite如果把全部的文件都给本地打包的话，体积就很大，所以把公共库给打包出来，就能减少很多体积。

使用vite插件vite-plugin-cdn-import，很方便的打包。下面以vue和element-plus为例。

## 安装插件

`npm install vite-plugin-cdn-import`

## 使用插件

找到vite配置文件vite.config.js

头部添加

```
npm install vite-plugin-cdn-import
```

添加到文件plugins节点中

```
importToCDN({
  modules: [
    {
      name: 'vue',
      var: 'Vue',
      path: `https://cdn.staticfile.org/vue/3.2.45/vue.runtime.global.prod.min.js`,
    },
    {

     name: 'element-plus',
      var: 'ElementPlus',
      path: `https://cdn.staticfile.org/element-plus/2.2.28/index.full.min.js`,
      css: 'https://cdn.staticfile.org/element-plus/2.2.28/index.min.css'
    },
  ]
})
```

**上述配置，配置了Vue和element-plus库**
**那么在JS引用如下**

```
import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
createApp(App).use(ElementPlus).mount('#app')
```

完整vite.config.js内容

```
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {Plugin as importToCDN} from "vite-plugin-cdn-import"
export default defineConfig({
    plugins: [
        vue(),
        importToCDN({
            modules: [
                {
                    name: 'vue',
                    var: 'Vue',
                    path: `https://cdn.staticfile.org/vue/3.2.45/vue.runtime.global.prod.min.js`,
                },
                {
                name: 'element-plus',
                var: 'ElementPlus',
                path: `https://cdn.staticfile.org/element-plus/2.2.28/index.full.min.js`,
                css: 'https://cdn.staticfile.org/element-plus/2.2.28/index.min.css'
            },
        ]
    }),
]
});
```

文章来源: https://blog.upx8.com/3619
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)