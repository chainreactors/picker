---
title: Navigation Bar Tutorial in iOS 18 - #30DaysOfSwift
url: https://buaq.net/go-265687.html
source: unSafe.sh - 不安全
date: 2024-10-06
fetch_date: 2025-10-06T18:48:19.784157
---

# Navigation Bar Tutorial in iOS 18 - #30DaysOfSwift

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

![](https://8aqnet.cdn.bcebos.com/c464a6ce2f46217d85b9b6e75638f802.jpg)

Navigation Bar Tutorial in iOS 18 - #30DaysOfSwift

Too Long; Didn't ReadIn the third post of the #30DaysOfSwift series, I am going to teach you how to
*2024-10-5 23:0:20
Author: [hackernoon.com(查看原文)](/jump-265687.htm)
阅读量:16
收藏*

---

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format&fit=max&w=48)

![Open TLDR](https://hackernoon.imgix.net/tl;dr-dark.png?auto=format&fit=max&w=128)![tldt arrow](https://hackernoon.imgix.net/arrow-dark.png)

## Too Long; Didn't Read

In the third post of the #30DaysOfSwift series, I am going to teach you how to make a sticky navigation bar. Create a new SwiftView file called "HomeView" Replace the ContentView() with HomeView() in YourAppNameApp.swift (in this case, my project is called ShipiOS. Thus, file name is ShipiOSApp.Swift).

![featured image - Navigation Bar Tutorial in iOS 18 - #30DaysOfSwift](https://hackernoon.imgix.net/images/eQHzh6rz7ETBHLjs0KzCl1Dooqp2-so0353y.webp?auto=format&fit=max&w=3840)

![Vaibhav HackerNoon profile picture](https://hackernoon.imgix.net/images/8BeqPUXlmKUL9raEruPQp4lfhAv2-5q834b7.png?w=100&auto=format&fit=max)

**Day 2: Wandering around the multiple paths 🛣️**

In the third post of the #30DaysOfSwift series, I am going to teach you how to make a sticky navigation bar.

The output would look something like this:

## Steps:

* Create a new SwiftView file called "HomeView."

* Replace the ContentView() with HomeView() in YourAppNameApp.swift (In this case, my project is called ShipiOS. Thus, file name is ShipiOSApp.swift).

```
var body: some Scene {
        WindowGroup {
            HomeView()
        }
    }
```

* Lastly, add the following code in your HomeView() file: [![Image description](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdal2vr1ggsj7u71s96pl.png?auto=format&fit=max&w=1920)](https://media.dev.to/dynamic/image/width%3D800%2Cheight%3D%2Cfit%3Dscale-down%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A//dev-to-uploads.s3.amazonaws.com/uploads/articles/dal2vr1ggsj7u71s96pl.png?ref=hackernoon.com)

Code:

```
struct HomeView: View {
    @State private var selectedTab = 0 // Track the selected tab
    let generator = UIImpactFeedbackGenerator(style: .light) // For Haptics

    @EnvironmentObject var userCommonData: CommonData

    var body: some View {
        TabView(selection: $selectedTab) {
            ContentView() // Replace with your view
                .tabItem {
                    Label("Home", systemImage: "house")
                }
                .tag(0)

            SecondView() // Replace with your view
                .tabItem {
                    Label("Chats", systemImage: "tray")
                }
                .tag(1)

            ThirdView() // Replace with your view
                .tabItem {
                    Label("Profile", systemImage: "gearshape")
                }
                .tag(2)
        }
        .accentColor(Color("AppSecondaryColor"))
        .onChange(of: selectedTab) {
            generator.impactOccurred()
        }
    }

}
```

Does it work? Let me know :)

**Happy coding!**

文章来源: https://hackernoon.com/navigation-bar-tutorial-in-ios-18-30daysofswift?source=rss
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)