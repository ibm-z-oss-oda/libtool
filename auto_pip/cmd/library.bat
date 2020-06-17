@echo off
python -c "import sys;from auto_pip._cmd_argv.cmd import parse ;parse('__file__ %*'.split())"
@echo on
