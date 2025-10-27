---
title: 攻防渗透集锦JS泄露突破多个后台
url: https://forum.butian.net/share/4538
source: 奇安信攻防社区
date: 2025-09-11
fetch_date: 2025-10-02T19:56:49.824655
---

# 攻防渗透集锦JS泄露突破多个后台

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

### 攻防渗透集锦JS泄露突破多个后台

记录近期渗透项目及护网攻防利用JS泄露突破后台案例,Nday扫的没有大佬快,0day没有大佬储备多,何不研究一下前后端分离网站下渗透突破思路呢,文章为笔记复制故无社区水印,欢迎转载 但请标明社区原创地址

### Swagger泄露到网站接管
#### 0x01 信息收集
经典开机登录框通过目录爆破,挖掘到一处`Swagger`文档泄露收获一枚未授权,且文档存在众多接口,此接口重点测试`GET`请求及接口名称为`list`相关,运气好会有信息泄露或者账号密码信息,虽然存在插件但是我还是习惯用`swagger-hack-main`工具提取出接口后,再用`BP`拼接接口访问单独处理,这样`hae`插件可以很快定位是否存在敏感参数
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846233810-8fbaa5c0-e1b7-458e-b15a-b39389644fe8.png "null")
`swagger-hack`可以将文档中的接口提取,但注意提取的位置必须是泄露`.json` 如果是`.html`将无法提取,一般只要出现了首页的`swagger`同样也会指明`json`格式文档的路径,拼接`.json`路径得到新的泄露体
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846233866-835b8a7b-3134-44cb-95fd-c44cd2d18f98.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846233926-84642a3d-0a81-4dd8-a820-621b9d6da018.png "null")
使用工具扫描,生成`swagger.csv`文件
```php
python swagger-hack2.0.py -u http://xxxxxx/swagger/v1/swagger.json
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234003-d0e481aa-edfe-4aa4-822c-20a871863bb2.png "null")
单独将里面的接口提出来,抓取一个首页包使用`BP`爆破
```php
/api/driver/msl/module/type
/api/driver/msl/module/list
/api/driver/msl/channel/list
/api/driver/msl/config/list
/api/driver/msl/config/read
/api/driver/simulation/list
/api/driver/simulation/gw/list
..........
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234100-1105379c-3bc2-466b-a7b0-6eccf72cb7b9.png "null")
接口爆破未两种一种`GET`直接拼接再就是`POST`携带空`JSON`,都需要尝试
```php
GET /api/driver/msl/module/type
---------------------------------
POST
Content-Type: application/json;
{
}
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234295-c703d856-755e-4cc0-ba07-4e508a66d3d2.png "null")
并且`swagger`泄露页面一些接口本来也会带出请求体参数,可以直接在泄露页面发包测试或者是带入数据包测试
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234388-4bfe40df-880f-42de-8ed1-2c5988d7c990.png "null")
#### 0x02 接口敏感信息
经过长达2分半时间的爆破,最终有多个接口出现内部的控制配置信息,以及多个账户密码泄露,
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234484-14c18a3c-796e-4c93-b290-ad28b438eeb6.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234568-f1b042f4-6891-4457-8391-3e3f80a721b7.png "null")
配置信息无法利用,故整理当前泄露的全部账号密码信息,尝试是否可以进入相关后台
```php
"brokerIP":"xx.xxx161.59",
"brokerPort":1883,
"clientID":"iot-driver-001",
"driverName":"MSL",
"clientName":"IoT Driver",
"userName":"msl\_mqtt\_user",
"password":"3HlcSiVhvalAq9JU",
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234682-f958d526-21d1-4131-87de-86b7e51a73d4.png "null")
```php
"brokerIP":"xxx.xxxx.32.65",
"brokerPort":1883,
"clientID":"iot-driver-003",
"driverName":"KNXMqtt Driver",
"userName":"msl\_mqtt\_user",
"password":"3HlcSiVhvalAq9JU",
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234766-18d6d970-2852-4d5a-bc20-99192c43912e.png "null")
```php
"clientId":"msl\_iot\_226CC04AF6026B84",
"userName":"iot-driver-user001",
"password":"z@.x%h&gt;4\*k18",
"name":"Client\_Test\_001",
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234861-b852ef05-f275-4f2a-9f34-5109ab5a72ba.png "null")
目前得到了两个IP地址已及账号密码,密码应该是那种在第一次注册时浏览器所生成的强密码,但是却保存到了配置文件中,那么依次对`IP`进行查询,看看是否有相关登录口尝试一发入魂！
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846234935-8eeb9f91-dd84-4295-b42a-66463cdf2c21.png "null")
```php
"brokerIP":"xx.xxx161.59",
"brokerIP":"xxx.xxxx.32.65",
全部账号密码整理
"userName":"msl\_mqtt\_user",
"password":"3HlcSiVhvalAq9JU",
"userName":"iot-driver-user001",
"password":"z@.x%h&gt;4\*k18"
```
首先收集`161.59` 通过观察定位到此`icon`和上方接口泄露出的的`mqtt`服务有些相似,那么就从这里入手
存在两个登录口,
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235019-6f3c2125-b321-4609-ace8-af6c65c179ec.png "null")
当我用泄露的密码直接登录以为能美美进入时,两个登录口却全部失败,第一个无任意有效反馈直接无法连接服务器另一个则是账号错误
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235086-098eea98-24fc-4d88-b40f-61c71b56abdd.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235185-45459034-1499-416f-b3a2-df8276fb9d62.png "null")
#### 0x03 渗透受挫
我继续尝试把得到的`2`组账号密码来回变换,不同组合方式在两个登录口重新尝试进入,均一无所获,故先放弃转而进攻`32.65`资产,显示多个资产,一一尝试,只有2处是有效的
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235278-07050586-2ebf-4fa5-aba2-fc92a3f10811.png "null")
出现两个有效登录框,相关特征跟上面的第一个一致,再次进行密码碰撞尝试登录,同样一无所获,目前4个网站没有一点反馈,一度怀疑前面的信息中肯定是漏掉了什么,故回去再看`swagger`接口泄露寻找信息,企业都能把密码配置文件放到公网了未删除了,那么安全意识肯定非常薄弱,我坚信这一点才一直会想去尝试
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235354-0fe5aea8-beee-4f01-ad19-d3ab5d7d8edc.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235461-cb28d39a-538c-4fbd-b957-49bfc62d87a9.png "null")
重新整理好接口泄露所有出现`name`相关字段的值,再次尝试对这4个登录框碰撞仍旧无法正确登录后台
```php
"clientName":"IoT Driver",
"driverName":"KNXMqtt Driver",
"name":"Client\_Test\_001",
```
思考一下从企业人员视角出发,大多密码账号会和单位简写有关,企业简称参数正是`MSL` 并且接口泄露出的一个`name`值也出现了`MSL`
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235553-39731ec4-d3af-4140-842a-d20f93a296be.png "null")
重新测试来到登录口,逐一测试,来到第一个登录口无任何响应
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235627-33278a8c-0e01-4819-a272-d248581c4f53.png "null")
来到第二个地方测试,通过两次账号不同所返回的响应,有经验的大佬已经发现了,典型的用户名枚举情况啊,但这里给出我的提示却是证明我的猜想是正确的,`MSL`企业简称正是系统的登录有效用户名
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235703-85c2ef66-b7ba-4678-8dd2-06f8aa7ff9f7.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846235829-daab9434-1cd1-4adc-a4c1-da2f2422b4c9.png "null")
这里我已经非常开心了,已经幻想自己进入后台,但是当我将前面所获得的密码再次进行用户名不变密码改变的情况爆破时,仍然无法进入.....而后继续按照此方式对其他的登录框进行操作,但是其他登录框并无用户枚举情况,但我还是将`MSL` 作为用户名配合上方得到的密码进行爆破, 仍就一无所获,哈基W,....还是办不到吗
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236011-9f50ccbb-d696-4782-99e2-201b45eec13e.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236139-48eba06f-6bef-4209-8e80-261c7b5938c1.png "null")
#### 0x04 弱口令之神
经历上述操作仍无法出货,真的很想关掉BP直接换站,但测试肯定是需要将所有思路全部穷尽,后开始上字典对第二个登录框爆破,寄希望与管理员未设置强密码,只针对用户名做了企业简写的操作
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236237-010b200e-db00-4905-b3bc-c31959bbf09d.png "null")
很难想象,第一个就出了....那我之前的信息收集 多个站来回碰撞算什么.....算我有耐心吗,我好像一拳打在了棉花上,我原以为弱口令真正意义上并不算一个漏洞,现在发现我对这个漏洞一无所知
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236324-8814f5a3-4404-4bed-9327-41245efcf4a4.png "null")
通过口令进入第二个网站发现是登录口,测试账号并无数据,凭着管理员头脑简单想法 相同账号密码去登录其他资产网站，毫无疑问直接拿下！
控制大楼全部灯光、电梯 等其他硬件设施
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236645-c18a5d06-ba47-4310-84b4-75c060aeb1d1.png "null")
控制酒店内所有客房服务,全区域空调开关,并且可调用摄像头监控
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236821-6fdc1b1c-f958-4b29-aed6-1b0f9eabb76c.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846236929-c20e88a2-139d-4062-9adc-ce8e282c4210.png "null")
### 登录框接口打入Nacos
站点已修复,无法完整复现,只能从留存的报告成果截图阐述整个流程。开局登录框,。通过域名后跟随`#`符号判断此为`Vue`框架站点,那么着重寻找未授权 信息泄露！
```php
https://xxxxxx/#/login
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846237027-5d21df5a-b50c-4cae-9515-0aaf3950127b.png "null")
首页抓取一个刷新的包,或者是输入账号密码的包 ,看看会加载哪些请求方便构造接口拼接,同时也可以观察是否有前置目录情况,刷新提供请求服务的地址是`/admin/tenant/list` 并且加载了`chunk`异步`JS` 这是现代前端构建工具（如 `Webpack、Vite` 等）的常见产物,将代码拆分为多个 `chunk`（代码块），主程序加载时先加载核心代码，其他非必要代码（如路由组件、第三方库）会被分割成独立的 `chunk` 文件，按需异步加载
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755847810955-57879ce0-29da-496a-afb3-abb075cd5b16.png)
```php
/admin/tenant/list
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1755846237266-49eda392-3d0e-47bd-86b8-4a679bcfe0d9.png "null")
#...