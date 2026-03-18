---
title: API安全漏洞挖掘指南：40种真实世界漏洞模型
url: https://mp.weixin.qq.com/s/DDb5XYatRTEik_7D-lTIoA
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:18:22.854796
---

# API安全漏洞挖掘指南：40种真实世界漏洞模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DdVXYMZZ2ziawRNSB7C7at3W4w8r9jrPJzWOgNyF1jyFiaE1j8YmkJyIHryFkHf7IDdsU2wBwgpzZuuhgWaocAZ7gBwO4codubczZZevhv4IY/0?wx_fmt=jpeg)

# API安全漏洞挖掘指南：40种真实世界漏洞模型

原创

地图大师挖漏洞
地图大师挖漏洞

地图大师的漏洞追踪指南

![]()

在小说阅读器中沉浸阅读

大家好我是地图大师，好久没给大家写技术文章了。最近作为碳基生物在现实世界中的事太忙了各种事赶着事，留给自己做技术研究的时间越来越压缩了。之前和很多师傅聊天的时候发现很多师傅都对API安全很感兴趣。大家觉得通过我消化过再讲出来的更容易让人理解。那么今天正好有空，我从我的角度给大家讲讲我理解的API安全及配套的案例，希望能让不了解API安全的师傅产生一个入门。

## 0x01什么是API？

##

        我不太喜欢引用网上那些官方的描述，大家如果阅读到这篇文章不知道什么是API的话可以用AI查询一下。这里我就以我的理解跟大家聊了。API 本质就是“程序之间的接口”。比如我们做了一个同X交友APP我们需要显示当地的温度（天气服务）、约会地点的路线（地图服务）、餐厅的评价（大众点评的接口服务）。这些东西如果我们不想从0开发的话，我们就得用现成的。那么API服务就应用而生了，有的API负责给你提供地图、有的API负责给你提供天气。

```
举个例子：我：“今天成都的气温是多少？”天气API接口：“今天的气温为23度”
我：“我要到鸿琳酒吧怎么走？”地图API接口：“下个路口左转520米”
```

```

```

        说白了API就是专门帮我们做某一样事或者某几件事的接口。基本上我们小程序、web网站、app中都有无数的API接口。可以说我们现在的数字社会是由无数的API组成的。API他不管是19XX年的web1.0或者到如今的WEB4.0（AI网络入口）都是不可或缺的，比如最近流行的openclaw（龙虾）也是调用这各种各样的API接口。

可以说我们整个网络社会中API都是不可获取的一部分。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DdVXYMZZ2zjatuUMhBiazOlicaZodj3Phmhhvz4gYEbhOGmYxUXm7d5pxwAse3hoHEUGcbLqpRGmK7CxUrOjmvDI76bccd04jZGjexbURSNY8/640?wx_fmt=jpeg&from=appmsg)

##

---

##

## 0x02API安全都有些什么

##

```

```

```
```
```
![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zgO9qYID9SptztXxlz16Bx65OvVF1O3E1vWnN3jVaQL2oCFL2ibFfgH2VV0fjJOFtUY0CJDVdT2ttqBjSgIEVSgUzSpRDyI9T14/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2zjGLjtKxnjFX2MdxxPQ4lHibXvC4w4eO7cUlEQ19YLuqUurEl5bcHsUmB3gR8XicvWuXOos0k6qaWyvibtJ7Siab0XE3TVJunA92Zk/640?wx_fmt=png&from=appmsg)
```
```
```

阅读完不知道大家是什么感觉，是不是有种都是中文汉字但是就是看不懂的感觉。哈哈。大师在这里以大师的理解给大家结合一些我们都知道的漏洞类型来给大家做一个详细解释。

### API1：失效的对象级别授权（用户层面越权漏洞）

### 简单理解

接口通过 **对象ID**来访问数据，但没有验证用户是否有权限访问这个对象。

攻击者只要修改 ID，就能查看或修改别人的数据。

```
接口：GET /api/user/1001返回：{ "username":"returnwrong", "phone":"13800000000"}
```

```

```

攻击者请求：

```
GET /api/user/1002
```

```

```

如果返回了 **另一个用户的数据**，就是越权漏洞,说白了就是我们最常见的越权。

### API2：身份认证失效

### 简单理解

系统的 **登录、Token 或 Session 机制存在问题**。

攻击者可以：

```
伪造身份冒充用户劫持账户
```

```

```

---

Token 可预测：

```
token=userid+timestamp
```

```

```

攻击者可以猜测：

```
token=1001_171000000
```

```

```

从而登录别人账号。

---

常见问题：

```
Token不过期Token可猜测JWT签名弱验证码无限尝试
```

```

```

---

### API3：过度的数据暴露（就是他给的比你要的多多了）

### 简单理解

接口返回的数据 **比实际需要的多**。

开发者把整个对象返回给前端，而不是只返回需要的字段。

---

```
接口：GET /api/user/profile返回：{ "username":"tom", "email":"tom@example.com", "password_hash":"xxxxx", "internal_id":"98321", "role":"admin"}
```

```

```

虽然前端只显示用户名，但 **攻击者仍然能看到所有字段**。

---

常见暴露：

```
密码hash内部ID权限字段手机号身份证
```

```

```

---

### API4：缺少资源限制和速率限制

### 简单理解

接口没有限制 **请求频率或资源使用量**。这个可以参考地图大师2022年发布的文章地图API漏洞怎么挖

攻击者可以：

```
暴力破解刷接口制造DoS
```

```

```

---

登录接口：

```
POST /api/login
```

```

```

如果没有限制请求次数,攻击者可以：

```
每秒尝试1000个密码进行暴力破解。
```

---

常见问题：

```
短信验证码无限发送密码无限尝试接口批量调用
```

```

```

---

### API5：功能级授权失效

普通用户可以调用 **管理员接口**。

---

普通用户接口：

```
GET /api/user/info
```

```

```

管理员接口：

```
GET /api/admin/user/list
```

```

```

如果普通用户访问：

```
GET /api/admin/user/list
```

```

```

系统仍然返回数据，就是漏洞。

---

常见于：

```
后台管理接口订单管理接口用户管理接口
```

```

```

---

### API6：批量赋值漏洞（我觉得这个名字容易引起很大的分歧，我觉得成为模糊测试参数更好点CAA永远的神）

接口允许用户 **修改不该修改的字段**。

攻击者可以直接在请求中加入隐藏字段。

---

正常请求：

```
POST /api/user/update{ "nickname":"tom"}
```

```

```

攻击者发送：

```
{ "nickname":"tom", "role":"admin"}
```

```

```

如果服务器直接更新数据库，就会产生漏洞。

---

常见被修改字段：

```
rolebalancevip_levelis_admin
```

```

```

---

### API7：安全配置错误（例如开启了不安全的HTTP方法）

### 简单理解

服务器或 API 配置不安全。

---

### 示例

服务器允许：

```
OPTIONSPUTDELETETRACE
```

```

```

这些方法可能被利用。

---

### 真实场景

常见问题：

```
Swagger接口公开调试接口未关闭CORS允许任意来源错误信息暴露堆栈
```

```

```

---

### API8：注入漏洞（万物离不开注入漏洞）

### 简单理解

用户输入的数据被当作 **代码或命令执行**。

---

### 示例

SQL注入：

```
GET /api/user?id=1 OR 1=1
```

```

```

如果数据库执行：

```
SELECT * FROM users WHERE id=1 OR 1=1
```

```
这个大家应该没人不知道吧
```

攻击者就能获取所有数据。

---

### 常见注入类型

```
SQL注入NoSQL注入命令注入LDAP注入
```

```

```

---

### API9：资产管理不当（这个类型和挖洞无关，主要还是安全管理方面的）

### 简单理解

公司 **不知道自己有多少API**。

旧接口、测试接口、调试接口仍然对外开放。

---

### 示例

企业上线：

```
/api/v1/api/v2/api/test/api/debug
```

```

```

攻击者可能发现：

```
/api/v1/admin/delete_user
```

```

```

这是旧版本接口。

---

### 真实场景

常见问题：

```
旧版本API未下线测试接口暴露内部接口外网可访问
```

```

```

---

### API10：日志和监控不足（这个类型和挖洞无关，主要还是安全管理方面的）

### 简单理解

系统没有记录安全日志。

攻击者入侵后 **很难被发现**。

---

### 示例

攻击者持续请求：

```
/api/user/1/api/user/2/api/user/3
```

```

```

爬取所有用户数据。

如果系统没有监控：

```
不会触发报警
```

企业可能 **几个月后才发现数据泄露**。

通过上面的“说人话”解释，大家可能恍然大悟。这不就是我平常挖的漏洞类型吗，owasp网站怎么写的这么复杂，哈哈。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DdVXYMZZ2ziaiagB0ygzxIBBWTDrricmQYTYvbFLicibNTKQqgkyRV4zpl9xf2vGDtebvzITKUC7bBBSSUjGQ2HmJv982raWicyfXszuxg8IFGuOU/640?wx_fmt=jpeg&from=appmsg)

## 0x03A地图大师总结的40种API安全漏洞

##

![](https://mmbiz.qpic.cn/mmbiz_jpg/DdVXYMZZ2zhBvxaicAPDdWep6RKv8RBdbxycPEq9lqTKbOPn4uuZLxSS2cOzwP9lblAK6iaqeV6xTzJf7R3vBDflyxrUFJobVFUQG2BXcuFibA/640?wx_fmt=jpeg&from=appmsg)

我按照我自己历史中挖SRC和渗透测试的经验，总结了大概六大类40种API相关的安全漏洞。肯定不能覆盖所有的API漏洞但是可以给大家做成一个CheckList挖洞过程中没有灵感的话可以翻出来看看。

我总结API漏洞大概分为六种：

```
1、认证类漏洞2、授权类漏洞3、数据暴露类漏洞4、参数逻辑漏洞5、资源滥用漏洞6、攻击面漏洞
```

```

```

### 一、认证类漏洞

这类漏洞主要影响 **用户身份验证**。

### 1 Token 可预测（这个之前带大家打过类似靶场）

例如：

```
token = userid + timestamp
```

```

```

攻击者可以猜测 Token。

---

### 2 Token 永不过期（这个渗透中比较常见，但是得配合其他漏洞拿到token）

Token 长期有效：

```
Authorization: Bearer returnwrong i love you
```

```

```

即使用户退出登录仍然可以使用。

---

### 3 Token 未绑定设备

Token 可以在不同设备上使用。

例如：

```
手机登录获取tokenPC继续使用token
```

```

```

---

### 4 Token 泄露（HaE永远的神，该漏洞可以配合上面的token永不过期）

Token 出现在：

```
URL日志Referer
```

```

```

攻击者可以直接复用。

---

### 5 验证码缺失或弱验证（比如没有图形验证码，或者验证码失效，这个讲过太多次了）

例如：

```
登录接口没有验证码验证码可以无限尝试
```

```

```

---

### 6 OAuth 配置错误

例如：

```
redirect_uri 未校验
```

```

```

可能导致账户接管。

---

### 7 API Key 暴露（地图API最明显的案例）

例如：

```
JS 文件中包含 API Key
```

```

```

攻击者直接调用接口。

---

# 二、授权类漏洞

这是 **API漏洞最多的一类**。

---

### 8 越权（用户身份越权=对象级越权）

接口：

```
GET /api/order/1001
```

```

```

修改：

```
GET /api/order/1002
```

```

```

读取别人订单。

---

### 9 水平越权

用户访问其他用户资源。

例如：

```
GET /api/user/profile?id=1002
```

```

```

---

### 10 垂直越权

普通用户调用管理员接口。

例如：

```
GET /api/admin/users
```

```

```

---

### 11 功能级越权（其实大家理解成垂直越权就行）

调用不属于当前角色的功能。

例如：

```
DELETE /api/admin/delete_user
```

```

```

---

### 12 接口隐藏但未鉴权（未授权，findsomething+hae+caa）

接口存在：

```
/api/internal/export
```

```

```

但未做权限控制。

---

### 13 多角色权限错误（渗透的时候经常有权限瞎设置的各种账号）

例如：

```
管理员客服普通用户
```

```

```

角色判断逻辑错误。

---

#

# 三、数据暴露类漏洞

接口返回 **过多敏感数据**。

---

### 14 过度数据暴露（前端只显示昵称，但是返回的json里带了很多敏感信息）

返回对象所有字段：

```
password_hashinternal_idreturnwrong
```

```

```

---

### 15 敏感字段泄露（从api 监测设备里看到的漏洞分类）

例如：

```
地图大师的手机号地图大师的身份证邮箱
```

```

```

---

### 16 调试信息暴露（从api 监测设备里看到的漏洞分类）

接口返回：

```
SQL语句系统路径
```

```

```

---

### 17 API文档暴露（swagger无需多说）

例如：

```
/swagger/openapi.json
```

```

```

攻击者可查看全部接口。

---

### 18 内部接口暴露（还记得harbor吗？）

例如：

```
/api/internal/debug
```

```

```

---

# 四、参数逻辑漏洞

这类漏洞 **SRC非常常见，说白了逻辑漏洞就是玩接口的艺术**。

---

### 19 参数篡改（下面的案例是支付漏洞）

例如：

```
price=1
```

```

```

改成：

```
price=0.01
```

```

```

---

### 20 数值边界漏洞（负数购买）

例如：

```
amount=-1
```

```

```

导致逻辑错误。

---

### 21 状态绕过（步骤跳过漏洞）

例如订单流程：

```
create → pay → deliver
```

```

```

攻击者直接调用：

```
deliver
```

```

```

---

### 22 重放攻击（并发的小弟）

重复提交请求：

```
POST /api/pay
```

```

```

多次执行。

---

### 23 批量接口漏洞

接口支持：

原始数据包只有1001但是通过加其他id看到了其他用户数据

```
{ "ids":[1001,1002,1003]}
```

```

```

可能读取大量数据。

---

### 24 批量赋值漏洞（当做fuzz参数的漏洞即可）

请求：

```
{ "nickname":"tom"}
```

```

```

攻击者加入：

```
role=admin
```

```

```

---

### 25 JSON结构绕过（此处举例一个越权）

例如：

```
{ "user": {"id":1001}}
```

```

```

攻击者构造：

```
"user.id":1002
```

```

```

---

# 五、资源滥用漏洞

接口没有限制请求。

---

### 26 暴力破解

例如：

```
POST /api/login
```

```

```

无限尝试密码。

---

### 27 验证码刷接口（轰炸）

例如：

```
POST /api/send_sms
```

```

```

无限发送。

---

### 28 批量注册（任意用户注册）

例如：

```
POST /api/register
```

```

```

无限注册账号。

---

### 29 数据批量爬取（薅羊毛）

例如：

```
/api/users?page=1
```

```
...