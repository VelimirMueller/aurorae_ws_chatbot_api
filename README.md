<picture>
  <source media="(prefers-color-scheme: light)" srcset="assets/banner/hero-v2-light.svg">
  <img alt="SYNTHWERK-LLM. LLM gateway. Local models in dev, any provider in prod. Scoped, audited SSE streaming. Rewrite." src="assets/banner/hero-v2-dark.svg" width="100%">
</picture>

<p align="center">

[![status: rewrite planned](https://img.shields.io/badge/status-rewrite_planned-10b981?style=flat-square&labelColor=0a0a0b)](#-05-status) [![VM. flagship](https://img.shields.io/badge/VM.-flagship-6366f1?style=flat-square&labelColor=0a0a0b)](https://github.com/VelimirMueller) [![license: MIT](https://img.shields.io/badge/license-MIT-a1a1aa?style=flat-square&labelColor=0a0a0b)](LICENSE) [![stack: Go 1.27](https://img.shields.io/badge/stack-Go_1.27-a1a1aa?style=flat-square&labelColor=0a0a0b)](#-05-status)

</p>

> Local models in dev. Any provider in prod.

```text
 █████  ██  ██  ██  ██  ██████  ██  ██  ██   ██  ██████  █████   ██  ██
██      ██  ██  ███ ██    ██    ██  ██  ██   ██  ██      ██  ██  ██ ██
 ████    ████   ██████    ██    ██████  ██ █ ██  █████   █████   ████
    ██    ██    ██ ███    ██    ██  ██  ███████  ██      ██ ██   ██ ██
█████     ██    ██  ██    ██    ██  ██   ██ ██   ██████  ██  ██  ██  ██

██      ██      ██   ██
██      ██      ███ ███
██      ██      ███████
██      ██      ██ █ ██
██████  ██████  ██   ██  ██

------ the llm gateway for the synthwerk family ------------------------
```

**synthwerk-llm** is the LLM gateway for the Synthwerk family. One API for chat and text tasks, scoped access, audited streaming.
This repo is being rewritten. There is no code on main. It is very good at waiting.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/stats-v2-dark.svg">
  <img alt="1 API, CHAT AND TEXT. 3 SCOPES: ADMIN, TENANT, USER. 2 PROVIDERS NAMED. 0 CODE ON MAIN" src="assets/readme/stats-v2-light.svg" width="100%">
</picture>

<br>

## // 01 WHAT IT DOES

<img alt="01 WHAT IT DOES. ONE API. EVERY PROVIDER." src="assets/readme/divider-what-v2.svg" width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/features-v2-dark.svg">
  <img alt="ONE API: Chat and text tasks behind one endpoint. The provider is chosen by env: Ollama locally, Anthropic or others in prod. SCOPES: platform-admin, tenant, user. Services enforce the scope on the token, never the prompt. AUDITED STREAM: Tokens stream over SSE. Every answer and tool call is audited" src="assets/readme/features-v2-light.svg" width="100%">
</picture>

- One API for chat and text tasks. The provider is chosen by env: Ollama in dev, Anthropic or any provider in prod.
- Tokens stream over SSE. Every answer and tool call is audited.
- Scopes are platform-admin, tenant and user. The service enforces the scope on the token, never the prompt.

<br>

## // 02 QUICK START

<img alt="02 QUICK START. NOTHING TO RUN. YET." src="assets/readme/divider-start-v2.svg" width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/start-v2-dark.svg">
  <img alt="Terminal: $ gh repo clone VelimirMueller/synthwerk-llm | $ cd synthwerk-llm | $ git checkout legacy-final | # the old Flask + GPT4All WebSocket demo" src="assets/readme/start-v2-light.svg" width="100%">
</picture>

There is no code to run on main yet. The old demo lives at the tag `legacy-final`.

```bash
gh repo clone VelimirMueller/synthwerk-llm
cd synthwerk-llm
git checkout legacy-final   # the old Flask + GPT4All WebSocket demo
```

- The ecosystem map is in [synthwerk](https://github.com/VelimirMueller/synthwerk).
- Shared CI, lint configs and templates come from [synthwerk-blueprint](https://github.com/VelimirMueller/synthwerk-blueprint).

<br>

## // 03 HOW IT WORKS

<img alt="03 HOW IT WORKS. IN ONE SIDE, OUT THE OTHER." src="assets/readme/divider-how-v2.svg" width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/flow-v2-dark.svg">
  <img alt="CLIENTS -> LLM GATEWAY -> PROVIDERS -> NATS BUS. The gateway also reads the other services through read-only MCP tools." src="assets/readme/flow-v2-light.svg" width="100%">
</picture>

```text
 feat/* --PR + checks--> main --auto--> dev --tag vX.Y.Z--> stg
                                                             |
                                          prd <--manual------+
                                               approval

 trunk-based. no env branches. digest promoted by approval.
```

- **Clients in.** synthwerk-widgets and SDK apps call the gateway over HTTP.
- **Provider out.** The gateway forwards to Ollama, Anthropic or another provider, chosen by env.
- **Read-only MCP.** The gateway reads the other services through read-only MCP tools. It never writes.
- **Events out.** Facts go to the NATS bus as events.

<br>

## // 04 USAGE

<img alt="04 USAGE. THE REFERENCE. CONDENSED." src="assets/readme/divider-usage-v2.svg" width="100%">

### Scopes

- platform-admin, tenant, user. Enforced on the token, never the prompt.

### Where it fits

- synthwerk-widgets and SDK apps call the gateway.
- The gateway reads service tools through read-only MCP tools.
- The gateway publishes events to the NATS bus.
- Ecosystem map: [synthwerk](https://github.com/VelimirMueller/synthwerk). Shared CI: [synthwerk-blueprint](https://github.com/VelimirMueller/synthwerk-blueprint).

### The old code

- Tag `legacy-final`: a Flask + GPT4All WebSocket demo, one shared session for all users.
- This repo was renamed. The old URL still redirects here.

### Branching

- main deploys to dev, a `vX.Y.Z` tag to stg, an approved digest to prd.

<br>

## // 05 STATUS

<img alt="05 STATUS. HONEST. NO CODE YET." src="assets/readme/divider-status-v2.svg" width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/status-v2-dark.svg">
  <img alt="Rewrite: planned, epic E3. Old code: tag legacy-final. Providers: Ollama, Anthropic, …. Streaming: SSE. Branching: main→dev, tag→stg, digest→prd" src="assets/readme/status-v2-light.svg" width="100%">
</picture>

There are no tests. There is no code to test. There is no CHANGELOG yet.

<br>

```text
-- EOF ------------------------------------------- NO CODE. YET. --
```

---

<sub>VM. studio / flagship · open source · look per <code>vm-brand</code> playbook · [MIT](LICENSE) © 2026 Velimir Mueller</sub>
