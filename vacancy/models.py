import unidecode

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from company.models import Company
from resume.models import Resume


class Vacancy(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название вакансии'
    )
    specialty = models.ForeignKey(
        'Specialty',
        on_delete=models.CASCADE,
        related_name='vacancies',
        verbose_name='Специализация'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Url'
    )
    company = models.ForeignKey(
        Company,
        related_name='vacancies',
        verbose_name='Компания',
        on_delete=models.CASCADE
    )
    skills = models.ManyToManyField(
        'Skill',
        verbose_name='Требуемые навыки',
        related_name='skills',
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание вакансии'
    )
    salary_min = models.IntegerField(
        default=0,
        verbose_name='Зарплата от'
    )
    salary_max = models.IntegerField(
        default=0,
        verbose_name='Зарплата до',
        blank=True)
    photo = models.ImageField(
        blank=True)
    published_at = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_at = models.DateField(
        auto_now=True)
    contacts = models.TextField(
        max_length=250,
        blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = unidecode.unidecode(self.title).lower()
        self.slug = slugify(value, allow_unicode=False)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'


class Specialty(models.Model):
    code = models.CharField(
        max_length=155,
        verbose_name='Код'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Url'
    )
    image = models.ImageField(
        upload_to='specialty/%Y/%m/%d/',
        verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('specialization', kwargs={'specialization': self.slug})

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Skill(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название навыка',
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Application(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='app'
    )
    written_cover_letter = models.TextField(
        verbose_name='Сопроводительное письмо'
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='applications',
        verbose_name='Отклик на вакансию',
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications',
        verbose_name='Пользователь',
        null=True
    )
