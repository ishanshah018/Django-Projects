from django.shortcuts import render, redirect, get_object_or_404
from .models import Player

def home(request):
    players = Player.objects.all()
    return render(request, 'home.html', {'players': players})

def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'player_detail.html', {'player': player})

def add_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        batting_style = request.POST.get('batting_style')
        bowling_style = request.POST.get('bowling_style')
        age = request.POST.get('age')
        runs_scored = request.POST.get('runs_scored')
        wickets_taken = request.POST.get('wickets_taken')

        Player.objects.create(
            name=name,
            country=country,
            batting_style=batting_style,
            bowling_style=bowling_style,
            age=age,
            runs_scored=runs_scored,
            wickets_taken=wickets_taken
        )
        return redirect('home')
    
    return render(request, 'add_player.html')



