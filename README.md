# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699259754)

## Latest News Headline
The latest news headline used to generate the GIF is:

**Oklahoma State football vs. OU: Five takeaways from Cowboys' win over Sooners in Bedlam**

You can read more about it [here](https://www.oklahoman.com/story/sports/college/cowboys/2023/11/04/oklahoma-state-football-score-vs-ou-sooners-bedlam-big-12-game-takeaways-osu-cowboys/71420569007/).

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
