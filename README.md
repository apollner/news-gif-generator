# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699340787)

## Latest News Headline
The latest news headline used to generate the GIF is:

**2023 LACMA Art + Film Gala: Kim Kardashian, Jennifer Lopez & More Stars Hit the Carpet! (Pics)**

You can read more about it [here](https://www.etonline.com/gallery/2023-lacma-art-film-gala-kim-kardashian-jennifer-lopez-more-stars-hit-the-carpet-214271?utm_content=ETOnline%2Fmagazine%2FPhotos&utm_source=flipboard).

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
