# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1701956224)

## Latest News Headline
The latest news headline used to generate the GIF is:

**ADP National Employment Report: Private Sector Employment Increased by 103,000 Jobs in November; Annual Pay was Up 5.6%**

You can read more about it [here](https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-103-000-jobs-in-november-annual-pay-was-up-5-6-302007536.html).

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
