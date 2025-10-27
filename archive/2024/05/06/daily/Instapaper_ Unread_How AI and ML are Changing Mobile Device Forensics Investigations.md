---
title: How AI and ML are Changing Mobile Device Forensics Investigations
url: https://www.sans.org/blog/how-ai-and-ml-are-changing-mobile-device-forensics-investigations/
source: Instapaper: Unread
date: 2024-05-06
fetch_date: 2025-10-06T17:15:55.839942
---

# How AI and ML are Changing Mobile Device Forensics Investigations

* Skip to main content
* Go to search
* Go to footer

[Log In](/account/login)

[Join - It's Free](/account/create)

Search

Search

TrainingLearning PathsCommunity ResourcesFor Organizations

Back[Training](/cyber-security-training-overview)

[Courses

Build cyber prowess with training from renowned experts](/cybersecurity-courses)

[Ways to Train

Multiple training options to best fit your schedule and preferred learning style](/cyber-security-training-formats)

[Cyber Ranges

Hands-on simulations exercises keep you at the top of your game](/cyber-ranges)

[Training Events & Summits

Expert-led training at locations around the world](/cyber-security-training-events)

[Certifications

Demonstrate cybersecurity expertise with GIAC certifications](/cyber-security-certifications)

[Free Training Events

Upcoming workshops, webinars and local events](/free-cybersecurity-events)

[Workforce Security and Risk Training

Harden enterprise security with end-user and role-based training](/for-organizations/workforce)

[Meet Our Instructors

Train with world-class cybersecurity experts who bring real-world expertise to class.](/instructors)

Featured Course[View All Courses](/cyber-security-courses)

### SEC595: Applied Data Science and AI/Machine Learning for Cybersecurity Professionals

SEC595Cyber Defense

![SEC595: Applied Data Science and AI/Machine Learning for Cybersecurity Professionals](/_next/image?url=https%3A%2F%2Fimages.contentstack.io%2Fv3%2Fassets%2Fbltabe50a4554f8e97f%2Fblta744d1449d56747e%2F68cc24727ca471dde41357dd%2Fcourse-cards_cyber-defense_SEC595_1514x792.png&w=3840&q=75)

[View course details](/cyber-security-courses/applied-data-science-machine-learning)[Register](/cyber-security-courses/applied-data-science-machine-learning#schedule-pricing)

Get a Free Hour of SANS Training

Experience SANS training through course previews.

[Learn More](/course-preview)

Back[Learning Paths](/learning-paths)

[By Focus Area

Chart your path to job-specific training courses](/cybersecurity-focus-areas)

[New to Cyber

Give your cybersecurity career the right foundation for success](/mlp/new-to-cyber)

[By Job Role

Find the courses and certifications that align with our current or desired role](/job-roles)

[Leadership

Training designed to help security leaders reduce organizational risk](/cybersecurity-focus-areas/leadership)

[By Skills Framework

Explore how SANS courses align with leading cybersecurity skills frameworks including NICE, ECSF and DoD 8140](/skills-frameworks)

[Degree and Certificate Programs

Gain the skills, certifications, and confidence to launch or advance your cybersecurity career.](https://www.sans.edu/)

[By Skills Roadmap

Find the right training path based on critical skills](/cyber-security-skills-roadmap)

Featured[View all Focus Areas](/cybersecurity-focus-areas)

[Cloud Security Training, Courses, and Resources](/cybersecurity-focus-areas/cloud-security)

Can't find what you are looking for?

Let us help.

[Contact us](/about/contact)

Back[Community Resources](/security-resources)

Watch & Listen[Webinars](/webcasts)[Summit Presentations](/presentations)[Podcasts & Live Streams](/podcasts)[Overview](/security-resources/watch-and-listen)Read[Blog](/blog)[Newsletters](/newsletters)[Internet Storm Center](https://isc.sans.edu/)[Overview](/security-resources/read)Download[Open Source Tools](/tools)[Posters & Cheat Sheets](/posters)[Policy Templates](/information-security-policy)[White Papers](/white-papers)[Overview](/security-resources/download)

[SANS Community Benefits

Connect, learn, and share with other cybersecurity professionals](/member-benefits)

[AI Risk & Readiness

Explore expert-driven guidance, training, and tools to help defend against AI-powered threats and adopt AI securely.](/mlp/artificial-intelligence)

Join the SANS Community

Become a member for instant access to our free resources.

[Sign Up](/member-benefits)

Back[For Organizations](/for-organizations)

Team Development[Why Partner with SANS](/for-organizations/team-development/why-partner-with-sans)[Group Purchases](/for-organizations/team-development/group-purchasing)[Skills & Talent Assessments](/for-organizations/team-development/cybersecurity-assessments)[Private & Custom Training Programs](/for-organizations/team-development/private-training)[Overview](/for-organizations/team-development)Leadership Development[Management Courses & Accreditation](/cyber-security-courses?refinementList%5Bfacets.focusArea%5D%5B0%5D=Cybersecurity%20Leadership)[Cyber Crisis Exercises](/cyber-ranges/executive-cybersecurity-exercises)[CISO Network](/for-organizations/ciso-network)[Overview](/cybersecurity-focus-areas/leadership)Workforce Security & Risk[Security Awareness Training](/for-organizations/workforce/security-awareness-training)[Compliance Training](/for-organizations/workforce/compliance-training)[Risk Management](/for-organizations/workforce/risk-management)[Services](/for-organizations/workforce/services)[Resources](/for-organizations/workforce/resources)[Overview](/for-organizations/workforce)

[Public Sector

Mission-focused cybersecurity training for government, defense, and education](/for-organizations/public-sector)

[Partnerships

Explore industry-specific programming and customized training solutions](/partnerships)

[Sponsorship Opportunities

Sponsor a SANS event or research paper](/sponsorship)

Interested in developing a training plan to fit your organization’s needs?

We're here to help.

[Contact Us](/about/contact)

[Talk With an Expert](/about/contact#connect-with-a-training-advisor)

[Log In](/account/login)

[Join - It's Free](/account/create)

Menu

Search

Search

[Talk With an Expert](/about/contact#connect-with-a-training-advisor)

1. [Blog](/blog)
2. How AI Forensics Is Transforming Mobile Device Investigations

[Previous level](/blog)

# How AI Forensics Is Transforming Mobile Device Investigations

May 03 2024

One of the biggest challenges with AI comes with determining whether the artifact in question was generated by a human behind the keyboard or by AI.

Authored byDomenica Lee Crognale

![Domenica Crognale](/_next/image?url=https%3A%2F%2Fimages.contentstack.io%2Fv3%2Fassets%2Fbltabe50a4554f8e97f%2Fblt8f05e0f042b8d508%2F67c5d6b0045f5807a4bfe9c9%2F370x370_Domenica-Crognale.jpg&w=768&q=75)

Has anyone NOT heard the buzzwords Artificial Intelligence (AI) or Machine Learning (ML)? It should come as no surprise they are quickly being integrated into many of the products we use daily, including our smartphones. While adopting these technologies and using them to supplement ordinary tasks may often be overlooked by most users, they add a layer of convenience which may also serve to enrich forensic investigations during an examination. But this can be a two-sided coin as users seek out services aimed at data creation (think videos, images, and documents). We forensic analysts may also need to rely on AI and ML to assist in what could become a muddy field of artifacts.

As mobile device users, we have reaped the rewards of ML for quite some time now, probably unbeknownst to most. I personally find many of these features extremely convenient (at least with my iPhone), but what are they and what do our phones do with all this data? As far back as iOS 8, Apple used the *Frequent Locations* feature to collect data points on the user’s most visited places. In iOS 10, they implemented *Significant Locations*, which also gathers a vast amount of data with astonishing accuracy. The purpose for collecting all this data? Based on the places you visit most and the length of time for these visits, Apple can provide with more tailored suggestions, alerts, and personalization when using Apple-related features like Apple Maps, Calendar, Photos, the Appstore, and Siri on your device. The information is encrypted and cannot be read by Apple, but as forensic investigators, we realize that this is a gold mine of location information on where and wh...