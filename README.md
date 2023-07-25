# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690266978)

Prompt: 'SpongeBob' Voice Actor's Wife Clarifies He is Not Dating Ariana Grande Amid Ethan Slater Romance

[Read more](https://www.etonline.com/spongebob-voice-actors-wife-clarifies-he-is-not-dating-ariana-grande-amid-ethan-slater-romance)