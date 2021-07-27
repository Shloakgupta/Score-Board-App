from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Team, Member

def home(request):
    teams = Team.objects.all().order_by("-team_points")
    members = Member.objects.all()
    stuff_for_frontend = {
        "teams":teams,
        "members":members
    }
    return render(request, "score_board/home.html", stuff_for_frontend)

def create_team(request):
    if request.method == "POST":
        team_name_obj = request.POST["name"]
        Team.objects.create(
            team_name=team_name_obj
        )
        return redirect('/')
    else:
        return render(request, "score_board/create_team.html")

def detail(request, team_id):
    team = Team.objects.get(id=team_id)
    stuff_for_frontend = {'team': team}
    return render(request, 'score_board/detail.html', stuff_for_frontend)

def edit(request, team_id):
    if request.method == "POST":
        team = Team.objects.get(id=team_id)
        new_team_name = request.POST['name']
        new_team_points = request.POST['points']
        team.team_name = new_team_name
        team.team_points = new_team_points
        team.save()
        return redirect('detail', team_id=team.id)
    else:
        team = Team.objects.get(id=team_id)
        stuff_for_frontend = {"team":team}
        return render(request, "score_board/edit_team.html", stuff_for_frontend)

def add_points(request, team_id):
    if request.method == "POST":
        team = Team.objects.get(id=team_id)
        team_points = team.team_points
        new_team_points = request.POST['points']
        team.team_points = int(team_points) + int(new_team_points)
        team.save()  
        return redirect('detail', team_id=team.id)
    else:
        team = Team.objects.get(id=team_id)
        stuff_for_frontend = {"team":team}
        return render(request, "score_board/add_points.html", stuff_for_frontend)

def delete(request, team_id):
    team_obj = Team.objects.get(id=team_id)
    team_obj.delete()
    return redirect('/')

def rename(request, team_id):
    if request.method == "POST":
        team = Team.objects.get(id=team_id)
        new_team_name = request.POST['name']
        team.team_name = new_team_name
        team.save()
        return redirect('detail', team_id=team.id)
    else:
        team = Team.objects.get(id=team_id)
        stuff_for_frontend = {"team":team}
        return render(request, "score_board/rename.html", stuff_for_frontend)

def create_member(request, team_id):
    if request.method == "POST":
        team_obj = Team.objects.get(id=team_id)
        new_member_name = request.POST['name']
        Member.objects.create(
            member_name=new_member_name,
            team=team_obj
        )
        return redirect('detail', team_id=team_obj.id)
    else:
        team = Team.objects.get(id=team_id)
        stuff_for_frontend = {"team":team}
        return render(request, "score_board/create_member.html", stuff_for_frontend)

def delete_member(request, member_id, team_id):
    member = Member.objects.get(id=member_id)
    team = Team.objects.get(id=team_id)
    member.delete()
    return redirect("detail", team_id=team.id)

def edit_member(request, member_id ,team_id):
    if request.method == "POST":
        team = Team.objects.get(id=team_id)
        member = Member.objects.get(id=member_id)
        new_member_name = request.POST['name']
        member.member_name = new_member_name
        member.save()
        return redirect('detail', team_id=team.id)
    else:
        team = Team.objects.get(id=team_id)
        member = Member.objects.get(id=member_id)
        stuff_for_frontend = {"team":team, "member":member}
        return render(request, "score_board/edit_member.html", stuff_for_frontend)