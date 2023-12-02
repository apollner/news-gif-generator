# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1701506021)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Piers Morgan Says Kate Middleton, King Charles Named for Alleged Skin Color Comments to Harry, Meghan - E! Online**

You can read more about it [here](https://www.eonline.com/news/1390683/piers-morgan-says-kate-middleton-king-charles-named-for-alleged-skin-color-comments-to-harry-meghan).

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
