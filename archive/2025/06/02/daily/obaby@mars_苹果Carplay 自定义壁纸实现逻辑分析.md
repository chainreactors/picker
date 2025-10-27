---
title: 苹果Carplay 自定义壁纸实现逻辑分析
url: https://h4ck.org.cn/2025/06/20875
source: obaby@mars
date: 2025-06-02
fetch_date: 2025-10-06T22:52:03.711504
---

# 苹果Carplay 自定义壁纸实现逻辑分析

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [苹果『iOS』](https://h4ck.org.cn/cats/xtxg/%E8%8B%B9%E6%9E%9C%E3%80%8Eios%E3%80%8F)

# 苹果Carplay 自定义壁纸实现逻辑分析

2025年6月1日
[21 条评论](https://h4ck.org.cn/2025/06/20875#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/330A1731-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/330A1731-tuya.jpg)

虽然在开车的时候，多数时间不会停留在carplay的桌面。然而，当第一次切进来的时候显示的那个桌面背景图片，着实不怎么喜欢。于是就想着能够换掉这个壁纸。

网上搜了一下，基本都是一年前的文章，或者说最新的文章都是一年前的。这就比较尴尬了。
而至于实现工具和方法，到处都是抄来抄去的文章，第一步基本都是安装巨魔助手，Troll app，https://trollstore.app
这是一个越狱的应用商店。通过这个越狱的商店安装AirWall，在air wall里面设置壁纸。
https://onejailbreak.com/blog/airwall/

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/airwall-carplay.766x0.webp)](https://h4ck.org.cn/wp-content/uploads/2025/06/airwall-carplay.766x0.webp)
这一切看起来似乎完美，但是，这个troll store app 最高支持到ios 17，我现在的18没有越狱，也不想越狱。那么又该怎么搞呢？

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-01-155325.png)](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-01-155325.png)
自然是自签名，目前爱思助手之类的貌似不支持普通的appstore账号签名安装了。
不过可以通过下面的工具，签名应用然后通过爱思助手安装。

> [Sideloadly Download iOS 18.3+ | Install IPA Without Revoke](https://iexmo.com/sideloadly/)

> Esign iPA download and install using Sideloaly App.
> Download Esign IPA:
> First, download the Esign IPA file for your PC.
> Download Esign iPA file.
> Install Sideloadly:
> Sideloadly is the tool we’ll use to install Esign on your iOS device.
> If you don’t have Sideloadly yet, download and install Sideloadly app on your PC(Windows or Mac).
> Connect Your Device:
> Connect your iPhone or iPad to your computer using a USB cable.
> Open Sideloadly:
> Launch the Sideloadly application on your computer.
> Select the IPA File:
> In Sideloadly, click on the IPA icon to select the Esign IPA file you downloaded earlier.
> Sign the IPA File:
> Enter your Apple ID and password when prompted. This step is necessary for signing the IPA file.
> Start Installation:
> Click the Start button in Sideloadly to begin the installation process.
> Sideloadly will sign the Esign IPA file and install it on your iOS device.
> Check Your Home Screen:
> Once the process is complete, you’ll find the Esign app icon on your home screen.
> Then go to Settings App → General → Profiles & Device Management → Find the Esign app profile and trust it.
> You can now use Esign to sign and install other IPA files directly on your device.

然而，签名安装之后却发现了另外一个问题，那就是卡在了加载界面。一直在获取目录，后面就进行不下去了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/failed.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/failed.jpg)

上网搜了一下，好无进展，都是说什么连接carplay之后在设置，然而，这就是句废话。连上了也没什么用。
不过，这个app体积不大，直接拉出来。扔到hopper里面看下实现逻辑，也并不复杂。
直接通过目录来获取的当前壁纸，同样替换壁纸也是直接写入文件实现的。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/wallpaper-1-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/wallpaper-1.jpg)
看F5之后的代码就更直观了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/wallpaper-2.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/wallpaper-2.jpg)
导出代码，直接扔给cursor，让cursor根据f5代码拆分重构代码。

现在代码逻辑就明朗了，更换壁纸的方法主要在AirawWallpaper.m中：

```
#pragma mark - Helper Methods

- (void)checkingPath {
    // 检查壁纸路径
    NSFileManager *fileManager = [NSFileManager defaultManager];
    NSString *basePath = @"/var/mobile/Containers/Data/Application/";

    // 检查是否有权限访问
    if (![fileManager isWritableFileAtPath:basePath]) {
        UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"权限错误"
                                                                      message:@"无法访问系统目录，请确保设备已越狱并授予了正确的权限。"
                                                               preferredStyle:UIAlertControllerStyleAlert];
        [alert addAction:[UIAlertAction actionWithTitle:@"确定" style:UIAlertActionStyleDefault handler:nil]];
        [self presentViewController:alert animated:YES completion:nil];
        return;
    }

    NSError *error = nil;
    NSArray *contents = [fileManager contentsOfDirectoryAtPath:basePath error:&error];
    if (error) {
        NSLog(@"Error reading directory: %@", error);
        return;
    }

    NSMutableArray *validPaths = [NSMutableArray array];
    for (NSString *path in contents) {
        if ([path containsString:@"com.apple.CarPlayApp.wallpaper-images"]) {
            NSString *fullPath = [basePath stringByAppendingPathComponent:path];
            BOOL isDirectory;
            if ([fileManager fileExistsAtPath:fullPath isDirectory:&isDirectory] && isDirectory) {
                [validPaths addObject:path];
            }
        }
    }

    if (validPaths.count > 0) {
        self.FullCache = [basePath stringByAppendingPathComponent:validPaths[0]];
        [self.tableView reloadData];
    } else {
        UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"错误"
                                                                      message:@"未找到 CarPlay 壁纸目录，请确保已正确安装 CarPlay 应用。"
                                                               preferredStyle:UIAlertControllerStyleAlert];
        [alert addAction:[UIAlertAction actionWithTitle:@"确定" style:UIAlertActionStyleDefault handler:nil]];
        [self presentViewController:alert animated:YES completion:nil];
    }
}
```

当然，上面这段代码的错误提示是我让cursor加上的。原来的并没有这段，这个是f5的代码：

```
int ___30-[AirawWallpaper checkingPath]_block_invoke(int arg0) {
    r31 = r31 - 0xc0;
    saved_fp = r29;
    stack[-8] = r30;
    var_80 = arg0;
    var_18 = [[NSFileManager defaultManager] retain];
    r0 = [var_18 enumeratorAtPath:@"/var/mobile/Containers/Data/Application/"];
    r29 = &saved_fp;
    var_20 = [r0 retain];
    var_28 = [@"" retain];
    do {
            r0 = [var_20 nextObject];
            r29 = r29;
            r0 = [r0 retain];
            r8 = var_28;
            var_28 = r0;
            [r8 release];
            if (r0 == 0x0) {
                break;
            }
            if ([var_28 rangeOfString:@"com.apple.CarPlayApp.wallpaper-images"] == 0x7fffffffffffffff) {
                continue;
            }
            r0 = [@"/var/mobile/Containers/Data/Application/" stringByAppendingPathComponent:var_28];
            r29 = r29;
            [var_18 fileExistsAtPath:[r0 retain] isDirectory:r29 - 0x29];
            if ((var_29 & 0x1) != 0x0) {
                    [*(var_80 + 0x20) addObject:var_28];
            }
            objc_storeStrong(r29 - 0x48, 0x0);
    } while (true);
    r11 = *(var_80 + 0x28);
    *(&var_78 + 0x10) = 0x100007ae0;
    *(&var_78 + 0x18) = 0x100014200;
    *(&var_78 + 0x20) = [*(var_80 + 0x30) retain];
    *(&var_78 + 0x28) = [*(var_80 + 0x20) retain];
    dispatch_async(r11, &var_78);
    objc_storeStrong(&var_78 + 0x28, 0x0);
    objc_storeStrong(&var_78 + 0x20, 0x0);
    objc_storeStrong(r29 - 0x28, 0x0);
    objc_storeStrong(r29 - 0x20, 0x0);
    r0 = objc_storeStrong(r29 - 0x18, 0x0);
    return r0;
}
```

不过现在，也能看出问题出在什么地方了。/var/mobile/Containers/Data/Application/这个目录，普通的app是没有足够的全项访问的。需要申请特殊的权限，直接让cursor创建权限申请的Entitlements：

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <!-- 基本权限 -->
    <key>application-identifier</ke...