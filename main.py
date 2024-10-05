from src.config import Config
from src.ssh_config import SSHConfig

def main():
  # Load the configuration (either from .env or argparse)
  config = Config().load_config()

  # Initialize the SSH configuration with the provided settings
  ssh = SSHConfig(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    private_key_path=config['key'],
    mac=config['mac'],
    interface=config['interface'],
    port=config['port']
  )

  # Execute the Wake-on-LAN command with retries
  try:
    ssh.retry_command()
    print("PC has been successfully turned on via MikroTik.")
  except Exception as e:
    print(f"Failed to turn on PC: {str(e)}")

if __name__ == "__main__":
  main()
