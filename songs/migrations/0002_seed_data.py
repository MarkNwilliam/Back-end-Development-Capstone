from django.db import migrations

def seed_songs(apps, schema_editor):
    Song = apps.get_model('songs', 'Song')
    songs_data = [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night at the Opera", "year": 1975, "lyrics": "Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality..."},
        {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "album": "Led Zeppelin IV", "year": 1971, "lyrics": "There's a lady who's sure all that glitters is gold, And she's buying a stairway to heaven..."},
        {"title": "Hotel California", "artist": "Eagles", "album": "Hotel California", "year": 1976, "lyrics": "On a dark desert highway, cool wind in my hair, Warm smell of colitas, rising up through the air..."},
        {"title": "Under Pressure", "artist": "Queen & David Bowie", "album": "Hot Space", "year": 1982, "lyrics": "Pressure pushing down on me, Pressing down on you, no man ask for..."},
        {"title": "Paint It Black", "artist": "The Rolling Stones", "album": "Aftermath", "year": 1966, "lyrics": "I see a red door and I want it painted black, No colors anymore I want them to turn black..."},
    ]
    for song_data in songs_data:
        Song.objects.create(**song_data)

class Migration(migrations.Migration):
    dependencies = [
        ('songs', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(seed_songs),
    ]
