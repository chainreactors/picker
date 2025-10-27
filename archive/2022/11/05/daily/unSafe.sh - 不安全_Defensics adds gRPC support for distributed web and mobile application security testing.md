---
title: Defensics adds gRPC support for distributed web and mobile application security testing
url: https://buaq.net/go-134231.html
source: unSafe.sh - 不安全
date: 2022-11-05
fetch_date: 2025-10-03T21:42:41.921310
---

# Defensics adds gRPC support for distributed web and mobile application security testing

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2cde7b2acfc19428d34d7dd8edac2818.jpg)

Defensics adds gRPC support for distributed web and mobile application security testing

Posted by on Friday, November 4, 2022
*2022-11-4 20:53:21
Author: [www.synopsys.com(查看原文)](/jump-134231.htm)
阅读量:26
收藏*

---

Posted by on Friday, November 4, 2022

*Learn how the gRPC test suite and gRPC wizard enable Defensics customers to create their own test sequences from protocol buffer definitions.*

As the leading tool on the market for negative testing, Synopsys Defensics® fuzz testing currently offers over 300 test suites to ensure system security and robustness. Defensics has now expanded testing of communication protocols with support for the popular gRPC framework used in microservices, mobile, web, and IoT applications. The gRPC framework uses HTTP/2 as a transport protocol and Protobuf (protocol buffers) for its service definition. The framework offers tools for creating client and server bindings for multiple programming languages including Go, Java, C++, Python, and many others. The code bindings are automatically generated based on a Protobuf definition.

Protobuf is an open source mechanism for serializing structured data, which are defined through the use of an interface definition language (IDL). The Protobuf IDL defines message structures and the remote procedure call (RPC) services of a system. Protobuf also includes a proto compiler, which generates serialization code from Protobuf definitions. The gRPC framework serializes and deserializes data when it is sent between network nodes.

## Fuzzing gRPC

Defensics is a model-based fuzzer. A basic Defensics test suite is written on the basis of protocol specifications. In the case of gRPC though, this does not work because each system has its own definition. We know the basic encoding for the various fields, but to create effective test cases, we need to know more about the system under test.

Another problem with gRPC fuzzing is that while we can learn the protocol model and service endpoints from a Protobuf definition, we don’t know how the system under test uses the RPCs and what data is sent over the messages. We could create a test sequence for each RPC separately, but most systems have an internal state in which RPC A needs to be sent before RPC B, so the server is in the correct state to receive RPC B.

The [gRPC test suite](https://synopsys.skilljar.com/defensics-grpc-test-suite) offers customers a way to import Protobuf files into Defensics using a gRPC wizard. The gRPC wizard takes in Protobuf definitions, parses them, and shows the available remote procedure calls defined in the files. RPCs can then be used for building a test sequence, which is relevant for the tested system. In addition to building a relevant test sequence, the wizard also allows users to modify each send message to have relevant valid values in the message fields. This is done to ensure the gRPC test suite is interoperable with the test target.

The following image shows the gRPC wizard in action. The imported file is example.proto.

![imported file example.proto in gRPC wizard | Synopsys](https://images-cdn.welcomesoftware.com/Zz05NDdhMGNhNDViYjQxMWVkYTIzYzhlNThiNDhjZjBiNA==?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOlsiOTQ3YTBjYTQ1YmI0MTFlZGEyM2M4ZTU4YjQ4Y2YwYjQiXSwiZXhwIjoxNjY3NTczNjAwfQ.1d5PdUE10D5rzrLPR5d4nUZVuKbf6zb_G1nOp7H7IlQ)

After completing the desired configuration, the gRPC wizard will create a sequence file for the gRPC test suite. This sequence file is loaded into a new gRPC test suite instance, and test cases are automatically generated, ready to fuzz the test target.

The following image shows a list of test cases generated based on the example.proto.

![list of test cases generated based on the example.proto | Synopsys](https://images-cdn.welcomesoftware.com/Zz1kYWIzNGVhNjViYjQxMWVkOTg4M2RlMjY2MzZkODM5YQ==?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOlsiZGFiMzRlYTY1YmI0MTFlZDk4ODNkZTI2NjM2ZDgzOWEiXSwiZXhwIjoxNjY3NTczNjAwfQ.YA5j_jk8kK-g-mqVR-b0AG2FKDQxIBT488RKiIgkxJY)

The gRPC test suite can fuzz both Protobuf/gRPC parsers and application code. For most users, the interesting part of [fuzzing](https://www.synopsys.com/software-integrity/security-testing/fuzz-testing.html) is the application-level implementation using gRPC for communication. To improve fuzzing speed, the gRPC test suite can be configured to limit test cases to the Protobuf field content, which is the data used in application-level implementation.

## About Defensics fuzz testing

Defensics is a comprehensive, powerful, and automated black box solution supporting most smart home wireless and IoT protocols, in addition to [more than 300 other protocols](https://www.synopsys.com/software-integrity/security-testing/fuzz-testing/defensics.html). Defensics is a generational fuzzer that knows the protocol you’re testing. All our wireless testing can be done over the air against a boxed device without the need for source code access. If you are interested in integrating fuzz testing into your [CI/CD pipeline](https://www.synopsys.com/glossary/what-is-cicd.html), Defensics allows headless test integration via a Jenkins plugin, CLI, and the REST API. All three integration interfaces allow a basic workflow of configuring the fuzzer, running and tracking test progress, and exporting test reports.

To learn more and find the right test suite for your system security needs, visit the [Defensics webpage](https://www.synopsys.com/software-integrity/security-testing/fuzz-testing/defensics.html).

![](https://pixel.welcomesoftware.com/px.gif?key=YXJ0aWNsZT00Yjg5NWZiZTU5NTYxMWVkYTRhNDVlN2I5MzliNmVjYw==)

文章来源: https://www.synopsys.com/blogs/software-security/defensics-grpc-support-for-web-mobile-app-testing/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)