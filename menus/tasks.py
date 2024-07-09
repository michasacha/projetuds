# tasks.py
from celery import shared_task
from .models import Menu, Repas
import random
from datetime import timedelta
from django.utils import timezone

@shared_task
def update_weekly_menu():
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    repass = Repas.objects.all()
    
    for day in range(7):
        menu_date = start_of_week + timedelta(days=day)
        repas = random.choice(repass)
        Menu.objects.update_or_create(date=menu_date, defaults={'repas': repas})
 