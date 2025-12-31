---
title: 【2025补天白帽黑客盛典】I flip WASM bits
url: https://forum.butian.net/share/4722
source: 奇安信攻防社区
date: 2025-12-30
fetch_date: 2025-12-31T03:23:43.381162
---

# 【2025补天白帽黑客盛典】I flip WASM bits

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【2025补天白帽黑客盛典】I flip WASM bits

我们针对Blackhat ASIA 2023议题:Attacking WebAssembly Compiler of WebKit使用的方法进行了改进，对Firefox、Chrome浏览器WASM模块进行fuzz并发现了多个漏洞。我们针对其中Firefox浏览器一个典型的WASM漏洞进行了详细分析,包含Firefox的一些机制和针对WASM memory的优化,揭示了漏洞产生的本质原因:新的WASM提案和功能的实现导致一些边界检查的绕过，实现新功能时旧功能的代码修改不完全导致新漏洞的出现。

### Speaker：neseesun
![幻灯片1.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-689bdddf25e542f11750a73aa8af95475112cae2.png)
![幻灯片2.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-34e5be60954eb51f009e878d82d164c2bbef57d1.png)
![幻灯片3.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-08951e615170e4f926bf670e0aa177f489b12d1e.png)
![幻灯片4.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-3976c23ec7c95bf2003628c5db51642575292dbc.png)
![幻灯片5.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-42d7cf86a8cba82c9241b063d0cdb7830a712121.png)
![幻灯片6.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-a5ec2f3772c3f7f3c77567f40ae26071a58dbe9e.png)
![幻灯片7.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-ea007f31b68ae9e4eb38fc21fc3ec8537fa2c748.png)
![幻灯片8.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-aaa1074221e4614eff8fae2bf51f79eb4c166c88.png)
![幻灯片9.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-45f5e5ce491bedddfbc5bd3331ada1d6e7cf9cfc.png)
![幻灯片10.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-7ebaf5af57c26f4d0fe6c66c42418ee1c69db218.png)
![幻灯片11.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-cfedc84cfcaa2f2200f803133798f94d40c06292.png)
![幻灯片12.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-3184937b8b9575bde72245adc98b6bc31e2e7dfa.png)
![幻灯片13.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-333b0607c9bf0737182b5b3b9f08da74fdd4c7de.png)
![幻灯片14.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-dc3405e620cce3eda02772c4060d389d05fd32a7.png)
![幻灯片15.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-0fecd7ffbac6dda4dc3dba3b63a69d5443fb3f92.png)
![幻灯片16.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-85c12d09d8126157bf3940bc17cc8866f75c1030.png)
![幻灯片17.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-c35fb2ce96d3d6f258d476d09ce033235442ca5c.png)
![幻灯片18.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-d98c174303dfd3c262c3133fc9acb3d848474fbd.png)
![幻灯片19.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-5f48d2108c0889b90da5d26e055ac989e6ee2a42.png)
![幻灯片20.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-616d15da2bdf79f7c81ab2d67812e96e79996533.png)
![幻灯片21.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-aa37934f448fd250bb77d5e0b5a11b1519d17bc9.png)
![幻灯片22.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-2004f0612accb21ef496b90defb90ed6fc0b9a9d.png)
![幻灯片23.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-50dd7bf46ca9ece5f9b708e2f6af7d99070f635e.png)
![幻灯片24.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-bd7f9e0bf709bf4cb8cc00add783525c1f482455.png)
![幻灯片25.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-80e4b658be36f25bbe7251fbf0343f3affaf0af4.png)
![幻灯片26.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-44c5ce29a2c575b97f19223529924b34e4d42398.png)
![幻灯片27.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-ed60c102c5f0cabd6351c9bca2367f58761918a6.png)

* 发表于 2025-12-30 10:44:36
* 阅读 ( 133 )
* 分类：[AI 人工智能](https://forum.butian.net/community/AI)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![奇安信攻防社区](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/avatars/000/00/00/user_origin_34.png)](https://forum.butian.net/people/34)

[奇安信攻防社区](https://forum.butian.net/people/34)

奇安信攻防社区官方账号

46 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![奇安信攻防社区](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/avatars/000/00/00/user_origin_34.png)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---