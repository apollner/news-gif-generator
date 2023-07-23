# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690144426)

Prompt: 2-year-old Nevada boy dies from brain-eating amoeba likely contracted at natural hot spring

[Read more](https://www.cnn.com/2023/07/22/us/nevada-brain-eating-amoeba/index.html)