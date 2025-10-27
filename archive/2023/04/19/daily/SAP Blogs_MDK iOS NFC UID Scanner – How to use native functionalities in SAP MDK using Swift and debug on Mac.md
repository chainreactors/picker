---
title: MDK iOS NFC UID Scanner – How to use native functionalities in SAP MDK using Swift and debug on Mac
url: https://blogs.sap.com/2023/04/18/mdk-ios-nfc-uid-scanner-how-to-use-native-functionalities-in-sap-mdk-using-swift-and-debug-on-mac/
source: SAP Blogs
date: 2023-04-19
fetch_date: 2025-10-04T11:34:14.124017
---

# MDK iOS NFC UID Scanner – How to use native functionalities in SAP MDK using Swift and debug on Mac

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* MDK iOS NFC UID Scanner - How to use native functi...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160681&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [MDK iOS NFC UID Scanner - How to use native functionalities in SAP MDK using Swift and debug on Mac](/t5/technology-blog-posts-by-members/mdk-ios-nfc-uid-scanner-how-to-use-native-functionalities-in-sap-mdk-using/ba-p/13553764)

![robbewuyts](https://avatars.profile.sap.com/f/0/idf035903edfb0ddd8545f5e45d4b0f0209ccc48d04a0cc9ad158113ca908f7f75_small.jpeg "robbewuyts")

[robbewuyts](https://community.sap.com/t5/user/viewprofilepage/user-id/139223)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160681)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160681)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553764)

‎2023 Apr 18
10:01 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160681/tab/all-users "Click here to see who gave kudos to this post.")

2,266

* SAP Managed Tags
* [SAP Mobile Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Services/pd-p/668874921104038800958643358380369)
* [mobile development kit client](https://community.sap.com/t5/c-khhcw49343/mobile%2520development%2520kit%2520client/pd-p/73555000100800001081)

* [SAP Mobile Services

  Software Product Function](/t5/c-khhcw49343/SAP%2BMobile%2BServices/pd-p/668874921104038800958643358380369)
* [mobile development kit client

  SAP Business Technology Platform](/t5/c-khhcw49343/mobile%2Bdevelopment%2Bkit%2Bclient/pd-p/73555000100800001081)

View products (2)

**Introduction**

In this blog I’ll demonstrate how you can add native code/functionalities to your SAP MDK project. Most requirements can be solved using the NativeScript plugins, like in this [tutorial](https://developers.sap.com/tutorials/cp-mobile-dev-kit-nativescript-geolocation.html). For our use case however, NativeScript alone, couldn’t provide the solution we needed. To tackle this limitation, you can create a Swift Class in Xcode and call it from an MDK app.

**Use case**

We want to read NFC tags, more specifically the NFC UID. This guaranties us that we read the ID from the tag that is unique in the world and cannot be overwritten. This UID will be saved in the Equipment (PM) master data. (not part of this tutorial)

*![](/legacyfs/online/storage/blog_attachments/2023/04/NFC-tags-2.jpg)*

*Why not use the NDEF messages?*

*We have about 15.000 NFC tags and the end users solely use iPhones. Writing NDEF messages, and locking the NFC tag afterwards using NativeScript alone is not possible (at least with available NPM packages that I could find) on iOS. [NativeSctript NFC GitHub](https://github.com/EddyVerbruggen/nativescript-nfc)*

**Prerequisites (iOS)**

If you want to debug your Swift code, you’ll need:

* A Mac with Xcode installed

* An Apple Developer Program account (Paid) -  needed for NFC reading

* Install all SDK dependencies: [Tutorial](https://developers.sap.com/tutorials/cp-mobile-dev-kit-build-client.html)

**Tutorial/Code**

The folder structure with all the needed files for the MDK client build will look like this:

```
NFCScanning.mdkproject/

┣ App_Resources/

┃ ┣ Android/

┃ ┃ ┗ src/

┃ ┃   ┗ main/

┃ ┗ iOS/

┃   ┣ src/

┃   ┃ ┗ NFCScanningControllerBridge.swift

┃   ┗ app.entitlements

┣ App_Resources_Merge/

┃ ┗ iOS/

┃   ┗ Info.plist

┣ extensions/

┣ BrandedSettings.json

┗ MDKProject.json
```

[Github](https://github.com/robbewuytsTVC/MDKNFCScanning)

Create a Swift class (**NFCScanningControlBridge.swift**) that reads an NFC tag UID and sends it back to the caller using a callback function:

```
import UIKit

import CoreNFC

@objc(NFCScanningControlBridge)

public class NFCScanningControlBridge: NSObject,  NFCTagReaderSessionDelegate {

    var session: NFCTagReaderSession?

    @objc public var onNFCFoundCallback: ((String) -> Void)? = nil

    public override init() {

        super.init()

        CaptureNFC()

    }

    @objc public func CaptureNFC() {

        print("CaptureNFC");

        self.session = NFCTagReaderSession(pollingOption: .iso14443, delegate: self)

        self.session?.alertMessage = "Hold Your Phone Near the NFC Tag"

        self.session?.begin()

    }

    public func tagReaderSessionDidBecomeActive(_ session: NFCTagReaderSession) {

        print("Session Begun!")

    }

    public func tagReaderSession(_ session: NFCTagReaderSession, didInvalidateWithError error: Error) {

        print("Error with Launching Session")

    }

    public func tagReaderSession(_ session: NFCTagReaderSession, didDetect tags: [NFCTag]) {

        if tags.count > 1{

            session.alertMessage = "More Than One Tag Detected, Please try again"

            session.invalidate()

        }

        let tag = tags.first!

        session.connect(to: tag) { (error) in

            if nil != error{

                session.invalidate(errorMessage: "Connection Failed")

            }

            if case let .miFare(sTag) = tag{

                let UID = sTag.identifier.map{ String(format: "%.2hhx", $0)}.joined()

                print("UID:", UID)

                print(sTag.identifier)

                session.invalidate()

                // Use main thread

                DispatchQueue.main.async {

                    self.onNFCFoundCallback?(UID);

                }

            }

        }

    }

}
```

Give permission to read NFC Tags, by adding the **app.entitlements** file.

```
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">

<dict>

	<key>com.apple.developer.nfc.readersession.formats</key>

	<array>

		<string>NDEF</string>

		<string>TAG</string>

	</array>

</dict>

</plist>
```

Add the iOS properties file (**Info.plist**) This file contains critical information about the configuration of an iOS mobile app. We add the NFC reader usage description.

**BEWARE**: this file is added in the App\_Resouces\_Merge folder. This is needed because the SAP MDK app will also generate this file, which we don’t want to overwrite. Therefore SAP has foreseen this overriding mechanism: [Overriding App Resources - SAP Mobile Services Documentation](https://help.sap.com/doc/f53c64b93e5140918d676b927a3cd65b/Cloud/en-US/docs-en/guides/getting-started/mdk/custom-client/app-resources-merge.html)

```
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">

<dict>

	<key>NFCReaderUsageDescription</key>

	<string>core</string>

</dict>

</plist>
```

Use the Swift class in the MDK app (in this case in the Scan.js rule)

```
/**

 * Describe this function...

 * @param {IClientAPI} clientAPI

 */

export default function Scan(clientAPI) {

  try {

    // Create instance native iOS nfc scanning class

    var _iOSNFCScanControl = NFCSc...