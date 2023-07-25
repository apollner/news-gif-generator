# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690276012)

Prompt: Indonesian boat capsizes, leaving more than a dozen dead and others missing

[Read more](https://www.npr.org/2023/07/24/1189714108/indonesian-boat-capsizes-leaving-more-than-a-dozen-dead-and-others-missing)