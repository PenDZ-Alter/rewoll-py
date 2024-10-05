import argparse
import os
from dotenv import load_dotenv

class Config:
  def __init__(self):
    # Load .env file if it exists
    load_dotenv()

  def load_config(self):
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Wake-on-LAN via MikroTik SSH")

    parser.add_argument('--host', '-hs', help="MikroTik host address", required=False)
    parser.add_argument('--user', '-u', help="MikroTik username", required=False)
    parser.add_argument('--password', help="MikroTik password (optional)", required=False)
    parser.add_argument('--port', '-p', help="MikroTik Port Number (default 22))", required=False)
    parser.add_argument('--mac', '-m', help="MAC address of the PC to wake up", required=False)
    parser.add_argument('--key', '-k', help="Path to the SSH private key (.pem)", required=False)
    parser.add_argument('--interface', '-i', help="Network interface to send the WOL packet through", required=False)

    args = parser.parse_args()

    # Retrieve values from command-line arguments or environment variables
    config = {
      'host': args.host or os.getenv("HOST"),
      'user': args.user or os.getenv("USER"),
      'password': args.password or os.getenv("PASS"),
      'mac': args.mac or os.getenv("MAC_TARGET"),
      'key': args.key or os.getenv("SSH_KEY"),
      'interface': args.interface or os.getenv("INTERFACE", "ether1"),
      'port': args.port or os.getenv("PORT", "22")
    }

    # Ensure required variables are present
    if not config['host'] or not config['user'] or not config['mac']:
      raise ValueError("Host, user, and MAC address are required. Please provide them via arguments or .env file.")

    return config
