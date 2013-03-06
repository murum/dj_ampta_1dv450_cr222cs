from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
import datetime
from ampta.models import Ticket, TicketForm, Project

@login_required(login_url='/login')
def detail(request, project_id, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	project = get_object_or_404(Project, pk=project_id)
	if project.is_member(request.user):
		context = {'ticket': ticket}
		return render(request, 'tickets/detail.html', context)
	else:
		context = {'message': "You don't have permissions to view this ticket"}
		return render(request, 'helper/permission.html', context)

@login_required(login_url='/login')
def add(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	
	if project.is_member(request.user):
		if request.method == "POST":
			form = TicketForm(request.POST)
			if form.is_valid():
				form.instance.project = get_object_or_404(Project, pk=project_id)
				form.instance.owner = request.user
				form.instance.pub_date = datetime.date.today()
				form.save()
				return redirect('project_list')
		else:
			form = TicketForm()
	else:
		context = {'message': "You don't have permissions to add a ticket to this project"}
		return render(request, 'helper/permission.html', context)

	context = {'form': form}
	return render(request, 'tickets/add.html', context)

@login_required(login_url='/login')
def edit(request, project_id, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)

	if ticket.is_owner(request.user):
		if request.method == "POST":
			form = TicketForm(request.POST, instance = ticket)
			if form.is_valid():
				try:
					form.save()
					return redirect('project_list')
				except:
					return HttpResponseServerError()
		else:
			form = TicketForm(instance = ticket)
	else:
		context = {'message': "You don't have permissions to edit this project"}
		return render(request, 'helper/permission.html', context)

	context = {'form': form}

	return render(request, 'tickets/add.html', context)

@login_required(login_url='/login')
def delete(request, project_id, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)

	if ticket.is_owner(request.user):
		ticket.delete()
		return redirect('project_list')
	else:
		context = {'message': "You don't have permissions to delete this ticket"}
		return render(request, 'helper/permission.html', context)