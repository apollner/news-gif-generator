# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690277631)

Prompt: The Open Championship payouts and points: Brian Harman wins first major championship - PGA TOUR

[Read more](https://www.pgatour.com/article/news/betting-dfs/2023/07/23/the-open-championship-payouts-and-points-brian-harman-royal-liverpool)