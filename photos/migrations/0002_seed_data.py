from django.db import migrations

def seed_photos(apps, schema_editor):
    Photo = apps.get_model('photos', 'Photo')
    photos_data = [
        {"title": "Live Concert", "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=400", "description": "Amazing live concert performance"},
        {"title": "Stage Setup", "image_url": "https://images.unsplash.com/photo-1501386761578-eac5c94b800a?w=400", "description": "The stage setup before the show"},
        {"title": "Crowd", "image_url": "https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=400", "description": "The crowd enjoying the music"},
    ]
    for photo_data in photos_data:
        Photo.objects.create(**photo_data)

class Migration(migrations.Migration):
    dependencies = [
        ('photos', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(seed_photos),
    ]
