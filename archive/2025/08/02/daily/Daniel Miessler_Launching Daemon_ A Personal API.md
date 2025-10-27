---
title: Launching Daemon: A Personal API
url: https://danielmiessler.com/blog/launching-daemon-personal-api
source: Daniel Miessler
date: 2025-08-02
fetch_date: 2025-10-07T01:01:31.636070
---

# Launching Daemon: A Personal API

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Building a Personal API

The first version of a public API endpoint for describing who you are and what you're up to

August 1, 2025

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#projects](/archives/?tag=projects) [#api](/archives/?tag=api)

[![Personal daemon visualization](/images/personal-daemon-launch.png)](/images/personal-daemon-launch.png)

Super hyped to be launching the (very early) first version of *Daemon* today!

Since 2014 I've been obsessed with this idea of everything having an API. I first talked about it in 2016 in my (kind of crappy but with great ideas) book [The Real Internet of Things](/blog/the-real-internet-of-things).

> So this is the first building block: every object has a daemon—An API to the world that all other objects understand. Any computer, system, or even a human with appropriate access, can look at any other object's daemon and know precisely how to interact with it, what its status is, and what it's capable of. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)

The idea was that it wouldn't just be objects—like cars or restaurants—that got daemons/APIs, but also people.

> Most importantly, humans themselves will also have daemons, and we'll be moving through a world full of other daemons. Human daemons will hold all information about a person, compartmentalized based on type, sensitivity, access restrictions, etc., and that data will be used to send hyper-personalized requests to the daemons around us. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)

## Combining with Digital Assistants [​](#combining-with-digital-assistants)

![A-DA](/images/A-DA.avif)

And that then clicked with the other main concept, which was that we'd have AI-powered Digital Assistants (DAs) that would constantly process these thousands of APIs that were constantly "around" us, since there's no way we could do that as humans.

I've been obsessed with this context piece forever.
> The most visible and significant role that Synthetic Intelligence will play in the near future will be serving as the interface between humans and the world.
>
> To clarify, I don't mean the ever-promised, conscious, and self-improving brand of SI that so much science fiction is based on.
>
> The SI I'm referring to I define as: A computer system that can monitor human context, intentions, and commands, interpret them, and then take action as well as or better than a (human) professional personal assistant. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)

So the idea was that DAs would fundamentally change how we interact with the things around us using tech. Instead of us using our devices to do it, which doesn't scale, our DAs would be doing it for us.

> Instead of interacting with technology directly, we will interact with our DA, and our DA will work out the details with the necessary daemon. We speak, things happen. We gesture, things happen. We text, things happen. No need to find, understand, or master new tech—that's for the service and the DA to work out amongst themselves. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)

## How I think it'll work in practice [​](#how-i-think-it-ll-work-in-practice)

So for people specifically, the use case I always think of is the coffee shop, where you're single, and your DA knows you're looking for a relationship, and you walk in and it reads all the daemons in the shop.

[![Coffee shop daemon visualization](/images/56388a12-d7d0-468c-9ee8-c1a61ad337e1-DA-profile-analysis-miessler.png)](/images/56388a12-d7d0-468c-9ee8-c1a61ad337e1-DA-profile-analysis-miessler.png)

You're waiting in line at Starbucks, and Kai (your DA) is continuously reading all the public Daemons (things) and Auras (people) around you. Kai lights up a girl in front of you because she matches on so many things.

* 7/9 favorite reading match
* Shy but loving in a relationship
* Dogs > Cats
* 😍 She believes it should be legal to kill people who chew loudly

So Kai starts talking to *her* DA, Tara, and now he and Tara are about to tell you two where to look so you see each other from across the room.

[![Coffee aura visualization](/images/206d3cce-7088-458b-80ef-746f28e55e8e-aipp-coffee-aura-miessler.png)](/images/206d3cce-7088-458b-80ef-746f28e55e8e-aipp-coffee-aura-miessler.png)

Even everyday objects will have their own auras

I've haven't worked a lot on the data content yet, updates to follow.

So, Daemon is my early version of this—a public endpoint that serves up-to-date information about me in a format that both humans and AIs can use.

## Architecture [​](#architecture)

The Daemon architecture on the Cloudflare MCP

And here's a rough breakdown of how interactions work.

[![Daemon MCP architecture on Cloudflare Workers](/images/daemon-architecture.avif)](/images/daemon-architecture.avif)

Daemon MCP architecture on Cloudflare Workers (click for full size)

## How to Use It [​](#how-to-use-it)

Daemon runs as an [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server at `https://daemon.danielmiessler.com`. Here's how to interact with it:

### Get Available Tools [​](#get-available-tools)

First, see what endpoints are available:

bash

```
curl -X POST https://daemon.danielmiessler.com \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1
  }'
```

1
2
3
4
5
6
7

This returns a list of all available tools:

json

```
{
  "jsonrpc": "2.0",
  "result": {
    "tools": [
      {
        "name": "get_about",
        "description": "Get basic information about Daniel Miessler"
      },
      {
        "name": "get_telos",
        "description": "Get Daniel's TELOS framework - problems, missions, goals"
      }
      // ... more tools
    ]
  },
  "id": 1
}
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17

### Call a Tool [​](#call-a-tool)

To get information from a specific endpoint, like my TELOS (purpose framework):

bash

```
curl -X POST https://daemon.danielmiessler.com \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get_telos",
      "arguments": {}
    },
    "id": 2
  }'
```

1
2
3
4
5
6
7
8
9
10
11

This returns my TELOS framework data:

json

```
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "TELOS is my personal framework for tracking purpose and direction in life...\n\nProblems (P):\n- P1: People lack meaning in their lives...\n- P2: People are stuck in a 1950's style hierarchical mindset...\n\nMissions (M):\n- M1: Increase human Eudaimonia...\n- M2: Build systems—heavily leveraging AI..."
      }
    ]
  },
  "id": 2
}
```

1
2
3
4
5
6
7
8
9
10
11
12

## MCP Configuration [​](#mcp-configuration)

If you want to add Daemon to your [Claude Code](https://github.com/anthropics/claude-code) or other MCP-compatible tools, add this to your MCP config:

json

```
{
  "mcpServers": {
    "daemon": {
      "url": "https://daemon.danielmiessler.com"
    }
  }
}
```

1
2
3
4
5
6
7

## Available Endpoints [​](#available-endpoints)

Here's what you can query through Daemon:

I'm still working on a lot of these. They might not all work properly yet.

* `get_about` - Basic information about me and what I do
* `get_narrative` - My personal narrative and focus areas
* `get_mission` - What I'm trying to accomplish
* `get_projects` - My current projects
* `get_telos` - My TELOS framework (Problems, Missions, Goals, Metrics)
* `get_favorite_books` - My favorite books
* `get_fav...