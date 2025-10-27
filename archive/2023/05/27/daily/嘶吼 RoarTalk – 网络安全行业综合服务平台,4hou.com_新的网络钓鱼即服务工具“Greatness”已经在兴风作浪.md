---
title: 新的网络钓鱼即服务工具“Greatness”已经在兴风作浪
url: https://www.4hou.com/posts/0o0V
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-27
fetch_date: 2025-10-04T11:38:04.587386
---

# 新的网络钓鱼即服务工具“Greatness”已经在兴风作浪

新的网络钓鱼即服务工具“Greatness”已经在兴风作浪 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的网络钓鱼即服务工具“Greatness”已经在兴风作浪

布加迪
[新闻](https://www.4hou.com/category/news)
2023-05-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)109927

收藏

导语：至少从2022年中期开始，一种名为“Greatness”的网络钓鱼即服务（PaaS）工具就被用于几次网络钓鱼活动。

至少从2022年中期开始，一种名为“Greatness”的网络钓鱼即服务（PaaS）工具就被用于几次网络钓鱼活动。Greatness整合了一些最先进的PaaS产品的功能，比如多因素身份验证（MFA）绕过、IP过滤以及与Telegram机器人程序集成。

目前，Greatness只专注于Microsoft 365网络钓鱼页面，为其加盟机构提供附件和链接构建器，以创建高度逼真的诱饵和登录页面。它含有诸多功能，比如预先填充受害者的电子邮件地址，并显示从目标组织的真实Microsoft 365登录页面提取的适当的公司徽标和背景图像。这使得Greatness特别适合对企业用户实施网络钓鱼。

分析几次进行中和过去的攻击活动中针对的域后发现，受害者几乎无一例外是美国、英国、澳大利亚、南非和加拿大的公司，最常见的目标行业是制造业、医疗保健业和科技业。每个国家和行业受害者的具体分布因攻击活动而略有不同。

要使用Greatness，加盟机构必须部署和配置提供有API密钥的网络钓鱼工具包，连不熟练的威胁分子也可以轻松利用该服务的更高级功能。网络钓鱼工具包和API充当Microsoft 365身份验证系统的代理，执行“中间人”攻击，并窃取受害者的身份验证凭据或cookie。

**活动和受害者研究**

Greatness似乎在2022年年中开始运作，从VirusTotal上可用的附件样本数量来看，活动高峰期出现在2022年12月至2023年3月。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581608168470.png "1684581608168470.png")

图1. VirusTotal上找到的附件样本数量

虽然每次活动侧重的地区略有不同，但总的来说，50%以上的目标都位于美国，其次是英国、澳大利亚、南非和加拿大。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581619518047.png "1684581619518047.png")

图2. 目标组织的地理分布

Greatness旨在危及Microsoft 365用户，可以使网络钓鱼页面特别令人信服，攻击企业特别有效。从思科Talos获得的数据来看，Greatness的加盟机构几乎只针对公司企业。分析几次活动的目标组织后显示，制造业是最常受攻击的行业，其次是医疗保健业、科技业和房地产业。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581629490271.png "1684581629490271.png")

图3. 按行业划分的目标组织分布

**攻击流**

当受害者收到恶意电子邮件时，攻击就开始了，该电子邮件通常含有一个HTML文件作为附件，并以共享文档为借口，诱使受害者打开HTML页面。

一旦受害者打开附加的HTML文件，Web浏览器就会执行一小段经过混淆处理的JavaScript代码，该代码与攻击者的服务器建立连接，以获取网络钓鱼页面的HTML代码，并在同一浏览器窗口中将其显示给用户。这段代码含有一个模糊的图像，显示旋转的轮子，假装加载文档。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581643203082.png "1684581643203082.png")

图4. 模糊处理的附件文档诱饵

然后，该页面将受害者重定向到Microsoft 365登录页面，该页面通常预先填充了受害者的电子邮件地址以及他们公司使用的自定义背景和徽标。在下面这个例子中，出于隐私原因，我们用虚假的Talos数据手动替换了实际网络钓鱼样本中真实受害者的电子邮件地址、背景图像和公司徽标，以显示其外观。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581654562653.png "1684581654562653.png")

图5. 要求目标受害者输入密码的屏幕示例

一旦受害者提交其密码，PaaS将连接到Microsoft 365，冒充受害者并尝试登录。如果使用了MFA，该服务将提示受害者使用实际Microsoft 365页面请求的MFA方法（比如短信码、语音呼叫代码和推送通知）进行身份验证。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581665115226.png "1684581665115226.png")

图6. 要求受害者输入MFA码的页面示例

一旦服务接收到MFA，它将在幕后继续冒充受害者，并完成登录过程以收集经过身份验证的会话cookie。然后，这些信息将通过其Telegram频道或直接通过Web面板传递给服务加盟机构。

**网络钓鱼服务**

该服务由三个组件组成：网络钓鱼工具包（含有管理面板）、服务API和Telegram机器人程序或电子邮件地址。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581680190133.png "1684581680190133.png")

图7. PaaS通信流程图

网络钓鱼工具包，即交付给加盟机构并部署在加盟机构控制的服务器上的服务组件，是受害者相连接的服务的唯一部分。该工具包为攻击的每一步提供HTML/JavaScript代码。该工具包在后台与PaaS API服务进行联系，转发从受害者那里收到的凭据，并在攻击的每个步骤中接收有关应该向受害者提供的页面的信息。当受害者将其凭据提交给工具包时，它将它们存储在本地，以便可以通过管理面板来访问它们；如果配置成这么做，则将它们发送到加盟机构的Telegram频道。

网络钓鱼工具包含有一个管理面板，允许加盟机构配置服务API密钥和Telegram机器人程序，并跟踪被盗的凭据。下图显示了管理面板登录页面和仪表板的示例。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581696115516.png "1684581696115516.png")

图8. 网络钓鱼工具包的管理面板登录页面

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581710176224.png "1684581710176224.png")

图9. 网络钓鱼工具包的管理面板仪表板

管理面板还可以构建恶意附件或链接，它们通过电子邮件提交给受害者。下图显示了用于生成附件的表单：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581725187471.png "1684581725187471.png")

图10. 网络钓鱼工具包恶意附件构建器

PaaS旨在以一种非常标准化的方式使用。传递给受害者的攻击载荷必须是一个链接，或者更常见的是一个HTML附件。攻击者可以使用上面的构建器表单来创建具有以下几个选项的攻击载荷：

自动抓取：该功能会在Microsoft 365登录页面中预先添加受害者的电子邮件，从而增加攻击的可信度。

背景：攻击者可能选择伪造的附件背景图像作为模糊的Microsoft Word、Excel或PowerPoint在线文档。

API是服务的核心部分。每家加盟机构必须有一个有效的API密钥才能使用Greatness，否则网络钓鱼页面将不会加载并显示一条消息称API密钥无效。下图显示了面板中可用的配置选项，加盟机构可以在这里插入API密钥。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230520/1684581739181850.png "1684581739181850.png")

图11. 管理面板配置页面

服务API含有验证会员密钥的逻辑，阻止不需要的IP地址查看网络钓鱼页面，最重要的是，与实际的Microsoft 365登录页面进行幕后通信，冒充受害者。

网络钓鱼工具包和API一起工作，执行“中间人”攻击，向受害者请求信息，然后API将信息实时提交到合法登录页面。如果受害者使用MFA, 这让PaaS加盟机构就可以窃取用户名和密码，以及经过身份验证的会话cookie。经过身份验证的会话通常会在一段时间后超时中断，这可能是使用Telegram机器人程序的原因之一——它会尽快向攻击者告知有效的cookie，以确保他们能够快速联系上感兴趣的目标。

**攻陷指标（IOC）**

这项研究的IOC也可以在我们的GitHub代码存储库中找到：https://github.com/Cisco-Talos/IOCs/tree/main/2023/04。

本文翻译自：https://blog.talosintelligence.com/new-phishing-as-a-service-tool-greatness-already-seen-in-the-wild/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?VsmJP9Ow)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)
...