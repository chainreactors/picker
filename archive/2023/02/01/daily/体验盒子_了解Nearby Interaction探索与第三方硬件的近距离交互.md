---
title: 了解Nearby Interaction探索与第三方硬件的近距离交互
url: https://www.uedbox.com/post/68717/
source: 体验盒子
date: 2023-02-01
fetch_date: 2025-10-04T05:21:05.992817
---

# 了解Nearby Interaction探索与第三方硬件的近距离交互

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# 了解Nearby Interaction探索与第三方硬件的近距离交互

* 发表于 2023年01月31日
* [IOS](https://www.uedbox.com/design/ios/)

iOS14苹果推出了
`NearbyInteraction`
 框架, 用于感知和连接具有U1芯片的设备。其主要目的是空间感知（近距离定位）。

目录表

Toggle

* [Nearby Interaction简介](#Nearby_Interaction%E7%AE%80%E4%BB%8B)
* [一、连接](#%E4%B8%80%E3%80%81%E8%BF%9E%E6%8E%A5)
* [二、Delegate回调](#%E4%BA%8C%E3%80%81Delegate%E5%9B%9E%E8%B0%83)
* [三. 了解NINearbyObject](#%E4%B8%89_%E4%BA%86%E8%A7%A3NINearbyObject)
* [四. 交互范围](#%E5%9B%9B_%E4%BA%A4%E4%BA%92%E8%8C%83%E5%9B%B4)
* [参考资料](#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)
* [探索与第三方硬件的近距离交互](#%E6%8E%A2%E7%B4%A2%E4%B8%8E%E7%AC%AC%E4%B8%89%E6%96%B9%E7%A1%AC%E4%BB%B6%E7%9A%84%E8%BF%91%E8%B7%9D%E7%A6%BB%E4%BA%A4%E4%BA%92)
  + [快速回顾一下如何使用 Nearby Interaction框架](#%E5%BF%AB%E9%80%9F%E5%9B%9E%E9%A1%BE%E4%B8%80%E4%B8%8B%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8_Nearby_Interaction%E6%A1%86%E6%9E%B6)
  + [用户权限上的改进](#%E7%94%A8%E6%88%B7%E6%9D%83%E9%99%90%E4%B8%8A%E7%9A%84%E6%94%B9%E8%BF%9B)
* [从一个简单的需求入手讲一下新的 API](#%E4%BB%8E%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84%E9%9C%80%E6%B1%82%E5%85%A5%E6%89%8B%E8%AE%B2%E4%B8%80%E4%B8%8B%E6%96%B0%E7%9A%84_API)
  + [part1 确保硬件设备与程序之间具备数据通道](#part1_%E7%A1%AE%E4%BF%9D%E7%A1%AC%E4%BB%B6%E8%AE%BE%E5%A4%87%E4%B8%8E%E7%A8%8B%E5%BA%8F%E4%B9%8B%E9%97%B4%E5%85%B7%E5%A4%87%E6%95%B0%E6%8D%AE%E9%80%9A%E9%81%93)
  + [part2 基于 token 创建 NearbyAccessoryConfiguration](#part2_%E5%9F%BA%E4%BA%8E_token_%E5%88%9B%E5%BB%BA_NearbyAccessoryConfiguration)
  + [part3 与硬件设备进行交互](#part3_%E4%B8%8E%E7%A1%AC%E4%BB%B6%E8%AE%BE%E5%A4%87%E8%BF%9B%E8%A1%8C%E4%BA%A4%E4%BA%92)
  + [part4 超时处理](#part4_%E8%B6%85%E6%97%B6%E5%A4%84%E7%90%86)
  + [part5 处理数据的更新](#part5_%E5%A4%84%E7%90%86%E6%95%B0%E6%8D%AE%E7%9A%84%E6%9B%B4%E6%96%B0)
* [总结](#%E6%80%BB%E7%BB%93)

## `Nearby Interaction` 简介

`Nearby Interaction`
 主要提供了两种信息, 距离（Distance）和方位(Direction)。 当两个设备通过
`Nearby Interaction`
 互相连接时, 他们会不断发送距离和方位信息， 这样就能互相定位了。 并且同一个设备能够和周围的多个设备建立连接，互不干扰

![了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/wp-content/uploads/2023/01/v2-18eca2d9df1619046e6cb4e0e622dcba_r1.png)

## 一、连接

1. 导入框架

|  |  |
| --- | --- |
| 1 | import NearbyInteraction |

2. 创建
`session`

|  |  |
| --- | --- |
| 1  2  3 | let session = NISession()  // token  print(session.discoveryToken) |

> `session`
> 有一个
> `discoveryToken`
>  属性, 两台设备互相交换
> `token`
>  才可以进行连接。 创建session后，我们读取token, 然后通过
> `MultipeerConnectivity`
>  框架进行token的交换。

![了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/wp-content/uploads/2023/01/v2-5078b9d18eccd77aa9fad727c2a59a3e_r1.png)

3. 一个完整的流程启用
`session`

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | let session = NISession()  session.delegate = self  let myDiscoveryToken = session.discoveryToken    // 发送token到需要连接的设备上  sendDiscoverTokenToMyPeer(peer, myDiscoveryToken)    // 使用接收到的token  let peerDiscoverToken = "xxxxx"    // 配置  let config = NINearbyPeerConfiguration(peerToken: peerDiscoverToken)    // 启动session  session.run(config) |

## 二、Delegate回调

1. 数据更新都是通过此方法回调

|  |  |
| --- | --- |
| 1 | optional func session(\_ session: NISession, didUpdate nearbyObjects: [NINearbyObject]) |

2. 当设备没有一段时间没有更新或者对方断开连接会收到此回调，需要注意的是这个回调并不是肯定会被调用，系统只会尽可能进行通知

|  |  |
| --- | --- |
| 1 | optional func session(\_ session: NISession, didRemove nearbyObjects: [NINearbyObject], reason: NINearbyObject.RemovalReason) |

3. 生命周期相关回调

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | // 比如app进入后台,这个方法会回调  optional func sessionWasSuspended(\_ session: NISession)  // 我们只有等此方法回调了才能继续使用session  optional func sessionSuspensionEnded(\_ session: NISession)  // 此方法回调后我们只能重新创建session进行连接  optional func session(\_ session: NISession, didInvalidateWith error: Error) |

> 当连接多个设备的时候,我们需要为每一个连接的设备创建
> `session`

## 三. 了解 `NINearbyObject`

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | open class NINearbyObject : NSObject, NSCopying, NSSecureCoding {    // token  @NSCopying open var discoveryToken: NIDiscoveryToken { get }    // 距离单位是米  public var distance: Float? { get }    // 方位  public var direction: simd\_float3? { get }  } |

## 四. 交互范围

> 检测距离大约是一个锥形，在这个方位内距离和方位都能正常更新。 超过方位距离会更新，但是方位可能不会更新。 然后我们需要确保手机是竖向的。

![了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/wp-content/uploads/2023/01/v2-68afa2c87d6c2e58ab8629169d47ce60_r.png)

## 参考资料

<https://www.wwdcnotes.com/notes/wwdc20/10668/>

<https://developer.apple.com/videos/play/wwdc2020/10668/>

<https://juejin.cn/post/7085521868320407582>

## 探索与第三方硬件的近距离交互

基于 [Session 10165](https://developer.apple.com/videos/play/wwdc2021/10165/) 探索与第三方硬件的近距离交互

2021 年 4 月的发布会上，AirTag 横空出世，从此妈妈再也不用担心我找不到钥匙了。UWB 这项技术也慢慢走进了人们的视野。现在不仅仅是只有官方的钥匙扣了。第三方的硬件授权设备也能与苹果进行交互了。 本文是讲了苹果在 Nearby Interaction 框架上的更新，全文主要分为三部分： 首先带你快速的了解一下之前是如何使用 Nearby Interaction 框架的，然后讲述在 iOS 15 上关于用户访问权限的改进，最后根据最新的 api 来实现一个简单的 demo。

### 快速回顾一下如何使用 Nearby Interaction框架

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | class ViewController: UIViewController, NISessionDelegate {    override func viewDidLoad() {  super.viewDidLoad()  let token = \_token  let niSession = NISession()  niSession.delegate = self  niSession.run(NINearbyPeerConfiguration(peerToken: token))  }  func session(\_ session: NISession, didUpdate nearbyObjects: [NINearbyObject]){  nearbyObjects.forEach { (niNearbyObject) in  print(niNearbyObject.distance!);  print(niNearbyObject.direction!);  }  }  } |

如何在两个手机之间建立联系呢？首先创建一个 NISessions 实例，然后在代码中遵守 NISessionDelegate 协议，在 session 实例的 run 函数中需要传入一个 NIConfiguration 的子类做配置对象。如果想要在两个 iPhone 之间建立联系，可以使用 NINearbyPeerConfiguration 做参数，但是在 NINearbyPeerConfiguration 的初始化中需要知道对方的 token，这个 token 可以通过网络进行传输，当你准备好这一切的时候，Nearby Interaction 将开始为程序提供 NearbyObject 更新流，每个更新包含到附近设备的距离和方向（可选）。如果想要继续深入的了解这个库的 API，可以去看去年演讲 "Meet Nearby Interaction"。

### 用户权限上的改进

在 iOS 14 上的的 Nearby Interaction 的权限流程是这样的，当你的 App 在一个新的生命周期中，第一次创建一个 NISession 会话的时候会展示弹窗，弹窗的样式如下图，但由于此权限是一次性的，因此在某些情况下也可能导致展示多次弹窗。

![了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/wp-content/uploads/2023/01/4536_0_0_0.png)

今年在 iOS 15 上对权限进行了改进，弹窗如下图。这是 iOS 15 中新的“附近交互”权限提示。看起来很相似，但却和之前的权限授予流程有以下不同：

![了解Nearby Interaction探索与第三方硬件的近距离交互](https://www.uedbox.com/wp-content/uploads/2023/01/crop-mark_4536_0_0_0.png)

* 提示时机：系统会在应用程序第一次运行 NISession 时自动显示权限提示。因此确保运行 NISession 的时间与用户想要使用这个功能的时间保持一致，这样您的用户就很容易理解为什么您需要这个权限。
* 提示的选项：让我们仔细看看提示上的新选项。新的“确定”选项可在应用程序使用时授予您的应用程序权限。无论用户接受还是拒绝您的应用使用附近交互的请求，权限提示都不会再次显示。
* 新的权限设置位置：从 iOS 15 开始，使用 Nearby Interaction 的应用将出现在“设置”中。因此，如果用户改变主意，他们可以转到“设置”应用并更改应用的“附近互动”访问权限。应确保在开发应用时针对权限的变更进行测试。

总结一下新的 Nearby Interaction 用户权限模型。在弹窗中点击 Allow 后，您的应用将获得在应用使用过程中使用 Nearby Interaction 的持久权限。弹窗上将显示一个使用说明字符串，在 Info.plist 中配置。在这个配置中要简洁明了的解释您在应用程序中访问附近的设备可以提供那些有趣的能力。在第一次也是最后一次出现提示后，您的应用的名称和图标将出现在“设置”中，这意味着用户可以随时更改您的应用的权限状态。当应用程序没有足够的权限使用 Nearby Interaction 时， NISessions 所有的功能都会失效。因此，如果应用程序中的关键功能依赖于对附近设备的访问，请务必向用户清楚地解释这一点，并在适当的时候引导他们使用“设置”去打开配置权限。

## 从一个简单的需求入手讲一下新的 API

没有业务场景的新特性都是瞎逼逼，下面将从一个实用的业务场景出发来介绍如何使用 Nearby Interaction API 与第三方配件一起工作。

> 想象一下，在你的设备周围定义了一个半径为 1.5 米的区域和另外一个半径为 3 米的更大的区域，当用户进入较大的区域的时候您希望启动功能 A，当用户进入较小的区域的时候你期望启动功能 B，如何使用 Nearby Interaction 来实现这一个功能？

### part1 确保硬件设备与程序之间具备数据通道

Nearby Interaction 需要硬件与应用程序之间具有数据交换的能力。至于采...