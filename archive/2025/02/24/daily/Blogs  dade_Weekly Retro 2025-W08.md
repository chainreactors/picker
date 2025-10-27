---
title: Weekly Retro 2025-W08
url: https://0xda.de/blog/2025/02/weekly-retro-2025-w08/
source: Blogs  dade
date: 2025-02-24
fetch_date: 2025-10-06T20:33:43.158423
---

# Weekly Retro 2025-W08

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/02/weekly-retro-2025-w08/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

8 minutes

# [Weekly Retro 2025-W08](https://0xda.de/blog/2025/02/weekly-retro-2025-w08/)

---

* [Designing an Audit Log Framework](#designing-an-audit-log-framework)
* [Natlas Django Rewrite](#natlas-django-rewrite)
* [What I’m Reading](#what-im-reading)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

I got obsessed with a problem at work this week - how do you build a useful audit log framework, where the audit logs are useful and the framework is easy for developers to integrate with. Boy what a rabbit hole. This weekend I spent a good chunk of time workin on my Natlas rewrite in Django, keeping in mind some of my immediate learnings about audit logs.

## Designing an Audit Log Framework

Before diving into this topic, I want to caveat that I had absolutely no prior knowledge on designing audit logs before this past week. With that in mind, I set out to figure out what makes a good audit log framework. The right amount of structure, the right amount of flexibility, and hopefully something that integrates well with the application.

Initial attempts at the audit log had some of the basic ideas in place. From the beginning, I had this idea that audit logs were made up of 3 things – actors, subjects, and events. The actor is the entity that triggered the event. The subject is the entity that is being acted upon. The event is the details unique to the thing that happened. We stored the id and type of each actor and subject, as well as an event type and some arbitrary metadata.

But there were a few problems. The event was super flat, mixing concerns between actor, subject, event, and request metadata all as top level keys. Second, our first approach took a “hydrate useful user-facing information at query, rather than at emit” – so to render audit logs required *at least* two additional database queries for each audit log entry.

I could, and probably will, create a whole blog post on this topic, because I think there’s a lot to consider. In fact, my friend Adam has already published a [useful post about building audit logs](https://www.technowizardry.net/2022/05/how-to-build-a-useful-service-data-change-audit-log/), though his focus was a little different than what I am working towards building. Some of the concepts absolutely overlap, though.

The last thing I will say about audit logs is that it is useful to have a single ID that can reference different entities in your data models. This is probably an auto-incrementing integer for most people using an RDBMS. In some cases maybe people are using a UUID instead of an auto-incrementing integer. But I don’t really like either of these options. UUIDs don’t contain any information about what the ID is for. Integers reveal potentially sensitive information about business velocity, in addition to not being useful to identify a particular object outside of context. E.g. if you sell widgets, and a customers audit log shows that they bought widget 123 on Monday and widget 124 on Tuesday, they can infer that you had no other widget sales during that time.

Instead, I think we should construct IDs for our database models that are based on the type of data they are. Stripe is a great example of this where they provide IDs for basically every resource you can fetch or reference, and they tend to all have a unique prefix. Just by looking at the ID, you can tell what kind of resource it is referencing. E.g. a user might have an ID in your database of `user_8hWAb-kHmq5nmfE-xPggAA`, or a widget might have an ID of `wdgt_fwz7uz86mmt1Crr2D-jnPA`. I personally think it should be used as the primary key, so that you really do have just one way to reference it. You *could* add an `external_id` or some way to derive an externally facing ID from an integer primary key, but now you have two different ways to refer to the same thing, which is likely to result in mistakes or confusion.

I’m sure some database admins hate this idea, I do think it has some drawbacks. For instance, IDs are no longer ordered, so you need another way to order objects (you should probably be timestamping your objects anyways). IDs also go from being allocated 32 or 64 bits of space per row to being allocated many bytes (my examples above are 27 bytes long, or 218 bits per row). But the space allocation doesn’t really matter if you have to come up with and store an external ID anyways.

Anyways, I’m kind of obsessed with this problem, and am even accounting for it in the initial designs of my Natlas django rewrite.

## Natlas Django Rewrite

As mentioned last week, I talked about whether or not my scan data should just be stored in an RDBMS instead of in elasticsearch, and whether or not I want to rewrite it in Django.

For all of it’s flaws (and by that I mean design decisions that I personally would do differently), Django provides a super useful framework for python web apps. It’s definitely more batteries-included than alternatives like Flask, FastAPI, Starlette, etc. At first I resisted this, but after working on Natlas again more with flask, I really missed the batteries that Django included by default, and even moreso, I missed the Django ecosystem.

I started the rewrite in Django yesterday. By simply adding a popular django app, [django-allauth](https://docs.allauth.org/en/latest/), I already have a more robust auth flow, with signup, MFA, email confirmation, session management forgot password, etc. Of course I have some work to do to style it and make it look how I want and feel integrated with the rest of the application, but that is child’s play compared to having to build that all out myself in a bespoke manner. And then there’s [django-anymail](https://anymail.dev/en/stable/), which lets me basically build my email system exactly once, but allow anyone who wants to run their own instance to setup any mail sending platform they want, by just swapping the backend with one that anymail already supports.

This rewrite is going to take quite a while and basically completely abandon the old code. There are features I previously wrote that are broken now, features that I over-complicated, things that simply don’t scale well for the types of installations that I know natlas users have.

I’m using this framework switch as an opportunity to basically start fresh. Which basically means that it’s going to *appear* that there’s no real movement on Natlas for quite a while. But then there’s going to be a ton of movement all at once.

## What I’m Reading

![Chasing Shadows: Cyber Espionage, Subversion, and the Global Fight for Democracy](https://0xda.de/img/books/ChasingShadows-RonaldDeibert.99eb242711d02fd63a723b933e89260f.jpg)

### Chasing Shadows

#### By Ronald J. Deibert

**ISBN: 978-1-668-01404-2**
[Learn More](https://www.simonandschuster.com/books/Chasing-Shadows/Ronald-J-Deibert/9781668014042 "Learn More About The Book")

---

I haven’t been reading much lately, but I was excited to see this book announced and I picked it up immediately. I’m about 5 chapters in right now and I’m really enjoying hearing about Citizen Lab’s side of the stories that I’ve seen in the news. If you’re interested in the global surveillance and spyware market and how a small group of talented researchers have been fighting back for over a decade, I highly recommend picking this up.

## Interesting Links

* [PROTOCOL - Internet Assign...