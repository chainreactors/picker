---
title: Reverse-lookup service exposed millions of photos of people’s faces
url: https://www.wired.com/story/reverse-lookup-service-exposed-millions-of-photos-of-peoples-faces/
source: Instapaper: Unread
date: 2026-08-24
fetch_date: 2026-08-25T03:00:55.656715
---

# Reverse-lookup service exposed millions of photos of people’s faces

[Skip to main content](#main-content)

Menu

[WIRED](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[WIRED](/)

Account

Account

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Podcasts](/podcasts/)

[Video](/video/)

[Livestreams](https://www.wired.com/livestreams)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Lily Hay Newman](/author/lily-hay-newman/)[Matt Burgess](/author/matt-burgess/)

[Security](/category/security)

Aug 19, 2026 6:00 AM

# Reverse-Lookup Service Exposed Millions of Photos of People’s Faces

The people-search tool ClarityCheck says its reverse image search service is “private and secure”—but it left a database containing more than 9 million image files exposed.

![ReverseLookup Service Exposed Millions of Photos of Peoples Faces](https://media.wired.com/photos/6a43d616847560b1128c28ca/master/w_2560%2Cc_limit/Security_Data%2520Broker%2520Leak%2520Exposes%25208%2520Million%2520Photos%2520of%2520People%25E2%2580%2599s%2520Faces_v1.jpg)

Photo-Illustration: Jobanny Cabrera; Getty Images

Comment

Loader

Save StorySave this story

Comment

Loader

Save StorySave this story

When someone uploads a photo to the people-search tool ClarityCheck, the website has a clear message: “Your reverse image search is private and secure.” New [research](https://www.expressvpn.com/blog/clarity-check-data-exposed/), though, shows that the website left more than 9 million image files, including photographs of people’s faces, publicly [exposed](https://www.wired.com/tag/data-breaches/). And a second misconfiguration publicly exposed people’s email addresses and phone numbers.

Overall, according to findings from independent security researcher Jeremiah Fowler, the exposed ClarityCheck database contained roughly 450 GB of images, including what appeared to be profile images, screenshots, and other photographs of adults, teenagers, and children. All of the images were stored in an unsecured Amazon S3 bucket, with files in folders named “faces” and “profiles,” which could be accessed by anyone online through a URL included in the company’s publicly available website code.

ClarityCheck is one of a number of so-called people-finder tools that have appeared online in recent years. These websites broadly claim to be able to search the web, public records, and other databases to identify individuals. ClarityCheck’s website says it can run searches on phone numbers, email addresses, vehicle identification numbers, and names. Its photo-search page says it can help “identify anyone in a photo” and find social media profiles “in seconds.”

While ClarityCheck secured the giant image database after WIRED contacted the company in July, Fowler warns that it was seemingly exposed for months, and his initial efforts to flag the problem to the company were unsuccessful. Accidental data exposures create risk for any personal information, but particularly for sensitive and unchangeable biometric data like face images.

And while ClarityCheck’s website requires people to attest that they have permission to upload photos to its site, Fowler points out that in practice, people whose faces were exposed may have had no idea that ClarityCheck held their image. After all, he notes, the service is explicitly designed for identification, and people don’t typically seek to identify themselves or people they know.

“If you’re trying to find out who a person is, you might not have authorization or permission, so people might not know that their image had been dumped into this database that was public,” Fowler tells WIRED. “An AI bot could crawl it, extract faces, and use them for training. And there are lots of pictures of kids in there.”

In a statement sent to WIRED, a spokesperson said that ClarityCheck appreciated Fowler’s efforts to alert the company about the issues. “Once this was drawn to the attention of the appropriate teams, we acted immediately to restrict access,” the spokesperson said.

The company disputed any characterization that the data was “exposed,” saying that an “ordinary member of the public” would not have come across it. “We do not accept that data in the temporary storage location was ‘publicly exposed,’ which implies large-scale public access,” the spokesperson says. “Access required knowledge of a specific, unindexed URL that was not discoverable through ordinary use of the ClarityCheck service or a general web search.”

The security industry broadly, as well as [the US federal government](https://www.cisa.gov/resources-tools/resources/exposure-reduction) specifically, considers data to be exposed if it could be accessed by people who are not intended to have access—particularly if it is reachable on the open internet without being protected by an authentication requirement, such as a username and password. “Exposure is the state in which personal or sensitive data has been left accessible, discoverable, or otherwise put at risk of unauthorized access, whether or not anyone has yet taken or misused it,” says Mark Beare, head of consumer products at the security company Malwarebytes. “A publicly reachable database backup, a misconfigured storage bucket, or credentials sitting in a system that a researcher can reach are all exposures.”

“There is no suggestion of malicious access, as the researcher notes,” the ClarityCheck statement continued. “The data involved includes duplicate, cropped, and resized copies of the same files, along with non-image data, not 9 million unique images.”

The company added that it has “improved” its security reporting procedures to help other researchers contact the company in the future.

In addition to the face data, ClarityCheck had also misconfigured its APIs such that its website URLs could be manipulated to reveal data about people simply by entering names; anyone using any consumer browser could have done this. Entering a name into one of the URLs would return multiple potential email addresses, physical addresses, and phone numbers for people with that name. After WIRED contacted the company, the URLs were secured. The ClarityCheck spokesperson said in the statement that the details displayed were “sourced from publicly available information and licensed third-party data providers.”

ClarityCheck’s face-search feature allows people to upload an image and then receive a “report” about where that image may appear online and who may be shown in the photo. When a WIRED reporter tested the system using their own face image, the website said it was “scanning facial landmarks” and “mapping unique face geometry” before matching the image to others online and offering a report that could include a full name, addresses, location history, public appearances, photos, videos, social media profiles, and “hidden dating profiles” for a fee. The resulting report named the reporter, provided a biography, and linked to multiple photos of them online.

Misconfigurations and accidental exposures are unfortunately common online, but as digital platforms offer more and more [automated capabilities](https://www.wired.com/story/thousands-of-vibe-coded-apps-expose-corporate-and-personal-data-on-the-open-web/) for collecting and analyzing sensitive personal data, the stakes grow ever higher for securing information.

“Systems that rely on highly sensitive personal info...