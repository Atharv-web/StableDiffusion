# Stable Diffusion Text-to-Image Generator

This project demonstrates the use of a Stable Diffusion model to generate images from text prompts. The implementation leverages TensorFlow and Keras with the `keras_cv` library for easy access to pre-trained diffusion models. Try this out to generate cool images with your prompts. Be creative!!

## Features
- Generates high-quality images from user-provided text prompts.
- Displays multiple generated images side by side for comparison.
- Customizable image dimensions and batch size.

## Requirements
### Prerequisites
Ensure you have Python 3.8 or higher installed.

### Required Libraries
Install the following libraries before running the script:

```bash
pip install tensorflow keras-cv matplotlib pillow
```

## Usage

1. **Clone the Repository**
   Clone the repository to your local machine or copy the script into your project folder.

2. **Run the Script**
   Execute the script with the following command:
   
   ```bash
   python aiart.py
   ```

3. **Enter the Text Prompt**
   When prompted, input the text description for the desired image. The model will generate three images based on your input.

4. **View the Results**
   The generated images will be displayed in a grid. Each image is generated with slight variations to provide a diverse output for the same prompt.

## Code Overview
### Key Components

1. **Stable Diffusion Model**
   The Stable Diffusion model is loaded using the `keras_cv.models.StableDiffusion` function. Image dimensions are set to 512x512 pixels, which is optimal for most tasks.

2. **Text-to-Image Generation**
   The `text_to_image` method of the model takes the input prompt and generates a batch of images.

3. **Image Plotting**
   The `plot_images` function uses Matplotlib to display the generated images side by side.

## Notes
- Ensure your system has sufficient GPU resources for optimal performance. Running Stable Diffusion on a CPU can be significantly slower.
- Image quality and variety may depend on the prompt; detailed prompts often produce better results.
