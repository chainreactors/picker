---
title: Intro to Data Analytics Using SQL
url: https://www.blackhillsinfosec.com/intro-to-data-analytics-using-sql-wrapup/
source: Black Hills Information Security
date: 2024-12-03
fetch_date: 2025-10-06T19:39:49.157311
---

# Intro to Data Analytics Using SQL

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

2
Dec
2024

[Ethan Robish](https://www.blackhillsinfosec.com/category/author/ethan-robish/), [Webcast Wrap-Up](https://www.blackhillsinfosec.com/category/webcast-wrap-up/)
[Data Analytics](https://www.blackhillsinfosec.com/tag/data-analytics/), [DuckDB](https://www.blackhillsinfosec.com/tag/duckdb/), [SQL](https://www.blackhillsinfosec.com/tag/sql/), [Structured Query Language](https://www.blackhillsinfosec.com/tag/structured-query-language/)

# [Intro to Data Analytics Using SQL](https://www.blackhillsinfosec.com/intro-to-data-analytics-using-sql-wrapup/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/WC_wrap-up_W0011.png)

*This webcast was originally published on November 21, 2024.*

In this video, Ethan Robish discusses the fundamentals and intricacies of data analytics using SQL. Viewers will gain insight into SQL’s capabilities for data exploration, aggregation, and the use of window functions, as well as how to enhance data analysis through advanced SQL techniques. The video also introduces DuckDB, a powerful tool for data analytics, and provides practical examples of SQL queries to enrich and manipulate data effectively.

* The webinar introduces data analytics using SQL, covering the basics of SQL, types of databases, and practical examples of SQL queries.
* Ethan emphasizes the power and versatility of SQL as a tool for data analysis, highlighting its widespread use and applicability across different types of databases.
* DuckDB, a relatively new analytical database, is introduced as a tool that is easy to install and use for SQL queries, making it a valuable asset for data analytics workflows.

### **Highlights**

### **Full Video**

### **Transcript**

**Jason Blanchard**

Hello, everybody. Welcome to today’s Black Hills Information Security webcast. My name is Jason Blanchard. I am the content & community director here at Black Hills. And today we got Ethan. Ethan Robish is going to do the webcast today, and it’s called Intro to Data Analytics Using SQL.

All right, so if you joined us today, there’s a good chance that you want to learn this topic, and Ethan is a good person to teach this topic. So whenever we reach out to our, technical team and we say, hey, what would you like to give a webcast on?

Normally it’s like, what do you find exciting? Or what are you passionate about? Or what? What’s something that now that you wish you would have known six months ago? Or, like, what do you think would be really beneficial to the community to know?

And we give everyone the opportunity to create their own topic. And Ethan decided to do this one. So here’s what that means. Ethan loves this kind of stuff. And so as you’re listening today, realize that the person who’s teaching you today loves this kind of stuff.

And if you love this kind of stuff, then cool, we’re all best friends now. and please stick around in the Discord server or attend future webcasts and then we’ll become best friends then. If, you see us at a conference, always come up and say hi.

And if this is your first time here, thank you so much for joining us today and spending your hour with us. And for that, I’m going to turn it over to Ethan so that he can actually do the webcast instead of me just talking about all the other things.

Ethan, are you ready?

**Ethan Robish**

I’m ready.

**Jason Blanchard**

All right, I’m going to head backstage. If you need me at any time, just go ahead and ask for me or I’ll just jump in if anything bad happens.

**Ethan Robish**

Sounds good?

**Jason Blanchard**

Yeah. All right, I’ll see you in a little bit.

**Ethan Robish**

Thanks, Jason. And thanks to everyone, joining me today to learn about SQL. So we’re going to go over an intro to data analytics and learn a little bit about, this language called SQL.

After we discuss a little bit about the background of SQL, we’re going to talk about different types of databases and why you might choose one type over another. Maybe you didn’t even realize there were multiple types and you could kind of break them up into categories.

Next, we’re going to start just diving into a data set and, using SQL to do some data exploration, in data science parlance, also called exploratory data analysis.

And Then finally we’re going to dive in and do some data, data analysis with the select statement.

All right, so a little bit about me. I’m a former pen tester from Black Hills, former developer for Active Countermeasures and Microsoft. And more recently, most recently I’ve done threat hunting, detection engineering.

I played the assistant to the platform engineer who runs our Elastic cluster. but in one common thread through all of these is there’s, I’ve been introduced to SQL, w...