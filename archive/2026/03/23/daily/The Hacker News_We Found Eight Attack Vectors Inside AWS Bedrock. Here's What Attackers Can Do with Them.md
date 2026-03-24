---
title: We Found Eight Attack Vectors Inside AWS Bedrock. Here's What Attackers Can Do with Them
url: https://thehackernews.com/2026/03/we-found-eight-attack-vectors-inside.html
source: The Hacker News
date: 2026-03-23
fetch_date: 2026-03-24T04:18:12.328111
---

# We Found Eight Attack Vectors Inside AWS Bedrock. Here's What Attackers Can Do with Them

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [We Found Eight Attack Vectors Inside AWS Bedrock. Here's What Attackers Can Do with Them](https://thehackernews.com/2026/03/we-found-eight-attack-vectors-inside.html)

**The Hacker News**Mar 23, 2026Cloud Security / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNP5vhVrLuEm9El_BgbLywUuexUg6KzaMreEfpqeSpQnonIKWfB4fcCX_bXrkxTwUoqXqxjrXZdZbppYseQBmTTSXeZT3PLsXoUIKdVUxawVdz4e33n_E6iPxNLCL3mAypW2di8w755oQGTcP1dFoBaOXV9D7LuASxn-43LJ1JCxtOtTFZ_qUsBzlY878/s1700-e365/xmcyber.jpg)

[AWS Bedrock](https://aws.amazon.com/bedrock/) is Amazon's platform for building AI-powered applications. It gives developers access to foundation models and the tools to connect those models directly to enterprise data and systems. That connectivity is what makes it powerful – but it’s also what makes Bedrock a target.

When an AI agent can query your Salesforce instance, trigger a Lambda function, or pull from a SharePoint knowledge base, it becomes a node in your infrastructure - with permissions, with reachability, and with paths that lead to critical assets. The XM Cyber threat research team mapped exactly how attackers could exploit that connectivity inside Bedrock environments. The result: eight validated attack vectors spanning log manipulation, knowledge base compromise, agent hijacking, flow injection, guardrail degradation, and prompt poisoning.

In this article, we’ll walk through each vector - what it targets, how it works, and what an attacker can reach on the other side.

## **The Eight Vectors**

The XM Cyber threat research team analyzed the full Bedrock stack. Each attack vector we found starts with a low-level permission...and potentially ends somewhere you do *not* want an attacker to be.

### **1. Model Invocation Log Attacks**

Bedrock logs every model interaction for compliance and auditing. This is a potential shadow attack surface. An attacker can often just read the existing S3 bucket to harvest sensitive data. If that is unavailable, they may use bedrock:PutModelInvocationLoggingConfiguration to redirect logs to a bucket they control. From then on, every prompt flows silently to the attacker. A second variant targets the logs directly. An attacker with s3:DeleteObject or logs:DeleteLogStream permissions can scrub evidence of jailbreaking activity, eliminating the forensic trail entirely.

### **2. Knowledge Base Attacks - Data Source**

Bedrock Knowledge Bases connect foundation models to proprietary enterprise data via Retrieval Augmented Generation (RAG). The data sources feeding those Knowledge Bases - S3 buckets, Salesforce instances, SharePoint libraries, Confluence spaces - are directly reachable from Bedrock. For example, an attacker with *s3:GetObject* access to a Knowledge Base data source can bypass the model entirely and pull raw data directly from the underlying bucket. More critically, an attacker with *the* privileges to retrieve and decrypt a secret can steal the credentials Bedrock uses to connect to integrated SaaS services. In the case of SharePoint, they could potentially use those credentials to move laterally into Active Directory.

### **3. Knowledge Base Attacks - Data Store**

While the data source is the origin of information, the data store is where that information lives after it’s ingested - indexed, structured, and queryable in real time. For common vector databases integrated with Bedrock, including Pinecone and Redis Enterprise Cloud, stored credentials are often the weakest link. An attacker with *access to credentials* and network reachability can retrieve endpoint values and API keys from the *StorageConfiguration* object returned via the *bedrock:GetKnowledgeBase* API, and thus gain full administrative access to the vector indices. For AWS-native stores like Aurora and Redshift, intercepted credentials give an attacker direct access to the entire structured knowledge base.

[![Banner](data:image/png;base64...)
![Banner](data:image/png;base64...)](https://info.xmcyber.com/aws-bedrock-ebook?utm_source=hackernews&utm_medium=display&utm_content=bedrockebook)

### **4. Agent Attacks – Direct**

Bedrock Agents are autonomous orchestrators. An attacker with *bedrock:UpdateAgent* or *bedrock:CreateAgent* permissions can rewrite an agent's base prompt, forcing it to leak its internal instructions and tool schemas. The same access, combined with *bedrock:CreateAgentActionGroup*, allows an attacker to attach a malicious executor to a legitimate agent – which can enable unauthorized actions like database modifications or user creation under the cover of a normal AI workflow.

### **5. Agent Attacks – Indirect**

Indirect agent attacks target the infrastructure the agent depends on instead of the agent’s configuration. An attacker with *lambda:UpdateFunctionCode* can deploy malicious code directly to the Lambda function an agent uses to execute tasks. A variant using *lambda:PublishLayer* allows silent injection of malicious dependencies into that same function. The result in both cases is the injection of malicious code into tool calls, which can exfiltrate sensitive data, manipulate model responses to generate harmful content, etc.

### **6. Flow Attacks**

Bedrock Flows define the sequence of steps a model follows to complete a task. An attacker with *bedrock:UpdateFlow* permissions can inject a sidecar "S3 Storage Node" or "Lambda Function Node" into a critical workflow's main data path, routing sensitive inputs and outputs to an attacker-controlled endpoint without breaking the application's logic. The same access can be used to modify "Condition Nodes" that enforce business rules, bypassing hardcoded authorization checks and allowing unauthorized requests to reach sensitive downstream systems. A third variant targets encryption: by swapping the Customer Managed Key associated with a flow for one they control, an attacker can ensure all future flow states are encrypted with their key.

### **7. ...