---
title: gRPC 介绍及 Go gRPC 入门教程
url: https://www.anquanke.com/post/id/285185
source: 安全客-有思想的安全新媒体
date: 2023-01-10
fetch_date: 2025-10-04T03:22:35.895593
---

# gRPC 介绍及 Go gRPC 入门教程

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# gRPC 介绍及 Go gRPC 入门教程

阅读量**212382**

发布时间 : 2023-01-09 10:31:00

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# 介绍

gRPC 是开源的远程过程调用（RPC）框架，可在任何环境运行。使用 gRPC 可以有效地连接数据中心内和跨数据中心的服务，gRPC 具有可插拔的负载均衡、追踪、健康检查和身份验证支持。它也适用于将设备、移动应用程序和浏览器连接到后端服务的分布式计算的最后一英里。

gRPC 具有如下特点：

1. 简单的服务定义：使用 Protocol Buffers（强大的二进制序列化工具集和语言）定义服务
2. 快速开始和伸缩：使用单行代码安装运行时和开发环境，还可以使用框架扩展到每秒数百万个 RPC
3. 适用于多种语言和平台：自动地为服务生成各种语言和平台的客户端和服务端存根
4. 双向流和集成认证：双向流和完全集成的基于 HTTP/2 传输的可插拔认证

gRPC 使用 Protocol Buffers 作为它的接口定义语言（Interface Definition Language，IDL），及底层的消息交换格式。

## 概览

在 gRPC 中，客户端应用程序可以直接调用部署在不同机器上的服务端应用程序中的方法，就好像它是本地对象一样，使用 gRPC 可以更容易地创建分布式应用程序和服务。与许多 RPC 系统一样，gRPC 基于定义服务的思想，指定可以通过参数和返回类型远程调用的方法。在服务端侧，服务端实现接口，运行 gRPC 服务，处理客户端调用。在客户端侧，客户端拥有存根（Stub，在某些语言中称为客户端），它提供与服务端相同的方法。

![]()

gRPC 客户端和服务端可以在各种环境中运行和相互通信 – 从 Google 内部的服务器到你自己的桌面 – 并且可以使用 gRPC 支持的任何语言编写。因此，比如，你可以轻松地用 Java 创建 gRPC 服务端，使用 Go、Python 或 Ruby 创建客户端。此外，最新的 Google API 将包含 gRPC 版本的接口，使你轻松地将 Google 功能构建到你的应用程序中。

## 使用 Protocol Buffer

默认，gRPC 使用 Protocol Buffers（https://developers.google.com/protocol-buffers/docs/overview），Google 的成熟的用于序列化结构化数据的开源机制（尽管可以使用其它数据格式，比如 JSON）。下面将快速介绍如何使用它。

当使用 Protocol Buffer 时，第一步是在 proto 文件中定义你想要序列化的数据的结构：它是扩展名为 .proto 的普通文本文件。Protocol Buffer 数据被构造为消息（message），其中每条消息是一个小的逻辑信息记录，包含一系列被称为字段（field）的名称-值对。下面是一个简单的示例：

message Person {

string name = 1;

int32 id = 2;

bool has\_ponycopter = 3;

}

在指定数据结构后，可以使用 Protocol Buffer 编译器 protoc 从 proto 定义中生成所选语言的数据访问类。它们为每个字段提供简单的访问器，比如 name() 和 set\_name()，以及用于将整个结构序列化成原始字节流和从原始字节流解析整个结构的方法。因此，比如，如果你选择的语言是 C++，那么在上面的示例上运行编译器将生成名为 Person 的类。然后可以在应用程序中使用该类填充、序列化和检索 Person Protocol Buffer 消息。

在普通的 proto 文件中定义 gRPC 服务，RPC 方法参数和返回类型被指定为 Protocol Buffer 消息：

// The greeter service definition.

service Greeter {

// Sends a greeting

rpc SayHello (HelloRequest) returns (HelloReply) {}

}

// The request message containing the user’s name.

message HelloRequest {

string name = 1;

}

// The response message containing the greetings

message HelloReply {

string message = 1;

}

gRPC 使用带特殊的 gRPC 插件的 protoc 从 proto 文件生成代码：你将获得生成的 gRPC 客户端和服务端代码，以及用于填充、序列化和检索消息类型的常规 Protocol Buffer 代码。如果想要了解更多关于 Protocol Buffer 的信息，包括如何在所选语言中安装带 gRPC 插件的 protoc，请参阅 protocol buffers documentation。

## Protocol Buffer 版本

虽然开源用户使用 protocol buffers 已有一段时间，但是本站点的大多数示例使用 Protocol Buffer 版本 3（proto3），它拥有略微简化的语法、一些有用的新特性，以及支持更多语言。Proto3 目前可用于 Java、C++、Dart、Python、Objective-C、C#、lite-runtime（Android Java）、Ruby 和来自 Protocol Buffer Github 仓库的 JavaScript，以及来自 golang/protobuf 官方包的 Go 语言生成器，更多语言正在开发中。你可以在 Proto3 语言指南和每种语言的可用参考文档中找到更多信息。参考文档也包含 .proto 文件格式的正式规范。

一般来说，虽然你可以使用 proto2（当前默认的 Protocol Buffer 版本），但我们建议你将 proto3 与 gRPC 一起使用，因为它可以让你使用 gRPC 支持的全部语言，以及避免 proto2 客户端与 proto3 服务端通信的兼容性问题，反之亦然。

# 核心概念

## 概览

##### **服务定义**

与许多 RPC 系统一样，gRPC 基于定义服务的思想，指定可以通过参数和返回类型远程调用的方法。默认情况下，gRPC 使用 Protocol Buffer 作为接口定义语言（IDL），来描述服务接口和负载消息的结构。如果需要，也可以使用其它替代品。

service HelloService {

rpc SayHello (HelloRequest) returns (HelloResponse);

}

message HelloRequest {

string greeting = 1;

}

message HelloResponse {

string reply = 1;

}

gRPC 支持定义四种服务方法：

1. 一元（unary）RPC，客户端向服务端发送单个请求，取回单个响应，就像普通的函数调用一样。

rpc SayHello(HelloRequest) returns (HelloResponse);

1. 服务端流 RPC，客户端向服务端发送一个请求，取回用于读取消息序列的流。客户端从返回的流中读取，直到没有更多消息。gRPC 保证单个 RPC 调用中的消息顺序。

rpc LotsOfReplies(HelloRequest) returns (stream HelloResponse);

1. 客户端流 RPC，客户端写消息序列，再使用提供的流，将它们发送到服务端。一旦客户端完成写消息，它等待服务端读消息，返回响应。gRPC 再次保证单个 RPC 调用中的消息顺序。

rpc LotsOfGreetings(stream HelloRequest) returns (HelloResponse);

1. 双向流 RPC，两侧都使用读-写流发送消息序列。这两个流独立运行，因此客户端和服务端可以按照它们喜欢的任何顺序进行读写：比如，服务端可以在写入响应之前等待接收所有客户端消息，或者交替地读消息，然后写消息，或者执行某些其它读写组合。每个流中的消息顺序保持不变。

rpc BidiHello(stream HelloRequest) returns (stream HelloResponse);

##### **使用 API**

从 .proto 文件中的服务定义开始，gRPC 提供生成客户端和服务端代码的 Protocol Buffer 编译器插件。gRPC 用户通常在客户端调用这些 API，并且在服务器端实现相应的 API。

1. 在服务端侧，服务端实现 service 声明的方法，运行 gRPC 服务处理客户端调用。gRPC 基础结构解码传入的请求，执行服务方法，对服务响应进行编码。
2. 在客户端侧，客户端拥有被称为存根（在某些语言中，首选术语是客户端）的本地对象，该对象实现与 service 相同的方法。客户端可以只调用本地对象上的方法，这些方法将调用的参数包装在适当的 Protocol Buffer 消息类型中，然后将请求发送到服务端，最后返回服务端的 Protocol Buffer 响应。

#####

##### **同步 vs. 异步**

同步 RPC 调用阻塞直到服务端的响应到达，这与 RPC 所期望的过程调用的抽象最接近。另一方面，网络本质上是异步的，在许多情况下，能够在不阻塞当前线程的情况下启动 RPC 非常有用。

大多数语言中的 gRPC 编程 API 都有同步和异步两种风格。你可以在每种语言的教程和参考文档中找到更多信息。

## RPC 生命周期（RPC Life Cycle）

#####

##### **一元 RPC（Unary RPC）**

首先看最简单的 RPC 类型，客户端发送单个请求，取回单个响应。

1. 当客户端调用存根（Stub）方法时，服务端将收到通知，客户端使用用于本次调用的元数据（metadata）、方法名称和指定的截止时间（deadline）调用 RPC。

2. 然后，服务端可以直接发送回它自己的初始元数据（必须在任何响应之前发送），也可以等待客户端的请求消息。先发生哪个，是特定于应用程序的。

3. 一旦服务端拥有客户端的请求消息，它就会执行创建和填充响应所需的所有工作。然后将响应（如果成功）连同状态详细信息（状态代码和可选的状态消息）和可选的尾随元数据一起返回到客户端。

4. 如果响应状态是 OK，那么客户端获取响应，在客户端侧完成响应。

##### **服务端流 RPC**

服务端流 RPC 与一元 RPC 类似，不同之处在于服务端返回消息流，以响应客户端的请求。在发送所有消息后，服务端的状态详情（状态码和可选的状态消息）和可选的尾随元数据被发送到客户端。这完成服务端侧的处理。客户端在拥有服务端的所有消息后完成处理。

#####

##### **客户端流 RPC**

客户端流 RPC 与一元 RPC 类似，不同之处在于客户端向服务端发送消息流，而不是单个消息。服务端响应单条消息（以及它的状态详细信息和可选的尾随元数据），通常（但不一定）在它接收到所有客户端消息之后。

#####

##### **双向流 RPC**

在双向流 RPC 中，调用由调用方法的客户端发起，服务端接收客户端的元数据、方法名和截止时间。服务端可以选择发送回它的初始元数据，或者等待客户端开始流消息。

客户端侧和服务端侧流处理是特定于语言的，由于这两个流是独立的，客户端和服务端可以以任意顺序读写消息。例如，服务端可以等待到收到客户端的所有消息后，再写它的消息，或者服务端和客户端可以玩“乒乓”游戏 – 服务器接收请求，然后发送回响应，然后客户端根据响应发送另一个请求，以此类推。

#####

##### **截止时间/超时**

gRPC 允许客户端指定在 RPC 以 DEADLINE\_EXCEEDED 错误终止之前，他们愿意等待多久。在服务端，服务可以查询特定的 RPC 是否超时，或者还剩下多少时间来完成该 RPC。

指定截止日期或超时是特定于语言的：一些语言 API 根据超时（持续时间）工作，一些语言 API 根据截止时间（固定的时间点）工作，并且可能有也可能没有默认截止时间。

#####

##### **RPC 终止**

在 gRPC 中，客户端和服务端都对调用的成功做出独立的本地决定，并且它们的结论可能不匹配。这意味着，比如，你可以有一个在服务端成功完成（“我已经发送所有响应！”），但在客户端失败（“响应在截止时间之后到达！”）的 RPC。服务端也可以在客户端发送所有请求之前决定完成。

#####

##### **取消 RPC**

客户端和服务端都可以随时取消 RPC，取消将立即终止 RPC，因此不会执行进一步的工作。

警告

在取消前发生的变更不会回滚。

##### **元数据**

元数据是键-值对列表形式的关于特定 RPC 调用（比如身份验证详细信息）的信息，其中键是字符串，值通常是字符串，但也可以是二进制数据。

键不区分大小写，由 ASCII 字母、数字和特殊字符 -、\_ 和 . 组成，并且不能以 grpc- 开头（为 gRPC 本身保留）。二进制值的键以 -bin 结尾，而 ASCII 值的键则不是。

用户定义的元数据不会被 gRPC 使用，它允许客户端向服务端提供与本次调用相关的信息，反之亦然。

对元数据的访问依赖于语言。

##### **通道**

gRPC 通道提供到指定主机和端口上的 gRPC 服务的连接。在创建客户端存根时使用。客户端可以指定通道参数来修改 gRPC 的默认行为，比如打开或关闭消息压缩。通道有状态，包括已连接和空闲。

gRPC 如何处理关闭通道取决于语言。有些语言也允许查询通道状态。

# 快速入门 Go gRPC

## 环境说明

1. 操作系统：macOS 12.6
2. Go：go version go1.19 darwin/amd64
3. Protobuf：3.21.5

## 创建测试项目

mkdir hellogrpc

cd hellogrpc

go mod init hellogrpc

## 给 protocol 编译器安装 Go 插件

1.使用下述命令为 Go 安装 protocol 编译器插件：

$ go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28

$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2

2. 更新 PATH，以便 protoc 编译器可以找到插件：

$ export PATH=”$PATH:$(go env GOPATH)/bin”

## 安装依赖包

$ go get google.golang.org/grpc

## 项目结构

hellogrpc % tree .

.

├── go.mod

├── go.sum

├── greeter\_client

│ └── main.go

├── greeter\_server

│ └── main.go

└── hellogrpc

└── hellogrpc.proto

3 directories, 5 files

go.mod：

module hellogrpc

go 1.19

require google.golang.org/grpc v1.51.0

require (

github.com/golang/protobuf v1.5.2 // indirect

golang.org/x/net v0.0.0-20220722155237-a158d28d115b // indirect

golang.org/x/sys v0.0.0-20220722155257-8c9f86f7a55f // indirect

golang.org/x/text v0.4.0 // indirect

google.golang.org/genproto v0.0.0-20200526211855-cb27e3aa2013 // indirect

google.golang.org/protobuf v1.27.1 // indirect

)

greeter\_client/main.go：

package main

import (

“context”

“flag”

“log”

“time”

“google.golang.org/grpc”

“google.golang.org/grpc/credentials/insecure”

pb “hellogrpc/hellogrpc”

)

const (

defaultName = “world”

)

var (

addr = flag.String(“addr”, “localhost:50051”, “the address to connect to”)

name = flag.String(“name”, defaultName, “Name to greet”)

)

func main() {

flag.Parse()

// Set up a connection to the server.

conn, err := grpc.Dial(\*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))

if err != nil {

log.Fatalf(“did not connect: %v”, err)

}

d...