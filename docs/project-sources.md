# Project descriptions

Refreshed at Wuzi’s request on 2026-11-04 using public repository READMEs and source. Original project names and links remain pinned in tests/fixtures/projects-original.json. Historical descriptions may be revised; original articles and media remain immutable. No current demo availability is promised.



### WireGUI

- Retain URL: https://github.com/Devsfy/wiregui
- Description: **A desktop control panel for WireGuard that lets you switch tunnels, browse saved configurations and see when each was last connected. Built with Electron, React and TypeScript; no longer actively maintained.**
- Category / stack: Desktop tools; TypeScript, React, Electron, WireGuard.
- Evidence: [README: features and explicit maintenance notice](https://github.com/Devsfy/wiregui/blob/master/README.md), [package.json: desktop and UI stack](https://github.com/Devsfy/wiregui/blob/master/package.json), [platform-specific tunnel control](https://github.com/Devsfy/wiregui/blob/master/src/utils/wg.ts).
- Status: README explicitly says no longer actively maintained; repository itself is not archived. Repository description names Linux and Windows; avoid adding an unverified macOS support claim.

### FXTrainer

- Retain URL: https://github.com/Wuzi/FXTrainer
- Description: **A historical GTA V and FiveM trainer with an in-game menu for vehicle boosts, free movement and player settings. Written in C++ as a Script Hook V ASI plugin.**
- Category / stack: Game modding; C++, Script Hook V.
- Evidence: [README: controls, GTA V/FiveM installation and Script Hook V](https://github.com/wuzi/FXTrainer/blob/master/readme.md), [changelog: airbreak and vehicle controls](https://github.com/wuzi/FXTrainer/blob/master/changelog.txt), [C++ implementation](https://github.com/wuzi/FXTrainer/blob/master/src/NativeTrainer/script.cpp).
- Status: Historical code, last repository push in 2018; current GTA V/FiveM compatibility is unverified. Do not imply compatibility with current multiplayer services.

### language-pawn

- Retain URL: https://github.com/Wuzi/language-pawn
- Description: **A historical Atom package for writing SA-MP scripts, with Pawn syntax highlighting and snippets for common libraries and plugins. Adapted from Atom's C grammar, it covers tools such as Streamer, sscanf and FCNPC.**
- Category / stack: Developer tools; Atom, Pawn, CoffeeScript.
- Evidence: [README: grammar origin and supported libraries](https://github.com/wuzi/language-pawn/blob/master/README.md), [package metadata](https://github.com/wuzi/language-pawn/blob/master/package.json).
- Status: Keep the Atom scope explicit; this is not a current VS Code extension or language server.

### labirong

- Retain URL: https://github.com/Wuzi/labirong
- Description: **Race other players through a randomly generated maze in the browser, then tackle a new layout when someone finds the exit. The JavaScript game uses a Node.js server and Socket.IO to synchronize players and rounds.**
- Category / stack: Multiplayer games; JavaScript, Node.js, Express, Socket.IO.
- Evidence: [README: multiplayer maze racing](https://github.com/wuzi/labirong/blob/master/README.md), [map generation](https://github.com/wuzi/labirong/blob/master/src/server/map.js), [server: player sync, winner and map reset](https://github.com/wuzi/labirong/blob/master/src/server/index.js), [dependencies](https://github.com/wuzi/labirong/blob/master/package.json).
- Status: README names a demo at `labirong.wuzi.dev`; availability was not verified.

### labironGO

- Retain URL: https://github.com/Wuzi/labirongo
- Description: **Escape a procedurally generated maze without leaving the terminal. This Go remake of Labirong draws the game with ANSI colors and handles keyboard input in a goroutine.**
- Category / stack: Terminal games; Go, ANSI terminal rendering.
- Evidence: [README: terminal-based Go remake](https://github.com/wuzi/labironGO/blob/master/README.md), [game loop and maze generator](https://github.com/wuzi/labironGO/blob/master/game.go), [terminal scenes and colors](https://github.com/wuzi/labironGO/blob/master/scene.go).
- Status: This version is single-player; do not inherit the original's multiplayer claim. The original lowercase URL resolves to the canonical `labironGO` repository.

### labirong3D

- Retain URL: https://github.com/Wuzi/labirong3d-client
- Description: **A browser-based multiplayer maze race, rebuilt in 3D with animated characters and in-game chat. A TypeScript and Babylon.js client synchronizes the shared world over WebSockets.**
- Category / stack: Multiplayer games; TypeScript, Babylon.js, WebSockets.
- Evidence: [README: experimental 3D remake and separate server](https://github.com/wuzi/labirong3d-client/blob/master/README.md), [browser canvas entry point](https://github.com/wuzi/labirong3d-client/blob/master/src/index.ts), [network events: world sync, chat, map regeneration and player escape](https://github.com/wuzi/labirong3d-client/blob/master/src/network/index.ts), [character animations and movement](https://github.com/wuzi/labirong3d-client/blob/master/src/entities/player.ts).
- Status: Client repository; the multiplayer backend is separate. The hard-coded server URL and repository homepage were not tested. Do not label it a standalone offline game.

### brawlio

- Retain URL: https://github.com/Wuzi/brawlio
- Description: **A browser arena where players jump across platforms and trade fireballs in real time. Phaser handles the 2D world and physics, while a Node.js and Socket.IO server relays movement and attacks.**
- Category / stack: Multiplayer games; JavaScript, Phaser, Node.js, Socket.IO.
- Evidence: [README: PvP brawl game](https://github.com/wuzi/brawlio/blob/master/README.md), [Phaser scene, controls, physics and projectiles](https://github.com/wuzi/brawlio/blob/master/public/game.js), [multiplayer server](https://github.com/wuzi/brawlio/blob/master/index.js).
- Status: Describe it as a game experiment, without promising current demo availability or server-authoritative simulation. README demo `brawlio.wuzi.dev` was not tested.

### vending

- Retain URL: https://github.com/Wuzi/vending
- Description: **Add interactive vending machines anywhere on a SA-MP server, with callbacks that let the gamemode decide prices, rewards and access. An in-game editor lets you place, customize and export machines.**
- Category / stack: Game server libraries; Pawn, SA-MP.
- Evidence: [README: purchase/drinking callbacks and custom machines](https://github.com/wuzi/vending/blob/master/README.md), [creator: in-game editing, colors and export](https://github.com/wuzi/vending/blob/master/vendingcreator.pwn).

### radars

- Retain URL: https://github.com/Wuzi/radars
- Description: **Build speed traps for SA-MP with configurable speed limits and detection radii. The Pawn library reports the player, radar and measured speed through a callback, so the gamemode can issue fines or trigger other events.**
- Category / stack: Game server libraries; Pawn, SA-MP.
- Evidence: [README: callback and fine example](https://github.com/wuzi/radars/blob/master/README.md), [library: max-speed/radius controls and callback signature](https://github.com/wuzi/radars/blob/master/radars.inc).

### streamersb

- Retain URL: https://github.com/Wuzi/streamersb
- Description: **A desktop soundboard for streamers: import local audio clips, assign global hotkeys and trigger sounds while another app has focus. Built with Electron and Vue, with sound lists and key bindings saved locally; the repository is archived.**
- Category / stack: Desktop tools; JavaScript, Electron, Vue.
- Evidence: [README: Electron/Vue project](https://github.com/wuzi/streamersb/blob/master/README.md), [UI: audio import, playback, key binding and localStorage](https://github.com/wuzi/streamersb/blob/master/src/renderer/components/LandingPage.vue), [main process: Electron global shortcuts](https://github.com/wuzi/streamersb/blob/master/src/main/index.js), [repository: archived flag](https://github.com/wuzi/streamersb).
- Status: GitHub reports `archived: true`. No audio routing, OBS integration or microphone injection is implemented in the inspected code; do not imply those features.

### houndbot

- Retain URL: https://github.com/Wuzi/houndbot
- Description: **A text-based Discord game built around League of Legends champions, with turn-based challenges between players. Abilities consume mana and use cooldowns, while Sequelize stores champions, experience and player progress.**
- Category / stack: Bots and games; TypeScript, Discord.js, Sequelize.
- Evidence: [README: Discord.js, TypeScript and database configuration](https://github.com/wuzi/houndbot/blob/master/README.md), [starter champion selection and League artwork](https://github.com/wuzi/houndbot/blob/master/src/commands/choose.ts), [duel rounds, mana, cooldowns and experience](https://github.com/wuzi/houndbot/blob/master/src/pools/duel.ts), [experience, level-ups and save](https://github.com/wuzi/houndbot/blob/master/src/helpers/duel.ts), [dependencies](https://github.com/wuzi/houndbot/blob/master/package.json).
- Correction: The old description says Pokémon-like, but the actual characters are League of Legends champions. Avoid adding catching/collecting mechanics that the inspected implementation does not establish. Package/README retain old `houndour/houndbot` self-links; the existing `Wuzi/houndbot` URL resolves publicly.
- Status: Uses Discord.js 11-era APIs; do not promise compatibility with today's Discord API without migration/testing.

### pgroups

- Retain URL: https://github.com/Wuzi/pgroups
- Description: **Organize SA-MP players into named groups such as gangs, police factions or staff teams. The Pawn library supports membership checks and messages targeted to one group or an entire group type.**
- Category / stack: Game server libraries; Pawn, SA-MP.
- Evidence: [README: named and typed groups, membership and group-type messaging](https://github.com/wuzi/pgroups/blob/master/README.md), [library API](https://github.com/wuzi/pgroups/blob/master/pgroups.inc).

### samp-missions

- Retain URL: https://github.com/Wuzi/samp-missions
- Description: **A Pawn prototype that recreates parts of GTA: San Andreas story mode inside SA-MP, with scripted cutscenes and subtitles. Its modular mission scripts include Home Invasion, alongside MySQL-backed player accounts.**
- Category / stack: Game modding; Pawn, SA-MP, MySQL.
- Evidence: [README: story missions and qualified cutscene support](https://github.com/wuzi/samp-missions/blob/master/README.md), [main: mission, account and visual modules](https://github.com/wuzi/samp-missions/blob/master/gamemodes/main.pwn), [Home Invasion: interiors, actors, carrying objects and noise/failure logic](https://github.com/wuzi/samp-missions/blob/master/modules/missions/homeinvasion.pwn).
- Status: Partial campaign prototype; never describe it as the complete GTA:SA campaign or imply cooperative mission play. The inspected mission uses per-player state/virtual worlds.

### uno-to-uno-rs485

- Retain URL: https://github.com/Wuzi/uno-to-uno-rs485
- Description: **Mirror digital inputs from one Arduino board to another over an RS485 link. Paired transmitter and receiver sketches encode nine pin states as serial commands and apply them to the remote board's outputs.**
- Category / stack: Embedded experiments; Arduino, C++, RS485, SoftwareSerial.
- Evidence: [README: two boards, RS485 and wiring](https://github.com/wuzi/uno-to-uno-rs485/blob/master/README.md), [transmitter: nine pin states and serial codes](https://github.com/wuzi/uno-to-uno-rs485/blob/master/transmitter/transmitter.ino), [receiver: codes mapped to output pins](https://github.com/wuzi/uno-to-uno-rs485/blob/master/receiver/receiver.ino).
- Status: Simple one-way hardware demonstration, sending every ten seconds; no reliability, distance, real-time control or industrial-protocol claims were established.

### ragemp-boilerplate

- Retain URL: https://github.com/Wuzi/ragemp-boilerplate
- Description: **A RAGE MP starter project with separate TypeScript modules for the GTA V multiplayer client and server. Includes MongoDB models through Mongoose, i18next localization and a React scaffold for embedded UI.**
- Category / stack: Developer tools and game servers; TypeScript, Node.js, RAGE MP, MongoDB, Mongoose, i18next, React.
- Evidence: [README: client/server modules, MongoDB and languages](https://github.com/wuzi/ragemp-boilerplate/blob/master/README.md), [package: builds, Mongoose and i18next](https://github.com/wuzi/ragemp-boilerplate/blob/master/package.json), [React UI scaffold](https://github.com/wuzi/ragemp-boilerplate/tree/master/src/views), [user/vehicle models](https://github.com/wuzi/ragemp-boilerplate/tree/master/src/server/models).
- Status: Historical scaffold; React is a scaffold, not a finished administration UI. Current RAGE MP compatibility was not tested.

### dynamicgz

- Retain URL: https://github.com/Wuzi/dynamicgz
- Description: **Turn SA-MP gang zones into gameplay triggers, with callbacks for players entering or leaving an area. The Pawn library wraps zone creation and includes an in-game tool for setting zone boundaries, choosing colors and exporting definitions.**
- Category / stack: Game server libraries; Pawn, SA-MP.
- Evidence: [README: zone creation and enter/leave callbacks](https://github.com/wuzi/dynamicgz/blob/master/README.md), [creator: position, color and export](https://github.com/wuzi/dynamicgz/blob/master/gz_creator.pwn).

### freeroam

- Retain URL: https://github.com/Wuzi/freeroam-samp
- Description: **A SA-MP gamemode that brings freeroam, racing, demolition derby and deathmatch together on one server. Includes dynamic race and map creation, a clothing and attachments shop, administration commands and MySQL-backed player data.**
- Category / stack: Game servers; Pawn, SA-MP, MySQL.
- Evidence: [README: modes, dynamic creation, shop and dependencies](https://github.com/wuzi/freeroam-samp/blob/master/README.md), [gameplay modules](https://github.com/wuzi/freeroam-samp/tree/master/modules/gameplay), [database schemas](https://github.com/wuzi/freeroam-samp/tree/master/tables).



### 1. whatsatui

- Repo: https://github.com/wuzi/whatsatui
- Language/year: Rust; repository created 2026.
- Status: Public, original, unarchived.
- Suggested description: **WhatsApp in the terminal, with keyboard-driven panes for chats, messages and composing. It supports fuzzy chat search, local history and drafts, inline images and stickers, plus audio and video playback.**
- Why it stands out: Immediately understandable everyday app with a substantial feature list and a screenshot, rather than another generic API example.
- Evidence: https://github.com/wuzi/whatsatui/blob/main/README.md documents Rust/Ratatui, direct and existing group chats, fuzzy switching, drafts, cached history, inline images/stickers/GIFs, mpv audio/video, downloads, and pane controls. The README includes a screenshot: https://github.com/user-attachments/assets/503bd6d4-bd16-423b-bfb4-fd3718ad7de8
- Demo: Screenshot in the README; no hosted interactive demo verified. Do not call it an official WhatsApp client or imply WhatsApp endorsement.
- Metadata: https://api.github.com/repos/wuzi/whatsatui

### 2. Cue

- Repo: https://github.com/wuzi/cue
- Language/year: Rust; repository created 2026. Native GTK4/libadwaita application for GNOME.
- Status: Public, original, unarchived.
- Suggested description: **A GNOME scratchpad that turns a line like `Call Ada @tomorrow 9am` into a desktop reminder. Notes stay in a local SQLite database, and reminders can be completed or snoozed directly from their notifications.**
- Why it stands out: A specific, useful interaction; a native desktop app with screenshots and a downloadable release.
- Evidence: https://github.com/wuzi/cue/blob/master/README.md documents inline `@schedule` syntax, local SQLite storage, Rust/GTK4/libadwaita, GNOME theme integration, and Done/snooze notification actions.
- Screenshot: https://github.com/wuzi/cue/blob/master/data/screenshots/cue.png
- Download: https://github.com/wuzi/cue/releases/tag/0.2.0 — fetched release metadata confirms a `Cue-0.2.0-x86_64.flatpak` asset, published by wuzi on 2026-08-16.
- Boundary: Reminder delivery after logout/reboot/forced termination is not promised; README says overdue reminders deliver on the next start. Do not imply a background system service.
- Metadata: https://api.github.com/repos/wuzi/cue

### 3. Paradise City RPG (SA-MP)

- Repo: https://github.com/Paradise-Devs/pc-rpg-gamemode
- Language: Pawn; MySQL persistence. Initial public authored commits date to 2015; current org repository was created in 2017.
- Status: Public, original, unarchived.
- Suggested description: **A city-life RPG for GTA: San Andreas Multiplayer, with jobs, player-owned homes and businesses, factions and vehicle systems. The Pawn gamemode ties those systems together with persistent player and world data in MySQL.**
- Why it stands out: A substantial game world, connecting many of the smaller SA-MP libraries already on the project page.
- Evidence: https://github.com/Paradise-Devs/pc-rpg-gamemode/blob/master/README.md explains the SA-MP RPG purpose and MySQL setup. Public recursive source tree verifies modules for bus drivers, fishing, garbage collection, taxis and other jobs; apartments/houses/businesses/vehicles; factions; player data; and `database/pcrpg.sql`.
- Source links: https://github.com/Paradise-Devs/pc-rpg-gamemode/tree/master/modules/job ; https://github.com/Paradise-Devs/pc-rpg-gamemode/tree/master/modules/properties ; https://github.com/Paradise-Devs/pc-rpg-gamemode/tree/master/modules/faction ; https://github.com/Paradise-Devs/pc-rpg-gamemode/tree/master/modules/data ; https://github.com/Paradise-Devs/pc-rpg-gamemode/blob/master/database/pcrpg.sql
- Authorship: Public commit search `initial author:wuzi is:public` returns https://github.com/Paradise-Devs/pc-rpg-gamemode/commit/ed8fe58336690d56e1648bfd2be5ea80dcc286df and https://github.com/Paradise-Devs/pc-rpg-gamemode/commit/ce2135c4787231e1884b31753831bcb973b1bedd . This supports contribution/authorship, not sole authorship; avoid claiming Wuzi built everything alone.
- Demo: No current live server verified. Repository homepage `http://pc-rpg.com.br` was not validated; omit it.
- Metadata: https://api.github.com/repos/Paradise-Devs/pc-rpg-gamemode

### 4. poe-idle

- Repo: https://github.com/wuzi/poe-idle
- Language/year: Rust; repository created 2026. Bevy 0.18.1 dependency.
- Status: Public, original, unarchived. Present as a **prototype**, not a released/finished game.
- Suggested description: **An idle RPG prototype in Rust and Bevy, where your character automatically moves through maps and fights enemy packs. Its progression systems explore loot, equipment, crafting and talents, with player progress saved locally.**
- Why it stands out: A more recent game project with an automatic-combat hook and visible game systems.
- Evidence: https://github.com/wuzi/poe-idle/blob/master/Cargo.toml verifies Rust/Bevy. https://github.com/wuzi/poe-idle/blob/master/src/gameplay.rs implements `begin_current_map`, map selection/transitions, enemy packs, automatic movement, health regeneration and `player_attack`; imports `roll_item`, item descriptions and player-derived stats. https://github.com/wuzi/poe-idle/blob/master/src/save.rs defines a five-second save interval, serialized player profile, saved map index and atlas tier.
- Additional system source: https://github.com/wuzi/poe-idle/blob/master/src/data/items.rs ; https://github.com/wuzi/poe-idle/blob/master/src/data/crafting.rs ; https://github.com/wuzi/poe-idle/blob/master/src/data/talents.rs ; https://github.com/wuzi/poe-idle/blob/master/src/ui/crafting.rs ; https://github.com/wuzi/poe-idle/blob/master/src/ui/talents.rs . These paths exist in the fetched public recursive tree; the gameplay and save files above were read in detail. Keep wording at prototype/system level.
- Demo: No README or hosted demo verified. Do not claim offline progression, a complete Path of Exile recreation, or production polish.
- Metadata: https://api.github.com/repos/wuzi/poe-idle

### 5. HuaweiOLTSDK

- Repo: https://github.com/wuzi/HuaweiOLTSDK
- Language/year: Go; repository created 2023.
- Status: Public, original, unarchived. No README found; source was checked.
- Suggested description: **A Go SDK for working with Huawei fiber-network equipment through its command-line interface. It handles command prompts and turns ONT discovery, optical readings and service-port output into structured Go data.**
- Why it stands out: A specific infrastructure problem outside the usual portfolio app examples.
- Evidence: https://github.com/wuzi/HuaweiOLTSDK/blob/master/pkg/sshclient/command_executor.go opens a shell, tracks command level/frame/slot, executes CLI commands and exposes `GetUnmanagedOpticalNetworkTerminals`, `GetOpticalInfo`, `GetGeneralInfoBySn`, and `GetServicePorts`. https://github.com/wuzi/HuaweiOLTSDK/blob/master/pkg/sshclient/parser.go defines/parses unmanaged ONTs and optical information including receive/transmit power, temperature and voltage. The repository description is “send commands to Huawei OLT in Go.”
- Demo: No hosted demo verified. Do not imply broad device-model support or production safety guarantees.
- Metadata: https://api.github.com/repos/wuzi/HuaweiOLTSDK

### 6. asaas

- Repo: https://github.com/wuzi/asaas
- Language/year: Rust; repository created 2026.
- Status: Public, original, unarchived.
- Suggested description: **A typed Rust SDK for Asaas payments, covering customers, charges, Pix QR codes and installment payment books. It also exposes payment and refund details for reconciliation, preserving monetary response values without floating-point conversion.**
- Why it stands out: A practical Brazilian payments integration with specific work on response fidelity and uncertain requests.
- Evidence: https://github.com/wuzi/asaas/blob/master/README.md — endpoint list includes customer creation, payment creation/update, Pix QR codes, billing information, installment lists and PDFs; reconciliation section documents `get_payment_details`, refunds and arbitrary-precision `serde_json::Number` monetary responses. Do not imply every request DTO uses decimals: the quick-start payment value is a float.
- Demo: Library; no hosted demo verified. README has usage examples.
- Metadata: https://api.github.com/repos/wuzi/asaas

