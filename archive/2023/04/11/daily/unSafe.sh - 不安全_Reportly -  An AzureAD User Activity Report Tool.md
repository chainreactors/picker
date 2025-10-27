---
title: Reportly -  An AzureAD User Activity Report Tool
url: https://buaq.net/go-157941.html
source: unSafe.sh - 不安全
date: 2023-04-11
fetch_date: 2025-10-04T11:29:36.629018
---

# Reportly -  An AzureAD User Activity Report Tool

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

![](https://8aqnet.cdn.bcebos.com/04309800198c3d037e6bb8cef4b3128d.jpg)

Reportly - An AzureAD User Activity Report Tool

Reportly is an AzureAD user activity report tool. This is a tool that will help blue team
*2023-4-10 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-157941.htm)
阅读量:37
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhKtu3LUMHFWuaDMxWY7NPlInCtM1ao0_8VDYFU2vRzkH-PeTudPkRHHPb8KSc8CBngHCdUqfFXMc1gIxYGvK17LjUM287CzIBAkVann3RRm7TAKF5_7HoK-KCuVTPi4lw4N7vusUcB0SggAEDOzQofMYkcrBaONHybIU21lL-n3ofLbyCpI6WA7M7HbQ=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEhKtu3LUMHFWuaDMxWY7NPlInCtM1ao0_8VDYFU2vRzkH-PeTudPkRHHPb8KSc8CBngHCdUqfFXMc1gIxYGvK17LjUM287CzIBAkVann3RRm7TAKF5_7HoK-KCuVTPi4lw4N7vusUcB0SggAEDOzQofMYkcrBaONHybIU21lL-n3ofLbyCpI6WA7M7HbQ)

Reportly is an AzureAD user activity report tool.

This is a tool that will help [blue teams](https://www.kitploit.com/search/label/Blue%20Teams "blue teams") during a cloud incident. When running the tool, the researcher will enter as input a suspicious user and a time frame and will receive a report detailing the following:

1. Information about the user
2. Actions taken by the user
3. Actions taken on the user
4. User login and failure logs

[ ](https://user-images.githubusercontent.com/88736901/202284687-9862e097-a5d6-4557-a474-d99e37269c2e.mp4)

When running the tool, a link to [authentication](https://www.kitploit.com/search/label/Authentication "authentication") and a device code will show, follow the link and enter the code to authenticate. [![](https://blogger.googleusercontent.com/img/a/AVvXsEhlEf_DcSqxBrNw1DHVGFL5cIetIiJlTGrz14CQOaY4XB21pNjkc_VApy-zBNc99iznXkDDCdmJqePHzUb1cR1IMNODAoNZ9lluygAHxihygL4tHQ4Wr40whsMgmu8MWRKcvrmkWg5kven6q29mbxOKP9YOfpezgSr42krw0hMF55C-Bsj0euN0EIgbbA=w640-h156)](https://blogger.googleusercontent.com/img/a/AVvXsEhlEf_DcSqxBrNw1DHVGFL5cIetIiJlTGrz14CQOaY4XB21pNjkc_VApy-zBNc99iznXkDDCdmJqePHzUb1cR1IMNODAoNZ9lluygAHxihygL4tHQ4Wr40whsMgmu8MWRKcvrmkWg5kven6q29mbxOKP9YOfpezgSr42krw0hMF55C-Bsj0euN0EIgbbA)

Insert User principal name of a suspicious user.

After authentication, in order to create a full report choose the option "5" [![](https://blogger.googleusercontent.com/img/a/AVvXsEiET-TSt49mTgn1dCWYkfn5fc3oI5nlWwo202PooXpsZ_LwNuJJjTAeRDNhShjQB67GgHvJaH5niwGHUGTfe6kzJ5PI8g_p6AiIsjMAGsRiiMdtv8yfSDIy8XkJpszMZhklcyjzB1bVOvSLcsR-f37EvygdASuDMOIOktlzXOMDZ69UmSIEvQ4E7ktUNQ=w640-h230)](https://blogger.googleusercontent.com/img/a/AVvXsEiET-TSt49mTgn1dCWYkfn5fc3oI5nlWwo202PooXpsZ_LwNuJJjTAeRDNhShjQB67GgHvJaH5niwGHUGTfe6kzJ5PI8g_p6AiIsjMAGsRiiMdtv8yfSDIy8XkJpszMZhklcyjzB1bVOvSLcsR-f37EvygdASuDMOIOktlzXOMDZ69UmSIEvQ4E7ktUNQ)

When the report will be ready the tool will print "Your report is ready!". The reports are created in the executable's directory.

In order to use the tool you will need an AzureAD application with the following **delegated** [microsoft](https://www.kitploit.com/search/label/Microsoft "microsoft") graph api permissions:

* AuditLog.Read.All
* GroupMember.Read.All
* RoleManagement.Read.Directory
* User.Read
* User.Read.All

  **dont forget to grant admin consent** [![](https://blogger.googleusercontent.com/img/a/AVvXsEhuuN5ziaE8rZe8CoTc_9mJ5ALOY1nGYvHTl3aeDI8btJnbVYlGKJB0-LzkuHE2Z1-oyfLJpa8k8niIXqeh7FDgAoRjJaNZdZv0Eicxrt3C_ZAlaMMbnfG4hd-cI3tr6oOI1OEnmRllU2KFrlTqhdEyvPM7mZl68j9CJavRthWaNrEqDMs7YZz6sP1YdQ=w640-h166)](https://blogger.googleusercontent.com/img/a/AVvXsEhuuN5ziaE8rZe8CoTc_9mJ5ALOY1nGYvHTl3aeDI8btJnbVYlGKJB0-LzkuHE2Z1-oyfLJpa8k8niIXqeh7FDgAoRjJaNZdZv0Eicxrt3C_ZAlaMMbnfG4hd-cI3tr6oOI1OEnmRllU2KFrlTqhdEyvPM7mZl68j9CJavRthWaNrEqDMs7YZz6sP1YdQ)

To create an application go to "App registration" tab and select "New registration" option.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg7B3l02Cmog3p0QANhXoisjXDIP1rCAdk6r6YNle7rM_VQQpLxCkSKHJuqaxRcFNExPuyij0rY7BYskMQWd1puN1lxv0CKLqiekIMROTR6rByCEPjreRfDEAdQYSqH6x1ISOhfbjVFMQspVGLftKR_jEq8-c1kSg2rZdSJ5UXcq7xYdTx1MAtGTT9ZGw=w640-h72)](https://blogger.googleusercontent.com/img/a/AVvXsEg7B3l02Cmog3p0QANhXoisjXDIP1rCAdk6r6YNle7rM_VQQpLxCkSKHJuqaxRcFNExPuyij0rY7BYskMQWd1puN1lxv0CKLqiekIMROTR6rByCEPjreRfDEAdQYSqH6x1ISOhfbjVFMQspVGLftKR_jEq8-c1kSg2rZdSJ5UXcq7xYdTx1MAtGTT9ZGw)

Also, when creating the application, make sure you mark the following option as "yes": [![](https://blogger.googleusercontent.com/img/a/AVvXsEjklHW86ryDHw7Sne0FSwlUCrTyGTO50fgvtCY9RDdTw6VRaXe9uHiOi5eih5mdcPZmCunBMhKRNg_OUmAsQfW4xBwjOiVqjLFimKVNoUn3uPVBWp3noGSilSS_H13mRgedQX0i_EOHcSgEYIakoQMtHXYcqOYQN-2Z_IbIqNNi0cD2f7yZGph5D6lZ5g=w640-h158)](https://blogger.googleusercontent.com/img/a/AVvXsEjklHW86ryDHw7Sne0FSwlUCrTyGTO50fgvtCY9RDdTw6VRaXe9uHiOi5eih5mdcPZmCunBMhKRNg_OUmAsQfW4xBwjOiVqjLFimKVNoUn3uPVBWp3noGSilSS_H13mRgedQX0i_EOHcSgEYIakoQMtHXYcqOYQN-2Z_IbIqNNi0cD2f7yZGph5D6lZ5g)

* you can find this property under the application's "Authentication" tab.

Add a [secret](https://www.kitploit.com/search/label/Secret "secret") to the application. [![](https://blogger.googleusercontent.com/img/a/AVvXsEhc1Yu4qNEcgkE4T1IuIIzkAkPL4hjbuvrBRU7Sf-HCGozQahX7AjDDtPYnIE9O3E022yuCF2m6orSDFtYXFu4pmCdrDTeCB5EXeaXbkODPLwWvr00UuDTw24m8rHJELFTahfGuaR5ysEl-_y_Qr5RPMGlLTQlGy3_lJGpFGGeqcYAqkiRhaBLczMsHLg=w640-h166)](https://blogger.googleusercontent.com/img/a/AVvXsEhc1Yu4qNEcgkE4T1IuIIzkAkPL4hjbuvrBRU7Sf-HCGozQahX7AjDDtPYnIE9O3E022yuCF2m6orSDFtYXFu4pmCdrDTeCB5EXeaXbkODPLwWvr00UuDTw24m8rHJELFTahfGuaR5ysEl-_y_Qr5RPMGlLTQlGy3_lJGpFGGeqcYAqkiRhaBLczMsHLg)

* Go to "Certificates & secrets"
* Add a secret
* Immediately copy the secret to the config file (after you watch it once, it disappears)

After you created the application you need to fill the config.cfg file:
 clientId = application id
 clientSecret = application secret
 tenantId = tenant id

Reportly - An AzureAD User Activity Report Tool
![Reportly -  An AzureAD User Activity Report Tool](https://blogger.googleusercontent.com/img/a/AVvXsEhKtu3LUMHFWuaDMxWY7NPlInCtM1ao0_8VDYFU2vRzkH-PeTudPkRHHPb8KSc8CBngHCdUqfFXMc1gIxYGvK17LjUM287CzIBAkVann3RRm7TAKF5_7HoK-KCuVTPi4lw4N7vusUcB0SggAEDOzQofMYkcrBaONHybIU21lL-n3ofLbyCpI6WA7M7HbQ=s72-c)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/04/reportly-azuread-user-activity-report.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)