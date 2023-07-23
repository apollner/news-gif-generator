# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif)

Prompt: Spanish general election tipped to put the far right back in office for the first time since Franco

[Read more](https://apnews.com/article/spain-election-what-to-know-a9aff5b0b50863b5f512a4b8dd24a1d1)