---
title: "1. How the Internet Works"
weight: 1
chapter: true
---

# How the Internet works

You probably use the internet every day — but have you ever wondered what actually happens when you type an address like `https://shecodes.com.au` into your browser and hit `enter`?
Let’s break it down.

A website is really just a collection of files stored on a hard drive — just like your photos, music, or videos. What makes websites special is that they contain code, mainly HTML. Web browsers like Chrome, Safari, or Firefox are built to read this code, follow its instructions, and display the content in a way that makes sense to you.

But these HTML files need to live somewhere. That’s where servers come in — powerful computers designed to store and deliver (or "serve") data. Unlike your personal computer, servers don’t need screens, keyboards, or mice. Their one job is to wait for requests and send back the right files.
That’s why they’re called servers — they serve up websites.

So what actually happens when you visit a site like `shecodes.com.au`?

It’s kind of like sending a letter that says:
 "Dear She Codes, please send me your website!"
Your request travels through a network of digital “post offices” (called routers), each one passing your message along to the next, getting closer and closer to the server that hosts the website. Once it arrives, the server sends the website’s data back — possibly taking a different route on the way to you.

Each little piece of the site you see — images, text, colours — arrives in separate data packets, like lots of tiny letters, and your browser puts them all back together to display the full page

![Figure 1.1](images/how_internet_works.png)

That’s the basic idea: you send a message and expect a response. Instead of paper and envelopes, you're using data — tiny chunks of information called bytes — but the concept is the same!

Instead of a street address with a city and postcode, websites use IP addresses — unique numbers that identify each server on the internet. But since it’s hard to remember a bunch of numbers, we use website names like shecodes.com.au. Your computer asks something called the DNS (Domain Name System) to look up that name and find the matching IP address — kind of like using an old-school phone book to find someone’s number.

Just like a physical letter needs certain things to be delivered properly — like an address, a stamp, and the right language — your computer messages do too. That’s where HTTP (Hypertext Transfer Protocol) comes in. It’s the “language” your browser and the server use to talk to each other and make sure everything gets where it’s supposed to go.

So, when someone visits your website, here’s what happens:
1. Their computer sends a request to your server.
2. Your server reads the request and sends back the website data — a response.

Now, since this is a Django tutorial, you’re probably wondering: Where does Django fit in?

Great question! Without Django, your website might always send the exact same thing to everyone — like mailing out the same generic flyer to every person. But Django lets you respond differently to each visitor. You can create smart, personalised responses — like sending a unique letter to each person based on who they are or what they asked for. Pretty powerful, right?

Alright, enough theory — let’s get building!











  
