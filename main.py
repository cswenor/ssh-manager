from ssh_manager import SSHManager

def main():
    manager = SSHManager()
    while True:
        command = input("Enter command (list, add, delete, execute, batch_execute, ssh, exit): ").lower()
        if command == 'list':
            tag = input("Enter tag to filter by or leave empty to list all: ")
            manager.list_computers(tag if tag else None)
        elif command == 'add':
            alias = input("Enter alias: ")
            ip = input("Enter IP: ")
            user = input("Enter user: ")
            port = input("Enter port: ")
            tags = input("Enter tags (comma-separated): ").split(',')
            manager.add_computer(alias, ip, user, port, tags)
        elif command == 'delete':
            index = input("Enter index of the computer to delete: ")
            manager.delete_computer(index)
        elif command == 'execute':
            index = input("Enter index of the computer: ")
            script_path = input("Enter script path: ")
            manager.execute_script(index, script_path)
        elif command == 'batch_execute':
            tag = input("Enter tag to filter by: ")
            script_path = input("Enter script path: ")
            delay = input("Enter delay in seconds between each computer: ")
            manager.execute_script_in_batches(tag, script_path, delay)
        elif command == 'ssh':
            index = input("Enter index of the computer: ")
            manager.open_ssh_terminal(index)
        elif command == 'exit':
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
