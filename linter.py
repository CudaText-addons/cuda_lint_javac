# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
# License: MIT
# Change for CudaLint: Alexey T.

from cuda_lint import Linter, util


class Javac(Linter):
    """Provides an interface to javac."""

    syntax = 'Java'
    executable = 'javac'
    version_args = '-version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.7'
    regex = (
        r'^(?P<file>.+?):(?P<line>\d+): '
        r'(?:(?P<error>error)|(?P<warning>warning)): '
        r'(?:\[.+?\] )?(?P<message>[^\r\n]+)\r?\n'
        r'[^\r\n]+\r?\n'
        r'(?P<col>[^\^]*)\^'
    )
    multiline = True
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDERR
    defaults = {
        'lint': ''
    }
    inline_settings = 'lint'
    comment_re = r'\s*/[/*]'

    def cmd(self):
        """
        Return the command line to execute.

        We override this because we have to munge the -Xlint argument
        based on the 'lint' setting.

        """

        xlint = '-Xlint'
        options = 'all'

        if options:
            xlint += ':' + options

        return (self.executable_path, xlint, '*')

    def split_match(self, match):
        """
        Return the components of the match.

        We override this because javac lints all referenced files,
        and we only want errors from the linted file.

        """

        if match:
            if match.group('file') != self.filename:
                match = None

        return super().split_match(match)
