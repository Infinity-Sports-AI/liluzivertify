# Lil Uzi Vertify

<!-- [![PyPI version](https://badge.fury.io/py/project-name.svg)](https://badge.fury.io/py/project-name) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Quickstart

Lil Uzi Vertify is an open-source Python library that automatically converts long videos into
clips. With just a few lines of code, you can segment a video into multiple clips and
resize its aspect ratio from 16:9 to 9:16.

> **Note:** Lil Uzi Vertify is designed for audio-centric, narrative-based videos such as
podcasts, interviews, speeches, and sermons. It actively employs video transcripts to
identify and create clips. Our resizing algorithm dynamically reframes and focuses on
the current speaker, converting the video into various aspect ratios.

For full documentation, visit [Lil Uzi Vertify Documentation](https://liluzivertify.com).
Check out a [UI demo](https://demo.liluzivertify.com) with clips generated by this library.

### Installation

1. Install Python dependencies. <br></br> *We highly suggest using a virtual environment (such as [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)) to avoid dependency conflicts*
    ```bash {{ language: 'python' }}
    pip install lil-uzi-vertify
    ```

    ```bash {{ language: 'python' }}
    pip install whisperx@git+https://github.com/m-bain/whisperx.git
    ```

2. Install [libmagic](https://github.com/ahupp/python-magic?tab=readme-ov-file#debianubuntu)

3. Install [ffmpeg](https://github.com/kkroening/ffmpeg-python/tree/master?tab=readme-ov-file#installing-ffmpeg)

### Creating clips

Since clips are found using the video's transcript, the video must first be transcribed. Transcribing is done with [WhisperX](https://github.com/m-bain/whisperX), an open-source wrapper on [Whisper](https://github.com/openai/whisper) with additional functionality for detecting start and stop times for each word. For trimming the original video into a chosen clip, refer to the clipping reference.
