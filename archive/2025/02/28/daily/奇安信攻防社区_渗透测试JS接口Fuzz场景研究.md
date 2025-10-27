---
title: 渗透测试JS接口Fuzz场景研究
url: https://forum.butian.net/share/4163
source: 奇安信攻防社区
date: 2025-02-28
fetch_date: 2025-10-06T20:32:30.893541
---

# 渗透测试JS接口Fuzz场景研究

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

### 渗透测试JS接口Fuzz场景研究

* [渗透测试](https://forum.butian.net/topic/47)

渗透测试中当页面功能点过少无处可测,或者攻防、SRC场景下开局一个登录框尝试弱口令,爆破、注入无果后针对JS接口寻找未授权信息泄露成为了得分关键,介绍尝试测试思路以及对参数Fuzz 手段

渗透测试中当页面功能点过少无处可测,或者攻防、`SRC`场景下开局一个登录框尝试弱口令,爆破、注入无果后针对`JS`接口寻找未授权信息泄露成为了得分关键
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587153-3e517f8a-169b-4f11-ae36-2e7cce6fecfb.png "null")
前端Webpack接口
-----------
`Vue`框架并且使用`Webpack`打包更容易产生未授权,不是框架本身未授权而是开发者大多使用前后端分离,接口较多更容易出现不鉴权情况
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587222-c7cec178-c1dd-490c-a6ac-4bcc9b5da1bd.png "null")
### 反编译`js.map`
`Vue`使用`webpack`(静态资源打包器)的时候，如果未进行正确配置，会产生一个`app.js.map`文件，而这个`js.map`可以通过`Node.js`环境安装`reverse-sourcemap`工具来反编译还原`Vue`源代码
[Webpack源码泄露反编译教程](https://blog.csdn.net/qq\_41760817/article/details/134977775)
```php
reverse-sourcemap -o aaa -v app.9fbea7c7.js.map
```
还原源代码`JS`文件中, 直接找关键的`api`目录、`config`目录从中提取出新的接口进行拼接测试未授权漏洞
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587293-855ecf52-d50b-4150-993f-2a0f70d4347c.png "null")
\*\*Python脚本提取JS接口\*\*
```php
import re
# 读取文件内容
file\_path = '1.js'
with open(file\_path, 'r', encoding='utf-8') as file:
js\_code = file.read()
# 使用正则表达式提取路径
# 匹配 GET 或 POST 请求的路径，支持单引号或双引号
pattern = r'''(D\.post|D\.get)\(["']([^"']+)["']'''
matches = re.findall(pattern, js\_code)
# 打印匹配到的路径
if matches:
print("Matched paths:")
for match in matches:
method, path = match
print(f"{method.upper()}: {path}")
else:
print("No paths matched.")
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587361-bf53ea62-bca5-421a-be7d-279555a684ee.png "null")
### `Packer-Fuzzer`寻找新接口`API`
`Webpack`打包站点手工审计`JS`寻找接口往往慢人一步,生成的`JS`文件数量异常之多并且总`JS`代码量异常庞大（多达上万行），这给我们的手工测试带来了极大的不便,利用此工具可以很好解决此问题
[Packer-FuzzerGithub地址](https://github.com/rtcatc/Packer-Fuzzer)
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587421-7c968b53-0276-40c3-ae23-7029c3069c5d.png "null")
工具会对`Webpack` 打包站点自动`API`模糊匹配与漏洞检测,扫描所有`JS`文件存在的接口并拼接访问测试未授权等漏洞。 结束后会生成报告文件参考
```php
// -t adv 代表使用高级版进行扫描
python3 PackerFuzzer.py -t adv -u http://baidu.com
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587476-9ae27b90-91f4-43d9-9033-59875468a7f2.png "null")
根据报告审查是否有未授权接口或其他漏洞产生
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587540-786f081a-3b86-4c82-b590-f53b9cd441f2.png "null")
JS接口构造
------
### 插件工具
#### \*\*熊猫头\*\*
熊猫头插件针对前端显示到的接口或者其他铭感信息进行捕获显示,复制粘贴到`BP`爆破器`GET` `POST` 两种请求方式都测试,接口未鉴权就可以发现一些信息泄露以及未授权漏洞 包括内网的IP
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587597-3e77d8d6-31e8-4ae6-8a9a-5dc621854acd.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587658-11f9c708-c312-4a06-8145-b5ac88a0c360.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587776-c82b1421-ac1a-4b9e-bb70-3135cdc5ec97.png "null")
但是插件显示是不完整的,针对熊猫头提取出的接口可以手工筛选一遍,例如`findsomething`显示接口
第一个接口应该将冒号去掉添加个数据,第二个接口也应该加入参数,一般也都是这样处理将 ,杂乱参数去除 需要值的参数就赋值
```php
/user/getInfo/:uid -----> 修改 /user/getInfo/uid
/user/getInfo?uid -----> 修改 /user/getInfo?uid=xxxx
```
#### \*\*URLFinder\*\*
[URLFinder工具地址](https://github.com/pingc0y/URLFinder)
相比熊猫头插件提取更加全面,会深入页面`JS`文件做二层深度扫描不会局限当前页面`JS`文件,会对`JS`文件中引入的`JS`文件做三次的扫描接口拼接,寻找未授权接口或未授权功能点
```php
baidu.com
app.js confif.js url.js
app.xxx.js config.xxxxxx.js url.xxxxxx.js
app.sdqew2324.js config.jkjk767.js url.vcbvcj213.js
api/user/info /api/getSharingJson /api/custommap/
baidu.com/api/user/info
baidu.com/api/getSharingJson
baidu.com/api/custommap/
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587838-96b16d50-4dcc-4946-bdad-85eac2b59fd9.png "null")
如遇到站点铭感无法利用使用扫描器, 利用`-t` 参数减少线程或者利用二开`URLFinder`规避
<https://github.com/N-Next/URLFinder-x>
```php
//扫描域名并指定输出200状态和403状态码接口 -m 安全深入抓取
URLFinder.exe -u https://baidu.com/ -s 200,403 -m 3
// 线程20
URLFinder.exe -u https://baidu.com/ -s 200,403 -m 3 -t 20
```
经典开局登录框并且插件也没有探测出有效接口,可以利用工具深度扫描页面`JS`文件
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587897-eb324864-86a6-4b7b-9edb-34ea9db52944.png "null")
通过二层探测`JS`拼接接口`size`大小判断是否有新的数据产生,如果`size`大小跟未登录状态一致那肯定是页面没有变化也不需要额外去看, `size`数字非常大那么响应出的内容更丰富
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151587960-4971dc2e-88d0-4761-9d8b-1317f23d7761.png "null")
使用`URLFinder`可以很好的发现隐藏的未授权页面 那么进入功能点了就可以到处点点点,测试是否可以未授权增删改查
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151588053-3a914851-f1fe-474f-bf40-c63826f642c5.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151588113-53ee5d86-29ae-4d9b-af3e-5c8070c576c7.png "null")
- 案例
`SRC`\*\*信息泄露\*\*
开局登录框,功能点无法利用`URLFinder`深入抓取JS拼接,找到一处下载接口,访问下载`xls`泄露网站部门人员工号+姓名,简单快速寻找未授权漏洞
```php
https://xxxxx/index.php/c/core\_user\_export/json?\_\_request\_data=
```
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-e351b049f760bb5c2f9c6115d15994758c591674.png)
\*\*文件上传接口\*\*`XSS`
同样开局登录框,熊猫头短暂测试没有效果使用此工具二次对JS深度抓取接口拼接
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151588236-97dff469-4de2-4c4f-b68f-0bdac6c970c7.png "null")
探测到隐藏文件上传功能点,成功利用收获文件上传XSS
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151588298-2cfb1f5a-ea89-459f-9ad1-73f1f975f9fb.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1739151588353-559dcb5a-8663-40ce-809c-15cb5c5aa64e.png "null")
### `Fuzz`功能接口
#### 构造功能
如果网站功能点只能允许查看 `info` 那么在查询接口功能抓包构造其他参数; 因为常见业务接口格式如果`js`文件中只有查询的接口，那么自己可以尝试一下构造添加、修改和删除接口多观察接口，推测其功能，然后根据功能去`FUZZ`，毕竟你要实现一个`web`功能，基本都要有对应的增删改查接口
```php
api/info?id=1 // 正常查询接口
api/ delete ?id=1 // 构造删除接口
/api/v1/api-docs
// 尝试替换数字
/api/ v2 /api-docs
/api/ v3 /api-docs
-----------------------------------------------------
查询（获取信息）
search list select query get find
删除（删除某个数据）
del Delete remove
编辑（更新某个信息）
Update Up edit Change
添加（增加某个信息）
add create new
// 查询接口
GET /api/模块名/list
/api/模块名/all
```
\*\*注意\*\*
增删改在实际Fuzz中尽可能不携带参数测试,这些操作涉及到业务 万一误打误撞影响到了真实用户就脱离了测试安全的意义了,携带参数也是利用小号的值
```php
// 添加
POST /api/模块名/add
// 删除接口
DELETE /api/模块名/id
GET /api/模块名/del?id=
POST /api/模块名/
// 修改接口
POST /api/模块名/modify
POST /api/模块名/
```
#### 接口信息泄露
除了构造增删改查外,泄露点更多是在查询处,查询处没有做好鉴权及易导致查询不当全站信息泄露,针对查询功能只要是查询的地方记住删除全部参数以及置空参数或者输入`%`
```Python
GET /api/demo/query=xxxxxx
GET /api/demo/ or querylist or list # 删除查询参数构造list列表
GET /api/demo/query= # 置空
GET /api/demo/query=%/\* # 模糊查询
```
假设一个接口是,如下,正常肯定是回显自己的,我们可以自行构造多余的功能,按照语义输出列表,并且前置的信息需要删除 `small`)翻译也是微小意思推断一下就是只输出小部分的,那么可以尝试这个参数删除发包测试,
```Markdown
/prod-api/system/info/small/userId ------> 个人信息
/prod-api/system/info/small/userId/list ------> 报错
/prod-api/system/info/userId/list ------> 全站用户信息
```
#### 无权限URL混淆添加资源后缀绕过
微信文章学习到的思路功能点Fuzz出来后但是无权限利用此方法进行绕过
<https://mp.weixin.qq.com/s/PoXSeckX0iwBSkIr02zYoQ>
URL混淆漏洞是指服务器和解析URL时，由于不同组件或系统的解析规则不一致，可以利用这种不一致来绕过安全控制或获取敏感信息,对路径进行编码添加后缀的方式从而进行绕过
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-eac9f10e19b26fbc9f58796230db9673a869a4c5.png)
正常接口无权限
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-a3644953a172edeacb32d77f0b76a002fb639a88.png)
对最后的接口后面添加混淆,利用字典去Fuzz 添加.json绕过,测试鉴权相关的漏洞时，可以尝试url混淆，接口多个位置fuzz 资源文件
```Markdown
/api/user ----> 未授权403
/api/user.json/css/png --- 200 ok
```
![image (1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-736ce6d621d8bc218ef3fb18b2a1073fd8d9e83d.png)
#### 白名单../绕过权限接口
社区师傅文章关于绕权限 [https://mp.weixin.qq.com/s/lDT80mNR\\\\_ubthHgArRCMLw](https://mp.weixin.qq.com/s/lDT80mNR%5C\_ubth...