---
title: SRC 视角下：渗透测试中的逻辑漏洞思路博弈
url: https://forum.butian.net/share/4441
source: 奇安信攻防社区
date: 2025-07-01
fetch_date: 2025-10-06T23:16:24.276815
---

# SRC 视角下：渗透测试中的逻辑漏洞思路博弈

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

### SRC 视角下：渗透测试中的逻辑漏洞思路博弈

最近挖到的中高危漏洞，既没靠 `0day` 这种 "王炸"，也没搞复杂利用链 "炫技"，纯靠瞪大眼睛当 "人肉扫描器"，连标点符号都不放过地逐行比对参数和响应。直到某个昏昏欲睡的下午，随手改了个藏在 `JSON` 数据深处的小参数，系统突然像短路反馈了全新的信息，反常的响应直接暴露未授权访问的 "马脚"。当时激动得差点把咖啡泼到键盘上，看着满地咖啡渍才顿悟 —— 原来倒掉的咖啡，比直接喝咖啡提神一百倍

渗透测试人员堪称代码世界的 "超级侦探"，手握 `Burp Suite` 这把 "神奇放大镜"，进入甲方的资产海洋遨游,在其中对着页面疯狂改参数、发请求，却总被系统用平淡入手的响应打发，如同在广阔的太平洋掷入一枚石子,不泛起一丝涟漪; 要么直接拦截请求让人气的砸电脑。开局登录框更是 "经典打卡圣地"，测 `API` 接口这边要扮成研究正常逻辑的好学生，那边得秒变设计注入 `Payload` 的 脑洞大师,还得时刻提防 `WAF`悄无声息送你一张`404`飞机票✈️, 漏洞挖掘本就是逆天而行,挖不到才是正常的
最近挖到的中高危漏洞，既没靠 `0day` 这种 "王炸"，也没搞复杂利用链 "炫技"，纯靠瞪大眼睛当 "人肉扫描器"，连标点符号都不放过地逐行比对参数和响应。直到某个昏昏欲睡的下午，随手改了个藏在 `JSON` 数据深处的小参数，系统突然像短路反馈了全新的信息，反常的响应直接暴露未授权访问的 "马脚"。当时激动得差点把咖啡泼到键盘上，看着满地咖啡渍才顿悟 —— 原来倒掉的咖啡，比直接喝咖啡提神一百倍
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405912150-71ac80bc-b817-4b61-bd40-ca6949f991a6.png "null")
无限抽奖币
-----
新的功能点往往被常规功能点所裹挟,黑盒测试的我们只能点点点,当坚持到隐秘功能点出现的那一刻,漏洞已经是呼之欲出了
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913087-8acb1d88-d05d-4af4-a5ec-8c8542e3f8da.png "null")
微信搜索厂商资产找到一处不起眼的资产,`20`币一次并且可得实物
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913145-b344db0f-e5be-435d-a75e-1b3c49a6e3ae.png "null")
初始币是`100`当我小心翼翼的尝试投币点进行一些,自定投币数量,修改返回包控制所得物品,并发签到等操作时,结果洞还没挖到我的游戏币就已经快测没了,真的是天塌了
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913222-3bc1ed75-d5a7-4520-a852-e3a26d345dd0.png "null")
当时已经非常晚了到了12点,当我最后一次爪子进行抓娃娃的时候,修改请求包发现还是一无所获,悬着的心最终还是死了,已经准备`win+x+u u` 光速下播,但游戏币消失的时候又出现了新的功能点,这让我死去的心又再次燃烧起来
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913284-40e6d781-0bf8-4ba2-9eb1-568dc98453e3.png "null")
分享赚币,点击后`BP`记录接口,在历史记录逐个对数据包进行查看,最终凭借经验锁定`/app/point/doll/share`接口就是关键的数值包,它的值所控制的就是所得金币数量
```php
points=15
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913341-256e4dde-d9cf-4ab0-b41d-52ed1d1c5581.png "null")
思路都理清了那还说啥,直接重发狠狠的输入最大数值
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913436-2b820fda-9a8c-4fc5-bfbf-dfa355bd8f87.png "null")
不出意外成功,爽吃一中,又可以多买几个馒头恰了,这次渗透告诉我,不测试完所有功能点就绝对不轻言放弃,不要自己跟自己说丧气话,因为大多数人在一个站比如测试越权发现有鉴权,就下定义觉得这个站已经没有越权了,这是万万不行的,作为白帽子最后是把所有思路穷尽才算是一次完整的渗透测试,细心再细心,虽然这样很枯燥但是长此以往相信肯定会有所收获
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913497-47402e01-3db9-47a2-a9cb-7382c2b17675.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913558-64a45ca3-766e-4d62-893d-54924e6b6e7f.png "null")
可控所得优惠卷
-------
功能点购入某些物品系统会赠送一部分优惠卷,但大多是一些小额优惠卷,除非购买昂贵的服务才会赠送价格不菲的优惠卷,利用低级服务所得优惠卷,通过手法找到高等级优惠卷对应`token`，替换后造成刷优惠卷效果
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913618-dbb87337-c17b-4755-8f84-2aa2fd26f762.png "null")
站点特征较明显,省略一些前期发现步骤,快进到数据包分析,选择一个商品服务进行下单,`BP`记录所有流量,通过逐个分析定位到此接口为关键的创建订单包,将其测试发送到重发起等待进一步测试
```php
https://xxxxx/restapi/soa2/19691/orderCreate?\_fxpcqlnired
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913681-ee9d0b2c-1fbc-4603-9ac3-337630f61f9c.png "null")
进行小程序看先前创建的订单,看有没有可以操作的业务,观察到订单创建后成功支付会相对应的赠送优惠卷
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913742-440de67d-3d32-44b5-8e99-0615cc4a72fd.png "null")
都是一些不起眼的小福利卷,跟`QQ`空间兰博基尼`5`元代金券不能说没有区别只能说一模一样
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913802-94fcb207-c031-4039-bddc-90f70d88325f.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405913856-f3eea552-d288-48d1-843d-7e5c8f601b93.png "null")
将创建订单接口发送到重发器后,观察数据包,这种涉及多个流程的业务数据包一般都很多参数,有的是关键参数,有的是多余参数用于迷惑,通过"人肉扫描器"一段段观察,定位到`data` 数据体记录了优惠卷对应的`token`
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914006-e3f785ac-4a98-4607-b353-c5c782e89548.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914068-9b2f6d03-a528-4a71-8118-b3a9524474c4.png "null")
通过一系列手法,找到了其他优惠卷的`token`,然后对先前的三处优惠卷`token`进行替换.并且全是一模一样的,意味着我可以通过低级服务自定义所得优惠卷,并且叠加
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914171-4924e257-cc07-472b-ab8e-fd42f384014f.png "null")
当前替换后再次创建新订单,先前的三张低级优惠卷已经被替换为了三张豪车打车减免卷,并且只需要我知道任意卷的`token`,就可以得到对应券,还可以叠加字段进行复用
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914245-92b92a40-8155-4b21-8572-a8d763902613.png "null")
普通的CSRF
-------
如今各种逻辑漏洞,云攻防,`Top10` 为主流的今天,最基础的`CSRF`往往是同其他漏洞结合利用,但忽略了单个`CSRF`所能造成的影响,我理解的是只要功能涉及到主观操作场景,如修改信息,增加收货地址,发送邮件...等等需要主观意愿才能进行,并且请求中并没有发现`token`或其他校验字段均可以尝试`CSRF`
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914313-f81382df-6175-4be6-950b-8f02930820f3.png "null")
正常用户修改绑定的邮箱需要输入交易密码才可以修改，但是功能点的个人信息接口可以直接修改绑定的邮箱,制作`post`请求的`csrf`数据包发送受害者点击, 就会自动修改绑定邮箱及个人信息为我们所设置的
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914394-83d0d8cb-9390-42ff-806b-8319d5083753.png "null")
为不影响业务,实名认证后准备两个小号相互测试
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914487-b281c6e4-a007-4971-bd9f-339189b6ab29.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914575-000d7411-84c8-41d6-9585-f4af7d66e4f4.png "null")
对个人信息进行修改,`BP`记录所有的流量,此接口为更新信息
```php
/fund/apl/postUserinfo
```
观察更新个人信息功能第一是携带了邮箱更新,如上所示,正常我们单独修改关键的邮箱是需要交易密码的, 因为站点是一处涉及基金交易,但是普通的修改个人信息却是可以直接修改邮箱,跳过交易密码,第二是请求包没有`token`等其他涉及状态码字段,那么是不是可以尝试一下`CSRF`呢
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914636-20325635-82ed-4cf4-a120-4e3ec3bf19d0.png "null")
将更新`POST`请求右键制作为`CSRFPOC` 把生成的代码拷贝一下随意改一下信息为自定义的,然后本地作为`html`文件
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914712-08ffc6de-922d-44fe-92f1-dd54cf1781e0.png "null")
`poc.html` 用当前小号登录的浏览器去打开,点击后返回修改成功
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914779-be4d8556-e254-4e4b-84d2-cc5a618c5d16.png "null")
刷新站点,当前的个人信息包括邮箱已经是我们所设置的,`CSRF` 攻击成功
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914847-7735b588-3ace-4222-84b4-ef4b01a19bcc.png "null")
网站泄露导致接管
--------
写多了企业`SRC`报告,现如今刚刚初入社会投身于工作当中,下班后再去花精力挖掘`SRC`可能是越来越少,还是怀念大学的时光没有压力,别管挖没挖到洞,你只管去挖剩下的交给时间,现在如果下班没有产出其实还是挺浪费时间的,因为本来是可以利用这个时间再去学习一些新知识,提高自己技术....分享一个在近期在公司渗透测试一个单位的过程,最终也是拿下网站超级管理员
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914922-f4d0ce74-004a-4692-a42c-23263ac0b53e.png "null")
企业`SRC`大多目标较少,且会给出具体的域名范围,工作渗透项目因为是会有地区网信办授权,所以给我某一地区庞大的单位,从中进行渗透,海量的资产梳理不是一件简单的事情
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405914980-8f998bc9-90f9-483e-af7f-d3d553c3bc58.png "null")
### 测绘资产处理
众多单位名有些是存在备案网址的,这些才是有效资产可以进行渗透,那么无备案的单位如果排除呢？测绘网站`hunter`可以很好的做到这一点，它支持企业备案名称进行查询,这是其他`fofa 360` 都没有的,所有在攻防项目还是企业渗透开局海量单位名`hunter`是最佳的选择,唯一缺点这个打法比较吃积分
```php
icp.name="xxx"
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1750405915042-2d68bb28-0feb-4a56-8a8b-5c41369578d8.png "null")
既然知道`hunter`可以根据备案名查询,那么写一个批量脚本,填入`API`进行调用语法即可
```php
import requests
import base64
import time
import json
import pandas as pd
# 鹰图平台的 API 地址
BASE\_URL = "https://hunter.qianxin.com"
SEARCH\_ENDPOINT = "/openApi/search"
# 你的 API Key（从鹰图平台获取）
API\_KEY = "" # 替换为实际的 API Key
# 字段翻译映射表
FIELD\_TRANSLATION = {
"code": "状态码",
"message": "错误信息",
"data": "数据部分",
"total": "资产总数",
"time": "时间",
"arr": "资产列表",
"is\_risk": "风险资产",
"url": "URL地址",
"ip": "IP地址",
"port": "端口号",
"web\_title": "网站标题",
"domain": "域名",
"is\_risk\_protocol": "高危协议",
"protocol": "协议类型",
"base\_protocol": "通讯协议",
"status\_code": "网站状态码",
"component": "应用组件/版本",
"os": "操作系统",
"company": "备案单位",
"number": "备案号",
"icp\_exception": "备案异常",
"country": "国家",
"province": "省份",
"city": "市区",
"ip\_tag": "IP标签",
"asset\_tag": "资产标签",
"vul\_list": "历史漏洞",
"updated\_at": "探查时间",
"is\_web": "Web资产",
"name": "组件名称",
"version": "组件版本",
"as\_org": "注册机构",
"isp": "运营...