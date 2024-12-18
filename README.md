# Arbitrage Bet Finder
Arbitrage Bet Finder

# Introduction

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