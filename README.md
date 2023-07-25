# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690251361)

Prompt: ‘Biblical proportions’: 3 months’ worth of rainfall floods Nova Scotia, forcing evacuations as crews search for missing people

[Read more](https://www.cnn.com/2023/07/23/americas/nova-scotia-canada-rain-floods/index.html)