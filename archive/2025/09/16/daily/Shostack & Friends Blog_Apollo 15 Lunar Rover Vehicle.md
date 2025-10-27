---
title: Apollo 15 Lunar Rover Vehicle
url: https://shostack.org/blog/apollo-15-lrv-boeing/
source: Shostack & Friends Blog
date: 2025-09-16
fetch_date: 2025-10-02T20:11:44.233006
---

# Apollo 15 Lunar Rover Vehicle

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Apollo 15 Lunar Rover Vehicle

Shostack + Friends Blog

# Apollo 15 Lunar Rover Vehicle

What can a signed Apollo 15 print teach us about modern threat modeling and risk management?
![Astronaut Jim Irwin in front of Apollo 15 and a moon rover](/images/blog/img/2025/as15-88-11866-signed-1000w.jpeg)

I was thrilled to find this photo at a thrift store. There’s a
typewritten letter on the back from Earl Houtz, LRV program
manager, which is .. not exceptionally personal, leading me to think this
could have been one of several sent to the LRV team. I imagine it hung on a wall at
Boeing, went home with someone during a re-org and ended up at a
thrift shop. I want to reflect a little on what the photo shows us
about high-risk technology development.

### The Photograph

Before I get there, let me talk about the photograph. I was able to track down exactly when it was
taken because the Apollo missions are well documented with [audio transcripts](https://www.nasa.gov/history/alsj/a15/images15.html#11866) and [photograph collections](https://www.nasa.gov/history/alsj/a15/images15.html). I
first thought that it was a colorized version of
[AS15-92-12446](https://www.flickr.com/photos/projectapolloarchive/51357004387/) but Jim Irwin is
a little far from the flagpole for that to be a match. (See the [EVA 2 transcript](https://www.nasa.gov/history/alsj/a15/a15.clsout2.html).) I’m now
confident that it’s a print of [as15-88-11866](https://www.nasa.gov/wp-content/uploads/static/history/alsj/a15/AS15-88-11866HR.jpg) because it’s a
wider field than [as15-88-11865](https://www.flickr.com/photos/projectapolloarchive/21471856630). The
[Flickr version](https://www.flickr.com/photos/nasa2explore/9356408741) has a nice
description, but less color intensity than the [NASA.gov version](https://www.nasa.gov/wp-content/uploads/static/history/alsj/a15/AS15-88-11866HR.jpg), which is
surprising because the Flickr version is from NASA’s Johnson Space Center.
A comment in NASA’s [Lunar Surface Journal](https://www.nasa.gov/history/alsj/a15/a15.eva3prelim.html) says “Few Apollo photographs
have been reproduced more often than this color photo of Jim, the
flag, the Rover, and the LM, with Mt. Hadley Delta in the
background. Note the bright, rectangular pattern on the high-gain
antenna. The pattern is produced by sunlight reflected by the
mirrored tiles on the top of the TV camera. A detail shows that
Jim has a strap-on pocket on each thigh.”

It’s interesting that film was so precious that the [film magazine](https://www.flickr.com/photos/projectapolloarchive/albums/72157658592471809/with/21471905148) takes us all the
way from the start of EVA-3 to the start of the trip back to Earth
— you can see the moon shrinking as the frames progress.

### The inscription

Having contextualized the picture, I want to talk about the
inscription at the bottom. It reads: “To the Boeing Team with many
thanks for the contributions to the success of Apollo 15.”

The Apollo program employed over 400,000 Americans across the
country, including workers at Boeing who made the Lunar Rover and
Playtex in Massachusetts, who hand-sewed the iconic
spacesuits. Many of the astronauts made a point of visiting local
manufacturers wherever they traveled to encourage them to
recognize the dangers and make sure what they made was ... higher
quality than was typical from low-bid government contractors.

The human end of managing and
aligning 400,000 people means that, as many technical challenges
existed, many of the challenges weren’t technical. In [Project Apollo: The Tough Decisions](https://amzn.to/3TSLED0), NASA
assistant administrator Robert Seamans presents what he saw as the
tough decisions in the program. They were about how to structure centers,
the complexity of dealing with contractors, and the like. These sorts
of decisions have a great deal in common with decisions companies need
to make today about how they’ll deliver. Roughly the only technical
decision that Seamans recounts was the deeply technical single
vehicle/multi-vehicle debate. Seamans credits von Braun for agreeing
that his single vehicle approach was less likely to succeed and
ending the debate.

I see this picture and the autographs as parts of that
process. Thanking the Boeing team for making the mission
successful is something they could tell their kids about. Hanging it
on an office wall tells people that what they do here is
important. Find it also tells a story about Boeing: Someone
let this go when they cleaned out an office.

### Risk

One of the themes I’ve been exploring recently is that risk measurement is
dependent on iterations. That’s both part of how we might talk about it
(“one in ten”) and that we can test if our predictions are
correct. If we then have roughly ten instances and the thing
happened in one of them, we had a good prediction. If it happened in six or seven, we
learn that our risk assessment was not very precise. For more on
this, see my [risk is not a hammer](https://shostack.org/blog/risk-is-not-a-hammer-usenix-enigma/) talk at Usenix.

Apollo pushed the bounds of what was possible, and involved a lot
of very expensively checking on future dangers. Could a spacecraft
navigate to the moon and back? Were there unforeseen dangers in
trying to dock in lunar orbit? Could the computer function as a
useful pilot assistant? David Mindell covers the fascinating technical and
human challenges of creating and using that function in [Digital Apollo](https://amzn.to/3TSLED0).

Breaking down the new hazards into multiple missions was referred to
as “buying down risk.” The decisions about which hazards to bundle
was a matter of balancing the danger with the goal of beating the
Russians and Kennedy’s deadline (“by the end of this decade.”) There was no
reasonable or satisfying way to quantify the dangers involved. So
they settled for “it worked once.” And in fact, each time
something was shown to be feasible was a reduction in risk, even
if that reduction was impossible to quantify.

![The Lego version of the rover, folded up](/images/blog/img/2025/lego-rover-folded-837w.png)

Back to the real thing, and risk: The LRV was an example of adding hazards. It added both weight and
mechanical complexity, and if it had failed, the astronauts might
well have been stranded with limited oxygen far from the
lander. The mechanical complexity is well-reflected in the Lego
model. The Lego wheels fold up to a flight configuration, and that model
was very complicated to build, even though it doesn’t account for the electrical
cabling. I do want to mention, I learned a lot about the rovers by building the incredibly fun [LEGO
Apollo LRV (42182)](https://amzn.to/4nUjMMF). The LRV may be my second favorite NASA
Lego kit, after the [Saturn V](https://amzn.to/4gpXIWO).

As in any good risk calculation, there was also a reward: The
astronauts could go further, get to sites that wouldn’t have
been accessible on foot, and carry more tools with them and rocks back.

Most of the good histories of the Apollo program blend the
technical, economic and managerial aspects into one story. And
those factors are in any interesting technology
project. Motivating people t...