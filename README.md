# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1698003206)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Hurricane Norma takes aim at Mexico's Los Cabos resorts, as Tammy threatens islands in the Atlantic**

You can read more about it [here](https://news.google.com/rss/articles/CBMibGh0dHBzOi8vYWJjbmV3cy5nby5jb20vSW50ZXJuYXRpb25hbC93aXJlU3RvcnkvaHVycmljYW5lLW5vcm1hLXRha2VzLWFpbS1tZXhpY29zLWxvcy1jYWJvcy1yZXNvcnRzLTEwNDE5MTAwNNIBcGh0dHBzOi8vYWJjbmV3cy5nby5jb20vYW1wL0ludGVybmF0aW9uYWwvd2lyZVN0b3J5L2h1cnJpY2FuZS1ub3JtYS10YWtlcy1haW0tbWV4aWNvcy1sb3MtY2Fib3MtcmVzb3J0cy0xMDQxOTEwMDQ?oc=5).

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
