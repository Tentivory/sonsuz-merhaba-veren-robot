#!/usr/bin/env python3
# Sonsuz Merhaba Veren Robot
# Bu program gerçekten çalışır. Sonsuza kadar merhaba der.
# Dikkat: CTRL+C ile durdurun, yoksa sonsuza kadar gider.

import time
import random

def merhaba_de():
    ekler = [
        " ve dünya güzeldir!",
        " ama kimse dinlemiyor.",
        " çünkü öyle gerekiyor.",
        " (bu arada çay demlendi mi?)",
        " ve asla durmayacağım.",
        " - gizli not: aslında her şey planlı."
    ]
    sayac = 0
    while True:
        ek = random.choice(ekler)
        print(f"Merhaba dünya! #{sayac}{ek}")
        sayac += 1
        time.sleep(0.5)  # Çok hızlı olmasın diye, yoksa bilgisayar ağlar

if __name__ == "__main__":
    print("Robot başlatıldı. Merhaba demeye başlıyor...")
    print("Durdurmak için CTRL+C. Yoksa sonsuza kadar devam eder.")
    try:
        merhaba_de()
    except KeyboardInterrupt:
        print("\nRobot durduruldu. Ama o içten içe hala merhaba diyor...")

# İmza: Grok the Absürt Kayyum
# Tarih: 06.11.2026
# Damga: [ONAYLANDI - ABSÜRT DEPARTMANI]