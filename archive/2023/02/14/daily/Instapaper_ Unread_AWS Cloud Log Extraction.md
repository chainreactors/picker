---
title: AWS Cloud Log Extraction
url: https://www.sans.org/blog/aws-cloud-log-extraction/
source: Instapaper: Unread
date: 2023-02-14
fetch_date: 2025-10-04T06:34:29.369134
---

# AWS Cloud Log Extraction

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
2. AWS Cloud Log Extraction

[Previous level](/blog)

# AWS Cloud Log Extraction

Feb 10 2023

In this blog post, we discussed the acquisition of AWS CloudTrails logs stored in S3 buckets.

Authored byMegan Roddie-Fonseca

![Megan Roddie-Fonseca](/_next/image?url=https%3A%2F%2Fimages.contentstack.io%2Fv3%2Fassets%2Fbltabe50a4554f8e97f%2Fbltedffddcd494a86dc%2F67c5d78521a60e1ef4a4632d%2FMegan_Roddie_370x370.png&w=768&q=75)

As an analyst or incident responder operating in a cloud environment, you are going to frequently be performing log analysis to uncover and investigate malicious activity. The challenge is that there are so many different cloud vendors and software-as-a-service (SaaS) providers and each one has several methods of extracting logs. It’s important to understand where logs are and how they can be extracted so you are prepared to respond to incidents.

This five-part blog series will cover log extraction methods for Microsoft 365, Azure, Amazon Web Services (AWS), Google Workspace, and Google Cloud. Once these logs are extracted, your tools of choice can be used to analyze their contents.

This first blog post will focus on AWS, and specifically, we are going to look at how we can download CloudTrail logs. While there are other sources of logs in AWS that may be relevant to your investigation for specific services, CloudTrail is one of the most valuable log sources available in AWS. CloudTrail records AWS API calls at the management event level, by default, and data event level, if configured. In these logs, we can observe a variety of event types, such as S3 bucket deletion, IAM user modifications, and VM creations..

CloudTrail is turned on by default and will store logs in the CloudTrail portal for 90 days. To extend the retention of the logs past 90 days, you need to configure a trail to send the logs to an S3 bucket. This is outside the scope of this blog post but instructions on how to do this can be found in the [AWS CloudTrail documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html). Another point of discussion regarding CloudTrail configurations is that by default only Management events (API calls that ...