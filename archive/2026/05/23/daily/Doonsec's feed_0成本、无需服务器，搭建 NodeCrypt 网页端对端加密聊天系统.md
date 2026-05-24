---
title: 0成本、无需服务器，搭建 NodeCrypt 网页端对端加密聊天系统
url: https://mp.weixin.qq.com/s/7MQPoL2ogmm5GT5S9UMKOQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:58:12.527894
---

# 0成本、无需服务器，搭建 NodeCrypt 网页端对端加密聊天系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LtibzcRx8GjWKx8ib0QZTGtEwoKmGkvUafIIuw99ds95lGibIxiawwPNR93cUmBAhsYpm4cxJiaNpkCO14drTUabX0C44NNCGNDF41ktBCLU64J4/0?wx_fmt=jpeg)

# 0成本、无需服务器，搭建 NodeCrypt 网页端对端加密聊天系统

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

NodeCrypt 是一个真正的端到端加密聊天系统。采用无数据库架构，所有消息在设备上本地加密，服务器仅作为加密数据的中转站，无法获取您的任何明文内容。

相比很多需要复杂依赖和高配置服务器的项目，NodeCrypt 更偏向“开箱即用”的思路，整体结构非常干净，即使是新手也能快速上手。

这次我们配合 Cloudflare 的免费服务进行部署，整个方案会有几个非常明显的优势：

* 完全免费，无需购买 VPS 或服务器
* 基于 Cloudflare 全球 CDN 网络，访问速度更快
* Serverless 架构，无需维护系统环境
* 一键部署，几分钟即可上线
* 不需要 Docker，不需要 Linux 运维经验
* 自动 HTTPS，自带安全防护能力
* 后续更新维护简单，基本零运维

最关键的是，这种部署方式非常适合长期使用。

因为你不需要关心服务器续费、系统维护、环境兼容这些问题，Cloudflare 会自动帮你处理底层运行环境，你只需要专注于项目本身即可。

对于想低成本、快速上线一个属于自己的聊天通讯系统的用户来说，这应该是目前最简单、最省心的一种方案。

NodeCrypt 更适合：

* 个人自用
* 轻量化部署
* 快速上线
* 低成本长期运行
* 不想折腾服务器运维的用户

它最大的特点就是：

轻量、简单、部署快，占用资源低。

尤其配合 Cloudflare，可以做到：

* 无需服务器
* 免费部署
* 几分钟上线
* 基本零运维

但它并不适合：

* 企业级业务
* 大规模用户场景
* 高并发系统
* 复杂后台和权限体系

因为 NodeCrypt 本身更偏向轻量工具，并不是一个完整的大型聊天系统。

在搭建之前，你需要准备好 GitHub 和 CloudFlare 的账号，只需要用邮箱即可注册，国内邮箱建议使用 @163.com 的邮箱。

这是项目官方地址：

```
https://github.com/shuaiplus/nodecrypt
```

记得给作者点个Star，支持并感谢作者开源项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUCOFy6DaPo4Uu5M3vAkICGQJ0zIQZwJXTibSciakAic502voJo37OhibNkwemkNefhAeQJa9KlFrzOJSfLbtKoJbhg8V90cAZMhEU/640?wx_fmt=png&from=appmsg)

打开NodeCrypt仓库，点击右上角的”Fork“按钮，将项目复制到自己的GitHub仓库，目的是为了后续能够让 Cloudflare 直接读取并部署你的项目，同时后续更新也会更加方便。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUibFkYygSvTibxGV46rUiaryHLAu6r65ybQdJP3d2YCKsaA6VoMXk8tRQWKvMMibibjAeGE41iad7MzCeKObbYoFHTZUAvl14xhLtGc/640?wx_fmt=png&from=appmsg)

内容不用改，保持默认即可，然后点击绿色的“Create fork”。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUW7tpxic1gMRPY2ZnKUP3JsZA9IiammwRvaC7IQPL4pwchZc7ARwfyokW3LsDgsLLnuVyLliaDrWe368rp03QnLvibyrfVY9No7uc/640?wx_fmt=png&from=appmsg)

之后就把原作者的项目复制到了自己的仓库。

Fork 完成后，回到项目主页，页面往下滑找到 README 文档中提供的 Cloudflare 一键部署按钮。点击之后会自动跳转到 Cloudflare 的部署页面。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjW1AWVwvCkJV7RPrghHLxpYDAXN2N4Wo1LZxRCr67CE6LIVbmfDFnicWnO6He6Ou853KCKbz8cashVjbPJ6MUiacibVnyTGPFic7fc/640?wx_fmt=png&from=appmsg)

整个过程不需要手动创建项目，也不需要自己上传代码，Cloudflare 会自动读取 GitHub 仓库内容并开始配置。

第一次使用cloudflare部署时，系统会要求你授权GitHub，点击新建GitHub连接。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWky8pwU0lgRxT9OIdz01YiagbA5xQwiaibaz6OPHDlrQHr7cDGiajjLCJjexwSo4I2uuUX2lYpWSnRlWycTt6rzicPK4iaKLoHkwL2c/640?wx_fmt=png&from=appmsg)

如果你授权所有GitHub账户上的仓库，你就选择“All repositories”，要是想指定某个仓库，你就选择下方的“Only select repositories”，选择你要部署的仓库即可。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUIib6ic3ZibCUrqNU5lu0RNlsKja6cw1fZJErm9X7h6rh69cnDSf5tDNiak3TWbfwV0E9Ppmry8F4UpZuicsiaMPicMDGjPc4P8wBFV0/640?wx_fmt=png&from=appmsg)

第一次连接可能还会让你在移动端GitHub确认数字，来完成验证，在移动端打开GitHub APP，会自动弹出一个框，让你输入电脑上显示的数字，然后授权即可。

授权完成之后，自会跳转回到cloudflare部署页面，然后接着，我们只需要修改一下项目名称，只要不与github仓库中的项目重名即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVXFV0L4GFVeSKAXL3pAggVZWIlmUhmqChXvuctXdibxiaXj6yCdBMk9iaRXLQFZcHKwVFxbMpqUoh4vaWdpItzpK2Y3cIa9a3Uvo/640?wx_fmt=png&from=appmsg)

之后点击部署。

等待部署完成。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVaYibZD4GCVWxMXM9iaQJuZbZXSojSDf0BiceNSQ5t1KFgNMPlbWZ3TJhMjdHjlTTfQPdZrfvz06r86d5DDH8f7a7Hic3gibP8Lia3Y/640?wx_fmt=png&from=appmsg)

部署完成后，确保构建日志这里要全部是对勾。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWaRozH7dTSMQJeibbeQQ8B2WNjT2YQPk1kCknicmoDPbOGPwqYNmDMkYPR0ym3Ziasib0MMxAAR3p4LyrQYmLyjEhx3xVyur1slfM/640?wx_fmt=png&from=appmsg)

之后点击右上角的访问，你就能进入到聊天系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWkeembDicibicqTicXj3dP6eGOfBiczrmXRKS07XibBlYlyQ2PuvwffTCbBkXrDT62bsUensQicJVXe3OOEJVWonTpyosIybf9rotXNg/640?wx_fmt=png&from=appmsg)

这个访问地址是你Cloudflare项目标识，和GitHub用户名，同时加上.workers容器组合而成，所以说后期条件允许或者不想裸漏信息，可以添加一个域名。

在上方菜单栏中找到“域”，然后点击“添加域名”，前提是你已经把域名解析托管到了cloudflare。在添加的时候可以添加二级域名。

比如你的域名是：xxx123.com，那么你可以输入 chat.xxx123.com，cloudflare会自动添加配置DNS。后期就可以通过域名来访问聊天系统。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUvAR2CdrbZbApBaaQpuN3DySQ9F7jbT6XG7hVs1M61mdNlkp1NWTcQ2mrkMMm35ITarY8lVYeXeqKDvqWWrWwsia7c4eC3FZvg/640?wx_fmt=png&from=appmsg)

进入聊天系统页面之后，登录页面就是这样👇

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWLZS3SoM4hb6z0RKIoYyOn90lPnjic0z83j2Rs4RxwsibfYEh0eZYIOtSvT0FmQQyYUVSkT8WoIqznGxACu9gDnYArJtUhv9J0k/640?wx_fmt=png&from=appmsg)

右上角的 ？ 是使用说明，可以简单看一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXZ4cib0GtTGH2uia4d1UvlIbFY2IuKW4mpIj6js0CYeKubkib9DETRm2wOkBMaflTEicaEO6TRZIM8XGcq2MYU9yRW3LeM15NWcBs/640?wx_fmt=png&from=appmsg)

这里我创建一个房间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjU5lDiaKqicdygrviaPrqNz70DibGQHIp8V6TPsIXmJUF1X7ILNZJQedK6qX2vyqqQYnkFjIdbyvju6yehq8PxahUNDZHjbIKuQXoE/640?wx_fmt=png&from=appmsg)

进去之后页面就是这样。界面与TG类似。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXrZroQ9eDFRNrueHcJWOjyFxdbicHdTtMichkI3ibEyzgd8Be8XhGYgk8q8XQibiaUpEpUIQVD9iaoYgoZvoEjW3r7uFw922vAgvX0Q/640?wx_fmt=png&from=appmsg)

这个项目的系统功能不完善。

在左上方的设置里，只能对通知、语言、主题进行设置，没有个性功能，没有信息编辑功能。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVPC5lgmrj7PTWjVyqqnorEtTxHM6M3qrFZSlQO6TvnQ3Hn0EzVyH6OIjB6MzyrXI72XibfrOjpS5ib1sFtbEHIQdr9qIibricZez4/640?wx_fmt=png&from=appmsg)

聊天系统没有单独的加好友功能，也就是说，你想要和某人对话，你只能让他进入房间，这个房间别人也能进入。不过作者给出了这样一个方法。

这里我创建三个用户进入同一个房间，在右侧你可以看到这个房间的用户，你点一下这个用户信息部分，然后下方输入栏会出现“私信给 某某用户”。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXtIVSvtL5HrpbbJIN2pZGx0icOoTQvn7S4uUhaSv2Gagiaa2SSug3ib56bEx2BGicqcvicYcmkeT8jDZQQ3Vhra1rwjRib5XaP9YHQc/640?wx_fmt=png&from=appmsg)

你在这个基础上发送一个消息，就按照我示例的，我要给admin2发私信消息，那么admin3这个用户却看不到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjV7gUvF456PsE7vEN6af2BnHJrzF5iaF9HsIDYaFia0RicrSzs3ia67PhM6EcE22Zn9ztZSx9w55dCyIm7WXmd9KMriciaze97GOaNfA/640?wx_fmt=png&from=appmsg)

但是admin2却能看到消息。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWfjRia0a8TWW2C6r8ibN0lZJIrmUkEzgtPKPUUibZt8jwAGdBrpKYKB9CNRTgquUaIxWqWvVAeCPuDhbRQictnNibtU7FeSUy1HSaM/640?wx_fmt=png&from=appmsg)

这样就可以别人看不到的情况下，与指定用户进行对话，就是不方便，要是用户有点多，发消息容易弄混。

这个项目坏处就是没有管理功能，你没办法管理用户的行为，比如踢人，谁使用了这个系统等等，都没有，别人创建了一个房间，你也看不到。所以这个项目整体很不完善，不过用这个项目也是冲着端对端加密来的。

自己用用，或者小团体用，还是很轻量，很不错的。部署简单，又轻量。

本期内容到此结束。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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