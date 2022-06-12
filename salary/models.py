from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Person(AbstractUser):
    middle_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(null=True)

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "persons"


class Project(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_absolute_url(self):
        return reverse("salary:project-detail", kwargs={'pk': self.pk})


class Bonus(models.Model):
    name = models.CharField(max_length=50)
    price_for_bonus = models.FloatField()

    def get_absolute_url(self):
        return reverse("salary:bonus-detail", kwargs={'pk': self.pk})

    def __str__(self):
        return f"+{self.price_for_bonus}$/day"


class PersonBonusProject(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    bonus = models.ForeignKey(to=Bonus, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.person}"


class ReportCard(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    person_bonus_project = models.ForeignKey(to=PersonBonusProject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.person_bonus_project.person} {self.person_bonus_project.project}"


class Wage(models.Model):
    position = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    pay_per_hour = models.FloatField()

    def __str__(self):
        return f"{self.position} {self.role}"

    def get_absolute_url(self):
        return reverse("salary:wage-detail", kwargs={'pk': self.pk})


class Main(models.Model):
    report_card = models.ForeignKey(to=ReportCard, on_delete=models.CASCADE)
    wage = models.ForeignKey(to=Wage, on_delete=models.CASCADE)

    @property
    def amount_of_days(self):
        return int(self.report_card.end.day - self.report_card.start.day)

    @property
    def base_salary(self):
        return f"{int((self.amount_of_days * 8) + self.wage.pay_per_hour)}$"

    @property
    def total_salary(self):
        return f"{float(self.report_card.person_bonus_project.bonus.price_for_bonus * (self.amount_of_days) + float(self.base_salary[:-1]))}$"

    def get_absolute_url(self):
        return reverse("salary:main-detail", kwargs={'pk': self.pk})
