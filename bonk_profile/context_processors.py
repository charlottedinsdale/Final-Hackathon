from .models import HighScore

def user_highscores(request):
    """
    Adds the user's highscores to the context
    """
    if  request.user.is_authenticated:
        highscores = HighScore.objects.filter(user=request.user)
    else:
        highscores = None
    return {"highscores": highscores}