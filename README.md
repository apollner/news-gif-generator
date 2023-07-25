# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690293968)

Prompt: House Republicans' CHOICE Act would roll back some Obamacare protections

[Read more](https://www.npr.org/sections/health-shots/2023/07/24/1189332308/house-republicans-choice-act-roll-back-obamacare-protections)