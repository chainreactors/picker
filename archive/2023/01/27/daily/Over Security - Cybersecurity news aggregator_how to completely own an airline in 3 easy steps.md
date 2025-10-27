---
title: how to completely own an airline in 3 easy steps
url: https://maia.crimew.gay/posts/how-to-hack-an-airline/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-27
fetch_date: 2025-10-04T05:00:01.010650
---

# how to completely own an airline in 3 easy steps

# maia blog

[home](/)
|
[blog](/posts/)
|
[citations](/citations/)
|
[contact](/contact/)
|
[sample packs](/samples/)

![a glitchy edited photo of an airplane](/img/posts/how-to-hack-an-airline/cover.jpg)

Jan 19, 2023
(updated Jan 22, 2023)

4 minutes to read

by maia arson crimew

in
[leak](/posts/tagged/leak/), [security](/posts/tagged/security/), [infosec](/posts/tagged/infosec/), [jenkins](/posts/tagged/jenkins/), [aviation](/posts/tagged/aviation/), [nofly](/posts/tagged/nofly/)

# how to completely own an airline in 3 easy steps

**and grab the TSA nofly list along the way**

*note: this is a slightly more technical\* and comedic write up of the story covered by my friends over at dailydot, which you can read [here](https://www.dailydot.com/debug/no-fly-list-us-tsa-unprotected-server-commuteair/)*
*i say slightly since there isnt a whole lot of complicated technical stuff going on here in the first place*

## step 1: boredom

like so many other of my hacks this story starts with me being bored and browsing [shodan](https://shodan.io) (or well, technically [zoomeye](https://www.zoomeye.org), chinese shodan), looking for exposed [jenkins](https://jenkins.io) servers that may contain some interesting goods. at this point i've probably clicked through about 20 boring exposed servers with very little of any interest, when i suddenly start seeing some familar words. "[ACARS](https://en.wikipedia.org/wiki/ACARS)", lots of mentions of "crew" and so on. lots of words i've heard before, most likely while binge watching [Mentour Pilot](https://youtube.com/c/MentourPilotaviation) YouTube videos. jackpot. an exposed jenkins server belonging to [CommuteAir](https://en.wikipedia.org/wiki/CommuteAir).

![zoomeye search for x-jenkins](/img/posts/how-to-hack-an-airline/zoomeye.jpg)

## step 2: how much access do we have really?

ok but let's not get too excited too quickly. just because we have found a funky jenkins server doesn't mean we'll have access to much more than build logs. it quickly turns out that while we don't have anonymous admin access (yes that's quite frequently the case [god i love jenkins]), we do have access to build workspaces. this means we get to see the repositories that were built for each one of the ~70 build jobs.

## step 3: let's dig in

most of the projects here seem to be fairly small spring boot projects. the standardized project layout and extensive use of the resources directory for configuration files will be very useful in this whole endeavour.

the very first project i decide to look at in more detail is something about "ACARS incoming", since ive heard the term acars before, and it sounds spicy. a quick look at the resource directory reveals a file called `application-prod.properties` (same also for `-dev` and `-uat`). it couldn't just be that easy now, could it?

well, it sure is! two minutes after finding said file im staring at [filezilla](https://filezilla-project.org/) connected to a [navtech](https://www.navblue.aero/) sftp server filled with incoming and outgoing ACARS messages. this aviation shit really do get serious.

![a photo of a screen showing filezilla navigated to a folder called ForNavtech/ACARS_IN full of acars messages, the image is captioned like a meme with "this aviation shit get serious"](/img/posts/how-to-hack-an-airline/this-aviation-shit-get-serious.jpg)

here is a sample of a departure ACARS message:

![screenshot of a terminal showing what an ACARS RCV file shows like](/img/posts/how-to-hack-an-airline/acars-sample.jpg)

from here on i started trying to find journalists interested in a probably pretty broad breach of US aviation. which unfortunately got peoples hopes up in thinking i was behind the TSA problems and groundings a day earlier, but unfortunately im not quite that cool. so while i was waiting for someone to respond to my call for journalists i just kept digging, and oh the things i found.

as i kept looking at more and more config files in more and more of the projects, it dawned on me just how heavily i had already owned them within just half an hour or so. hardcoded credentials there would allow me access to navblue apis for refueling, cancelling and updating flights, swapping out crew members and so on (assuming i was willing to ever interact with a SOAP api in my life which i sure as hell am not).

i however kept looking back at the two projects named `noflycomparison` and `noflycomparisonv2`, which seemingly take the TSA nofly list and check if any of commuteair's crew members have ended up there. there are hardcoded credentials and s3 bucket names, however i just cant find the actual list itself anywhere. probably partially because it seemingly always gets deleted immediately after processing it, most likely specifically because of nosy kittens like me.

![heavily redacted example of a config file from one of the repositories](/img/posts/how-to-hack-an-airline/config-example.jpg)

fast forward a few hours and im now talking to [Mikael Thalen](https://twitter.com/MikaelThalen), a staff writer at dailydot. i give him a quick rundown of what i have found so far and how in the meantime, just half an hour before we started talking, i have ended up finding AWS credentials. i now seemingly have access to pretty much their entire aws infrastructure via `aws-cli`. numerous s3 buckets, dozens of dynamodb tables, as well as various servers and much more. commute really loves aws.

![two terminal screenshots composed together showing some examples of aws buckets and dynamodb tables](/img/posts/how-to-hack-an-airline/aws-overview.jpg)

i also share with him how close we seemingly are to actually finding the TSA nofly list, which would obviously immediately make this an even bigger story than if it were "only" a super trivially ownable airline. i had even peeked at the nofly s3 bucket at this point which was seemingly empty. so we took one last look at the noflycomparison repositories to see if there is anything in there, and for the first time actually take a peek at the test data in the repository. and there it is. three csv files, `employee_information.csv`, `NOFLY.CSV` and `SELECTEE.CSV`. all commited to the repository in july 2022. the nofly csv is almost 80mb in size and contains over 1.56 million rows of data. this HAS to be the real deal (we later get confirmation that it is indeed a copy of the nofly list from 2019).

holy shit, we actually have the nofly list. holy fucking bingle. what?! :3

![me holding a sprigatito pokemon plushie in front of a laptop screen showing a very blurry long csv list in vscode](/img/posts/how-to-hack-an-airline/weed-cat-crimes.jpg)

with the jackpot found and being looked into by my journalism friends i decided to dig a little further into aws. grabbing sample documents from various s3 buckets, going through flight plans and dumping some dynamodb tables. at this point i had found pretty much all PII imaginable for each of their crew members. full names, addresses, phone numbers, passport numbers, pilot's license numbers, when their next [linecheck](https://icadet.com/aviation-term/line-check/) is due and much more. i had trip sheets for every flight, the potential to access every flight plan ever, a whole bunch of image attachments to bookings for reimbursement flights containing yet again more PII, airplane maintenance data, you name it.

i had owned them completely in less than a day, with pretty much no skill required besides the patience to sift through hundreds of shodan/zoomeye results.

## so what happens next with the nofly data

while the nature of this information is sensitive, i believe it is in the public interest for this list to be made available to journalists and human rights organizations. if you are a journalist, researcher, or other party with legitimate interest, the data is available for access (upon request) [via DDoSecrets](https://ddosecrets.com/wiki/No_Fly_List).

[if you enjoyed this or any of my other work feel free to suppo...