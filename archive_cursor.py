from treerec.trcursor import TreeObj_Cursor, retrieve
from trec_arx.archive_commands import cmd_new_archive#, ArchiveInputParser
from trec_arx.file_list import new_archive

class Arx_Cursor(TreeObj_Cursor):
    """
    def execute(self, command_input:str='', echo_command:bool=True):
        if echo_command: print(self.prompt(), command_input)
        madout = MainInputParser(command_input)
        if not madout:
            # print the error message
            print(madout)
        else:
            parameters = madout[1]
            cmd = parameters.get('command', None)
            nextcommand = self.command_dict.get(cmd, False)
            if nextcommand!=False:
                if retrieve(parameters, 'help', False):
                    print_help(cmd)
                else:
                    nextcommand(parameters)
    """
    def __init__(self):
        super().__init__()
        self.welcome_string = self.welcome_string + ', with archive commands'

    def build_command_dict(self):
        temp_dict = super().build_command_dict()
        temp_dict.update({cmd_new_archive: self.new_archive})
        return temp_dict

    def new_archive(self, parameters):
        if self.engine.CTREE!=self.engine.SYSCHAR:
            print('Must curently be on system (' + self.engine.SYSCHAR + ') to use this command.')
            return
        directory = retrieve(parameters, 'directory')
        filename = retrieve(parameters, 'filename')
        append_text = retrieve(parameters, 'append_text', strip=False)
        new_archive(pathstr=directory, append_text=append_text, filename=filename)
    

