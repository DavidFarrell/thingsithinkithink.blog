---
title: "Where to Host Your FastHTML Apps"
date: 2025-08-16T11:00:00Z
slug: /08-16-where-to-host-fasthtml-apps/
description: "Deployment options for FastHTML applications."
categories:
  - coding
  - web-development
tags:
  - fasthtml
  - deployment
  - hosting
draft: false
---

FastHTML apps are built on Starlette, which means they can run anywhere Starlette runs. Some options for hosting so I don't need to look next time.

---

## Simple Deployment Options

- **Railway**: go-to choice for simple deployment
- **Plash**: Answer.ai's new hosting service (currently in beta)  
- **Modal**: Good option if you have free credits (like I do from the Hamel course)

---

## Any Starlette-Compatible Hosting

Since FastHTML apps run on Starlette, they work with any hosting service that supports Starlette applications.

[Answer.ai's FastHTML Deploy repository](https://github.com/answerdotai/fh-deploy) includes guides for:

- HuggingFace
- Replit 
- Vercel
- Heroku
- Digital Ocean Droplets (with Docker + SSL)
- Fly.io
- Coolify

