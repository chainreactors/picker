---
title: WEB前端逆向在nodejs环境中复用webpack代码
url: https://blog.nsfocus.net/nodejs/
source: 绿盟科技技术博客
date: 2025-05-14
fetch_date: 2025-10-06T22:29:15.259828
---

# WEB前端逆向在nodejs环境中复用webpack代码

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# WEB前端逆向在nodejs环境中复用webpack代码

### WEB前端逆向在nodejs环境中复用webpack代码

[2025-05-13](https://blog.nsfocus.net/nodejs/ "WEB前端逆向在nodejs环境中复用webpack代码")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 2,009

目录:

☆ 背景介绍

☆ nodejs环境完整实验用例

☆ 安装webpack开发环境

☆ 用webpack打包成browser可用代码

1) hello.js

2) webpack配置文件

3) webpack打包

4) hello.html

☆ 用AI辅助理解webpack打包结果框架流程

☆ webpack动态导出

☆ 在nodejs环境中使用browser环境代码

1) 全局导出\_\_webpack\_require\_\_函数

2) run\_webpack\_code\_1.js

3) 生产模式webpack打包结果复用

3.1) 全局导出\_\_webpack\_require\_\_函数

3.2) run\_webpack\_code\_1.js

3.3) 半自动收集245模块所有依赖模块

☆ 小结

————————————————————————–

☆ 背景介绍

WEB前端逆向中会遭遇webpack处理过的js代码，这种代码不是给人类阅读的，所以没

什么可读性。有些生成关键字段的函数位于其中，不想调试分析算法逻辑，想视之为

黑盒函数，给in，返回out；想在nodejs环境中复用本来在browser环境中运行的

webpack代码；此过程俗称「webpack代码抠取」。

简单点说，webpack是一种工具，可将本来在nodejs环境中运行的js处理一下，生成

可在browser环境中运行的js。对WEB前端逆向人员，没必要往更复杂理解。学习思路

如下

a. 写一套nodejs中可用的测试用例

b. 正向应用webpack技术，从a中js得到新的带符号信息的js

c. 编写HTML，在browser中使用b中js

d. F12调试，了解webpack框架流程

e. 正向应用webpack技术，从a中js得到新的strip过的js，接近现实世界案例

f. 针对e中js进行逆向工程，从中抠取webpack代码，得到新的js

g. 在nodejs中加载f中js，调用其中感兴趣的函数，得到返回值

按此思路学习，可从原理上真正理解「webpack代码抠取」。

☆ nodejs环境完整实验用例

假设目录结构如下

————————————————————————–

/path/hello/

|

\—src/

foo\_0.js

foo\_1.js

foo\_2.js

foo\_3.js

bar\_0.js

bar\_1.js

bar\_2.js

bar\_3.js

hello\_node.js

crypto-js.min.js

————————————————————————–

a中js位于”hello/src”子目录，这是一组nodejs环境完整实验用例。

————————————————————————–

// foo\_0.js

function func\_foo\_0 ( sth ) {

console.log( sth );

}

module.exports  = {

func\_foo\_0  : func\_foo\_0,

};

————————————————————————–

// foo\_1.js

function func\_foo\_1 ( a, b ) {

return a + b;

}

module.exports  = {

func\_foo\_1  : func\_foo\_1,

};

————————————————————————–

// foo\_2.js

let CryptoJS    = require( ‘./crypto-js.min.js’ );

function func\_foo\_2 ( sth ) {

let hash    = CryptoJS.MD5( sth );

return hash.toString( CryptoJS.enc.Hex );

}

module.exports  = {

func\_foo\_2  : func\_foo\_2,

};

————————————————————————–

// foo\_3.js

let CryptoJS    = require( ‘./crypto-js.min.js’ );

function func\_foo\_3 ( sth ) {

let hash    = CryptoJS.SHA256( sth );

return hash.toString( CryptoJS.enc.Hex );

}

module.exports  = {

func\_foo\_3  : func\_foo\_3,

};

————————————————————————–

// bar\_0.js

let foo\_0   = require( ‘./foo\_0.js’ );

function func\_bar\_0 ( sth ) {

foo\_0.func\_foo\_0( sth );

}

module.exports  = {

func\_bar\_0  : func\_bar\_0,

};

————————————————————————–

// bar\_1.js

let foo\_1   = require( ‘./foo\_1.js’ );

function func\_bar\_1 ( a, b ) {

return foo\_1.func\_foo\_1( a, b );

}

module.exports  = {

func\_bar\_1  : func\_bar\_1,

};

————————————————————————–

// bar\_2.js

let foo\_2   = require( ‘./foo\_2.js’ );

function func\_bar\_2 ( sth ) {

return foo\_2.func\_foo\_2( sth );

}

module.exports  = {

func\_bar\_2  : func\_bar\_2,

};

————————————————————————–

// bar\_3.js

async function func\_bar\_3 ( sth ) {

let foo\_3   = await import( ‘./foo\_3.js’ );

return foo\_3.func\_foo\_3( sth );

}

module.exports  = {

func\_bar\_3  : func\_bar\_3,

};

————————————————————————–

// hello\_node.js

(async() => {

let bar\_1   = require( ‘./bar\_1.js’ );

let bar\_3   = require( ‘./bar\_3.js’ );

let foo\_3   = require( ‘./foo\_3.js’ );

async function dosth ( sth, a, b ) {

let bar\_0   = await import( ‘./bar\_0.js’ );

let bar\_2   = await import( ‘./bar\_2.js’ );

let foo\_2   = await import( ‘./foo\_2.js’ );

sth         = sth + ‘ ‘ + bar\_1.func\_bar\_1( a, b );

bar\_0.func\_bar\_0( sth );

let ret\_2   = bar\_2.func\_bar\_2( sth );

bar\_0.func\_bar\_0( ret\_2 );

ret\_2       = foo\_2.func\_foo\_2( sth );

bar\_0.func\_bar\_0( ret\_2 );

let ret\_3   = await bar\_3.func\_bar\_3( sth );

bar\_0.func\_bar\_0( ret\_3 );

ret\_3       = foo\_3.func\_foo\_3( sth );

bar\_0.func\_bar\_0( ret\_3 );

}

await dosth( ‘Hello World’, 5120, 1314 );

await dosth( ‘Webpack Test’, 1234, 5678 );

})();

————————————————————————–

上例涉及静态导入、动态导入、静态导出，但未涉及动态导出，求MD5、SHA256。

cd /path/hello/src

node hello\_node.js

Hello World 6434

2ab71d221778bf89844546711dab751d

2ab71d221778bf89844546711dab751d

f9b5771e0c341ceec6546e44b4d4212930413f185396542628d544618a45149a

f9b5771e0c341ceec6546e44b4d4212930413f185396542628d544618a45149a

Webpack Test 6912

1c4a039a5443cdee3fc425220a46a576

1c4a039a5443cdee3fc425220a46a576

f00ac1bc3e8d90718658228e0c5657c24f55537583fee7527a5e10933657ff27

f00ac1bc3e8d90718658228e0c5657c24f55537583fee7527a5e10933657ff27

☆ 安装webpack开发环境

cd /path/hello

npm init -y (将在当前目录生成package.json)

npm install –save-dev webpack webpack-cli (不要指定-g，将使用当前目录)

npm list

npm uninstall webpack webpack-cli

当前测试版本如下

Node.js v20.11.1

webpack-cli@6.0.1

webpack@5.99.7

☆ 用webpack打包成browser可用代码

1) hello.js

————————————————————————–

// /path/hello/src/hello.js

(async() => {

let bar\_1   = require( ‘./bar\_1.js’ );

let bar\_3   = require( ‘./bar\_3.js’ );

let foo\_3   = require( ‘./foo\_3.js’ );

async function dosth ( sth, a, b ) {

let bar\_0   = await import( ‘./bar\_0.js’ );

let bar\_2   = await import( ‘./bar\_2.js’ );

let foo\_2   = await import( ‘./foo\_2.js’ );

sth         = sth + ‘ ‘ + bar\_1.func\_bar\_1( a, b );

bar\_0.func\_bar\_0( sth );

let ret\_2   = bar\_2.func\_bar\_2( sth );

bar\_0.func\_bar\_0( ret\_2 );

ret\_2       = foo\_2.func\_foo\_2( sth );

bar\_0.func\_bar\_0( ret\_2 );

let ret\_3   = await bar\_3.func\_bar\_3( sth );

bar\_0.func\_bar\_0( ret\_3 );

ret\_3       = foo\_3.func\_foo\_3( sth );

bar\_0.func\_bar\_0( ret\_3 );

}

window.dosth = dosth;

})();

————————————————————————–

从hello\_node.js修改出hello.js，主要区别是，全局导出dosth函数，不在IIFE (

Immediately Invoked Function Expression/立即执行的函数表达式)中直接调用

dosth函数，留待hello.html交互式调用，见后。

2) webpack配置文件

webpack打包时，需要原始js，还需要配置文件，一般名为webpack.config.js

————————————————————————–

// /path/hello/webpack.config.js

let path        = require( ‘path’ );

module.exports  = {

mode: ‘development’,

entry: ‘./src/hello.js’,

output: {

filename: ‘hello.bundle.js’,

path: path.resolve( \_\_dirname, ‘dist’ ),

publicPath: ‘dist/’,

chunkFilename: ‘[name].chunk.js’,

},

resolve: {

fallback: {

“crypto”: false,

},

},

experiments: {

topLevelAwait: false,

},

optimization: {

clean: true,

minimize: false,

},

devtool: ‘source-map’,

};

————————————————————————–

// /path/hello/webpack.config\_1.js

let path        = require( ‘path’ );

module.exports  = {

mode: ‘production’,

entry: ‘./src/hello.js’,

output: {

filename: ‘hello.bundle.js’,

path: path.resolve( \_\_dirname, ‘dist\_1’ ),

publicPath: ‘dist\_1/’,

chunkFilename: ‘[name].chunk.js’,

},

resolve: {

fallback: {

“crypto”: false,

},

},

experiments: {

topLevelAwait: false,

},

optimization: {

clean: true,

minimize: true,

},

devtool: false...