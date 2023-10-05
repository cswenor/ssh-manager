# SSH Manager

SSH Manager is a command-line application written in Python, utilizing the Fabric library to manage and interact with remote computers via SSH. It provides features like listing, adding, deleting computers, executing scripts remotely, opening an SSH terminal, and executing scripts in batches based on tags with a specified delay between each computer.

## Setup

1. **Install Python**:
    - Ensure you have Python 3.6 or newer installed on your machine.
    - Download and install Python from [the official website](https://www.python.org/downloads/).

2. **Install Fabric**:
    - Open a terminal.
    - Run the following command to install the Fabric library:
        ```bash
        pip install fabric
        ```

3. **Setup SSH Agent**:
    - Run the following command to start the SSH agent in the background:
        ```bash
        eval $(ssh-agent -s)
        ```
    - Now, add your private key to the agent:
        ```bash
        ssh-add ~/.ssh/your-private-key
        ```
    - You'll be prompted to enter the passphrase for your private key. This is the only time you'll need to enter the passphrase, as long as the SSH agent is running.

4. **Clone or Download the Repository**:
    - Clone this repository to your local machine or download the scripts `ssh_manager.py`, `main.py`, and the initial `computers.json` file.
    - Place these files in a directory of your choice.

## Usage

1. **Start the Application**:
    - Navigate to the directory containing the scripts.
    - Run the following command to start the application:
        ```bash
        python main.py
        ```

2. **Adding Computers**:
    - When prompted, enter the command `add` to add a new computer.
    - Follow the prompts to enter the alias, IP address, username, port, and tags for the computer.

3. **Listing Computers**:
    - Enter the command `list` to list all computers, or `list [tag]` to list all computers with a specific tag.

4. **Deleting Computers**:
    - Enter the command `delete`, then enter the index of the computer you want to delete when prompted.

5. **Executing Scripts**:
    - Enter the command `execute`, then follow the prompts to enter the index of the computer and the path to the script you want to execute.

6. **Batch Executing Scripts**:
    - Enter the command `batch_execute`, then follow the prompts to enter the tag, the path to the script, and the delay in seconds between each computer.

7. **Opening an SSH Terminal**:
    - Enter the command `ssh`, then enter the index of the computer you want to open an SSH terminal to.

8. **Exiting the Application**:
    - Enter the command `exit` to exit the application.

---

This README provides a general outline of the setup and usage of your scripts. Make sure to adjust the paths and commands to match your actual setup and requirements.