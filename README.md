# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1704267231)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Taylor Swift & Travis Kelce cruise in a Rolls-Royce after New Year's party**

You can read more about it [here](https://www.hindustantimes.com/entertainment/music/taylor-swift-travis-kelce-roll-out-in-400k-rolls-royce-after-rocking-brittany-patricks-new-years-101704164911017.html).

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
