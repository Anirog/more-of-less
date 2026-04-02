---
title: More of less blog design
date: 2026-04-01
slug: more-of-less-blog-design
---

When designing this blog, I wanted to keep things simple, working on the principle that improvement does not always mean adding things. I knew I didn't want a dark/light mode button or toggle, but I like the idea of a light and dark mode for a website. Instead of a toggle, this site shows a light or dark variation based on the user’s device preference for the colour scheme. This is achieved by using the `@media (prefers-color-scheme: dark)` media query, like this:

![Prefers color scheme media query](https://ik.imagekit.io/1wh3oo1zp/prefers-color-scheme-dark.png)

Then in the CSS I can use the color variable, on any element like this example for setting the background color of the body, the text colour and the link colour:

![Body background example](https://ik.imagekit.io/1wh3oo1zp/set-background-text-link-colour_yWLRs0WxT)

I also made four different themes, each with its own light and dark mode. These are the themes I made, and the one I went with was Oxford Blue 🙂

## Himalaya

![Himalaya Theme](https://ik.imagekit.io/1wh3oo1zp/himalaya.png)

## Kabul

![Kabul Theme](https://ik.imagekit.io/1wh3oo1zp/kabul.png)

## Nero

![Nero Theme](https://ik.imagekit.io/1wh3oo1zp/nero.png)

## Oxford Blue

![Oxford Blue Theme](https://ik.imagekit.io/1wh3oo1zp/oxford-blue.png)