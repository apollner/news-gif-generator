# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif)

Prompt: Body of girl found in river believed to be that of 2-year-old lost in Pennsylvania flash flood

[Read more](https://apnews.com/article/bucks-county-flash-flood-missing-children-pennsyvlania-1add97718bfceb9c4034a4f26b08bf20)