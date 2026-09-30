import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio

archivo = 'AnalisisTextos_convertido.wav'

audio, sr = sf.read(archivo)

print("Vector de la señal segmentada:")
print(audio)
print("Cantidad de elementos (Largo array):", len(audio))

audio_baja_calidad = (audio * (2**3)).astype(np.int8)

print("Reproduciendo señal con calidad reducida (8 bits):")
Audio(audio_baja_calidad, rate=sr)

duracion = len(audio) / sr
print("Duración en segundos:", duracion)

plt.figure(figsize=(10, 4))
plt.plot(audio_baja_calidad)
plt.title("Visualización de la Señal Sonora")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()



