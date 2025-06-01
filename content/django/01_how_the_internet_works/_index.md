---
title: "1. How the Internet Works"
weight: 1
chapter: true
---

# How the Internet works

We bet you use the Internet every day. But do you actually know what happens when you type an address like https://shecodes.com.au/ into your browser and press `enter`?

The first thing you need to understand is that a website consists of a bunch of files saved on a hard disk -- just like your movies, music, or pictures. However, there is one part that is unique for websites: they include computer code called HTML. Your web browsers (like Chrome, Safari, Firefox, etc.) love it. Web browsers are designed to understand this code,
follow its instructions, and present these files that your website is made of, exactly the way you want.

As with every file, we need to store HTML files somewhere on a hard disk. For the Internet, we use special, powerful computers called *servers*. They don't have
a screen, mouse or a keyboard, because their main purpose is to store data and serve it. That's why they're called *servers* – because they *serve* you data.

OK, but you want to know how the Internet looks, right?

Imagine that when you type https://shecodes.com.au/, you send a letter that says: "Dear She Coder, I want to see the shecodes.com.au website. Send it to me, please!"

Your letter goes to the post office closest to you. Then it goes to another that is a bit nearer to your addressee, then to another, and another until it is delivered at its destination. The only unique thing is that if you send many letters (*data packets*) to the same place, they could go through totally different post offices (*routers*). This depends on how they are distributed at each office.

![Figure 1.1](images/how_internet_works.png)


That's how it works - you send messages and you expect some response. Instead of paper and pen you use bytes of data, but the idea is the same!

Instead of addresses with a street name, city, zip code and country name, we use IP addresses. Your computer first asks the DNS (Domain Name System) to translate `shecodes.com.au` into an IP address. It works a little bit like old-fashioned phonebooks where you can look up the name of the person you want to contact and find their phone number and address.

When you send a letter, it needs to have certain features to be delivered correctly: an address, a stamp, etc. You also use a language that the receiver understands, right? The same applies to the *data packets* you send to see a website. We use a protocol called HTTP (Hypertext Transfer Protocol).

So, basically, when you have a website, you need to have a *server* (machine) where it lives. When the *server* receives an incoming *request* (in a letter), it sends back your website (in another letter).

Since this is a Django tutorial, you might ask what Django does. Instead of sending the same generic response to everyone, Django enables you to create personalized, dynamic responses—much like sending a tailored letter to each person rather than a one-size-fits-all announcement. It helps you craft personalized, interesting letters for each individual!

Enough talk – time to create!

  
