# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1696388917)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Blazers reveal unexpected plan for Malcolm Brogdon after Celtics trade**

You can read more about it [here](https://news.google.com/rss/articles/CBMidGh0dHBzOi8vd3d3Lm1hc3NsaXZlLmNvbS9jZWx0aWNzLzIwMjMvMTAvYmxhemVycy1yZXZlYWwtdW5leHBlY3RlZC1wbGFuLWZvci1tYWxjb2xtLWJyb2dkb24tYWZ0ZXItY2VsdGljcy10cmFkZS5odG1s0gGDAWh0dHBzOi8vd3d3Lm1hc3NsaXZlLmNvbS9jZWx0aWNzLzIwMjMvMTAvYmxhemVycy1yZXZlYWwtdW5leHBlY3RlZC1wbGFuLWZvci1tYWxjb2xtLWJyb2dkb24tYWZ0ZXItY2VsdGljcy10cmFkZS5odG1sP291dHB1dFR5cGU9YW1w?oc=5).

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
