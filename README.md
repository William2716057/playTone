# Ultrasound Tone Generator
This project demonstrates how to generate and play a simple sine wave tone using Python. The script utilizes the numpy library to generate the sine wave and the pyaudio library to play the audio.

## Features
- Generate a sine wave tone at a specified frequency and duration.
- Play the generated tone using your computer's audio output.

##Requirements
- Python 3.x
- numpy library
- pyaudio library

## Installation
1. Clone the repository:
```
https://github.com/William2716057/playTone.git
```
2. Adjust parameters:
- sample_rate: The sample rate of the audio (default: 44100 Hz).
- ultrasound_freq: The frequency of the generated tone in Hz (default: 22000 Hz).
- duration: The duration of the tone in seconds (default: 15 seconds).

The script will generate a sine wave tone with the specified parameters and play it through the audio output.

## Code Explanation

### generate_tone function

This function generates a sine wave signal.

```
def generate_tone(frequency, duration, sample_rate, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal
```

### play_sound function
This function plays the generated sine wave signal using the pyaudio library.

```
def play_sound(signal, sample_rate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    stream.write(signal.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
```

### main function
The main function sets the parameters, generates the tone, and plays it.
```
def main():
    sample_rate = 44100
    ultrasound_freq = 22000
    duration = 15
    
    ultrasound_signal = generate_tone(ultrasound_freq, duration, sample_rate)
    play_sound(ultrasound_signal, sample_rate)
    
    print("playing tone... ")
```

### Contributing
Contributions are welcome. Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.
