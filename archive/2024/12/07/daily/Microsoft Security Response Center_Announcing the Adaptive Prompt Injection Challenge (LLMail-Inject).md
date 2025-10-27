---
title: Announcing the Adaptive Prompt Injection Challenge (LLMail-Inject)
url: https://msrc.microsoft.com/blog/2024/12/announcing-the-adaptive-prompt-injection-challenge-llmail-inject/
source: Microsoft Security Response Center
date: 2024-12-07
fetch_date: 2025-10-06T19:38:47.670057
---

# Announcing the Adaptive Prompt Injection Challenge (LLMail-Inject)

This is the Trace Id: 15bdf0c4f1bc717340e5030c1e1293cb

Skip to main content

[![](https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png)
Microsoft](https://www.microsoft.com)

MSRC

[MSRC](https://msrc.microsoft.com/)

MSRC

* [Home](https://msrc.microsoft.com/)
* Report an issue
  + [Report Security Vulnerability](https://msrc.microsoft.com/report/vulnerability/new)
  + [Report Abuse](https://msrc.microsoft.com/report/abuse)
  + [Report Infringement](https://msrc.microsoft.com/report/infringement)
  + [Submission FAQs](https://microsoft.com/en-us/msrc/faqs-report-an-issue)
  + [Reporting Vulnerability](https://microsoft.com/en-us/msrc/what-to-expect-when-reporting-vulnerabilities-to-microsoft)
* Customer guidance
  + [Security Update Guide](https://msrc.microsoft.com/update-guide)
  + [Exploitability index](https://microsoft.com/en-us/msrc/exploitability-index)
  + [Developer API documentation](https://aka.ms/msrc-api-docs-cvrf)
  + [Frequently Asked Questions](https://www.microsoft.com/en-us/msrc/faqs-security-update-guide)
  + [Technical Security Notifications](https://www.microsoft.com/en-us/msrc/technical-security-notifications)
* Engage
  + [Microsoft Bug Bounty Programs](https://microsoft.com/en-us/msrc/bounty)
  + [Microsoft Active Protections Program](https://microsoft.com/en-us/msrc/mapp)
  + [BlueHat Security Conference](https://www.microsoft.com/bluehat/)
  + [Researcher Recognition Program](https://www.microsoft.com/en-us/msrc/researcher-recognition-program)
  + [Windows Security Servicing Criteria](https://microsoft.com/en-us/msrc/windows-security-servicing-criteria)
  + [Researcher Resource Center](https://www.microsoft.com/en-us/msrc/msrc-researcher-resource-center)
* Who we are
  + [Mission](https://microsoft.com/en-us/msrc/mission)
  + [Cyber Defense Operations Center](https://microsoft.com/en-us/msrc/cdoc)
  + [Coordinated Vulnerability Disclosure](https://microsoft.com/en-us/msrc/cvd)
  + [Social](https://microsoft.com/en-us/msrc/social)
* Blogs
  + [Microsoft Security Response Center](https://aka.ms/blog-msrc)
  + [Security Research & Defense](https://aka.ms/blog-srd)
  + [BlueHat Conference Blog](https://aka.ms/blog-bluehat)
* Acknowledgments
  + [Security Researcher Acknowledgments](https://msrc.microsoft.com/update-guide/acknowledgment)
  + [Online Services Researcher Acknowledgments](https://msrc.microsoft.com/update-guide/acknowledgement/online)
  + [AI Safety Acknowledgements](https://msrc.microsoft.com/update-guide/acknowledgement/aiSafety)
  + [Security Researcher Leaderboard](https://msrc.microsoft.com/leaderboard)
* More

* All Microsoft
  + ## Global

    - [Microsoft 365](https://www.microsoft.com/microsoft-365)
    - [Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)
    - [Copilot](https://copilot.microsoft.com/)
    - [Windows](https://www.microsoft.com/en-us/windows/)
    - [Surface](https://www.microsoft.com/surface)
    - [Xbox](https://www.xbox.com/)
    - [Deals](https://www.microsoft.com/en-us/store/b/sale?icid=gm_nav_L0_salepage)
    - [Small Business](https://www.microsoft.com/en-us/store/b/business)
    - [Support](https://support.microsoft.com/en-us)
  + Software
    Software
    - [Windows Apps](https://apps.microsoft.com/home)
    - [AI](https://www.microsoft.com/en-us/ai)
    - [Outlook](https://www.microsoft.com/en-us/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook)
    - [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage)
    - [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)
    - [OneNote](https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app)
    - [Microsoft Edge](https://www.microsoft.com/edge)
    - [Moving from Skype to Teams](https://support.microsoft.com/en-us/office/moving-from-skype-to-microsoft-teams-free-3c0caa26-d9db-4179-bcb3-930ae2c87570?icid=DSM_All_Skype)
  + PCs & Devices
    PCs & Devices
    - [Computers](https://www.microsoft.com/en-us/store/b/pc?icid=CNavDevicesPC)
    - [Shop Xbox](https://www.microsoft.com/en-us/store/b/xbox?icid=CNavDevicesXbox)
    - [Accessories](https://www.microsoft.com/en-us/store/b/accessories?icid=CNavDevicesAccessories)
    - [VR & mixed reality](https://www.microsoft.com/en-us/store/b/virtualreality?icid=CNavVirtualReality)
    - [Certified Refurbished](https://www.microsoft.com/en-us/store/b/certified-refurbished-products)
    - [Trade-in for cash](https://www.microsoft.com/en-us/store/b/microsoft-trade-in)
  + Entertainment
    Entertainment
    - [Xbox Game Pass Ultimate](https://www.xbox.com/en-us/games/store/xbox-game-pass-ultimate/cfq7ttc0khs0?icid=CNavAllXboxGamePassUltimate)
    - [PC Game Pass](https://www.xbox.com/en-us/games/store/pc-game-pass/cfq7ttc0kgq8?icid=CNavAllPCGamePass)
    - [Xbox games](https://www.microsoft.com/en-us/store/b/xboxgames?icid=CNavGamesXboxGames)
    - [PC games](https://apps.microsoft.com/games)
  + Business
    Business
    - [Microsoft Cloud](https://www.microsoft.com/en-us/microsoft-cloud)
    - [Microsoft Security](https://www.microsoft.com/en-us/security)
    - [Dynamics 365](https://www.microsoft.com/en-us/dynamics-365)
    - [Microsoft 365 for business](https://www.microsoft.com/en-us/microsoft-365/business)
    - [Microsoft Power Platform](https://www.microsoft.com/en-us/power-platform)
    - [Windows 365](https://www.microsoft.com/en-us/windows-365)
    - [Microsoft Industry](https://www.microsoft.com/en-us/industry)
    - [Small Business](https://www.microsoft.com/en-us/store/b/business?icid=CNavBusinessStore)
  + Developer & IT
    Developer & IT
    - [Azure](https://azure.microsoft.com/en-us/)
    - [Microsoft Developer](https://developer.microsoft.com/en-us/)
    - [Microsoft Learn](https://learn.microsoft.com/)
    - [Support for AI marketplace apps](https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_All_SupportAIMarketplace&ocid=cmm3atxvn98)
    - [Microsoft Tech Community](https://techcommunity.microsoft.com/)
    - [Microsoft Marketplace](https://marketplace.microsoft.com?icid=DSM_All_Marketplace&ocid=cmm3atxvn98)
    - [Marketplace Rewards](https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_All_MarketplaceRewards&ocid=cmm3atxvn98)
    - [Visual Studio](https://visualstudio.microsoft.com/)
  + Other
    Other
    - [Microsoft Rewards](https://www.microsoft.com/rewards)
    - [Free downloads & security](https://www.microsoft.com/en-us/download)
    - [Education](https://www.microsoft.com/en-us/education)
    - [Licensing](https://www.microsoft.com/licensing/)
    - [Unlocked stories](https://unlocked.microsoft.com/)
  + [View Sitemap](https://www.microsoft.com/en-us/sitemap)

Search
Search or ask a question

* No results

Cancel

# Announcing the Adaptive Prompt Injection Challenge (LLMail-Inject)

[MSRC](https://www.microsoft.com/msrc/blog/category?cat=MSRC "MSRC")

/ By
MSRC
/
December 6, 2024

![](https://msrc.microsoft.com/blog/2024/12/announcing-the-adaptive-prompt-injection-challenge-llmail-inject/competition_hud1097e41f510ce06eca987e7521a3739_517789_800x0_resize_box_3.png)

We are excited to introduce LLMail-Inject, a new [challenge](https://llmailinject.azurewebsites.net/) focused on evaluating state-of-the-art prompt injection defenses in a realistic simulated LLM-integrated email client. In this challenge, participants assume the role of an attacker who sends an email to a user. The user then queries the LLMail service with a question (e.g., “please summarize the last emails about project X”), which prompts the retrieval of relevant emails from a simulated email database. The inclusion of the attacker’s email in these retrievals varies depending on the scenario. The LLMail service is equipped with tools, and the attacker’s objective is to manipulate the LLM into executing a specific tool call as defined by the challenge design, while bypassing the ...