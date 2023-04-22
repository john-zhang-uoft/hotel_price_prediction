<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Hotel Price Prediction</h3>
  <p align="center">
    By Fernando Assad, John Zhang, and Nathan Henry
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Our Hotel Price Prediction project aims to predict the price of hotels given a listing. Our model takes as inputs images, text reviews and descriptions, ratings in many categories, location, and outputs a price prediction. The aim is to be able to use our model as a tool to quickly combine information found in the form of many reviews and numerical, and even image data to tell users what a hotel's price should be. This way, they can discern whether a hotel is overpriced, priced fairly, or a good deal. We trained our model with supervised learning, using a tuned pretrained text transformers on the text data, a tuned pretrained CNN on image data, and fed all of the embeddings of these networks into a fully connected network, along with numerical data.

In addition to the price prediction model, we explored training a causal model to learn the latent variable "quality", which is the instrinsic value of a hotel detached from everything else. We explored using an autoencoder-like architecture, and analyzed different approaches of solving the problem of extracting a latent quality variable which is not directly expressed by any of the features in the data found on hotel listings.


Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tools and Technologies

* [![PyTorch][pytorch]](https://pytorch.org/)
* [![Transformers][huggingface]](https://huggingface.co/docs/transformers/index)
* [![Apify][apify.com]](https://apify.com/)
* [![scikit-learn][scikit-learn]](https://scikit-learn.org/stable)
* [![pandas][pandas]](https://pandas.pydata.org/)
* [![NumPy][numpy]](https://numpy.org/)
* [![matplotlib][matplotlib]](https://matplotlib.org/)
* [![seaborn][seaborn]](https://seaborn.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Required packages
* pip
  ```sh
  pip install torch torchvision torchaudio transformers datasets pandas numpy matplotlib seaborn scikit-learn
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/john-zhang-uoft/hotel_price_prediction
   ```
2. Install python packages
   ```sh
   pip install torch torchvision torchaudio transformers datasets pandas numpy matplotlib seaborn scikit-learn
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

[causal_model.ipynb](https://github.com/john-zhang-uoft/hotel_price_prediction/blob/main/src/causal_model.ipynb) is the training for the quality encoding model.

[multi-modal_network.ipynb](https://github.com/john-zhang-uoft/hotel_price_prediction/blob/main/src/multi-modal_network.ipynb) is the training of the final price prediction multi-modal network.

[extract_json.ipynb](https://github.com/john-zhang-uoft/hotel_price_prediction/blob/main/src/extract_json.ipynb) contains unpacking the json data.

[final_dataset.ipynb](https://github.com/john-zhang-uoft/hotel_price_prediction/blob/main/src/final_dataset.ipynb) contains the construction of the final dataset after filtering images.

[image_heuristics.ipynb](https://github.com/john-zhang-uoft/hotel_price_prediction/blob/main/src/image_heuristics.ipynb) contains the calculation for different predictive heuristics we used for images to simplify the task of regressing on images.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

We would like to thank professor Michael Guerzhoy and our TA Parsa Farinneya for their excellent teaching and help this semester.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



