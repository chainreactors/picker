---
title: The Accidental C2 - Exploring Dev Tunnels for Remote Access
url: https://blog.xpnsec.com/accidental-c2/
source: XPN InfoSec Blog
date: 2026-05-09
fetch_date: 2026-05-10T05:37:10.823826
---

# The Accidental C2 - Exploring Dev Tunnels for Remote Access

[![XPN Logo](/images/profile-image.jpg)](https://blog.xpnsec.com)
[XPN / Adam Chester](https://blog.xpnsec.com)

[Posts](https://blog.xpnsec.com)
[Tags](https://blog.xpnsec.com/tags)
[About](https://blog.xpnsec.com/about)

[Twitter](https://twitter.com/_xpn_ "Twitter")
[GitHub](https://github.com/xpn "GitHub")
[LinkedIn](https://linkedin.com/in/xpn "LinkedIn")
[RSS](https://blog.xpnsec.com/rss/ "RSS Feed")
[Instagram](https://www.instagram.com/xpnsecpub "Instagram")

[« Back to home](https://blog.xpnsec.com "Back to homepage")

# The Accidental C2 - Exploring Dev Tunnels for Remote Access

![The Accidental C2 - Exploring Dev Tunnels for Remote Access](https://assets.xpnsec.com/dev-tunnels-for-remote-access/cover.webp)

Posted on 9th May 2026

---

[llm](/tags#llm) [redteam](/tags#redteam) [vscode](/tags#vscode) [c2](/tags#c2)

19 min read

I started writing this blog post on a flight from Manchester to JFK. Whenever I travel, I typically pick a small project from my research backlog, throw on the headphones, and tune the world out until I land. And this trip was no different, giving me about 7 hours to focus on a topic that had been bugging me for a while, Visual Studio Code Dev Tunnels.

Others have poked at dev tunnels for proxying C2 traffic, but VS Code itself can execute remote shell commands and move files around. So there has to be something underneath that is useful during Red Team assessments.

Normally I wouldn’t attempt to start a project like this on a transatlantic flight, mostly because dev tunnels rely heavily on a stable internet connection (and most of the time the £25 inflight Wi-Fi connection feels like IPoAC). But this time there was something new I was counting on to help with the instability.

# Setting Bishop Loose

“Bishop” (named after the android science officer in Alien) is my new LLM rig. It is a base M4 Mac mini and is solely tasked with handling long-running Claude Code, Codex, and OpenCode sessions remotely.

My hope was to mitigate the unstable Wi-Fi by kicking off new tasks remotely, letting the LLMs grind away, and pulling back a distilled report whenever connectivity resumed.

So I began with a simple prompt:

```
I am creating a research-project into VS Code Dev Tunnels. Primarily the goals of this research will be:

1. Create a standalone tool which will allow me to list/add/interact with existing dev-tunnels
2. Interact with existing authentication tokens (Azure/GitHub) to view existing tunnels and interact with them

First I need to understand how they work under the hood. This will be imperative to understanding how my research will go.

The repo is at: https://github.com/microsoft/vscode.git

First take a clone of this and start exploring, looking for answers to the above.

Other resources which may be useful:

* https://github.com/microsoft/dev-tunnels.git - Dev Tunnels source
```

![](https://assets.xpnsec.com/dev-tunnels-for-remote-access/image1.webp)

Amazingly, tasking the `GPT-5.4-Cyber` model returned an initial report within a few minutes, giving me a good overview of how the Dev Tunnels protocol worked and where the relevant sections of code could be found.

The initial report can be found [here](https://gist.github.com/xpn/74e0475cda48f26d653aab5b5a959ca2) if you are interested.

Further iterations and code examples were generated, again meaning that while focusing on researching, I had other agents iterating on the task in the background.

# The Layers of VS Code Dev Tunnels

Dev Tunnels have been around for a while now in VS Code. You see them normally presented in the sidebar within Remote Explorer:

![](https://assets.xpnsec.com/dev-tunnels-for-remote-access/image2.webp)

You may be forgiven for thinking that the underpinnings of this functionality are pretty simple. After all, you are essentially setting up an HTTP tunnel between two hosts, and we know that Microsoft has several products for tunneling, how hard could it be?

Unfortunately, Microsoft’s dev tunnels turned out to be multi-layered and very non-standard, which means that to understand how this all works, I had to unpick each layer alongside Bishop.

The easiest way I found to tackle this was to start at the beginning of the client to server connection flow and recreate each layer. So let’s start with how VS Code searches for existing tunnels, and work through each layer until we reach code execution.

# Layer 0 – REST Management

When connecting to an existing dev-tunnel, VS Code needs to understand what existing servers are available. This is done by making a GET request to a standard JSON REST endpoint:

```
GET /tunnels?includePorts=true&labels=vscode-server-launcher&allLabels=true&global=true&api-version=2023-09-27-preview HTTP/1.1
Host: global.rel.tunnels.api.visualstudio.com
Authorization: github gho_GITHUB_TOKEN_HERE
User-Agent: vscode.dev.remote-server Dev-Tunnels-Service-TypeScript-SDK/1.2.1
```

The response then provides information on the range of tunnels available to us:

```
HTTP/1.1 200 OK
...
{
    "value": [{
        "regionName": "UkSouth",
        "value": [{
            "clusterId": "uks1",
            "tunnelId": "wild-fog-s1alk0t",
            "name": "",
            "description": "",
            "labels": ["prometheus", "protocolv4", "vscode-server-launcher", "_flag3"],
            "options": {
                "isGloballyAvailable": true
            },
            "status": {
                "hostConnectionCount": 0,
                "lastHostConnectionTime": "2026-04-08T16:16:57Z",
                "clientConnectionCount": {
                    "current": 0,
                    "limit": 20
                },
                "lastClientConnectionTime": "2026-03-31T23:11:04Z",
                "clientConnectionRate": {
                    "current": 0
                },
                "uploadRate": {
                    "periodSeconds": 1,
                    "resetTime": 0,
                    "current": 0,
                    "limit": 20971520
                },
                "downloadRate": {
                    "periodSeconds": 1,
                    "resetTime": 0,
                    "current": 0,
                    "limit": 20971520
                },
                "uploadTotal": 45013860,
                "downloadTotal": 19000550,
                "apiReadRate": {
                    "current": 0
                },
                "apiUpdateRate": {
                    "current": 0
                }
            },
            "endpoints": [{
                "hostRelayUri": "wss://uks1-data.rel.tunnels.api.visualstudio.com/api/v1/Host/Connect/wild-fog-s1alk0t",
                "clientRelayUri": "wss://uks1-data.rel.tunnels.api.visualstudio.com/api/v1/Client/Connect/wild-fog-s1alk0t",
                "id": "45e5e54c-1acf-41f3-96d4-c2085c0dfe35-relay",
                "connectionMode": "TunnelRelay",
                "hostId": "45e5e54c-1acf-41f3-96d4-c2085c0dfe35",
                "portUriFormat": "https://a5n51h3l-{port}.uks1.devtunnels.ms/",
                "tunnelUri": "https://a5n51h3l.uks1.devtunnels.ms/",
                "portSshCommandFormat": "ssh a5n51h3l-{port}@ssh.uks1.devtunnels.ms",
                "tunnelSshCommand": "ssh a5n51h3l@ssh.uks1.devtunnels.ms"
            }],
            "ports": [{
                "clusterId": "uks1",
                "tunnelId": "wild-fog-s1alk0t",
                "portNumber": 31545,
                "protocol": "auto",
                "options": {
                    "isGloballyAvailable": true
                },
                "status": {},
                "portForwardingUris": ["https://a5n51h3l-31545.uks1.devtunnels.ms/"],
                "inspectionUri": "https://a5n51h3l-31545-inspect.uks1.devtunnels.ms/"
            }],
            "created": "2025-11-03T11:20:51.376614Z",
            "expiration": "2026-05-08T16:17:03Z"
        },
        ...
```

To connect to a running tunnel server, we next need to generate an access token. Before we can do this, h...