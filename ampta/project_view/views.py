from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from ampta.models import Project, ProjectForm, SearchForm

@login_required(login_url='/login')
def index(request):
	project_list = get_list_or_404(Project.objects.all())
	context = {'project_list': project_list}
	return render(request, 'projects/index.html', context)

@login_required(login_url='/login')
def search(request):
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			search = form.cleaned_data["search"]
			try:
				results = Project.objects.filter(name__contains=search)
				context = {"form": form, "results": results}
				return render(request, 'projects/search.html', context)
			except Exception as e:
				context = {"form": form, "message": "No projects found"}
				return render(request, 'projects/search.html', context)
	else:
		form = SearchForm()

	context = {"form": form}
	return render(request, 'projects/search.html', context)

@login_required(login_url='/login')
def detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if project.is_member(request.user):
		context = {'project': project}
		return render(request, 'projects/detail.html', context)
	else:
		context = {'message': "You don't have permissions to view this project"}
		return render(request, 'helper/permission.html', context)

@login_required(login_url='/login')
def edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)

	if project.is_owner(request.user):
		if request.method == "POST":
			form = ProjectForm(request.POST, instance = project)
			if form.is_valid():
				try:
					form.save()
					return redirect('project_list')
				except:
					context = {'message': "Something went wrong in the save process."}
					return render(request, 'helper/permission.html', context)
		else:
			form = ProjectForm(instance = project)
	else:
		context = {'message': "You don't have permissions to edit this project"}
		return render(request, 'helper/permission.html', context)

	context = {'form': form}
	return render(request, 'projects/add.html', context)


@login_required(login_url='/login')
def delete(request, project_id):
	project = get_object_or_404(Project, pk=project_id)

	if project.is_owner(request.user):
		project.delete()
		return redirect('project_list')
	else:
		context = {'message': "You don't have permissions to delete this project"}
		return render(request, 'helper/permission.html', context)

@login_required(login_url='/login')
def add(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.instance.owner = request.user
			form.instance.pub_date = datetime.date.today()
			form.save()
			return redirect('project_list')
	else:
		form = ProjectForm()

	context = {'form': form }
	return render(request, 'projects/add.html', context)