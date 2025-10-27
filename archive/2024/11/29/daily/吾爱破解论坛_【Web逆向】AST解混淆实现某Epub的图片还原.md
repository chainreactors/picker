---
title: 【Web逆向】AST解混淆实现某Epub的图片还原
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141535&idx=1&sn=b41c794f7c204d46ef8e50d94b657ade&chksm=bd50a5cb8a272cdd419d0a2cd34af514580aa986c9f4268ed9fc382f55304ac43610b64e1796&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-11-29
fetch_date: 2025-10-06T19:17:27.430898
---

# 【Web逆向】AST解混淆实现某Epub的图片还原

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJxs34guur6PntYDl0d8DNReicTwMlujS1ibT3jWGKa10pQS4AdO6icEIR7xrxK64HKVicicN851WymsyA/0?wx_fmt=jpeg)

# 【Web逆向】AST解混淆实现某Epub的图片还原

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：T4DNA**

### 免责声明

1、本贴仅作为技术讨论，本人不会利用以下技术盈利、或从事任何侵害该网站的行为。
2、如觉得此贴不妥，请联系本人将第一时间删除。

### 背景

使用的xhtml文件和img均在附件中。

某网站下载的漫画epub使用calibre等常规阅读器阅读不便，出现白屏，无法下拉等情况。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRHXg6YBNtvsjMHrSf6g8iadB2PBKFwJVhu8XoNUw1ERREKtI3ibkxwCJA/640?wx_fmt=png&from=appmsg)

epub文件本质是压缩包，文字为xhtml文件，图片放在Image文件夹下。

解压发现该epub每一章节的xhtml是乱七八糟一堆，而Image则为分割的图片，不仅乱序，还有反过来的。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRt578zUyovNxNiaPK650eA72xSOiaTKQiaT7s56bGFDg1gOLhgvbg11jMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJxs34guur6PntYDl0d8DNRKtIf4tiasia9I7mNDdZ8qOMu8e678op3DBX1QCY1PbJY0KhbtpXWfffA/640?wx_fmt=jpeg&from=appmsg)

通过浏览器打开这个网页，即可正常显示图片。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRakic4E6rYqqYjCzkOqxCt3rTrAo4hY8cnRTG8ovUcUcbZwA4QLN4yeg/640?wx_fmt=png&from=appmsg)

### xhtml改为html

代码有混淆，不是一目了然的，所以得动态调试。

浏览器虽然可以打开xhtml，但是js代码被CDATA区域包裹，只是Xhtml代码用于忽略语法错误的。

尽管浏览器可以正常解析，但是不方便下断点，故删除CDATA包裹，并且将xhtml改为html后缀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRiak8fjK1VlxEmI1eIkgQvCSKkYn2KR6LqbiaTQ6ibBibPsdkZvIu9Mep6w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRib847CFvSpF0fOkJL3icSQn3cX7rThFnZPFKAqZWGFY63ian8hyFX0uiag/640?wx_fmt=png&from=appmsg)

### AST解混淆

html结构包含两个javascript块，第一个块仅仅定义了一个\_\_animations\_\_变量。animations是动画的意思，猜测应该是包含了图片的打乱/还原信息。

它看起来是一个base64字符串，猜测是对称加密的产物，大概率是AES。

第二块是主要的程序，用于解析\_\_animations\_\_并且完成图片的还原操作。

第二块首先定义了一个lnT9，然后是一个自执行函数，后面的代码中则使用了大量的lnT9.XXX(NNN)，显然是一种字符串替换的混淆，而中间一大坨的自执行函数则是对lnT9的定义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRWnnOoOms2HImE0MoTq19z5AME5vTCCX1fTWS2t9iavjibYLwK9rKzK1w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRrvsia2E8edt9fzhuNzzcEyicXH14wJRDyIEwdR7BereEia2GlAbQVXj1w/640?wx_fmt=png&from=appmsg)

那么自执行函数是如何定义lnT9的呢？打开发现首先是一个eval，将字符串转为代码，那么我们把return断住，步进进入解析出的vm代码中，发现也是混淆过的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRGnGwh8HQ9R2bysyxBic8gSTC0icZ6WdXo1iakVPLCWe4H3VWYnmyWmHHg/640?wx_fmt=png&from=appmsg)

不过我们无需进行解混淆，因为两个混淆的函数都被用于解析那一坨字符串，最后的结果z8Ke仍然是字符串，还要再通过一次eval生效，所以我们只需断住z8ke即可获取最终运行的代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRw6r5HzicwnPHB9FfyDdFjy092ibb5CmUAXdH9r1vCkp4AYWV2zIZluqA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNR18YrFBBHyjCNfIVHbIRkJY8DRWGGSnwBZVWlpMjfBEQZMOvBZ3GBWQ/640?wx_fmt=png&from=appmsg)

结果这又是一段混淆的代码，不过我们之前已经分析过了，所有这段代码的根本目的应该只是定义一堆函数用于后面的主逻辑混淆，所以实际上我们无需关心这段代码的实现（后面打脸）。只需要对后面主逻辑的函数进行解混淆。

### ①字符串加密函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRyTfEgSriaoM5bmqSQXWaFrN9ao2o36XxyZ6Zh5XAFNBrDjmvUU7XeFg/640?wx_fmt=png&from=appmsg)

lnT9.函数(数字)显然是一种的字符串加密，虽然函数名字各不相同，但是实际上并没有出现不同偏移的情况，本质上都是对同一个数组的取值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRaJ6RPHGCwicOibc2OCgQia9yvRZ7fVDBh4fCU4fl24S1VPX3fx7wXmjGg/640?wx_fmt=png&from=appmsg)

因此我们只需要关心这个数组就可以将所有相关函数解混淆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNR0bQYA7AJ4vwGcShFtuPbF9hhdkCe0uVrCV1CjAVxjVrywqZdudQDQQ/640?wx_fmt=png&from=appmsg)

我们将第二块js代码保存为comp.js，并编写函数用于解混保存为decomp\_.js。对于所有的MemberExpression，如果Object的Identifier是lnT9且参数为Literal一律替换成\_0x00031C的X位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRibkCQlHmQ85ndnzLX9zHmDm4iba67TT3yPOr5Nwpdo5Bibk4XxBjD3zFg/640?wx_fmt=png&from=appmsg)

```
 复制代码 隐藏代码
traverse(ast, {
    CallExpression(path) {
      const { callee, arguments: args } = path.node;
      if (
        types.isMemberExpression(callee) &&
        types.isIdentifier(callee.object, { name: "lnT9" }) &&
        args.length === 1 &&
        types.isNumericLiteral(args[0])
      ) {
        const index = args[0].value;

        const replacementValue = _0x00031C[index];

        if (replacementValue !== undefined) {
          path.replaceWith(types.stringLiteral(replacementValue));
        }
      }
    }
});
```

运行后成功替换了所有的字符串加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRlJnQicDN8A2bWVwiaW2VKBqpfvYvaC4icDOicNTJSK8uzF52H0iaYcINgsQ/640?wx_fmt=png&from=appmsg)

### ②常量还原

注意到很多case使用了-， ^ 表达，实际上两边都是常量，结果也是一个常量，我们可以直接替换成计算结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRg5GnjRialdSrYHCe5NStjCQKicMNFicwaBZeU3dicIfJia5s3l8nZZAickYQ/640?wx_fmt=png&from=appmsg)

```
 复制代码 隐藏代码
    BinaryExpression(path) {
        const { operator, left, right } = path.node;
        if (types.isNumericLiteral(left) && types.isNumericLiteral(right)) {
            const result = eval(`${left.value} ${operator} ${right.value}`);
          path.replaceWith(types.numericLiteral(result));
        }
    },
```

完成后：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNR2SDbowpcjruxibaib0JO8KKa2RbqS4Edg62HAiciczibyLRueZ093jkDHZw/640?wx_fmt=png&from=appmsg)

准备对while switch case的控制流进行处理时，发现还有一些lnT9的尾巴作比较的一个值，应当为一个数字常量。

为了处理这些lnT9函数，先将XXX["YYY"](NNN) 替换为 XXX.YYY(NNN)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRvEmxtL0oicPAh2JxbJIVzO4cveYJvm2UtmvyBic7JEyZfFDTxktnjJ4Q/640?wx_fmt=png&from=appmsg)

```
 复制代码 隐藏代码
traverse(ast, {
    MemberExpression(path) {
        const { node } = path;
        console.log(node.property);
        if (types.isStringLiteral(node.property)) {
        node.property = types.identifier(node.property.value);
        node.computed = false;
        }
    }
});
```

然后，我们还是回到了之前的lnT9的构造方法，因此，我们先把前面的eval替换成最终的vm代码，并全部放入解密的js中。让lnT9方法直接存在于解密js文件的环境中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNRUXfiahXQsH91RXe0fvfBLr17gs4FmzAQxwIqiaQjAywktoCwiamS0jH5w/640?wx_fmt=png&from=appmsg)

这样我们就可以在ast中直接调用替换，最终成功替换了所有的lnT9相关的函数，所以前面的一大段lnT9相关代码可以删除了。

```
 复制代码 隐藏代码
traverse(ast, {
    CallExpression(path) {
        const { callee } = path.node;
        if (
          types.isMemberExpression(callee) &&
          types.isIdentifier(callee.object, { name: "lnT9" }) &&
          types.isIdentifier(callee.property)
        ) {
          const methodName = callee.property.name;
          if (lnT9 && typeof lnT9[methodName] === "function") {
            const returnValue = lnT9[methodName]();
            if (typeof returnValue === "number") {
              path.replaceWith(types.numericLiteral(returnValue));
            }
          }
        }
      },
})
//既然lnT9全部放入了环境中，也可以把前面的字符串加密部分写到这个AST处理。
```

### ③反流程平坦化

代码中将很多的if...else...和循环语句都使用while switch和三元表达式平坦化了，比如

```
 复制代码 隐藏代码
    while (_0x0003B1 < lnT9[lnT9.h445(5)]())
        switch (_0x0003B1) {
        case (0x75bcd15 - 0O726746425):
            _0x0003B1 = _0x0003B0 == null ? lnT9[lnT9.xmS5(6)]() : lnT9[lnT9.h445(5)]();
            break;
        case (0O57060516 - 0xbc614d):
            _0x0003B1 = lnT9[lnT9.h445(5)]();
            return;
        }
```

经过前面基本的ast处理后为

```
 复制代码 隐藏代码
  var _0x0003B1 = 0;
  while (_0x0003B1 < 65535) switch (_0x0003B1) {
    case 0:
      _0x0003B1 = _0x0003B0 == null ? 1 : 65535;
      break;
    case 1:
      _0x0003B1 = 65535;
      return;
  }
```

它实际则应该为

```
 复制代码 隐藏代码
  if (_0x0003B0 == null) {
    return;
  }
```

统一的地方是，都是初始将判断字符置为0，跳出判断均为65535。

因此，处理时应该从case 0开始处理，对每一个WhileStatement，如果SwitchStatement，则从0开始拼接case的代码，因为不断跳转，所以对每个case的处理可以写一个getCodeOf(caseIndex)函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJxs34guur6PntYDl0d8DNR2rTicoQCDpcDbphSbGbyiaMCCCr3BHfZ2SldXLibibibsPSs6oFXmN99kpg/640?wx_fmt=png&from=appmsg)

函数里，创建一个tcode变量用于存放修改后的代码，case中存在多个语句（在switchCase.consequent中），检查每个语句，有以下几种情况：

[b]①如果是BreakStatement即跳出这个case，所以此时return tcode。

```
 复制代码 隐藏代码
function getCode...