---
title: goproxy v1.9.1
url: https://kitploit.com/en/posts/github-elazarl-goproxy-v191
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:52.833629
---

# goproxy v1.9.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50732/c93f82447e84642519904d8b1e1685a41c13c66d6a77ee66857847da171578c2-display-v1.webp)

New releaseSep 6, 2026

# goproxy v1.9.1

A customizable HTTP/HTTPS proxy library for Go supporting regular forwarding, CONNECT tunneling, MITM TLS interception, and programmatic request/response modification.

Share

# GoProxy

![Status](https://github.com/elazarl/goproxy/workflows/Go/badge.svg)
[![GoDoc](https://pkg.go.dev/badge/github.com/elazarl/goproxy)](https://pkg.go.dev/github.com/elazarl/goproxy)
[![Go Report](https://goreportcard.com/badge/github.com/elazarl/goproxy)](https://goreportcard.com/report/github.com/elazarl/goproxy)
[![BSD-3 License](https://img.shields.io/badge/License-BSD%203--Clause-orange.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Pull Requests](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![Awesome Go](https://awesome.re/mentioned-badge.svg)](https://github.com/avelino/awesome-go?tab=readme-ov-file#networking)

GoProxy is a library to create a `customized` HTTP/HTTPS `proxy server` using
Go (aka Golang), with several configurable settings available.
The target of this project is to offer an `optimized` proxy server, usable with
reasonable amount of traffic, yet `customizable` and `programmable`.

The proxy itself is simply a `net/http` handler, so you can add multiple
middlewares (panic recover, logging, compression, etc.) over it. It can be
easily integrated with any other HTTP network library.

In order to use goproxy, one should set their browser (or any other client)
to use goproxy as an HTTP proxy.
Here is how you do that in [Chrome](https://www.wikihow.com/Connect-to-a-Proxy-Server)
and in [Firefox](https://www.wikihow.com/Enter-Proxy-Settings-in-Firefox).
If you decide to start with the `base` example, the URL you should use as
proxy is `localhost:8080`, which is the default one in our example.
You also have to [trust](https://github.com/elazarl/goproxy/blob/master/examples/customca/README.md)
the proxy CA certificate, to avoid any certificate issue in the clients.

> [✈️ Telegram Group](https://telegram.me/goproxygroup)
>
> [🎁 Become a Sponsor](https://opencollective.com/goproxy)

## Features

* Perform certain actions only on `specific hosts`, with a single equality comparison or with regex evaluation
* Manipulate `requests` and `responses` before sending them to the browser
* Use a `custom http.Transport` to perform requests to the target server
* You can specify a `MITM certificates cache`, to reuse them later for other requests to the same host, thus saving CPU. Not enabled by default, but you should use it in production!
* Redirect normal HTTP traffic to a `custom handler`, when the target is a `relative path` (e.g. `/ping`)
* You can choose the logger to use, by implementing the `Logger` interface
* You can `disable` the HTTP request headers `canonicalization`, by setting `PreventCanonicalization` to true

## Proxy modes

1. Regular HTTP proxy
2. HTTPS through CONNECT
3. HTTPS MITM ("Man in the Middle") proxy server, in which the server generate TLS certificates to parse request/response data and perform actions on them
4. "Hijacked" proxy connection, where the configured handler can access the raw net.Conn data

## Sponsors

Does your company use GoProxy? Help us keep the project maintained and healthy!
Supporting GoProxy allows us to dedicate more time to bug fixes and new features.
In exchange, if you choose a Gold Supporter or Enterprise plan, we'll proudly display your company logo here.

> [Become a Sponsor](https://opencollective.com/goproxy)

[![Gold Supporters](https://opencollective.com/goproxy/tiers/gold-sponsor.svg?width=890)](https://opencollective.com/goproxy)
[![Enterprise Supporters](https://opencollective.com/goproxy/tiers/enterprise.svg?width=890)](https://opencollective.com/goproxy)

## Maintainers

* [Elazar Leibovich](https://github.com/elazarl): Creator of the project, Software Engineer
* [Erik Pellizzon](https://github.com/ErikPelli): Maintainer, Freelancer (open to collaborations!)

If you need to integrate GoProxy into your project, or you need some custom
features to maintain in your fork, you can contact [Erik](/cdn-cgi/l/email-protection#600512090b10050c0c0920141514010d01090c4e030f0d)
(the current maintainer) by email, and you can discuss together how he
can help you as a paid independent consultant.

## Contributions

If you have any trouble, suggestion, or if you find a bug, feel free to reach
out by opening a GitHub `issue`.
This is an `open source` project managed by volunteers, and we're happy
to discuss anything that can improve it.

Make sure to explain everything, including the reason behind the issue
and what you want to change, to make the problem easier to understand.
You can also directly open a `Pull Request`, if it's a small code change, but
you need to explain in the description everything.
If you open a pull request named `refactoring` with `5,000` lines changed,
we won't merge it... `:D`

The code for this project is released under the `BSD 3-Clause` license,
making it useful for `commercial` uses as well.

### Submit your case study

So, you have introduced & integrated GoProxy into one of your personal projects
or a project inside the company you work for.

We're happy to learn about new `creative solutions` made with this library,
so feel free to `contact` the maintainer listed above via e-mail, to explaining
why you found this project useful for your needs.

If you have signed a `Non Disclosure Agreement` with the company, you
can propose them to write a `blog post` on their official website about
this topic, so this information will be public by their choice, and you can
`share the link` of the blog post with us :)

The purpose of case studies is to share with the `community` why all the
`contributors` to this project are `improving` the world with their help and
what people are building using it.

### Linter

The codebase uses an automatic lint check over your Pull Request code.
Before opening it, you should check if your changes respect it, by running
the linter in your local machine, so you won't have any surprise.

To install the linter:

root@kitploit:~

```
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

This will create an executable in your `$GOPATH/bin` folder
(`$GOPATH` is an environment variable, usually
its value is equivalent to `~/go`, check its value in your machine if you
aren't sure about it).
Make sure to include the bin folder in the path of your shell, to be able to
directly use the `golangci-lint run` command.

## A taste of GoProxy

To get a taste of `goproxy`, here you are a basic HTTP/HTTPS proxy
that just forward data to the destination:

root@kitploit:~

```
package main

import (
    "log"
    "net/http"

    "github.com/elazarl/goproxy"
)

func main() {
    proxy := goproxy.NewProxyHttpServer()
    proxy.Verbose = true
    log.Fatal(http.ListenAndServe(":8080", proxy))
}
```

### Request handler

This line will add `X-GoProxy: yxorPoG-X` header to all requests sent through the proxy,
before sending them to the destination:

root@kitploit:~

```
proxy.OnRequest().DoFunc(
    func(r *http.Request,ctx *goproxy.ProxyCtx)(*http.Request,*http.Response) {
        r.Header.Set("X-GoProxy","yxorPoG-X")
        return r,nil
    })
```

When the `OnRequest()` input is empty, the function specified in `DoFunc`
will process all incoming requests to the proxy. In this case, it will add
a header to the request and return it to the caller.
The proxy will send the mod...