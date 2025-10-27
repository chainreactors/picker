---
title: Vite项目使用CDN
url: https://blog.upx8.com/3619
source: 黑海洋 - WIKI
date: 2023-06-04
fetch_date: 2025-10-04T11:45:50.352879
---

# Vite项目使用CDN

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Vite项目使用CDN

发布时间:
2023-06-03

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
15507

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
主要添加到modules中，多个CDN，就添加多个对象
name为需要 CDN 加速的包名称，一般名称为在js文件中from后的名称，import xx from 'name'
var为引用的变量，一般在js文件中import后的名称
css如果引用CDN库中有CSS，就把CSS填写上，无需在JS文件中再引入了

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

[取消回复](https://blog.upx8.com/3619#respond-post-3619)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")