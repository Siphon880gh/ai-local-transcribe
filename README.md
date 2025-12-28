# Whisper Transcription Tool

**By Weng**

![Last Commit](https://img.shields.io/github/last-commit/Siphon880gh/ai-local-transcribe/main)
<a target="_blank" href="https://github.com/Siphon880gh" rel="nofollow"><img src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" alt="Github" data-canonical-src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" style="max-width:8.5ch;"></a>
<a target="_blank" href="https://www.linkedin.com/in/weng-fung/" rel="nofollow"><img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue" alt="Linked-In" data-canonical-src="https://img.shields.io/badge/LinkedIn-blue?style=flat&amp;logo=linkedin&amp;labelColor=blue" style="max-width:10ch;"></a>
<a target="_blank" href="https://www.youtube.com/@WayneTeachesCode/" rel="nofollow"><img src="https://img.shields.io/badge/Youtube-red?style=flat&logo=youtube&labelColor=red" alt="Youtube" data-canonical-src="https://img.shields.io/badge/Youtube-red?style=flat&amp;logo=youtube&amp;labelColor=red" style="max-width:10ch;"></a>

A simple speech-to-text transcription tool using OpenAI's Whisper model. Ideal for transcribing voice memos you've AirDropped from your iPhone.

## Setup

Install [`ffmpeg`](https://ffmpeg.org/):

```bash
# on macOS using Homebrew (https://brew.sh/)
brew install ffmpeg
```

Install the `whisper` package:

```bash
pip install openai-whisper
```

## Usage

### Batch Transcription (Multiple Files)

Use `start.py` to transcribe multiple audio files at once. Perfect for voice memos you've AirDropped into this folder.

**How it works:**
1. Name your files sequentially: `a.m4a`, `b.m4a`, `c.m4a`, `d.m4a`, etc.
2. Run the script — it finds all sequential files and transcribes them in order
3. Stops at the first missing letter (e.g., if you have a, b, c but no d, it stops after c)

**Supported formats:** m4a (preferred), mp3, wav, flac, aac, ogg, wma, webm, mp4, mkv

```bash
python start.py
```

Example output:
```
Found files (in order):
 - a.m4a
 - b.m4a
 - c.m4a

--- Transcriptions ---

[a.m4a]
This is my first voice memo...

[b.m4a]
And here's the second one...

[c.m4a]
The third memo continues...
```

### Single File Transcription

Use `direct.py` for transcribing a single audio file.

1. Place your audio file in this folder
2. Edit `direct.py` and change `"INPUT.m4a"` to your filename
3. Run:

```bash
python direct.py
```

## Tips

- **Voice Memos Workflow:** AirDrop your voice memos from iPhone, rename them to a.m4a, b.m4a, c.m4a, etc., then run `python start.py`
- The model used is `small` by default — good balance of speed and accuracy
- For better accuracy on longer recordings, consider using `medium` or `large` models (edit the script to change)
