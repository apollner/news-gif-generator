# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690105775)

Prompt: Kamala Harris takes pols' fight over Black history to Jacksonville

[Read more](https://www.jacksonville.com/story/news/politics/government/2023/07/21/kamala-harris-takes-floridas-fight-over-black-history-to-jacksonville/70443827007/)