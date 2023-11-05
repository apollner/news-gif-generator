# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699205630)

## Latest News Headline
The latest news headline used to generate the GIF is:

**No. 7 Texas vs. No. 23 Kansas State live updates: AD Mitchell catches 37-yard TD pass for 7-0 lead**

You can read more about it [here](https://www.burntorangenation.com/2023/11/4/23946220/texas-longhorns-kansas-state-wildcats-live-updates-scores-injuries).

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
