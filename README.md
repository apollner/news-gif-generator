# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690265521)

Prompt: China Box Office: ‘Barbie’ Opens in Fifth Place With $8 Million

[Read more](https://variety.com/2023/film/global/china-box-office-barbie-opens-fifth-1235678092/)