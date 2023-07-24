# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690198434)

Prompt: Formula 1 picks, odds, race time: 2023 Hungarian Grand Prix predictions, F1 best bets from proven model

[Read more](https://www.cbssports.com/motor-sports/news/formula-1-picks-odds-race-time-2023-hungarian-grand-prix-predictions-f1-best-bets-from-proven-model/)