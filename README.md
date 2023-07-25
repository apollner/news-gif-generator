# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690254534)

Prompt: The Open 2023 - Brian Harman's victory was decades in the making - ESPN

[Read more](https://www.espn.com/golf/story/_/id/38058715/2023-open-brian-harman-win-royal-liverpool-georgia-bulldogs)