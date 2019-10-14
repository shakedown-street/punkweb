from apps.music import models as music_models


def listed_artists(request):
    objects = music_models.Artist.objects

    if request.user and request.user.is_superuser:
        return objects.filter(
            albums__isnull=False
        ).distinct().order_by("name")

    listed = objects.filter(
        is_listed=True,
        albums__isnull=False,
    ).distinct()
    return listed.order_by("name")


def listed_albums(request):
    objects = music_models.Album.objects

    if request.user and request.user.is_superuser:
        return objects.filter(
            tracks__isnull=False
        ).distinct().order_by("-release_date")

    listed = objects.filter(
        is_listed=True,
        tracks__isnull=False,
    ).distinct()
    return listed.order_by("-release_date")


def listed_audio(request):
    objects = music_models.Audio.objects

    if request.user and request.user.is_superuser:
        return objects.all().order_by("disc_num", "track_num")

    return objects.filter(album__is_listed=True).order_by(
        "disc_num", "track_num"
    )
