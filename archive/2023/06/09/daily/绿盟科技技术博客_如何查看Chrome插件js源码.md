---
title: 如何查看Chrome插件js源码
url: http://blog.nsfocus.net/chromejs/
source: 绿盟科技技术博客
date: 2023-06-09
fetch_date: 2025-10-04T11:48:09.273405
---

# 如何查看Chrome插件js源码

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

# 如何查看Chrome插件js源码

### 如何查看Chrome插件js源码

[2023-06-08](https://blog.nsfocus.net/chromejs/ "如何查看Chrome插件js源码")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,369

分两种情况，一种是已安装插件，一种是未安装插件。查看已安装插件

chrome://extensions/

以”WebRTC Leak Shield”为例，点击”详情”，转到另一个URL

chrome://extensions/?id=bppamachkoflopbagkdoflbgfjflfnfl

去资源管理器中访问

%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Extensions\bppamachkoflopbagkdoflbgfjflfnfl\

环境变量USERPROFILE会展开，比如

C:\Users\scz\AppData\Local\Google\Chrome\User Data\Default\Extensions\bppamachkoflopbagkdoflbgfjflfnfl\

此即该插件的本地目录，其中有一个js目录，内有插件的js源码，比如

C:\Users\scz\AppData\Local\Google\Chrome\User Data\Default\Extensions\bppamachkoflopbagkdoflbgfjflfnfl\1.0.8\_0\js\

其下有background.js、popup.js。

若未安装插件，但想查看其js源码，需要下载其对应的some.crx，参看

《离线安装Chrome插件》
https://scz.617.cn/web/202205271527.txt

先打开chrome web store

https://chrome.google.com/webstore/
https://chrome.google.com/webstore/category/extensions
https://chrome.google.com/webstore/category/extensions?hl=en-US

搜索”WebRTC Leak Shield”，得到

https://chrome.google.com/webstore/detail/webrtc-leak-shield/bppamachkoflopbagkdoflbgfjflfnfl?hl=en-US

有个在线网站

https://crxextractor.com/

网站有大量广告，视觉干扰很多。点击”LET’S START”，将这种URL贴进去

https://chrome.google.com/webstore/detail/webrtc-leak-shield/bppamachkoflopbagkdoflbgfjflfnfl?hl=en-US

依次点击”OK”、”GET .CRX”，即可下载some.crx。用7-Zip解压some.crx，其目录结构完全同

%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Extensions\bppamachkoflopbagkdoflbgfjflfnfl\1.0.8\_0\

若懂WEB前端开发，这些不用讲。不懂WEB前端开发，看js源码也白看，我就是后者，尴尬。胡乱看了一下background.js，试图理解某些代码逻辑。

若是Firefox，调

browser.privacy.network.peerConnectionEnabled.set({ value: false })

这会禁用WebRTC PeerConnection。

若是Chrome，调

————————————————————————–
chrome.privacy.network.webRTCIPHandlingPolicy.set({
value: “disable\_non\_proxied\_udp”
}, function () {
…
});
————————————————————————–

该API第一形参可选值有

“default”
“default\_public\_interface\_only”
“disable\_non\_proxied\_udp”
“disable\_all\_interfaces”

该API第二形参对应一个回调函数，不必理会。实际管事的是

chrome.privacy.network.webRTCIPHandlingPolicy.set({ value: “disable\_non\_proxied\_udp” })

禁止非代理的UDP通信。

关于WebRTC，参看

《WebRTC泄露源IP的防范措施》
https://scz.617.cn/web/202304131224.txt

**版权声明**

本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/cyberinfrastructure/)

[Next](https://blog.nsfocus.net/weeklyreport202323/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)