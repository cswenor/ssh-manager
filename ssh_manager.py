import json
import os
import subprocess
import time
from fabric import Connection

class SSHManager:
    def __init__(self):
        self.start_ssh_agent()
        self.load_computers()

    def start_ssh_agent(self):
        # Check if SSH agent is already running
        if "SSH_AUTH_SOCK" not in os.environ:
            # Start SSH agent and set environment variables
            agent_output = subprocess.check_output(['ssh-agent', '-s']).decode()
            for line in agent_output.splitlines():
                if line.startswith('SSH_AUTH_SOCK='):
                    # Extract and set the SSH_AUTH_SOCK environment variable
                    os.environ['SSH_AUTH_SOCK'] = line.split(';')[0].split('=')[1]
                if line.startswith('SSH_AGENT_PID='):
                    # Extract and set the SSH_AGENT_PID environment variable
                    os.environ['SSH_AGENT_PID'] = line.split(';')[0].split('=')[1]

    def load_computers(self):
        with open('computers.json', 'r') as file:
            self.computers = json.load(file).get('computers', [])

    def save_computers(self):
        with open('computers.json', 'w') as file:
            json.dump({'computers': self.computers}, file, indent=4)

    def add_computer(self, alias, ip, user, port, tags):
        self.computers.append({
            'alias': alias,
            'ip': ip,
            'user': user,
            'port': port,
            'tags': tags
        })
        self.save_computers()

    def list_computers(self, tag=None):
        for index, comp in enumerate(self.computers, start=1):
            if tag is None or tag in comp['tags']:
                print(f"{index}. {comp['alias']} - {comp['ip']}:{comp['port']} - Tags: {', '.join(comp['tags'])}")

    def execute_script(self, index, script_path):
        try:
            comp = self.computers[int(index) - 1]
        except IndexError:
            print(f"No computer found at index {index}")
            return
        
        conn = Connection(host=comp['ip'], user=comp['user'], port=comp['port'])
        result = conn.run(f'bash {script_path}')
        print(result.stdout.strip())

    def execute_script_in_batches(self, tag, script_path, delay):
        for index, comp in enumerate(self.computers, start=1):
            if tag in comp['tags']:
                print(f"Executing script on {comp['alias']} - {comp['ip']}:{comp['port']}")
                conn = Connection(host=comp['ip'], user=comp['user'], port=comp['port'])
                result = conn.run(f'bash {script_path}')
                print(result.stdout.strip())
                if index < len(self.computers):  # Check if this is not the last computer
                    print(f"Waiting {delay} seconds before proceeding to the next computer...")
                    time.sleep(int(delay))  # Delay before proceeding to the next computer

    def delete_computer(self, index):
        try:
            self.computers.pop(int(index) - 1)
        except IndexError:
            print(f"No computer found at index {index}")
            return
        self.save_computers()

    def open_ssh_terminal(self, index):
        try:
            comp = self.computers[int(index) - 1]
        except IndexError:
            print(f"No computer found at index {index}")
            return
        
        os.system(f"ssh {comp['user']}@{comp['ip']} -p {comp['port']}")
