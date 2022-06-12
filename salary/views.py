from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    ProjectForm,
    WageForm,
    BonusForm,
    BonusSearchForm,
    WageSearchForm,
    ProjectSearchForm,
    MainSearchForm,
    MainForm,
)
from .models import Project, Bonus, Main, Wage


class MainListView(generic.ListView):
    model = Main
    paginate_by = 2
    queryset = Main.objects.all()


class MainDetailView(generic.DetailView):
    model = Main


class MainCreateView(generic.CreateView):
    model = Main
    form_class = MainForm
    template_name = "salary/main_form.html"
    success_url = reverse_lazy("salary:main-list")


class MainUpdateView(generic.UpdateView):
    model = Main
    form_class = MainForm
    template_name = "salary/main_form.html"
    success_url = reverse_lazy("salary:main-list")


class MainDeleteView(generic.DeleteView):
    model = Main
    fields = "__all__"
    template_name = "salary/main_confirm_delete.html"
    success_url = reverse_lazy("salary:main-delete")


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 2
    queryset = Project.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = ProjectSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = ProjectSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])

        return self.queryset


class ProjectCreateView(generic.CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "salary/project_form.html"
    success_url = reverse_lazy("salary:project-list")


class ProjectUpdateView(generic.UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "salary/project_form.html"
    success_url = reverse_lazy("salary:project-list")


class ProjectDeleteView(generic.DeleteView):
    model = Project
    fields = "__all__"
    template_name = "salary/project_confirm_delete.html"
    success_url = reverse_lazy("salary:project-delete")


class ProjectDetailView(generic.DetailView):
    model = Project


class WageListView(generic.ListView):
    model = Wage
    context_object_name = "wage_list"
    template_name = "salary/wage_list.html"
    paginate_by = 2
    queryset = Wage.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WageListView, self).get_context_data(**kwargs)

        position = self.request.GET.get("position", "")

        context["search_form"] = WageSearchForm(initial={"position": position})

        return context

    def get_queryset(self):
        form = WageSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                position__icontains=form.cleaned_data["position"]
            )

        return self.queryset


class WageCreateView(generic.CreateView):
    model = Wage
    form_class = WageForm
    template_name = "salary/wage_form.html"
    success_url = reverse_lazy("salary:wage-list")


class WageUpdateView(generic.UpdateView):
    model = Wage
    form_class = WageForm
    template_name = "salary/wage_form.html"
    success_url = reverse_lazy("salary:wage-list")


class WageDeleteView(generic.DeleteView):
    model = Wage
    fields = "__all__"
    template_name = "salary/wage_confirm_delete.html"
    success_url = reverse_lazy("salary:wage-delete")


class WageDetailView(generic.DetailView):
    model = Wage


class BonusListView(generic.ListView):
    model = Bonus
    context_object_name = "bonus_list"
    template_name = "salary/bonus_list.html"
    paginate_by = 2
    queryset = Bonus.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BonusListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = BonusSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = BonusSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])

        return self.queryset


class BonusCreateView(generic.CreateView):
    model = Bonus
    form_class = BonusForm
    template_name = "salary/bonus_form.html"
    success_url = reverse_lazy("salary:bonus-list")


class BonusUpdateView(generic.UpdateView):
    model = Bonus
    form_class = BonusForm
    template_name = "salary/bonus_form.html"
    success_url = reverse_lazy("salary:bonus-list")


class BonusDeleteView(generic.DeleteView):
    model = Bonus
    fields = "__all__"
    template_name = "salary/bonus_confirm_delete.html"
    success_url = reverse_lazy("salary:bonus-delete")


class BonusDetailView(generic.DetailView):
    model = Bonus
