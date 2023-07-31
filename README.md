# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1690772981)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Twitter rebrands to ‘X,’ hackers infect Call of Duty, and foreign visitors to China go cashless**

You can read more about it [here](https://techcrunch.com/2023/07/29/twitter-rebrands-to-x-hackers-infect-call-of-duty-and-foreign-visitors-to-china-go-cashless/).

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
