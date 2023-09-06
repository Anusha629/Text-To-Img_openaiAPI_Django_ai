from django.shortcuts import render

import openai
from PIL import Image

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define a function to generate an image
def generate_image(request):
    # Get the text input from the request
    text_input = request.GET.get('text_input')
    image_url = None

    # Check if text_input is not None
    if text_input is not None:
        # Check if there's a newline character in the text_input
        if '\n' in text_input:
            prompt = text_input
        else:
            # If there's no newline, check for additional features_input
            features_input = request.GET.get('features_input')
            if features_input is not None:
                # Combine text_input and features_input with a newline
                prompt = f"{text_input}\n{features_input}"
            else:
                # Use just the text_input
                prompt = text_input

        # Use OpenAI API to create an image
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='512x512',  # You can adjust the size as needed
        )

        # Get the image URL from the API response
        if 'data' in response and response['data']:
            image_url = response['data'][0]['url']

    # Create a context dictionary to pass the image URL to your HTML template
    context = {'image_url': image_url}

    # Render the HTML template with the context
    return render(request, 'index.html', context)


