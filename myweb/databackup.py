from django.core.management import call_command
from django.core.management import execute_from_command_line
import  os,sys
def dbbackup():
    call_command("dbbackup")

dbbackup()