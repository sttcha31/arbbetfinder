# Arbitrage Bet Finder
Arbitrage Bet Finder

# Introduction
## Available Websits
    * DraftKing
    * BetMGM
## Coming Soon
    * [bet365](https://www.va.bet365.com/?_h=Bh4f8Zb5idsEAAVTf9C40Q%3D%3D&btsffd=1#/AC/B18/C20604387/D43/E181378/F43/)

# Usage

1. Open Amazon AWS EC2 Instance of instance type t2.2xlarge and of OS Amazon Linux
2. **ONLY NEEDS TO BE DONE ONCE**: 
    - Clone github Project

        ```
        git clone https://github.com/sttcha31/arbbetfinder
        ```
    - Install python
        ```
        sudo yum groupinstall "Development Tools"
        sudo yum install python3 python3-devel
        ```
    - Locate Python.h location, and save it for later
        ```
        find /usr -name "Python.h" 2>/dev/null
        ```
    - Replace follow command with your python verson and the path from previous step
        ```
        g++ -o program your_program.cpp -I/<PATH_FROM_ABOVEW> -lpython3.<PYTHON_VERSON>
        ```
3. CD into repository

    ```
    cd arbbetfinder
    ```
4. Do this
    ```
    Xvfb :99 & export DISPLAY=:99
    ```
5. Run mgmgamelinkcatcher
    ```
    python3 betmgm_gamelinks.py
    ```
6. Run mgm scraper
    ```
    python3 betmgm_scraper.py
    ```
7. Run draft king scraper
    ```
    python3 draftking_scraper.py
    ```
8. Remove duplicates
    ```
    python3 duplicate.py
    ```
9. Compile main.exe
    ```
    clang++ -std=c++11 -o main  main.cpp Bookie.cpp
    ```
10. Run main.exe
    ```
    ./main.exe
    ```
