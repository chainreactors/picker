---
title: WEB前端逆向拦截页面跳转
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487787&idx=1&sn=c9f78157d67619339c84a9681a33dbba&chksm=fab2d214cdc55b023bdba2249f75e859c30fccfdfbc65d01e89796fdca9180b197f879ee9063&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-12-08
fetch_date: 2025-10-06T19:38:13.921764
---

# WEB前端逆向拦截页面跳转

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPMeVqMiaRuNvM4CHE6Uwp7XZj6ku4sUPEN9y28T06gEpmxPp0QT9XTTxXXJsOR4hBrJY3hPku40qfg/0?wx_fmt=jpeg)

# WEB前端逆向拦截页面跳转

原创

沈沉舟

青衣十三楼飞花堂

```
创建: 2024-12-05 10:07
更新: 2024-12-07 16:53
https://scz.617.cn/web/202412051007.txt

目录:

    ☆ 背景介绍
    ☆ js跳转页面
    ☆ Object.defineProperty (失败)
    ☆ 渣浪求助
    ☆ beforeunload事件
        1) 方案1 (较重)
        2) 方案2
    ☆ navigate事件
    ☆ AI回答
    ☆ 其他讨论
        1) HookObjectMethod
        2) Tampermonkey要求Developer mode
        3) debug(func)
    ☆ 满足原始需求
```

☆ 背景介绍

云海碰上个URL，没开F12的情况下，访问中途会自动跳转到「aboub:blank」。起初因为其他原因，他没往js反调试上想，出于对浏览器二进制漏洞的敏感，想别的方向去了。

我看了一下目标URL，用「Script First Statement」断点一个个看过去

确认跳转发生时流程位于一个混淆过的js中，obfuscation那种风格的。应该就是反调试代码干的，不知为何误判在F12调试，从而跳转。Babel反混淆js，再Overrides，应该能看出误判原因。这个站有其他选择，不必面对自动跳转，我们也是正常访问，又不是要搞它，所以不考虑反混淆js细究。

我想快速断在目标js中，找到触发跳转的js代码，确认是它导致的，仅此而已。问题演变成一个通用技术问题，知道某页面中途发生跳转，如何快速定位跳转代码所在。

本文记录了提出问题、解决问题的学习过程。吾非WEB前端程序员，本文意义更多是方法论层面的。

☆ js跳转页面

向AI(选自己喜欢的吧)提问，AI回答如下

```
Q:

js将当前页面跳转到「aboub:blank」，大概怎么写？

A:

window.location.href = "about:blank";
window.open( "about:blank", "_self" );

Q:

_self怎么理解，可以是什么值？

A:

_blank  在新窗口或标签页中打开
_self   在当前窗口或标签页中打开 (默认行为)
_parent 在当前窗口父级框架中打开，若页面没有父级，则表现为_self
_top    在最顶层框架中打开，即使嵌套了多个iframe，也会在整个窗口中打开

window.open( "https://www.example.com/", "_blank" );
window.open( "https://www.example.com/", "_self" );
window.open( "https://www.example.com/", "_parent" );
window.open( "https://www.example.com/", "_top" );
```

AI回答，不背书，未查官方文档，可在F12 Console中实测。或有其他方案，但猜测目标js大概率使用前述两种方案之一，更可能是href那种。

☆ Object.defineProperty (失败)

先看一段油猴脚本

```
// ==UserScript==
// @name         Debug Helper
// @namespace    http://tampermonkey.net/
// @version      2024-03-28
// @description  Some helper function
// @author       Me
// @match        https://*/*
// @grant        none
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    function HookObjectProperty ( object, attr ) {
        let prop    = object[attr];

        let getter  = function () {
            console.log( 'Hooking get', object, attr, prop );
            debugger;
            return prop;
        };

        let setter  = function ( value ) {
            console.log( 'Hooking set', object, attr, value );
            debugger;
            prop    = value;
        };

        Object.defineProperty( object, attr, {
            get: getter,
            set: setter,
            enumerable: true,
            configurable: true
        });
    }

    HookObjectProperty( document, 'cookie' );
})();
```

油猴脚本的好处就是尽早Hook，防止目标js先下手为强。关于先下手的事，参看:

《WEB前端逆向反反调试一例》

```
https://scz.617.cn/web/202406281614.txt
```

不用Tampermonkey，直接在F12 Console中输入HookObjectProperty()的代码也成，只是对付不了先下手的情况。

在Console中测试

```
document.cookie = 'key:value';
```

设置cookie时会断下来，可查看调用栈回溯。

在Console中测试

```
HookObjectProperty( window.document, 'location' );
HookObjectProperty( window, 'location' );
HookObjectProperty( window.location, 'href' );
```

报错

```
Uncaught TypeError: Cannot redefine property: location
Uncaught TypeError: Cannot redefine property: href
```

AI忽悠，window.location是一个特殊对象，该对象的属性如href、protocol、host等，由浏览器严格控制，许多属性被设计为只读或受限可写，以保证安全性。虽然可通过直接赋值「window.location.href = …」改变页面地址，但这实际上调用了浏览器实现的底层逻辑，而不是直接对href属性赋值。

在浏览器中，window.location.href的descriptor(属性描述符)是不可配置的，这意味着你无法使用Object.defineProperty来重新定义它。

在Console中执行

```
Object.getOwnPropertyDescriptor( window.document, 'location' )
Object.getOwnPropertyDescriptor( window, 'location' )
Object.getOwnPropertyDescriptor( window.location, 'href' );
```

均返回

```
{
    configurable: false,
    enumerable: true,
    get: f,
    set: f
}
```

configurable为false，此时不能使用Object.defineProperty重新定义它。get和set是由浏览器内置实现的，无法覆盖这些内置的getter和setter。

这都AI忽悠的，谨慎对之。

☆ 渣浪求助

前一小节失败后，不想放狗，偷懒直接在渣浪求助。向人提问，向AI提问，本身就是个技术活，我是这么问的:

*请教个WEB前端调试的问题*

*想Hook如下操作*

*window.location.href = "something";*

*已经尝试过Object.defineProperty，提示*

*Cannot redefine property: href*

*原始需求是，有js在设这个，但不知道在哪儿设的，想拦截这个操作，断下来，查看调用栈回溯。*

目标js可能并非用此法，但这是个通用问题，即便解决不了目标js，有答案也是好的。

☆ beforeunload事件

网友UID(3110320275)提供了两组解决方案，第二组是他参考另一网友解答后对第一组的改进，从学习角度全部展示于此，因为我觉得过程与结果同样重要。需要特别感谢的是，他提供了理论说明，同时提供了具有可操作性的测试步骤。与之对比，这么多年在网上见识过太多「每个字都认识」系列，老虎吃天、无处下爪的那种。虽说谁都没有义务掰碎了喂到谁嘴里，但能提供有效帮助时，我个人是不吝多写几句的。

1) 方案1 (较重)

a. 写一个beforeunload事件监听方法，在Console中输入进去
b. 在F12 Sources面板启用「Event Listener Breakpoints->Load->beforeunload」
c. 触发页面跳转行为，查看调用栈回溯

步骤a代码如下

```
window.addEventListener(
    'beforeunload',
    function ( event ) {
        /*
         * 这些console.log无所谓
         */
        console.log( window.location.href );
        console.log( event );
        /*
         * 若有这句，F8继续时Chrome弹框提示Leave或Cancel。若无这句，F8继续
         * 时不弹框提示，直接跳转。若只为查看调用栈回溯，并不打算阻止跳转，
         * 不需要这句。
         *
         * 上面是一般情况。云海那个目标URL似乎存在某种对抗措施，即使有这句，
         * Chrome也不弹框提示Leave或Cancel，而直接跳转，暂不清楚原因。
         */
        event.preventDefault();
    }
);
```

步骤c可在Console中输入

```
window.location.href = "about:blank";
```

步骤b所设断点命中，停在function(event)的入口代码处，上例就是第一条log()处。此时调用栈的上一层就是「window.location.href = …」。

离开function(event)后，Chrome弹框提示Leave或Cancel，前者完成跳转，后者放弃跳转。若放弃跳转，可重复步骤c，再次测试整个流程。

2) 方案2

a. 写一个beforeunload事件监听方法，在Console中输入进去
b. 触发页面跳转行为，查看调用栈回溯

步骤a代码如下

```
window.addEventListener(
    'beforeunload',
    function ( event ) {
        event.preventDefault();
        debugger;
    }
);
```

步骤b可在Console中输入

```
window.location.href = "about:blank";
```

相比方案1，略去原步骤b，用debugger语句断下来，操作更简洁。

☆ navigate事件

网友UID(6161718960)在github提供基于navigate事件的解决方案，参看

```
https://github.com/LingYanSi/blog/issues/167
```

---

```
/*
 * 通过js触发的页面跳转
 */
navigation.addEventListener(
    'navigate',
    ( event ) => {
        console.log( event );
        /*
         * 若有这句，F8继续时不跳转。若无这句，F8继续时发生跳转。若只为查
         * 看调用栈回溯，并不打算阻止跳转，不需要这句。
         *
         * 对href而言，navigate事件在beforeunload事件之前，若有这句，后续
         * 触发beforeunload事件，若无这句，后续不会触发beforeunload事件。
         */
        event.preventDefault();
        debugger;
    }
);
```

---

```
/*
 * 通过a/form标签触发的页面跳转
 */
window.addEventListener(
    'click',
    ( event ) => {
        const findParent = ( d, check ) => {
            while ( d ) {
                if ( check( d ) ) {
                    return d;
                }
                d = d.parentElement;
            }
            return null;
        }
        const dom = findParent( event.target, (d) => /^(a|form)$/i.test(d.tagName) );
        dom && console.log( 'dom element', dom );
    },
    {
        capture: true
    }
)
```

在Console中测试

```
window.location.href = "about:blank";
```

测了第一段代码，满足原始需求。第二段代码未碰上测试场景，备忘。

若不用debugger语句，可仿照beforeunload方案1

a. 写一个navigate事件监听方法，在Console中输入进去
b. 在F12 Sources面板启用「Event Listener Breakpoints->Load->navigate」

```
navigation.addEventListener(
    'navigate',
    ( event ) => {
        console.log( event );
        event.preventDefault();
    }
);
```

---

```
Event Listener Breakpoints
  Load
    navigate
```

---

```
window.location.href = "about:blank";
```

看明白了，这些「Event Listener Breakpoints」有相应事件监听方法时才会生效，否则只在GUI中勾选这类断点，没用。

基于这种思路，对href额外测了hashchange、popstate事件，未断下来。

下面是navigate事件先于beforeunload事件的验证方案

```
navigation.addEventListener(
    'navigate',
    ( event ) => {
        debugger;
    }
);

window.addEventListener(
    'beforeunload',
    function ( event ) {
        event.preventDefault();
        debugger;
    }
);

window.location.href = "about:blank";
```

☆ AI回答

在渣浪求助前，我问AI，在F12调试中想拦截这种跳转操作，但不知具体位置，如何做？它建议用Object.defineProperty。我说这扯呢，它转而建议用ES6 JS Proxy，同样给了理论上就不可行的代码。

渣浪求助后，我新开会话问AI，用了Markdown的三个反引号

```
Event Listener Breakpoints
  Load
    beforeunload
```

这个断点什么时候命中？

这次GPT-4o的回答明显靠谱些

a. 什么是beforeunload事件

beforeunload是一个浏览器事件，在即将离开当前页面(例如刷新/关闭标签页、导航到另一个页面)时触发。其主要用途是允许开发者在用户离开页面之前执行某些操作，或者提示用户确认是否真地要离开页面。

b. 什么时候会触发beforeunload断点

当页面中的代码中监听了beforeunload事件时，浏览器会在以下情况下命中断点

b.0 用户操作触发页面卸载

刷新页面
关闭当前标签页或浏览器窗口
通过链接或输入新URL导航到另一个页面

b.1 代码主动触发页面卸载

在js中修改window.location.href或调用window.location.replace()
调用window.history.back()或window.hist...