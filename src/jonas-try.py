import numpy as np

def konfidenz(dateiname, gamma):
    # 1. Daten einlesen      
    A = np.loadtxt(dateiname)  # Lädt die Daten aus der Datei 'Daten_TV.txt'
     
    # 2. Berechnung des Mittelwerts
    n = len(A)  # Anzahl der Datenpunkte
    mittelwert = np.sum(A) / n
    mu = mittelwert  # Mittelwert zur Rückgabe 
    print(f"Mittelwert (mu): {mu}")
    
    # 3. Berechnung der Varianz
    varianz = np.sum((A - mittelwert) ** 2) / (n - 1)  # erwartungstreue Varianz
    print(f"Varianz (sigma^2): {varianz}")
    
    # 4. Numerische Integration mit der Trapezregel (berechne Konstante c)
    flaeche = 0.5
    start = 0
    ende = 0.001  # Schrittweite
    gesucht = (gamma + 1) / 2  # Zielwert
    
    # Funktion für die Standardnormalverteilung
    def standardnormalverteilung(x):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x ** 2)
    
    # Trapezregel zur Berechnung des Integrals der Standardnormalverteilung
    while flaeche < gesucht:
        flaeche += (ende - start) / 2 * (standardnormalverteilung(start) + standardnormalverteilung(ende))
        start += 0.001
        ende += 0.001
    
    c = start  # das gesuchte c
    print(f"Konstante c (aus der Trapezregel): {c}")

    # 5. Berechnung des Konfidenzintervalls
    oben = mu + c * np.sqrt(varianz / n)
    unten = mu - c * np.sqrt(varianz / n)
    
    return mu, oben, unten, varianz, c

# Testaufruf der Funktion
mu, oben, unten, varianz, c = konfidenz('Daten_TV.txt', 0.99)
print(f"Konfidenzintervall: ({unten}, {oben})")
