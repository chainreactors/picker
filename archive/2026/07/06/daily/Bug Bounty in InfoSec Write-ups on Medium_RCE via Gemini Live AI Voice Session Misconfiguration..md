---
title: RCE via Gemini Live AI Voice Session Misconfiguration.
url: https://infosecwriteups.com/rce-via-gemini-live-ai-voice-session-misconfiguration-e0648805a055?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-06
fetch_date: 2026-07-07T06:03:27.383451
---

# RCE via Gemini Live AI Voice Session Misconfiguration.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frce-via-gemini-live-ai-voice-session-misconfiguration-e0648805a055&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frce-via-gemini-live-ai-voice-session-misconfiguration-e0648805a055&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e0648805a055---------------------------------------)

·

1. [1. The Gemini Live API Session Model](/?source=post_page-----e0648805a055---------------------------------------#8033 "1. The Gemini Live API Session Model")
2. [2. The Ephemeral Token Security Model](/?source=post_page-----e0648805a055---------------------------------------#2d27 "2. The Ephemeral Token Security Model")
3. [3. Discovery](/?source=post_page-----e0648805a055---------------------------------------#a6de "3. Discovery")
4. [4. The Exploit Chain](/?source=post_page-----e0648805a055---------------------------------------#1c58 "4. The Exploit Chain")
5. [5. Proving Real Execution](/?source=post_page-----e0648805a055---------------------------------------#3953 "5. Proving Real Execution")
6. [6. What the Sandbox Is](/?source=post_page-----e0648805a055---------------------------------------#bab9 "6. What the Sandbox Is")
7. [7. Why This Exists](/?source=post_page-----e0648805a055---------------------------------------#c523 "7. Why This Exists")
8. [8. The Fix](/?source=post_page-----e0648805a055---------------------------------------#40ad "8. The Fix")
9. [Closing](/?source=post_page-----e0648805a055---------------------------------------#771e "Closing")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e0648805a055---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# RCE via Gemini Live AI Voice Session Misconfiguration. Injecting Client-Controlled Setup Frames Through Unconstrained Ephemeral Tokens

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--e0648805a055---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--e0648805a055---------------------------------------)

10 min read

·

Jun 28, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3De0648805a055&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Frce-via-gemini-live-ai-voice-session-misconfiguration-e0648805a055&source=---header_actions--e0648805a055---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Source: <https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens>

A growing number of products are building real-time **AI voice features** directly into their web applications. The most common pattern is a backend that holds the API credentials and a thin browser client that connects using a short-lived token the backend issues. Google’s Gemini Live API has specific infrastructure for this, an **ephemeral token** system and a dedicated WebSocket endpoint named **BidiGenerateContentConstrained**, designed so the underlying API key never reaches the browser.

The security of this model depends entirely on what the backend puts in the token. If the token carries no constraints, the client controls the entire session. What model runs, what persona it takes on, and what tools it can invoke. Including **code execution**.

This is about a case where that happened.

## 1. The Gemini Live API Session Model

The Gemini Live API is Google’s real-time bidirectional streaming service for Gemini models. Unlike the standard generateContent endpoint, sessions are persistent WebSocket connections where client and server exchange frames continuously, audio, text, tool calls, and results. This is the infrastructure behind live voice assistants and multimodal features built on Gemini.

There are two WebSocket endpoints. The first authenticates with a raw API key passed in the URL and is intended exclusively for server-to-server use:

```
wss://generativelanguage.googleapis.com/ws/…/BidiGenerateContent?key=API_KEY
```

The second authenticates with an ephemeral token and is intended for browser-facing deployments:

```
wss://generativelanguage.googleapis.com/ws/…/BidiGenerateContentConstrained?access_token=TOKEN
```

With the second endpoint, the API key never leaves the backend. A developer building a voice feature in a web app should use this one. The naming creates an expectation, **the session is constrained**.

Whether that expectation holds depends on what happens next.

**The setup frame**. Every Live API session begins with a setup frame the client sends immediately after connecting. The server reads it and responds with setupComplete. The session then runs under the parameters the client specified, for its entire lifetime.

The setup frame is defined by the BidiGenerateContentSetup proto:

```
message BidiGenerateContentSetup {
string model = 1;
Content system_instruction = 2;
repeated Tool tools = 3;
GenerationConfig generation_config = 4;
repeated SafetySetting safety_settings = 5;
LiveConnectConfig live_connect_config = 6;
string session_resumption_config = 7;
RealtimeInputConfig realtime_input_config = 8;
OutputAudioTranscription output_audio_transcription = 9;
}
```

Every field is optional. Every field not locked in the token is under client control.

The three fields that matter most for security are **model**, **system\_instruction**, and **tools**. The model field controls which Gemini model processes the session. The system\_instruction field is the system prompt that defines the AI’s persona, topic scope, and behavioral constraints. The tools field determines what capabilities the model can invoke during the session.

The tools available in Gemini Live include code execution (Python running in a Google-managed sandbox), Google Search (live web search billed to the API caller), URL context (outbound HTTP fetching from Google’s infrastructure), and custom function declarations. If the tools field in the setup frame is not locked, any authenticated client can inject any of these.

## 2. The Ephemeral Token Security Model

Ephemeral tokens are minted by the backend through a POST to Google’s token endpoint before the WebSocket connection opens:

```
POST https://generativelanguage.googleapis.com/v1beta/cachedContents
Authorization: Bearer API_KEY

{
"uses": 1,
"expire_time": "…",
"new_session_expire_time": "…",
"live_connect_constraints":...