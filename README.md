# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699932895)

## Latest News Headline
The latest news headline used to generate the GIF is:

**NFL Week 10 grades: Lions earn 'A' for thrilling win vs. Chargers; Cards get 'B' in Kyler Murray's 2023 debut**

You can read more about it [here](https://www.cbssports.com/nfl/news/nfl-week-10-grades-raiders-earn-b-for-sunday-night-win-over-jets-browns-get-an-a-for-stunning-ravens/).

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
