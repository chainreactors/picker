---
title: Back to the Basics
url: https://0xda.de/blog/2023/01/back-to-the-basics/
source: Blogs on dade
date: 2023-01-15
fetch_date: 2025-10-04T03:56:34.836303
---

# Back to the Basics

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2023/01/back-to-the-basics/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

4 minutes

# [Back to the Basics](https://0xda.de/blog/2023/01/back-to-the-basics/)

I used to love web development. I mean, I wasn’t necessarily great at it. But I loved it. I even managed to pay my rent through my senior year of college mostly from subcontract work where I’d take some lowest-bidder web design from a guy and turn it into a responsive bootstrap site for his small business customers. It wasn’t great, but I was to the point where I was able to crank out the whole site in about 4 hours (remember, small businesses, so they tended to have simple sites).

Then I started to get into web app development more as I started to take over [natlas](https://natlas.io/), formerly known as nweb. I taught myself how to work in flask and took the pretty simple nweb and turned it into something that I felt pretty proud of. It felt more like a service someone would really use. It had users, it had a back office, it had full text search of port scan results and a complete history of scans for every host we looked at. Not to mention the screenshotting behavior which let us visually see the sites we were scanning (not very well, mind you). Then I started to hit some scaling limitations as my employer wanted to get to scanning approximately half a million IP addresses for several thousand ports, with script scanning, every couple hours in order to detect deviations from baselines nearly immediately. We needed to scan faster, but my poor little flask app was getting crushed under the weight of all of those scanning agents talking http to it. Waiting for your search request to get processed became painful. I was convinced I needed to scale up. Abandon sqlite, fix my incompatibilities and make it work with postgres, so I could scale horizontally. That’s what all the cool kids were doing.

Well, after postgres, I realized that I had also been abusing global variables in flask to keep application state, and that application state being replicated into additional processes would result in undesirable behaviors for complete scan coverage. So now I also needed to extract that state into something else. I could go with a multiprocessing shared memory pool, but that seemed like a short term solution that wouldn’t work if I needed more servers. I could build a microservice to handle the state for me, since most of the time the state updates only required sub-millisecond computations. But that was more complexity and felt hard with my current architecture, or lack-thereof. My code was much like the vomit on Eminem’s sweater already, [mom’s spaghetti](https://www.youtube.com/watch?v=SW-BU6keEUw). Time for a ground up rewrite.

Except I talked myself into the ground up rewrite and then got intimidated by the amount of work and abandoned the project. I was embracing needless complexity, trying to solve for problems I wasn’t having yet. I was thinking about… *shudders* running a React app and turning the server into a mere data API.

But now, at work, I work with Django and React, and the idea of having to duplicate so much application logic between the backend and the frontend… FOR FUN… well, thank goodness I abandoned Natlas when I did. I’m tired of javascript hell. I’m tired of complex build pipelines and having to bundle and compile and tree shake and yada yada just to produce something that a few dozen kilobytes of html and css could have done. CSS-in-JS makes me want to mom’s spaghetti on my sweater.

It’s time to go back to the basics. For me, that means I’m going to go back to using [flask](https://flask.palletsprojects.com/en/2.2.x/) for side projects. I’m going to go back to [sqlite](https://www.sqlite.org/index.html) and try out [litestream](https://litestream.io/). I’m going to continue to use docker, because even with the added complexity, I love being able to literally ship “works on my machine” into production. I’m going to try out [fly.io](https://fly.io/) for deployment, I’ve heard good things. I want to check out [htmx.org](https://htmx.org/) and see if I can build a nice, modern feeling app without having to worry about the density of node\_modules opening a black hole on my SSD.

I’m working on a tiny habit tracking app right now. I want to track things in my life better, and most things I’ve tried have felt clunky or not really behaved as expected. A tiny habit tracking app using a tiny tech stack. Time to Marie Kondo my software development stack.

---

Share this page

`https://0xda.de/blog/2023/01/back-to-the-basics/`

[software development](https://0xda.de/tags/software-development)

734 Words

Date Published

2023-01-14 06:00 +0000

32fc96e @ 2024-03-17

---

[芒聠聬
Anatomy of a Hash](https://0xda.de/blog/2023/01/anatomy-of-a-hash/)

[Helm to Mailinabox
芒聠聮](https://0xda.de/blog/2022/12/helm-to-mailinabox/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2023/01/back-to-the-basics/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.json "JSON Feed")