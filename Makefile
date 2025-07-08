
# Elara Makefile - Useful setup and run commands

# Usage:
#   make venv        -> Create virtual environment
#   make install     -> Install Python dependencies
#   make run         -> Run Elara bot
#   make clean       -> Remove temporary files and caches

venv:
	python -m venv .venv
	@echo "✅ Virtual environment created."

install:
	.venv\Scripts\activate && pip install -r requirements.txt
	@echo "✅ Dependencies installed."

run:
	.venv\Scripts\activate && python main.py

clean:
	rmdir /s /q __pycache__
	del /s *.pyc
	del /s *.wav
	@echo "🧹 Cleaned up build files."
