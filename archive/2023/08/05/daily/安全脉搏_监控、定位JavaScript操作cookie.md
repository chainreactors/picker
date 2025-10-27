---
title: 监控、定位JavaScript操作cookie
url: https://www.secpulse.com/archives/202892.html
source: 安全脉搏
date: 2023-08-05
fetch_date: 2025-10-04T12:00:19.144268
---

# 监控、定位JavaScript操作cookie

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 监控、定位JavaScript操作cookie

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[CC11001100](https://www.secpulse.com/newpage/author?author_id=50049)

2023-08-04

48,436

# 监控、定位JavaScript操作cookie

## 一、脚本说明

### 为什么会有这个东西？

数据无价的时代，爬虫与反爬的对抗已经进入白热化状态，其中Cookie反爬是`最常见之一`的反爬类型， 网站方通过混淆得亲妈都不认识的JS代码设置Cookie（通常是浏览器指纹、请求时必须带上的Cookie之类的），

面对请求时必须要带上但是又不知道在哪里生成的Cookie， 你在几万行混淆的亲妈都不认识的JS屎海中苦苦挣扎希望能找到生成Cookie的地方（要是逆向思路不科学兴许还会呛上几口...），

甚至几度想找个借口骗自己放弃，或者要不干脆用Selenium之类的浏览器模拟方式算了？ 怂个球，此脚本就是来助你一臂之力的！ （你我都知道，这段只是撑场面的废话，你可以略过，如果你没有不幸读完的话...）

### 脚本功能

本脚本的功能大致分为两个部分：

- monitor： 监控所有JS操作cookie变化的动作并打印在控制台上

- debugger: 在cookie符合给定条件并且发生变化时打debugger断点

### Hook生效的条件

- 需要本脚本被成功注入到页面头部最先执行，脚本都未注入成功自然无法Hook

- 需要是JavaScript操作document.cookie赋值来操作Cookie才能够Hook到 （目前还没碰到不是这么赋值的...）

### 使用须知

本脚本是通过将自己的JS代码注入到页面，Hook住`document.cookie`来完成各种功能， 因此在使用本脚本之前要先确定要搞的Cookie确实是通过JS生成的

（后面介绍了一种非常简单的确定Cookie是JS生成还是服务器返回的方式）。

## 二、有何优势？

## 2.1 不影响浏览器自带的Cookie管理

目前很多Hook脚本Hook姿势并不对，本脚本采用的是一次性、反复Hook，对浏览器自带的Cookie管理无影响：

![https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img.png](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img.png)

## 2.2 功能更强：监控Cookie变化

除了cookie断点功能之外，增加了Cookie修改监控功能，能够在更宏观的角度分析页面上的Cookie：

![https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_1.png](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_1.png)

（算了，放弃打码了...）

颜色是用于区分操作类型：

- 绿色是添加Cookie

- 红色是删除Cookie

- 黄色是修改已经存在的Cookie的值

每个操作都会跟着一个code location，单击可以定位到做了此操作的JS代码的位置。

## 2.3 功能更强：打断点时细分变化类型

从v0.6开始引入了功能更强大并且配置更灵活的断点规则，引入事件机制， 将Cookie修改细分为增加、删除、更新三个事件，支持更细粒度的打断点， 关于Cookie事件，详情请参阅本文第五部分。

关于为什么要这样设计？ 一种比较常见的情况，目标网站有反爬的Cookie是JS设置的， 但是JS代码的逻辑是先疯狂的删除，然后删除好多次之后才添加真正的值， 这种方式设置Cookie正好能反制一般的Cookie Hook调试。

这里是其中一个例子，比如F5的Cookie保护，有一个Cookie `TS51c47c46075`，它就是先被删除好多次，然后再被添加一次：

![](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/README\_images/20f986d7.png)

这种情况下可以针对\*\*添加\*\*名为`TS51c47c46075`的Cookie事件打一个断点， 就可以避免那些红色的删除事件混淆视听。

## 三、 安装

### 3.1 安装油猴插件

理论上只要本脚本的JS代码能够注入到页面上即可，这里采用的是油猴插件来将JS代码注入到页面上。

油猴插件可从Chrome商店安装：

[https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)

如果无法翻墙，可以在百度搜索“Tampermonkey”字样寻找第三方网站下载，但请注意不要安装了虚假的恶意插件，推荐从官方商店安装。

其它工具亦可，只要能够将本脚本的JS代码注入到页面最头部执行即可。

### 3.2 安装本脚本

安装油猴脚本可以从官方商店，也可以拷贝代码自己在本地创建。

#### 3.2.1 从油猴商店安装本脚本

推荐此方式，从油猴商店安装的油猴脚本有后续版本更新时能够自动更新，本脚本已经在油猴商店上架：

[https://greasyfork.org/zh-CN/scripts/419781-js-cookie-monitor-debugger-hook](https://greasyfork.org/zh-CN/scripts/419781-js-cookie-monitor-debugger-hook)

#### 3.2.2 手动创建插件

如果您觉得自动更新太烦，或者有其它的顾虑，可以在这里复制本脚本的代码：

[https://github.com/CC11001100/js-cookie-monitor-debugger-hook/blob/main/js-cookie-monitor-debugger-hook.js](https://github.com/CC11001100/js-cookie-monitor-debugger-hook/blob/main/js-cookie-monitor-debugger-hook.js)

review确认没问题之后在油猴的管理面板添加即可。

## 四、监控Cookie的变化（monitor）

### 4.1 基本用法

注意，监控是为了在宏观上有一个全局的认识，并不是为了定位细节 （通常情况下正确的使用工具才能提高效率哇，当然一个人的认知是有限的，欢迎大家反馈更有意思的玩法）， 比如打开一个页面时：

![https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_1.png](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_1.png)

根据这张图，我们就能够对这个网站上哪些cookie是JS操作的，什么时间如何操作的有个大致的了解。

### 4.2 基本用法进阶

再比如借助monitor观察cookie的变化规律，比如这个页面，根据时间能够看出这个cookie每隔半分钟会被改变一次：

![https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_2.png](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_2.png)

### 4.3 过滤打印信息，只查看某个Cookie的变化

（2021-1-7 18:27:49更新v0.4添加此功能）： 如果控制台打印的信息过多， 可以借助Chrome浏览器自带的过滤来筛选，打印的日志的格式已经统一，只需要`cookieName = Cookie名字`即可， 比如：

![https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_9.png](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_9.png)

请注意，搜索时要保证你的搜索信息是URL解码了的，否则可能会不匹配， 因为控制台的打印信息都是先URL解码再打印的。

### 4.4 过滤打印信息，快速确定Cookie是否是JS本地生成的

如果你不确定要搞的Cookie是本地生成的还是某个请求服务器`set-cookie`返回的， 则可以把本脚本打开，然后刷新目标网站的页面，然后在控制台搜索Cookie名字即可，

方法与上一节类似，当Cookie的名字比较短没有标识性的时候可以加`cookieName`辅助定位，比如：

```text

cookieName = v

```

### 4.5 减少冗余信息（不推荐）

有时候目标网站可能会反复设置一个cookie，还都是同样的值，这个变量用于忽略此类事件：

![https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_8.png](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/img\_8.png)

一般保持默认即可。

## 五、 定位Cookie的变化（debugger）

```@since v0.6 ```

此部分的文档适用于v0.6+版本，如果您本地的版本小于0.6，请升级版本后再来阅读文档。

从v0.6开始，在Cookie的值发生改变时打断点变得很复杂，也变得很简单， 复杂是因为引入了事件机制，简单是因为简化了断点规则配置更灵活。

断点规则可以分为`标准规则`和`简化规则`，标准规则是程序底层方便实现处理的， 简化规则是为了用户更方便地配置，通常情况下您只需要了解简化规则就可以了， 当简化规则配置无法满足需求时再来查阅标准规则如何配置。

#### 5.1 debuggerRules

所有的规则都是配置在`debuggerRules`数组中的，在脚本的头部有一个变量：

![](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/README\_images/45ecea34.png)

如果找不到的话，可以按Ctrl+F按变量的名字搜索：

```js

debuggerRules

```

这个变量是一个数组类型，里面存放着一些规则条件，来决定什么情况下会进入断点。

注意，这是一个数组，数组中的规则是或的关系，触发Cookie修改事件时， 会顺序匹配每条规则， 只要有一条规则匹配成功就会进入一次断点。

### 5.2 常用配置方式（简化的配置规则）

#### 5.2.1 Cookie名字过滤

当名为`foo`的Cookie发生变化时进入断点：

```js

const debuggerRules = ["foo"];

```

上面这种方式指定一个字符串，会按照Cookie名字等于给定的字符串去匹配。

注意，此处的完全匹配如果有被URL编码的部分也需要先URL解码再粘贴到这里， 其它涉及到字符串的地方都一样后面不再赘述。

如果Cookie的名字中包含一直变化的部分，比如时间戳、UUID之类的， 通过名字已经无法定位，则通过正则匹配：

```js

const debuggerRules = [/foo.+/];

```

绝大多数情况只需要这两种配置就够了。

下面来实践一下，当打开这个页面

[https://www.ishumei.com/trial/captcha.html](https://www.ishumei.com/trial/captcha.html)

能看到脚本检测到了一些Cookie操作：

![](https://raw.githubusercontent.com/JSREI/js-cookie-monitor-debugger-hook/main/images/README\_images/36eb394d.png)

...