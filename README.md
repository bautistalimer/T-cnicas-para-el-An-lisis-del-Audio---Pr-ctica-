# 🎵 Técnicas para el Análisis del Audio

Este proyecto contiene herramientas de **Procesamiento Digital de Señales (DSP)** en Python orientadas al análisis, conversión, modificación de tasa de muestreo/cuantización y visualización temporal de señales sonoras.

---

## 📌 Descripción del Proyecto

El código implementa técnicas fundamentales para la manipulación e inspección de audio digital en formato WAV (`PCM_S16LE` / `16 kHz`, Monocanal):

1. **Lectura y Vectorización**: Carga y conversión del archivo de audio a arreglos numéricos (`numpy.ndarray`).
2. **Cuantización y Reducción de Calidad**: Recuantización de la señal de 16-bits a **8-bits (`np.int8`)** para analizar el impacto del sesgo de cuantización y truncamiento de dinámica.
3. **Cálculo de Parámetros Físicos**: Cálculo de la duración total del audio en segundos en función de la frecuencia de muestreo ($f_s$).
4. **Visualización Dominio del Tiempo**: Gráficos de amplitud vs. número de muestras utilizando `matplotlib`.
5. **Reproducción Interactiva**: Métodos para reproducir señales modificadas en entornos interactivos (Jupyter / IPython).

---

## 🛠️ Requisitos e Instalación

Asegúrate de contar con Python 3.8+ instalado. Puedes instalar las dependencias necesarias mediante `pip`:

```bash
pip install soundfile matplotlib numpy ipython
```

---

## 📁 Archivos del Repositorio

* `técnicas_para_el_Análisis_del_Audio.py`: Script principal de procesamiento y graficación de señales.
* `AnalisisTextos_convertido.wav`: Archivo de audio monocanal a 16 kHz utilizado como entrada de muestra.
* `técnicas_para_el_Análisis_del_Audio.pdf`: Reporte técnico con capturas e inspección del audio mediante MediaInfo y gráficos de salida.

---

## ⚙️ Especificaciones de la Señal de Audio

Basado en las propiedades del archivo `AnalisisTextos_convertido.wav`:

| Parámetro | Valor |
| :--- | :--- |
| **Formato de Contenedor** | Waveform Audio (`.wav`) |
| **Códec / Formato** | PCM (`PCM_S16LE`) |
| **Frecuencia de Muestreo ($f_s$)** | $16\,000\text{ Hz}$ (16 kHz) |
| **Canales** | 1 (Monocanal / Mono) |
| **Profundidad de Bits Original** | 16 bits |
| **Tasa de Bits (Bitrate)** | 256 kbps |

---

## 🚀 Uso del Código

Ejecuta el script directamente desde la consola:

```bash
python técnicas_para_el_Análisis_del_Audio.py
```

### Fragmento Principal del Código

```python
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio

# 1. Carga de audio
archivo = 'AnalisisTextos_convertido.wav'
audio, sr = sf.read(archivo)

# 2. Información del vector
print("Cantidad de elementos (Muestras):", len(audio))
duracion = len(audio) / sr
print("Duración en segundos:", duracion)

# 3. Reducción de resolución a 8 bits
audio_baja_calidad = (audio * (2**3)).astype(np.int8)

# 4. Graficación temporal
plt.figure(figsize=(10, 4))
plt.plot(audio_baja_calidad)
plt.title("Visualización de la Señal Sonora")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()
```

---

## 📊 Visualizaciones e Interpretación

Al reducir la profundidad a 8 bits (`int8`), la señal sufre un fenómeno de **saturación y cuantización**, produciendo una señal recortada en amplitud ($[-128, 127]$):

```text
               Visualización de la Señal Sonora
   Amplitud
     1.00 ┤        │          │   │
     0.50 ┤        │          │   │
     0.00 ┼────────┴──────────┴───┴───────
    -0.50 ┤        │          │   │
    -1.00 ┤        │          │   │
          └────────┴──────────┴───┴───────> Muestras
          0      20000      60000    100000
```
