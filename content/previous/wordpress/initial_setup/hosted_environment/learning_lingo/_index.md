+++
title = "Learning the Lingo"
weight = 1
chapter = true
+++

# Learning the Lingo

The internet is controlled by DNS records. DNS stands for **Domain Name System** and it's kind of like a map and signposts that tell computers where to find certain information on the internet.

![](images/huh.gif)

Don't worry too much if you don't fully understand these terms by the end of this section - but hopefully they'll be slightly less daunting in the following steps if we explain them a little bit now!

## Domain Names

Let's pretend your website is a business. Your domain name is like the name of that business on the internet - the thing people use to identify you, like "She Codes" is the name of our organisation. Our domain name is [shecodes.com.au](https://shecodes.com.au).

You will get to choose your domain name at the start of the process we're about to follow. Your domain must be registered with a domain name registrar - an organisation that has been accredited by the Internet Corporation for Assigned Names and Numbers (ICANN) to register new domain names. 

Many registrars also offer web hosting as a service, and many hosting companies are also registrars. It is significantly less important who you register your domain name with than who you have hosting with, but as a rule of thumb you should not be paying hundreds of dollars for a domain name unless it's extremely highly sought after. Registrars are allowed to charge whatever they want, and some shady registrars will send physical letters to newly registered businesses offering to sell them domain names for much higher than what they would normally cost.

For the purposes of this tutorial, our sponsors VentraIP are providing us with free domain names that end in `.co` - so as long as your preferred domain name is available you can register it for free for 12 months. If you would like a different domain name (e.g. yoursite.com or yoursite.com.au) you can still take advantage of the 3 months free hosting, but you will need to purchase the domain name. You can always change your domain name later, so we recommend just using the free option for now!

## Website Hosting

Hosting refers to the place on the internet where your website (the content & code) is stored. If your domain name is your 'business name' then your hosting is like your physical office location. Just like a business, a website contains stuff - and that stuff needs to be kept somewhere. Because hosting takes up space, we have to pay for it somewhere down the line - servers require things like power, internet & cooling to operate.

She Codes has partnered with a company called VentraIP for our workshops, and they give all of our attendees 3 months free hosting. We recommend them as a quality hosting provider based in Australia - they are very well-priced, have a great product and offer 24/7 chat support.

## DNS

The Domain Name System is a pretty central part of the internet, providing a way to match names (e.g. the website URL you type into the search bar) to numbers that represent a 'location' of that address on the internet. Just like all houses and businesses on a street are given a unique physical address so that people can easily locate them, all devices connected to the internet (including servers that host websites) have an **IP Address.** 

The IP Address for the She Codes website is just a string of random numbers - imagine having to remember that each time you wanted to visit the site! That's where DNS records save the day - they store two or more bits of data in a record that can be used by devices navigating the internet to match up nice names (like shecodes.com.au) with ugly IP Addresses. 

There are different types of DNS records used for different things, such as Nameservers, MX records (used for email), CNAME records (used to connect different domains and subdomains together) and TXT records (which allow us to store notes for a domain name, like whether we've allowed certain applications to access it).

## Nameservers
If you register your domain name and your web hosting with two separate companies, you need a way to tell your domain registrar where to look for the files that make up your website. The way we do this is using a specific type of DNS record called a **nameserver**. Name Servers always store two pieces of information - the Domain Name and the IP Address of the hosting server. Because we are registering both our domain name and hosting with the same company today, this record will be automatically added for us.

{{% notice info %}}
If you decide at a later date to move your website or change the domain name, you will need to update the nameservers accordingly.
{{% /notice %}}
