---
title: An “invisible” car? Researcher uses machine learning to hide vehicles from Flock cameras
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/invisible-car-machine-learning-hide-vehicle-flock-cameras
source: GRAHAM CLULEY
date: 2026-08-17
fetch_date: 2026-08-18T02:53:54.980549
---

# An “invisible” car? Researcher uses machine learning to hide vehicles from Flock cameras

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

2 min read

# An "invisible" car? Researcher uses machine learning to hide vehicles from Flock cameras

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

August 17, 2026

  ![An "invisible" car? Researcher uses machine learning to hide vehicles from Flock cameras](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/08/invisible-car.jpeg "An \"invisible\" car? Researcher uses machine learning to hide vehicles from Flock cameras")

A cybersecurity expert has demonstrated how computer-generated patterns can successfully prevent surveillance cameras from detecting vehicles - such as the controversial AI-powered Flock licence plate readers that are becoming increasingly common on American streets.

Bill Swearingen, founder of SIXCYBER, has spent the past year running an impressive 31 million tests developing what he calls [noRecognition](https://sandbox.norecognition.org/research). noRecognition is a reinforcement learning model that generates patterns capable of defeating the algorithms built into surveillance cameras to detect objects.

The patterns do not prevent cameras from actually recording footage, so a human watching the video would still see a car. But what fails is the software use to identify objects, logs vehicle licence plates, and triggers alerts.

Earlier this month at the DEF CON security conference in Las Vegas, Swearingen demonstrated the technique for the first time in public. He wrapped a 2009 Toyota Yaris in one of his newest patterns and drove it past a live Flock camera. Although the camera correctly recorded the vehicle, its detection software logged nothing.

"We proved it was effective," Swearingen [told *TechCrunch*](https://techcrunch.com/2026/08/09/this-adversarial-pattern-can-prevent-surveillance-cameras-from-detecting-you/), although he noted that the vehicle's wheels presented a challenge.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2026/08/car.jpeg)

So, how does the vehicle avoid detection by the camera's software?

Swearingen set up a system that tested generated patterns against camera detection software. When a pattern was spotted, the system adjusted and tried again. And again. And again... After 31 million attempts, it had worked out a pattern which avoided detection.

The system has now been tested against 11 open-source detection algorithms, including the software behind Flock licence plate readers, Axon body-worn cameras, and cameras running Clearview AI's facial recognition system. According to Swearingen, it beats all of them.

Swearingen says he is continuing to generate new patterns which avoid detection every minute, and is deliberately keeping the strongest ones offline to prevent camera manufacturers from training against them.

Flock is selling automated licence plate recognition cameras to police departments across the United States, who use them to photograph passing vehicles and cross-reference plates in real-time against law enforcement databases.

The network has expanded rapidly, and earlier this year it was revealed that Flock had proposed enlisting 350,000 Uber and Lyft dashcams to scan cars nationwide. The company's actions have caused a backlash amongst privacy campaigners.

One issue is that Flock cameras can be inaccurate, with innocent drivers finding themselves pulled over at gunpoint following incorrect plate matches.

Swearingen says he started the project after wanting to attend a protest and feeling uncomfortable about being tracked.

"Privacy is a fundamental right," he told *TechCrunch*, explaining that he believes the patterns are a way for people to "opt out of being tracked."

Obscuring a number plate, of course, is illegal. And so the noRecognition patterns cover the body of the car, but not the number plate itself.

Whether covering a car's bodywork in a printed pattern designed to fool surveillance camera software might itself become an offence remains to be seen.

tags

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

---

### Author

---

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=150&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[## Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s.

[View all posts](/en-us/blog/hotforsecurity/author/gcluley)

---

## You might also like

#### Bookmarks

---

![loader](https://download.bitdefender.com/resources/themes/draco/images/lite_v2/blog-images/loader-white.svg "loader")

[Legal Information](https://www.bitdefender.com/site/view/legal-terms.html "Legal Information") | [Privacy Policy](https://www.bitdefender.com/site/view/legal-privacy-policy-for-bitdefender-websites.html "Privacy Policy") | [Contact Us](https://www.bitdefender.com/site/Main/contact/1 "Contact Us")

Copyright © 1997 - 2026 Bitdefender.