from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from django.views.generic.edit import FormMixin
from .models import Ticket, TicketComment
from .forms import TicketForm, TicketCommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from django.core.paginator import Paginator
from django.views.generic.base import RedirectView


@method_decorator(login_required, name='dispatch')
class RedirectHome(RedirectView):
    '''Class view to handle redirects back to Homepage'''
    permanent = False
    query_string = True
    pattern_name = 'ticket_list'
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class TicketListView(ListView):
    '''Class to handle ticket Model Data.'''
    paginate_by = 5
    queryset = Ticket.objects.all().order_by('-created_on')
    context_object_name = 'tickets'
    template_name = 'ticket-list.html'

@method_decorator(login_required, name='dispatch')
class TicketDetailView(DetailView, FormMixin):
    '''Class to handle single ticket model data.'''
    model = Ticket
    template_name = 'ticket-detail.html'

    def get_success_url(self):
        return reverse('ticket_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        kwargs['form'] = TicketCommentForm()
        kwargs['ticket'] = self.object
        kwargs['comments'] = TicketComment.objects.filter(ticket=self.object).order_by('-created_on')

        # code to set page indexing for comment listing
        paginator = Paginator(kwargs['comments'], 5)
        page_number = self.request.GET.get('page')
        kwargs['page_obj'] = paginator.get_page(page_number)
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TicketCommentForm(request.POST)
        form.instance.creator = request.user
        form.instance.ticket = self.object
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TicketCreateView(View):
    '''Class to create ticket object'''
    
    def get(self, request, *args, **kwargs):
        form = TicketForm()
        data = {'form': form}
        return render(request, 'ticket-create.html', data)
    
    def post(self, request, *args, **kwards):
        form = TicketForm(request.POST)
        form.instance.creator = request.user
        if form.is_valid():
            form.save()
        return render(request, 'success-confirmation.html')

@method_decorator(login_required, name='dispatch')
class TicketDeleteView(View):
    '''View to delete ticket object.'''
    template_name = 'success-confirmation.html'

    def get(self, request, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk = kwargs['pk'])
        ticket.delete()
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class TicketUpdateView(View):
    '''View to update ticket object.'''

    def get(self, request, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk = kwargs['pk'])
        data_form = {
            'description': ticket.description,
            'is_resolved': ticket.is_resolved,
            'project': ticket.project,
            'priority': ticket.priority
        }
        form = TicketForm(initial=data_form)
        form_comment = TicketCommentForm()
        context = {
            'form': form,
            'form_comment': form_comment,
            'ticket': ticket
        }
        return render(request, 'ticket-update.html', context)

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        form_comment = TicketCommentForm(request.POST)
        print(form_comment)
        if form.is_valid():
            Ticket.objects.filter(pk=kwargs['pk']).update(
                description=form.cleaned_data['description'],
                is_resolved=form.cleaned_data['is_resolved'],
                project=form.cleaned_data['project'],
                priority=form.cleaned_data['priority'],
                last_updated=timezone.now()
            )
        return render(request, 'success-confirmation.html')
