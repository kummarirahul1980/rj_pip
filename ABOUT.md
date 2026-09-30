# RJ Developer Ecosystem

RJ Developer is a collection of ordinary Python packages designed to make development faster, more flexible, and easier to customise — without hiding Python behind a heavy framework.

The core idea is simple:

> 💡 **Keep Python ordinary. Make the repetitive parts easier.**

RJ is not intended to become one giant framework.

Instead, it is an ecosystem of small, independent `rj_*` packages that solve practical development problems and can be combined when useful.

---

# 🧭 What is RJ Developer?

Modern development often involves writing the same supporting code repeatedly:

- ✅ Validation
- 🛠️ Helper functions
- 📧 Mail services
- 🔌 API utilities
- 🔄 Serialization
- 🧩 Reusable application modules
- 🌐 Framework integration
- ⚙️ CLI configuration
- 📦 Project conventions

RJ Developer exists to reduce that repetition without taking architectural control away from the developer.

Instead of introducing a completely new programming model, RJ builds on ordinary Python and provides reusable tools around it.

You can use:

- 🐍 One RJ package in a small Python script
- 📦 Several RJ packages in a larger application
- 🌐 The wider ecosystem inside a Django project

**Nothing requires you to adopt the entire ecosystem.**

---

# 🏠 `rj_home`

`rj_home` is the **home and controller package for the RJ ecosystem**.

It provides common ecosystem conventions while allowing individual packages to remain independent.

Its responsibilities include:

- 🧭 Common `rj.*` package namespace
- ⚙️ Shared ecosystem conventions
- 💻 Common CLI conventions
- 🔧 Ecosystem-level settings conventions
- 🚪 Central entry point for RJ tooling
- 🔗 Coordination between independently developed RJ packages

Conceptually, `rj_home` is where the ecosystem meets — not a framework that everything must depend on.

## 📦 RJ Namespace

RJ packages live under a common namespace:

    rj
    ├── core
    ├── mails
    ├── apps
    ├── api
    └── serialisers

The namespace does not imply a monolithic architecture.

Each package can remain independently:

- developed
- versioned
- installed
- used
- extended

---

# 🎯 Design Philosophy

RJ Developer follows a few simple principles.

## 😊 User-friendly

Common development tasks should require as little boilerplate as reasonably possible.

    # ordinary Python
    # with useful helpers around it

RJ should make development shorter without making the underlying code mysterious.

---

## 🪶 Flexible

**Use only what you need.**

A project using `rj.core` does not automatically need:

    rj.mails
    rj.apps
    Django
    rj.api
    ...

RJ should fit into an application rather than forcing the application to fit into RJ.

---

## 🎛️ Customisable

RJ provides conventions, not restrictions.

Developers should be able to:

- extend RJ components
- configure them
- replace them
- bypass them
- integrate them with their own architecture

**Your application remains yours.**

---

## 🧩 Modular

Functionality belongs in separate packages.

Instead of:

    One giant framework
            ↓
        Everything

RJ prefers:

    Small package
          +
    Another package
          +
    Another package
          ↓
    Only what you actually need

Each package should have a clear purpose and a useful life outside of the rest of the ecosystem.

---

## 🐍 Python-native

RJ does not attempt to replace Python with another programming model.

The underlying language remains Python.

The goal is not:

> «Learn RJ before you can use Python.»

The goal is:

> «Use Python normally, and let RJ remove some of the repetitive work.»

---

## ⚡ Time-saving

RJ exists primarily to remove repetitive development work.

If the same useful piece of code keeps appearing across projects, it can potentially become an RJ building block.

> «Write the idea once. Reuse it where it makes sense.»

---

# 📦 RJ Packages

## 🧱 `rj_core`

`rj_core` is the common foundation of the ecosystem.

It contains small, reusable utilities that can be useful across many types of Python projects.

Current areas include:

- ✅ Validators
- 🛠️ Helpers
- 🔧 Common utility functions
- 🔗 Shared RJ infrastructure

The philosophy of `rj_core` is intentionally simple:

> «Small building blocks, not another framework.»

A helper should solve a problem without forcing the rest of the application to adopt a particular architecture.

---

## 📧 `rj_mails`

`rj_mails` provides reusable mail functionality for Python applications.

It focuses on making email delivery and email construction straightforward while remaining close to Python's existing mail capabilities.

Features include:

- 📡 SMTP mail services
- 📝 Plain-text email
- 🌐 HTML email
- 🛠️ Reusable mail helpers
- 🔧 Email-related utilities
- 🌐 Django-oriented mail applications

It can therefore serve both ordinary Python applications and framework-based projects.

    Application
        │
        └── rj.mails
              ├── SMTP
              ├── Plain-text mail
              ├── HTML mail
              └── Django mail components

The implementation stays close to Python while `rj.mails` handles the repetitive parts.

---

## 🧩 `rj_apps`

`rj_apps` focuses on reusable application modules.

Rather than creating another complete framework, the goal is to provide smaller application-level components that can be incorporated into existing projects.

The architecture is intended to support multiple frameworks over time.

Current development is focused primarily on:

    rj_apps
    └── Django

The long-term idea is simple:

> «Reusable application modules without forcing the entire project to adopt an RJ architecture.»

A project using an RJ application module can still keep its own:

- 📁 Project structure
- 🗃️ Models
- 👁️ Views
- 🔗 URLs
- ⚙️ Settings
- 🔐 Authentication
- 🧠 Business logic

RJ provides the reusable component.

**The project remains in control.**

---

# 🔌 Additional Packages

The ecosystem is intentionally open-ended.

## 🔗 `rj_api`

Reusable API-related utilities and abstractions.

## 🔄 `rj_serialisers`

Serialization-related utilities for converting application data between useful representations.

These packages can evolve independently and do not need to become mandatory components of the ecosystem.

Additional packages may be introduced whenever a recurring development problem can be solved cleanly as an independent RJ component.

---

# 🧰 How the Ecosystem Fits Together

RJ does not have a strict dependency pyramid.

Think of it as a **toolbox**.

Start with ordinary Python and add whichever RJ components are useful:

    Your Application
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          rj.core       rj.mails       rj.apps
             │             │             │
        helpers &       mail        application
        validators     services       modules
             │             │             │
             └─────────────┼─────────────┘
                           │
                         Python

`rj_home` provides the ecosystem-level home and conventions, while individual packages remain independently usable.

For example, all of these are valid:

    🐍 Python
    └── rj.core

    🐍 Python
    ├── rj.core
    └── rj.mails

    🌐 Django
    ├── rj.core
    ├── rj.mails
    ├── rj.apps
    └── Your project code

There is **no requirement to install everything**.

---

# 📥 Installation

Install the ecosystem home:

    pip install rj_home

Then install the packages required by your project.

For example:

    pip install rj_mails

Individual packages may have additional dependencies depending on the functionality being used.

The ecosystem is intentionally designed so that optional functionality remains optional.

---

# 🚧 Development Model

RJ Developer is released incrementally.

Instead of waiting for one large framework release, individual packages can evolve independently.

## Current direction

| 📦 Package | 🎯 Purpose |
|---|---|
| `rj_home` | Ecosystem home, controller, CLI and shared conventions |
| `rj_core` | Validators, helpers and common utilities |
| `rj_mails` | Mail services and Django mail applications |
| `rj_apps` | Reusable application modules |
| `rj_api` | API utilities |
| `rj_serialisers` | Serialization utilities |

The package boundaries are intentional.

A package should exist because it provides a **useful, reusable capability** — not simply because the ecosystem needs another package.

---

# 🤔 Why Not Just Build a Framework?

Because RJ is not trying to control the application.

Traditional frameworks often provide an entire application architecture.

RJ takes a different approach:

    🏗️ Framework
          ↓
    "Here is how your application should work."

Where RJ says:

    🧰 RJ
          ↓
    "Here are useful components.
     Use them where they make sense."

The developer keeps ownership of the architecture.

RJ simply removes some of the repetitive work required to build it.

---

# 🧠 The RJ Principle

RJ Developer can ultimately be reduced to three ideas:

## 🐍 Python First

Use the language developers already know.

## 🧩 Modules Over Monoliths

Separate reusable functionality into independently useful packages.

## ⚡ Automation Without Loss of Control

Make repetitive work easier without hiding what the application is actually doing.

---

# 🚧 Status

RJ Developer is currently **under active development**.

The ecosystem is being built incrementally, package by package.

The architecture is intentionally:

- 🪶 Small
- 🧩 Modular
- 🐍 Python-native
- 📦 Independently installable
- 🎛️ Flexible
- 🛠️ Customisable
- ⚡ Focused on practical development problems

The project will grow according to the problems it solves rather than trying to become a framework for everything.

---

# 💭 The RJ Idea

RJ is ultimately about keeping the boundary simple:

> «Python should remain Python.»

RJ should handle the boring, repetitive, and reusable pieces so developers can spend more time building the actual application.

---

# 🚀 Build with Python.

# ⚡ Remove the repetitive work.

# 🎛️ Keep control of the architecture.
