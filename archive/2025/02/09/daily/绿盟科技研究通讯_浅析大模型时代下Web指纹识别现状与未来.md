---
title: 浅析大模型时代下Web指纹识别现状与未来
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498284&idx=1&sn=029b662ca7283b0701a75459a3377967&chksm=e84c5cf3df3bd5e59ffcb059aed33ac10569b635186a505da32fcb5f315eb26eb4d9879954a3&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2025-02-09
fetch_date: 2025-10-06T20:36:49.970759
---

# 浅析大模型时代下Web指纹识别现状与未来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhy8DIicQiav4I0gt5HLh3MKLOybVOeG7RWOY2eYbnwhLNkL11iart8723kw/0?wx_fmt=jpeg)

# 浅析大模型时代下Web指纹识别现状与未来

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyVQtjALbYPQY7aFQAaJnRwHyialr6pnw31d30B9DuNtInTNxibCGb2zhw/640?wx_fmt=gif&from=appmsg)

随着网络安全威胁的不断演变，Web安全始终是热点话题， Verizon发表的《2024 Data Breach Investigations Report》指出约40%的网络攻击是通过Web应用程序进行的，是网络攻击的主要切入点。无论“攻”还是“防”，Web指纹识别技术都尤为重要，对于防守方来说，指纹识别能在早期发现漏洞和安全隐患，降低被攻击的风险；所以接下来本文将介绍Web指纹识别的相关技术和工具现状，帮助读者可以从资产识别的视角了解Web的安全防护。

一. Web技术简介

Web技术是支撑现代互联网的核心技术体系，其主要包括浏览器（如Chrome、Firefox），负责解析和呈现Web内容；前端框架（如React、Vue），用于构建动态、交互式用户界面；Web中间件（如Nginx、Apache、Tomcat），负责处理请求和协调前后端通信；后端框架（如Django、ThinkPHP），实现业务逻辑与动态数据处理；数据存储（如MySQL、Redis），管理和存储结构化或非结构化数据；以及操作系统（如Linux、Windows），提供底层支撑和运行环境。此外，基于HTTP和加密的HTTPS协议实现了客户端与服务器之间的高效通信，Web相关技术如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyUVHyZOnoeib5s8GbjwvbgTyibia0220VoHuHDWPmgYibvM2mXWVeYq5rRg/640?wx_fmt=png&from=appmsg)

图1 Web技术示意图

二. 主流Web识别方法

Web技术识别通常通过指纹识别和信息收集来实现，包括分析HTTP Headers、HTML页面、Cookies特征以及文件路径结构等，通过访问特定路径（如/wp-admin或/robots.txt）和观察页面内容，也能推断出部分技术细节。

2.1

HTTP Headers

HTTP 头部信息是 Web 请求和响应的重要组成部分，其中包含了丰富的服务器和应用相关的信息。主要包括Server、X-Powered-By、Set-Cookie、Location，识别维度和例子如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyylUdgE7mMksh6oSGqS7TtZriaxBichcRVlXJYCsrGkEMKOVhGiaIEniclg/640?wx_fmt=png&from=appmsg)

图2 HTTP Header中识别Web信息

2.2

HTTP body

HTTP body 是 Web 请求和响应中的主体部分，它包含了网页内容、JSON 数据、XML 数据等信息。也可以识别出 Web 服务所使用的框架、技术栈及其他相关信息。

2.2.1

页面内容特征

通过分析网页的 HTML 内容，我们可以识别出 Web 服务所使用的框架和技术栈。许多 Web 应用会在生成的页面中嵌入特定的标识符，如特定的 CSS、JavaScript 文件和 HTML 标签。例如：

* WordPress 页面会包含 wp-content 和 wp-includes 等特定路径。
* Joomla 页面会包含  的标记。

2.2.2

错误页面信息

许多 Web 应用在出现错误时，会返回带有错误详情的 HTML 页面，这些错误页面通常带有框架或应用的标识信息。例如：

* PHP 错误页面：返回包含 Fatal error: Uncaught Error: Call to undefined function，可以推测目标 Web 服务使用了 PHP。
* Django 错误页面：包含 Django Debug Mode: Traceback 的错误页面可能表明该应用使用了 Django 框架。

2.2.3

JavaScript 特征

JavaScript 代码中可能包含与 Web 服务相关的特定库和框架信息。例如：

* React：页面中包含 react.js，并且有 React.createElement 等函数调用时，说明该页面使用了 React 框架。
* Angular：包含 angular.js，并且有 ng-app 或 ng-controller 等 Angular 特有的标记时，说明使用了 Angular 框架。
* Vue.js：如果页面中包含 vue.js，且有 v-bind、v-if 等 Vue.js 特有指令时，说明使用了 Vue.js。

2.2.4

文件hash

文件哈希（File Hash）是通过哈希算法对文件内容进行计算，生成一个唯一的标识符，用于识别文件。通过对 Web 应用中的关键文件（如 JavaScript、CSS、HTML 模板文件、图标文件等）的哈希计算，可以帮助我们识别网站所使用的技术栈、框架或内容管理系统（CMS）。常见的关键文件：

* JavaScript 文件：Web 应用的框架和库通常会以 JavaScript 文件的形式存在。通过检查这些 JavaScript 文件的哈希值，可以识别出框架（例如 React、Vue、Angular）。
* CSS 文件：一些 Web 框架（如 Bootstrap、Tailwind CSS）会包含特定的样式表文件，通过这些 CSS 文件的哈希值可以识别使用的前端框架。
* HTML 模板文件：一些 CMS 和 Web 应用会提供特定的 HTML 模板文件，如 WordPress 的 wp-content 和 wp-includes 目录中的文件。
* 图标文件（如 Favicon）：如前所述，Favicon 图标文件也可以帮助识别 Web 技术。
* 特定技术的文件：例如，PHP 应用可能会包含名为 index.php 的文件，Django 应用可能包含 manage.py，Ruby on Rails 应用可能包含 config.ru

三. 常用Web识别工具

为了提高识别准确性和效率，通常会使用一些自动化工具来帮助进行Web框架指纹识别。接下来介绍几款常见的工具。

3.1

Wapplayzer

Wappalyzer 是一款用于识别网站技术栈的开源工具。它能够分析网站的 HTTP 头、HTML 代码、JavaScript 变量等信息，推测出网站使用的 CMS、Web 服务器、JavaScript 框架、CDN、数据库等技术。最初由 Elbert Alias 开发，目前已成为一款广泛使用的技术指纹识别工具，被用于安全研究、市场分析和渗透测试。

Wappalyzer主要特点：

* 多种检测方式，利用 URL 结构、HTTP 响应头、网页内容和 JavaScript 变量等信息进行识别。
* 跨平台支持，提供浏览器插件、CLI 工具和 API（需要付费订阅），适用于多种环境。
* 丰富的技术库，维护一个不断更新的技术指纹数据库，覆盖数千种技术。

Wappalyzer主要通过模式匹配来识别网站的技术组件，具体的规则格式如下图所示，目前版本的支持识别5595种Web技术，包含105钟类型。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyZp9WQ1iaHBlGibTOjbyy9AicyLtbOScriaWaSiax0CZWAxUQTicKNRJIhtkg/640?wx_fmt=png&from=appmsg)

图3 Wappalyzer识别规则（Nginx）

具体识别效果以Wappalyzer官网为例，如下图所示，可识别网站使用的分析工具、JavaScript 框架、支付处理工具、安全技术、Web框架、实时聊天相关技术。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyJpXGFxVOpgOPxgo0WVLDK8C4zLEZ51jthO9d4PErjnVnHicdUlFBdHA/640?wx_fmt=png&from=appmsg)

图4 wappalyzer识别效果

此外，Wappalyzer会将匿名的收集用户的数据并传回他们的服务器，建议在设置中关闭。

3.2

ObserverWard

ObserverWard （侦查守卫）是一款开源的指纹识别工具，主要用于 Web 资产的识别和安全评估。它类似于Wappalyzer，但更侧重于信息安全领域，能够识别网站使用的 CMS、框架、Web 服务器、中间件、安全防护设备等信息。

ObserverWard主要特点：

* 基于 YAML 编写探针：支持 YAML 格式的指纹规则，用户可以自定义匹配规则和提取器，提高识别的灵活性。
* 支持服务和 Web 应用版本识别：不仅能识别 Web 技术栈，还可检测后端服务及其具体版本信息。
* 符合 CPE 命名规范：使用 NVD以及标准的通用CPE规范，提高指纹匹配的标准化程度。
* 社区化指纹库与 Nmap 服务探针：结合社区贡献的指纹数据，并支持 Nmap 探针，以提升识别的广度和准确性。
* 集成 Nuclei 进行漏洞验证：与 Nuclei 扫描器集成，支持漏洞验证，便于进行安全评估和渗透测试。

ObserverWard有一个独立的指纹库项目，地址为https://github.com/0x727/FingerprintHub，下图是ObserverWard为识别thinkphp的规则格式样例：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhy6k1vdwOV6O8oUHkbRfFNIcIKVCFG3iaOOXEtevkuAhnJP7g67kWMDicw/640?wx_fmt=png&from=appmsg)

图5 ObserverWard识别规则（thinkphp）

工具识别效果如下图所示，识别的Web组件的维度Wapplayzer要少很多，但ObserverWard支持识别Web组件的风险情况，这部分主要调用Nuclei的识别能力。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyHq1B0sMRib6TTm8A40Pn9Sib3G8AlliaIchnFXpqKB2MyRMpHSJfVw19g/640?wx_fmt=png&from=appmsg)

图6 ObserverWard Web组件识别样例（Nginx）

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhy9GLE6ux3jiaYtFJfpibYmuceQiaXWNHiaj69KVdGW5iaICKXET1LCOKicuQg/640?wx_fmt=png&from=appmsg)

图7 ObserverWard 识别脆弱性[4]

3.3

BlindElephant

BlindElephant是一款开源的Web应用程序指纹识别工具。该工具支持15种常见Web应用几百个版本的识别。同时，它还提供WordPress和Joomla的各种插件。该工具支持用户自己扩展，添加更多的版本识别支持。

BlindElephant该项目已经不在维护了，但其Web版本识别的方法很经典。通过读取目标网站的特定静态文件，计算其对应的哈希值，然后和预先计算出的哈希值做对比，通过对不同路径的版本号取交集，推测最可能得版本信息。原理示意图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7VRDicibzRywgiaL3gPPXxhyXUpmibsdH03CJchScUDaBdHRbI8pzibWl1A1HTZ6beNDozMdY3W37V8A/640?wx_fmt=png&from=appmsg)

图8 BlindElephant版本识别原理示意图[5]

四. 总结

Web指纹识别技术在网络安全中扮演着重要角色，本文浅析了一些识别技术的基本原理以及工具，通过使用一些工具，对HTTP头部、网页内容、文件哈希等信息的分析，能够有效识别Web应用所使用的技术栈和框架。未来，随着技术的发展，Web技术类型也在持续增加，未知指纹和版本识别仍然是我们需要面对的问题，所以除了传统的静态分析，动态内容分析和网络协议特征以及结合AI大模型对资产识别的研究。大模型能够从复杂和多样化的输入中提取深层次的特征，不仅能识别已知资产，还能够应对新的、未曾见过的资产类型。它们通过预训练和迁移学习等技术，能够在面临未知或不完全信息时，依然进行有效的推理和判断，从而提升资产识别的准确性和效率。所以，未知资产识别网络安全难题将会在大模型时代被解决，让我们拭目以待。

    绿盟CAASM（网络资产攻击面管理）已全面覆盖本文所有识别能力，并在此基础上增加AI驱动的未知资产识别能力，突破传统指纹库限制，智能发现潜在风险资产，建立全局资产视图，助力安全团队掌控全局。欢迎感兴趣的小伙伴，做进一步交流。

参考文献

[1].

https://www.verizon.com/business/resources/T697/reports/2024-dbir-data-breach-investigations-report.pdf

[2].     https://github.com/emo-crab/observer\_ward

[3].     https://www.wappalyzer.com/

[4].     https://github.com/emo-crab/observer\_ward?tab=readme-ov-file

[5].     https://blindelephant.sourceforge.net/

相关阅读：

[从传统企业资产管理到CAASM](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498033&idx=1&sn=943c9ed666555f7eedce8684d35621af&scene=21#wechat_redirect)

[构建精益安全体系：浅析4个攻击面管理技术](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247497870&idx=1&sn=e2e08e7d2b0b10480613533d6a8ad447&scene=21#wechat_redirect)

[应对攻击面的未来之路：持续威胁暴露管理（CTEM）](https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247496246&idx=1&sn=7ee66574ad19adbf22127d495cbc49f7&scene=21#wechat_redirect)

内容编辑：创新研究院 桑鸿庆
    责任编辑：创新研究院 陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

绿盟科技研究通讯

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过