---
title: restsharp/RestSharp: Simple REST and HTTP API Client for .NET
url: https://buaq.net/go-130887.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:55:05.687866
---

# restsharp/RestSharp: Simple REST and HTTP API Client for .NET

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

![]()

restsharp/RestSharp: Simple REST and HTTP API Client for .NET

RestSharp is a lightweight HTTP client library. It's a wrapper around HttpClient, not
*2022-10-14 19:3:16
Author: [github.com(查看原文)](/jump-130887.htm)
阅读量:23
收藏*

---

RestSharp is a lightweight HTTP client library. It's a wrapper around `HttpClient`, not a full-fledged client on its own.

What RestSharp adds to `HttpClient`:

* Default parameters of any kind, not just headers
* Add a parameter of any kind to requests, like query, URL segment, header, cookie, or body
* Multiple ways to add a request body, including JSON, XML, and form data
* Built-in serialization and deserilization of JSON and XML

## RestSharp vNext

Finally, RestSharp has moved to `HttpClient`. We also deprecated the following:

* SimpleJson in favour of `System.Text.Json.JsonSerialzer`
* `IRestClient`, `IRestRequest`, and `IRestResponse` in favour of implementing classes
* Everything `Http` and `IHttp` as those are just wrappers

Most of the client and some of the request options are now in `RestClientOptions`.

Check [v107+ docs](https://restsharp.dev/v107) for more information.

| 💥 Interfaces rage! |
| --- |
| Before you start to rage in public about interfaces that are useful for unit-testing HTTP calls, |

## Builds and Packages

### Build

|  |  |
| --- | --- |
| dev | [![](https://camo.githubusercontent.com/083e56252486bffaa34a1e2b697dcdfc8bb13300f4042723139724ceaa4d8a8b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f776f726b666c6f772f7374617475732f7265737473686172702f5265737453686172702f4275696c64253230616e642532306465706c6f79)](https://github.com/restsharp/RestSharp/actions?query=workflow%3A%22Build+and+deploy%22) |

### Nuget

|  |  |
| --- | --- |
| downloads | [![](https://camo.githubusercontent.com/1a16eda03474ff352038b0d645526028aed173f344aefe6dcb7ab56bade8e228/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f64742f526573745368617270)](https://camo.githubusercontent.com/1a16eda03474ff352038b0d645526028aed173f344aefe6dcb7ab56bade8e228/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f64742f526573745368617270) |
| stable | [![](https://camo.githubusercontent.com/7afd856a948671b0a6b38fdcc7e8f57ea6c5d3842e7e8061bdc9e507d724a828/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f762f526573745368617270)](https://www.nuget.org/packages/RestSharp) |
| preview | [![](https://camo.githubusercontent.com/24fb2df00b19a1137c128692e3389aac5eeceac585e264345704b366de3d5a74/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f767072652f526573745368617270)](https://camo.githubusercontent.com/24fb2df00b19a1137c128692e3389aac5eeceac585e264345704b366de3d5a74/68747470733a2f2f696d672e736869656c64732e696f2f6e756765742f767072652f526573745368617270) |

## Code of Conduct

This project has adopted the code of conduct defined by the Contributor Covenant to clarify expected behavior in our community.
For more information see the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct).

## Support

RestSharp is an open-source project with a single maintainer. Do not expect your issue to be resolved unless it concerns a large group of RestSharp users.
The best way to resolve your issue is to fix it yourself. Fork the repository and submit a pull request.
You can also motivate the maintainer by sponsoring this project.

### Contribute

Please read [CONTRIBUTING.md](https://github.com/restsharp/RestSharp/blob/dev/CONTRIBUTING.md) for details on the process for reporting issues and submitting pull requests.

### Get help

Read the docs: [Official Site](https://restsharp.dev)

Ask a question on StackOverflow with the tag `restsharp`.

Find RestSharp on Twitter: [@RestSharp](https://twitter.com/RestSharp)

## Community

### .NET Foundation

This project is supported by the [.NET Foundation](https://dotnetfoundation.org).

### Code Contributors

This project exists thanks to all the people who contribute.
[![](https://camo.githubusercontent.com/ee3dc271705b1dbd7cc2c3c049118e3ee73dd7cbe0282a9951de13be06d0ef11/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f636f6e7472696275746f72732e7376673f77696474683d38393026627574746f6e3d66616c7365)](https://github.com/restsharp/RestSharp/graphs/contributors)

### Financial Contributors

Become a financial contributor and help us sustain our community. [[Contribute](https://opencollective.com/RestSharp/contribute)]

#### Individuals

[![](https://camo.githubusercontent.com/7d0a109f1ea67fca0c1109a599033d30323e87e9d6ca4c6283ee45a28eb18243/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f696e646976696475616c732e7376673f77696474683d383930)](https://opencollective.com/RestSharp)

#### Organizations

Support this project with your organization. Your logo will show up here with a link to your website. [[Contribute](https://opencollective.com/RestSharp/contribute)]

[![](https://camo.githubusercontent.com/1d5737581af6da3f68ee0a06de4cd69b51b4b3465fb24dd2fed77621a5cf24e3/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f302f6176617461722e737667)](https://opencollective.com/RestSharp/organization/0/website)
[![](https://camo.githubusercontent.com/291a00212c62b63f7489d5c2040a494acd5b8f26c159930af1705bce7156c0a3/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f312f6176617461722e737667)](https://opencollective.com/RestSharp/organization/1/website)
[![](https://camo.githubusercontent.com/0f2c7467ebb4dbd3c331b103514e8ddb52f2b5978a1eae6a94b20cbb16966084/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f322f6176617461722e737667)](https://opencollective.com/RestSharp/organization/2/website)
[![](https://camo.githubusercontent.com/b68e180010bd872ab27501ed526b669f69955a057dc90d99fdf35d51b384d947/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f332f6176617461722e737667)](https://opencollective.com/RestSharp/organization/3/website)
[![](https://camo.githubusercontent.com/0e1d59ffec6d78c385f542e6052eec993eb51b4957fba2b2a09ec6b7d6f0ad8f/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f342f6176617461722e737667)](https://opencollective.com/RestSharp/organization/4/website)
[![](https://camo.githubusercontent.com/8ba16f1030be8a0ab2132d3e56065d41510535d06f99a62f3a43696ddc265c5b/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f352f6176617461722e737667)](https://opencollective.com/RestSharp/organization/5/website)
[![](https://camo.githubusercontent.com/1884a7fe25ce4155e24008101564c546e63eac9d6e6df661ccbc11f13734dc16/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f362f6176617461722e737667)](https://opencollective.com/RestSharp/organization/6/website)
[![](https://camo.githubusercontent.com/2bbc53d03100bbf2930c24b9ffd56da3f61a00433de2690e7b0bd453d79ea429/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f372f6176617461722e737667)](https://opencollective.com/RestSharp/organization/7/website)
[![](https://camo.githubusercontent.com/752f2a014555a4007c0b5cf1b736b8a33aacb6a5cf1d3abafadb6da7c113893d/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5265737453686172702f6f7267616e697a6174696f6e2f382f6176617461722e737667)](https://opencollective.com/RestSharp/organization/8/website)
[![](https://camo.githubusercontent.com/cd17dbc47c850eb110f9655e8b18ef5ba25248dc2746fcf82aa5da76...