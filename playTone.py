import numpy as np
import pyaudio

def generate_tone(frequency, duration, sample_rate, amplitude=0.5):
    #generate sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal

def play_sound(signal, sample_rate):
    #play the audio
    p = pyaudio.PyAudio()
    
    #open stream
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    
    #convert signal to bytes and play
    stream.write(signal.astype(np.float32).tobytes())
    
    #close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

def main():
    #parameters
    sample_rate = 44100  #sample rate
    ultrasound_freq = 22000  #frequency in Hz 
    duration = 15 #Duration in seconds
    
    #generate tone
    ultrasound_signal = generate_tone(ultrasound_freq, duration, sample_rate)
    
    #play tone
    play_sound(ultrasound_signal, sample_rate)
    
    print("playing tone... ")

if __name__ == "__main__":
    main()