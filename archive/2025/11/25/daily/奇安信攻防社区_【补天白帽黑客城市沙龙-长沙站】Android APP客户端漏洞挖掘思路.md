---
title: 【补天白帽黑客城市沙龙-长沙站】Android APP客户端漏洞挖掘思路
url: https://forum.butian.net/share/4661
source: 奇安信攻防社区
date: 2025-11-25
fetch_date: 2025-11-26T03:12:36.129524
---

# 【补天白帽黑客城市沙龙-长沙站】Android APP客户端漏洞挖掘思路

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
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【补天白帽黑客城市沙龙-长沙站】Android APP客户端漏洞挖掘思路

随着Android系统在移动设备中的主导地位，APP客户端安全漏洞已成为黑客攻击的主要入口。本议题将梳理Android APP常见客户端漏洞挖掘思路，包括:四大组件漏洞、Webview组件漏洞、防抓包对抗等，并结合实际案例演示漏洞挖掘过程。

### Speaker：China\\_Sec
![幻灯片1.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-8084e0ed33e761452408eb9601c8964d9be7150c.png)
![幻灯片2.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-8f63de38265fc0b4748574f9e3fab181e1dfc26b.png)
![幻灯片3.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-455df3612832dce088f60e7bdce78281455e25e3.png)
![幻灯片4.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-378fe58c1594e86a5f29011847c7c718a20928bd.png)
![幻灯片5.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-c076548e7c34e00bf4862ff05b0507f46c0ccfe9.png)
![幻灯片6.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-68066553d785095ca2fbdb51a989ecc0654e5c4f.png)
![幻灯片7.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-cdb09aa7865683cc60ab006ad23edb70908f5f30.png)
![幻灯片8.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-a33e75eafd2d1424b900dd17813e703843d5da8f.png)
![幻灯片9.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-7f65d150656e0eeb3ec90b263e66d014f1fa592f.png)
![幻灯片10.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-7863eaca64685d7fe908761141db0f701563ec5e.png)
![幻灯片11.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-044ff97d74480c49fc858fbfe14a9cd3dfe879be.png)
![幻灯片12.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-60def1952426a05cc11906b12a0888a4fcffeb60.png)
![幻灯片13.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-cac73f7ece5f784f2217025837ebd0166fe2e474.png)
![幻灯片14.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-c5d18df0d6cdfd03b15a0adf85386574b57c3ec8.png)
![幻灯片15.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-13574f5d8cfc48067508797455c9a2e66c10d6eb.png)
![幻灯片16.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-42851d2ae50451bfedb2e81c6dc47ca2ef0d20f0.png)
![幻灯片17.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-b2edba123bf55311c1ff2dc3e23881f91fe82d32.png)
![幻灯片18.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-19b1f88387c391419fd450dcec192902cd9347a5.png)
![幻灯片19.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-acbe6631f0c7b02ce13534b7d4830da5bb878379.png)
![幻灯片20.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-c4a9d6b4479e27d36bc8d2e195a9a3845b53b214.png)
![幻灯片21.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-331c645251eecd74c6040d5bb184d9aca0b97936.png)
![幻灯片22.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-475ecf61e8147624cf00ae6bc90a597f1a0fe045.png)
![幻灯片23.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-a9ddadec9bff1bdd930d5ff20c0e7999a7ce8686.png)
![幻灯片24.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-ae7c82a841504b2112d48ee9ee2f188af7226ab0.png)
![幻灯片25.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-8acbf0d6857c090e6c153dd46873712c79b4032e.png)
![幻灯片26.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-9d928cc523b73fb9e2fc1acb41291d7f86a56ca2.png)
![幻灯片27.PNG](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-90cb1d273439a82c78b7fbe8b10d3e2dec6a7803.png)

* 发表于 2025-11-25 10:43:53
* 阅读 ( 267 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![奇安信攻防社区](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/avatars/000/00/00/user_origin_34.png)](https://forum.butian.net/people/34)

[奇安信攻防社区](https://forum.butian.net/people/34)

奇安信攻防社区官方账号

41 篇文章

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