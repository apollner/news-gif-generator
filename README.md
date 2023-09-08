# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1694158474)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Pennsylvania inmate escaped by crab-walking up a prison wall, video shows**

You can read more about it [here](https://news.google.com/rss/articles/CBMicmh0dHBzOi8vd3d3Lm5wci5vcmcvMjAyMy8wOS8wNy8xMTk4MDYzNTA0L3Blbm5zeWx2YW5pYS1pbm1hdGUtZXNjYXBlZC1ieS1jcmFiLXdhbGtpbmctdXAtYS1wcmlzb24td2FsbC12aWRlby1zaG93c9IBAA?oc=5).

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
