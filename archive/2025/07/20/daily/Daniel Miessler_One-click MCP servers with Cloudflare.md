---
title: One-click MCP servers with Cloudflare
url: https://danielmiessler.com/blog/one-click-mcp-servers-cloudflare
source: Daniel Miessler
date: 2025-07-20
fetch_date: 2025-10-06T23:50:59.384110
---

# One-click MCP servers with Cloudflare

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# One-click MCP servers with Cloudflare

Finally, MCP infrastructure without the infrastructure headache

July 19, 2025

[#technology](/archives/?tag=technology) [#innovation](/archives/?tag=innovation) [#ai](/archives/?tag=ai) [#tutorial](/archives/?tag=tutorial)

[![Cloudflare MCP servers visualization](/images/cloudflare-mcp-servers.png)](/images/cloudflare-mcp-servers.png)

Cloudflare simplifying MCP deployment (click for full size)

One thing I've never liked about [the whole MCP thing](https://www.anthropic.com/news/model-context-protocol) is the fact that you have to build a server and host it yourself.

So ever since hearing about this, I've been looking for a self-contained solution where I could basically just describe the functionality that I want and the infrastructure could be handled itself.

It turns out Cloudflare actually has [a solution for doing this](https://community.cloudflare.com/t/introducing-one-click-remote-mcp-servers-with-cloudflare/795791), and I just love this about Cloudflare. I've actually [talked about this elsewhere](/blog/ai-is-eating-the-software-world) how they're doing all sorts of one-off services really well, and just kind of eating the internet.

## What are MCP servers? [​](#what-are-mcp-servers)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers are a way to extend AI assistants with custom tools and data sources. They let you give your AI assistant access to specific capabilities—like querying databases, calling APIs, or performing specialized tasks. The problem is, traditionally you need to:

* Set up a server
* Handle authentication
* Manage scaling
* Deal with infrastructure
* Maintain uptime

This is a lot of overhead when you just want to add a simple capability to your AI workflow.

## Enter Cloudflare's one-click solution [​](#enter-cloudflare-s-one-click-solution)

[Cloudflare Workers](https://workers.cloudflare.com/) provides the perfect platform for MCP servers because:

* **No infrastructure management** - Cloudflare handles all the scaling and distribution
* **Global edge network** - Your MCP server runs close to users everywhere
* **Simple deployment** - Push code and it's live
* **Pay-per-use pricing** - No paying for idle servers

## Building a working MCP server [​](#building-a-working-mcp-server)

Let's build an actual MCP server that I can use. I'll create a simple "website analyzer" that can fetch and analyze any website's content.

### Step 1: Set up the project [​](#step-1-set-up-the-project)

bash

```
mkdir cloudflare-mcp-analyzer
cd cloudflare-mcp-analyzer
bun init -y
bun add @modelcontextprotocol/sdk wrangler
```

1
2
3
4

### Step 2: Create the MCP server [​](#step-2-create-the-mcp-server)

Create `src/index.js`:

javascript

```
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // CORS headers
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    // Root endpoint - server info
    if (url.pathname === "/") {
      return new Response(
        JSON.stringify(
          {
            name: env.MCP_SERVER_NAME || "website-analyzer",
            version: env.MCP_SERVER_VERSION || "1.0.0",
            description: "Website analysis MCP server",
            endpoints: ["/tools", "/call"],
          },
          null,
          2,
        ),
        {
          headers: { "Content-Type": "application/json", ...corsHeaders },
        },
      );
    }

    // List available tools
    if (url.pathname === "/tools") {
      return new Response(
        JSON.stringify(
          {
            tools: [
              {
                name: "analyze_website",
                description: "Analyze a website and extract key information",
                inputSchema: {
                  type: "object",
                  properties: {
                    url: { type: "string", description: "The URL to analyze" },
                  },
                  required: ["url"],
                },
              },
            ],
          },
          null,
          2,
        ),
        {
          headers: { "Content-Type": "application/json", ...corsHeaders },
        },
      );
    }

    // Execute tool
    if (url.pathname === "/call" && request.method === "POST") {
      const body = await request.json();
      const { name, arguments: args } = body;

      if (name === "analyze_website") {
        try {
          const response = await fetch(args.url);
          const html = await response.text();

          // Extract basic info
          const titleMatch = html.match(/<title>(.*?)<\/title>/i);
          const title = titleMatch ? titleMatch[1] : "No title found";

          const linkCount = (html.match(/<a\s/gi) || []).length;
          const imageCount = (html.match(/<img\s/gi) || []).length;

          return new Response(
            JSON.stringify({
              content: [
                {
                  type: "text",
                  text: JSON.stringify(
                    {
                      url: args.url,
                      title,
                      stats: {
                        links: linkCount,
                        images: imageCount,
                        contentLength: html.length,
                      },
                    },
                    null,
                    2,
                  ),
                },
              ],
            }),
            {
              headers: { "Content-Type": "application/json", ...corsHeaders },
            },
          );
        } catch (error) {
          return new Response(
            JSON.stringify({
              content: [
                {
                  type: "text",
                  text: `Error: ${error.message}`,
                },
              ],
            }),
            {
              headers: { "Content-Type": "application/json", ...corsHeaders },
            },
          );
        }
      }
    }

    return new Response("Not Found", { status: 404 });
  },
};
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
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125

### Step 3: Configure for Cloudflare [​](#step-3-configure-for-cloudflare)

Create `wrangler.toml`:

toml

```
name = "mcp-website-analyzer"
main = "src/index.js"
compatibility_date = "2024-01-01"

[vars]
MCP_SERVER_NAME = "website-analyzer"
MCP_SERVER_VERSION = "1.0.0"
```

1
2
3
4
5
6
7

### Step 4: Test locally (optional) [​](#step-4-test-locally-optional)

bash

```
# Test your worker locally
wrangler dev
```

1
2

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) is Cloudflare's CLI tool for managing Workers

### Step 5: Deploy to Cloudflare [​](#step-5-deploy-to-cloudflare)

bash

```
# Login to Cloudflare
wrangler login

# Deploy the worker
wrangler deploy
```

1
2
3
4
5

Pro tip: If you have environment variables set, use `(unset CF_API_TOKEN && wrangler deploy)`

That's it! Your MCP server is now live on Cloudflare's global network.

### Step 6: Connect to your AI assistant [​](#step-6-connect-to-your-ai-assistant)

Add to your MCP configuration:

json

```
{
  "mcpServers": {
    "website-analyzer": {
      "url": "https://mcp-website-analyzer.YOUR-SUBDOMAIN.workers.dev",
      "description": "Analyzes ...