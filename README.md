# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699693565)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Caitlin Clark guides No. 3 Iowa women's basketball to tough win over No. 5 Virginia Tech**

You can read more about it [here](https://www.hawkcentral.com/story/sports/college/iowa/basketball-women/2023/11/09/iowa-womens-basketball-holds-off-virginia-tech-behind-caitlin-clarks/71518548007/).

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
