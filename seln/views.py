from django.shortcuts import render
from seln.utils import AutomationWhatsApp

def send_message(message, numbers):
    automation = AutomationWhatsApp(content=message, numbers=numbers)
    return automation.send()