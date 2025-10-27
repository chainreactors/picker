---
title: Vue3.4+Element-plus+Vite通用后台管理系统
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508431&idx=2&sn=b5926aedcfdcf7d0f301b7e13c6742d0&chksm=e9d36a2ddea4e33baa1c8d49405d1e042544533b4693e538669bcbf3e7eed476fdbef8f9230c&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-07-27
fetch_date: 2025-10-06T17:43:26.484826
---

# Vue3.4+Element-plus+Vite通用后台管理系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjCf3vOfiam78JrECgOXfa0RDGiaiamXo7miczeAOgYhykUIGrS89oNBslibbt2Ezzv8TYtTgLa6ibWk3yg/0?wx_fmt=jpeg)

# Vue3.4+Element-plus+Vite通用后台管理系统

字节跳动技术团队

以下文章来源于稀土掘金技术社区
，作者the局外人

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7YyxZtr9dqXDATzlgGsENjAzWK2dBWH5OsiajWImcJACg/0)

**稀土掘金技术社区**
.

掘金，一个帮助开发者成长的技术社区

##

## 🔥 前言

经过一段时间的打磨（具体忘了），迎来管理系统的第一个版本， 相较于其他后台管理模板，本后台管理模版只包含基本的刷新，全屏以及暗黑模式效果。本模板只供学习使用，难免会存在一些bug，还请见谅。

## 😀 项目介绍

一个基于`Vue3.4+Element-plus+Vite`搭建的轻量级后台管理模板，本项目分一个登录接口和一个用户信息接口，并且采用mockjs模拟数据，有简单的权限划分。

### ✨ 效果展示

#### 在线预览

https://dragon-xjy.atomgit.net/xjy-admin/#/login?url=/home

#### 仓库地址Gitee

https://gitee.com/dragon-xjy/xjy\_admin

#### 首页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjCf3vOfiam78JrECgOXfa0R0BzFGvP05x9Sx1fUpOcq1wHMytQMBOcibT5DfSmibW1AoPkMAVqTG5eQ/640?wx_fmt=png&from=appmsg)

## 🏅 技术栈

| 技术栈 | 描述 | 官网 |
| --- | --- | --- |
| Vue3 | 渐进式JavaScript框架 | https://cn.vuejs.org/ |
| Element-plus | 基于 Vue 3，面向设计师和开发者的组件库 | https://element-plus.org/zh-CN/ |
| Vite | 前端构建工具 | https://vitejs.cn/vite3-cn/ |
| Pinia | 符合直觉的 Vue.js 状态管理库 | https://pinia.web3doc.top/ |
| Echarts | 一个基于 JavaScript 的开源可视化图表库 | https://echarts.apache.org/zh/index.html |
| VueUse | 基于Vue组合式API的实用工具集 | https://www.vueusejs.com/ |
| animate.css | 一个现成的跨浏览器动画库 | https://animate.style/ |
| wangEditor | 开源 Web 富文本编辑器，开箱即用，配置简单 | https://www.wangeditor.com/ |

## 🌈 项目基本配置

### 项目全局配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjCf3vOfiam78JrECgOXfa0RFe7Dyjzf7cNT8Jfa0ibmqfl4qwtswW9b4nyOPJhXgrNdeY6HHicicrG4A/640?wx_fmt=png&from=appmsg)

### 代码统一规范

* Eslint：语法规则和代码风格检查
* Prettier：美化代码样式
* Stylelint: CSS 统一规范和代码检测

#### .eslintrc.cjs

```
// @see https://eslint.bootcss.com/docs/rules/
module.exports = {
    env: {
        browser: true,
        es2021: true,
        node: true,
        jest: true,
    },
    /* 指定如何解析语法 */
    parser: 'vue-eslint-parser',
    /** 优先级低于 parse 的语法解析配置 */
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        parser: '@typescript-eslint/parser',
        jsxPragma: 'React',
        ecmaFeatures: {
            jsx: true,
        },
    },
    /* 继承已有的规则 */
    extends: [
        'eslint:recommended',
        'plugin:vue/vue3-essential',
        'plugin:@typescript-eslint/recommended',
        'plugin:prettier/recommended',
    ],
    plugins: ['vue', '@typescript-eslint'],
    /*
     * "off" 或 0    ==>  关闭规则
     * "warn" 或 1   ==>  打开的规则作为警告（不影响代码执行）
     * "error" 或 2  ==>  规则作为一个错误（代码不能执行，界面报错）
     */
    rules: {
        // eslint（https://eslint.bootcss.com/docs/rules/）
        'no-var': 'error', // 要求使用 let 或 const 而不是 var
        'no-multiple-empty-lines': ['warn', { max: 1 }], // 不允许多个空行
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-unexpected-multiline': 'error', // 禁止空余的多行
        'no-useless-escape': 'off', // 禁止不必要的转义字符

        // typeScript (https://typescript-eslint.io/rules)
        '@typescript-eslint/no-unused-vars': 'off', // 禁止定义未使用的变量
        '@typescript-eslint/prefer-ts-expect-error': 'off', // 禁止使用 @ts-ignore
        '@typescript-eslint/no-explicit-any': 'off', // 禁止使用 any 类型
        '@typescript-eslint/no-non-null-assertion': 'off',
        '@typescript-eslint/no-namespace': 'off', // 禁止使用自定义 TypeScript 模块和命名空间。
        '@typescript-eslint/semi': 'off',

        // eslint-plugin-vue (https://eslint.vuejs.org/rules/)
        'vue/multi-word-component-names': 'off', // 要求组件名称始终为 “-” 链接的单词
        'vue/script-setup-uses-vars': 'error', // 防止<script setup>使用的变量<template>被标记为未使用
        'vue/no-mutating-props': 'off', // 不允许组件 prop的改变
        'vue/attribute-hyphenation': 'off', // 对模板中的自定义组件强制执行属性命名样式
    },
}
```

#### .prettierrc.json

```
{
  "singleQuote": false,
  "semi": false,
  "bracketSpacing": true,
  "htmlWhitespaceSensitivity": "ignore",
  "endOfLine": "auto",
  "trailingComma": "all",
  "tabWidth": 2
}
```

#### .stylelintrc.cjs

```
// @see https://stylelint.bootcss.com/
// 美化css书写的样式
module.exports = {
    extends: [
      'stylelint-config-standard', // 配置stylelint拓展插件
      'stylelint-config-html/vue', // 配置 vue 中 template 样式格式化
      'stylelint-config-standard-scss', // 配置stylelint scss插件
      'stylelint-config-recommended-vue/scss', // 配置 vue 中 scss 样式格式化
      'stylelint-config-recess-order', // 配置stylelint css属性书写顺序插件,
      'stylelint-config-prettier', // 配置stylelint和prettier兼容
    ],
    overrides: [
      {
        files: ['**/*.(scss|css|vue|html)'],
        customSyntax: 'postcss-scss',
      },
      {
        files: ['**/*.(html|vue)'],
        customSyntax: 'postcss-html',
      },
    ],
    ignoreFiles: [
      '**/*.js',
      '**/*.jsx',
      '**/*.tsx',
      '**/*.ts',
      '**/*.json',
      '**/*.md',
      '**/*.yaml',
    ],
    /**
     * null  => 关闭该规则
     * always => 必须
     */
    rules: {
      'value-keyword-case': null, // 在 css 中使用 v-bind，不报错
      'no-descending-specificity': null, // 禁止在具有较高优先级的选择器后出现被其覆盖的较低优先级的选择器
      'function-url-quotes': 'always', // 要求或禁止 URL 的引号 "always(必须加上引号)"|"never(没有引号)"
      'no-empty-source': null, // 关闭禁止空源码
      'selector-class-pattern': null, // 关闭强制选择器类名的格式
      'property-no-unknown': null, // 禁止未知的属性(true 为不允许)
      'block-opening-brace-space-before': 'always', //大括号之前必须有一个空格或不能有空白符
      'value-no-vendor-prefix': null, // 关闭 属性值前缀 --webkit-box
      'property-no-vendor-prefix': null, // 关闭 属性前缀 -webkit-mask
      'selector-pseudo-class-no-unknown': [
        // 不允许未知的选择器
        true,
        {
          ignorePseudoClasses: ['global', 'v-deep', 'deep'], // 忽略属性，修改element默认样式的时候能使用到
        },
      ],
    },
  }
```

## 🎈 按钮主题色

在`style/element/index.scss`中配置

```
/* 只需要重写你需要的即可 */
@forward 'element-plus/theme-chalk/src/common/var.scss' with ($colors: (
    'primary': (// 主色
      'base':#0F5197,
    ),
    'success': ( // 成功色
      'base': #199D33,
    ),
    'info': ('base': #4e4f51,
    ),
    'warning': ( // 警告色
      'base': #e26f03,
    ),
    'danger': ( // 危险色
      'base': #de2e06,
    ),
    'error': ( // 危险色
      'base': #de2e06,
    ),
  ));
```

**「vite.config.ts 配置」**

```
 css: {
      preprocessorOptions: {
        scss: {
          javascriptEnabled: true,
          // 自动导入定制化样式文件进行样式覆盖
          additionalData: `
          @use "@/styles/element/index.scss" as *;
           @use "@/config/public.scss" as *;
          `,
        },
      },
    },
```

## 🔑 项目集成

### mock.js

> ❝
>
> mock.js 生成随机数据，拦截 Ajax 请求
>
> ❞

参考：mock.js 官网

**「安装」**

```
pnpm install -D vite-plugin-mock mockjs
```

**「vite.config.ts 配置」**

```
import { viteMockServe } from 'vite-plugin-mock'

 plugins: [
      viteMockServe({
        mockPath: "./src/mock",
        // localEnabled: true,
      })
 ]
```

### UnoCSS

> ❝
>
> UnoCSS 是即时原子 CSS 引擎，通俗易懂的讲，就是在`template`模版中书写`css`
>
> ❞

参考：UnoCSS中文文档

**「安装」**

```
pnpm install -D unocss
```

**「vite.config.ts 配置」**

```
复制代码
// vite.config.ts
import UnoCSS from 'unocss/vite'

export default {
  plugins: [
    UnoCSS({ /* options */ }),
  ],
}
```

**「main.js中」**

```
// main.js
import "virtual:uno.css"
```

**「uno.config.js中可自行配置」**

```
// uno.config.ts
import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup,
} from "unocss"

export default defineConfig({
  shortcuts: {
    "flex-center": "flex justify-center items-center",
    "flex-x-center": "flex justify-center",
    "flex-y-center": "flex items-center",
    "wh-full": "w-full h-full",
    "flex-x-between": "flex items-center justify-between",
    "flex-x-end": "flex items-center justify-end",
    "absolute-lt": "absolute left-0 top-0",
    "absolute-rt": "absolute right-0 top-0 ",
    "fixed-lt": "fixed left-0 top-0",
    "b1-red": "b-1 border-solid b-red",
  },
  theme: {
    colors: {
      primary: "va...