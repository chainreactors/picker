---
title: Golang gRPC 错误处理
url: https://jiajunhuang.com/articles/2022_11_04-grpc_error_handling.md.html
source: Jiajun的编程随想
date: 2022-11-05
fetch_date: 2025-10-03T21:42:30.998418
---

# Golang gRPC 错误处理

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

* [Golang gRPC 错误处理](#Golang%2bgRPC%2b%25E9%2594%2599%25E8%25AF%25AF%25E5%25A4%2584%25E7%2590%2586)
* [错误处理库](#%25E9%2594%2599%25E8%25AF%25AF%25E5%25A4%2584%25E7%2590%2586%25E5%25BA%2593)
* [gRPC 错误处理](#gRPC%2b%25E9%2594%2599%25E8%25AF%25AF%25E5%25A4%2584%25E7%2590%2586)
* [gRPC gateway 状态码](#gRPC%2bgateway%2b%25E7%258A%25B6%25E6%2580%2581%25E7%25A0%2581)
* [监控](#%25E7%259B%2591%25E6%258E%25A7)
* [总结](#%25E6%2580%25BB%25E7%25BB%2593)

# Golang gRPC 错误处理

gRPC 最常见的错误处理方式就是直接返回错误，例如 `return nil, err`，但是实际业务中，我们还有业务码需要返回，常见的方式
是在返回的结构体里定义一个错误码，但是这样写起来又很是麻烦，例如，你可能需要这样写：

```
user, err := dao.GetUserByEmail(ctx, email)
if err != nil  {
    if err == gorm.RecordNotFound {
        return &GetUserResp{Code: USER_NOT_FOUND, Msg: "user not found"}, nil
    }
    return nil, err
}
```

这里有几个问题：

1. 返回错误写起来很麻烦，因为需要每次都判断错误，然后转换成对应的错误码写在 Code, Msg 两个字段中
2. 如果直接返回 `err`，而不是 grpc 自定义的 `codes.NotFound` 等错误，无法在客户端中进行识别
3. 如果使用了 gRPC Gateway，对于返回了非 grpc 自定义错误的地方，统统会表示成500

上面几个问题，分开来都有解法，例如对于1，可以直接返回err，但是会导致问题2；对于问题2，可以使用1，但是写起来麻烦；对于
问题3，可以使用grpc内置的错误，但是表达能力非常受限，无法传达业务错误码。

因此，为了解决这一系列问题，在比较多个错误处理库之后，我们整理了一整套结合他们优点同时又适配业务需求的错误处理体系。

## 错误处理库

Python的异常体系是一个非常值得借鉴的设计。首先我们会将程序的非正常执行分为错误和异常，在Go语言中，错误是我们希望能够
进行检查和处理的，而异常是只能通过 recover 尝试进行恢复的。

我们首先将错误，分为错误的类型，和错误的实例。定义错误时，我们定义的是错误的类型，这里就携带了它所应该展示的HTTP状态码
和业务错误码。当抛出错误时，也就是实例化错误的时候，此时携带上错误的栈信息、执行信息等。

例如，定义错误：

```
ErrBadRequest       = RegisterErrorType(BaseErr, http.StatusBadRequest, ErrCodeBadRequest)             // 400
ErrUnauthorized     = RegisterErrorType(BaseErr, http.StatusUnauthorized, ErrCodeUnauthorized)         // 401
ErrPaymentRequired  = RegisterErrorType(BaseErr, http.StatusPaymentRequired, ErrCodePaymentRequired)   // 402
ErrForbidden        = RegisterErrorType(BaseErr, http.StatusForbidden, ErrCodeForbidden)               // 403
ErrNotFound         = RegisterErrorType(BaseErr, http.StatusNotFound, ErrCodeNotFound)                 // 404
ErrMethodNotAllowed = RegisterErrorType(BaseErr, http.StatusMethodNotAllowed, ErrCodeMethodNotAllowed) // 405
```

实例化错误：

```
err = validateReq(req)
if err != nil {
    return nil, errs.NewBadRequest(err.Error(), err)
}
```

检测错误类型：

```
if errs.IsError(err, ErrBadRequest) {
    //
}
```

提取错误：

```
if baseErr, ok := errs.AsBaseErr(err); ok {
    //
}
```

有了上面这一套错误库以后，我们就可以愉快的携带错误栈信息、错误类型、错误业务码、错误HTTP状态码、错误信息、导致错误发生
的元错误在整个代码体系中流转，并且还可以进行类型判断、信息提取。那么怎么和 gRPC 结合在一起呢？

## gRPC 错误处理

上面我们说过，如果直接使用 `return nil, err` 的形式，客户端无法准确识别，而如果使用 `return Resp{Code, Msg}, nil` 的形式，
写起来又很麻烦，而且 gRPC gateway 无法准确翻译成对应的 HTTP 状态码。

我们的解决方案就是，直接返回上一节描述的错误体系，例如：

```
func (s *service) CreateUser(ctx context.Context, req *pb.CreateUserReq) (*pb.CreateUserResp, error) {
    err = validateReq(req)
    if err != nil {
        return nil, errs.NewBadRequest(err.Error(), err)
    }
}
```

然后在中间件中，提取 `Resp` 并且将 `code` 和 `msg` 进行赋值：

```
func UnaryServerInterceptor() grpc.UnaryServerInterceptor {
    return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
        resp, err := handler(ctx, req)
        if err == nil {
            return resp, err
        }

        if errs.IsError(err, errs.BaseErr) {
            return resp, err
        }

        if val := reflect.ValueOf(resp); !val.IsValid() || val.IsNil() {
            tp := getRespType(ctx, info)
            if tp == nil {
                return resp, err
            }
            resp = reflect.New(tp).Interface()
        }

        if be, ok := errs.AsBaseErr(err); ok {
            grpc.SetHeader(ctx, metadata.Pairs("x-http-code", fmt.Sprintf("%d", be.HTTPCode())))
            return baseErrSetter(resp, be)
        }
    }
}
```

这样我们就可以将返回的错误自动序列化到Resp中对应的字段。

## gRPC gateway 状态码

如果上一步，我们处理完了错误之后，直接返回error，由于不是gRPC体系内的错误码，gRPC gateway会返回500，但如果我们返回nil，
gRPC gateway又会返回200，这两者都不符合预期。既然我们错误体系已经包含了HTTP状态码，是否可以直接使用呢？答案是是的，看上
面的代码中，最后我们设置了一个metadata `x-http-code`，我们可以在 gRPC gateway 中注册一个中间件，用这里传递的状态码：

```
mux := runtime.NewServeMux(
    runtime.WithForwardResponseOption(GRPCGatewayHTTPResponseModifier),
)

func GRPCGatewayHTTPResponseModifier(ctx context.Context, w http.ResponseWriter, p proto.Message) error {
    md, ok := runtime.ServerMetadataFromContext(ctx)
    if !ok {
        return nil
    }

    // set http status code
    if vals := md.HeaderMD.Get(httpStatusCodeKey); len(vals) > 0 {
        code, err := strconv.Atoi(vals[0])
        if err != nil {
            return err
        }
        // delete the headers to not expose any grpc-metadata in http response
        delete(md.HeaderMD, httpStatusCodeKey)
        delete(w.Header(), grpcHTTPStatusCodeKey)
        w.WriteHeader(code)
    }

    return nil
}
```

这样，我们在 gRPC 中返回的是 `ErrBadRequest` 的实例，最终体现在 gRPC gateway 的响应中就会是400，返回的是 `ErrForbidden`，
在 gRPC gateway 中就会体现为 403，我们的目的就成功达成了。

## 监控

同时我们还提供了一套中间件，能够结合 sentry 收集错误栈。

## 总结

这一套整套体系，最终可以达到的效果是：

* 能结合 gRPC 与 HTTP，符合对应规范，能充分支持业务需求
* 错误有分级和分类，能组成错误树
* 能识别和判断类型，能包含足够多的信息，能够自定义错误和错误类型
* 能结合 sentry 和监控系统进行错误收集和监控
* 使用简单方便，通俗易懂
* 能够保持 grpc gateway 与 grpc 中状态码、错误码一致

---

ref:

* <https://docs.python.org/3/tutorial/errors.html>
* <https://docs.python.org/3/library/exceptions.html>
* <https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/customizing_your_gateway/#controlling-http-response-status-codes>

---

##### 相关文章

* [Go的custom import path](/articles/2018_09_07-go_custom_import_path.md.html)
* [如何挖掘二级子域名？](/articles/2018_09_06-how_to_dig_subdomain.md.html)
* [Go Module 简明教程](/articles/2018_09_03-go_module.md.html)
* [写了一个Telegram Bot：自动化分享高质量内容](/articles/2018_09_02-write_a_tgbot.md.html)
* [ArchLinux 怎么降级 package ？](/articles/2018_09_01-archlinux_downgrade_package.md.html)
* [Vim打开很慢，怎么找出最慢的插件？怎么解决？](/articles/2018_09_01-vim_speed_up.md.html)
* [Web后端工程师进阶指南(2018)](/articles/2018_08_29-become_a_better_programmer.md.html)
* [How to implement fork syscall in Golang?](/articles/2018_08_28-how_does_golang_implement_fork_syscall.md.html)
* [macOS ansible 遇到 rsync: --chown=www-data: unknown option](/articles/2018_08_28-mac_rsync_unknow_option.md.html)
* [关于运营的思考-运营要怎么做？](/articles/2018_08_26-about_traffic.md.html)
* [Python中实现单例模式的n种方式和原理](/articles/2018_08_24-python_singleton.md.html)
* [Golang defer中修改返回值](/articles/2018_08_23-go_defer_named_return_values.md.html)
* [Python dataclass 源码阅读与分析](/articles/2018_08_12-python_dataclasses.md.html)
* [gRPC-gateway 源码阅读与分析](/articles/2018_08_08-grpc_gateway_source_code.md.html)
* [如何阅读源代码](/articles/2018_08_04-how_to_read_source_code.md.html)

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
* [Docker组件介绍（二）：shim, docker-i...