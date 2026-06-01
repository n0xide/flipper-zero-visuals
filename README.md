# Flipper Zero Visuals

Interactive HTML visualizations for a self-taught Flipper Zero curriculum
covering device foundations, Sub-GHz, card technologies (LF + HF NFC), IR +
iButton, Bad USB, wireless (BLE / WiFi / NRF24), GPIO + hardware hacking,
the blue-team defense matrix, and integration capstones across 5 canonical
environments. ~50 visualizations across 9 phase pages plus a hub index and
a searchable glossary — all self-contained, offline-capable. Every phase
opens with a legality callout so the reader knows which workflows are public
practice and which need authorization, ends with a 5-question understanding
check, and cross-links to the Phase 8 defense matrix for every attack class
taught.

Calculator state (Phase 2 brute-force, Phase 6 PSK, Phase 8 filter/sort)
serialises into the URL hash — links are shareable. Keyboard-first
navigation throughout (GPIO pins, MIFARE sectors, matrix headers, audit-chain
steps), and `prefers-reduced-motion` honoured on every page.

**Live site:** <https://n0xide.github.io/flipper-zero-visuals/>

## What's inside

| File | Phase | Topics covered |
|---|---|---|
| `index.html` | Hub | Master grid of all visualizations + phase navigation |
| `phase-1-foundations.html` | 01 | Interactive Flipper teardown (top view + inside); chip-to-phase map; 3-tier bench gear checklist with budget tags; firmware ecosystem comparison (OFW vs Momentum vs Xtreme) |
| `phase-2-subghz.html` | 02 | Modulation (ASK/OOK/2-FSK), encoding (NRZ/Manchester/PWM), fixed vs rolling code, KeeLoq packet anatomy, RollJam timeline, brute-force math |
| `phase-3-cards.html` | 03 | LF (EM4100, HID) + HF (MIFARE Classic, DESFire, NTAG); sector/block map; Crypto1 attack ladder + decision matrix (dictionary → nested → hardnested → darkside → mfkey32); EMV clarity; clone workflow |
| `phase-4-ir-ibutton.html` | 04 | 38 kHz IR physics; NEC vs RC5 vs SIRC vs Pronto waveform comparison; Flipper IR capability matrix; 1-Wire iButton bus model + DS1990A read sequence + clone workflow |
| `phase-5-badusb.html` | 05 | HID injection premise (USB enumeration); annotated Ducky Script; Stage 1 → Stage 2 chain (8-step animated); 6-ring defense onion with named products (USBGuard, BeamGun, Defender ASR); keyboard-layout footgun (live US/AZERTY/QWERTZ/Dvorak transliteration) |
| `phase-6-wireless.html` | 06 | BLE address types + tracking sim; WPA2 4-way handshake step-through; PMKID-attack flow; PMF on/off comparison; evil twin diagram; MouseJack; PSK crack-time calculator (length × charset × GPU rate) |
| `phase-7-hardware.html` | 07 | Keyboard-accessible 18-pin GPIO header (canonical pinout); UART/SPI/I²C wiring + timing; SOIC-8 SPI flash dumping + CH341A; 8-step audit chain; ARM Cortex-M RDP levels; voltage / level-shift matrix |
| `phase-8-defense.html` | 08 | Sortable attack→defense matrix (30 rows across Phases 2-7, filterable by phase, sortable by cost, deep-linkable per row); detection-layer breakdown (physical / RF / EDR / network / access / USB / tamper); 7-section audit deliverable checklist; remediation priority list |
| `phase-9-capstones.html` | 09 | Five scenario site maps (home, office, vehicle, IoT, OT) with clickable attack-surface hotspots; per-scenario scoping checklist; 5-stage engagement playbook; every hotspot cross-links to the matching Phase 8 defense row |
| `glossary.html` | All | Searchable glossary of every acronym used across the curriculum (PMKID, RDP, Crypto1, hashcat, IRK, MIC, PTK, GTK, FAP, SWD, …). Tagged by domain. Each entry links back to the phase(s) where it appears. |

All visualizations are interactive — sliders, animated waveforms, clickable diagrams.

## Ethics & legal note

This curriculum is for **white-hat / ethical / lab-only** study. Anything taught
here applies to systems you own, systems you have explicit written permission to
test, or generic protocol education. Do not use against systems you don't own or
have authorization to test. See your local jurisdiction's computer-misuse laws.

## How to use

**Online** — open the live URL above.

**Offline** — clone or download:

```bash
git clone https://github.com/n0xide/flipper-zero-visuals.git
cd flipper-zero-visuals
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

No build step. No external CSS/JS/CDN. Works from `file://`.

## Structure

```
.
├── index.html              ← hub: links to all phases
├── README.md
├── LICENSE                 ← MIT
├── MAINTAINING.md          ← agent / contributor workflow
├── phase-2-subghz.html
├── phase-3-cards.html
├── phase-5-badusb.html
├── phase-6-wireless.html
└── phase-7-hardware.html
```

## License

[MIT](LICENSE). Educational content — use at your own risk; the legal /
ethical constraints in the "Ethics & legal note" above remain your
responsibility.

## Source

Derived from a personal cybersecurity study workspace. The markdown
curriculum sources (phase notes, exercises, references) live in the
source workspace and are not published here. See `MAINTAINING.md` for
the round-trip workflow.
