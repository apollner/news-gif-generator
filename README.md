# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690168130)

Prompt: Hall of Fame classmates Fred McGriff, Scott Rolen becoming friends forever in Cooperstown

[Read more](https://www.usatoday.com/story/sports/mlb/columnist/bob-nightengale/2023/07/22/baseball-hall-of-fame-2023-fred-mcgriff-scott-rolen/70451784007/)