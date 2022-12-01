import subprocess
import tempfile
from pathlib import Path

PROG_LEADS = ('python', '-m', 'filemagick')


def test_sub_file_basic():
    with tempfile.TemporaryDirectory() as d:
        filepath = Path(d) / 'test.txt'
        filepath.write_text('hello,\n<name>!')

        ret = subprocess.check_output([
            *PROG_LEADS, 'sub', f'{d}/test.txt', '-p' '<name>', '-r', 'world'
        ]).decode()
        assert ret == 'hello,\nworld!'


def test_sub_file_verbose():
    with tempfile.TemporaryDirectory() as d:
        filepath = Path(d) / '__init__.py'
        filepath.write_text(
            'A = 1\n'
            '__version__ = "0.1.0"  # SOME COMMENT\n'
            'B = 2\n'
            'C = 3\n'
        )

        ret = subprocess.check_output([
            *PROG_LEADS, 'sub', str(filepath),
            '-p' r'__version__\s*=\s*"[^"]+"',
            '-r', r'__version__ = "0.1.0"'
        ]).decode()
        assert ret == (
            'A = 1\n'
            '__version__ = "0.1.0"  # SOME COMMENT\n'
            'B = 2\n'
            'C = 3\n'
        )


def test_sub_file_inplace_mode():
    with tempfile.TemporaryDirectory() as d:
        filepath = Path(d) / 'test.txt'
        filepath.write_text('hello,\n<name>!')

        ret = subprocess.check_output([
            *PROG_LEADS, 'sub', '-i', f'{d}/test.txt', '-p' '<name>', '-r', 'world'
        ]).decode()
        assert ret == ''
        assert filepath.read_text() == 'hello,\nworld!'
