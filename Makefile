.PHONY: help run

# Default target
all: run

run:
	@echo "This is an audio file to transcription tool using Whisper small installed on the system."
	@echo "Run 'make help' to get more details."
	@python3 start.py

help:
	@echo "Audio Transcription Tool - Help"
	@echo "================================"
	@echo ""
	@echo "Instructions:"
	@echo "1. Drop your audio file in this folder"
	@echo "2. Adjust the target path of audio file in start.py"
	@echo ""
	@echo "Usage:"
	@echo "  make        - Run the transcription tool"
	@echo "  make help   - Show this help message"
	@echo "  make run    - Run the transcription tool"
