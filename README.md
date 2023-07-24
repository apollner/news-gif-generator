# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690159000)

Prompt: Judge declares mistrial in YNW Melly double murder case

[Read more](https://www.nbcmiami.com/news/local/judge-declares-mistrial-in-ynw-melly-double-murder-case/3076540/)