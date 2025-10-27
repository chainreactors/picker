---
title: 拦截 Chrome DevTools Protocol 实现忽略与自定义 debugger
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141388&idx=1&sn=b7f552ac87aeb5eb013223371f68bf55&chksm=bd50a5588a272c4eeb6b4593d15aeeefc6fbe0350b021c6a1c27edcc1aa2cc92cc63f874ff7e&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-09-25
fetch_date: 2025-10-06T18:27:02.243590
---

# 拦截 Chrome DevTools Protocol 实现忽略与自定义 debugger

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaRGD4B2os7wjEPvYAQ4DZoibcMsCeHicmxD2bib1gkE9w6jDSZKc86sR8Q/0?wx_fmt=jpeg)

# 拦截 Chrome DevTools Protocol 实现忽略与自定义 debugger

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：LoveCode**

这次不是斗法、是锻造法器啦。

使用本文的方案，可以在 `Edge、Chrome` 浏览器上忽略 `debugger` 语句，同时可以定义属于自己的 `debugger` —— 而且不影响代码的可移植性哟。

这是本文的结构：

1. 本方案的缺点 —— 至关重要，必看内容！
2. 项目的使用方式 —— 我知道你很急，所以放在了前面
3. 网站检测调试的原理与绕过 —— 安心地打开开发者工具
4. 简述本文方案的原理

# 本方案的缺点

使用本方案需要以下步骤：

* 打开浏览器的远程调试功能。
* 安装一个浏览器插件，由项目提供，有以下辅助作用：

+ 快速打开单独的开发者工具，并不是按 `F12` 键打开的那个版本哟。
+ 自动插入与取消自定义的 `debugger` 语句。
+ 与标签页关联 —— 标签页关闭时自动关闭开发者工具等等。

* 需要点击插件打开新的开发者工具使用，不能使用按 `F12` 键显示的那个版本。
* 启动一个服务器 `cdp server`，由项目提供，它是最核心的部分。

上述操作可以在需要过 debugger 时再快速启用，如果能接受以上繁杂的步骤，可以继续阅读下文了。

# 项目的使用方式

本文以 `Chrome` 浏览器为例进行展示，`Edge` 浏览器的配置也是一样的。

## 基本配置

### step 1

访问项目，获取源代码：Hosinoharu/SkipJSDebugger。在 `Releases` 中的文件根据后文说明按需求下载。

### step 2

修改浏览器的启动参数为如下情形，然后打开浏览器。

```
 复制代码 隐藏代码
// chrome.exe --remote-debugging-port=9222 --remote-allow-origins=localhost

// --remote-debugging-port 启动远程调试端口，暂时定为 9222，后续可以手动修改
// --remote-allow-origins 远程调试时允许连接的来源，建议设置为 localhost。使用 * 运行任何来源
```

项目中提供了一个 `powershell` 脚本，位于 `scripts\debug_browser.ps1`，可以等到需要的时候再快速启动浏览器。不过使用之前需要填入本机浏览器的位置。

```
 复制代码 隐藏代码
# 找到脚本的这个位置，修改这两个变量的值为本机的浏览器的路径
$Edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$Chrome = "E:\Google\Chrome\Application\chrome.exe"
```

基本使用如下：

```
 复制代码 隐藏代码
# 首先修改 powershell 执行脚本的权限
Set-ExecutionPolicy RemoteSigned

# 然后按需执行下面任意一条命令打开浏览器，注意！执行 ps 脚本时需要加上路径哟
.\debug_browser.ps1             # 默认打开 Chrome 浏览器，远程调试端口为 9222
.\debug_browser.ps1 -Port 8888  # 默认打开 Chrome 浏览器，远程调试端口为 8888

.\debug_browser.ps1 Edge               # 打开 Edge 浏览器，远程调试端口为 9222
.\debug_browser.ps1 Edge -Port 8888    # 打开 Edge 浏览器，远程调试端口为 8888
```

### step 3

手动添加插件 `OpenDevtoolsPage`，其位于项目根目录。在浏览器地址栏输入 `chrome://extensions/` 打开界面，然后如下进行添加：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaASibGp1ib5hPfM7fYI01YooYMv6jr3TRp9Qvmicx8dzoyNIYMpI9rPg5Q/640?wx_fmt=png&from=appmsg)

### step 4

运行 `cdp server`，位于项目的 `cdp_server` 目录中，共有两个版本。

* `Python` 实现。最初的版本，使用此版本时，每次打开浏览器开发者工具时它都会发动时间法则，硬控我一秒，所以后续使用 Go 重写。如果没有 Go 环境，可以用这个版本。
* `Go` 实现。可以自己从源代码编译，也可以在 `Releases` 中下载编译好的版本 —— 仅限于 `windows 10`。

下图本机的处理效果。提交到 `Github Releases` 的文件 `SHA256 hash`：`F96B7896A2ED14BC088DCB37B030F2C6A2B81E559FEE9DA632695B498C2E97EA`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoa1rwh6UW2FXcStjlSiamO5R4libjbZfO85oFnbtGvr5KmO3Ie81HDn91Q/640?wx_fmt=png&from=appmsg)

### step 5

测试效果。先打开项目的 `test/test_debugger.html` 文件，然后按下述步骤测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaOuHYS0iaKryswnOzaiaQuib1Dzv077ia04lkmtP6XPeVCqVOoshxupqPGw/640?wx_fmt=png&from=appmsg)

然后*关闭刚刚打开的开发者工具，刷新网页*，继续下面的操作。

> 注：现在给插件换了个图标，所以和下图会有些区别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoa14c7FLribO2esd3nuyPoxYC31R4dIRhibw3bgSibSnNZVMwGVr913fu7g/640?wx_fmt=png&from=appmsg)

如果以上过程顺利，那么现在可以忽略其它网站的 `debugger` 语句了。

## 关于插件打开的开发者工具

确保点击插件 `OpenDevtoolsPage` 打开新的开发者工具时，*要关闭由 `F12` 键等方式打开的、原版自带的开发者工具*，否则在显示上一定会出现问题 —— 因为出现了两个开发者工具调试网站。

* 简单而言，只保留由插件打开的开发者工具。
* 如果懂编程概念，这种情况类似*两个多线程读写同一个变量*。

如果点击插件打开开发者工具后，出现这样的信息，说明程序可能出错了，先检查上述的步骤，如果依然未能解决问题，可以在评论区说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaDzLL38aGxXQwYVyZjs1wQQGrSG689KmZxSwKunwze1BR05skgm3Wzw/640?wx_fmt=png&from=appmsg)

### 补充说明

内嵌的开发者工具就是按 `F12` 键打开的那个版本，它的链接是 `devtools://devtools/bundled/inspector.html`，在浏览器中可以输入该链接进行访问。

本来是使用这个进行调试的，经过测试它会造成浏览器闪退（是浏览器突然就消失了，并不会弹出一个警告框告诉我浏览器已经崩溃），所以使用了远程调试的版本，即 `localhost:port/devtools/inspector.html` 这个版本。

这带来一个问题：得重新设置一下开发者工具，我指的是一些设置项、布局等需要重新设置一下。

## 自定义 debugger

默认情况下 —— 指的是：启动 `cdp_server`，并且用插件打开开发者工具，浏览器会忽略普通的 `debugger` 语句，且只会在 `lovedebug()` 函数的下一行断住 —— 其它的手动断点、条件断点均不受影响啦。

即默认情况下使用 `lovedebug()` 函数作为预定义的 `debugger`，下面展示如何使用它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaTbcEorXm9NxtCodRXoyEbpecYiaPN9RSezgOgQaFiaThEicBwCibjWmazw/640?wx_fmt=png&from=appmsg)

如果需要设置独属于自己的 `debugger`，比如取名为 `hello_world`，那么请按照以下步骤进行。

第一步，修改 `cdp server`。

如果使用 `Python` 实现的版本，修改 `cdp_server/py/settings.py` 的这里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaErDl0TtqbV1UlktGiaEicKdKErFViavaF5MZwuSkkFlKS1ZSpAX6p1e2w/640?wx_fmt=png&from=appmsg)

如果是使用 `Go` 实现，后续执行程序时传参： `cdp_server.exe -debugger hello_world` 即可，也可以自行修改源代码进行编译。*另外，使用 `cdp_server.exe -h` 可以查看有哪些参数*。

第二步，修改 `OpenDevtoolsPage` 插件的配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoatiayDZBsrNAMNEeOQEOWibwcYqbjngaxeO9EfULWj66Hoibz2EfTBsuyw/640?wx_fmt=png&from=appmsg)

## 自定义端口

总共有 2 个端口可以自定义。

*一个是浏览器的远程调试端口*，默认使用的 `9222`。如果要修改它，比如修改为 `8888`。

首先要修改 `Chrome` 的启动参数 `--remote-debugging-port=8888`。如果使用上述的 PS 脚本时需要传参。

对于 `cdp_server`：

* 使用 Python 版本，在 `cdp_server/py/settings.py` 中修改变量 `WEB_SOCKET_PORT` 的值为 `8888`。
* 是 Go 版本，启动时传入参数： `cdp_server.exe -port 8888`。

然后打开 `OpenDevtoolsPage` 插件的设置项做相应的修改。

*一个是 `cdp_server` 的端口*，默认使用的是 `9221`。如果要修改它，比如修改为 `8887`。

对于 `cdp_server`：

* 使用 Python 版本，在 `cdp_server/py/settings.py` 中修改变量 `CDP_SERVER_PORT` 值为 `8887`。
* 是 Go 版本，启动时传入参数： `cdp_server.exe -cdp 8887`。

然后打开 `OpenDevtoolsPage` 插件的设置项做相应的修改。

# 网站检测调试的原理与绕过

现在去除了 `debugger` 语句，网站还有一些检测控制台是否打开的方式，在项目中有一个 JS 文件，其位于  `scripts\anti_dev_detector.js`，它就是为了去除这些检测。

因为整个项目，额……略显鸡肋？所以我将它单独拿了出来，请将它放在油猴插件中运行。

在 `test\test_console.html` 文件中整理了我搜索到的检测方式，下面阐述相关的检测逻辑与处理。

## 利用 Console API

如果是使用 `Console API` 进行检测，那么将其 `Hook` 并改为空函数即可。当然还有一些检测被 `Hook` 的方式，常见的是检测 `.toString()` 返回结果。

我建议不要使用以下方式进行 hook：

```
 复制代码 隐藏代码
const raw_log = console.log;
console.log = function log() {}
// 省略其它的步骤，如增加 toString()、或者添加属性描述符等等
```

建议利用 `Proxy API` 进行 hook：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaE65RCxqR5yGrzlBdg0iaYBCAah4oVNIaDpwsHSAcI5DplEubbp31TNg/640?wx_fmt=png&from=appmsg)

这样处理 `.toString()` 检测就方便了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoasiaBB2Jw0V9DGsQUmwSqu44qMDJ2LqysQamkA5LQ6II6via33Zgd4B6g/640?wx_fmt=png&from=appmsg)

如下是测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoaKRJMh7zwW9PN7AY0pLSSzHIDpTvRD1IXiaukPrRv0CSBP7krXibicvibFw/640?wx_fmt=png&from=appmsg)

## 报错式检测

这种检测方案来自 `https://www.bilibili.com/video/BV1Gi421C7Rz`，核心思想是添加属性描述符 `getter`，所以通过 `Hook Object.defineProperty、Object.prototype.__defineGetter__` 等函数可以过掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoadyFFoxwVbmptgEqU3ja4CiahCoEgbL6Y4A76Cl61biaDo92vgpBvX15g/640?wx_fmt=png&from=appmsg)

在 `test/teset_console.html` 文件中已经加入了这种检测。

请注意，一些前端框架可能利用这种方式进行错误日志记录等等，所以如果网站功能出现异常，应该禁用脚本。

## 其它检测方案

基于 `debugger` 语句的检测方案现在可以忽略不谈了，比如下面这种：

```
 复制代码 隐藏代码
const a = new Date;
debugger;
const b = new Date;
if ((b - a) > 10) {
    alert("检测到啦")
}
```

还有检测 `F12` 按键、浏览器窗口的大小变化的检测方案也不用谈了，因为现在是点击插件打开的浏览器开发者工具。

其它的大都是利用 `Console API`，比如下面这种形式。

```
 复制代码 隐藏代码
const re = /x/;
re.toString = function () {
    alert("检测到啦");
}
console.log(re);
```

还有这种形式的递归循环 + debugger，本质上还是利用的 debugger。

```
 复制代码 隐藏代码
setInterval(function() {
  check()
}, 4000);

var check = function() {
  function doCheck(a) {
    // 无论进入哪个分支都会调用 debugger 语句
    if (("" + a/a)["length"] !== 1 || a % 20 === 0) {
      (function() {}
      ["constructor"]("debugger")())
    } else {
      (function() {}
      ["constructor"]("debugger")())
    }
    doCheck(++a)   // 这里递归调用
  }

  // 一直调用，直到堆栈溢出出错，然后进入 catch 块中
  try {
    doCheck(0)
  } catch (err) {}
};

check();
```

目前我所搜索到的、稳定的检测方案就这些了。

# 本方案原理

仅图示原理，并未从代码上详细解释。

## 关于 Chrome Devtools Protocol

`Chrome Devtools Protocol` 简称 `CDP`，是一种通信协议，通常使用 `websocket` 进行传输。

简单描述为如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZImQiaDpHanib2kbySeZMHXoanBIWs4f1RErUqrb5zw42vqtqdKO2NdL6vTb9asAmLRMFiaP2v9geiajA/640?wx_fmt=png&from=appmsg)

如何理解呢？

1. 按 `F12` 键能打开开发者工具界面，将它单独分离出来。
2. 继续按 `Ctrl+Shift+I` 还能打开它的开发者工具。
3. 然后就能看到原来的那...