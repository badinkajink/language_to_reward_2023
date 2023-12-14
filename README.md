# pHRI Class Project - Fall '23

## Installation and Usage (L2R-Go1)
```sh
# Grab, install, and update Miniconda: https://educe-ubc.github.io/conda.html
curl -sL \
    "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" > \
    "Miniconda3.sh"
bash Miniconda3.sh
conda update conda
conda install wget

# and create the l2r-go1 environment from the provided YAML
conda env create -f environment.yml
conda activate l2r-go1

# Build and install mujoco_mpc from the go1 fork
git clone https://github.com/badinkajink/mujoco_mpc.git
cd mujoco_mpc

# Compile mujoco_mpc from source and install, this step can take a few minutes.
pip install ./python

cd ..

# Build and install language_to_reward_2023
git clone https://github.com/badinkajink/language_to_reward_2023.git
cd language_to_reward_2023

# Compile language_to_reward_2023 from source and install, this step can take a few minutes.
pip install .

# Run the demo
python -m language_to_reward_2023.user_interaction --api_key=<Open AI API key>
```


## Results of Multi-Step Planning & Sentiment-Afforded Motions

<div style="text-align: center;">
    <p>"Walk excitedly"<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/orig_excitedly.gif.gif" alt="First GIF" width="200" height="200">
        <p>L2R</p>
    </div>
    <div style="text-align: center;">
        <img src="./gifs/excitedly.gif.gif" alt="Second GIF" width="200" height="200">
        <p>Our Work</p>
    </div>
</div>
