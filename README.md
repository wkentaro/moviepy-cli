<div align="center">
  <h1>moviepy-cli</h1>
  <h3>Command line interface for MoviePy.</h3>
  <a href="https://pypi.python.org/pypi/moviepy-cli"><img src="https://img.shields.io/pypi/v/moviepy-cli.svg"></a>
  <a href="https://pypi.org/project/moviepy-cli"><img src="https://img.shields.io/pypi/pyversions/moviepy-cli.svg"></a>
  <a href="https://github.com/wkentaro/moviepy-cli/actions"><img src="https://github.com/wkentaro/moviepy-cli/workflows/ci/badge.svg"></a>
</div>

Moviepy-cli is designed to **apply several video editing in a single command**
with [Moviepy](https://github.com/Zulko/moviepy) as an alternative to [Video-cli](https://github.com/wkentaro/video-cli).

## Installation

```bash
pip install moviepy-cli
```

## Usage

```bash
moviepy --start 8 --retime 2 data/annotation.mp4

# edit video files in 4 processes maximum
echo *.mp4 | xargs -n1 -P4 moviepy --start 8 --retime 2
```

```bash
usage: moviepy [-h] [--start START] [--end END] [--retime RETIME] [--inplace]
               [--scale SCALE] [--height HEIGHT] [--width WIDTH] [--fps FPS]
               [--output-file OUTPUT_FILE]
               input_file

positional arguments:
  input_file            input file

optional arguments:
  -h, --help            show this help message and exit
  --start START         start time (default: None)
  --end END             end time (default: None)
  --retime RETIME       retime (default: None)
  --inplace, -i         inplace (default: False)
  --scale SCALE         scale (default: None)
  --height HEIGHT       height (default: None)
  --width WIDTH         width (default: None)
  --fps FPS             fps (default: None)
  --output-file OUTPUT_FILE, -o OUTPUT_FILE
                        output file (default: None)
```
