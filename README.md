# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1700089671)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Israel shows alleged Hamas ‘armory’ under children’s hospital in Gaza. Local health officials dismiss the claims**

You can read more about it [here](https://news.google.com/rss/articles/CBMicGh0dHBzOi8vd3d3LmNubi5jb20vMjAyMy8xMS8xNC9taWRkbGVlYXN0L2lzcmFlbC1hbGxlZ2VzLWhhbWFzLWFybW9yeS11bmRlci1ob3NwaXRhbC1pbi1nYXphLWhuay1pbnRsL2luZGV4Lmh0bWzSAXRodHRwczovL2FtcC5jbm4uY29tL2Nubi8yMDIzLzExLzE0L21pZGRsZWVhc3QvaXNyYWVsLWFsbGVnZXMtaGFtYXMtYXJtb3J5LXVuZGVyLWhvc3BpdGFsLWluLWdhemEtaG5rLWludGwvaW5kZXguaHRtbA?oc=5).

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
