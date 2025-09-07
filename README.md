# CloudBlast RPG Game

Un affascinante gioco RPG 2D platform basato su **pygame** che offre un'esperienza di gioco completa con combattimenti, magia, nemici intelligenti, effetti particellari e tutto ciò che ci si aspetta da un classico gioco RPG vintage.

## 📋 Descrizione del Progetto

CloudBlast è un gioco di ruolo bidimensionale che combina elementi platform con meccaniche RPG tradizionali. Il giocatore esplora un mondo ricco di nemici, raccoglie esperienza, migliora le proprie statistiche e utilizza diverse armi e magie per progredire nel gioco.

### ✨ Caratteristiche Principali

- **Sistema di combattimento**: 5 armi diverse (spada, lancia, ascia, rapier, sai) con statistiche uniche
- **Sistema magico**: Incantesimi di fuoco e guarigione
- **Nemici diversificati**: 4 tipi di nemici (squid, raccoon, spirit, bamboo) con comportamenti AI distinti
- **Sistema di progressione**: Guadagna esperienza e migliora le statistiche del personaggio
- **Effetti particellari**: Animazioni fluide e effetti visivi accattivanti
- **Audio immersivo**: Musica di sottofondo e effetti sonori
- **Mappa dettagliata**: Mondo basato su tilemap con diversi livelli di profondità

## 🔧 Requisiti di Sistema

### Prerequisiti Software
- **Python 3.7+** (testato con Python 3.12.3)
- **pygame** 2.0+
- Sistema operativo: Windows, macOS, o Linux

### Requisiti Hardware Minimi
- RAM: 512 MB
- Spazio su disco: 50 MB
- Scheda grafica: Compatibile con DirectX 9.0c o OpenGL 2.1

## 🚀 Installazione e Configurazione

### Opzione 1: Eseguibile Pre-compilato (Windows)
L'eseguibile `main.exe` è disponibile nella cartella `code/`:
```bash
cd code/
./main.exe  # Su Linux/macOS
# main.exe  # Su Windows
```

### Opzione 2: Esecuzione da Codice Sorgente

1. **Clona il repository**:
```bash
git clone https://github.com/GiorCocc/RPG-GAME.git
cd RPG-GAME
```

2. **Installa le dipendenze**:
```bash
pip install -r requirements.txt
# Oppure manualmente:
# pip install pygame
```

3. **Avvia il gioco**:
```bash
cd code/
python main.py
```

### Configurazione dell'Ambiente di Sviluppo

Per sviluppatori che vogliono modificare il gioco:

```bash
# Crea un ambiente virtuale (raccomandato)
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# Installa pygame
pip install pygame

# Per creare un nuovo eseguibile (opzionale)
pip install pyinstaller
pyinstaller --onefile main.py
```

## 🎮 Comandi di Gioco

| Comando              | Tasto                    | Descrizione                                                  |
| -------------------- | ------------------------ | ------------------------------------------------------------ |
| Movimento in alto    | `Freccia su`             | Muove il personaggio verso l'alto                           |
| Movimento in basso   | `Freccia giù`            | Muove il personaggio verso il basso                         |
| Movimento a destra   | `Freccia destra`         | Muove il personaggio verso destra                           |
| Movimento a sinistra | `Freccia sinistra`       | Muove il personaggio verso sinistra                         |
| Attacco              | `Spazio`                 | Attacco verso il nemico o i cespugli con l'arma selezionata |
| Magia                | `CTRL sinistra`          | Lancia un incantesimo con la magia selezionata              |
| Cambio arma          | `Q`                      | Cicla tra: spada, lancia, ascia, rapier, sai                |
| Cambio magia         | `E`                      | Alterna tra: fuoco e guarigione                             |
| Menu upgrade         | `M`                      | Apre il menu per migliorare le statistiche con i punti XP   |
| Navigazione menu     | `Frecce destra-sinistra` | Naviga tra le opzioni del menu                              |
| Conferma menu        | `Spazio`                 | Conferma la selezione nel menu upgrade                      |

## 📁 Struttura del Progetto

```
RPG-GAME/
├── code/                    # Codice sorgente principale
│   ├── main.py             # File principale del gioco
│   ├── player.py           # Logica del giocatore
│   ├── enemy.py            # Sistema dei nemici
│   ├── level.py            # Gestione dei livelli
│   ├── weapon.py           # Sistema delle armi
│   ├── magic.py            # Sistema magico
│   ├── ui.py               # Interfaccia utente
│   ├── settings.py         # Configurazioni del gioco
│   ├── particles.py        # Effetti particellari
│   ├── upgrade.py          # Sistema di miglioramento
│   ├── support.py          # Funzioni di supporto
│   ├── entity.py           # Classe base per entità
│   ├── tile.py             # Sistema di tilemap
│   ├── debug.py            # Strumenti di debug
│   └── main.exe            # Eseguibile Windows
├── graphics/               # Asset grafici
│   ├── player/             # Sprite del giocatore
│   ├── monsters/           # Sprite dei nemici
│   ├── weapons/            # Sprite delle armi
│   ├── particles/          # Effetti visivi
│   ├── objects/            # Oggetti del mondo
│   ├── tilemap/            # Tile per la mappa
│   └── font/               # Font personalizzati
├── audio/                  # File audio
│   ├── main.ogg            # Musica di sottofondo
│   ├── attack/             # Suoni di attacco
│   └── *.wav               # Vari effetti sonori
├── map/                    # Dati della mappa
│   └── *.csv               # File CSV per i livelli
└── README.md               # Questo file
```

## 🎯 Elementi di Gioco

### Armi Disponibili
- **Spada**: Bilanciata, danni medi, velocità media
- **Lancia**: Alto danno, velocità lenta
- **Ascia**: Danni elevati, velocità moderata
- **Rapier**: Basso danno, velocità molto alta
- **Sai**: Danni moderati, velocità alta

### Sistema Magico
- **Fiamma**: Incantesimo offensivo che infligge danni da fuoco
- **Guarigione**: Ripristina i punti vita del giocatore

### Nemici
- **Squid**: Nemico acquatico con attacco a taglio
- **Raccoon**: Nemico resistente con attacco ad artiglio
- **Spirit**: Nemico veloce con attacco fulmine
- **Bamboo**: Nemico agile con attacco foglia

## 🛠️ Sviluppo Futuro

- Nuovi mondi e livelli
- Meccaniche di gioco aggiuntive
- Sistema di inventario espanso
- Multiplayer locale
- Nuovi tipi di nemici e boss
- Sistema di quest e missioni

## 🎨 Crediti e Asset

Le grafiche sono state gentilmente fornite da:
- **[Ninja Adventure - Asset Pack by pixel-boy](https://pixel-boy.itch.io/ninja-adventure-asset-pack)** - Disponibile in free-download

Tutti gli asset grafici sono utilizzati sotto licenza free-to-use per progetti personali e open source.

## 📄 Licenza

Questo progetto è distribuito sotto licenza open source. I diritti relativi agli asset grafici appartengono ai rispettivi autori (vedere sezione Crediti).

**Nota**: Gli asset grafici di Ninja Adventure sono utilizzati secondo i termini della loro licenza free-to-use. Per uso commerciale, consultare la licenza originale.

## 🤝 Contribuire

I contributi sono benvenuti! Per contribuire:

1. Fai un fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Committa i tuoi cambiamenti (`git commit -m 'Add some AmazingFeature'`)
4. Pusha sul branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📞 Contatti

Per domande, suggerimenti o segnalazioni di bug, apri una issue su GitHub.

---

**Buon divertimento con CloudBlast! 🎮**

