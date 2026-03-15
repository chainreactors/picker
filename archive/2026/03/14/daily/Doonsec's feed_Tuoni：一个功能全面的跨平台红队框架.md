---
title: Tuoni：一个功能全面的跨平台红队框架
url: https://mp.weixin.qq.com/s/LxbbKqAWATd3feVwM-E8Cw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:29.467589
---

# Tuoni：一个功能全面的跨平台红队框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdHv55KfDq0AU0iclCJO2J6icfROZXYkRrM7BwoXNMYt3L2TYwnD7bysUjSKDWN4EmjI7l5aZicTicj31BLF4yZWzlIbfLxVuJqYL4/0?wx_fmt=jpeg)

# Tuoni：一个功能全面的跨平台红队框架

原创

工具党
工具党

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 如果你想找一个用于网络安全教学和演练的综合性红队指挥控制（C2）框架，这篇文章会带你了解Tuoni。它是一个基于Java、Docker，并提供Web界面的开源工具，上手和使用都不算复杂。

## 它是干嘛的？

简单说，Tuoni是为了大规模网络安全防御演练设计的。它的目标是让红队培训和技术研究更方便。这东西用Java开发的，所以挺稳定；用Docker打包，到处都能跑；还有个在浏览器里用的管理后台，操作起来直观。

它最核心的特点是那个插件系统。你可以按自己的需要，给它加功能或者改功能，用来适应不同的训练场景。整个框架设计的出发点是实用和灵活，不是花架子。

## 怎么安装？

安装过程不算繁琐。官方提供了一键安装脚本。它会自动帮你安装Docker（版本需要≥25.0.0），然后把Tuoni部署起来。

用wget：

wget -O - https://tuoni.sh | bash
cd /srv/tuoni

用curl也行：

curl https://tuoni.sh | bash
cd /srv/tuoni

安装脚本会问你一些问题，比如设置管理员用户名密码。如果你嫌麻烦，或者想用在自动化部署里，可以设置静默安装。

加上`SILENT=1`就行：

export SILENT=1; curl https://tuoni.sh | bash

脚本支持一些环境变量来控制安装行为，下面这些都是可选的：

* SILENT= （默认不设置，设为1可以跳过所有提问）
* NO\_UPDATE= （默认不设置，设为1可以跳过更新应用的步骤）
* TUONI\_USERNAME=tuoni
* TUONI\_PASSWORD= （默认会自动生成一个）

* TUONI\_DOCKER\_IPV6\_ENABLED=false

简单解释下这几个参数：

* `SILENT=1`

  ：静默安装，跳过所有交互提示。
* `NO_UPDATE=1`

  ：如果已经装过了，这个参数会跳过更新步骤。
* `TUONI_USERNAME`

  和`TUONI_PASSWORD`：设置后台登录的账号密码。
* `TUONI_DOCKER_IPV6_ENABLED`

  ：默认关掉IPv6支持。
* 剩下的几个参数像`TUONI_REPO`、`TUONI_BRANCH`，普通用户不用管，是给开发自己测试用的。

安装脚本可以重复运行。如果检测到Tuoni已经安装，它会自动执行更新操作，然后重启C2服务。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfcEHwGbKCODbftykiaCeOYzoKdzKPMo78xHa1n0BaTGC5oVnic4x0TZwgJKxJUMtZPsTgwPwn6NroQzE0AVXcz3sapKHBMsOiaXk/640?wx_fmt=png&from=appmsg)

如果运气不好，运行脚本没反应，可以先检查下系统里有没有wget或curl工具，没有的话装上就行。

sudo apt-get install -y wget curl

## 看下长啥样

装好之后，你可以通过Web界面来管理。这是它的一个截图，可以看到整体布局和功能模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibelHMialM3E3UUNgcckT1vhDJSktOl7uLvYxqQjH172oa8gQOVBhbm6WU8K2ib5q12Jmsbbm36Eop9hGPVdJv4iboZkZYGYnvFTqk/640?wx_fmt=png&from=appmsg)

## 遇到问题怎么办？

使用过程中，有几个地方可能会卡住：

> 最大的坑可能是Docker版本。脚本要求Docker版本至少是25.0.0，如果你系统里是旧版本，得先升级Docker Engine，不然跑不起来。

另外，一键脚本默认是从GitHub拉代码。如果你那儿网络环境对GitHub访问不畅，可能会安装失败或者很慢。这种情况，你可能需要自己想办法解决网络问题。

静默安装时，默认密码是自动生成的。装完之后，一定要记得到`/srv/tuoni`目录下或者Docker日志里，把生成的密码找出来，不然进不去后台。

## 更多资料

想深入了解，比如插件开发、详细配置、API使用，可以去看看官方文档。文档里写得比较全。

官网文档地址：https://docs.shelldot.com/

总的来说，Tuoni算是一个设计得比较务实的红队框架，特别适合用来搭建内部训练环境。安装部署的步骤已经简化了很多，对于有Docker使用经验的人来说，十分钟内搭起来开始用，问题不大。

---

### 参考资料

[1] https://github.com/shell-dot/tuoni

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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