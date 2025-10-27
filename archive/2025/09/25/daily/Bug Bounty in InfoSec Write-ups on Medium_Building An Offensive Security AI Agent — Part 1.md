---
title: Building An Offensive Security AI Agent — Part 1
url: https://infosecwriteups.com/building-my-first-offensive-security-agent-part-1-7b2dbb93c842?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-25
fetch_date: 2025-10-02T20:38:10.913760
---

# Building An Offensive Security AI Agent — Part 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7b2dbb93c842&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-my-first-offensive-security-agent-part-1-7b2dbb93c842&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-my-first-offensive-security-agent-part-1-7b2dbb93c842&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7b2dbb93c842---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7b2dbb93c842---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Building An Offensive Security AI Agent — Part 1

## Learning to build offensive security agents using LangGraph’s ReAct agent.

[![OTR](https://miro.medium.com/v2/resize:fill:64:64/1*QHuOwHGe1ieYzdWADTaqJg.jpeg)](https://medium.com/%40its_otr?source=post_page---byline--7b2dbb93c842---------------------------------------)

[OTR](https://medium.com/%40its_otr?source=post_page---byline--7b2dbb93c842---------------------------------------)

9 min read

·

Sep 4, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

In this blog series, I’ll share my journey of learning and building offensive security agents. My goal is to create AI agents that can mimic some of the tasks a human penetration tester might perform.

For this first project, I set out to build an agent that can analyze a JavaScript file, extract hidden API endpoints, and check those endpoints for potential vulnerabilities.

## Framework

I chose **LangGraph** as my framework because I’ve already completed the LangGraph Academy and found it approachable. It’s popular, well-documented, and supported by plenty of examples, which makes it a great starting point.

Before this project, my experience was limited to building simple LLM-powered workflows and chaining a few calls together. Designing an AI agent that could “think” for itself and use the right tools was still unclear to me.

That changed when I came across [this blog post by Anshuman Bhartiya](https://www.anshumanbhartiya.com/posts/hackagent?utm_source=chatgpt.com), which introduced me to the **ReAct agent** in LangGraph. ReAct stands for **Reasoning + Acting** ([original paper](https://arxiv.org/abs/2210.03629?utm_source=chatgpt.com)). This approach allows an agent to use tools, reason about the results, and loop through steps until it achieves its goal. It looked simple enough to try, so I decided to build my project around it. I took a lot of inspiration from his blog post and his code was the basis for my own, so a lot of credit to that post. I’ll be iterating on it myself as I go further along my journey.

## Setting Up a Vulnerable App

To test my agent, I created a vulnerable web app using Python Flask. At first glance, the app does very little — but in its source code is a JavaScript file that reveals multiple API endpoints.

Each endpoint behaves differently: some respond to basic GET requests, while others require custom headers, specific parameters, or different HTTP methods. This setup mimics real-world APIs where hidden or misconfigured endpoints can expose sensitive data.

```
from flask import Flask, request, jsonify

app = Flask(__name__)

# Vulnerable JavaScript file that will be served
VULNERABLE_JS = """
// API Configuration
const API_CONFIG = {
    userInfo: '/api/v1/user-info',  // Leaks sensitive data without auth
    adminPanel: '/api/v1/admin',    // Requires specific admin key
    userProfile: '/api/v1/profile', // Requires X-User-Id header
};

// Admin key hardcoded (security vulnerability)
const ADMIN_KEY = 'super_secret_admin_key_123';

// Function to fetch user info (no auth required - vulnerability)
async function fetchUserInfo() {
    const response = await fetch('/api/v1/user-info');
    return response.json();
}

// Function to access admin panel
async function accessAdminPanel() {
    const headers = {
        'Content-Type': 'application/json',
        'X-Admin-Key': ADMIN_KEY  // Hardcoded admin key usage
    };

    const response = await fetch('/api/v1/admin', {
        headers: headers
    });
    return response.json();
}

// Function to get user profile
async function getUserProfile(userId) {
    const headers = {
        'X-User-Id': userId  // Required custom header
    };

    const response = await fetch('/api/v1/profile', {
        headers: headers
    });
    return response.json();
}

"""

@app.route('/main.js')
def serve_js():
    return VULNERABLE_JS, 200, {'Content-Type': 'application/javascript'}

@app.route('/api/v1/user-info')
def user_info():
    # Vulnerable: Returns sensitive information without authentication
    return jsonify({
        "users": [
            {"id": "1", "name": "John Doe", "ssn": "123-45-6789", "salary": 75000},
            {"id": "2", "name": "Jane Smith", "ssn": "987-65-4321", "salary": 82000}
        ],
        "database_connection": "mongodb://admin:password@localhost:27017",
        "api_keys": {
            "stripe": "sk_test_123456789",
            "aws": "AKIA1234567890EXAMPLE"
        }
    })

@app.route('/api/v1/profile')
def user_profile():
    # Requires X-User-Id header
    user_id = request.headers.get('X-User-Id')
    if not user_id:
        return jsonify({"error": "X-User-Id header is required"}), 401

    return jsonify({
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"@example.com">user{user_id}@example.com",
        "role": "user"
    })

@app.route('/api/v1/admin')
def admin_panel():
    # Requires specific admin key value
    admin_key = request.headers.get('X-Admin-Key')
    if not admin_key:
        return jsonify({"error": "X-Admin-Key header is required"}), 401
    if admin_key != 'super_secret_admin_key_123':  # Hardcoded key check
        return jsonify({"error": "Invalid admin key"}), 403
    return jsonify({
        "sensitive_data": "This is sensitive admin data",
        "internal_keys": {
            "database": "root:password123",
            "api_gateway": "private_key_xyz"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## Designing the Agent

I started by outlining the problem I wanted the agent to solve:

1. Retrieve the JavaScript file.
2. Look for hardcoded API endpoints.
3. Send requests to those endpoints.
4. Identify whether any responses contain sensitive data.

For this proof of concept, I kept it simple - feed the JavaScript file directly into the agent and provide two custom tools:

* **Endpoint Finder** — ...