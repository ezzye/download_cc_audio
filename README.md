## **“Before you run it”** – MacBook workflow (Poetry + Homebrew)

1. **Make sure Homebrew is available**

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Poetry (Python dependency-manager)**

   ```bash
   brew install poetry        # easiest on macOS :contentReference[oaicite:0]{index=0}
   # --or--
   # curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Create a fresh project and lock dependencies**

   ```bash
   mkdir download-cc-audio && cd download-cc-audio
   poetry init --name download_cc_audio -n   # empty project, no prompts
   poetry add yt-dlp                         # adds yt-dlp to pyproject.toml
   ```

4. **Install FFmpeg via Homebrew**

   ```bash
   brew install ffmpeg      # brings in FFmpeg and all codecs :contentReference[oaicite:1]{index=1}
   ```

5. **Save the script** (from the previous message) as `download_cc_audio.py`
   in the same directory.

6. **Run the script inside Poetry’s virtual-env**

   ```bash
   poetry run python download_cc_audio.py "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

That’s it: Poetry keeps the Python bits isolated, while Homebrew supplies the system-wide FFmpeg binaries your Mac needs.
