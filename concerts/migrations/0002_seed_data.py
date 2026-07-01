from django.db import migrations

def seed_concerts(apps, schema_editor):
    Concert = apps.get_model('concerts', 'Concert')
    concerts_data = [
        {"band_name": "The Rockers", "venue": "Madison Square Garden", "city": "New York", "date": "2025-12-15", "ticket_price": "89.99"},
        {"band_name": "Jazz Ensemble", "venue": "Blue Note", "city": "Chicago", "date": "2025-11-20", "ticket_price": "65.00"},
        {"band_name": "Electric Dreams", "venue": "The Forum", "city": "Los Angeles", "date": "2026-01-10", "ticket_price": "75.50"},
        {"band_name": "Acoustic Vibes", "venue": "Ryman Auditorium", "city": "Nashville", "date": "2025-10-05", "ticket_price": "55.00"},
    ]
    for concert_data in concerts_data:
        Concert.objects.create(**concert_data)

class Migration(migrations.Migration):
    dependencies = [
        ('concerts', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(seed_concerts),
    ]
