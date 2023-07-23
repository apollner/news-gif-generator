# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690128475)

Prompt: Here’s The List Of Promised ‘Diablo 4’ Changes Blizzard Says Are Coming

[Read more](https://www.forbes.com/sites/paultassi/2023/07/22/heres-the-list-of-promised-diablo-4-changes-blizzard-says-are-coming/)