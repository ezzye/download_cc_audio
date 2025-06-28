#!/usr/bin/env python3
"""
Download the audio track (as .m4a) from a Creative Commons
YouTube video.  Requires:
  pip install yt-dlp
and a working ffmpeg binary on your PATH.
Usage:
  python download_cc_audio.py "https://www.youtube.com/watch?v=VIDEO_ID"
"""

import sys
import subprocess
from pathlib import Path

def download_audio(url: str, out_dir: Path = Path(".")) -> Path:
    """
    Download audio from a YouTube URL using yt-dlp.

    Parameters
    ----------
    url : str
        Full YouTube URL.
    out_dir : Path, optional
        Directory to save the file.

    Returns
    -------
    Path
        Path to the downloaded audio file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    # yt-dlp output template: %(title)s-%(id)s.%(ext)s
    output_tpl = str(out_dir / "%(title)s-%(id)s.%(ext)s")
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "m4a",
        "--audio-quality", "0",          # best quality
        "--write-info-json",             # keep metadata
        "--write-thumbnail",
        "--embed-thumbnail",
        "--add-metadata",
        url,
        "-o", output_tpl,
    ]
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd)
    # yt-dlp fills in %(ext)s; find resulting file
    downloaded = max(out_dir.glob("*-*.m4a"), key=lambda p: p.stat().st_mtime)
    return downloaded

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_cc_audio.py <YouTube_URL>")
        sys.exit(1)

    video_url = sys.argv[1]
    try:
        audio_file = download_audio(video_url)
        print(f"Audio saved to: {audio_file.resolve()}")
    except subprocess.CalledProcessError as e:
        print("yt-dlp/ffmpeg failed:", e)
        sys.exit(e.returncode)
