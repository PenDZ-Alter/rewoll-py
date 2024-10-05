## rewoll-py
A Simple program to turning on your PC using WoL from mikrotik via SSH.

### Getting Started
Before you do anything, clone this repository
```bash
git clone https://github.com/PenDZ-Alter/rewoll-py
```

### How to use?
1. There's to options to input your credentials <br>
    Using args : <br>
    To connect via args, you can use this example command : 
    ```bash
    python main.py -hs <host> -p 22 -u <mikrotik_user> -k <ssh_key_pem> -m <mac_addr> -i <interface>
    ```

    Using env : 
    ```bash
    HOST= # Host or IP of mikrotik
    USER= # Mikrotik user
    PASS= # Mikrotik pass
    MAC_TARGET= # MAC Address Target
    SSH_KEY= # SSH Key Path
    INTERFACE= # Interface Target
    PORT= # Port of SSH mikrotik
    ```

    Don't forget to rename `.env.example` to `.env`, otherwise this will not work for you.

2. If you using env, simply run this command : 
    ```bash
    python main.py
    ```