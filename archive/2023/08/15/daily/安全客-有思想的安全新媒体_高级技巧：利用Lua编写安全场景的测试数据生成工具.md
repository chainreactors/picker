---
title: 高级技巧：利用Lua编写安全场景的测试数据生成工具
url: https://www.anquanke.com/post/id/290203
source: 安全客-有思想的安全新媒体
date: 2023-08-15
fetch_date: 2025-10-04T11:58:52.870518
---

# 高级技巧：利用Lua编写安全场景的测试数据生成工具

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

# 高级技巧：利用Lua编写安全场景的测试数据生成工具

阅读量**1047674**

发布时间 : 2023-08-14 10:18:57

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## 背景

在流量采集和分析的场景中，一种常见架构如下所示：

![]()​

编辑切换为居中

添加图片注释，不超过 140 字（可选）

在上述架构中，交换机通过流量镜像的方式，将用户与应用服务器之间的流量“复制”给流量采集/分析服务器。流量服务器上部署的采集探针负责协议数据包的重组，以及一部分流量分析工作，比如判断数据包是否触发某些规则。此时，需要对流量采集探针进行两方面的测试工作：

1. 性能测试：如果采集探针重组和分析数据包的性能不够高，那么将导致丢包，进而影响后续的进一步分析
2. 功能测试：从大量的流量中，准确地识别出风险事件、敏感数据等是流量分析的基础工作，如果无法做好这些工作，那么流量采集和分析将失去其意义

为进行性能测试，需要在模拟的用户和应用服务器之间，发送大量请求。为进行功能测试，需要在模拟的用户和应用服务器之间发送多种具有特定特征的流量。当前最主流的应用层协议非 HTTP 莫属。接下来将讲述如何使用 Lua 语言扩展 Nginx 和 Wrk，实现针对 HTTP 协议的性能测试和功能测试。

![]()​

编辑切换为居中

添加图片注释，不超过 140 字（可选）

## 测试环境

1. 操作系统：CentOS 7.9

## 安装 Openresty

Openresty 是完全成熟的 Web 应用服务器，它捆绑了标准的 Nginx 核心，大量的第三方模块，以及它们的大部分外部依赖。

### 安装依赖包

sudo yum install -y pcre pcre-devel openssl openssl-devel perl make gcc curl zlib zlib-devel

### 下载源码包

去官网的 [Download](http://openresty.org/cn/download.html) 页面，下载 Openrestry 源码包。本文使用的是 [openresty-1.19.9.1.tar.gz](https://openresty.org/download/openresty-1.19.9.1.tar.gz)。

wget https://openresty.org/download/openresty-1.19.9.1.tar.gz

### 安装

tar zxf openresty-1.19.9.1.tar.gz

cd openresty-1.19.9.1/

./configure –with-luajit –with-http\_iconv\_module

make -j8 && sudo make install

Openresty 默认被安装到 /usr/local/openresty/。

### 验证

/usr/local/openresty/bin/openresty -V

## 安装 Wrk

wrk 是现代的 HTTP 基准测试工具，当在单个多核 CPU 上运行时，能够产生显著的负载。它结合多线程设计和可扩展的事件通知系统，比如 epoll 和 kqueue。 可选的 LuaJIT 脚本可以执行 HTTP 请求生成、响应处理和自定义报告。

### 安装依赖包

sudo yum install -y gcc openssl openssl-devel git curl

### 克隆源码

git clone https://github.com/wg/wrk.git wrk

### 编译

cd wrk/ make

编译完成后，生成的二进制可执行文件 wrk 被保存当前目录中。可以将其移动到 PATH 中的某个目录下。

### 验证

./wrk -v

## Wrk 脚本简介

### 概览

**Wrk 支持在三个不同阶段期间执行 LuaJIT 脚本：Setup、Running 和 Done。每个 Wrk 线程拥有独立的脚本环境，Setup 和 Done 阶段在单独的环境中执行，该环境不参与 Running 阶段。**

公有 Lua API 包含全局表和多个全局函数：

wrk = {

scheme = “http”,

host = “localhost”,

port = nil,

method = “GET”,

path = “/”,

headers = {},

body = nil,

thread = <userdata>,

}

function wrk.format(method, path, headers, body)

wrk.format 返回由传入参数与 wrk 表中的值合并得到的 HTTP 请求字符串。

function wrk.lookup(host, service)

wrk.lookup 返回包含 host 和 service 对的所有已知地址的表。与 POSIX getaddrinfo() 函数对应。

function wrk.connect(addr)

如果能够连接到 addr，wrk.connect 返回 true，否则返回 false。addr 必须是从 wrk.lookup 返回的地址。 如下全局变量是可选的，如果定义，那么必须是函数：

1. global setup — 在线程 Setup 期间调用
2. global init — 在线程启动时调用
3. global delay — 用于获取请求延迟
4. global request — 用于生成 HTTP 请求
5. global response — 使用 HTTP 响应数据调用
6. global done — 使用运行结果调用

### Setup

function setup(thread)

在已解析目标 IP 地址，并且所有线程已初始化，但尚未启动之后，Setup 阶段开始。 为每个线程，调用一次 setup()，该函数接收代表线程的 userdata 对象。

1. thread.addr – 获取或设置线程的服务端地址
2. thread:get(name) – 获取线程环境中的全局变量的值
3. thread:set(name, value) – 设置线程环境中的全局变量的值
4. thread:stop() – 停止线程

只有布尔值、nil、number 和字符串值或相同的表可以通过 get()/set() 传递，thread:stop() 只能在线程运行时调用。

### Running

function init(args)

function delay()

function request()

function response(status, headers, body)

Running 阶段从对 init() 的单次调用开始，接下来为每个请求周期调用 request() 和 response()。 init() 函数为脚本接受额外的命令行参数，必须用 “–” 将其与 wrk 参数隔开。

delay() 返回延迟发送下个请求的毫秒数。 request() 返回包含 HTTP 请求的字符串。在测试高性能服务器时，每次都构建新请求代价很大。一个方案**是在 init() 中预生成所有请求，然后在 request() 中进行快速查询**。

使用 HTTP 响应状态码、头和体调用 response()。解析头和体代价很大，因此如果在调用 init() 后，response 全局变量是 nil，wrk 将忽略头和体。

### Done

function done(summary, latency, requests)

done() 函数接收包含结果数据，以及代表每个请求延迟和每个线程请求速率的两个统计对象的表。持续时间和延迟都是微秒值，而速率以每秒的请求数来衡量。

1. latency.min — 所见的最小值
2. latency.max — 所见的最大值
3. latency.mean — 所见的平均值
4. latency.stdev — 标准偏差
5. latency:percentile(99.0) — 百分之 99 的值
6. latency(i) — 原始值和计数

summary = {

duration = N, — 运行持续时间，单位为微秒

requests = N, — 已完成的请求总数

bytes = N, — 接收的总字节数

errors = {

connect = N, — Socket 连接错误总数

read = N, — Socket 读取错误总数

write = N, — Socket 写错误总数

status = N, — 大于 399 的 HTTP 状态码总数

timeout = N — 请求超时总数

}

}

## 使用 Python 生成随机图片

图片是非常常见的资源类型，常见图片格式包括 JPG、PNG、GIF 等。测试过程中，可能希望模拟的服务端返回具有指定宽度和高度的图片。Pillow 是 Python 中强大的图片处理库，接下来使用 Pillow 生成随机的 JPG、PNG、GIF 图片。

首先，需要安装 Pillow：

pip install pillow

下面是实现代码：

import string

import typing

from optparse import OptionParser

import random

import os

from PIL import Image, ImageDraw

def generate\_jpg(width: int, height: int, output: str) -> None:

“””

生成一张随机的 JPG 图片

:param width: 生成的图片的宽度

:param height: 生成的图片的高度

:param output: 输出文件名称

“””

img: Image = Image.new(“RGB”, (width, height))

pixels = img.load()

for x in range(width):

for y in range(height):

r = random.randint(0, 255)

g = random.randint(0, 255)

b = random.randint(0, 255)

pixels[x, y] = (r, g, b)

img.save(output, format=”JPEG”)

print(f”the generated JPEG image is stored in {output}, file size is {os.stat(output).st\_size / 1024} KB”)

def generate\_png(width: int, height: int, output: str) -> None:

“””

生成一张随机的 PNG 图片

:param width: 生成的图片的宽度

:param height: 生成的图片的高度

:param output: 输出文件名称

“””

img: Image = Image.new(“RGBA”, (width, height))

draw: ImageDraw = ImageDraw.Draw(img)

for x in range(width):

for y in range(height):

alpha = random.randint(0, 255)

r = random.randint(0, 255)

g = random.randint(0, 255)

b = random.randint(0, 255)

draw.point((x, y), fill=(r, g, b, alpha))

img.save(output, format=”PNG”)

print(f”the generated PNG image is stored in {output}, file size is {os.stat(output).st\_size / 1024} KB”)

def generate\_gif(width: int, height: int, num\_frames: int, output: str) -> None:

“””

生成一张随机的 GIF 图片

:param width: 生成的图片的宽度

:param height: 生成的图片的高度

:param num\_frames: 生成的图片的桢数

:param output: 输出文件名称

“””

frames: typing.List[Image] = []

for \_ in range(num\_frames):

# 生成每一帧的随机图像

image = Image.new(“RGB”, (width, height))

for x in range(width):

for y in range(height):

r = random.randint(0, 255)

g = random.randint(0, 255)

b = random.randint(0, 255)

image.putpixel((x, y), (r, g, b))

# 将当前帧添加到帧列表中

frames.append(image)

# 保存图像

frames[0].save(output, format=”GIF”, append\_images=frames[1:], save\_all=True, duration=200, loop=1)

print(f”the generated GIF image is stored in {output}, file size is {os.stat(output).st\_size / 1024} KB”)

def generate\_text(size: int, output: str) -> None:

“””

生成特定长度的随机文本

:param size: 生成的随机文本的长度

:param output: 输出文件名称

“””

with open(output, “wb”) as fd:

current\_size: int = size

while current\_size > 0:

# 每次生成 4K

batch: int = min(4096, current\_size)

fd.write(“”.join([random.choice(string.printable) for \_ in range(batch)]).encode())

current\_size -= batch

print(f”the generated text is store in {output}, file size is {os.stat(output).st\_size / 1024} KB”)

def main() -> None:

parser: OptionParser = OptionParser(usage=”python %prog options…”)

parser.add\_option(“-t”, “–type”, dest=”type”, default=”txt”, type=str,

help=”the type of generated file, including jpg, png, gif, txt”)

parser.add\_option(“-w”, “–width”, dest=”width”, default=200, type=int,

help=”the width of image, if type is image”)

parser.add\_option(“-H”, “–height”, dest=”height”, default=200, type=int,

help=”the height of image, if type is image”)

parser.add\_option(“-s”, “–size”, dest=”size”, default=1024, type=int,

help=”the size of generated file, in bytes”)

parser.add\_option(“-o”, “–output”, dest=”output”, default=”a”, type=str,

help=”output file name”)

parser.add\_option(“-n”, “–num-frames”, dest=”num\_frames”, default=10, type=int,

help=”the frame number of generated GIF image”)

options, \_ = parser.parse\_args()

\_, ext = os.path.splitext(options.output)

if options.type.lower() == “jpg”:

if ext not in [“.jpg”, “jpeg”, “.jfif”]:

options.output += “.jpg”

generate\_jpg(options.width, options.height, options.output)

return

if options.type.lower() == “png”:

if ext not in [“.png”]:

options.output += “.png”

ge...