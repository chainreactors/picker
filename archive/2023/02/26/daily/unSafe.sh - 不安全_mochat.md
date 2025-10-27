---
title: mochat
url: https://buaq.net/go-150999.html
source: unSafe.sh - 不安全
date: 2023-02-26
fetch_date: 2025-10-04T08:08:11.351265
---

# mochat

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

![](https://8aqnet.cdn.bcebos.com/cb401490d7ac477ac33c4564c01df691.jpg)

mochat

MoChat —— 让企业微信开发更简单 中文 | Java文档 | 安装 | 截图 | 架构 | 数据库字典 | API文档 | 快速
*2023-2-25 23:7:30
Author: [github.com(查看原文)](/jump-150999.htm)
阅读量:39
收藏*

---

[![logo](https://camo.githubusercontent.com/f4884e2506e77a0780774fe00ec8dd199d3f034bc409e3e9fb5234028fe814fa/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f6c6f676f2e706e67)](https://camo.githubusercontent.com/f4884e2506e77a0780774fe00ec8dd199d3f034bc409e3e9fb5234028fe814fa/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f6c6f676f2e706e67)

## MoChat —— 让企业微信开发更简单

[![Php Version](https://camo.githubusercontent.com/7b57680f1ee3f5376fe153f1cc517c7ad95d1e8f0b4c7410b8c651a0807212d3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7068702d2533453d372e342d627269676874677265656e2e7376673f6d61784167653d32353932303030)](https://www.php.net)
[![Swoole Version](https://camo.githubusercontent.com/1ae869365953019672d8cf72ec496d5b6823a316458b567297c685334d60e001/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73776f6f6c652d2533453d342e352d627269676874677265656e2e7376673f6d61784167653d32353932303030)](https://github.com/swoole/swoole-src)
[![MoChat License](https://camo.githubusercontent.com/4315c1189f3631a1af96594dc4a6a376749a37ccdaf96d19a0f38ea4c4db7645/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d6f636861742d636c6f75642f6d6f636861742e7376673f6d61784167653d32353932303030)](https://github.com/mochat-cloud/mochat/blob/master/LICENSE)

[![输入图片说明](https://camo.githubusercontent.com/26422e326bbcddc03087891b15f0132bee6db471b11e4b35303481ecdded321e/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f6865616465722e706e67)](https://camo.githubusercontent.com/26422e326bbcddc03087891b15f0132bee6db471b11e4b35303481ecdded321e/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f6865616465722e706e67)

中文 | [Java](https://github.com/mochat-cloud/mochat-java)

[文档](https://mochat.wiki) | [安装](https://mochat.wiki/quick-start/install-bt.html) | [截图](#%E9%83%A8%E5%88%86%E6%BC%94%E7%A4%BA%E5%9B%BE%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0) | [架构](#%E4%B8%9A%E5%8A%A1%E6%9E%B6%E6%9E%84) | [数据库字典](https://mochat.wiki/database/md/tables.html) | [API文档](https://mochat.wiki/api/) | [快速开始](https://mochat.wiki/wework/how-to-authorize.html)

### 项目简介

> MoChat, easy way to WeWork

MoChat 是开源的企业微信应用开发框架&引擎，是一套通用的企业微信多租户SaaS管理系统，得益于 `Swoole` 和 `Hyperf` 框架的优秀，MoChat 可提供超高性能的同时，也保持着极其灵活的可扩展性。

#### 应用场景

可用于电商、金融、零售、餐饮服装等服务行业的企业微信用户，通过简单的分流、引流转化微信客户为企业客户，结合强大的后台支持，灵活的运营模式，建立企业与客户的强联系，让企业的盈利模式有了多种不同的选择。

#### 功能特性

六大模块助力企业营销能力升级：

* 引流获取：通过多渠道活码获取客户，条理有序分类
* 客户转化：素材库、欢迎语互动客户，加强与客户联系
* 客户管理：精准定位客户，一对一标签编辑，自定义跟踪轨迹，流失客户提醒与反馈
* 客户群管理：于客户的基础，进一步获取客户裂变，自动拉群。集中管理，快速群发
* 聊天侧边栏：提高企业员工沟通效率，精准服务
* 企业风控：客户聊天记录存档，并设立敏感词库、敏感词报警，多方位跟进管理员工服务

#### 业务架构

严格的分层来保证架构的灵活性

[![架构](https://camo.githubusercontent.com/6729c6c8facb2ee21b18e18d4d2ac1154f179bbb8eae64b913ef20f347ba7984/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f6672616d65776f726b322e706e67 "mochat微信.png")](https://camo.githubusercontent.com/6729c6c8facb2ee21b18e18d4d2ac1154f179bbb8eae64b913ef20f347ba7984/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f6672616d65776f726b322e706e67)

#### 核心技术

* 前端技术栈: `Vue`、`Vuex`、`Vant`、`Ant Design of Vue`
* 后端技术栈: `PHP`、`MySQL`、`Redis`、 `Swoole`、`Hyperf`

### 特此鸣谢

MoChat 的诞生离不开社区其他优秀的开源项目，在此特别鸣谢：

[![Swoole](https://camo.githubusercontent.com/3681a2dfd6552bf03dac9bf74ae87da5666375df78c1ec9d25d9e8c011d0064c/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f53776f6f6c652d6d696e692e706e67)](https://www.swoole.com/)
[![Hyperf](https://camo.githubusercontent.com/95f684f92524bcde687720a3feaaea3276b6fa8a337d9ec0593cef89f479db35/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f4879706572662d6d696e692e706e67)](https://www.hyperf.io/)
[![EasyWechat](https://camo.githubusercontent.com/5ae98a7e7d02be1329114b7d0d25e2e02253e07dc998c3f306b56292780d1094/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f456173795765436861742d6d696e692e706e67)](https://www.easywechat.com)
[![Vue](https://camo.githubusercontent.com/064445268e03d38ae39f3750a41a2bcffef042678e3a220772eb8fffbf3ba030/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f5675652d6d696e692e706e67)](https://cn.vuejs.org)
[![Vant](https://camo.githubusercontent.com/4a8ef2e0e2ddc3018981fae30ab9bec804af87ceaf482076071b495ef8f07e85/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f56616e742d6d696e692e706e67)](https://vant-contrib.gitee.io/vant/#/zh-CN/)
[![Ant](https://camo.githubusercontent.com/7c169d6d77ab8893d38ae4571954df2d2d4c83aea954c3b72ebbf9dc6389bf30/68747470733a2f2f6d6f63686174636c6f75642e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f6769746875622f416e7464762d6d696e692e706e67)](https://antdv.com)

### 环境部署

#### 准备工作

```
PHP >= 7.4 (推荐7.4版本)
Swoole >= 4.5
Wxwork_finance_sdk(so扩展)
pcntl扩展
Composer
MySQL >= 5.7
Redis
FFmpeg
Node.js >= 10
```

#### 运行系统

##### 后端运行

```
# 目录
git clone https://github.com/mochat-cloud/mochat.git

cd /path/to/mochat/api-server

# 安装依赖
composer install

# 运行PHP服务
php bin/hyperf.php start
```

##### 前端运行

```
# 进入项目目录
cd /path/to/mochat/dashboard

# 安装依赖
yarn install

# 编译生成dist
yarn run build
```

##### 必要配置

1、后端配置运行脚本

* `php bin/hyperf.php mc:init`，根据提示完成配置

2、前端配置

* 修改 .env 中的配置 VUE\_APP\_API\_BASE\_URL= 接口地址

#### 部署系统

##### 后端部署

* Docker：推荐根据`api-server/Dockerfile`使用K8S部署
* Shell： 使用`linux-install.sh`安装必要依赖

```
cd /usr/local/src && wget https://mochatcloud.oss-cn-beijing.aliyuncs.com/deploy/CentOS-install.sh && ./CentOS-install.sh
```

* Nginx 配置：具体参考开发文档

##### 前端部署

当项目开发完毕，只需要运行一行命令就可以打包你的应用

```
# dashboard 打包正式环境
yarn run build

# sidebar 打包正式环境
yarn run build
```

构建打包成功之后，会在根目录生成 `dist` 文件夹，里面就是构建打包好的文件，通常是 `.js` 、`.css`、`index.html` 等静态文件。

通常情况下 `dist` 文件夹的静态文件发布到你的 `nginx` 或者静态服务器即可，其中的 `index.html` 是后台服务的入口页面。

##### 更详细安装见: [传送门](https://mochat.wiki/quick-start/install.html)

### 项目介绍

#### 文件结构

```
.
├── api-server------------------------------------------ 后端接口代码
├── dashboard------------------------------------------- 商户后台前端代码
├── sidebar--------------------------------------------- 聊天侧边栏前端代码
└── workbench------------------------------------------- 工作台前端代码
└── operation------------------------------------------- 运营工具前端代码
```

##### 后端结构

```
.
├── app
│   ├── core-------------------------------------------- 核心应用目录
│   │   ├── chat-tool----------------------------------- 聊天侧边栏
│   │   ├── common-------------------------------------- 公共
│   │   ├── corp---------------------------------------- 企业
│   │   ├── index--------------------------------------- 首页
│   │   ├── install------------------------------------- 安装
│   │   ├── medium-------------------------------------- 媒体库
│   │   ├── official-account---------------------------- 公众号
│   │   ├── rbac---------------------------------------- RBAC权限
│   │   ├── tenant-------------------------------------- 租户
│   │   ├── user---------------------------------------- 用户
│   │   ├── work-agent-------...