---
title: whitelist-bypass – WebRTC Tunnels Through Video-Calling Platforms
url: https://www.darknet.org.uk/2026/09/whitelist-bypass-webrtc-tunnels-through-video-calling-platforms/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-09-14
fetch_date: 2026-09-15T07:01:45.405806
---

# whitelist-bypass – WebRTC Tunnels Through Video-Calling Platforms

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](data:image/svg+xml...)![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Countermeasures](https://www.darknet.org.uk/category/countermeasures/) / whitelist-bypass – WebRTC Tunnels Through Video-Calling Platforms

# whitelist-bypass – WebRTC Tunnels Through Video-Calling Platforms

Published September 15, 2026 |

Views: 103

whitelist-bypass tunnels internet traffic through commercial video-calling platforms, aimed at networks that permit an approved list of domains and block everything else. Tunnelling over WebRTC isn’t new. What caught my attention is what this project chooses to ride.

![whitelist-bypass — WebRTC Tunnels Through Video Calls, showing one orange media route passing an allowlist gate; darknet.org.uk.](data:image/svg+xml...)![whitelist-bypass — WebRTC Tunnels Through Video Calls, showing one orange media route passing an allowlist gate; darknet.org.uk.](https://www.darknet.org.uk/wp-content/uploads/2026/09/whitelist-bypass-webrtc-video-call-tunnels-640x360.webp)

Whitelist censorship is a different problem from a blocklist. A blocklist leaves the rest of the internet reachable, so a proxy on some unremarkable host usually gets you out.

Advertisement

A whitelist inverts that. Only approved destinations resolve and connect; everything else fails. To get through, your traffic has to *be* one of the approved destinations, not merely look unlike a blocked one.

whitelist-bypass’s answer is to send your data to a video-calling service the censor has already allowed. A device on the censored network places what looks like an ordinary call to VK Call, Yandex Telemost, or WB Stream; a machine on the free internet answers, and the traffic you actually want rides inside that call.

It all rests on the platform’s media server sitting on the approved list. Whether a given platform is permitted, and stays permitted, is a fact about one network at one moment. The tool doesn’t control it.

## Two tunnels, and why there are two

The project gives you two ways to carry data through the call, and the second one exists because the first can be throttled.

**DC mode** opens a WebRTC data channel – an SCTP stream, the same primitive a browser uses for peer-to-peer file transfer – and pushes a SOCKS5 tunnel through it. Your traffic becomes data-channel payload, relayed by the platform’s media server like any other call data.

**Video mode** does the same job, but encodes the data onto a published VP8 video track instead. It’s there for a reason the repository makes clear: some media servers rate-limit data channels while passing video freely, and on at least one supported platform the publisher’s track has to be video at all.

Advertisement

So when the data channel gets squeezed, the tunnel moves into the one stream a video call can’t do without. Both modes share the same framing and multiplexing above the transport, so the only difference is which stream carries the bytes.

The recommended deployment runs headless on both ends: pure Go on the [Pion](https://github.com/pion/webrtc) WebRTC stack, talking to the platform’s media server directly with no browser in the loop.

## What is actually in the repository

I cloned the current `main` branch (commit `747f8f2`, 3 September 2026) and read the source rather than the description of it. The tunnel is real code, not a README promise.

The shared relay under `relay/` implements the SOCKS5 proxy, the data-channel and VP8 tunnels, a connection multiplexer and an obfuscator. Separate headless creators handle each platform – `vk`, `telemost`, `wbstream` and `dion` – each its own Go module that creates or joins a call through the platform’s API without a browser.

The obfuscator is a deliberate choice. It derives a secret from the call’s join link, hashes it with SHA-256, and uses that key with XChaCha20-Poly1305 authenticated encryption and random per-message nonces; it also pads keepalive frames.

So the payload inside the call is encrypted independently of the platform’s own transport security, keyed by something both ends already share: the link used to join the call. Any smoothing of the video track’s timing is separate transport code, not part of the obfuscator.

It’s genuinely multi-platform. The joiner – the client on the censored side – targets Android, iOS and Linux; the creator, on the free side, targets Windows, macOS and Linux. On Android it runs as a system VPN, so all traffic flows through the call.

iOS is more involved. The source tree carries two forms: a proxy app that exposes a local SOCKS5 endpoint another app points at, and a VPN app that uses Apple’s Network Extension capability for system-wide routing.

Only the proxy build ships as a prebuilt IPA in the v0.3.8 release. The VPN app is in the source and its build target is documented, but it needs signing and that capability, so if you want it you’ll be building and signing it yourself.

Build documentation note

If you build from source, do not follow the README’s build table exactly. It lists `./build-app.sh` for the Android app; that script is not in the repository. The scripts that exist are `build-android.sh`, `build-joiner-app.sh`, `build-go.sh`, `build-headless.sh` and the rest. Prebuilt Android, iOS and desktop binaries are on the Releases page and are unaffected; it is the source-build instructions that have drifted from the code.

## Where it sits among WebRTC tunnels

Carrying a tunnel over WebRTC is well-trodden ground. Pion’s own ecosystem list includes Tor’s [Snowflake](https://snowflake.torproject.org/), weron, rtctunnel and a WebRTC socket proxy, and whitelist-bypass sits on that same list. So the interesting part isn’t the transport but the carrier it rides.

Snowflake, the closest well-known relative, uses volunteer browsers as ephemeral WebRTC proxies to reach Tor. whitelist-bypass instead points at named commercial calling services and leans on them being individually whitelisted by the censor.

That’s a sharper bet, and a more fragile one. It works precisely because a specific platform is on the approved list, and it stops working the moment that platform comes off it. The video-track fallback is the same logic one level down: when the cheap channel is squeezed, you move to the stream the service can’t throttle without breaking the calls it exists to carry.

Darknet has covered the covert-tunnel idea before, from the enterprise side. [ProxyBlob](https://www.darknet.org.uk/2025/06/proxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling/) runs a SOCKS5 tunnel over Azure Blob Storage, betting that a cloud endpoint is too ordinary to block. whitelist-bypass makes the same structural move against a stricter filter, with a consumer platform as the cover instead of a cloud service.

## The claim to be careful about

The project says that to deep-packet inspection the tunnel “looks like a normal video call”. That’s the load-bearing claim, and it’s the one this article can’t verify.

So does it actually look like a v...