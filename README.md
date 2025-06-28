# NOVA — The Fee-Free, Standalone Voice Assistant

> **Status:** 🚧 In Development

NOVA is a standalone, cross-platform voice assistant designed to be a **showstopper-quality application** — not just a prototype. Unlike many hobby projects, NOVA aims for modern UI design, natural conversation flow, and robust offline capabilities, all without recurring fees for cloud services.

---

## 🎯 Project Goals

- **Free & Open-Source**  
  - No reliance on paid APIs for core functionality
  - Local speech recognition and TTS wherever possible

- **Modern Voice Interaction**  
  - Speech-to-text with high accuracy
  - Natural language understanding (NLU)
  - Context memory for follow-up commands
  - Text-to-speech with natural-sounding voices

- **Attractive UI**  
  - Cross-platform desktop application
  - Smooth animations and modern design
  - Chat-style conversation display

- **Extensible Skills**  
  - Reminder management
  - Weather info (using free APIs)
  - Local file searches
  - System commands (open apps, adjust volume, etc.)
  - Fun commands (jokes, trivia)

- **Privacy-First**  
  - Local processing preferred
  - User control over any network connections

---

## ✅ Current Status

### ✔️ Completed

- **Project Planning**
  - Defined architecture goals
  - Decided on free/open-source stack
  - Drafted development roadmap

---

### 🔨 In Progress

- **Reminder Engine (Python)**
  - Currently building:
    - Create reminders
    - Delete reminders
    - Modify reminders
  - Persistence layer still in development

- Evaluating open-source speech-to-text engines:
  - Whisper
  - Vosk
- Prototyping text-to-speech with:
  - pyttsx3
  - Coqui TTS
- Planning the UI:
  - Electron (Node.js + HTML/CSS/JS)
- Designing the NLP intent system:
  - spaCy
  - HuggingFace transformers
- Exploring Dockerization for modular components

---

## 🔧 Planned Tech Stack

| Component            | Proposed Tools              |
|-----------------------|-----------------------------|
| Speech-to-Text (STT)  | Whisper (via whisper.cpp)   |
| Text-to-Speech (TTS)  | Coqui TTS / pyttsx3         |
| NLP / Intent Parsing  | spaCy, Transformers         |
| UI                    | Electron + Node.js          |
| Database              | PostgreSQL or SQLite        |
| Containerization      | Docker                      |
| Orchestration (opt.)  | Temporal (if feasible)      |
| APIs                  | Free APIs like Open-Meteo   |

---

## 🛣️ Roadmap

- **Phase 1: Audio Pipeline**
  - Build offline STT and TTS prototypes
- **Phase 2: NLP & Intent Engine**
  - Design intent structure and command handling
- **Phase 3: UI Development**
  - Build Electron-based desktop interface
- **Phase 4: Complete Reminder Engine**
  - Finish create, delete, modify reminders
  - Integrate reminders into NOVA’s conversation flow
- **Phase 5: Polish & Expand**
  - Add new skills
  - Optimize performance
  - Implement wake-word detection (optional)

---

## 💡 Why NOVA?

There are plenty of voice assistants out there, but:
- Most depend on paid cloud services
- Few respect user privacy
- Many feel like demos rather than polished products

NOVA aims to change that by being:
- Free
- Open-source
- Private
- Beautiful
- Extensible

---

## 🤝 Contributions

Right now, NOVA is a solo project in early development. Contributions will be welcome once the architecture stabilizes!

---

## License

To be determined (MIT / Apache 2.0 preferred).

---

### Stay tuned for more updates as NOVA evolves into a true showstopper voice assistant!
