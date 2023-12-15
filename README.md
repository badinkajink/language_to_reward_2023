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
    <p>"Patrol a museum."<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/museum_trimmed_10x_compressed.gif" alt="Dog Patrol Museum 10x Sped" width="200" height="200">
        <p>10x Speed Up</p>
    </div>
</div>

<div style="text-align: center;">
    <p>"Walk like you are preening at a dog show."<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/orig_preening.gif" alt="Preening -  Original" width="200" height="200">
        <p>L2R</p>
    </div>
    <div style="text-align: center;">
        <img src="./gifs/preening.gif" alt="Preening - Ours" width="200" height="200">
        <p>Our Work</p>
    </div>
</div>

<div style="text-align: center;">
    <p>"Back way like you are scared."<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/orig_scared.gif" alt="Scared -  Original" width="200" height="200">
        <p>L2R</p>
    </div>
    <div style="text-align: center;">
        <img src="./gifs/scared.gif" alt="SCared - Ours" width="200" height="200">
        <p>Our Work</p>
    </div>
</div>

<div style="text-align: center;">
    <p>"Walk excitedly"<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/orig_excitedly.gif" alt="Excied -  Original" width="200" height="200">
        <p>L2R</p>
    </div>
    <div style="text-align: center;">
        <img src="./gifs/excitedly.gif" alt="Excited - Ours" width="200" height="200">
        <p>Our Work</p>
    </div>
</div>

<div style="text-align: center;">
    <p>"Walk sadly."<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/orig_sadly.gif" alt="Sad -  Original" width="200" height="200">
        <p>L2R</p>
    </div>
    <div style="text-align: center;">
        <img src="./gifs/sadly.gif" alt="Sad - Ours" width="200" height="200">
        <p>Our Work</p>
    </div>
</div>

<div style="text-align: center;">
    <p>"Walk sternly."<p>
</div>
<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="./gifs/orig_sternly.gif" alt="Sternly -  Original" width="200" height="200">
        <p>L2R</p>
    </div>
    <div style="text-align: center;">
        <img src="./gifs/sternly.gif" alt="Sternly - Ours" width="200" height="200">
        <p>Our Work</p>
    </div>
</div>


