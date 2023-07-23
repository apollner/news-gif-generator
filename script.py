import os
import time
import random
import requests
import json

# Install necessary packages
os.system('pip install diffusers --upgrade')
os.system('pip install invisible_watermark transformers accelerate safetensors')
os.system('pip install moviepy')

# Import necessary packages after installation
from huggingface_hub import login
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
from moviepy.editor import VideoFileClip

# Initialize the DiffusionPipeline
pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=api_key"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    
    # Select a random article
    article = random.choice(articles)

    # Get the article title and remove the newspaper name
    prompt = article["title"].rsplit(" - ", 1)[0]

    # Get the URL of the article
    article_url = article["url"]
    video_frames = pipe(prompt, num_inference_steps=25).frames
    video_path = export_to_video(video_frames)
    clip = (VideoFileClip(video_path))
    clip_resized = clip.resize(height=800)
    clip_resized.write_gif('output.gif')

    # Update the README file
    version = int(time.time())  # Use the current timestamp as the version
    with open('README.md', 'w') as f:
        f.write("# News GIF Generation\n")
        f.write("This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.\n")
        f.write("The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.\n")
        f.write("The script runs every few minutes, fetching a new headline and generating a new GIF each time.\n")
        f.write("\n---\n\n")
        f.write(f'![Generated GIF](output.gif?raw=true&v={version})\n\nPrompt: {prompt}\n\n[Read more]({article_url})')

get_news()
