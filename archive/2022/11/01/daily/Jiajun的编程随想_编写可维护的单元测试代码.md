---
title: 编写可维护的单元测试代码
url: https://jiajunhuang.com/articles/2022_10_31-goconvey.md.html
source: Jiajun的编程随想
date: 2022-11-01
fetch_date: 2025-10-03T21:24:39.537597
---

# 编写可维护的单元测试代码

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [编写可维护的单元测试代码](#%25E7%25BC%2596%25E5%2586%2599%25E5%258F%25AF%25E7%25BB%25B4%25E6%258A%25A4%25E7%259A%2584%25E5%258D%2595%25E5%2585%2583%25E6%25B5%258B%25E8%25AF%2595%25E4%25BB%25A3%25E7%25A0%2581)
* [解决方案](#%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588)
* [GoConvey](#GoConvey)
* [testify assert suite](#testify%2bassert%2bsuite)
* [总结](#%25E6%2580%25BB%25E7%25BB%2593)

# 编写可维护的单元测试代码

这篇文章主要讲讲单元测试代码的可维护性。不知道你是否写过面条式的单元测试，也就是这样的结构。坦白讲，我写过不少：

```
func TestFoo(t *testing.T) {
    // test get
    resp, err := GET(blabalbal)
    assert.Nil(err)
    ...

    // test post
    resp, err = POST(blabalbal)
    assert.Nil(err)
    ...

    // test update
    resp, err = PUT(blabalbal)
    assert.Nil(err)
    ...
}
```

绝大部分童鞋这样写的时候，都是为了方便：方便初始化变量，方便复用。但是一旦当用例代码行数过长，而单测恰好又执行失败，
需要找到具体原因时，就会比较困难，调试时，需要花很多时间定位。

## 解决方案

Go社区的测试框架，已经提供了两套比较成熟的解决方案：

* [GoConvey](https://github.com/smartystreets/goconvey)
* [Go testify assert suite](https://pkg.go.dev/github.com/stretchr/testify/suite)

我们分别看看这两者。

### GoConvey

```
package package_name

import (
    "testing"
    . "github.com/smartystreets/goconvey/convey"
)

func TestSpec(t *testing.T) {
    // Only pass t into top-level Convey calls
    Convey("Given some integer with a starting value", t, func() {
        x := 1

        Convey("When the integer is incremented", func() {
            x++

            Convey("The value should be greater by one", func() {
                So(x, ShouldEqual, 2)
            })
        })

        Convey("When the integer is incremented again", func() {
            x++

            Convey("The value should be greater by one", func() {
                So(x, ShouldEqual, 2)
            })
        })
    })
}
```

如上代码，是可以通过的。GoConvey比较特殊的一点，是它是树状执行的，而不是从上到下执行的。也就是说，它是深度优先遍历执行，
且不共享变量的，在 `When the integer is incremented` 和 `When the integer is incremented again` 执行时，x的值都是上层
赋值的1。

以上代码执行顺序为：

* `Given some integer...` -> `When the integer is incremented` -> `The value should be....`
* `Given some integer...` -> `When the integer is incremented again` -> `The value should be....`

### testify assert suite

```
// Basic imports
import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/suite"
)

// Define the suite, and absorb the built-in basic suite
// functionality from testify - including a T() method which
// returns the current testing context
type ExampleTestSuite struct {
    suite.Suite
    VariableThatShouldStartAtFive int
}

// Make sure that VariableThatShouldStartAtFive is set to five
// before each test
func (suite *ExampleTestSuite) SetupTest() {
    suite.VariableThatShouldStartAtFive = 5
}

// All methods that begin with "Test" are run as tests within a
// suite.
func (suite *ExampleTestSuite) TestExample() {
    assert.Equal(suite.T(), 5, suite.VariableThatShouldStartAtFive)
    suite.Equal(5, suite.VariableThatShouldStartAtFive)
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestExampleTestSuite(t *testing.T) {
    suite.Run(t, new(ExampleTestSuite))
}
```

suite 主要通过如下几个hook函数：

```
// SetupAllSuite has a SetupSuite method, which will run before the
// tests in the suite are run.
// 执行测试之前先执行这个
type SetupAllSuite interface {
    SetupSuite()
}

// SetupTestSuite has a SetupTest method, which will run before each
// test in the suite.
// 执行每个用例之前都会执行这个
type SetupTestSuite interface {
    SetupTest()
}

// TearDownAllSuite has a TearDownSuite method, which will run after
// all the tests in the suite have been run.
// 执行整个测试之后，执行这个
type TearDownAllSuite interface {
    TearDownSuite()
}

// TearDownTestSuite has a TearDownTest method, which will run after
// each test in the suite.
// 执行每个用例之后都会执行这个
type TearDownTestSuite interface {
    TearDownTest()
}
```

这样，就可以把共享变量以及销毁等分别放置到对应函数进行处理，从而将一系列函数整合成一套一套的测试。

## 总结

我个人更喜欢用 `convey`，只要理解它的树状执行模式，就会发现这样整体测试代码可以少写很多，结构也很清晰。通过树状组织，
可以将同一主题的测试用例，放在同一个 `TestXXX` 函数中，然后逐层根据条件细化，分别放在各个 `Convey` 函数中，最后通过
`So` 传入断言，进行校验。

这篇文章没有讲具体技术的东西，主要是简单介绍了两个单元测试框架，但最重要的，是想要说明单元测试代码，同样是需要受到
重视的代码，也需要好好地组织代码结构和用例，单元测试是用来确保代码本身执行的，通常写好以后，变更频率都不会太高，如果
使用面条式组织方式，在时间久了以后，调试起来非常困难。

借助 convey 这种工具，就可以将测试用例代码细分到不同函数，且互不干扰，非常有利于维护性。

---

##### 相关文章

* [Go语言MySQL时区问题](/articles/2019_11_14-golang_mysql_timezone.md.html)
* [我的技术栈选型](/articles/2019_11_13-tech_stack.md.html)
* [为什么我要用Linux作为桌面？](/articles/2019_11_11-why_linux_as_desktop.md.html)
* [disqus获取评论时忽略query string](/articles/2019_11_08-disqus_thread_identifier.md.html)
* [MySQL性能优化指南](/articles/2019_11_06-mysql.md.html)
* [网络编程所需要熟悉的那些函数](/articles/2019_11_01-network_programming.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [这些年，我们错过的n个亿](/articles/2019_10_25-oh_my_money.md.html)
* [给Linux用户的FreeBSD快速指南](/articles/2019_10_19-freebsd_for_linux_users.md.html)
* [旧电脑也不能闲着：家用备份方案](/articles/2019_10_18-build_your_own_nas.md.html)
* [将SQLite的数据迁移到MySQL](/articles/2019_10_15-grafana_moved_to_mysql.md.html)
* [Linux托管Windows虚拟机最佳实践](/articles/2019_10_08-linux_windows.md.html)
* [为什么gRPC难以推广](/articles/2019_09_29-why_grpc_is_not_popular.md.html)
* [关于ORM的思考](/articles/2019_09_26-orm.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。