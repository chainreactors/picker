---
title: When South Park's Restaurant Had Worse Security Than Cartman's Password
url: https://bobdahacker.com/blog/i-hacked-southpark
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:36.060448
---

# When South Park's Restaurant Had Worse Security Than Cartman's Password

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# When South Park's Restaurant Had Worse Security Than Cartman's Password

August 17, 2025

BobDaHacker

*They fixed it after my friend who runs a company partnered with South Park had to personally contact them.*

## Oh My God, They Killed Privacy! You Bastards!

I'm a huge South Park fan, so when I decided to check out Casa Bonita's website (the legendary Denver restaurant that Matt Stone and Trey Parker bought and renovated), I wasn't expecting to find their entire customer database exposed.

But here we are.

### Respect My Authority! (The Founders Club Had None)

For context, Casa Bonita's Founders Club is their exclusive membership program for early supporters. You got in by signing up for their email list before initial reservations opened - basically the people who were excited enough to sign up sight unseen when Matt and Trey first announced they bought the place. Members get perks like early reservation access, discounts at the Mercado, exclusive event invitations, and a personalized membership card. These are the restaurant's most loyal customers.

Their admin panel for managing these VIP members at `tfc-admin.casabonitadenver.com` was... interesting:

**No password required** - The email list of all these loyal Founders Club members was just sitting there, accessible to anyone

Here's what the TFC admin panel looked like (luckily archived on the Wayback Machine before it hit production - just test emails):

![TFC Admin Panel](/static/images/blogs/casabonita/tfc_admin1.png)
![TFC Admin Panel](/static/images/blogs/casabonita/tfc_admin2.png)
*The Founders Club admin panel showing member emails and invite codes*

Another funny thing is anyone could become a founder member really easily, the Founders Club registration was handled through Supabase, and they left the Supabase signups completely open, even after they stopped sending out founder club invites. Creating an account automatically triggered the membership card process.

## Screw You Guys, I'm Going Into Your POS System

The real treasure trove was at `service.casabonitadenver.com` - their actual point-of-sale and management system.

First, I found the registration was "disabled":

![Casa Bonita Registration Page](/static/images/blogs/casabonita/register_form.png)
*The registration form was blank, but...*

But the API endpoint still worked perfectly:

![Registration API Call](/static/images/blogs/casabonita/register_api.png)
*Just call the API directly and you're in*

### I'm Not Fat, I'm Big-Boned (With Admin Privileges)

With my newly created admin account (that took 30 seconds to make), I had full access to their POS system. I could:

**1. Search and view all customer data:**

![Customer Search](/static/images/blogs/casabonita/customer_search.png)
*Search for any customer - shows emails, phones, everything*

![Customer List](/static/images/blogs/casabonita/customer_list.png)
*Customer Search by RFID Bracelet Token, most likely their pos computers automatically enter it into the field, if the token is not valid it lets you search by name*

**2. Access any reservation by just incrementing IDs:**

![Reservation Details API](/static/images/blogs/casabonita/reservation_view.png)
*Reservation 16004 showing payment amounts, tips, personal info*

**3. Manage customer tabs and transactions:**

![Customer Tab Management](/static/images/blogs/casabonita/tab_management.png)
*Full control over customer tabs, payments, and experiences*

**4. Create products in their system:**

![Product Creation](/static/images/blogs/casabonita/product_create.png)
*Could add any product to their inventory system*

and more

The reservation data was particularly bad - I could see:

* Full names, emails, phone numbers
* Exactly how much each customer paid
* How much they tipped (awkward)
* Their Shopify reference numbers
* Table locations and guest counts

With incrementing IDs, I could literally enumerate through every single reservation they'd ever had.

### With Great Power Comes Great Sopapillas

Casa Bonita had no security contact. No security.txt. Nothing.

I first emailed all parkcounty.com emails I could find and all emails that had access to the POS system. I didn't get a response in one day and this was really bad so I had to get creative.

I reached out to a friend who's the CEO of a company that had partnered with South Park before. They said they'd pass it along, and then told me South Park said "they would get back to me to thank me".

They fixed it quickly (good!), but never got back to me (classic).

### To Casa Bonita

Thanks for the quick fixes. A security contact would help researchers report issues more easily in the future.

Matt and Trey did an amazing job renovating the restaurant - the digital infrastructure deserves the same care.

---

*P.S. - Six months later, a Casa Bonita Founders Club membership card randomly showed up in the mail. Totally threw me by surprise - I had no idea that was coming. Turns out when you sign up through their open Supabase endpoint, it automatically triggers their membership card fulfillment process. I guess they can't stop it once it's in the system. I'm guessing they're paying for the cheapest possible shipping to save money, which is why it took 6 months. LOL.*

[home](/)
[blog](/blog)

© 2025 bobdahacker