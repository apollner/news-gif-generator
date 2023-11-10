# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699626876)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Actors’ union reaches tentative deal with Hollywood film and TV studios, ending historic strike**

You can read more about it [here](https://news.google.com/rss/articles/CBMiTGh0dHBzOi8vd3d3LmNubi5jb20vMjAyMy8xMS8wOC9tZWRpYS9zYWctYWZ0cmEtYWN0b3JzLXN0cmlrZS1vdmVyL2luZGV4Lmh0bWzSAVBodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDIzLzExLzA4L21lZGlhL3NhZy1hZnRyYS1hY3RvcnMtc3RyaWtlLW92ZXIvaW5kZXguaHRtbA?oc=5).

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
