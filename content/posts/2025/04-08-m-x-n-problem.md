---
title: "The M×N Problem in Software Architecture"
date: 2025-04-08T12:00:00Z
slug: /04-08-the-m-x-n-problem-in-software-architecture/
description: "Understanding the combinatorial complexity problem that plagues many software systems, and how modern architectures solve it."
image: images/2025/mxn/IMG_1903.PNG
caption: A comparison of jQuery's direct DOM manipulation versus React's state-based approach
categories:
  - blog
tags:
  - software-architecture
  - system-design
  - programming
draft: false
---

I've heard about the "M×N problem" a couple of times lately. After watching Swyx on the Latent Space podcast interviewing the creators of MCP from Anthropic, where he mentioned this problem again, I decided to figure out what it actually meant. According to Swyx, it's a problem he's had to solve repeatedly in his career because of his work on developer tooling.

## The M×N Problem Defined

The M×N problem occurs in software architecture when you have M components that need to interact with N other components, with each interaction handled individually. This creates a tangled web of connections where the total number of integrations grows to M × N.

This might sound abstract, but it's a pattern that appears constantly in software systems. Whenever we have multiple sources of events connecting to multiple targets, we risk creating this complexity explosion.

![jQuery vs React.js event handling comparison](/images/2025/mxn/IMG_1903.PNG)

The image above shows how event handlers in jQuery directly manipulate DOM elements, creating many point-to-point connections. React.js, on the other hand, uses a state-based approach that centralises these interactions.

## Why This Matters

The core issue here is coupling. In a system with M×N connections:

- Adding a new component requires wiring it to potentially every existing component
- Logic becomes scattered across the codebase
- Changes in one part can have unpredictable effects elsewhere
- Debugging becomes exponentially more difficult

These systems quickly become brittle and resistant to change-exactly what we try to avoid in good architecture.

## The M+N Solution

According to Swyx, the solution to this problem is to introduce a shared abstraction layer or central coordinator. Instead of direct links between components, all M sources send messages to a shared system, and all N targets read from it.

This transforms the connection count from M×N to M+N.

![REST vs GraphQL architecture comparison](/images/2025/mxn/IMG_1901.PNG)

This diagram from the Apollo Blog illustrates the difference between REST, where clients need to know about various endpoints (M×N), versus GraphQL, which provides a single interface that handles the complexity internally (M+N).

## Real-World Examples

### UI Frameworks: jQuery vs React

The evolution from jQuery to React demonstrates this shift clearly:

- **jQuery** encouraged direct manipulation: select an element, modify it. Each event handler contained custom logic for updating specific DOM elements, leading to scattered logic and brittle interfaces.
- **React** introduced a state-centric model where UI is a function of state. Components don't directly manipulate each other; they update a shared state that triggers re-rendering.

![Neuropod unified ML framework architecture](/images/2025/mxn/IMG_1900.PNG)

The Neuropod architecture shown above is another example of this pattern. It provides a unified interface for multiple machine learning frameworks, reducing the complexity of working with different models.

### System Design: Choreography vs Orchestration

In distributed systems, we see similar patterns:

- **Choreography**: Services emit and respond to events with minimal central coordination
- **Orchestration**: A process manager coordinates the workflow explicitly

While choreography offers flexibility, it can create an implicit M×N problem as services need to understand messages from many sources. Orchestration centralises this logic, making the system more predictable.

![Choreography vs Orchestration in distributed systems](/images/2025/mxn/IMG_1902.PNG)

This slide from a presentation on Temporal React shows the fundamental difference between choreography (with many connections between services) and orchestration (with a central coordinator).

### API Design: REST vs GraphQL

The shift from REST to GraphQL presents another example:

- In **REST**, each client must be adapted to specific endpoints, with custom logic for combining data from multiple sources. The client needs to understand the API's structure in detail.
- With **GraphQL**, clients declare what they want, and a single endpoint handles the complexity. The server centralises the logic of fulfilling these requests.

## thingsithinkithink

- The M×N problem is a lens through which we can talk about system complexity. It helps explain why certain architectures feel cleaner and more maintainable than others.

- Many architectural patterns we consider "modern" apply this principle of reducing connections through abstraction. State management (Redux, MobX), event buses, message queues, and API gateways all serve this purpose.

- There's a trade-off between the simplicity of direct connections and the overhead of an intermediary layer. For very small systems, M×N might be simpler initially. The challenge is recognising when you're reaching the inflection point where M+N becomes the better approach.
