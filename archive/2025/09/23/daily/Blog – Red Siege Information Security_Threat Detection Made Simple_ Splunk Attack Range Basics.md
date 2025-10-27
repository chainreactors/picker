---
title: Threat Detection Made Simple: Splunk Attack Range Basics
url: https://redsiege.com/blog/2025/09/threat-detection-made-simple-splunk-attack-range-basics/
source: Blog – Red Siege Information Security
date: 2025-09-23
fetch_date: 2025-10-02T20:31:07.400553
---

# Threat Detection Made Simple: Splunk Attack Range Basics

Register Now For On-Demand Training!

[Learn More](https://training.redsiege.com)

[![](https://redsiege.com/wp-content/uploads/2022/01/redsiege-logo-300x73.png)](https://redsiege.com)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

![](https://redsiege.com/wp-content/themes/red-siege-theme/img/icon-phone.svg) +1 234-249-1337

# Threat Detection Made Simple: Splunk Attack Range Basics

By Red Siege | September 22, 2025

![](https://redsiege.com/wp-content/uploads/2025/09/threatdetection.png)

Table of Contents

Toggle

* [Three Simple Commands](#Three_Simple_Commands)
* [Let’s Build Us an Empire](#Lets_Build_Us_an_Empire)
* [Let’s talk about cost really quick](#Lets_talk_about_cost_really_quick)
* [Let’s simulate our first attack!](#Lets_simulate_our_first_attack)
* [Keep the AWS Boogie Man Bill Away](#Keep_the_AWS_Boogie_Man_Bill_Away)
* [Big Recommendation](#Big_Recommendation)
* [What’s next?](#Whats_next)
  + [About Ian Briley, Security Consultant](#About_Ian_Briley_Security_Consultant)

**by Ian Briley**

Let’s be honest, when starting a new skill or interest, one of the largest hurdles is setting up an environment//playground//attack range for your learning activities. Sometimes it feels like you spend 95% of the time setting up the environment, troubleshooting why some tool isn’t talking to another tool, dealing with finding and using licenses, etc. These are all valuable lessons learned, but not when you’re trying to at least get your feet wet.

My preferred method is finding a way to get my feet into the water as quickly as possible, and later on discover why wet feet are important to the process. This is how I’m approaching starting my learning journey with Threat Detection. I think, “I may like this, let’s find a (mostly) frictionless way to dip my feet into threat detection.”

Please welcome to the stage:

[Splunk Attack Range](https://redsiege.atlassian.net/wiki/spaces/RSM/pages/444104718/Babys%2BFirst%2BThreat%2BDetection%2BSetup%2Band%2BMimikatz#Splunk-Attack-Range)
![](https://redsiege.com/wp-content/uploads/2025/09/baby1-300x214.png)

After passing through the dead remains of [DetectionLab](https://github.com/clong/DetectionLab), finding old setup guides, dead links, references to other projects using software stacks that require more tinkering for set up. I finally found the [Splunk Attack Range](https://github.com/splunk/attack_range). This checks ALL of the boxes.

* Uses a well-known SIEM (Actually useful resume candy)
* Splunk has a TON of tutorials (most of which are free)
* Uses AWS/Cloud Technology (costs less than $0.50 an hour, no Frankenstein PCs on my network)
* Everything is contained in Docker (Mess something up? Destroy the range and restart docker)
* Has range guides, and a fairly large community support.
* Written mostly in Python so I can actually fix things if need be (although I didn’t need it)

Spoiler Alert: I was able to set this range up in about 45 minutes, and only about 5 minutes of that was hands on keyboard configuration setup.

So, let’s get our feet into the water!

### Three Simple Commands

Just use Docker. Docker is and probably will always remain magic to me, good news is you just need to run these three commands to start our lab journey.

This command will pull the latest and greatest Splunk Attack Range.
`docker pull splunk/attack_range`

![](https://redsiege.com/wp-content/uploads/2025/09/baby2-300x173.png)

Download the Docker container

Now we’ll use the next command to run the docker instance to create our environment.
`docker run -it splunk/attack_range`

![](https://redsiege.com/wp-content/uploads/2025/09/baby3-300x131.png)

Run the Docker container

Finally, we will configure AWS inside of the Docker instance. (I find AWS easier to use then the other cloud platforms) You’ll need to create a key pair in the AWS console for this. [There’s tons of guides how to get this](https://docs.aws.amazon.com/keyspaces/latest/devguide/create.keypair.html). The big thing you want to pay attention to is the zone you choose here **NEEDS** to match the zone you configure the range for. I use **us-east-1** because I’m on the east coast.
`aws configure`

![](https://redsiege.com/wp-content/uploads/2025/09/baby4-300x51.png)

Configure AWS

Now we’re ready to actually setup and build the range. This next command will be the bulk of the hands on keyboard time for the setup.
`python attack_range.py configure`

![](https://redsiege.com/wp-content/uploads/2025/09/baby5-300x255.png)

Starting our setup

You’ll run through a list of choices in the screenshot below is what I ended up doing that worked the best out of the box for me. For starting out all we really need is a Windows Server feeding Sysmon logs to a Splunk Server.

As shown in the screenshot below, I chose AWS as my cloud provider, because, as I said before, I think it’s the easiest to work with, and I also kept the randomly-created range password.

![](https://redsiege.com/wp-content/uploads/2025/09/baby6-300x141.png)

Use the password given

Create an SSH key, the program should pull your region from the AWS configuration automatically. Only allow your home IP to connect to it. Again the program should pull this automatically for you and throw it into a CIDR /32 as shown below.

![](https://redsiege.com/wp-content/uploads/2025/09/baby7-300x141.png)

Make sure your IP can access

Give it a name, it doesn’t matter these environments at most live only 8 hours. Say “Yes” to building a windows server, select 2022, say “Yes” to making it a DC, and installing “red team tools” on to it. This will help us simulate attacks later on.

Then say “No” to everything after the “red team tools”. It’s VERY tempting to want to use [badblood](https://github.com/davidprowe/BadBlood) right off the bat to populate our testing domain with AD objects and configurations.

![](https://redsiege.com/wp-content/uploads/2025/09/baby8-300x144.png)

Say NO to BadBlood

But when I tried to do the badblood module, I would get an error like the one shown in the screenshot below. I’m sure this is normal but for just starting out I want to make sure everything can be logged into and checked manually if need be. This will be useful later on down the road, for doing things like making detections for someone accessing an admin account outside of business hours, but it’s not necessary for just getting our feet wet.

![](https://redsiege.com/wp-content/uploads/2025/09/baby9-300x123.png)

Can’t RDP to Admin User when BadBlood was enabled

###

### Let’s Build Us an Empire

Having configured our Splunk Attack Range, we’ll run the following command and wait for it to finish (took about 40ish minutes for me.) You’ll see a bunch of lines of text showing what’s being installed and set up. The way we have it configured currently it’ll set up a DC, a Splunk server, red team attacker tools, and will have a Guacamole session manager installed.
`python attack_range.py build`

![](https://redsiege.com/wp-content/uploads/2025/09/baby10-295x300.png)

Build Start

![](https://redsiege.com/wp-content/uploads/2025/09/baby11-300x187.png)

Verbose Output

You won’t really need to pay attention to anything in this until the very end (assuming everything is set up correctly). You can also pull this information up by running the following command after the setup is complete.
`python attack_range.py show`

![](https://redsiege.com/wp-content/uploads/2025/09/baby12-300x187.png)

Got our connection information

We can use thi...