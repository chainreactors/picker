---
title: 浅学Go下的ssti
url: https://www.secpulse.com/archives/192052.html
source: 安全脉搏
date: 2022-11-25
fetch_date: 2025-10-03T23:43:04.563657
---

# 浅学Go下的ssti

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 浅学Go下的ssti

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-24

10,577

# 前言

作为强类型的静态语言，golang的安全属性从编译过程就能够避免大多数安全问题，一般来说也唯有依赖库和开发者自己所编写的操作漏洞，才有可能形成漏洞利用点，在本文，主要学习探讨一下golang的一些ssti模板注入问题

# GO模板引擎

Go 提供了两个模板包。一个是 `text/template`，另一个是`html/template`。text/template对 XSS 或任何类型的 HTML 编码都没有保护，因此该模板并不适合构建 Web 应用程序，而html/template与text/template基本相同，但增加了HTML编码等安全保护，更加适用于构建web应用程序

## template简介

template之所以称作为模板的原因就是其由静态内容和动态内容所组成，可以根据动态内容的变化而生成不同的内容信息交由客户端，以下即一个简单例子

```
模板内容 Hello, {{.Name}} Welcome to go web programming…
期待输出 Hello, liumiaocn Welcome to go web programming…
```

而作为go所提供的模板包，text/template和html/template的主要区别就在于对于特殊字符的转义与转义函数的不同，但其原理基本一致，均是动静态内容结合，以下是两种模板的简单演示

### text/template

```
package main

import (
    "net/http"
    "text/template"
)

type User struct {
    ID       int
    Name  string
    Email    string
    Password string
}

func StringTpl2Exam(w http.ResponseWriter, r *http.Request) {
    user := &User{1,"John", "test@example.com", "test123"}
    r.ParseForm()
    tpl := `<h1>Hi, {{ .Name }}</h1><br>Your Email is {{ .Email }}`
    data := map[string]string{
        "Name":  user.Name,
        "Email": user.Email,
    }
    html := template.Must(template.New("login").Parse(tpl))
    html.Execute(w, data)
}

func main() {
    server := http.Server{
        Addr: "127.0.0.1:8888",
    }
    http.HandleFunc("/string", StringTpl2Exam)
    server.ListenAndServe()
}
```

struct是定义了的一个结构体，在go中，我们是通过结构体来类比一个对象，因此他的字段就是一个对象的属性，在该实例中，我们所期待的输出内容为下

```
模板内容 <h1>Hi, {{ .Name }}</h1><br>Your Email is {{ .Email }}
期待输出 <h1>Hi, John</h1><br>Your Email is test@example.com
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192052-1669274184.png "null")

可以看得出来，当传入参数可控时，就会经过动态内容生成不同的内容，而我们又可以知道，go模板是提供字符串打印功能的，我们就有机会实现xss

```
package main

import (
    "net/http"
    "text/template"
)

type User struct {
    ID       int
    Name  string
    Email    string
    Password string
}

func StringTpl2Exam(w http.ResponseWriter, r *http.Request) {
    user := &User{1,"John", "test@example.com", "test123"}
    r.ParseForm()
    tpl := `<h1>Hi, {{"<script>alert(/xss/)</script>"}}</h1><br>Your Email is {{ .Email }}`
    data := map[string]string{
        "Name":  user.Name,
        "Email": user.Email,
    }
    html := template.Must(template.New("login").Parse(tpl))
    html.Execute(w, data)
}

func main() {
    server := http.Server{
        Addr: "127.0.0.1:8888",
    }
    http.HandleFunc("/string", StringTpl2Exam)
    server.ListenAndServe()
}
```

```
模板内容 <h1>Hi, {{"<script>alert(/xss/)</script>"}}</h1><br>Your Email is {{ .Email }}
期待输出 <h1>Hi, {{"<script>alert(/xss/)</script>"}}</h1><br>Your Email is test@example.com
实际输出 弹出/xss/
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192052-1669274185.png "null")

这里就是text/template和html/template的最大不同了

### html/template

同样的例子，但是我们把导入的模板包变成html/template

```
package main

import (
    "net/http"
    "html/template"
)

type User struct {
    ID       int
    Name  string
    Email    string
    Password string
}

func StringTpl2Exam(w http.ResponseWriter, r *http.Request) {
    user := &User{1,"John", "test@example.com", "test123"}
    r.ParseForm()
    tpl := `<h1>Hi, {{"<script>alert(/xss/)</script>"}}</h1><br>Your Email is {{ .Email }}`
    data := map[string]string{
        "Name":  user.Name,
        "Email": user.Email,
    }
    html := template.Must(template.New("login").Parse(tpl))
    html.Execute(w, data)
}

func main() {
    server := http.Server{
        Addr: "127.0.0.1:8888",
    }
    http.HandleFunc("/string", StringTpl2Exam)
    server.ListenAndServe()
}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192052-16692741851.png "null")

可以看到，xss语句已经被转义实体化了，因此对于html/template来说，传入的script和js都会被转义，很好地防范了xss，但text/template也提供了内置函数html来转义特殊字符，除此之外还有js，也存在`template.HTMLEscapeString`等转义函数

而通过html/template包等，go提供了诸如Parse/ParseFiles/Execute等方法可以从字符串或者文件加载模板然后注入数据形成最终要显示的结果

`html/template` 包会做一些编码来帮助防止代码注入，而且这种编码方式是上下文相关的，这意味着它可以发生在 HTML、CSS、JavaScript 甚至 URL 中，模板库将确定如何正确编码文本

## template常用基本语法

在`{{}}`内的操作称之为pipeline

```
{{.}} 表示当前对象，如user对象

{{.FieldName}} 表示对象的某个字段

{{range …}}{{end}} go中for…range语法类似，循环

{{with …}}{{end}} 当前对象的值，上下文

{{if …}}{{else}}{{end}} go中的if-else语法类似，条件选择

{{xxx | xxx}} 左边的输出作为右边的输入

{{template "navbar"}} 引入子模版
```

# 漏洞演示

在go中检测 SSTI 并不像发送 {{7\*7}} 并在源代码中检查 49 那么简单，我们需要浏览文档以查找仅 Go 原生模板中的行为，最常见的就是占位符`.`

在template中，点"."代表当前作用域的当前对象，它类似于java/c++的this关键字，类似于perl/python的self

```
package main

import (
    "net/http"
    "text/template"
)

type User struct {
    ID       int
    Name  string
    Email    string
    Password string
}

func StringTpl2Exam(w http.ResponseWriter, r *http.Request) {
    user := &User{1,"John", "test@example.com", "test123"}
    r.ParseForm()
    tpl := `<h1>Hi, {{ .Name }}</h1><br>Your Email is {{ . }}`
    data := map[string]string{
        "Name":  user.Name,
        "Email": user.Email,
    }
    html := template.Must(template.New("login").Parse(tpl))
    html.Execute(w, data)
}

func main() {
    server := http.Server{
        Addr: "127.0.0.1:8888",
    }
    http.HandleFunc("/string", StringTpl2Exam)
    server.ListenAndServe()
}
```

输出为

```
模板内容 <h1>Hi, {{ .Name }}</h1><br>Your Email is {{ . }}
期待输出 <h1>Hi, John</h1><br>Your Email is map[Email:test@example.com Name:John]
```

可以看到结构体内的都会被打印出来，我们也常常利用这个检测是否存在SSTI

接下来就以几道题目来验证一下

## [LineCTF2022]gotm

```
package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "os"
    "text/template"

    "github.com/golang-jw...