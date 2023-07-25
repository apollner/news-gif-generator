# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690253946)

Prompt: Benjamin Netanyahu in hospital as crisis erupts over Israel's judicial overhaul

[Read more](https://www.ft.com/content/39cabf17-d225-48c1-931b-ac5bf0d041d1)