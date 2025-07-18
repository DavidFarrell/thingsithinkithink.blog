---
title: "Connecting Chrome DevTools to FastHTML Apps for Rapid Style Iteration"
date: 2025-07-18T09:00:00Z
slug: /07-18-chrome-devtools-fasthtml-development/
description: "How to connect Chrome DevTools to your FastHTML applications for fast CSS and HTML debugging and iteration during development."
image: /images/2025/07-18-devtools-hero.png
caption: "Chrome DevTools connected to a FastHTML app for live style editing"
categories:
  - coding
  - web-development
tags:
  - fasthtml
  - chrome-devtools
  - css
  - debugging
  - development
  - python
draft: false
---

I learned a cool trick that I think will speed up the web development process for me.

The process of editing CSS, saving it, refreshing the web browser page is quite annoying. And although you can edit the CSS inside the Chrome DevTools, having to then go back into your main IDE to make the changes is something that's a bit of a pain.

I've been experimenting with FastHTML, which is a Python library for building HTML apps. And Jeremy from Answer.ai [shared a nice wee trick](https://www.youtube.com/watch?v=576ouCQ6mlk) that will speed up the iteration process. And I haven't actually seen this before, so I thought I'd write about it here.

![Live editing a CSS file directly from within Chrome DevTools and seeing it save locally.](/images/2025/07-18-devtools-live-editing.png)
_Live editing a CSS file directly from within Chrome DevTools and seeing it save locally._

## How It's Done

So imagine you've got some CSS like this:

```css
H1 {
  color: blueviolet;
}
P {
  background: aliceblue;
  margin: 2rem;
}
.container {
  padding: 4rem;
}
```

You want to be able to edit it inside DevTools and then save it directly back into your application. There are two steps to this.

**Step one:** You need to enable the experimental flags in Chrome.

1. Go to `chrome://flags` in your Chrome browser.
2. Search for "DevTools Project Settings" and set it to "Enabled".
3. Search for "DevTools Automatic Workspace Folders" and set it to "Enabled".
4. Relaunch Chrome if prompted.

**Step two:** The FastHTML integration.
Include the code of his app and then say how you need to add this `app.devtools_json()` thing. When you do that, FastHTML will automatically generate a special JSON file at the `/.well-known/appspecific/com.chrome.devtools.json` endpoint of your local server.

Chrome DevTools knows to look for this exact file. This JSON file contains two pieces of information: the `root` path to your project folder on your local machine and a unique `uuid` for the workspace. That's what allows Chrome to directly establish the link to your project.

It only works on `localhost`, so there's no risk of accidentally exposing development features in production.

```python
from fasthtml.common import *
from pathlib import Path

hdrs = [Link(href="static/styles.css", rel="stylesheet")]
app, rt = fast_app(hdrs=hdrs)
app.devtools_json()

@rt
def index():
    return Titled('com.chrome.devtools.json demo',
                P('You can see the devtools json here: ', A(devtools_loc, href=devtools_loc)))

serve()
```
