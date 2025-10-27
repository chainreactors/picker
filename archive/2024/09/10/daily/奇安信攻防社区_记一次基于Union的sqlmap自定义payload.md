---
title: 记一次基于Union的sqlmap自定义payload
url: https://forum.butian.net/share/3708
source: 奇安信攻防社区
date: 2024-09-10
fetch_date: 2025-10-06T18:21:55.000783
---

# 记一次基于Union的sqlmap自定义payload

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

### 记一次基于Union的sqlmap自定义payload

hw期间某晚上10点，某知名小朋友审计了一套bc源码，有sql注入，注入的位置比较刁钻，sqlmap无法识别，不能取证 (公众号转发务必说明来源，标注作者！)

hw期间某晚上10点，某知名小朋友审计了一套bc源码，有sql注入，注入的位置比较刁钻，sqlmap无法识别，不能取证
##### 注入场景
```js
pay.php?id=pay`+/\*\_\*/where+false 注入error
pay.php?id=pay`+/\*\_\*/where+false# 注入正常
```
![Snipaste\_2024-08-13\_23-43-18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-34eb4ca1550ccb57df23aaabd462a9309e5eb508.png)
![Snipaste\_2024-08-13\_22-54-36.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-196e7fcd53f245d5e95631a9ea6c2a4e8edc5a9e.png)
###### sqlmap无法识别
![微信图片\_20240813223537-1723561048427.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-afe79b09fb31c96f33af2d5a69e6fa531fc03710.png)
注入位置比较刁钻，小朋友说得保留
```js
pay`+/\*\_\*/where+false
```
字段才可控，
在网上搜了一圈，没有找到基于union的自定义查询，于是下了些功夫，研究了sqlmap的union注入流程
##### union注入流程
union联合查询，用于合并左右两侧select语句的结果，得要求两侧select的列数相同，两侧select列数不同发生error,那注入就失败;因此 union注入必须得先进行order by的判断确定列数，后续才能拼接子查询测试。
![Snipaste\_2024-08-13\_23-25-39.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1ba67ae92b089d4f3621c434291fb38ff07348b6.png)
![Snipaste\_2024-08-13\_23-26-34.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-bba6a2c4c30e7fb491148e7a67b7d02e85a68a45.png)
所以，站点union注入失败的原因在于order by测试没命中
![Snipaste\_2024-08-13\_23-07-38.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-6ad534c4446c93a7fd3a4f2cc35fab1c204829fc.png)
sqlmap测试union注入的文件在data\\xml\\payloads\\union\\_query.xml 根据发包提示信息和order by相关的是"Generic UNION query"模板
![Snipaste\_2024-08-13\_23-49-57.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-3cbf755f33483da57f390159e4d5c9140526dcad.png)
网上转了一圈，参考报错注入和时间注入的修改request和response两处标签，通过正则等方式去匹配命中，发现\*\*无法过编译\*\*， 后续测试，union\\_query.xml的标签\[vector\]、\[request\]、\[response\]不可控，(修改后测试流程依旧没变化)。
猜测可能和\*\*子语句测试\*\*有关，站在sqlmap的视角，他肯定是无法识别当前子语句注入方式的，比如位置是在where后可控还是order by后可控，或者是逻辑符可控，比如例示列名 (SELECT \\* FROM users ORDER BY column\\_name)等，得构造某特定的类型才能识别，自定义类型，跟进到xml/payloads/\*\*boundaries.xml\*\*
###### 自定义payload
boundaries文件几处属性是控制自定义字符的，preffix和suffix，把这里的preffix改为站点的自定义字段
![Snipaste\_2024-08-14\_08-02-18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fa62132ad06a54af23f66d4e81ec381428fdf28b.png)
然后得考虑该字段如何去和union模板里的test组合问题，网上转了一圈，当boundaries的clause和where属性值包含union模板的clause、where两个属性值即会匹配组合
clause取值为1-9，联合查询有关的子查询有 where、order by，取值为1，3
![Snipaste\_2024-08-14\_08-11-41.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-265c6d692f309318a745981581c191e318f6d693.png)
where取值为1-3，where标签，用来确定整体注入payload的插入位置，比如第一个注入参数，取值为1，第二个注入参数，取值为2，这里就默认为1
![Snipaste\_2024-08-14\_08-14-26.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-6bb8d3f60a1248c9f9589d5d7693745cbe4089ad.png)
```js
<boundary>
<level>1</level>
<clause>1,2</clause>
<where>1</where>
<ptype>1</ptype>
<prefix>pay`+/\*\_\*/where+false</prefix>
<suffix>#</suffix>
</boundary>
```
观察union模板的"Generic UNION query" where、clause标签是否能匹配
![Snipaste\_2024-08-14\_08-20-04.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-15a5e769a6974167bdba5cd2039f613b6222d6aa.png)
没啥问题，发包测试
##### 测试问题
再测试已经能识别到自定义的payload了，但探测的深度很有限,order by的注入得取两个值，一大一小来确定字段，从发包payload来看只发了order by 1
![Snipaste\_2024-08-14\_08-22-46.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-d6df6dc1621b149306e2120edc157288698a1324.png)
把流量挂到burp看看，代理后，再次发包
![Snipaste\_2024-08-14\_08-28-26.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-00e7a312db0f6efe3dd0b1b860353c100a4452ec.png)
```js
pay`+/\*\_\*/where+false order by 1#
pay`+/\*\_\*/where+false order by 4839#
```
这里命中了，但没识别出order by的注入
###### 编码问题
在这折腾了好久，觉得是sqlmap的版本原因，下载了最新的版本，再次发包，再测试发现order by 4839#这部分包又不测试了，觉得是代理的问题，于是换了socks发现也一样，后续发现报文出问题了
![Snipaste\_2024-08-14\_08-40-39.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b7606e1b428b3ed0bf4184351f806340e57af91f.png)
sqlmap报文编码导致自定义的字符失效了，被编码了%2B%2F%2A\\_%2A%2F
burp做个发包替换，
```js
%2B%2F%2A\_%2A%2F->pay`+/\*\_\*/where
```
###### 识别注入
识别成功，order by
![Snipaste\_2024-08-14\_08-45-34.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-693cfe20a644bd521d6ce329b675fdb5e1a46ab6.png)
后续的流程就很简单了，识别到order by 判断列数，union子查询拼接case条件从句
![Snipaste\_2024-08-14\_08-48-54.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-476bd8fdef3c9ff71f8c1c8cc48379eb5a29676e.png)
![Snipaste\_2024-08-14\_10-08-40.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9fbc2fbf099fa405abf1e7c43d6e70380057a0a7.png)
取证完成
![Snipaste\_2024-08-14\_08-50-22.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0a83d9ddf3baa82253bfa7bf79845ff0830d42de.png)
##### 扩展思路
###### 自定义前后缀
后续发现一种更便捷的方式，不用修改boundary，自定义前后缀，在sqlmap发包的时候提供
```js
preffix="pay`+/\*\_\*/where"
suffix="#"
technique=U
```
这样发包会更精准，由于提供了前缀，sqlma后续不会从boundary取注入符，会调用默认的clause和where去匹配union\\_query.xml里的test模板，免去了其他符号的测试
完整参数
![Snipaste\_2024-08-14\_09-03-02.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-bd343a2c396b3365c401a18f0f6e6ad9965ff7e8.png)
```js
--proxy=https://127.0.0.1:8080 --prefix=pay`+/\*\_\*/where+false --suffix=# -v 3 --technique U
```

* 发表于 2024-09-09 10:00:01
* 阅读 ( 4865 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![echoa](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/7780)

[echoa](https://forum.butian.net/people/7780)

6 篇文章

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

#### ![echoa](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---