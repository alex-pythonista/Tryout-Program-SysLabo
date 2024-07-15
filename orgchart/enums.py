from django.db import models


class CalendarChoice(models.TextChoices):
    OUTLOOK = "OUTLOOK"
    GOOGLE_CALENDER = "GOOGLE_CALENDAR"


class DateFormatChoice(models.TextChoices):
    YYYY_MM_DD = "YYYY-MM-DD"
    MM_DD_YYYY = "MM-DD-YYYY"
    DD_MM_YYYY = "DD-MM-YYYY"


class GenderChoice(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    N_A = "N/A"