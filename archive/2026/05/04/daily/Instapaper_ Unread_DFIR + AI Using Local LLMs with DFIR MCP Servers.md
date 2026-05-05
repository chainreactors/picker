---
title: DFIR + AI Using Local LLMs with DFIR MCP Servers
url: https://www.cybertriage.com/blog/dfir-ai-using-local-llms-with-dfir-mcp-servers/
source: Instapaper: Unread
date: 2026-05-04
fetch_date: 2026-05-05T05:04:21.046961
---

# DFIR + AI Using Local LLMs with DFIR MCP Servers

[Skip to content](#primary)

[cyber-triage-logo](https://www.cybertriage.com/)

Primary Menu

* [Platform](https://www.cybertriage.com/features/)
  + - * [Workflow](https://www.cybertriage.com/how-cyber-triage-works/)
      * [Benefits](https://www.cybertriage.com/benefits/)
      * [Why Cyber Triage](https://www.cybertriage.com/why-cyber-triage-digital-forensics-tool/)
      * [Compare Versions](https://www.cybertriage.com/pricing/)
      * [Cyber Triage for Teams](https://www.cybertriage.com/team-version/)
      * [Cyber Triage for Enterprise](https://www.cybertriage.com/enterprise/)
    - * #### Key Features
      * [The Collector](https://www.cybertriage.com/cyber-triage-dfir-collector/)
      * [Automated Analysis](https://www.cybertriage.com/features/prioritize-with-cyber-triage/)
      * [Malware Detection](https://www.cybertriage.com/malware-forensics-tool/)
      * [Ransomware Detection](https://www.cybertriage.com/features/ransomware/)
      * [Server API](https://www.cybertriage.com/team-rest-api/)
    - * #### EDR
      * [EDR + Cyber Triage](https://www.cybertriage.com/edr/)
      * [EDR Evasion 101](https://www.cybertriage.com/blog/how-edr-evasion-works-attacker-tactics/)
    - * #### Integrations
      * [EDR Powershell Script](https://www.cybertriage.com/deployer-script/)
      * [Integrated Capabilities](https://www.cybertriage.com/features/integrations/)
      * [Malware Scanner for Autopsy](https://www.cybertriage.com/autopsy-malware-module/)
* [Use Cases](https://www.cybertriage.com/benefits/)
  + [SOC Endpoint Investigation](https://www.cybertriage.com/soc-alert-investigation/)
  + [Consultants](https://www.cybertriage.com/benefits/consultants/)
  + [SOC DFIR Teams](https://www.cybertriage.com/benefits/internal-incident-responders/)
  + [Law Enforcement - Intrusions](https://www.cybertriage.com/benefits/law-enforcement/)
  + [Law Enforcement - ICAC (Trojan Defense)](https://www.cybertriage.com/detect-remote-access-for-icac-and-trojan-defense/)
* [Pricing](https://www.cybertriage.com/pricing/)
  + [Buy Cyber Triage](https://www.cybertriage.com/pricing/)
  + [Buy Malware Scanning Boosts](https://www.cybertriage.com/boost-checkout/)
  + [Buy Autopsy Malware Scanner Module](https://www.cybertriage.com/autopsy-checkout/)
  + [Buy Rapid Endpoint Triage Service](https://www.sleuthkitlabs.com/rapid_checkout/)
* [Resources](https://www.cybertriage.com/online-response-training/)
  + - * #### DFIR Education
      * [Blog](https://www.cybertriage.com/blog/)
      * [Training](https://www.cybertriage.com/training/)
      * [Webinars](https://www.cybertriage.com/events/)
      * [Product Videos](https://www.cybertriage.com/videos/)
      * [Intro to DFIR Blog Series](https://www.cybertriage.com/intro-to-cyber-incident-response/)
    - * #### Case Studies
      * [How to Bridge the EDR/Forensics Gap](https://www.cybertriage.com/blog/how-an-industrial-manufacturer-accelerated-investigations-with-cyber-triage/)
      * [How to Scale IR Collaboration](https://www.cybertriage.com/blog/how-a-fortune-100s-ir-team-accelerated-client-investigations/)
      * [How to Escalate to IR with Confidence](https://www.cybertriage.com/blog/how-a-major-german-bank-reduced-risk-saved-money-with-cyber-triage/)
      * [How to Speed Up Client Investigations](https://www.cybertriage.com/blog/how-cy4-cut-analysis-time-75/)
    - * #### Recent Releases
      * [3.17 (MCP & GenAI)](https://www.cybertriage.com/blog/cyber-triage-3-17-use-cyber-triage-with-ai/)
      * [3.16 (Enterprise Tier)](https://www.cybertriage.com/blog/cyber-triage-3-16-investigate-faster-with-cyber-triage-enterprise/)
      * [3.15 (Defender Telemetry, Access Control, IRIS)](https://www.cybertriage.com/blog/cyber-triage-3-15-import-defender-telemetry-more-soc-features/)
      * [3.14 (Tactics, Hayabusa, Baselining)](https://www.cybertriage.com/blog/3-14-release-brings-new-uis-hayabusa-baselining-and-much-more/)
* [About](https://www.cybertriage.com/about/)
  + [About](https://www.cybertriage.com/about/)
  + [Team](https://www.cybertriage.com/team/)
  + [Contact](https://www.cybertriage.com/contact/)
* [Start Free Trial](https://www.cybertriage.com/download-eval/)

Close signup

![](https://www.cybertriage.com/wp-content/uploads/2021/04/cyber-triage-logo-color-1.png)
Stay up to date on our **technology, training, events,** and more.

By submitting this form, you agree that Sleuth Kit Labs may process your information in accordance with our [Privacy Policy](https://sleuthkitlabs.com/privacy-policy/). We’ll use your information to send educational and marketing communications.

You can unsubscribe at any time using the link in our emails.

Not now >

Sleuth Kit Labs | 1070 Broadway, Somerville, MA 02144-2078 | info@sleuthkitlabs.com

# DFIR + AI: Using Local LLMs with DFIR MCP Servers

* April 30, 2026

[All Blogs](https://www.cybertriage.com/blog/)

After the release of MCP servers for Autopsy ([release blog](https://www.autopsy.com/autopsy-4-23-0-release-claude-ai-assistant-mcp-cyber-triage-integration/)) and Cyber Triage ([release blog](https://www.cybertriage.com/blog/cyber-triage-3-17-use-cyber-triage-with-ai/)), we received requests for how to use only local LLMs instead of public servers. This blog post shows you how to use LM Studio to run local LLMs along with Cyber Triage and Autopsy.

This topic is also relevant for those who want to experiment with AI and enter the [DFIR+AI Challenge: Good vs Ugly](http://ugly/). This allows you to use your case data without sending data to remote sites.

[LM Studio](https://lmstudio.ai/) is a free tool that allows you to run local LLM models on your computer. It will download models, load them, and provide the chat interface to them. Thanks to Nanni on the [Sleuth Kit Forum](https://sleuthkit.discourse.group/t/autopsy-mcp-server-is-faster-in-lm-studio/5558) for highlighting this was so easy.

## **Why Use Local Models**

The main reason that organizations use local LLMs are because either the lab is airgapped or because their policies prevent them from sending data to the cloud or vendor systems.

Using a local LLM means that everything can stay in your network.

But, local models have some downsides:

* They are small and therefore have less knowledge in them to enable enrichment of hashes, files, etc.
* They have less reasoning abilities
* They are **SLOWER**

But, all of those downsides could be better than no AI at all.

## **Setup**

First, setup Autopsy and Cyber Triage MCP servers using their respective user manuals, but stop when you get to the step about installing Claude Desktop. I.e. enable it in the options panel.

* [Autopsy](https://sleuthkit.org/autopsy/docs/user-docs/4.23.0/claude_mcp_page.html)
* [Cyber Triage](https://docs.cybertriage.com/en/latest/chapters/integrations/claude_client.html)

Before you proceed, make sure you have the path that you got from the Cyber Triage or Autopsy options panel (such as c:\\Program Files\\Cyber Triage\\bin\\cybertriage-mcp-stdio.exe).

**LM Studio Setup:**

1. [Download LM Studio](https://lmstudio.ai/download)
2. Install and launch it
3. Pick a model to download (we don’t yet have a strong opinion on which is best)

* Gemma 4 E4B is the default
* Qwen3.5 9B is also recommended if you have 16GB+ of RAM

4. Once the model has downloaded, open the chat window.
5. You should see a “+ Install” button on the right. Choose that and select “edit mcp.json”

![](https://www.cybertriage.com/wp-content/uploads/2026/04/2026-04-30-lmstudio-1.png)
6. That will give you json to enter the path into. The end result should look something like this (for Autopsy):

![](https://www.cybertriage.com/wp-content/uploads/2026/04/2026-04-30-lmstudio-2-800x212.png)
7. You can then enable the MCP on the right hand side.

![](https://www.cybertriage.com/wp-content/uploads/2026/04/2026-04-30-lmstudio-3.png)

That’s it. You can then start typing away. As always, we recommend your first prompt is something like “can you see the Cyber...