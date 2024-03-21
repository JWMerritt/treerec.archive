from treerec.command_parser import *
from treerec.commands import MainInputParser
from copy import copy

cmd_new_archive = 'new_archive'


NEW_ARCHIVE = CommandInput(
    'new_archive', 'archive', 'make_archive',
    include_help=False,
    default_data = {
        'command': cmd_new_archive,
        'directory': '.',
        'append_text': '',
        'filename': '.archive-new.txt'
    },
    flags=[
        InputParam(
            '-a', '--append',
            children=[
                VariableInputParam(
                    action_func=theirkey_func('append_text'),
                    final=True
                )
            ]
        ),
        InputParam(
            '-d', '--dir',
            children=[
                VariableInputParam(
                    action_func=theirkey_func('directory'),
                    final=True
                )
            ]
        ),
        InputParam(
            '-n', '--name',
            children=[
                VariableInputParam(
                    action_func=theirkey_func('filename'),
                    final=True
                )
            ]
        )
    ],
    children=[],
    final=True
)


ArchiveInputParser = MainInputParser
ArchiveInputParser.add_command(NEW_ARCHIVE)