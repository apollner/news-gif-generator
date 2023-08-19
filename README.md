# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1692464761)

## Latest News Headline
The latest news headline used to generate the GIF is:

**‘Having an adorable 15lb mutt as a hero made my job a little bit easier’: Strays director Josh Greenbaum**

You can read more about it [here](https://www.theguardian.com/film/2023/aug/18/having-an-adorable-15lb-mutt-as-a-hero-made-my-job-a-little-bit-easier-strays-director-josh-greenbaum).

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
