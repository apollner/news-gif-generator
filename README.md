# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699095883)

## Latest News Headline
The latest news headline used to generate the GIF is:

**New US sanctions over Russia-Ukraine war target Lancet drones**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZmh0dHBzOi8vd3d3LmFsamF6ZWVyYS5jb20vbmV3cy8yMDIzLzExLzMvbmV3LXVzLXNhbmN0aW9ucy1vdmVyLXJ1c3NpYS11a3JhaW5lLXdhci10YXJnZXQtbGFuY2V0LWRyb25lc9IBamh0dHBzOi8vd3d3LmFsamF6ZWVyYS5jb20vYW1wL25ld3MvMjAyMy8xMS8zL25ldy11cy1zYW5jdGlvbnMtb3Zlci1ydXNzaWEtdWtyYWluZS13YXItdGFyZ2V0LWxhbmNldC1kcm9uZXM?oc=5).

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
