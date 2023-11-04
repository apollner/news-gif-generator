# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699090424)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Double Surprise: NASA's Lucy Spacecraft Makes “Marvelous” Discovery During Asteroid Dinkinesh Flyby**

You can read more about it [here](https://news.google.com/rss/articles/CBMieWh0dHBzOi8vc2NpdGVjaGRhaWx5LmNvbS9kb3VibGUtc3VycHJpc2UtbmFzYXMtbHVjeS1zcGFjZWNyYWZ0LW1ha2VzLW1hcnZlbG91cy1kaXNjb3ZlcnktZHVyaW5nLWFzdGVyb2lkLWRpbmtpbmVzaC1mbHlieS_SAQA?oc=5).

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
