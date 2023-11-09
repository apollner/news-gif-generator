# News GIF Generation
This repository contains a Python script that automatically generates a GIF based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates a GIF using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Video task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new GIF, which is then displayed below. The GIF generation process is performed on a GPU.

## Generated GIF
Below is the latest generated GIF:
![Generated GIF](output.gif?raw=true&v=1699558483)

## Latest News Headline
The latest news headline used to generate the GIF is:

**13 Years Before Landing ‘Zelda’ Movie, Director Wes Ball Called It the ‘Next Avatar-Like’ Film and Said He ‘Could Never Hope to Have the Chance to Direct It’**

You can read more about it [here](https://variety.com/2023/film/news/wes-ball-directing-zelda-movie-23-years-after-tweet-1235783773/).

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
