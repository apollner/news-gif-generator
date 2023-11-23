# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1700724824)

## Latest News Headline
The latest news headline used to generate the GIF is:

**IDF breaches blast door in Hamas tunnel under Gaza’s Shifa Hospital**

You can read more about it [here](https://news.google.com/rss/articles/CBMiYWh0dHBzOi8vd3d3LnRpbWVzb2Zpc3JhZWwuY29tL2lkZi1icmVhY2hlcy1ibGFzdC1kb29yLWluLWhhbWFzLXR1bm5lbC11bmRlci1nYXphcy1zaGlmYS1ob3NwaXRhbC_SAWVodHRwczovL3d3dy50aW1lc29maXNyYWVsLmNvbS9pZGYtYnJlYWNoZXMtYmxhc3QtZG9vci1pbi1oYW1hcy10dW5uZWwtdW5kZXItZ2F6YXMtc2hpZmEtaG9zcGl0YWwvYW1wLw?oc=5).

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
