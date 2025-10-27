---
title: Embedding Frida in iOS TestFlight Apps
url: https://naehrdine.blogspot.com/2023/02/embedding-frida-in-ios-testflight-apps.html
source: cat /dev/brain
date: 2023-02-16
fetch_date: 2025-10-04T06:48:48.179945
---

# Embedding Frida in iOS TestFlight Apps

[Skip to main content](#main)

### Search This Blog

# [cat /dev/brain](https://naehrdine.blogspot.com/)

Reverse Engineering & Research

### Embedding Frida in iOS TestFlight Apps

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[February 15, 2023](https://naehrdine.blogspot.com/2023/02/embedding-frida-in-ios-testflight-apps.html "permanent link")

Learning reverse engineering on mobile devices can be challenging, especially on iOS, where tooling is less accessible than on Android. On YouTube, I published various [videos on reverse engineering with Frida](https://youtube.com/%40jiskac), which is a tool for dynamic reverse engineering of applications during runtime. Last year, I started giving public reversing trainings via BlackHoodie and the university I'm teaching at, along with a training at [NULLCON Berlin](https://nullcon.net/berlin-2023/training/mobile-reversing-and-security-analysis/) in March. While starting off with a focus on Android, which can easily be virtualized and rooted, knowledge on iOS reversing is a rare resource that many people want to learn about. But how can we make iOS reversing more accessible to learn, in a world dominated by closed-source tooling and strictly controlled by Apple?

Frida can be used on iOS without any jailbreak. Especially when building your own apps, adding it for educational purposes and using it on your own iPhone can be fun. In this blog post, we'll look into two options: (1) Distributing debug builds directly to other phones as well as (2) distributing the app via TestFlight.

Distributing debug builds is challenging, as Apple tremendously limits sideloading, meaning options to distribute your own apps without App Store. Personal (free) developer accounts have a limit of signing 8 apps in total, with no more than 3 apps per device. But also paid developer accounts have a limit of 100 devices. While this number sounds high, when considering to share an app with students in a 2-day training setting multiple times a year, the 100 devices will be reached quickly. When using a virtual device with Corellium, one can simply change a device's ECID, thereby only using up one device no matter to how many people an app is shared. Especially when not having a pile of iPhones at hand, this is probably the best option for a training. But when on a budget and assuming that some students will bring their own iPhone, one might want to explore other possibilities. Especially at SEEMOO, we already have a pile of research phones, with some of them on recent versions laying around and waiting for the next jailbreak release... which we could probably used for a mobile reversing training, but how?

|  |
| --- |
| [![pile_of_phones.jpeg](https://blogger.googleusercontent.com/img/a/AVvXsEjY1QuTHUuNMaUhtPMwZUaK2DZSUeZkIJhRzx8QRnrGkdXQUFQEe9bYNGPvZYlHp4_U2ldtxijCUy8DoO_5UqFvzrXEjcYYFlDdaPGEi5HjHyKnIIZ1EoiA5mDax5Ot_weLaEU7K298v9O17LcDU3mB-gMf0_klKgkmUCDnpWkVd0N7atWVH9eU-Llb)](https://blogger.googleusercontent.com/img/a/AVvXsEjY1QuTHUuNMaUhtPMwZUaK2DZSUeZkIJhRzx8QRnrGkdXQUFQEe9bYNGPvZYlHp4_U2ldtxijCUy8DoO_5UqFvzrXEjcYYFlDdaPGEi5HjHyKnIIZ1EoiA5mDax5Ot_weLaEU7K298v9O17LcDU3mB-gMf0_klKgkmUCDnpWkVd0N7atWVH9eU-Llb) |
| pile\_of\_phones.jpeg - a very realistic problem, as you can see. |

Of course, an app with built-in Frida functionality would probably not make it into the App Store. But there's TestFlight, where apps can be shared to a group of people for testing purposes. Apps shared via TestFlight expire after 90 days, which is perfectly fine for this use case.

## Option 1: Debug Build via TrollStore/AltStore

When the app is a debug build and the Development Disk Image is mounted, Frida can list processes and add to debuggable processes even *without* jailbreak. Debug builds can be created directly with Xcode for a specific device.

Distribution via TrollStore/AltStore requires exporting the debug build app. This can be done by exporting it from the Xcode debug build directory and packing this as a developer-signed app. The app then needs to be re-signed when distributing it to another iPhone.

**Without archiving**, build an iPA from the intermediate compilation as follows:

Figure out the Product folder by clicking `Products` in the left pane of Xcode. For my `Test.app`, the `Full Path` is `/Users/test/Library/Developer/Xcode/DerivedData/Test-*/Build/Products/Debug-iphoneos/Test.app`.

```
cd ...Build/Products/Debug-iphoneos/
mkdir Payload
cp -r Test.app Payload
zip -r Test_unsigned_debug.ipa Payload
```

Upload the app to iCloud or share via USB stick when using TrollStore/AltStore, copy to the phone, and then share app to TrollStore/AltStore. When using AirDrop, iOS can't store the app on Files, even though it offers to do so.

**This works!! Why?**

A debug build will work with Frida, as it has a special entitlement to allow debuggers to attach to it, called get-task-allow.

Everything else essentially doesn't work.

Archiving with a Distribution certificate will strip the `get-task-allow` attribute from the entitlements, as a distribution certificate is not allowed to sign this entitlement. This means, this entitlement won't be allowed during distribution via TestFlight/AppStore. Removing `get-task-allow` allows other processes attaching to the app's task port, a rather dangerous setting in practice. Removing it from a build effectively disables `debugserverd` from attaching a debugger to the app. Archiving the app will always remove the `get-task-allow` entitlement, also on debug builds. This is a neat trick to prevent developers from accidentally distributing debuggable apps, but in our case, this is essential to get Frida running, as it is internally using debugging APIs.

Distribution of debug builds is limited via the included embedded.mobileprovision file inside the app. They can only be installed on designated devices associated with the developer's account.

On a jailbroken device, app signature checks on iOS can be bypassed using [AppSync](https://github.com/akemin-dayo/AppSync) and installing the app with ios-deploy from the debug app folder Test.app. But not every device can be jailbroken.

## Option 2: Frida Gadget via TestFlight

As long as you have an iPhone setup where you can debug your own apps, you'll also be able to debug these apps with Frida. There's no need to inject a `FridaGadget.dylib` into your own app when debugging is allowed.

However, as we can't distribute debug builds with debug permission via TestFlight, we can also distribute a binary with a built-in gadget. This should *not* be run on a jailbroken iPhone, as Frida doesn't detect double injection. In my tests it was working nonetheless, but better make sure to not combine jailbreak + gadget.

**Rebuild gadget** without private APIs. Any usage of private APIs will block the app from TestFlight.

Build `frida` with the following `config.mk` from source:

```
# Include jailbreak-specific integrations
FRIDA_JAILBREAK ?= disabled
```

Create `frida-cert` and then run `make frida-ios`.

The non-jailbreak dylib will be in `build/frida-ios-arm64/usr/lib/frida/frida-gadget.dylib`.

**Library to Framework conversion.**

Without distribution via TestFlight, we could simply include the FridaGadget.dylib into the Frameworks folder. However, App Store Connect checks prior distribution in TestFlight will prevent any dylib not starting with libSwift from being located directly in the Frameworks folder. Instead, there must be a Framework subfolder. While xcodebuild can create an xcframework from a dylib library, this would again end up in the main Frameworks folder after archiving. *(Edit:)* I'm using lipo here, but it might also be sufficient to just rename the library. The error message is rather unspecific, telling us the libSwift dylibs weren't located in the Frameworks folder, but they are (ITMS-90429) and the check for that only happens after the App Store Connect upload.

```
lipo -create FridaGadget.dylib -output Frida
codesign --remov...