# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1700338053)

## Latest News Headline
The latest news headline used to generate the GIF is:

**NFL to investigate Bengals over Joe Burrow injury: League set to look into whether team violated NFL policy**

You can read more about it [here](https://www.cbssports.com/nfl/news/nfl-to-investigate-bengals-over-joe-burrow-injury-league-set-to-look-into-whether-team-violated-nfl-policy/).

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
