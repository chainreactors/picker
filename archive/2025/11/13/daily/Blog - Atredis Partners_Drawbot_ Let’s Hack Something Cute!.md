---
title: Drawbot: Let’s Hack Something Cute!
url: https://www.atredis.com/blog/2025/9/30/drawbot-lets-hack-something-cute
source: Blog - Atredis Partners
date: 2025-11-13
fetch_date: 2025-11-14T03:12:38.154702
---

# Drawbot: Let’s Hack Something Cute!

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# Drawbot: Let’s Hack Something Cute!

Nov 13

Written By [Jessie Chab](/blog?author=681e1537728d000ec6ae86e5)

## The Target

A few months ago I realized I was overdue for a fun, quirky hardware project. Every so often I like to see what new and interesting electronic children's toys are out there. When looking, I keep in mind the potential attack surface, typically preferring toys with companion mobile apps, wireless communications, or any other added complexity.

I came across these robots that draw from a set of pre-defined images. They all come with a pack of 100 or 150 cards, and the drawings appear very similar across brands. The attack surface seemed especially small, given that it uses pre-defined physical cards, so I wouldn't be able to snoop an FCC ID for this one and peek its sweet sweet innards (I consider those spoilers anyway). Regardless, it seemed like an interesting target and I couldn't resist.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/8b343437-35c3-4480-895a-d89a601af0af/drawbots-amazon.png)

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/774007fb-419c-4b89-bee0-75dee39d5aa6/box.png)

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/d1d72913-dc1f-4836-92d9-f3a63dac41a8/cards.JPG)

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/a9869977-2f55-42b2-988a-51b91c680d53/drawbot-in-action.jpg)

I picked this one because it had the best face. The wording/typos on the box were definitely a good sign that there was some quirkiness afoot. It came with a stack of 100 cards, each with a very minimal "barcode" consisting of 8 bits of information, meaning 256 possible barcodes/drawings. The cards were separated into five categories: food, animal, plant, vehicle, and circle (obviously). I loaded up the “bulbous cactus” card and sent it on its way. It talked. It sang. It’s perfect.

Let us commence the evisceration.

## Tearing it Down

If I'm being honest, this is my favorite part.

On the bottom we have a few ultra-recessed screw-holes. You'd think at this point I'd be properly equipped to deal with these, but I'm not. Without fail, every hardware assessment helps me realize what I still don't have (besides patience). No matter how many specialized tools or components I amass in my home lab, there's always something that I end up having to buy. At this point I could have easily purchased what I needed for same or next-day delivery, but that would require patience. I could have probably 3D printed something to do the job. Again, I'm not that patient.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/5c4a1c1f-0608-47b4-93a2-553c389c2e93/ultra-recessed-screwhole.JPG)

What I lack in patience I make up for in power tools. I ended up using a combination of, well, drilling the hole slightly bigger to clear some of my screwdriver bits, and chaining bits together.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/8c7a38a3-4cf3-465d-b122-760af4e93c0c/unscrew-rig-both.png)

With the four recessed screws removed, the top half popped off without much additional trouble.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/0ddca391-2aa5-46a2-8173-fecff1676ec9/main-board02.JPG)

With the barcode reader exposed, I tried some very basic preliminary fuzzing by taking a valid card and shifting it around to provide unexpected input. When a card is placed over the sensors, the device makes a sound and then announces the associated image.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/3b962ebc-3581-434b-b1d0-65ccbd94a0cd/take-a-bath.jpg)

While fuzzing, various images were announced, all of which seemed to match up with other cards I had seen in the deck, until the robot announced "Take a bath!" This seemed odd (and mildly offensive), so I rummaged through the deck and could not for the life of me find any cards with bath imagery.

With the card held in place, I pushed the button to initiate drawing. The robot started singing and, surely enough, drew this image:

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1e6be10b-d63b-465e-a71a-210c15760981/bath-time.jpeg)

## Goals

Now that I had a decent idea what I was working with, I set the following two goals for myself:

1. Enumerate and identify all available drawings. The cards clearly don’t tell the whole story here.
2. The classic goal at Atredis: Put a Bird on It™ (i.e. figure out how these drawings are represented and stored, and use this information to add our own).

## Components

My next step was to identify the components on the board and see what I could gather/dump. The three juicy ones are labelled below.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/f0cd51ce-e59f-454c-9b25-063348d2b3aa/teardown-labelled-minimal.png)

* LKS32MC07x - ARM Cortex-M0 MCU
* uc25IQ64 - 64MB SPI NOR flash
* uc25IQ128A - 128MB SPI NOR flash

I was able to dump the 64MB flash via its SPI interface, had no luck with the 128MB flash, and also had no luck connecting to the MCU via SWD. Not a great start, but i was undeterred.

## Barcode Analysis

Using a multimeter and the printed trace lines, we can map the connections for the optical sensors that read the barcode to determine which card is inserted.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/ffda2b29-de60-48ae-9d47-af1d6863cfb3/barcode-new.jpg)

I was initially stumped by the fact that there was some overlap between the sensors and the pins. In my research, I came upon the concept of input multiplexing. Essentially, the board will power sensors 1-5 using VCC 1, then read the values on the input pins. Then it powers sensors 6-8 using VCC 2, and reuses the same input pins to read those values.

To test this theory, I decided to hook a logic analyzer up to the various inputs. To keep myself sane, I replaced the original all-red-wired connector with two sets of color-coded custom ones broken out to a breadboard with two rows of headers between them. This setup would facilitate both passive analysis and active signal manipulation simultaneously.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/6133161a-9233-4f26-8388-97598149fcd6/sensor-breakout.JPG)

Sure enough, the VCC lines alternated at a regular cadence, lending massive credibility to the multiplexing theory.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/97f94fbb-385d-4c70-8122-09cad94194a6/cycle-table.png)

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/d2f78baa-f364-4c08-9ff6-14843b3eaefc/vcc-multiplex-trim.png)

With everything connected to the Saleae, I could now observe the behavior when a card was scanned. I chose the card corresponding to barcode value 00000001 to hopefully make the data more obvious to recognize. With the crab card in place, I would expect the rightmost sensor to register the HIGH v...