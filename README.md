# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1693044363)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Upset Over Divorce, Ex-US Cop Opens Fire At Wife, Others At Bar, Kills 3**

You can read more about it [here](https://news.google.com/rss/articles/CBMibWh0dHBzOi8vd3d3Lm5kdHYuY29tL3dvcmxkLW5ld3MvdXBzZXQtb3Zlci1kaXZvcmNlLWV4LXVzLWNvcC1vcGVucy1maXJlLWF0LXdpZmUtb3RoZXJzLWF0LWJhci1raWxscy0zLTQzMjc3MTfSAXNodHRwczovL3d3dy5uZHR2LmNvbS93b3JsZC1uZXdzL3Vwc2V0LW92ZXItZGl2b3JjZS1leC11cy1jb3Atb3BlbnMtZmlyZS1hdC13aWZlLW90aGVycy1hdC1iYXIta2lsbHMtMy00MzI3NzE3L2FtcC8x?oc=5).

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
