---
title: Exploring Apple Intelligence Artifacts in iOS
url: https://dig-fo4-6.blogspot.com/2026/03/exploring-apple-intelligence-artifacts.html
source: Instapaper: Unread
date: 2026-03-23
fetch_date: 2026-03-24T04:18:07.277107
---

# Exploring Apple Intelligence Artifacts in iOS

[Skip to main content](#main)

### Search This Blog

# [HK\_Dig4nsics](https://dig-fo4-6.blogspot.com/)

### Exploring Apple Intelligence Artifacts in iOS

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[March 22, 2026](https://dig-fo4-6.blogspot.com/2026/03/exploring-apple-intelligence-artifacts.html "permanent link")

In 2024, Apple introduced Apple Intelligence during Apple Worldwide Developers Conference 2024, describing it as a new AI system integrated into iOS, iPadOS, and macOS. This represented a progression beyond the capabilities previously associated with Siri, expanding the system’s ability to use contextual information from the device.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgZySm373AZcKP_p6iQIQGM16MzJy0Ok5wTsm2Qu60VPEn8eHX5wNMjvdNuIJD4KVnJOYqBgUAD7eqiThU_O8pUAyuwW9NZNhWz78rHTPJ7tk7xubiFuNF_hA6uF8O5HEvqYuef9kJlSX9RHLz-ds56UazYptwDao3dRHEx3oZsSpD6Iac1hgS1gN9oTOo=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgZySm373AZcKP_p6iQIQGM16MzJy0Ok5wTsm2Qu60VPEn8eHX5wNMjvdNuIJD4KVnJOYqBgUAD7eqiThU_O8pUAyuwW9NZNhWz78rHTPJ7tk7xubiFuNF_hA6uF8O5HEvqYuef9kJlSX9RHLz-ds56UazYptwDao3dRHEx3oZsSpD6Iac1hgS1gN9oTOo)

Apple states on its Apple Intelligence [page](https://www.apple.com/apple-intelligence/) that the system is “aware of your personal information without collecting your personal information.” With this in mind, I wanted to review artifacts in an iOS filesystem extraction to determine how Apple Intelligence data might be useful in an iOS forensic investigation.

I did not have a suitable dataset for testing until Magnet CTF 2026. I would like to thank Magnet Forensics for hosting the event and providing the data used in this research. I would also like to thank [Jessica Hyde](https://www.linkedin.com/in/hydejessica/) and her team for the tremendous work they put into creating the dataset and challenges.

As part of the CTF, an iPhone 15 full filesystem extraction was provided. The extraction contained artifacts related to the **Apple Intelligence Platform (AIP)**. Artifacts associated with the AIP were located in:

***/private/var/mobile/Library/IntelligencePlatform/***

The dominant artifact format within this directory is SQLite databases, which appear to store data used by Apple Intelligence to build and maintain its internal knowledge.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjwsX_c9PKiXNc5h9IecIJT4W5fMh20s86bTKcbJran0eS6v7bBG9RkS3Vh9SrbJKTM8HT5LeQfqRabL-Lo1pYFmJ-re80JaVqOEeOpsUpVCwSytwAXQuS1rBUOetoDoop2M7e8paOqaeRrUeRoxWayNaSTJBEsSiEi-BbeR94YMsaf9BtaiAFH6NfS1dk=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjwsX_c9PKiXNc5h9IecIJT4W5fMh20s86bTKcbJran0eS6v7bBG9RkS3Vh9SrbJKTM8HT5LeQfqRabL-Lo1pYFmJ-re80JaVqOEeOpsUpVCwSytwAXQuS1rBUOetoDoop2M7e8paOqaeRrUeRoxWayNaSTJBEsSiEi-BbeR94YMsaf9BtaiAFH6NfS1dk)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjKwEXjul_T2YRO14HHbEOXVTeIPeR4taohbapZLGqy4tRSTbMVWe_CeL3DZyeNKBlT89lZdY9mYx0mry_H7xx-mbW6x83csqEfrS5BcFQFy3g4Cw7jrGdsGPYwYcZbVPyv1XZELzKeMyJqlVL00OXb_BRR6dCQhtqxls_j29NxfU2ZXBJ1fjJshEIbkxU=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjKwEXjul_T2YRO14HHbEOXVTeIPeR4taohbapZLGqy4tRSTbMVWe_CeL3DZyeNKBlT89lZdY9mYx0mry_H7xx-mbW6x83csqEfrS5BcFQFy3g4Cw7jrGdsGPYwYcZbVPyv1XZELzKeMyJqlVL00OXb_BRR6dCQhtqxls_j29NxfU2ZXBJ1fjJshEIbkxU)

Figure 1. Screenshots of the AIP directory and subdirectories (FTK Imager)

One of the first confirmations that Apple Intelligence references personal device information was found in ***graph.db***. Within this database, the ***translated*** table contained entries representing a location labeled “***home***.” The entries included a full street address along with latitude and longitude coordinates. The final column in the table stores timestamps.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjxO6sEzBba6GFHpZy5Isgilxa7rF9c92PrylMuxVjENveFmzgMBwFjcwvdgozjKZYOISoYFkNlCiqvYRDtwA9MWZaikIELWqyZCUioXcAtJi-sYcAFXNSjSm1hyAWxaOmixhvd3fQcYGg3Zv1qGzmMu00zFNpAnnx8W_yBW1sANIe8mhxukV5g_Kp1vuw=w640-h184)](https://blogger.googleusercontent.com/img/a/AVvXsEjxO6sEzBba6GFHpZy5Isgilxa7rF9c92PrylMuxVjENveFmzgMBwFjcwvdgozjKZYOISoYFkNlCiqvYRDtwA9MWZaikIELWqyZCUioXcAtJi-sYcAFXNSjSm1hyAWxaOmixhvd3fQcYGg3Zv1qGzmMu00zFNpAnnx8W_yBW1sANIe8mhxukV5g_Kp1vuw)

Figure 2. Screenshot of the translated table in graph.db (FQLite)

All entries in the ***translated*** table contained timestamps that were nearly identical, differing only by microseconds.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj7HJa8r5WtV2KOzcQPRF7_4bE5BZMne_ZvFOCfPu9AwG7jwaQ8XExLTshlsP09frQOaFl8Q4Xkq3-H9KdRUsnEtpIqgbJAB2AZSyo7w72FxiFeoLxLAhznxbgTHdsWEhic5erdHbr-_Y507vN3TurvxL_X7O36Uzv4lM_MRuD1TI0--p-5xJShAi4Dfd8=w640-h522)](https://blogger.googleusercontent.com/img/a/AVvXsEj7HJa8r5WtV2KOzcQPRF7_4bE5BZMne_ZvFOCfPu9AwG7jwaQ8XExLTshlsP09frQOaFl8Q4Xkq3-H9KdRUsnEtpIqgbJAB2AZSyo7w72FxiFeoLxLAhznxbgTHdsWEhic5erdHbr-_Y507vN3TurvxL_X7O36Uzv4lM_MRuD1TI0--p-5xJShAi4Dfd8)

Figure 3. Screenshot of the ***timestamp*** column in the ***translated*** table in ***graph.db*** (FQLite)

The most interesting table identified during the initial review was the ***stable\_graph*** table within ***graph.db***. This table contained more than one thousand entries and appears to store relationships between entities used by the AIP.

Sorting the table by the ***subject*** column grouped related entries together. One group referenced an entity labeled “***SMS;-;6700***.” This appears to represent an entity associated with SMS communication involving the phone number ***6700***. The actual message content was not recorded in AIP artifacts; however, evidence of the communication was present in ***sms.db***.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgQ5C6QJCenYY35HveEj5Mg_eM7hq5vAkZ6429kHSM4srvYR9u9OwqZh_VWtuoi-gHelCg6wrlbaNChlnAXPw-Aht3xeMTZ56cPzAnEGu4MowfpCn70BIdktzdqDkwh34M9s7rSW7K_q8wDh5nMmr7hZ9zfTGm1hbVpeHCeHgifTH0DMzIt63BXg18OobA=w640-h187)](https://blogger.googleusercontent.com/img/a/AVvXsEgQ5C6QJCenYY35HveEj5Mg_eM7hq5vAkZ6429kHSM4srvYR9u9OwqZh_VWtuoi-gHelCg6wrlbaNChlnAXPw-Aht3xeMTZ56cPzAnEGu4MowfpCn70BIdktzdqDkwh34M9s7rSW7K_q8wDh5nMmr7hZ9zfTGm1hbVpeHCeHgifTH0DMzIt63BXg18OobA)

Figure 4. Screenshot of the ***stable\_graph*** table in ***graph.db*** (FQLite)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjdhxmC6VQr4II5gAuhZpMPaRBFbLF6yaLLDx9X0Mco5Acf8FHOusGTvX_syfjaMIY2JbQY4pXdPjQiR1q6iKilUZmD0MRdCNS8OH8noKkUTIFNL-FfGCgzWRm3mxQSAXKP_3FcL5aEwjZy48I65MCjd4nOFxbljmjqlmi-mEn0o1pOO8D7eb-AAAqhlmw=w640-h316)](https://blogger.googleusercontent.com/img/a/AVvXsEjdhxmC6VQr4II5gAuhZpMPaRBFbLF6yaLLDx9X0Mco5Acf8FHOusGTvX_syfjaMIY2JbQY4pXdPjQiR1q6iKilUZmD0MRdCNS8OH8noKkUTIFNL-FfGCgzWRm3mxQSAXKP_3FcL5aEwjZy48I65MCjd4nOFxbljmjqlmi-mEn0o1pOO8D7eb-AAAqhlmw)

Figure 5. Screenshot of SMS and iMessage communication (iLEAP)

As seen in Figure 4, the two entries highlighted in blue have predicate value of ***PS33***. The meaning of this value is not recorded in the ***graph.db***. I found the meaning of this predicate in the ***ontology.db*** database which can be found in the same directory as ***graph.db***. The ***predicate*** table of the ***ontology.d******b*** database lists the ***label*** for ***PS33*** as ***name***.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhZ5HqywA2fy1YPptYKYHw054QlPMWi1-EWv3MJal_skbcW1a4XLWWTq8DtebZ7zMvJKBtL48aXYLHH_eDu8vgkj8iZzNGBg0ax9tRytFMZ2-x_LnZ9zusc_Y0_TUht-ltOvepO2v1rGP7CXkU5WOjNeZDkjA9oqr_OETi58vzFwrGi9eD2ul0PY8kDNsU=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhZ5HqywA2fy1YPptYKYHw054QlPMWi1-EWv3MJal_skbcW1a4XLWWTq8DtebZ7zMvJKBtL48aXYLHH_eDu8vgkj8iZzNGBg0ax9tRytFMZ2-x_LnZ9zusc_Y0_TUht-ltOvepO2v1rGP7CXkU5WOjNeZDkjA9oqr_OETi58vzFwrGi9eD2ul0PY8kDNsU)

Figure 6. Screenshot of the ***predicate*** table in ***ontology.db*** (FQLite)

Further review of the ontology database showed that it also contains the labels for many other ***predicate*** and ***relationshipPredicate*** values observed in the ***stable\_graph...