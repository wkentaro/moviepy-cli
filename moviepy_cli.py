import argparse
import tempfile

import moviepy.editor
import path


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("input_file", type=path.Path, help="input file")
    parser.add_argument("--start", type=float, help="start time")
    parser.add_argument("--retime", type=float, help="retime")
    parser.add_argument("--inplace", action="store_true", help="inplace")
    parser.add_argument("--output-file", type=path.Path, help="output file")
    args = parser.parse_args()

    args.input_file = args.input_file.abspath()

    clip = moviepy.editor.VideoFileClip(args.input_file)

    if args.start:
        clip = clip.subclip(args.start)
    if args.retime:
        clip = clip.fx(moviepy.editor.vfx.speedx, args.retime)

    if args.output_file is None:
        args.output_file = path.Path(
            tempfile.mktemp(
                prefix=args.input_file.stem + ".",
                suffix=".mp4",
                dir=args.input_file.parent,
            )
        )
    clip.write_videofile(args.output_file)

    if args.inplace:
        print(
            f"Moviepy-cli - Replacing {args.input_file} by {args.output_file}"
        )
        args.output_file.move(args.input_file)
