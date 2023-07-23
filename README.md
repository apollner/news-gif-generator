# News GIF Generation
This repository contains a script that generates an GIF based on a news headline. The GIF is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the GIF is generated using the DiffusionPipeline from the `diffusers` Python package. The GIF generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new GIF each time.

---

![Generated GIF](output.gif?raw=true&v=1690124821)

Prompt: British Open: Follow Brian Harman, Tommy Fleetwood, Sepp Straka and others Saturday at Royal Liverpool

[Read more](https://sports.yahoo.com/british-open-follow-brian-harman-tommy-fleetwood-sepp-straka-and-others-saturday-at-royal-liverpool-064506047.html)