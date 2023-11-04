# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699070952)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Parents are struggling to get the new RSV drug for their babies. Here's what it's like.**

You can read more about it [here](https://news.google.com/rss/articles/CBMiYmh0dHBzOi8vd3d3LnlhaG9vLmNvbS9saWZlc3R5bGUvcGFyZW50cy1zdHJ1Z2dsaW5nLXRvLWdldC1yc3YtZHJ1Zy1iYWJpZXMtYmV5Zm9ydHVzLTIyMDIxNDY2Mi5odG1s0gFqaHR0cHM6Ly93d3cueWFob28uY29tL2FtcGh0bWwvbGlmZXN0eWxlL3BhcmVudHMtc3RydWdnbGluZy10by1nZXQtcnN2LWRydWctYmFiaWVzLWJleWZvcnR1cy0yMjAyMTQ2NjIuaHRtbA?oc=5).

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
