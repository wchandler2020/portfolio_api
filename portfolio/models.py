from django.db import models

# Create your models here.
class Portfolio(models.Model):
    PORTFOLIO_CATEGORIES = (
    ('WEB DEVELOPMENT', 'Web Development'),
    ('FIGMA', 'Figma'),
    ('APPLICATION' , 'Application'),
    ('MOBILE', "Mobile Application"),
    )

    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100, choices=PORTFOLIO_CATEGORIES)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/files')
    git_hub_link = models.CharField(max_length=250)
    project_link = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "portfolio"

    def __str__(self) -> str:
        return self.title


class Education(models.Model):
    EDUCATION_CATEGORIES = (
    ('COLLEGE', 'College'),
    ('CODING BOOTCAMP', 'Coding Bootcamp'),
    ('ONLINE COURSE' , 'Online Course'),
    )
    category = models.CharField(max_length=100, choices=EDUCATION_CATEGORIES)
    year = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    desc = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "education"
