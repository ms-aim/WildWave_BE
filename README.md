# WildWave
🐦 BirdNet API: AI-Powered Species IdentificationAn automated backend service that identifies bird species from audio recordings. This project leverages the BirdNet-Analyzer (developed by Cornell Lab of Ornithology) to provide high-confidence species detection based on geographic location.⚙️ How it WorksThe API follows a specific pipeline to ensure accurate detection:Audio Normalization: Converts uploaded files to the required 48kHz Mono WAV format using pydub.Geospatial Filtering: Uses Nashik coordinates ($19.9975^\circ N, 73.7898^\circ E$) to narrow down species likely to be found in the region.AI Inference: Processes the audio through the BirdNet model to detect common names and confidence scores.🛠 Tech StackFramework: FastAPI (Python 3.11)AI Engine: BirdNet-Analyzer / TensorFlow LiteAudio Processing: Pydub (FFmpeg)Documentation: Swagger UI (/docs)

📦 Installation & Setup
Install FFmpeg (Required for audio processing):

Bash
# On Windows using Chocolatey
choco install ffmpeg
Install Python Dependencies:

Bash
pip install fastapi uvicorn birdnetlib pydub
Run the Server:

Bash
uvicorn uniquebirds:app --reload

Bash
Install the CPU version of TensorFlow (most compatible for Windows 3.11)
pip install tensorflow-cpu==2.15.0

🧪 Testing the API
Open http://127.0.0.1:8000/docs.

Find the /detect-birds/ POST endpoint.

Click "Try it out" and upload a .wav or .mp3 file of bird sounds.

View the JSON response containing the bird names and confidence percentages.
