# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1694250600)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Hong Kong paralyzed by flash flooding after heaviest rainfall since 1884**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWmh0dHBzOi8vd3d3LmNubi5jb20vMjAyMy8wOS8wNy9hc2lhL2hvbmcta29uZy1ibGFjay1yYWluc3Rvcm0tZmxvb2RpbmctaW50bC1obmsvaW5kZXguaHRtbNIBXmh0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjMvMDkvMDcvYXNpYS9ob25nLWtvbmctYmxhY2stcmFpbnN0b3JtLWZsb29kaW5nLWludGwtaG5rL2luZGV4Lmh0bWw?oc=5).

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
