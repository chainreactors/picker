---
title: Hunting Chromium Notifications
url: https://blog.nviso.eu/2024/09/06/hunting-chromium-notifications/
source: NVISO Labs
date: 2024-09-07
fetch_date: 2025-10-06T18:26:31.577879
---

# Hunting Chromium Notifications

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Hunting Chromium Notifications

[Maxime Thiebaut](https://blog.nviso.eu/author/maxime-thiebaut/ "Posts by Maxime Thiebaut")

[Forensics](https://blog.nviso.eu/category/forensics/), [Threat Hunting](https://blog.nviso.eu/category/threat-hunting/)

September 6, 2024September 5, 2024
4 Minutes

Earlier this year, NVISO identified an active cluster of domains likely tied to social engineering. Upon analysis, the domains masqueraded themselves as [CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA) verification pages, requesting visitors to press a button to verify they’re human.

![An Azure-hosted CAPTCHA phishing page requesting notification permissions.](https://blog.nviso.eu/wp-content/uploads/2024/01/image-33.png)

Figure 1: An Azure-hosted CAPTCHA phishing page requesting notification permissions.

While seasoned professionals may immediately recognize the page as fraudulent, less alert users might inadvertently provide their consent to notifications. Shortly after giving consent, the end-user would continuously receive browser-delivered phishing notifications.

![Browser-delivered phishing notifications.](https://blog.nviso.eu/wp-content/uploads/2024/01/image-34.png)

Figure 2: Browser-delivered phishing notifications.

As the hunt’s hypothesis assumed breach, we further hunted for traces of both successful social engineering and follow-on abuse. In the following sections we will present which forensic Chromium evidence can be found for initial social engineering (i.e., granted permissions) and follow-on interactions (i.e., delivered notifications, user interactions). Finally, we will cover how this hunt can be performed enterprise-wide through our contributed Velociraptor artifact and provide enterprise hardening recommendations to prevent such abuse.

This article focuses on Chromium-based web-browsers (e.g., Google Chrome, Microsoft Edge) as available telemetry scoped potential victims down to these browsers.

## Evidence

In this section we will cover which evidence allowed us to answer if a user had allowed websites to send notifications, had subsequently received notifications and, finally, interacted with the received notifications.

### Chromium User Preferences

The Chromium user preferences is a JSON file titled `Preferences` located within the user’s data directory. The file contains a flurry of settings, of which some pertaining to the notifications. For the two most prominent enterprise Chromium browsers (Google Chrome & Microsoft Edge), the locations are as follows:

|  |  |
| --- | --- |
| **Operating System** | **Standard Google Chrome Path** |
| Windows | `*:\Users\*\AppData\Local\Google\Chrome\User Data\*\Preferences` |
| MacOS | `/Users/*/Library/Application Support/Google/Chrome/*/Preferences` |
| Linux | `/home/*/.config/google-chrome/*/Preferences` |

Figure 3: Standard Google Chrome path for the user preferences.

|  |  |
| --- | --- |
| **Operating System** | **Standard Microsoft Edge Path** |
| Windows | `*:\Users\*\AppData\Local\Microsoft\Edge\User Data\*\Preferences` |
| MacOS | `/Users/*/Library/Application Support/Microsoft/Edge/*/Preferences` |
| Linux | `/home/*/.config/microsoft-edge/*/Preferences` |

Figure 4: Standard Microsoft Edge path for the user preferences.

#### Notifications

The `$.profile.content_settings.exceptions.notifications` dictionary contains the notification permissions attributed to websites. Each website with non-default permissions has its own entry with a `last_modified` and `setting` property.

```
{
    "https://bestclevercaptcha.azurewebsites.net:443,*": {
        "last_modified": "13349960779269787",
        "setting": 1
    }
}
```

JSON (Beatified)

The `last_modified` value is a variation of the Windows’ `[FILETIME](https://learn.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime)`. It represents the [number of microsecond intervals since January 1, 1601 UTC (as opposed to Windows’ 100-nanosecond)](https://github.com/chromium/chromium/blob/162defbaadf2a53e4820bd446eb0b2fa6fa31c9c/base/time/time.h#L507-L510). Conversion to the more common Linux-like timestamp can be achieved through the `(last_modified/1000000)-11644473600` formula (i.e., convert `last_modified` into seconds and remove the number of seconds between Linux’s `1970` and Windows’ `1601` epoch).

The `setting` property can be mapped to Chromium’s `ContentSetting` enum. In our case, a `setting` of value `1` indicates the website has the `CONTENT_SETTING_ALLOW` permission for notifications.

```
enum ContentSetting {
  CONTENT_SETTING_DEFAULT = 0,              // 0
  CONTENT_SETTING_ALLOW,                    // 1
  CONTENT_SETTING_BLOCK,                    // 2
  CONTENT_SETTING_ASK,                      // 3
  CONTENT_SETTING_SESSION_ONLY,             // 4
  CONTENT_SETTING_DETECT_IMPORTANT_CONTENT, // 5
  CONTENT_SETTING_NUM_SETTINGS
};
```

C

The `$.profile.content_settings.exceptions.notifications` object hence provides preliminary evidence on whether a user has set specific website notification permissions, and when this occurred. The object however represents the current permission state; If a user revoked/changed the assigned permissions, the previous states are not available.

#### Notification Interactions

The `$.profile.content_settings.exceptions.notification_interactions` dictionary contains metrics on issued and interacted notifications. As soon as a notification is issued or interacted with, the daily metrics are updated.

As was the case for the previously covered `notifications` object, the `notification_interactions` object contains per-URL keys as well as a `last_modified` property. The `setting` property is however a dictionary where the keys represent Linux-like timestamps (rounded to the day) and the `display_count` alongside `click_count` properties provide daily counters on the respective amount of displayed notifications and optional user-interacted notifications.

```
{
    "https://bestclevercaptcha.azurewebsites.net:443,*": {
        "last_modified": "13349960822063286",
        "setting": {
            "1704672000": {
                "click_count": 1,
                "display_count": 3
            },
            "1705449600": {
                "display_count": 1
            }
        }
    }
}
```

JSON (Beatified)

Together, the `notifications` and `notification_interactions` preferences provide sufficient...