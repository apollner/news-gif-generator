# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1704231226)

## Latest News Headline
The latest news headline used to generate the GIF is:

**‘Wonka’ Wins New Year’s Box Office Battle With $29.5 Million, 2023 Domestic Ticket Sales Top $9 Billion**

You can read more about it [here](https://variety.com/2024/film/news/wonka-wins-new-years-box-office-2023-domestic-ticket-sales-final-numbers-1235859046/).

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
