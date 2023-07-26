# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1690405585)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Miami-Dade Police Director Freddy Ramirez recovering from gunshot wound, expected to undergo another surgery**

You can read more about it [here](https://www.local10.com/news/local/2023/07/25/miami-dade-police-director-freddy-ramirez-recovering-from-gunshot-wound-expected-to-remain-in-tampa-hospital-all-week/).

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
