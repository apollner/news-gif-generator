# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1690355154)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Doja Cat Slams Admirers Who Call Themselves ‘Kittenz’—And She’s Not The First Celebrity To Diss Her Fans**

You can read more about it [here](https://www.forbes.com/sites/maryroeloffs/2023/07/24/doja-cat-slams-admirers-who-call-themselves-kittenz-and-shes-not-the-first-celebrity-to-diss-her-fans/).

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
