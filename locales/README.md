# 🌐 Localization Guide

The Broader Movement is maintained in **English** as the source language. Translations live in this directory, one folder per language code (ISO 639-1 or BCP 47).

## Available languages

| Code | Language | Status |
|---|---|---|
| `en` | English | ✅ Source |
| `ru` | Русский | ✅ Available |

## Structure

```
locales/
├── README.md          # this guide
└── ru/
    ├── README.md
    ├── BROADER_MANIFESTO.md
    ├── BROADER_LICENSE.md
    ├── BROADER_SPEC.txt
    └── BROADER_LIBRARY.md
```

## How to add a language

1. Create a folder `locales/<code>/` (for example `locales/es/`).
2. Copy each root file into it and translate it fully.
3. Keep the filenames identical (`README.md`, `BROADER_MANIFESTO.md`, …).
4. Add the language to the switcher at the top of [`README.md`](../README.md) and to the table above.
5. Open a Pull Request.

## Rules

- Translate the *meaning*, not word-for-word; keep the tone — visionary, rebellious, ethical.
- Keep `BROADER_SPEC.txt` ASCII-aligned (every line the same width) in every language.
- Keep links pointing to the original English files unless a translated file exists.
- Do not invent new terms — reuse **Broading**, **Broader**, **to Broad**, and the **Broader Loop** as-is.
