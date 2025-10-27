---
title: Would you like an IDOR with that? Leaking 64 million McDonald’s job applications
url: https://ian.sh/mcdonalds
source: Over Security - Cybersecurity news aggregator
date: 2025-07-11
fetch_date: 2025-10-06T23:39:29.470351
---

# Would you like an IDOR with that? Leaking 64 million McDonald’s job applications

[ian carroll](/)

# Would you like an IDOR with that? Leaking 64 million McDonald’s job applications

## Introduction

**[McHire](https://signup.mchire.com/)** is the chatbot recruitment platform used by [90%](https://www.paradox.ai/blog/7-companies-that-found-success-hiring-with-conversational-ai#toc-mcdonald-s-reduced-time-to-hire-by-60-and-saved-store-managers-5-hours-per-week-while-increasing-candidate-satisfaction-) of McDonald’s franchisees. Prospective employees chat with a bot named Olivia, created by a company called [Paradox.ai](https://www.paradox.ai/), that collects their personal information, shift preferences, and administers personality tests. We noticed this after seeing complaints on Reddit of the bot [responding with nonsensical answers](https://www.reddit.com/r/mildlyinfuriating/comments/1lo9s75/mcdonalds_hiring_ai_is_making_me_go_insane/).

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/a24bbffa-ecda-4c54-8cc5-c309477aa209/Screenshot_2025-07-02_at_9.36.13_AM/w=3840,quality=90,fit=scale-down)

During a cursory security review of a few hours, we identified two serious issues: the McHire administration interface for restaurant owners accepted the default credentials `123456:123456`, and an insecure direct object reference (IDOR) on an internal API allowed us to access any contacts and chats we wanted. Together they allowed us and anyone else with a McHire account and access to any inbox to retrieve the personal data of more than 64 million applicants.

## Applying for a job

We started by applying for a job at our local McDonald’s. McHire has a consumer-facing site at <https://jobs.mchire.com/> where it is easy to find available postings near you. We were immediately sent to Olivia, who helped us fill in our email and phone number along with what shifts we can work, and we were instantly moved to the next stage: the personality test!

![McHire personality test](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b4385a17-7e6e-48ea-b4f0-029ff1731b92/image/w=3840,quality=90,fit=scale-down)

McHire personality test

The personality test was a disturbing experience powered by [Traitify.com](http://Traitify.com) where we were asked if phrases like “enjoys overtime” are either **Me** or **Not Me**. It was simple to guess that we should probably select **Me** for the pro-employer questions and **Not Me** for questions referencing being argumentative or aggressive, but it was still quite strange.

Unfortunately, after this, we were stuck without any further progress and appeared to be awaiting human review. We tried to prompt inject the Olivia chatbot, which likely ruined our chance at a human approving us, but it seemed to be locked to a list of pre-set responses or something similar, and there were no interesting APIs for the candidates.

## Logging in

We noticed that restaurant owners can login to view applicants at <https://www.mchire.com/signin>. Although the app tries to force SSO for McDonald’s, there is a smaller link for “Paradox team members” that caught our eye.

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/c3c5bfed-b5fb-4398-8c7c-d4c18162f5f3/image/w=3840,quality=90,fit=scale-down)

Without much thought, we entered “123456” as the username and “123456” as the password and were surprised to see we were immediately logged in!

![McHire user administration](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ffcf9477-0a55-425d-ada9-24ab3f06904a/Screenshot_2025-06-30_at_5.16.01_PM/w=3840,quality=90,fit=scale-down)

McHire user administration

It turned out we had become the administrator of a test restaurant inside the McHire system. We could see all of the employees of the restaurant were simply employees of Paradox.ai, the company behind McHire. This was great because we could now see how the app worked, but annoying because we had still not demonstrated any actual confidentiality or integrity impact.

## Applying for our job

We decided to apply to one of the test job postings the account had set up already and see what it looked like on the other side. The restaurant can view all of the in-progress conversations with “Olivia” and then intervene when they hit certain stages like having completed the personality test.

![Restaurant’s view of our conversation application](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/bd64ba8f-e653-42ab-b364-2bf3801e5534/image/w=3840,quality=90,fit=scale-down)

Restaurant’s view of our conversation application

While viewing our test conversations, we noticed an interesting API to fetch the candidate information `PUT /api/lead/cem-xhr`, which seems to be a reference to proxying to some kind of Customer or Candidate Experience Manager (CEM) via an XHR request. The main parameter of this request was the `lead_id` of the chat, which for our test applicant was about `64,185,742`. We tried decrementing this number, and were immediately faced with PII from another McDonald’s applicant (including “unmasked” contact data)!

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6376f768-0ca4-40ed-9ebd-7d68b693d037/Screenshot_2025-07-10_at_19.50.36/w=3840,quality=90,fit=scale-down)

We quickly realized this API allows us to access every chat interaction that has ever applied for a job at McDonald’s. The information returned included:

* Name, email address, phone number, address
* Candidacy state and every state change/form input the candidate had submitted (shifts they could work, etc)
* Auth token to log into the consumer UI as that user, leaking their raw chat messages and presumably other information

We immediately began disclosure of this issue once we realized the potential impact. Unfortunately, no disclosure contacts were publicly available and we had to resort to emailing random people. The [Paradox.ai security page](https://www.paradox.ai/legal/security) just says that we do not have to worry about security!

After our outreach reached the appropriate people, the [Paradox.ai](http://paradox.ai/) team engaged with us, emphasized that safeguarding candidate and client data was their top priority, promptly remediated the vulnerability, and committed to further reviews to identify and close any remaining avenues of exploitation.

## Disclosure

We disclosed this issue to [Paradox.ai](http://Paradox.ai) and McDonald’s at the same time.

* **06/30/2025 5:46PM ET:** Disclosed to [Paradox.ai](http://Paradox.ai) and McDonald’s
* **06/30/2025 6:24PM ET:** McDonald’s confirms receipt and requests technical details
* **06/30/2025 7:31PM ET:** Credentials are no longer usable to access the app
* **07/01/2025 9:44PM ET:** Followed up on status
* **07/01/2025 10:18PM ET:** Paradox.ai confirms the issues have been resolved

## Collaborators

* Ian Carroll (<https://twitter.com/iangcarroll>)
* Sam Curry (<https://twitter.com/samwcyo>)