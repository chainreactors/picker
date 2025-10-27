---
title: An Innocent Picture? How the rise of AI makes it easier to abuse photos online.
url: https://blog.nviso.eu/2023/04/04/an-innocent-picture-how-the-rise-of-ai-makes-it-easier-to-abuse-photos-online/
source: NVISO Labs
date: 2023-04-05
fetch_date: 2025-10-04T11:30:26.225468
---

# An Innocent Picture? How the rise of AI makes it easier to abuse photos online.

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# An Innocent Picture? How the rise of AI makes it easier to abuse photos online.

[Jonas Bauters](https://blog.nviso.eu/author/jonas-bauters/ "Posts by Jonas Bauters")

[AI](https://blog.nviso.eu/category/ai/), [Awareness](https://blog.nviso.eu/category/awareness/), [Artifical Intelligence](https://blog.nviso.eu/category/artifical-intelligence/)

April 4, 2023April 26, 2023
10 Minutes

## Introduction

The topic of this blog post is not directly related to red teaming (which is my usual go-to), but something I find important personally. Last month, I gave an info session at a local elementary school to highlight the risks of public sharing of children’s pictures at school. They decided that instead of their photos being publicly accessible, changes would be implemented to restrict access to a subset of people. However, there are many more instances of excessive sharing of information online; photographers’ portfolios, youth/sports clubs, [sharenting](https://www.nbcnews.com/better/lifestyle/sharenting-how-safeguard-your-kids-personal-information-social-media-ncna1058006) on social media, etc.

There are many risks stemming from this type of information being openly available, and the potential risks have only increased with the rise of artificial intelligence. Since you are reading this post on the NVISO blog, I’m assuming you are more cyber-aware than the average person out there and therefore perfectly positioned to use the takeaways from this post and spread the word to others. Obligatory Simpsons reference:

![](https://blog.nviso.eu/wp-content/uploads/2023/03/image-1.png)

Since the children themselves may not have a say in the matter yet and the people who do may not be aware of the possible dangers, it’s up to us to think of the children!

## Traditional Risks

When thinking of the risks linked to the presence of children’s pictures online, an obvious threat is the type of person that might drive a van like this:

![](https://blog.nviso.eu/wp-content/uploads/2023/03/image-2.png)

There are three traditional risks we will be discussing here:

* Kidnapping
* Digital Kidnapping
* Pornographic Collections

### Kidnapping

How does a picture of a child pose a risk for physical kidnapping? First of all, a picture could give away a physical location, for example due to the presence of street signs/names, recognizable elements such as shops, bars, monuments, schools, etc. If this is a location frequented by the child, a possible child predator could identify an opportunity for kidnapping there.

In case no identifiable elements are present, certain people might still giveaway the location due to oversharing. Imagine a picture on a Facebook profile that is publicly accessible with comments such as “birthday party at …”, “visiting grandma & grandpa in …”, “always a fun day when we go to …”. Often-visited locations can be deduced from comments like these.

Finally, a more technical approach is looking at the picture’s metadata, which often gives information about the type of camera that was used, shutter time, lens, etc. but can also contain an exact location where the picture was taken. No additional research is required to figure out where the child has been.

### Digital Kidnapping

With [digital kidnapping](https://www.parentmap.com/article/kidnappers-kids-photos-digital-kidnapping-social-media), the victim is affected by some type of identity fraud. Pictures of the child are stolen and reused by people online on their own social media, often pretending to be related to the children. An example could be an adoption fantasy, reposting pictures of the child for likes and comments without the child or its parents knowing about this.

Another, more dangerous form of digital kidnapping consists of a sexual predator reusing the victim’s pictures to target other possible victims. Someone could pretend to be a young child themselves to lure other children into meeting with them online or sharing potentially explicit pictures.

### Pornographic Collections

Continuing on the topic of potentially explicit pictures, it is not a secret that the Dark Web is full of pornographic pictures of children. However, pictures that you or I would not consider to be risky or explicit could end up in such collections as well. [Holiday pictures](https://www.stuff.co.nz/sunday-star-times/latest-edition/782095/Warning-over-kids-holiday-photos-on-internet) of children in swimsuits are happily shared by child predators in an attempt to fulfill their fantasies. They search through social media to identify such pictures, sharing them among each other along with sexual fantasies. With pictures of a certain child, they might search for pictures of lookalike children to add to their fantasy. With only a textual story, they might search for pictures of children that match the story.

However, these risks have been existent for a number of years already. What’s more dangerous is that the life of a child predator looking for pictures has been facilitated with rise of artificial intelligence.

## Next-gen Risks

So what is the problem with public pictures? Not only can they be retrieved by anyone browsing the web, but they can and will also be gathered by automated systems through concepts called spidering and scraping. These activities aren’t particularly nefarious and actually part of the regular functioning of the web, used by search engines for example. However, other applications can make use of these same techniques and have already done so to create massive collections of pictures, even those you would not expect to be public, such as [medical records](https://arstechnica.com/information-technology/2022/09/artist-finds-private-medical-record-photos-in-popular-ai-training-data-set/)

### Facial Recognition

One such example is [ClearView AI](https://www.businessinsider.com/clearview-scraped-30-billion-images-facebook-police-facial-recogntion-database-2023-4?r=US&IR=T), which is aimed at law enforcement by applying its facial recognition algorithm to a huge collection of facial images to help with investigative leads. However, for the broader public, a similar application has become available, allowing anyone to upload a picture and receive an overview of other pictures with matching faces. While probably having legitimate use cases, [PimEyes](https://pimeyes.com/en) provides people with less honorable intentio...