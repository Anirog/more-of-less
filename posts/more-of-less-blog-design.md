---
title: More of less blog design
date: 2026-04-01
slug: more-of-less-blog-design
---

When designing this blog, I wanted to keep things simple, working on the principle that improvement does not always mean adding things. I knew I didn't want a dark/light mode button or toggle, but I like the idea of a light and dark mode for a website. Instead of a toggle, this site shows a light or dark variation based on the user’s device preference for the colour scheme. This is achieved by using:

`@media (prefers-color-scheme: dark)`

In my CSS, I set up a color variable for the background colour, text colour and link colour. The default is the light mode, and then when the media query detects that the user prefers a dark colour scheme, it changes the value of the variable to the dark mode colours.

![Prefers color scheme media query](https://ik.imagekit.io/1wh3oo1zp/prefers-color-scheme-dark.png)

Using the colour variable in CSS allows me to set the background, text and link colours for any element like this example.

![Body background example](https://ik.imagekit.io/1wh3oo1zp/set-background-text-link-colour_yWLRs0WxT)

I created four themes for the blog, each has its own light and dark mode. Here are the themes I designed and my favourite colour is Oxford Blue.

## Himalaya

![Himalaya Theme](https://ik.imagekit.io/1wh3oo1zp/himalaya.png)

## Kabul

![Kabul Theme](https://ik.imagekit.io/1wh3oo1zp/kabul.png)

## Nero

![Nero Theme](https://ik.imagekit.io/1wh3oo1zp/nero.png)

## Oxford Blue

![Oxford Blue Theme](https://ik.imagekit.io/1wh3oo1zp/oxford-blue.png)