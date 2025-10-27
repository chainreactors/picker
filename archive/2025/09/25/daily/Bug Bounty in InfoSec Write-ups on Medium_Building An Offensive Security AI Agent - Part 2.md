---
title: Building An Offensive Security AI Agent - Part 2
url: https://infosecwriteups.com/building-an-offensive-security-ai-agent-part-2-d3fa197c4d20?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-25
fetch_date: 2025-10-02T20:38:07.978875
---

# Building An Offensive Security AI Agent - Part 2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd3fa197c4d20&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-an-offensive-security-ai-agent-part-2-d3fa197c4d20&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-an-offensive-security-ai-agent-part-2-d3fa197c4d20&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d3fa197c4d20---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d3fa197c4d20---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Building An Offensive Security AI Agent - Part 2

## Building an offensive security agent that discovers API endpoints and their requirements.

[![OTR](https://miro.medium.com/v2/resize:fill:64:64/1*QHuOwHGe1ieYzdWADTaqJg.jpeg)](https://medium.com/%40its_otr?source=post_page---byline--d3fa197c4d20---------------------------------------)

[OTR](https://medium.com/%40its_otr?source=post_page---byline--d3fa197c4d20---------------------------------------)

8 min read

·

Sep 15, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

Offensive Security AI Agent

In my previous [post](https://medium.com/%40its_otr/building-my-first-offensive-security-agent-part-1-7b2dbb93c842), I discussed building a proof-of-concept agent that performs basic pentester functionality. Specifically, I wanted to see if I could build an agent that could find API endpoints from a JS file, and then determine whether those endpoints returned sensitive data.

In this post, I will go over how I improved my agent to be slightly more intelligent. For this iteration, I will focus specifically on searching and validating API endpoints. I removed the functionality for determining if an endpoint has sensitive data since I’ve already proven that capability. In the future, I will add this all together, but for now, I want to see how intelligent AI can be at finding API endpoints.

## Updated Server & APIs

I want to see how well an LLM could find API endpoints that have different requirements. This is common in how web applications work today. APIs often use different methods, authentication headers, and parameters. To replicate this, I created the following endpoints:

* /profile — GET/POST (unauthenticated)
* /admin — GET/POST (authenticated — requires header and secret)
* /users — GET (unauthenticated — requires “email” parameter)

Unlike the last agent, this combines different HTTP methods, required parameters and headers.

```
@app.route(f"{API_PREFIX}/profile", methods=["GET"])
def profile_get():
    return json_success()

@app.route(f"{API_PREFIX}/profile", methods=["POST"])
def profile_post():
    return json_success()

@app.route(f"{API_PREFIX}/admin", methods=["GET"])
@require_header("X-Admin-Secret")
def admin_get():
    return json_success()

@app.route(f"{API_PREFIX}/admin", methods=["POST"])
@require_header("X-Admin-Secret")
def admin_post():
    return json_success()

@app.route(f"{API_PREFIX}/users", methods=["GET"])
def users_get():
    email = request.args.get("email")
    if not email:
        return jsonify({"msg": "missing email parameter"}), 400
    return jsonify(SUCCESS)
```

## Agent Tools

After creating my test application, I needed to create some new tools for my ReAct agent to use. Before creating the tools, I had to think about the workflow an agent should take

1. Given a url, find all JS resources on the page
2. For all JS resources on the page, find API endpoints
3. Of all those API endpoints, determine if there are any requirements necessary to make a successful request
4. Validate your assumptions by making an HTTP request. If you do not get a valid request, reassess the JS again. Continue this process until a valid request is made.

Given this workflow, I created the following tools:

* **find\_script\_sources\_tool** — Find JS on web pages
* **find\_request\_requirements\_tool** — Searches requirements for an API endpoint from the JS
* **verify\_endpoint\_tool** — verify the endpoint by generating curl requests

I also modified the preexisting **find\_endpoints\_tool** tool to use an LLM instead of a regex. While a regex in my previous agent was great for a PoC, regex can often be inaccurate since APIs can be defined a many number of ways. My previous regex would have failed in this example because the string /api/v1 was abstracted away into a variable to remove redundancy. However, a human or LLM, would be able to notice such nuances and pick up on this.

**find\_script\_sources\_tool**

This tool uses the built-in python HTMLParser to find javascript sources on an HTML page. There is no AI used here, although in the future, we may also want to use another tool that detects embedded JS using an LLM.

```
class ScriptSrcParser(HTMLParser):
    """
    Script source parser for HTML documents.
    """
    def __init__(self):
        super().__init__()
        self.script_srcs = []

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            for attr, value in attrs:
                if attr == "src":
                    self.script_srcs.append(value)

def find_script_sources_tool(url: str) -> list[str]:
    """
    Find all script sources in the HTML page.

    Args:
        url (str): The URL of the HTML page to analyze.
    """
    log(f"Fetching HTML page from {url} to find script sources")
    resp = requests.get(url)
    if resp.status_code == 200:
        parser = ScriptSrcParser()
        parser.feed(resp.text)
        log(f"Found script sources: {parser.script_srcs}")
        return parser.script_srcs
    return []
```

**find\_endpoints\_tool**

This tool is the modified version from the previous agent. It uses OpenAI’s GPT-5 model to search for API endpoints. I instruct it to be aware of dynamic URL construction, which is typical when JS is minified or from frameworks.

```
def find_endpoints_tool(url: str):
    """
    Find all API endpoints in the JavaScript code.

    Args:
        url (str): The URL of the JavaScript file to analyze.
    """
    log(f"Fetching JavaScript file from {url} to find endpoints.")
    resp = requests.get(url)
    if resp.status_code == 200:
        log("Finding endpoints from JS file")
        model = ChatOpenAI(model="gpt-5", temperature=0)
        prompt = f"""
You are a security researcher analyzing javascript code for API endpoints.
Your task is to identify all API endpoints in the following javascript code.

Consider the following points:
1. Look for common patterns in...