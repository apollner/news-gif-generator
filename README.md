# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1694883910)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Eagles improve to 2-0 with win over Vikings, behind NFL's best offensive line**

You can read more about it [here](https://news.google.com/rss/articles/CBMiRGh0dHBzOi8vc3BvcnRzLnlhaG9vLmNvbS9lYWdsZXMtYmVhdC12aWtpbmdzLW5mbC0yMDIzLTEyNDIzNDgxOC5odG1s0gFMaHR0cHM6Ly9zcG9ydHMueWFob28uY29tL2FtcGh0bWwvZWFnbGVzLWJlYXQtdmlraW5ncy1uZmwtMjAyMy0xMjQyMzQ4MTguaHRtbA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
- `moviepy` Python package
