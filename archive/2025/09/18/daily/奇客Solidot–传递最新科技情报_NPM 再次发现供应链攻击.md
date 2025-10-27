---
title: NPM 再次发现供应链攻击
url: https://www.solidot.org/story?sid=82340
source: 奇客Solidot–传递最新科技情报
date: 2025-09-18
fetch_date: 2025-10-02T20:18:04.076829
---

# NPM 再次发现供应链攻击

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251001)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 4087 次**

## NPM 再次发现供应链攻击

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2025年09月17日 18时54分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82340&appkey=1370085986&title=NPM%20%E5%86%8D%E6%AC%A1%E5%8F%91%E7%8E%B0%E4%BE%9B%E5%BA%94%E9%93%BE%E6%94%BB%E5%87%BB%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自遗忘之海**

在 NPM 包维护者被钓鱼攻击导致数十个包被植入窃取加密货币的恶意代码之后，NPM 包再次遭遇供应链攻击，，这一次攻击者可能有点恶作剧。至少 187 个 NPM 包感染了以《沙丘》中沙虫命名的自我复制蠕虫 Shai-Hulu，它会窃取开发者的凭证，然后公开发布到 GitHub 上的 Shai-Hulud 库中。一旦开发者安装了感染了蠕虫的 NPM 包，恶意软件会搜寻 npm 令牌，一旦发现它会修改该 npm 令牌能访问的 20 个最流行的包，植入该蠕虫，发布新版本。安全公司 CrowdStrike 有至少 25 个 NPM 包感染了该蠕虫，该公司表示这些软件包没有被 Falcon 使用，因此 Falcon 不受影响。安全研究人员发现，攻击者有意放过了 Windows 平台，假设开发者在 Linux 或 macOS 环境中工作。
krebsonsecurity.com/2025/09/self-replicating-worm-hits-180-software-packages/

[回复](/comments?sid=82340&op=reply&type=story)

﻿

尊严不值钱，却是我唯一真正拥有的！

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251001)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>