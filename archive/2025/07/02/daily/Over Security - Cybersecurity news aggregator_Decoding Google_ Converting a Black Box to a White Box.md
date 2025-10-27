---
title: Decoding Google: Converting a Black Box to a White Box
url: https://brutecat.com/articles/decoding-google
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:55:58.702701
---

# Decoding Google: Converting a Black Box to a White Box

[< Back](/)

[< Back](/)

## Decoding Google: Converting a Black Box to a White Box

2024-11-01

![](/assets/decoding-google.jpeg)

We've all been there - staring at Google's search box, overwhelmed by the maze of complexity hiding behind that minimalist interface, thinking it's impossible to break in. The key to decoding Google? Converting the attack surface from a black box to a white box. The first step is finding all the endpoints that exist, and all of their respective parameters, especially ones that are hidden and aren't used in the actual app and were left from some developer testing, since they likely contain security bugs.
‎

#### Table of Contents

* [How Google API authentication works on the web](/articles/decoding-google#how-google-api-authentication-works-on-the-web)
* ["Secret" visibility labels](/articles/decoding-google#-quot-secret-quot-visibility-labels)
* [How Google API authentication works on Android](/articles/decoding-google#how-google-api-authentication-works-on-android)
* [A word on X-Goog-Spatula](/articles/decoding-google#a-word-on-x-goog-spatula)
* [Leaking request parameters through error messages](/articles/decoding-google#leaking-request-parameters-through-error-messages)
  ‎

In Google, there's something known as [discovery documents](https://developers.google.com/discovery/v1/reference/apis) that are essentially like swagger documents, intended for listing API methods on Google's public APIs such as their [YouTube Data API](https://developers.google.com/youtube/v3) ([discovery](https://youtube.googleapis.com/%24discovery/rest)). As it turns out, these discovery documents aren't just available for their public APIs but also for their private ones such as the Internal People API ([discovery](https://people-pa.googleapis.com/%24discovery/rest)).
‎

While this discovery document doesn't require any authentication to view, if we try fetching something like the Takeout Private API, we get the following error:
‎

**Request**

```
GET /$discovery/rest
Host: takeout-pa.googleapis.com
```

**Response**

```
HTTP/2 403 Forbidden
Content-Type: application/json; charset=UTF-8

{
  "error": {
    "code": 403,
    "message": "Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.",
    "status": "PERMISSION_DENIED"
  }
}
```

Thankfully, by looking into how Google authentication works, it's possible to get past this.

### How Google API authentication works on the web

If we look at a random request to the People Internal API to lookup a Google user from the web that we can find from DevTools on <https://chat.google.com>:

```
POST /$rpc/google.internal.people.v2.minimal.InternalPeopleMinimalService/GetPeople HTTP/2
Host: people-pa.clients6.google.com
Cookie: <redacted>
Content-Type: application/json+protobuf
X-Goog-Api-Key: AIzaSyB0RaagJhe9JF2mKDpMml645yslHfLI8iA
Origin: https://chat.google.com
Authorization: SAPISIDHASH <redacted>
...
```

> Note: clients6.google.com is an alias for googleapis.com

‎

The first important header here is `X-Goog-Api-Key`. This API key gives us permission to call endpoints in the Internal People API. This specific endpoint requires us to be authenticated with our Google account, which is done through the `Cookie` header and `SAPISIDHASH` (this value is generated [using the SAPISID cookie](https://stackoverflow.com/a/32065323))
‎

If you're worked with Google Cloud before, you might know that APIs need to be enabled for your project before you can make calls to them. If we tried taking this key and doing a call to some random unrelated API like the Play Atoms Private API `playatoms-pa.googleapis.com`

```
GET /$discovery/rest
Host: playatoms-pa.googleapis.com
X-Goog-Api-Key: AIzaSyB0RaagJhe9JF2mKDpMml645yslHfLI8iA
```

We would get the following error:

```
{
  "error": {
    "code": 403,
    "message": "Play Atoms Private API has not been used in project 576267593750 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/playatoms-pa.googleapis.com/overview?project=576267593750 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
    ...
  }
}
```

This is because just like Google Cloud projects we can make ourselves, the API key we found is tied to some Google-owned Cloud project, which doesn't have the Play Atoms Private API enabled for it.
‎

However, this key does in fact work for the **staging environment** of the Internal People API which otherwise without authentication isn't public:
‎
**Request**

```
GET /$discovery/rest
Host: staging-people-pa.sandbox.googleapis.com
Referer: https://chat.google.com
X-Goog-Api-Key: AIzaSyB0RaagJhe9JF2mKDpMml645yslHfLI8iA
```

> Note: all staging/test endpoints are under \*.sandbox.googleapis.com. This API key also requires the use of the chat.google.com Referer header.

‎
**Response**

```
HTTP/2 200 OK
Content-Type: application/json; charset=UTF-8

{
  "title": "Internal People API - Staging",
  "documentationLink": "http://boq/java/com/google/social/boq/release/socialgraphapiserver",
  "discoveryVersion": "v1",
  "id": "people_pa:v2",
  "revision": "20241031",
  ...
}
```

‎
Unlike the public discovery document, this version contains comments for everything, leaking a lot of how stuff works behind-the-scenes:

```
...
    "InAppNotificationTarget": {
      "id": "InAppNotificationTarget",
      "description": "How and where to send notifications to this person in other apps, and why the requester can do so. See go/reachability for more info. \"How\" and \"where\" identify the recipient in a P2P Bridge (glossary/p2p bridge), and \"why\" may be helpful in a UI to disambiguate which of several ways may be used to contact the recipient. How: Via a Google profile or a reachable-only phone number that the requester has access to. Specified in the target \"type\" and \"value\". Where: Apps in which the profile/phone number owner may receive notifications. Specified in the repeated \"app\". Why: Which fields in, e.g., a contact associated with this person make the notification target info visible to the requester. Specified in the repeated originating_field param. Example: Alice has a contact Bob, with: Email 0 = [email protected] Phone 0 = +12223334444 Phone 1 = +15556667777 Email 0 and Phone 0 let Alice see Bob's public profile (obfuscated gaia ID = 123). Public profiles are visible by email by default, and Bob has explicitly made it visible via Phone 0. Bob says people can send notifications to his public profile in YouTube. Phone 2 is associated with another Google profile that Bob owns, but he doesn't want others to see it. He is okay with people sending notifications to him in Who's Down if they have this phone number, however. There will be separate InAppNotificationTargets: one for Bob's public Google profile, and one for the second phone number, which is in his private profile. IANT #1 - targeting Bob's public profile (visible via Email 0 and Phone 0): app = [YOUTUBE] type = OBFUSCATED_GAIA_ID value = 123 originating_field: [ { field_type = EMAIL, field_index = 0 } // For Email 0 { field_type = PHONE, field_index = 0 } // For Phone 0 ] IANT #2 - targeting Bob's private profile phone number Phone 1: app = [WHOS_DOWN] type = PHONE value = +15556667777 originating_field: [ { field_type = PHONE, field_index = 1 } // For Phone 1 ]",
...
```

> **Update 2025-02-06:** Google has [removed all comments](https://x.com/brutecat/status/1887436162744410509) from the staging discovery doc.

### "Secret" visibility labels

As it turns out, certain Google cloud projects have visibility labels enabled for them, giving them more access than others. Endpoints can be hidden behind visibility labels, and they won't show up in the discovery document unless the secret `labels` parameter is provided. This [was discovered](https://www.youtube.com/watch?v=9pviQ19njIs) b...