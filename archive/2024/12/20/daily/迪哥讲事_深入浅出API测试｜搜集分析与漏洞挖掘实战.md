---
title: 深入浅出API测试｜搜集分析与漏洞挖掘实战
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496635&idx=1&sn=34c31d16785a1db6359cc507f1312498&chksm=e8a5f9d8dfd270ce98244fefaaff483cbbfc2b1a94710d1eb30fdc1b35c8f91dcb606f71c6f6&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-20
fetch_date: 2025-10-06T19:39:41.491933
---

# 深入浅出API测试｜搜集分析与漏洞挖掘实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6qIGureJec4PcmicjvW2pRmjbp2NmYEIlpRKmAF7fia9nhtUTgzVKmTwicfWFhJ0wSUhyFpHjyDib0SA/0?wx_fmt=jpeg)

# 深入浅出API测试｜搜集分析与漏洞挖掘实战

迪哥讲事

以下文章来源于一位不愿透露姓名的热心网友
，作者不愿透露姓名的热心网友

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7EomoAliaxuCKn0blUwibX3ANtxXaSz0vFiaynokNXbMybQ/0)

**一位不愿透露姓名的热心网友**
.

不定时更新一些渗透、逆向及个人心得随笔。

# 深入浅出API测试

标题展示

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQYse9Esr0VCM3ibsfk7c9qaERMFqZN7ZbDLvb3bs2Ww1BsU20ENMRIgw/640?wx_fmt=png&from=appmsg)

所有动态网站都由 API 组成，因此 SQL 注入等经典 Web 漏洞可以归类为 API 测试。因此测试之前要尽可能的去测试功能点，观察代理流量，发现API目录收集信息，拓展攻击面。

例如，某个功能的请求的 API 端点是 `/api/books` 这会 API 进行交互，从图书馆中检索书籍列表：

```
GET /api/books HTTP/1.1
Host: example.com
```

除了明面上已使用且可看见的功能外，可能还存在一些隐藏的或是权限不足导致的不展示的功能。因此，可能会有些`API`接口会被隐藏在`JS`中没有被激活。这时候可以使用 JS Link Finder插件辅助分析`Javascript`文件中的接口，具体可以看：[技巧 | Burp攻击面拓展与实用工具](http://mp.weixin.qq.com/s?__biz=MzkzODEzNjA3MQ==&mid=2247488184&idx=1&sn=30593b45bbc8ea3b1c719cef70ef2b1b&chksm=c28595d0f5f21cc61a83029a1198ee47cf71f42cb0d57c96cccb41c0e8c7761561b01b5c998f&scene=21#wechat_redirect)

除此之外，还可以通过`FUZZ`对接口进行猜解，例如`POST /api/user/update` 接口，可能会存在`/add`或者`/delete`功能，或是将接口命名规则丢给`GPT`让它帮忙生成相关路径。

## **发现 API开发文档并拓展攻击面**

即使 API 文档未公开提供，仍可以通过`FUZZ`或爬取的方式访问未授权的API开发文档手册，例如：

```
/api/swagger/v1
/api/swagger
/api
/swagger
/api-docs
/api.html
/swagger-ui
/swagger/codes
/api/index.html
/api/v2/api-docs
/v2/swagger.json
/swagger-ui/html
/distv2/index.html
/swagger/index.html
/sw/swagger-ui.html
/api/swagger-ui.html
/static/swagger.json
/user/swagger-ui.html
/swagger-ui/index.html
/swagger-dubbo/api-docs
/template/swagger-ui.html
/swagger/static/index.html
/dubbo-provider/distv2/index.html
/spring-security-rest/api/swagger-ui.html
/spring-security-oauth-resource/swagger-ui.html
```

`github`中关于`springboot`接口相关利用这篇文章非常详细：`https://github.com/LandGrey/SpringBootVulExploit`

API字典什么的我也没什么好东西，只推荐这`Burp`插件，自动帮忙多递归扫描，它让我捡到的API文档数量已经数不过来了：https://github.com/F6JO/RouteVulScan

### 隐藏的 HTTP 方法

`API`文档中一般规定了`API`接口地址，允许的`HTTP`方法与支持的内容类型。当然也有非一般情况，如：**文档未更新或者细节问题，导致与实际不一致。因此`API`端点可能潜在隐藏的`HTTP`方法，所以测试所有潜在方法非常重要。**

例如， `/api/tasks` 可能支持以下方法：

* `GET /api/tasks` - 检索任务列表。
* `POST /api/tasks` - 创建新任务。
* `DELETE /api/tasks/1` - 删除任务。

> 在`Intruder`中内置了名为`HTTP verbs`的HTTP方法字典

### 隐藏的内容类型

在实际生产中，因为业务互交，数据需要多系统之间透传；由于系统之间框架语言不一致，经常会出现`XML`和`JSON`数据互转。这种情况下，可能会产生处理逻辑的差异。**例如，`API` 在处理 `JSON` 数据时可能是安全的，但在处理 `XML`时容易受到注入攻击。**

在测速接口时候，要注意`Content-Type` 标头，然后相应的设置请求正文的格式，在`BApp`中Content type converter插件可以快速的在 `XML`和 `JSON`中互转换。

### 使用自动化工具分析API文档

当发现到API文档后，可以获取到大量的API接口功能信息，除了可以手动构造外，还可以通过APIKIT、OpenAPI Parser、SoapUI 这类工具对API文档进行分析与参数构造。

> 自动化测试API接口时，注意手动测试增、删接口，不要影响网站运行。

## Lab: 发现隐藏的API文档

> 通过暴露的API端点位置，想办法删除`carlos`账户；账户:`wiener:peter`

Lab: Exploiting an API endpoint using documentation | Web Security Academy (portswigger.net)

正常登陆，测试功能点。查看HTTP历史记录发现`/api/user/wiener HTTP/2` 这么一个目录请求，将`winer`修改为`carlos`发现可以正常取得信息 ，尝试只访问`/api` 路径。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQnaj0tBpiahkqtdkuddNKaTxfbn6wWX0nphRz2Q5AIUSKqibYU5kd30pg/640?wx_fmt=png&from=appmsg)

image

发现暴露了API文档信息。

根据`DELETE`格式调用删除`carlos`

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQ8VkGz18PviaF9bqnHMZs5O3SFniadFR9EL0T2Z2kNVJZtMicSsBNLaZ7Q/640?wx_fmt=png&from=appmsg)

image

---

## **Lab: 找到未使用的API接口**

> 利用隐藏的 API 端点购买**Lightweight l33t Leather Jacket**.

Lab: Finding and exploiting an unused API endpoint | Web Security Academy

走完所有功能流程，发现只有一个`API`路径

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQ1xcxqMjWjuEov5iauh20KibxxhNBKIKic8uRb6IEHy5I9a2nZfvdBWwibg/640?wx_fmt=png&from=appmsg)

image

使用内置`content discover` 扫描功能也只能发现这个路径。根据上面说的几点，拓展利用。尝试`HTTP`方法枚举，发现`PATHCH`方法会报错内容类型错误

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQ5PoHGRjL8WVsffScdXOVUl7IUbWuc9tKWndP35HTtAH3uib06xuPj2A/640?wx_fmt=png&from=appmsg)

构造内容类型与方法发送，发现提示`“price parameter missing in body”`

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQIXnkiaD5gUdkWmvbibQLVYicia3HPwWGYK9vK2eoYscmS0rbP3sqDMyyFA/640?wx_fmt=png&from=appmsg)

添加上参数，实在不知道返回的`price 0.01`是什么意思。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQItTBTkv07BicyicxouzgOr7J5fDKWfGrb5Olor799mQAyhHR6cGy7wCw/640?wx_fmt=png&from=appmsg)

image

刷新购物车发现，是设置价格的。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQDQAhvNacIAOzEJibzic0JY2DzFbuQRsXbMYNduhN6TOzZ1IE8GjiahmaQ/640?wx_fmt=png&from=appmsg)

image

那么改为0

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQuicibAPg5Up5FnFjO5IzfgPq7fyWOibISopMjgCcLC6upr6koiaPUFwiajA/640?wx_fmt=png&from=appmsg)

image

---

## Lab: **Mass Assignment 批量赋值**

Mass Assignment - OWASP Cheat Sheet Series --- 质量分配 - OWASP 备忘单系列

批量赋值（也称为自动绑定）可能会无意中创建隐藏参数。当Web框架自动将请求参数绑定到内部模型对象上的字段时（直接将用户输入参数赋值给模型实例），就会发生这种情况。因此，批量赋值可能会导致网站允许处理开发人员设置的隐藏参数。通俗来说，就像是餐馆中的隐藏菜单，虽然菜单中没有展示，但是厨师也是可以制作的。

### 识别隐藏参数

漏洞成因是由于从模型对象字段中创建参数，这种情况下，通常可以通过手动查询API返回的模型对象来发现隐藏的参数。

例如，有这么个接口：`/api/users/update` 它允许用户更新用户名称和邮箱

```
{
    "username": "wiener",
    "email": "wiener@example.com",
}
```

而恰巧有这么一个接口：`/api/users/{username}` 返回以下信息🧐

```
{
    "id": 123,
    "username": "wiener",
    "email": "wiener@example.com",
    "isAdmin": "false"
}
```

这可能表示返回的`id` 和 `isAdmin` 参数与`/api/users/update`接口更新的用户名和电子邮件参数，可能会作为隐藏参数一起绑定到内部`User`对象。

---

### 测试**批量赋值漏洞**

**SpringBoot 代码示例:**

假设有一个用于编辑用户帐户信息的表单：

```
<form>
     <input name="userid" type="text">
     <input name="password" type="text">
     <input name="email" text="text">
     <input type="submit">
</form>
```

下面是表单绑定到的`User`对象：

```
@Data
public class User {
   private String userid;
   private String password;
   private String email;
   private boolean admin;

   //Getters & Setters
}
```

下面是处理请求的\*\*`Controller`\*\*：

```
@RestController
public class UserController {

    @PostMapping("/update")
    public User updateUser(@RequestBody User user) {

        System.out.println("Updating user: " + user);
        return user;
    }
}
```

正常提交`html`会产生以下请求：

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQoouPibmfALAHRQ5AjiaZibxwl0NgNZvRlJRxcibAvACnn7LBDARNvibeyZA/640?wx_fmt=png&from=appmsg)

image

利用`Admin` 隐藏参数：

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQkF48pcf0We6hVDS1k2pddPvUjJGzFmxZBhibD4ribrDsw4PXQibxlqIDg/640?wx_fmt=png&from=appmsg)

如果请求中的 `Admin` 值绑定到`User`对象而没有进行充分的验证和清理，则可能会错误地向用户 `test`授予管理员权限。

---

**以下是Python Flask实现的效果：**

```
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
app = Flask(__name__)

users = []
class User:
    def __init__(self, username, password, email):
        self.id = len(users)
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        # 默认角色为user
        self.isAdmin = False

@app.route("/regist", methods=["POST"])
def create_user():
    data = request.get_json()

    username = data["username"]
    password = data["password"]
    email = data["email"]

    # 默认注册用户非admin
    user = User(username, password, email)

    # for user in users:
    #   if user.email == email:
    #       return jsonify({"error": "Email already exists"}), 403
    users.append(user)

    # 自动绑定所有其他参数到user对象上
    for key, value in data.items():
        if key != "password":
            setattr(user, key, value)

    return jsonify(user.__dict__)

if __name__ == "__main__":
    app.run()
```

正常注册：

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQ4G11l6ziavvSUWEB5faLmaibIXcNxiacV5pjCsxUBLS51YhAmibfAZPPpg/640?wx_fmt=png&from=appmsg)

image

利用

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISbMQNUu70qlnV5HCznypHDQBKOYL5Z5WviaC1MsSbWsyDGQZDMX1FPsWBU7IZgqtMKm9jN4S4fLb8Q/640?wx_fmt=png&from=appmsg)

image

---

### Lab：a mass assignment vulnerability

以下是`Burp`靶场：

Lab: Exploiting a mass assignment vulnerability | Web Security Academy (portswigger.net)

走一圈功能点发现只有一个接口

![](https://mmbiz.qp...