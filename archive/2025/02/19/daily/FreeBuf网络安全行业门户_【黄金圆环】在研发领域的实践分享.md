---
title: 【黄金圆环】在研发领域的实践分享
url: https://www.freebuf.com/news/422069.html
source: FreeBuf网络安全行业门户
date: 2025-02-19
fetch_date: 2025-10-06T20:40:02.683426
---

# 【黄金圆环】在研发领域的实践分享

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

【黄金圆环】在研发领域的实践分享

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

【黄金圆环】在研发领域的实践分享

2025-02-18 14:37:19

所属地 北京

作者：京东科技 屠永涛

这是我参与创作者计划的第1篇文章

## 一、引言

在前端开发中，构建工具的选择和使用至关重要。Webpack 一直是前端构建工具的主流选择，但随着前端技术的发展，Vite 作为一种新兴的构建工具，以其快速的开发体验和现代化特性，逐渐受到开发者的青睐。

**本文将****结合****黄金圆环****法则，详细探讨****如何将一个 Webpack 项目迁移到 Vite****。**

**通过项目的迁移实践，我们实现了系统项目：** **构建时长极大缩短，由原来的120s构建时长， 提升为1.5s构建，效率上提升了 98%。**

## 二、什么是黄金圆环

黄金圆环是由美国营销顾问西蒙·斯涅克（Simon Sinek）提出的一个用来阐释激励人心的领袖力的模型。它由三个同心圆组成

![](https://image.3001.net/images/20250218/1739860640_67b42aa0423a264d21c72.png!small)

1. **Why（为什么）**：核心动机，为什么要做这件事。

2. **How（如何）**：方法和手段，如何实现目标。

3. **What（做什么）**：具体的行动和产出，做了什么。

我们大部分人的思考方式是先考虑外面，都知道自己在做什么，其中一部分人知道自己怎么去做，但很少的人知道自己为什么要做这件事情。然而，成功的伟大领袖的思考模式与大多数人完全相反的。他们是从里到外的生活方式，他们会先思考为什么，再到怎么做再到是什么。

人们不因你所做的而买单，他们因你所做的理由而买单，你的行动就证明了你的信念。

在前端项目的迁移过程中，我们也可以应用黄金圆环法则来指导我们的决策和行动**。**

## 三、为什么迁移

### 1. 当前业务系统的困境

团队有个webpack构建的核心系统：

1. 功能复杂，模快依赖多，目前的依赖模块有 6336个，加上自身的源码，总的模块依赖数量超过7000;

2. 开发构建特别慢，mac电脑启动需要**120S**左右，windows更慢；

3. 热更新速度很慢，mac电脑接近**2s，**windows更慢**;**

4. 打包构建体积大，已经无法再通过配置进行优化。

以下是webpack的构建模式： 原来有 7000个模块， 需要等待 7000各模块解析好了， 才能启动服务，导致启动特别慢。

![](https://image.3001.net/images/20250218/1739860642_67b42aa23d1e4ac3a39a5.png!small)

由于系统存在这些问题，我选去思考如何加快我们的开发效率，同时减少打包体积，直接提升用户体验。

### 2. vite更快的开发体验

Vite 利用浏览器的原生 ES 模块支持，在开发阶段不需要对整个项目进行打包，从而大大加快了启动速度和热更新速度。这对于大型项目尤为重要，可以显著提升开发效率。开发者可以更快地看到代码的变化，减少等待时间，提高工作效率。

#### 2.1 vite构建模式

现在有 7000个模块，利用浏览器提供的ESM能力，解析首页需要的模块，就可以启动服务，实现快速启动。红色就是启动需要的模块。

![](https://image.3001.net/images/20250218/1739860643_67b42aa329ba998bf21c3.png!small)

### 3. 更现代的构建工具

Vite 内置了许多现代化特性，如支持 ES 模块、基于 Rollup 的生产构建、内置的 TypeScript 支持等。这些特性使得 Vite 更加适应现代前端开发的需求。通过使用 Vite，开发者可以更轻松地利用最新的前端技术和工具，提高项目的可维护性和扩展性。

### 4. 更简洁的配置

相较于 Webpack 的复杂配置，Vite 提供了更简洁和直观的配置方式，使得项目的配置和维护更加容易。Vite 的配置文件通常较短且易于理解，减少了配置错误的可能性，并使得新手开发者也能快速上手。

## 四、如何迁移

原项目基于 vue2.6.10开发。该小节介绍如何迁移的一个整体思路，具体实施在第五节。

### 1. 初始化 Vite 基础依赖

首先，我们需要安装vite的基础依赖包。

### 2. 初始化 vite 插件依赖

其次，我们需要安装适配vue2的相关依赖

### 3. 更改项目结构

1. 将原有 Webpack 项目中 **public** 目录下的入口文件 **index.html** 文件copy到根目录下。

2. 更改入口文件中的模板变量

3. 在环境变量文件(.env)中定义: **VITE\_APP\_TITLE**

### 4. 配置 Vite

根据项目需求，配置 Vite。Vite 的配置文件是 **`vite.config.js**`，可以在其中配置别名、插件、服务器选项等。

### 5. 处理CSS module

项目中可能会有将CSS文件导出为模块的部分，此时需要将该文件配置为CSS module。

### 6. 处理 深度选择器 /deep/ 相关的问题

在vite2中 /deep/的写法不被支持，需要将其转化成**::v-deep** 的形式。

### 7. 处理全局scss变量

在项目中，我们定义的scss变量有可能不生效，需要在**vite.config.js**中做特殊配置。

## 五、迁移的价值和具体行动

### 1. 迁移的价值

通过我们以上的实践， 我们最终完成迁移，同时进行了迁移效果的比对，得出如下结论：

![](https://image.3001.net/images/20250218/1739860644_67b42aa4008fc70bcf538.png!small)

### **2. 迁移的具体行动**

#### 2.1. 初始化 Vite 基础依赖

我们需要安装vite的基础依赖包。

```
npm i vite-plugin-vue2@1.9.0 vite@2.9.18 -D
```

#### 2.2. 初始化 vite 插件依赖

我们需要安装适配vue2的相关依赖

```
npm i
vite-plugin-dynamic-import@1.5.0
vite-plugin-env-compatible@1.1.1
vite-plugin-node-polyfills@0.7.0
vite-plugin-commonjs@0.10.0
vite-plugin-require-context@0.10.0
path-browserify@1.0.1
```

#### 2.3. 更改项目结构

1. 我们需要将原有 Webpack 项目中 **public** 目录下的入口文件 **index.html** 文件copy到根目录下。

2. 我们需要更改入口文件中的模板变量

原来的：

![](https://image.3001.net/images/20250218/1739860644_67b42aa4a55cd0fd00d84.png!small)

更新后的：

![](https://image.3001.net/images/20250218/1739860645_67b42aa540045ff142d9a.png!small)

3. 我们需要在环境变量文件(.env)中定义: **VITE\_APP\_TITLE**

![](https://image.3001.net/images/20250218/1739860646_67b42aa61e035c4a6f52b.png!small)

#### 2.4. 配置 Vite

根据项目需求，配置 Vite。Vite 的配置文件是 `vite.config.js`，在其中配置别名、插件、服务器选项等。以下是一个示例配置：

```
import{defineConfig }from'vite'import{createVuePlugin }from'vite-plugin-vue2'importenvCompatible from'vite-plugin-env-compatible'import{viteCommonjs }from'vite-plugin-commonjs'importviteRequireContext from'vite-plugin-require-context'importdynamicImport from'vite-plugin-dynamic-import'import{nodePolyfills }from'vite-plugin-node-polyfills'exportdefaultdefineConfig({// 项目公共的配置plugins:[createVuePlugin({jsx:true,// 支持vue jsx语法(需要同时把.js改为.jsx或者script标签加属性lang="jsx")}),dynamicImport(),viteCommonjs(),viteRequireContext(),envCompatible(),nodePolyfills(),],envPrefix:['VUE_APP_'],// 兼容VUE_APP_前缀// 项目个性化的配置base:'/',server:{host:'me.jr.jd.com',},resolve:{extensions:['.js','.vue','.json',],alias:{}},})
```

通过上述配置，我们可以轻松地设置项目的别名、插件和开发服务器选项，使项目更加符合开发需求；后面的步骤是一些个性化的配置。

#### 2.5. 处理CSS module

如果你的项目中有下面写法：

```
$menuText:red;:export{menuText:$menuText;}
```

你需要按照特定的命名约定来命名你的 SCSS 文件。通常，这个约定是将文件命名为 **\*.module.scss。** 在任何以`.module.css`为后缀名的 CSS 文件都被认为是一个[CSS modules 文件](https://github.com/css-modules/css-modules)。具体配置看各个项目个性化需求。

#### 2.6. 处理 深度选择器 /deep/ 相关的问题

在你的项目中，可能会使用深度选择器： /deep/。 这在vite2中是不被支持的， 你需要将其转成 **::v-deep**。 这里提供一个插件将其进行转换，可以避免在项目中进行全局的替换。

然后在**vite.config.js**中作为插件引入。具体配置看各个项目个性化需求。

```
function vitePluginTransDeep() {
  return {
    name: 'vite-plugin-transform-scss',
    enforce: 'pre',
    transform(src, id) {
      if (
        /\.(js|vue)(\?)*/.test(id) &&
        id.includes('lang.scss') &&
        !id.includes('node_modules')
      ) {
        return {
          code: src.replace(/(\/deep\/|>>>)/gi, '::v-deep')
        }
      }
    }
  }
}
```

#### 2.7. 处理全局scss变量

在Vite中我们可以通过**css.preprocessorOptions**进行配置。具体配置看各个项目个性化需求。

```
css:{preprocessorOptions:{scss:{additionalData:`@import "src/styles/variables.scss";`,// 如果有全局变量文件},},}
```

#### 2.8. 最终配置如下

```
import{defineConfig }from'vite'import{createVuePlugin }from'vite-plugin-vue2'importenvCompatible from'vite-plugin-env-compatible'import{viteCommonjs }from'vite-plugin-commonjs'importviteRequireContext from'vite-plugin-require-context'importdynamicImport from'vite-plugin-dynamic-import'import{nodePolyfills }from'vite-plugin-node-polyfills'functionvitePluginTransDeep(){return{name:'vite-plugin-transform-scss',enforce:'pre',transform(src, id){if(/\.(js|vue)(\?)*/.test(id)&&id.includes('lang.scss')&&!id.includes('node_modules')){return{code:src.replace(/(\/deep\/|>>>)/gi,'::v-deep'),}}}}}exportdefaultdefineConfig({// 公共配置plugins:[createVuePlugin({jsx:true,}),vitePluginTransDeep(),dynamicImport(),viteCommonjs(),viteRequireContext(),envCompatible(),nodePolyfills(),],envPrefix:['VUE_APP_'],// 兼容VUE_APP_前缀// 个性化配置base:'/dd/',server:{host:'me.jr.jd.com',},resolve:{extensions:['.js','.vue','.json',],alias:{}//},css:{preprocessorOptions:{scss:{additionalData:`@import './src/variables/index.scss';`,}}}})
```

## 六、整体总结

本文通过应用黄金圆环法则，我们从动机（Why）、方法（How）和实际操作（What）三个层面，详细探讨了如何将一个 Webpack 项目迁移到 Vite。Vite 的快速开发体验、现代化特性和简洁配置，使得它成为前端开发的新选择。

本文旨在帮助大家打开一种思考的思路，在平时的工作、学习、生活中换种思路去思考我们为什么要做我们正在做的事，做一个能够深度思考的学习者。在大脑中走得越远，我们才能在现实中走得越稳。

同时也给大家介绍了一下前端开发领域的工程化改造实践，如果你正在考虑优化你的前端项目，不妨尝试一下 Vite，相信它会带给你不一样的开发体验。

---

**最后，最重要的一点：**

**欢迎点赞、评论、收藏、关注！**

**欢迎大家交流学习，共同成长。**

# 资讯

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

一、引言

二、什么是黄金圆环

三、为什么迁移

* 1. 当前业务系统的困境
* 2. vite更快的开发体验
* 3. 更现代的构建工具
* 4. 更简洁的配置

四、如何迁移

* 1. 初始化 Vite 基础依赖
* 2. 初始化 vite 插件依赖
* 3. 更改项目结构
* 4. 配置 Vite
* 5. 处理CSS module
* 6. 处理 深度选择器 /deep/ 相关的问题
* 7. 处理全局scss变量

五、迁移的价值和具体行动

* 1. 迁移的价值
* 2. 迁移的具体行动

六、整体总结

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](ht...