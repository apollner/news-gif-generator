# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690216658)

Prompt: 25 people hospitalized after deck collapses at Billings, Montana, country club

[Read more](https://www.usatoday.com/story/news/nation/2023/07/23/billings-montana-deck-collapse/70452869007/)