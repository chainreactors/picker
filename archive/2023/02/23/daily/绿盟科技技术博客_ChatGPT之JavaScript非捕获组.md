---
title: ChatGPT之JavaScript非捕获组
url: http://blog.nsfocus.net/chatgptjavascript/
source: 绿盟科技技术博客
date: 2023-02-23
fetch_date: 2025-10-04T07:51:15.261489
---

# ChatGPT之JavaScript非捕获组

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

# ChatGPT之JavaScript非捕获组

### ChatGPT之JavaScript非捕获组

[2023-02-22](https://blog.nsfocus.net/chatgptjavascript/ "ChatGPT之JavaScript非捕获组")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")[ChatGPT](https://blog.nsfocus.net/tag/chatgpt/)

阅读： 750

有个脚本出现了JavaScript非捕获组

————————————————————————–
/\*
\* What does ?: do in regex – [2010-09-14]
\* https://stackoverflow.com/questions/3705842/what-does-do-in-regex
\*
\* 脚本中的”?:”好像未达预期目的
\*/
var temp = resp.data.html.match( /(?:uid=\”)(\d+)(?:\”)/g );
————————————————————————–

放狗查(?:)的含义，stackoverflow的回答与Chrome F12中执行结果不符，下面是其简化示例

————————————————————————–
var text = ‘prefix uid=”1234″ postfix’;
var temp = text.match( /(?:uid=\”)(\d+)(?:\”)/g );
console.log( temp );
————————————————————————–

Chrome F12输出

[‘uid=”1234″‘]

temp的值是uid=”1234″，而非”1234″，未体现「非捕获组」的效果。

ChatGPT给了一个非捕获组示例

————————————————————————–
var text = “Here are some links to https://www.google.com and https://www.github.com”;
var temp = text.match( /(?:https:\/\/)(\S+)/g );
console.log( temp );
————————————————————————–

ChatGPT声称其输出

[“www.google.com”, “www.github.com”]

Chrome F12输出

[“https://www.google.com”, “https://www.github.com”]

问ChatGPT为啥Chrome的执行结果与它声称的不符，它说它在Node.js v16.14.0中测的，Chrome所用JavaScript引擎与Node.js并不等价，然后ChatGPT提供了修改版

————————————————————————–
var text = “Here are some links to https://www.google.com and https://www.github.com”;
var temp = Array.from( text.matchAll( /(?:https:\/\/)(\S+)/g ), m => m[1] );
console.log( temp );
————————————————————————–

Chrome F12输出

[“www.google.com”, “www.github.com”]

我没有Node.js v16.14.0环境，在Ubuntu 22中

$ aptitude install nodejs

$ node -v
v12.22.9

$ node some.js

Node.js v12.22.9的反应同Chrome F12，与ChatGPT声称的Node.js v16.14.0不同。

ChatGPT算得上生产力工具，像我对JavaScript基本文盲，让我去一条条翻语言手册不现实，直接放狗，有时英文描述起来费劲，而ChatGPT对话有上下文，贴近自然语言，像个助教一样。前述修改版不是我要求的，只是在有上下文的对话里质疑它，它就理解了我在干啥，并提供修改版。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/joomlacve-2023-23752/)

[Next](https://blog.nsfocus.net/ssh-server/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)