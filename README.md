**Choose your language / Wybierz język**

[EN](#english) / [PL](#polski)

#### English

# Graph Coloring App - Python Tkinter

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)
6. [Authors](#authors)

## Description

The TKinter Graph Coloring App is a Python application that uses the TKinter library to provide a graphical user interface (GUI) for graph coloring. This app allows users to create graphs and apply coloring algorithms to them. It is a useful tool for visualizing graph theory concepts and for educational purposes. [!!!App runs only in polish language!!!]

## Features

- Create and visualize graphs
- Apply graph coloring algorithms
- Interactive GUI using TKinter
- Save and load graphs

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/PiotrGren/TKinter-Graph-Coloring-App.git
   ```
2. Navigate to the project directory:
   ```sh
   cd TKinter-Graph-Coloring-App
   ```
3. Project is ready to use.

#### Alternative

As an alternative, there is an installation file GraphColoring_setup.exe in the Installer folder. The file will launch the installer, which atuomatically installs the application already in .exe format and creates a shortcut to it on the desktop. All you have to do is run it and install the application, then run the application.

```sh
Installer/GraphColoring_setup.exe
```

## Usage

To start the application, run the following command:

```sh
python Graph_Coloring.py
```

If you didn't choose to install the application by running **GraphColoring_setup.exe** you can create your own .exe file app after downloading this repository.
To run this process on your local machine, follow these steps:

1. Install pyinstaller:
   ```sh
   pip install pyinstaller
   ```

2. Create a destination folder for .exe file (optional)
   ```sh
   mkdir -p path/to/your/destination/folder
   ```
   
3. Navigate to the folder where the project was downloaded:
   ```sh
   cd path/to/your/project/folder
   ```

4. Run this code:
   ```sh
   pyinstaller --onefile --windowed --icon=icon.png --distpath path/to/your/destination/folder Graph_Coloring.py
   ```
   or (if you want to create .exe file in the same folder as your project):
   ```sh
   pyinstaller --onefile --icon=icon.png Graph_Coloring.py
   ```
After completing these steps, an executable [.exe] file will appear in the specified destination folder which launches the application.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Authors

Piotr Greń - Main developer - https://github.com/PiotrGren

### Co-authors

- Gabriela Kiwacka - Co-developer of an algorithm for graph coloring


#### Polski

# Aplikacja do kolorowania grafów - Python Tkinter

## Table of Contents

1. [Opis](#opis)
2. [Funkcje](#funkcje)
3. [Instalacja](#instalacja)
4. [Użycie](#użycie)
5. [Licencja](#licencja)
6. [Autorzy](#autorzy)

## Opis

TKinter Graph Coloring App to aplikacja w języku Python, która wykorzystuje bibliotekę TKinter do zapewnienia graficznego interfejsu użytkownika (GUI) do kolorowania grafów. Aplikacja umożliwia tworzenie grafów i stosowanie do nich algorytmów kolorowania. Jest to przydatne narzędzie do wizualizacji koncepcji teorii grafów i celów edukacyjnych.

## Funkcje

- Tworzenie i wizualizacja grafów
- Stosowanie algorytmów kolorowania grafów
- Interaktywny GUI z wykorzystaniem TKinter
- Zapis i ładowanie grafów

## Instalacja

1. Sklonuj repozytorium:
   ```sh
   git clone https://github.com/PiotrGren/TKinter-Graph-Coloring-App.git
   ```
2. Przejdź do katalogu projektu:
   ```sh
   cd TKinter-Graph-Coloring-App
   ```
3. Projekt jest gotowy do użycia.

#### Alternatywa

Jako alternatywa, w folderze Installer znajduje się plik instalacyjny GraphColoring_setup.exe. Plik uruchomi instalator, który atuomatycznie zainstaluje aplikację już w formacie .exe oraz utworzy skrót do niej na pulpicie. Wystarczy go uruchomić i zainstalować aplikację, a następnie uruchomić aplikację.

```sh
Installer/GraphColoring_setup.exe
```

## Użycie

Aby uruchomić aplikację, wykonaj następujące polecenie:

```sh
python Graph_Coloring.py
```

Jeśli nie zdecydowałeś się na instalację aplikacji poprzez uruchomienie **GraphColoring_setup.exe**, możesz utworzyć własną aplikację w pliku .exe po pobraniu tego repozytorium.
Aby uruchomić ten proces na komputerze lokalnym, wykonaj następujące kroki:

1. Zainstaluj bibliotekę pyinstaller:
   ```sh
   pip install pyinstaller
   ```
   
2. Utwórz folder docelowy dla pliku .exe (opcjonalnie):
   ```sh
   mkdir -p /sciezka/do/twojego/folderu/docelowego
   ```

3. Przejdź do folderu, do którego został pobrany projekt:
   ```sh
   cd /sciezka/do/twojego/folderu/z/projektem
   ```

4. Uruchom to polecenie:
   ```sh
   pyinstaller --onefile --windowed --icon=icon.png --distpath /sciezka/do/twojego/folderu/docelowego Graph_Coloring.py
   ```
   lub (jeżeli chcesz utworzyć plik .exe w tym samym folderze co projekt):
   ```sh
   pyinstaller --onefile --icon=icon.png Graph_Coloring.py
   ```
Po wykonaniu tych kroków w określonym folderze docelowym pojawi się plik wykonywalny [.exe], uruchamiający aplikację.

## Licencja

Ten projekt jest licencjonowany na licencji MIT. Zobacz plik LICENSE aby uzyskać więcej informacji.

## Autorzy

Piotr Greń - Main developer - https://github.com/PiotrGren

### Współautorzy

- Gabriela Kiwacka - Współtwórca algorytmu kolorowania grafów
