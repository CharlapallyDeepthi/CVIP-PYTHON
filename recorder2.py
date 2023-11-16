import pyaudio
import wave
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class AudioRecorderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Recorder")

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

        self.p = pyaudio.PyAudio()
        self.frames = []
        self.stream = None  # Initialize the stream variable
        self.recordings = []  # List to store recording filenames

        # Load previous recordings from file
        self.load_recordings()

        self.record_button = ttk.Button(self.master, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = ttk.Button(self.master, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack(pady=10)

        self.show_recordings_button = ttk.Button(self.master, text="Show Recordings", command=self.show_recordings)
        self.show_recordings_button.pack(pady=10)

    def start_recording(self):
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)
        print("Recording started...")
        self.frames = []  # Clear any previous frames

        # Start the update loop
        self.master.after(1, self.update)

    def stop_recording(self):
        if self.stream and self.stream.is_active():
            print("Recording stopped.")
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

            # Save the recorded audio to a WAV file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.wav"
            wf = wave.open(filename, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()

            self.recordings.append(filename)  # Add the filename to the list

            # Save the recordings list to file
            self.save_recordings()

        else:
            print("No active stream to stop.")

    def update(self):
        # Continue reading frames while recording
        if self.stream and self.stream.is_active():
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)
            self.master.after(1, self.update)
        else:
            print("Recording stopped or no active stream.")

    def show_recordings(self):
        if self.recordings:
            print("Previous Recordings:")
            for recording in self.recordings:
                print(recording)
        else:
            print("No previous recordings.")

    def save_recordings(self):
        with open("recordings.txt", "w") as file:
            for recording in self.recordings:
                file.write(recording + "\n")

    def load_recordings(self):
        try:
            with open("recordings.txt", "r") as file:
                self.recordings = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("No previous recordings file found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorderGUI(root)
    root.geometry("300x200")
    root.protocol("WM_DELETE_WINDOW", app.stop_recording)  # Stop recording when the window is closed
    root.mainloop()
