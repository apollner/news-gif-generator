# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690135691)

Prompt: Box Office: ‘Barbie’ Breaks Ground With Biggest Opening Day of 2023, ‘Oppenheimer’ Dolling Up to $77 Million Debut

[Read more](https://variety.com/2023/film/box-office/box-office-barbie-oppenheimer-opening-day-projections-1235676681/)