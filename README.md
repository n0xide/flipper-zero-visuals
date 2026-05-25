# Flipper Zero Visuals

Interactive HTML visualizations for a self-taught Flipper Zero curriculum
covering Sub-GHz, card technologies (LF + HF NFC), Bad USB, wireless
(BLE / WiFi / NRF24), and GPIO + hardware hacking. ~31 visualizations across
5 phase pages plus a hub index — all self-contained, offline-capable.

**Live site:** <https://n0xide.github.io/flipper-zero-visuals/>

## What's inside

| File | Phase | Topics covered |
|---|---|---|
| `index.html` | Hub | Master grid of all visualizations + phase navigation |
| `phase-2-subghz.html` | 02 | Modulation (AM/FM/ASK/OOK/FSK), capture vs replay vs rolling-code, frequency bands, common attacks |
| `phase-3-cards.html` | 03 | LF (EM4100, HID, Indala) + HF (MIFARE Classic, DESFire, NTAG); sector/block memory map; UID vs sector data |
| `phase-5-badusb.html` | 05 | HID injection script anatomy, payload examples, Rubber Ducky lineage, defensive postures |
| `phase-6-wireless.html` | 06 | BLE GATT, WiFi deauth ethics, NRF24 sniffing, RF spectrum overview |
| `phase-7-hardware.html` | 07 | GPIO pinout, SPI/I²C/UART probes, JTAG/SWD, glitching basics, logic analyzer reads |

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
