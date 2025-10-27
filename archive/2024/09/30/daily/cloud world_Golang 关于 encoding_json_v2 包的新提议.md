---
title: Golang 关于 encoding/json/v2 包的新提议
url: https://cloudsjhan.github.io/2024/09/29/Golang-%E5%85%B3%E4%BA%8E-encoding-json-v2-%E5%8C%85%E7%9A%84%E6%96%B0%E6%8F%90%E8%AE%AE/
source: cloud world
date: 2024-09-30
fetch_date: 2025-10-06T18:24:48.431843
---

# Golang 关于 encoding/json/v2 包的新提议

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Golang 关于 encoding/json/v2 包的新提议

posted

2024-09-29

|

in

[Golang](/categories/Golang/)

|

visitors:

|

|

wordcount:

1,027
|

min2read ≈

5

![](https://)

### 背景介绍

JSON 是一种轻量级数据交换格式，自十年前 Go 的编码/json 软件包问世以来，开发人员一直对其灵活的特性青睐有加。开发人员可以通过 struct 标记自定义 struct 字段的 JSON 表示法，也允许 Go 类型自定义自己的 JSON 表示法。然而，随着 Go 语言和 JSON 标准的发展，一些功能缺陷和性能限制也逐渐暴露出来。

* 功能缺失：例如，无法为 time.Time 类型指定自定义格式，无法在序列化过程中省略特定的 Go 值等。
* API 的缺陷：例如，没有简单的方法从 io.Reader.Reader 中正确反序列化 JSON。
* 性能限制：标准 json 软件包的性能并不令人满意，尤其是在处理大量数据时。

* 行为缺陷：例如，JSON 语法的错误处理不够严格，反序列化不区分大小写等。

与 math/v2 一样，Go 官方也提出了 [encoding/json/v2](https://github.com/golang/go/discussions/63397 "json/v2 disscussion") 来解决上述问题。本文的主要目的是分析在 encoding/json 中有关空值的一些问题，以及在 encoding/json/v2 中如何解决这些问题。本文不涉及 encoding/json/v2 中的其他修改。

### omitempty 行为

在 `encoding/json` 包中，对 omitempty 有如下描述：

> omitemptyoption 指定，如果字段的值为空（定义为 false、0、nil 指针、nil 接口值以及任何空数组、片、映射或字符串），则编码中应省略该字段。

这种预定义的 nil value 的判断逻辑并不能满足所有实际场景的需要。让我们来看一个例子：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` type Post struct {       Id         int64           `json:"id,omitempty"`       CreateTime time.Time       `json:"create_time,omitempty"`       TagList    []Tag           `json:"tag_list,omitempty"`       Name       string          `json:"name,omitempty"`       Score      float64         `json:"score,omitempty"`       Category   Category        `json:"category,omitempty"`       LikePost   map[string]Post `json:"like,omitempty"`   }   type Tag struct {       ID   string `json:"id"`       Name string `json:"name"`   }   type Category struct {       ID   float64 `json:"id"`       Name string  `json:"name"`   }      func main() {       b, _ := json.Marshal(new(Post))       fmt.Println(string(b))   } ``` |

输出结果为:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` {"create_time":"0001-01-01T00:00:00Z","category":{"id":0,"name":""}} ``` |

虽然在 Post 的每个字段中都添加了 omitempty，但结果并不尽如人意。

* omitempty 不能处理空结构，如 Post.Category
* omitempty 处理 time.Time 的方式不是我们理解的 UTC =0，即 1970-01-01 00:00:00，而是 0001-01-01T00:00:00Z。

### omitzero Tag

在 [encoding/json/v2](https://github.com/golang/go/discussions/63397 "json/v2/disscusstion") 中，将添加一个新标签 omitzero，它增加了两个功能来解决上述两个问题。(此功能仍在开发中，开发者可以通过 `go-json-experiment/json` 提前体验新功能）

* 更好地处理时间类型
* 支持自定义 IsZero 函数，例如以下代码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` | ``` package main      import (       "encoding/json"       "fmt"    v2_json "github.com/go-json-experiment/json"       "math"    "time")      type Post struct {       Id         int64           `json:"id,omitempty,omitzero"`       CreateTime time.Time       `json:"create_time,omitempty,omitzero"`       TagList    []Tag           `json:"tag_list,omitempty"`       Name       string          `json:"name,omitempty"`       Score      ScoreType       `json:"score,omitempty,omitzero"`       Category   Category        `json:"category,omitempty,omitzero"`       LikePost   map[string]Post `json:"like,omitempty"`   }   type ScoreType float64      func (s ScoreType) IsZero() bool {       return s < math.MinInt64   }      type Tag struct {       ID   string `json:"id"`       Name string `json:"name"`   }   type Category struct {       ID   float64 `json:"id"`       Name string  `json:"name"`   }      func main() {       v1String, _ := json.Marshal(new(Post))       fmt.Println(string(v1String))       v2String, _ := v2_json.Marshal(new(Post))       fmt.Println(string(v2String))   } ``` |

与 encoding/json 相比，encoding/json/v2 解决了上述问题。

输出结果为：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` {"create_time":"0001-01-01T00:00:00Z","category":{"id":0,"name":""}} {"score":0} ``` |

### 结论

通过引入 omitzero 标记，Go 在解决 JSON 编码中 nil value 处理的痛点方面迈出了非常关键的一步。这一解决方案不仅满足了开发人员对更灵活的 nil 值定义的需求，还保持了与现有系统的兼容性。omitzero 的登陆时间尚未确定，最早也要等到 Go 1.24 版本。

此外，`encoding/xml` 和其他软件包也将遵循 json 软件包，并添加 omitzero 标记。encoding/json/v2 还包括其他方面的更新，例如性能。感兴趣的 Gophers 可以提前了解这些变化，本博客也将继续关注这一提议。

---

-------------The End-------------

Title:[Golang 关于 encoding/json/v2 包的新提议](/2024/09/29/Golang-%E5%85%B3%E4%BA%8E-encoding-json-v2-%E5%8C%85%E7%9A%84%E6%96%B0%E6%8F%90%E8%AE%AE/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年09月29日 - 21:09

Last Update:2024年09月29日 - 21:09

Original Link:[https://cloudsjhan.github.io/2024/09/29/Golang-关于-encoding-json-v2-包的新提议/](/2024/09/29/Golang-%E5%85%B3%E4%BA%8E-encoding-json-v2-%E5%8C%85%E7%9A%84%E6%96%B0%E6%8F%90%E8%AE%AE/ "Golang 关于 encoding/json/v2 包的新提议")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Go](/tags/Go/)

(>给这篇博客打个分吧<)

[构建由大型语言模型（LLM）驱动的 Go 应用程序](/2024/09/14/%E6%9E%84%E5%BB%BA%E7%94%B1%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%EF%BC%88LLM%EF%BC%89%E9%A9%B1%E5%8A%A8%E7%9A%84-Go-%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F/ "构建由大型语言模型（LLM）驱动的 Go 应用程序")

[Varint 及其在 Golang 中的应用](/2024/09/29/Varint-%E5%8F%8A%E5%85%B6%E5%9C%A8-Golang-%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8/ "Varint 及其在 Golang 中的应用")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

cloud sjhan

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hantmac "GitHub")

E-Mail

Links

* [CSDN](https://blog.csdn.net/u012421976 "CSDN")
* [w3school](http://www.w3school.com.cn/ "w3school")
* [快搜](http://search.chongbuluo.com/ "快搜")

1. [1. 背景介绍](#背景介绍)
2. [2. omitempty 行为](#omitempty-行为)
3. [3. omitzero Tag](#omitzero-Tag)
4. [4. 结论](#结论)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;