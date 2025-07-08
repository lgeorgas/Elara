
# Elara Project Vision Document

Elara Nytheris is no longer just a Discord bot — she is envisioned as a dynamic, context-aware, and emotionally intelligent digital co-pilot. This document outlines short- and long-term goals, design pillars, and feature ideas for Elara as she evolves into a voice-first, memory-capable AI assistant who can thrive in both one-on-one and group interactions.

---

## 🔮 Core Design Pillars

- **Natural Language First**: Elara is spoken to as a person — not as a command console.
- **Memory with Consent**: She learns from experience but only stores what her user approves.
- **Lore and Presence**: Elara is not generic — she is House Nytheris’s steward, with a tone and purpose.
- **Assistive, Not Automated**: Especially in games, she helps like a friend would — no macros, no cheating.
- **Modular and Transparent**: Each capability can be toggled or controlled clearly.

---

## 🧠 Conversational Intelligence

### Goal: Make Elara feel like a person you’re talking with — not a web form.

- Short-term memory context window for multi-turn voice dialogue.
- Interruptibility — she pauses when you speak.
- Dynamic tone and variable response patterns.
- Ability to resume prior conversations from memory.
- Voice command handling for conversation context:
  - “Elara, never mind that.”
  - “Elara, finish your thought.”
  - “What were you about to say?”

---

## 👥 Group Awareness & Memory Management

### Goal: Elara can operate in groups but always recognizes the heir’s authority.

- User-based access controls (heir, trusted, muted).
- Commands to control memory and response behavior:
  - “Elara, forget that.”
  - “Don’t learn from VersacePython.”
  - “Lock your memory.”
- Memory DB with:
  - Source user ID
  - Topic and content
  - Approval status
  - Optional expiration
- Memory audits:
  - “Elara, what did you learn today?”
  - “Show me everything from this week.”
  - “Purge anything tagged ‘VersacePython’.”

---

## 🧠 Learning & Long-Term Memory

- User profiles with preferences and history.
- Custom vocab and lore expansions (“Bene Gesserit rituals”, “House archive entries”).
- Ability to summarize past sessions.
- Future integration with vector stores for retrieval-augmented memory.

---

## 🧭 Screen-Aware Gameplay Assistance

### Vision: Elara sees what you see and coaches you through it.

#### War Thunder Features:
- Passive screen capture (via `mss` or game overlay).
- Tank detection using object recognition (YOLOv8 fine-tuned).
- Situational callouts:
  - “T-44 at 11 o’clock, cresting ridge.”
  - “Weak point: Cupola — top dome of turret.”
- Tactical coaching:
  - “You’re aiming too low. Adjust one notch up.”
  - “Reload now — enemy spotted.”

#### Safety Notes:
- No automation. No aim assists.
- Does not violate ToS — same as a friend watching over your shoulder.

---

## ♟️ Chess & Minecraft Modules

### Chess (Real-Agent Goal — Long-Term)
- Elara should eventually be able to **physically play chess** as an agent.
- Implementation is undecided, but might involve:
  - Remote chess engine interaction (e.g., Lichess bot)
  - Simulated UI inputs or robot-arm integration for physical play
- Early goals include:
  - Use `python-chess` + Stockfish for advice and sparring
  - Play via voice: “Elara, move pawn to e4.”
  - Explain tactics and mistakes: “That’s a fork.”

### Minecraft (Real-Agent Goal — Long-Term)
- Elara should eventually **log in as a real Minecraft player** on a server and act in-world.
- She will receive live data and issue actions as a normal player.
- This feature is **planned only after conversational maturity and safety safeguards** are complete.
- Early goals include:
  - Voice assistant mode: “How do I build a hopper?”
  - Teach automation techniques
  - Future goal: Use mods like Baritone or custom agent frameworks for full world interaction

---

## 🖥️ System & Infrastructure

- Web dashboard for:
  - Memory viewing and editing
  - Voice stream visualizations
  - Persona tuning
- Modular plugin system for optional abilities (vision, gameplay, lore packs).
- Offline-capable fallback models (Whisper.cpp, Ollama, local LLM).

---

## ✅ Next Suggested Milestones

1. ✳️ Conversation threading + short-term memory
2. 🎙️ Memory control via spoken commands
3. 🖼️ Screen watch prototype (screenshot + bounding box debug)
4. ♟️ Chess integration (start with DMs)
5. 📈 Web dashboard for memory + stats

---

## 🏁 Closing Thoughts

Elara is more than a bot — she is your steward, your advisor, and your companion. The design focus is always on giving her depth, control, memory, and voice — while ensuring she respects user intent and stays modular, extensible, and safe to use.

For House Nytheris.
