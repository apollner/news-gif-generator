# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690211280)

Prompt: Summer’s most spectacular meteor shower now underway, best dates for viewing

[Read more](https://www.mlive.com/news/2023/07/summers-most-spectacular-meteor-shower-now-underway-best-dates-for-viewing.html)