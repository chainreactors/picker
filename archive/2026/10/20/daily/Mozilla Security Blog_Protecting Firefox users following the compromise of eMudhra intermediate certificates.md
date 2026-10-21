---
title: Protecting Firefox users following the compromise of eMudhra intermediate certificates
url: https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/
source: Mozilla Security Blog
date: 2026-10-20
fetch_date: 2026-10-21T06:49:26.084138
---

# Protecting Firefox users following the compromise of eMudhra intermediate certificates

[Mozilla](https://www.mozilla.org/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav "Visit mozilla.org")

Menu

* [About Mozilla](https://www.mozilla.org/about/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Products](https://www.mozilla.org/firefox/products/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Give](https://donate.mozilla.org/?presets=50,30,20,10&amount=30&currency=usd&utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Discover Firefox](https://www.mozilla.org/firefox/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)

[#### Mozilla Security Blog](https://blog.mozilla.org/security/ "Go to the front page")

* Search this site

  Search

**Categories:**
[Security](https://blog.mozilla.org/security/category/security/)

# Protecting Firefox users following the compromise of eMudhra intermediate certificates

Firefox Security Team
October 20, 2026

On Saturday, October 17, at 20:06 UTC, Mozilla received a report that private keys associated with eight eMudhra intermediate certificates had been compromised. These keys could allow attackers to issue fraudulent HTTPS certificates for websites they do not control. An attacker who could intercept a user’s connection could use those certificates to impersonate websites and potentially read or modify traffic.

Mozilla engineers responded immediately, blocking the affected certificates in Firefox using [OneCRL](https://blog.mozilla.org/security/2015/03/03/revoking-intermediate-certificates-introducing-onecrl/), Mozilla’s centralized list of revoked certificates. OneCRL delivers this protection without requiring users to update or restart Firefox.

By 22:59 UTC that same day, in less than 3 hours after we received the report, the updated OneCRL distribution was complete for all Firefox users with standard configurations.

Today, we are also releasing [Firefox 158.0.1](https://www.firefox.com/en-US/firefox/158.0.1/releasenotes/) for Desktop and Android, along with [Firefox ESR 115.43.1](https://www.firefox.com/en-US/firefox/115.43.1/releasenotes/) and [Firefox ESR 153.5.1](https://www.firefox.com/en-US/firefox/153.5.1/releasenotes/). These releases will distribute this protection for a minority of users whose custom settings may have prevented them from receiving the OneCRL update.

We are also updating the trusted certificate list in NSS ([NSS 3.131.1](https://groups.google.com/a/mozilla.org/g/dev-tech-crypto/c/vSxZxnOMMvs)) to remove the root certificate that signed the affected intermediates. Firefox is already protected through OneCRL, but this additional update helps protect other applications that use Mozilla’s trust store or versions derived from it and do not receive OneCRL updates.

Mozilla believes everyone has a fundamental right to security and privacy online. We remain committed to defending those rights and acting quickly to protect users.

Transparency is essential to trust. We will share more information as soon as circumstances allow.

#### Browse fast. Browse free.

[Download Firefox](https://www.mozilla.org/firefox/new/?utm_source=blog.mozilla.org&utm_campaign=firefox_frontier&utm_medium=referral)

[Previous article
**Updated GPG key for signing Firefox and Thunderbird Releases**
August 10, 2026](https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/)

#### More articles in “Security”

* ##### [Updated GPG key for signing Firefox and Thunderbird Releases](https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/)

  August 10, 2026
* ##### [Firefox Security Response to pwn2own 2025](https://blog.mozilla.org/security/2025/05/17/firefox-security-response-to-pwn2own-2025/)

  May 17, 2025
* ##### [Updated GPG key for signing Firefox Releases](https://blog.mozilla.org/security/2025/04/01/updated-gpg-key-for-signing-firefox-releases-2/)

  April 1, 2025
* ##### [Enhancing CA Practices: Key Updates in Mozilla Root Store Policy, v3.0](https://blog.mozilla.org/security/2025/03/12/enhancing-ca-practices-key-updates-in-mozilla-root-store-policy-v3-0/)

  March 12, 2025
* ##### [Behind the Scenes: Fixing an In-the-Wild Firefox Exploit](https://blog.mozilla.org/security/2024/10/11/behind-the-scenes-fixing-an-in-the-wild-firefox-exploit/)

  October 11, 2024

#### Recent articles

* ##### [Updated GPG key for signing Firefox and Thunderbird Releases](https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/)

  August 10, 2026
* ##### [Improving Transparency and Assurance in the Web PKI: Mozilla Root Store Policy v3.1](https://blog.mozilla.org/security/2026/06/29/improving-transparency-and-assurance-in-the-web-pki-mozilla-root-store-policy-v3-1/)

  June 29, 2026
* ##### [Firefox Security Response to pwn2own 2025](https://blog.mozilla.org/security/2025/05/17/firefox-security-response-to-pwn2own-2025/)

  May 17, 2025
* ##### [Updated GPG key for signing Firefox Releases](https://blog.mozilla.org/security/2025/04/01/updated-gpg-key-for-signing-firefox-releases-2/)

  April 1, 2025
* ##### [Enhancing CA Practices: Key Updates in Mozilla Root Store Policy, v3.0](https://blog.mozilla.org/security/2025/03/12/enhancing-ca-practices-key-updates-in-mozilla-root-store-policy-v3-0/)

  March 12, 2025

### Keep up with all things Firefox.

Your e-mail address

Country

- select -
Afghanistan
Akrotiri
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antarctica
Antigua and Barbuda
Argentina
Armenia
Aruba
Ashmore and Cartier Islands
Australia
Austria
Azerbaijan
Bahamas, The
Bahrain
Baker Island
Bangladesh
Barbados
Bassas da India
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bonaire, Sint Eustatius, and Saba
Bosnia and Herzegovina
Botswana
Bouvet Island
Brazil
British Indian Ocean Territory
Brunei
Bulgaria
Burkina Faso
Burma
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Cayman Islands
Central African Republic
Chad
Chile
China
Christmas Island
Clipperton Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo (Brazzaville)
Congo (Kinshasa)
Cook Islands
Coral Sea Islands
Costa Rica
Croatia
Cuba
Curaçao
Cyprus
Czech Republic
Côte d’Ivoire
Denmark
Dhekelia
Diego Garcia
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Europa Island
Falkland Islands (Islas Malvinas)
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
French Southern and Antarctic Lands
Gabon
Gambia, The
Gaza Strip
Georgia
Germany
Ghana
Gibraltar
Glorioso Islands
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard Island and McDonald Islands
Honduras
Hong Kong
Howland Island
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Isle of Man
Israel
Italy
Jamaica
Jan Mayen
Japan
Jarvis Island
Jersey
Johnston Atoll
Jordan
Juan de Nova Island
Kazakhstan
Kenya
Kingman Reef
Kiribati
Korea, North
Korea, South
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macau
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia, Federated States of
Midway Islands
Moldova
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Namibia
Nauru
Navassa Island
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Palmyra Atoll
Panama
Papua New Guinea
Paracel Islands
Paraguay
Peru
Philippines
Pitcairn Islands
Poland
Portugal
Puerto Rico
Qatar
Reunion
Romania
Russia
Rwanda
Saint Barthelemy
Saint Helena, Ascension, and Tristan da Cunha
Saint Kitts and Nevis
Saint Lucia
Saint Martin
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Maarten
Slovakia
Slovenia
Solomon Isl...