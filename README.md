# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1691550485)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Fans describe chaos and danger at Beyoncé concert as severe weather leads to crowd disaster at FedEx Field**

You can read more about it [here](https://wjla.com/news/local/beyonce-fans-renaissance-tour-describe-chaos-danger-concert-severe-weather-lightning-leads-crowd-fedex-field-washington-commanders-shelter-in-place-safety-heat-exhaustion).

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
