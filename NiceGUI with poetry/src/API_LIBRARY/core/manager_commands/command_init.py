class CommandInit():
    command_dic = {}

    def __init__(self, *argv):
        for arg in argv:
            self.command_dic[arg.__class__] = arg