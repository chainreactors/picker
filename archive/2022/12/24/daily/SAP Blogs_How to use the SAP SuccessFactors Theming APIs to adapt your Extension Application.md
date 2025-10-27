---
title: How to use the SAP SuccessFactors Theming APIs to adapt your Extension Application
url: https://blogs.sap.com/2022/12/23/how-to-use-the-sap-successfactors-theming-apis-to-adapt-your-extension-application/
source: SAP Blogs
date: 2022-12-24
fetch_date: 2025-10-04T02:25:18.429315
---

# How to use the SAP SuccessFactors Theming APIs to adapt your Extension Application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* How to use the SAP SuccessFactors Theming APIs to ...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5975&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to use the SAP SuccessFactors Theming APIs to adapt your Extension Application](/t5/human-capital-management-blog-posts-by-sap/how-to-use-the-sap-successfactors-theming-apis-to-adapt-your-extension/ba-p/13558353)

![gerald_reinhard](https://avatars.profile.sap.com/2/1/id219c98e8e7f444abd7a8316c92f1a6a64ccaca537943bb6f3f917988ac6af7ed_small.jpeg "gerald_reinhard")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[gerald\_reinhard](https://community.sap.com/t5/user/viewprofilepage/user-id/14828)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5975)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5975)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558353)

‎2022 Dec 23
4:11 PM

[1
Kudo](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5975/tab/all-users "Click here to see who gave kudos to this post.")

1,612

* SAP Managed Tags
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)

View products (3)

The Theming of the SAP SuccessFactors system can be managed using the [Theme Manager](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/1062532103004fdca0969f59297e1aae/2fe2d1ebd32d49ecacb78c1337a83c2c.html?q=Theme%20Manager&locale=en-US).

This Theme manager allows to define own themes or select preselected themes for the product. Customer use this functionality to adapt the look and feel of the product to their corporate colors and logos.

![](/legacyfs/online/storage/blog_attachments/2022/12/ThemeManagerOverview-Screenshot-2022-12-23-163619.png)

When Partner or Customers are building an extension application to the SAP SuccessFactors products there is often the need to apply the same theming to the extension. The good news is that all this Theming information is stored within the product and is accessible to a series of APIs.

In this blog post I will show how to retrieve this information based on the example of the company logo which can be set in the Theme Manager using the fine tuning logo section as shown below

![](/legacyfs/online/storage/blog_attachments/2022/12/ThemeManager-Screenshot-2022-12-23-163619.png)

The SAP SuccessFactors [Theming APIs](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/28bc3c8e3f214ab487ec51b1b8709adc/d8c5d8e76fb840a3a7d159fcf21ac467.html?q=Theming%20API&locale=en-US) are documented in the OData V2 Reference Guide and the first API to know is the ThemingInfo API. This API will return the ID of the current selected Theme in the Theme Manager.

```
GET https://api68sales.successfactors.com/odata/v2/ThemeInfo?$format=JSON
```

The result of this API looks like this:

```
{

    "d": {

        "results": [

            {

                "__metadata": {

                    "uri": "https://api68sales.successfactors.com/odata/v2/ThemeInfo('11uyoqg2t8')",

                    "type": "SFOData.ThemeInfo"

                },

                "id": "11uyoqg2t8",

                "ui5Theme": "sap_fiori_3",

                "urls": {

                    "baseUrl": "https://hcm68sales.successfactors.com",

                    "configUrl": "/public/theme-api/config/SFPRO001234/11uyoqg2t8;mod=1853f8061b1",

                    "cssUrl": "/public/theme-api/css/SFPRO001234/11uyoqg2t8/.dcss;mod=1853f8061b1",

                    "ui5BaseThemeRootUrl": "/public/theme-api/css/SFPRO001234/11uyoqg2t8/.dcss/merge_v1/verp/ui/sapui5-aux/resources_1.1.27/theming!/verp/ui/sapui5-main/resources_1.102.6/resources/"

                },

                "lastModifiedDate": "1671807656369",

                "accessibilityPreferences": {

                    "blindnessSupport": false,

                    "colorVisionType": null,

                    "keyboardOnlyNavigation": false,

                    "lowVisionType": null

                },

                "locale": "en_US",

                "modules": null,

                "fingerprints": {

                    "config": "1853f8061b1",

                    "css": "1853f8061b1",

                    "ui5BaseThemeRoot": "v1"

                }

            }

        ]

    }

}
```

With the id from the above response of the API the next API can be called which is the ThemingConfig API:

```
GET https://api68sales.successfactors.com/odata/v2/ThemeConfig('11uyoqg2t8')?$format=JSON
```

This API returns all the information provided in the Theme Manager including the URL to company Logo:

```
"logo": {

                "backdropColor": {

                    "value": "#FFFFFF"

                },

                "position": "left",

                "url": {

                    "value": "uires:638?mod=dcc48fc2b3b390735e7673714fe66323&name=sap%2dlogo%2dpng%5f2285421small.png"

                },

                "useBackdrop": false,

                "useUploadedLogo": true

            },
```

This information together with the URLs for the UI resources (uires) which is the UI URL of the SuccessFactors system plus "public/ui-resources/<company ID>"

```
https://hcm68sales.successfactors.com/public/ui-resource/SFPRO001234/
```

can be used to retrieve the Logo of the company. By appending the value of the "url" parameter from the response of the ThemingConfig API (excluding the "uires:" part):

```
https://hcm68sales.successfactors.com/public/ui-resource/SFPRO001234/638;mod=dcc48fc2b3b390735e76737...
```

The above URL can be used without any additional authentication from any application which needs the company logo. Please note that if you copy the above URL you will not get the logo since in all examples above the company ID was replaced by a fake one.

In a similar fashion all other resources can be accessed or CSS information extracted to apply it to your extension application.

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [Implementation design principles for SuccessFactors Solutions](/t5/tag/Implementation%20design%20principles%20for%20SuccessFactors%20Solutions/tg-p/board-id/hcm-blog-sap)
* [SFIDPs](/t...