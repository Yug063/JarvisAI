import subprocess
import sys

# Install the required library if not already installed
required_package = "google-generativeai"

try:
    import google.generativeai as genai
except ImportError:
    print(f"Installing {required_package} library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", required_package])
    print("Installation complete.")
    import google.generativeai as genai

# Replace 'YOUR_API_KEY' with your actual Gemini API key
your_api_key = "YOUR_API_KEY"

# Configure the API key
genai.configure(api_key=your_api_key)

# Define the question prompt
question = "Write an email to my boss for resignation?"

# Create a generative model (choose 'gemini-pro' for best results)
model = genai.GenerativeModel("gemini-pro")

# Generate the answer
response = model.generate_content(question)

# Print the answer
print(response.text)
