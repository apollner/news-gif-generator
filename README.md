# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1702629339)

## Latest News Headline
The latest news headline used to generate the GIF is:

**US Dollar Sinks on Fed Dovish Pivot, Setups on EUR/USD, USD/JPY, GBP/USD**

You can read more about it [here](https://www.dailyfx.com/news/forex-usd-dollar-sinks-on-fed-dovish-pivot-setups-on-eur-usd-usd-jpy-gbp-usd-20231213.html).

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
