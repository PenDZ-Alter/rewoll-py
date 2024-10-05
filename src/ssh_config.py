import paramiko
import time

class SSHConfig:
  def __init__(self, host, user, password=None, private_key_path=None, mac=None, interface="ether1", port=22):
    self.host = host
    self.user = user
    self.password = password
    self.private_key_path = private_key_path
    self.mac = mac
    self.interface = interface
    self.port = port
    
    paramiko.util.log_to_file("paramiko.log")

  # Method to send the WOL command via SSH
  def send_wol_via_ssh(self):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
      # Authentication using either password or private key
      if self.private_key_path:
        print(f"Using private key for authentication: {self.private_key_path}")
        private_key = paramiko.RSAKey.from_private_key_file(self.private_key_path)
        ssh.connect(self.host, username=self.user, pkey=private_key, port=self.port)
      elif self.password:
        print("Using password for authentication")
        ssh.connect(self.host, username=self.user, password=self.password, port=self.port)
      else:
        raise Exception("No valid authentication method provided. Provide either a password or a private key.")

      # Command to execute WOL
      wol_command = f"/tool wol interface={self.interface} mac={self.mac}"

      stdin, stdout, stderr = ssh.exec_command(wol_command)
      output = stdout.read().decode('utf-8')
      errors = stderr.read().decode('utf-8')

      if errors:
        raise Exception(f"Error from MikroTik: {errors}")

      print(f"Output from MikroTik: {output}")

    except FileNotFoundError:
      print(f"Private key file not found: {self.private_key_path}")
    except paramiko.ssh_exception.AuthenticationException as auth_error:
      print(f"Authentication failed: {auth_error}")
    except Exception as e:
      print(f"An error occurred: {str(e)}")
    finally:
      ssh.close()

  # Retry mechanism for running the command
  def retry_command(self, retries=10, delay=5):
    attempt = 0
    while attempt < retries:
      try:
        self.send_wol_via_ssh()
        print("Command executed successfully!")
        return True
      except Exception as e:
        print(f"Error executing command. Attempt {attempt + 1}/{retries}: {str(e)}")
        attempt += 1
        time.sleep(delay)
    raise Exception(f"Max retries reached. Command failed.")
