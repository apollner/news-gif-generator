# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690212837)

Prompt: Should you buy the M2 MacBook Pro or wait for the M3?

[Read more](http://www.digitaltrends.com/computing/buy-m2-macbook-pro-or-wait-for-m3/)