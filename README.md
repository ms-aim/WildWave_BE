# WildWave
🐦 BirdNet API: AI-Powered Species IdentificationAn automated backend service that identifies bird species from audio recordings. This project leverages the BirdNet-Analyzer (developed by Cornell Lab of Ornithology) to provide high-confidence species detection based on geographic location.⚙️ How it WorksThe API follows a specific pipeline to ensure accurate detection:Audio Normalization: Converts uploaded files to the required 48kHz Mono WAV format using pydub.Geospatial Filtering: Uses Nashik coordinates ($19.9975^\circ N, 73.7898^\circ E$) to narrow down species likely to be found in the region.AI Inference: Processes the audio through the BirdNet model to detect common names and confidence scores.🛠 Tech StackFramework: FastAPI (Python 3.11)AI Engine: BirdNet-Analyzer / TensorFlow LiteAudio Processing: Pydub (FFmpeg)Documentation: Swagger UI (/docs)

📦 Installation & Setup
# 1. Update pip to avoid installation conflicts
python -m pip install --upgrade pip

# 2. Install FastAPI and the Uvicorn server
pip install "fastapi[all]"

# 3. Install the BirdNet library
pip install birdnetlib

# 4. Install the Windows-compatible CPU version of TensorFlow
# (This satisfies the tflite_runtime requirement)
pip install tensorflow-cpu==2.15.0

# 5. Install Pydub for audio manipulation
pip install pydub

# 6. Instal lyibrosa
pip install librosa resampy

🧪 Testing the API
Open http://127.0.0.1:8000/docs.

Find the /detect-birds/ POST endpoint.

Click "Try it out" and upload a .wav or .mp3 file of bird sounds.

View the JSON response containing the bird names and confidence percentages.
