# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690149933)

Prompt: Black man who says he was elected mayor of Alabama town alleges that White leaders are keeping him from position

[Read more](https://www.cbsnews.com/news/patrick-braxton-black-man-says-he-was-elected-mayor-of-newburn-alabama/)