class Command:
    def __init__(self, name):
        self.name = name

    def execute(self):
        try:
            exec(self.name)
        except Exception as e:
            print(f"命令执行出错：{e}")

    def __str__(self):
        return f"Command(name={self.name})"


class Bucket:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def remove_command(self, command):
        if command in self.commands:
            self.commands.remove(command)

    def new_bucket(self):
        self.commands = []

    def move_up(self, command):
        if command in self.commands:
            index = self.commands.index(command)
            if index > 0:
                self.commands[index], self.commands[index-1] = self.commands[index-1], self.commands[index]

    def move_down(self, command):
        if command in self.commands:
            index = self.commands.index(command)
            if index < len(self.commands) - 1:
                self.commands[index], self.commands[index+1] = self.commands[index+1], self.commands[index]

    def execute_top_command(self):
        if not self.commands:
            print("桶为空，无命令可执行！")
            return

        command = self.commands.pop()

        print(f"正在执行命令：{command}")
        command.execute()
        print(f"命令执行完毕：{command}")

    def __str__(self):
        return f"Bucket(commands={self.commands})"
