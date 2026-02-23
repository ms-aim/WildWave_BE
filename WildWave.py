from fastapi import FastAPI, UploadFile, File
from birdnetlib.analyzer import Analyzer
from birdnetlib.main import Recording
from datetime import datetime
from pydub import AudioSegment
import os
import shutil

app = FastAPI()

def prepare_audio(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(48000).set_channels(1)
    audio.export(output_path, format="wav")

@app.post("/detect-birds/")
async def detect_birds(file: UploadFile = File(...)):
    input_path = f"temp_{file.filename}"
    processed_path = f"processed_{file.filename}.wav"
    
    # Correct way to save UploadFile in FastAPI
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        prepare_audio(input_path, processed_path)

        analyzer = Analyzer()
        # Ensure 'lon' and 'lat' are passed correctly for the specific library version
        recording = Recording(
            analyzer,
            processed_path,
            lat=19.9975,
            lon=73.7898,
            date=datetime.now(),
            min_conf=0.5
        )

        recording.analyze()

        unique_birds = {}
        for d in recording.detections:
            name = d['common_name']
            confidence = d['confidence']
            if name not in unique_birds or confidence > unique_birds[name]:
                unique_birds[name] = confidence

        return {
            "total_unique_birds": len(unique_birds),
            "birds": [
                {"name": bird, "confidence": round(conf * 100, 2)}
                for bird, conf in unique_birds.items()
            ]
        }

    finally:
        # Guaranteed cleanup in Python 3.11
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(processed_path):
            os.remove(processed_path)