---
title: 如何利用JS
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496230&idx=1&sn=88fd1c4d7c5d9cb6932887c86f27c7d1&chksm=e8a5f845dfd27153e161ccba08c1a11be3b71383b314b1464064f24ff1c8a41fd4934750e80b&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-29
fetch_date: 2025-10-06T18:52:14.481161
---

# 如何利用JS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7saBV8r0TxetCibTviafmSkIZr1icoNosQiayIqMcgbO30eDqYiaO3euSLzrp23fw9ruh4yXYSt9cuIJA/0?wx_fmt=jpeg)

# 如何利用JS

迪哥讲事

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwzfic3VPt0EfMjicnGXzicDLoHEqtz1cP3Iozxf1tSyMxCFNG9Aya8SziaVKhVw7ia6QugE/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

# **文章原文：****https://gugesay.com/archives/3541**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

# 常用工具列表

* hakrawler — 简单、快速的网络爬虫，旨在轻松、快速地发现网络应用程序中的端点和资产
* crawley——用 Golang 编写的快速、功能丰富的 unix 方式网络抓取/爬虫
* katana — 下一代爬虫框架
* LinkFinder — 一个在 JavaScript 文件中查找端点的 python 脚本
* JS-Scan — 一个 .js 文件扫描，内置于 php，旨在抓取网址和其它信息
* LinksDumper — 从响应中提取（链接/可能的端点）并通过解码/排序过滤它们
* GoLinkFinder — 一个快速且最小的 JS 端点提取器
* BurpJSLinkFinder – Burp 扩展，用于被动扫描 JS 文件中的端点链接
* urlgrab — 一个 golang 实用程序，用于通过网站搜索其它链接
* waybackurls — 获取 Wayback Machine 中某个域的所有 URL
* gau — 从 AlienVault 的 Open Threat Exchange、Wayback Machine 和 Common Crawl 获取已知 URL
* getJS — 快速获取所有 javascript 源/文件的工具
* linx — 显示 JavaScript 文件中的不可见链接
* waymore — 从 Wayback Machine 找到更多信息
* xnLinkFinder — 用于发现给定目标的端点、潜在参数和目标特定单词列表的 python 工具

一般从子域枚举开始，获取站点中相应的js文件，然后从js文件中获取有价值的信息，通常一条命令就能搞定：

`subfinder -d domain.com | httpx -mc 200 | tee subdomains.txt && cat subdomains.txt | waybackurls | httpx -mc 200 | grep .js | tee js.txt`

# 常用的基本字典列表

```
dialogs540f334e628dbce748a8js navigation_secondary55dfd8fe215f8edecd48js dialogsb18150a252f68f70f0c9js navigation_secondary147987372ed67d94de50js buttons147987372ed67d94de50js npmangular-animate8f9be52ce8a521f715a3js mainb18150a252f68f70f0c9js navigation7b5ba7de4b5e5fb011c7js dialogs147987372ed67d94de50js appmain7b5ba7de4b5e5fb011c7js main147987372ed67d94de50js buttons7b5ba7de4b5e5fb011c7js npmangulary-focus-store9327d7778ee0d85c3500js mainfb562f3396222d196abfjs breeze7b5ba7de4b5e5fb011c7js breezeb18150a252f68f70f0c9js breeze30886581e43164d9d721js breeze147987372ed67d94de50js navigationb18150a252f68f70f0c9js appmain147987372ed67d94de50js breezeee32c0b1526644e9b562js main7b5ba7de4b5e5fb011c7js dialogs7b5ba7de4b5e5fb011c7js navigationba64bbac173b1d655721js navigation147987372ed67d94de50js navigation_secondaryb18150a252f68f70f0c9js buttonscf9c75fee1de19837ae7js appmainb18150a252f68f70f0c9js navigation_secondary7b5ba7de4b5e5fb011c7js modalsb0f4a82ac6f25a46dc71js npmangular-ui-calendar423a597b943dc586730djs npmapollo-angular-link-httpe7a942f9925da8411a4ejs npmangular-ui-switch90766204ecd17b03ca76js appmainaf9ea97e6139d8cd52c2js npmapollo-angular-link-http-common87eff82eb4bc194887bfjs npmapollo-angular22f1de8a666515c86242js npmapollo-cache53668769616dc1466d8djs npmapollo-cache-inmemorydaeb4f1b88a15680fd12js buttonsb18150a252f68f70f0c9js npmangular-ui-bootstrapcd3d849d20f1a4f7dfacjs configjs npmattr-accept81d56f5e133bac14feb5js npmapollo-clientf1fffac92f44507c8f3ajs npmbase64-js61d2367f7816d6fec60fjs npmapollo-utilities9e092209349bda108468js npmaxiosb02cc1c0e336b6ce9d09js app147987372ed67d94de50js npmauth0b681a646eef51d083006js npmbraintree24d4f13fb9a355dadc24js npmbabel5fd8b43fabbd6864e9a2js npmcall-bind0f09a0bd48e4dac9d679js npmbreeze-client-labs03a64fb13d406c33bbc8js appaf9ea97e6139d8cd52c2js npmavailable-typed-arrays558d90654f4d4fc2aa04js npmcharacter-entities-legacy7f4022465f0c9c4a6fabjs npmblueimp-load-image3d0d2393c631d92c5a1ejs npmchartjs-color-stringbd3a54729bf6f60404afjs npmapollo-linka5d82a3252db6d3e8d15js npmaria-hiddena316c352eb617c047815js npmckeditorfde05d6a29366eaf2c71js npmcollapse-white-spacebdd075f4c3faca5c940fjs npmcharacter-reference-invalid2f9cdaeeea24c3f3897ejs npmbail2e238f58e0858fcf0e31js npmcolor-convert101a98cb8d9df306dc12js npmchartjs-color703b6867120bd9ebf784js npmbreeze-client75c1a11b2c8e46de7ce4js
```

因此我们可以在目标上使用这些单词列表：

`waybackurls “site.com” | grep -Eo ‘https?://[^/]+/[^”]+\.js’ | sed ‘s|^https\?://[^/]\+/||’ | awk -F ‘/’ ‘{print $NF}’`

以上命令的作用：

* `waybackurls "example.com"` ：从 Wayback Machine 档案中检索与“example.com”关联的 URL
* `grep -Eo 'https?://[^/]+/[^"]+\.js'`：搜索带有.js扩展名的 URL， -E标志启用扩展正则表达式， -o标志告诉grep仅输出匹配部分
* `sed 's|^https\?://[^/]\+/||'`：从每个 URL 中删除协议（http://或https://）和域名，仅保留路径
* `awk -F '/' '{print $NF}'`：用/分割后提取每个 URL 的最后部分

因此，当上面这条命令时，它将为你提供从存档快照中提取的.js端点列表，同时排除域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlQTialMwLXicX1evHOr9pLBkE8PITouwl9tCHK3CGPaoLOywH8u35fg7qnocW3v41P0UmLvIWLjS8w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlQTialMwLXicX1evHOr9pLBk6tAkYL7udQPiaMdLjoibM0YKXIfMMQ3HeJSAIibySmqJHibZtic3lkH13rA/640?wx_fmt=png&from=appmsg)

可以看到很少有关键字是新的和独特的，因此我们可以从一个目标中制定一个 js 单词列表，然后就可以在新目标上使用它，举个例子：

假设我们从 dell.com 获得了 JS 单词，并在 data.samsung.com 上使用了这些单词，我们就可以获得新文件、堆栈错误，从而对目录列表非常有用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlQTialMwLXicX1evHOr9pLBkLdy5MpI4EPOAgElrpQ5L06BOGNQ33EuBkojfCdDtx0FzLHKdpUJMvw/640?wx_fmt=png&from=appmsg)

可以在新目标上获得非常新的 JS 文件，然后按大小、数据类型、内容进行排序，同时也可以在你从 shodan、fofa 上获得的 IP 上使用这些相同的关键字：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlQTialMwLXicX1evHOr9pLBkhZQ19w0ARlia3N0ibiaLJOWibCUczonZoE7zMw058Fib5YgfnRSczQjOhAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlQTialMwLXicX1evHOr9pLBkvauP3oQEibg0QsArJfNRGaqNiclXdl5x4cw0WsNzI9Nmh6mE8icHHY1xQ/640?wx_fmt=png&from=appmsg)

其它利用基本也是如此，只是会有一点小修改：

```
curl -s https://app.site.com/config.js | \
grep -E “environment: ‘Production’|storageUrl: ‘https://buildxact.blob.core.windows.net/'|googleApiKey: ‘|appInsightsInstrumentationKey: ‘|globalApiEndpoint: ‘|streamChatApiKey: ‘|auth0ClientId: ‘|auth0Domain: ‘|flatfileApiKey: ‘|webSpellCheckerServiceId: ‘|webSpellCheckerServiceUrl: ‘|clientPortalUrl: ‘|appVersion: ‘|appVersionDate: ‘|appDomainUrl: ‘|oneBuildKey: ‘|flatfilePlatformPublishableKey: ‘|flatfilePlatformEnvironmentId: ‘“ | \
sed “s/.*’\(.*\)’.*/\1/”
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlQTialMwLXicX1evHOr9pLBknzl4iaZO5p1D3GHSdZH3dBRpZc4PXHNBFe3JqosfDoHUNYvM6T60FXg/640?wx_fmt=png&from=appmsg)

还可以添加我们自定义的敏感单词，例如：

```
ANACONDA_TOKEN=
ANALYTICS=
ANDROID_DOCS_DEPLOY_TOKEN=
android_sdk_license=
android_sdk_preview_license=
ANSIBLE_VAULT_PASSWORD=
aos_key=
aos_sec=
API_KEY_MCM=
API_KEY_SECRET=
API_KEY_SID=
API_KEY=
API_SECRET=
APIARY_API_KEY=
APIDOC_KEY
APIGW_ACCESS_TOKEN=
apiKey
apiSecret
APP_BUCKET_PERM=
APP_ID=
APP_NAME=
APP_REPORT_TOKEN_KEY=
APP_SECRETE=
APP_SETTINGS=
APP_TOKEN=
appClientSecret=
APPLE_ID_PASSWORD=
APPLE_ID_USERNAME=
APPLICATION_ID_MCM=
APPLICATION_ID=
applicationCacheEnabled=
ARGOS_TOKEN=
ARTIFACTORY_KEY=
ARTIFACTORY_USERNAME=
ARTIFACTS
ARTIFACTS_AWS_ACCESS_KEY_ID=
ARTIFACTS_AWS_SECRET_ACCESS_KEY=
ARTIFACTS_BUCKET=
ARTIFACTS_KEY=
ARTIFACTS_SECRET=
ASSISTANT_IAM_APIKEY=
ASYNC_MQ_APP_SECRET
```

一旦获得了 JS URL，就可以使用 nuclei Exposures 来获取更多敏感信息。

要对带有 Exposures 标签的 js.txt 文件运行 Nuclei 命令，可以使用以下命令：

`nuclei -l js.txt -t ~/nuclei-templates/exposures/ -o js_exposures_results.txt`

你学到了么？

以上内容由骨哥翻译并整理。

原文：https://kongsec.medium.com/js-for-bug-bounties-2-0-extreme-edition-2024-f167fa48276a

****如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款****

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzI...