---
title: Tracking iOS App Installs and Purchase History with StoreUser DB
url: https://www.stark4n6.com/2025/04/tracking-ios-app-installs-and-purchase.html
source: Instapaper: Unread
date: 2025-04-20
fetch_date: 2025-10-06T22:04:14.798155
---

# Tracking iOS App Installs and Purchase History with StoreUser DB

[Skip to main content](#main)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKbEuDpbWt2h4R7y02WrWiCmAG90SxVmMkXsEXZE0k3gAACuFYgfUVuTHkKpfowS3WWbkh6XGjqMXh77QkxuZv0osjeusHJnR_ehrMU9r8RaAa3a2R61zmMgl3wLsGpQxSh7rCRX4oQEM/s1600/1947245.png)

Search

### Search This Blog

### Tracking iOS App Installs and Purchase History with StoreUser DB

Posted by

[Kevin Pagano](https://www.blogger.com/profile/13417965550116928863 "author profile")

[April 14, 2025](https://www.stark4n6.com/2025/04/tracking-ios-app-installs-and-purchase.html "permanent link")

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk62xlG7jisj2T8atI2rnVHq2jM_H14lNINv9r00w6IzW5CXXlmxHPsfrT8C_-pXdlZXGo4hfGgq2wqz_oyYPPlIboH-sMNamJezQOEEVSjOeT9WApzoquUJ47vDub8TsTE8R8pE0HQmyeL_uRsrkHlp_2rk4_ZKa93vncA_5-NR-HrwtrRe4yW3LalBM/w632-h640/storeuser.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk62xlG7jisj2T8atI2rnVHq2jM_H14lNINv9r00w6IzW5CXXlmxHPsfrT8C_-pXdlZXGo4hfGgq2wqz_oyYPPlIboH-sMNamJezQOEEVSjOeT9WApzoquUJ47vDub8TsTE8R8pE0HQmyeL_uRsrkHlp_2rk4_ZKa93vncA_5-NR-HrwtrRe4yW3LalBM/s509/storeuser.png)

In my ongoing hunting for new(ish) research to blog about I recently came across a database on iOS that I couldn't find much info on in the wider community. As briefly touched on from Mattia ([read his blog here](https://blog.digital-forensics.it/2023/12/has-user-ever-used-xyz-application-aka.html)) the storeUser.db contains details on app installs and purchases from the app store. From the full file system extraction the database lives at path:

/private/var/mobile/Library/Caches/com.apple.appstored/storeUser.db\*

I have seen variations of the amount of tables from across different iOS versions but generally the two tables of interest are:

* **current\_apps** - A list of the current apps installed on the phone, including versioning history
* **purchase\_history\_apps** - A list of purchased apps from the app store, TBD if these have to be installed locally to show here

## Current Apps

Here we get generalized information regarding the apps that are installed on the device, including bundle ID's, name, timestamp of installation, app version (including entries for multiple versions of the same app).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhHcNW_xXt4JeYg329yxqA7NtFVs1f_BNWKJp1GHJT5lOUjKvPq_iF3tfrxrmDgh3JhRQhWUV2thFeGlkftDqv-VmqvPDl8_xD7a-zXrIDbFzsaC38c5RdoxjG93WNfbXZl_3F5xMhMtHd5MS6ekNqHQwXJAiQgy6ZJ6tOMf3KHbexM3249n7VWZQjaYqM=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhHcNW_xXt4JeYg329yxqA7NtFVs1f_BNWKJp1GHJT5lOUjKvPq_iF3tfrxrmDgh3JhRQhWUV2thFeGlkftDqv-VmqvPDl8_xD7a-zXrIDbFzsaC38c5RdoxjG93WNfbXZl_3F5xMhMtHd5MS6ekNqHQwXJAiQgy6ZJ6tOMf3KHbexM3249n7VWZQjaYqM)

*Figure 1: current\_apps table query from Josh Hickman's iOS 17 image*

We do get a deletion date column but I have not seen that with any data in all my test images so far.

If we focus on the GETTR app, we can see that the install date aligns nicely with Josh's image creation documentation (his date is local vs. UTC in the DB).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiP9t05NoHVKOIOH4xuZCBoSY57_rN9BbZuawlmSckY1ldncNqKhbvWAaWX7czAnsO9ljaien3A2_V7Pt-G-TYfc9bIlkQvWkaMAoNbBLcwMBZopY2MX9hjkeQw2PW1QRdUaj-XvEYDjT_7Wsqz6UMPoj8m6gvsyKtMyBRQDZsmcSv_bhlOpWC6Iv-doZs=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEiP9t05NoHVKOIOH4xuZCBoSY57_rN9BbZuawlmSckY1ldncNqKhbvWAaWX7czAnsO9ljaien3A2_V7Pt-G-TYfc9bIlkQvWkaMAoNbBLcwMBZopY2MX9hjkeQw2PW1QRdUaj-XvEYDjT_7Wsqz6UMPoj8m6gvsyKtMyBRQDZsmcSv_bhlOpWC6Iv-doZs)

*Figure 2: GETTR info from Josh's image creation documentation*

Having historical versioning of app installs can be helpful in possibly tracing how long the device had been utilizing a specific app and tracking down times when a specific version might have been used if there is a need to test/recreate scenarios.

## Purchase History Apps

In this table we get more information about apps that were purchased from the Apple App Store. While this might not mean they were directly installed on the device they can be associated with an ender user account.

There is a column for a flag if the app was hidden from the Springboard which seems to suggest this might be a list of apps on the device itself, but I know there are times when you're setting up a new device they don't always download and have an iCloud download icon next to it. My understanding is that family shared apps would show here too.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjn2uOOlXrjibhndeOB2EaWLgrZ9nKxxYEs80wwNhZM_Sf4DZUWacnlnlGTBPm1aSym38MjND70NUuq7BbxTk45OAQWlBoV7myfbaCQkxlnM6rcbVgJ62TnamYSd_Ofd6OFshRYTnvYwgzSl9-8CLgbfjeQ1d3EvgODlQvqHeKaiUamDWU-BfQPPHFgt6A=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjn2uOOlXrjibhndeOB2EaWLgrZ9nKxxYEs80wwNhZM_Sf4DZUWacnlnlGTBPm1aSym38MjND70NUuq7BbxTk45OAQWlBoV7myfbaCQkxlnM6rcbVgJ62TnamYSd_Ofd6OFshRYTnvYwgzSl9-8CLgbfjeQ1d3EvgODlQvqHeKaiUamDWU-BfQPPHFgt6A)

*Figure 3: purchase\_history\_apps query from Josh's iOS 17 image*

Parsers have been added to the latest [iLEAPP codebase](https://github.com/abrignoni/iLEAPP), please test it out and let me know!

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgO2qj_l-dfWX9GX_5pYEgfLYw45n1FO8Zs_aAt8X4y08FcaskmLgDwJagbtjX3bgk0rw5XY3RVgAOA8Z5w2CX6eL070MmKLC4dZdeIaQ6FqZoLM4muAWiGB_D7pHNwqHwvW6rml13sxlvYLoJ0Nt5qNHYotlWkiDxQKKUIMyNyF9HkN0Le2--WHn_mSo8=w400-h171)](https://blogger.googleusercontent.com/img/a/AVvXsEgO2qj_l-dfWX9GX_5pYEgfLYw45n1FO8Zs_aAt8X4y08FcaskmLgDwJagbtjX3bgk0rw5XY3RVgAOA8Z5w2CX6eL070MmKLC4dZdeIaQ6FqZoLM4muAWiGB_D7pHNwqHwvW6rml13sxlvYLoJ0Nt5qNHYotlWkiDxQKKUIMyNyF9HkN0Le2--WHn_mSo8)

[app store](https://www.stark4n6.com/search/label/app%20store)
[Apple](https://www.stark4n6.com/search/label/Apple)
[iOS](https://www.stark4n6.com/search/label/iOS)
[sqlite](https://www.stark4n6.com/search/label/sqlite)
[storeUser](https://www.stark4n6.com/search/label/storeUser)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_rv98XOSpQWTx_-D_OwQHINXes6_8Q4J2QRmauiB7JMXfh6dp50JzZY1zhNlD0O0yYr01eKAj2jcAFv1S06jcx2ifxvmj1Pm18gESACkCmMdSldHhX_EO_prxaQJoeQ6FuCjeXLNkb0g/s150/FullColor_1024x1024_300dpi.jpg)

### Archive

* [September 20251](https://www.stark4n6.com/2025/09/)
* [August 20251](https://www.stark4n6.com/2025/08/)
* [July 20254](https://www.stark4n6.com/2025/07/)
* [June 20252](https://www.stark4n6.com/2025/06/)
* [April 20252](https://www.stark4n6.com/2025/04/)
* [March 20259](https://www.stark4n6.com/2025/03/)
* [February 20251](https://www.stark4n6.com/2025/02/)
* [January 20252](https://www.stark4n6.com/2025/01/)
* [December 20242](https://www.stark4n6.com/2024/12/)
* [October 20241](https://www.stark4n6.com/2024/10/)

* [May 20241](https://www.stark4n6.com/2024/05/)
* [April 20242](https://www.stark4n6.com/2024/04/)
* [March 20244](https://www.stark4n6.com/2024/03/)
* [February 20241](https://www.stark4n6.com/2024/02/)
* [January 20243](https://www.stark4n6.com/2024/01/)
* [December 20231](https://www.stark4n6.com/2023/12/)
* [October 20233](https://www.stark4n6.com/2023/10/)
* [September 20232](https://www.stark4n6.com/2023/09/)
* [August 20232](https://www.stark4n6.com/2023/08/)
* [July 20231](https://www.stark4n6.com/2023/07/)
* [June 20232](https://www.stark4n6.com/2023/06/)
* [May 20235](https://www.stark4n6.com/2023/05/)
* [April 20232](https://www.stark4n6.com/2023/04/)
* [March 20236](https://www.stark4n6.com/2023/03/)
* [February 20231](https://www.stark4n6.com/2023/02/)
* [January 20232](https://www.stark4n6.com/2023/01/)
* [December 20223](https://www.stark4n6.com/2022/12/)
* [November 20222](https://www.stark4n6.com/2022/11/)
* [October 20221](https://www.stark4n6.com/2022/10/)
* [September 20222](https://www.stark4n6.com/2022/09/)
* [August 20223](https://www.stark4n6.com/2022/08/)
* [June 20228](https://www.stark4n6.com/2022/06/)
* [May 20...