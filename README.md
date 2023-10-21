# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1697907892)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Who won ALCS Game 4? Houston scores 10 runs from Jose Abreu, Chas McCormick home runs to even series with Texas Rangers**

You can read more about it [here](https://abc13.com/houston-astros-lineup-today-texas-rangers-roof-open-jose-urquidy-andrew-heaney/13940759/).

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
