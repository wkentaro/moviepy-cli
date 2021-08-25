# moviepy-cli

Moviepy-cli is designed to apply **several video editing in a single command** and to be used as an alternative to [video-cli](https://github.com/wkentaro/video-cli).

## Usage

```bash
moviepy --start 8 --retime 2 data/annotation.mp4
```

```bash
usage: moviepy [-h] [--start START] [--retime RETIME] [--inplace]
               [--output-file OUTPUT_FILE]
               input_file

positional arguments:
  input_file            input file

optional arguments:
  -h, --help            show this help message and exit
  --start START         start time (default: None)
  --retime RETIME       retime (default: None)
  --inplace             inplace (default: False)
  --output-file OUTPUT_FILE
                        output file (default: None)
```

## Tips

```bash
# edit video files in 4 processes maximum
echo *.mp4 | xargs -n1 -P4 moviepy --start 8 --retime 2
```
