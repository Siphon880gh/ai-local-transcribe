"""
Batch-transcribe sequentially named audio files like:
  a.m4a, b.m4a, c.m4a, ...

How it works:
1) We look for files in alphabetical order: a, b, c, ...
2) For each letter, we check multiple audio extensions (m4a first, since iPhone Voice Memos are often .m4a).
   Example: for "a" we try: a.m4a, a.mp3, a.wav, ...
3) If we find a match, we add the filepath to a list.
4) Once we hit the first missing letter (e.g., no "d.*"), we stop (assumes your sequence is contiguous).
5) We load the Whisper model once, then transcribe each file in order and print the text.

Usage:
- Put your files in the same folder as this script (or change AUDIO_DIR).
- Name them a.m4a, b.m4a, c.m4a, etc (or a.mp3 / a.wav, etc).
"""

from pathlib import Path
import whisper

# Folder to scan (default: current folder)
AUDIO_DIR = Path(".")

# Check m4a first, then other common audio formats Whisper can handle.
EXT_PREFERENCE = [
    "m4a",  # iPhone Voice Memos commonly
    "mp3",
    "wav",
    "flac",
    "aac",
    "ogg",
    "wma",
    "webm",
    "mp4",
    "mkv",
]

def find_sequential_audio_files(folder: Path) -> list[Path]:
    files: list[Path] = []

    # Scan a, b, c, ... z
    for code in range(ord("a"), ord("z") + 1):
        base = chr(code)
        found = None

        # Try extensions in preferred order
        for ext in EXT_PREFERENCE:
            candidate = folder / f"{base}.{ext}"
            if candidate.is_file():
                found = candidate
                break

        if found:
            files.append(found)
        else:
            # Stop at the first missing letter (contiguous sequence assumption)
            break

    return files

def main():
    audio_files = find_sequential_audio_files(AUDIO_DIR)

    if not audio_files:
        print(f"No sequential audio files found in: {AUDIO_DIR.resolve()}")
        print("Expected something like: a.m4a (or a.mp3/a.wav/etc), then b.m4a, c.m4a, ...")
        return

    print("Found files (in order):")
    for p in audio_files:
        print(f" - {p.name}")

    # Load the model once (faster than reloading per file)
    model = whisper.load_model("small")

    print("\n--- Transcriptions ---\n")
    for p in audio_files:
        result = model.transcribe(str(p))
        print(f"[{p.name}]")
        print(result["text"].strip())
        print()

if __name__ == "__main__":
    main()
