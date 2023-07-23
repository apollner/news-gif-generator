# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690130179)

Prompt: 2023 British Open leaderboard: Live coverage, Rory McIlroy score, golf scores today, how to watch Round 3

[Read more](https://www.cbssports.com/golf/news/2023-british-open-leaderboard-live-coverage-rory-mcilroy-score-golf-scores-today-how-to-watch-round-3/live/)