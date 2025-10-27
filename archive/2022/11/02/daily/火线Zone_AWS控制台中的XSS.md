---
title: AWS控制台中的XSS
url: https://mp.weixin.qq.com/s?__biz=MzI2NDQ5NTQzOQ==&mid=2247497115&idx=1&sn=ee55d8dcf27432e5495d7a1722d4c6ca&chksm=eaa97dbbdddef4ad6509cb9e4d1cf2c48bfc77299a004ce9dc3ad7fab087dddcd8106610d669&scene=58&subscene=0#rd
source: 火线Zone
date: 2022-11-02
fetch_date: 2025-10-03T21:33:21.353147
---

# AWS控制台中的XSS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vibRuZ6bNFe1BppmNyzcZktibDf6wNk8rzCxnqJiaM5svtrybbJFD1ZOpg/0?wx_fmt=jpeg)

# AWS控制台中的XSS

M1n0s

火线Zone

**本文为翻译文章，原文链接：****https://frichetten.com/blog/xss\_in\_aws\_console/**

正如我在Twitter上发布的那样，我最近开始了一个对 AWS API 进行模糊测试的辅助项目。这是我之前关于该主题的工作的合乎逻辑的下一步。为了支持它，我必须构建自己的库来手动制作 AWS API 请求并对其进行变异。我认为这将是一条非常富有成效的研究道路，但是我设法模糊了自己的方式，订阅了一项我无法禁用的每年 36,000 美元的服务。它最终得到了解决（非常感谢所有帮助/提供帮助的人。这是一次令人伤脑筋的经历），但出于显而易见的原因，我暂时不会对 AWS API 进行模糊测试。

好消息是，在整个惨败之前，即使图书馆还没有完成，它已经为自己赢得了一个错误，这篇文章就是对它的解释。它是通过 AWS 漏洞披露计划报告的，现已修复。感谢 AWS 安全部门的 Peter 和 Patrick 忍受我所有的电子邮件！

发现

可以想象，对 AWS API 进行模糊测试并非易事。有数百种 AWS 服务和数千种可能的操作。这与无数参数相结合，每个协议都有不同的格式、不同的区域、不同的版本以及我们想要使用的所有输入类型，这使得它非常耗时。

为了增加这个困难，我向 API 发送合法流量，这反过来会创建需要花钱的资源（作者注：本节是在上述事件之前编写的。这是轻描淡写的）。结果，我一直像鹰一样观察计费仪表板，并删除创建的任何内容。我也一直在浏览 AWS 控制台以寻找任何不妥之处。

在这些检查过程中，我偶然发现了Elastic Beanstalk更改历史记录中的一条错误消息。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vOPD4zLVsjsNJNoteQ8vzh3Q95WJiagL5kk3Bn26t9TBIMNjfJrrmAeA/640?wx_fmt=png)

有趣的。然而，当时，我有点把它放在一边，因为“很奇怪，你可以破坏 AWS 控制台的一部分”，并继续致力于模糊测试库。我什至把这张照片贴到了推特上（如果你是我把它拿下来之前喜欢它的两个人之一；谢谢）。然而，经过一点工作后，我有点恍然大悟，“这有安全隐患吗？” （是的，我知道对吗？黑客大师在工作）。

那么，什么是“b.requestParameters”，为什么 AWS 控制台会不高兴它为空？好吧，为了找出答案，我积累了从我多年的软件开发和信息安全经验中积累的所有技能和知识...... .. Ctrl+F 用于 JavaScript 中的“b.requestParameters”（再次，黑客大师在工作）。

这立即返回了答案。在 beanstalk-xp\_en.min.js 的第 17,240 行（该行号来自美化的 JS 输出）有对 b.requestParameters 的引用。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1veuRibiaz8fRBSABRbG1aWEiaHAthBJeNf5GZbmPq7YcT36ZyYiaDGsC4Wg/640?wx_fmt=png)

使用调试器进行单步调试后，可以清楚地看到更改历史记录页面正在从 CloudTrail 加载事件并显示它们。作为参考，这就是它的外观（取自此处）。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vM7Ivoew4iby9YpQAiaumVVwVFgjic9PicC6HuIGz3KrMmarC2k3ic5Hl5bw/640?wx_fmt=png)

Elastic Beanstalk 的更改历史记录功能是一项相当新的功能（于 2021 年 1 月发布），可让您查看 EB 环境配置的更改。

这并没有回答为什么 b.requestParameters 为空感到不安的问题，发生了什么？通过调试，很明显它正在寻找 CloudTrail 事件的特定属性，而 fuzzer 没有提供它。在 CloudTrail 中查找该特定事件，果然，在尝试update-environment操作时我没有提供任何参数，因此 requestParameters 为空。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vaE9VZiaILHcL70dCtIoP7OicQKn3JA7pv4Yyj2r4kN6WawjguVDQEZkw/640?wx_fmt=png)

**终于我们找到了罪魁祸首，但是我们能用我们发现的新错误做什么呢？下一个合乎逻辑的步骤是稍微探索一下。**

HTML注入

从 JavaScript 可以看出，我们对两个值有高度的控制。那些是用户代理和环境名称。此外，这些值似乎被直接插入到DOM中。

想到了跨站点脚本 (XSS)攻击，但 AWS 通常非常擅长在将内容呈现到浏览器中之前对其进行清理。这是我在使用SSM Agent时遇到的第一手经验。因此，我认为任何恶意内容都会在显示之前进行清理。

为了测试这一点，我将一个损坏的图像标签的简单有效负载放在一起（我故意将源设置为“x”）。我喜欢用它作为测试，因为如果它被渲染，它会给我一个很好的视觉指示器，否则我只会看到编码值。

我修改了我的框架，将用户代理设置为有效负载，点击发送并等待。等了 10 分钟后，我刷新了控制台，然后傻眼了。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vCyazMicL7mAlFz1tNlWXichWB5bibPykbZbPnFkYSQ0sXxVbnqwknYibAg/640?wx_fmt=png)

这是 AWS 控制台中的有效 HTML 注入！下一步，XSS 会起作用吗？更改了有效载荷，发送了它，然后等待了几分钟。坏消息：没有 JavaScript 执行。原因？内容安全策略 (CSP)阻止了我。如果您不熟悉，可以将 CSP 视为浏览器可以加载某些资源的指南。JavaScript 可以从某些域加载，字体可以从不同的域加载，等等。

虽然 CSP 不能减轻跨站点脚本攻击的原因，但它可以减轻影响。在这种情况下，CSP 阻止了内联脚本，这使我的 XSS 有效负载失败。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vLEic0hCrkZBaLicvM6hfHwE3ISvOmmDZJK0lzwFgGucP9RibNV8a8mxIg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vRicJ8SSpuicohNictBTCJcQ1mPo9UTiclW6t5zibfJayWuiaThWGHTM2kbKA/640?wx_fmt=png)

浏览控制台的 CSP，我找不到解决方法。这给我们留下了令人失望的 HTML 注入。你能做一些迟钝的网络钓鱼或社会工程计划吗？是的，也许。它很简洁，但仅限于在 AWS 控制台中找到的上下文中。我认为最现实的是，您可以尝试插入带有链接的“错误”消息并尝试以这种方式欺骗某人。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vTAeJapNPRx5IGuBuN4AiafSFtg6xM771FRpsm06QEicIN4hT60Dt5Y6w/640?wx_fmt=png)

有趣的是，您只需要与该帐户关联的有效凭据即可。这些凭证不需要 Elastic Beanstalk 或 CloudTrail 权限。此更改历史仪表板也会加载失败的尝试。因此，即使您对某个角色或用户拥有零权限，您更新 Elastic Beanstalk 环境的尝试也会显示出来。

iframe注入

没有看到绕过 CSP 的方法，我向一些朋友寻求想法。在与我的朋友 Chris 聊天时（查看他在schneidersec.com上的博客），他注意到 iframe 部分下有一些有趣的东西。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vwks5r8qnriaUBibZb8Tp3CflCrfOZ5Q6s2Jhv4CbibDhn1E8PMlsnqFLg/640?wx_fmt=png)

内容安全策略允许您从与控制台设置在同一区域的 S3 存储桶加载 iframe。我们都对此感到惊讶，难道您不能创建自己的存储桶并托管 HTML 吗？我们不明白为什么不这样做，所以我创建了一个 S3 存储桶，放置了一些 HTML 并更改了我的有效负载以创建一个 iframe。结果是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vfurESR5z6h92XsW750McHicnlicFvtere5TEPjjB3HMhlP4diblc9advA/640?wx_fmt=png)

事实上，您可以从 S3 存储桶加载 iframe！

提交给AWS

没有看到通过 HTML/iframe 注入解决的 CSP 的明显方法。很酷吗？当然，我的意思是 AWS 控制台中的任何漏洞都是整洁的，但 HTML 注入对于渗透测试报告来说是无用的。无论哪种方式，我都向 AWS 漏洞披露程序发送了一封电子邮件以及一些屏幕截图和一个概念证明（用于在用户代理中粘贴 HTML 有效负载以进行更新环境 API 调用的 Python 脚本）。

AWS 安全团队迅速做出回应，并表示他们已将信息转发给服务团队。从这里开始，我等了大约两周，发现“更改历史记录”页面中不再有任何事件。“奇怪”，我想，“也许他们只是老掉了”？所以我创建了一些新的 CloudTrail 事件，但它们仍然没有出现。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vLoQmw6M3v5vTskpWDKMdFmhPAdXZl2rkwDC06EpZxo6d4XGQdW0DdA/640?wx_fmt=png)

“也许他们现在对事件进行了验证？是检查恶意输入还是影响现有环境？”。我可以看出负责构建表格的 JavaScript 已被修改，但它已被缩小并且区分新旧看起来太费时了。所以我创建了一个合法的 Elastic Beanstalk 应用程序和环境。当我这样做的时候，我想四处看看是否有其他领域容易受到 HTML 注入的影响，而且确实有一些。几个例子：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1v4XX9JZTQylNzpXA7Smrg7JsibNm5Dibn9LzXCUDib8FdiaW7pxju3Goicaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vFN9z4bKtVbHtWltGVaImpOsWQyT7Vsj4pUib8ribQmdvkEgzQCU1ZHxg/640?wx_fmt=png)

为了提供帮助（希望不会令人讨厌），我向 AWS 发送了另一封电子邮件，其中附有一些屏幕截图。失望的是我无法再次填充更改历史记录，即使使用真正的应用程序，我也开始清理。正是在这个时候，我有了一个想法，“这使用的是什么版本的Angular ”？我很快发现它没有。它使用了 AngularJS。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vbOrWuRVf1JBMsLRCp84d0jyTgCYE3KDWYzvsZGYIyNFYCGI1IYOYRg/640?wx_fmt=png)

模版注入

页面使用 AngularJS 的实现引入了另一种类型的注入攻击，我们可以尝试，客户端模板注入。当攻击者可以提供自己的模板语言输入时，就会发生模板注入攻击。这会导致在用户的浏览器中评估这些输入。例如（取决于模板格式）您可以插入`{{ 2+2 }}`，这将评估为`4`.

在对自己之前没有意识到 AngularJS 的情况感到非常失望之后，我创建了一个具有模板名称的应用程序并刷新了浏览器。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1viaHZAYDg4rsvOGic2yy5jZFyODMwCAyGlo5br7YgyWeeWKn7kS0SoSSw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vAeNBDzRzOfDbcibyzhCb0AMnRYQhjGlQLicZzT7aQMsNa6CIxvTRr1wQ/640?wx_fmt=png)

我们已经确认它很容易受到模板注入的影响，但是我们可以从哪里开始呢？好消息是 PortSwigger 的Gareth Heyes在这方面做了一些巨大的研究（1、2）。

简而言之，我们可以利用模板注入作为执行任意 JavaScript 并获得跨站点脚本的方法！以前，这需要一些工作来逃避 Angular 表达式沙箱，然而，在 AngularJS 1.6 中，沙箱被删除了。由于我们使用的是 1.8.1，因此我们不必担心它，而是可以使用以下有效负载（取自此处）。

     `{{constructor.constructor('alert(1)')()}}`

这将允许我们运行传统的警报 XSS 有效负载，但它会通过内容安全策略吗？我实际上并不确定。

我在这里的思考过程是我没有注入新的脚本标签，我只是要求 AngularJS 评估模板表达式，并且因为 AngularJS 已经被允许，它不会工作吗？这不是真正的内联评估，对吗？所以我发送了有效载荷并重新加载了屏幕以迎接这个讨厌的图。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vabZgQun7kloys4bN6TYfWcCrk5d8poaiaBuxicSfLcfGk8KV4DAcfREA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1v2QBs2OsXJhjZzgdsxRPHOkg7pa8y62C13zIPNG6afVbxBYsrRh9hbg/640?wx_fmt=png)

又被坑了！即使我们要求 AngularJS 评估一个模板，它也不会给我们 XSS。我们有什么办法可以绕过这个内容安全政策？

绕过CSP

令人惊奇的是，AngularJS 可以用来绕过 CSP！这样做的方法大致相当于我的想法，除了我们将注入 HTML 而不是注入模板。等等，这不是倒退吗？你会看到的 ：）

感谢 Gareth Heyes 所做的一些令人难以置信的研究，我们让 AngularJS 通过指令来评估 JavaScript 。经过一番摆弄，我想出了以下有效载荷。

     `<input ng-focus=$event.view.alert('XSS')>`

这将利用该`ng-focus`指令来启动 JavaScript。该`$event.view`变量将使我们能够访问我们需要的所有普通 JavaScript 功能。所以我用这个名字创建了一个应用程序，刷新了页面，然后……

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vAA0kyicbwGZHCJpltTZuWhkDebwlPK5ibvGWood170iavlDeAPnduy6iaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vAQlG2HEtYGQNugEkE8KE10Y3avzydqqL8AMV0VP9hwnq0ibdaI3aAUg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vsicFyh5wPtaNyaF0VnY9ESjR2iapwmZzAiceWZibxFPA7nvnibURnw6iclJw/640?wx_fmt=png)

任务完成！拿那个 CSP！胜利的呐喊！

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaR10zibS8icsyXO0nib9jviaZ1vib7VIMoaYU8JITL9RH6M5AM2dQibSvPUby4E2DGF03PybS1l4xs1icYDg/640?wx_fmt=png)

在确认我没有产生幻觉后，我截取了一些屏幕截图并将它们发送到 AWS。

结语

关于这一点，我想指出几件事。首先是我认为这是一个非常有趣的攻击场景，可能从 API 访问到试图通过 AWS 控制台攻击用户。需要明确的是，这是一种非常罕见的情况。据我所知（和 Google 搜索），在 AWS 控制台中只发现了一个其他 XSS 错误并公开披露。这绝对不是你的普通渗透顾问可以在订婚时引发的那种事情。但是，对于一个足够老练的对手来说，在正确的情况下它可能非常方便。

特别是，我认为我们可以在没有任何权限的情况下在更改历史中设置 XSS 是非常有趣的。假设...