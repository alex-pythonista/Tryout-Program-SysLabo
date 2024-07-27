from django.db import models


class CalendarChoice(models.TextChoices):
    OUTLOOK = "OUTLOOK"
    GOOGLE_CALENDER = "GOOGLE_CALENDAR"


class DateFormatChoice(models.TextChoices):
    YYYY_MM_DD = "YYYY-MM-DD"
    MM_DD_YYYY = "MM-DD-YYYY"
    DD_MM_YYYY = "DD-MM-YYYY"


class TimeFormatChoice(models.TextChoices):
    HOUR_12 = "12 HOUR"
    HOUR_24 = "24 HOUR"


class GenderChoice(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    N_A = "N/A"


class NotificationChoice(models.TextChoices):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DepartmentChoice(models.TextChoices):
    営業本部_Sales_Division = "営業本部"
    システム事業部_System_Division = "システム事業部"
    ITサポート事業部_IT_Support_Division = "ITサポート事業部"
    管理部_Management_Department = "管理部"
    N_A = "N/A"


class DivisionChoice(models.TextChoices):
    ソリューション営業部_Solution_Sales_Department = "ソリューション営業部"
    研究開発課_Research_and_Development_Section = "研究開発課"
    システム課_System_Section = "システム課"
    SW開発課_Software_Development_Section = "SW開発課"
    購買調達部_Purchasing_and_Procurement_Department = "購買調達部"
    N_A = "N/A"


class SectionChoice(models.TextChoices):
    課_1 = "1課"
    課_2 = "2課"
    N_A = "N/A"


class GroupChoice(models.TextChoices):
    G1 = "1G"
    G2 = "2G"
    G3 = "3G"
    G4 = "4G"
    N_A = "N/A"


class TitleChoice(models.TextChoices):
    代表取締役 = "代表取締役"
    本部長 = "本部長"
    事業部長 = "事業部長"
    部長 = "部長"
    課長 = "課長"
    担当課長 = "担当課長"
    主任 = "主任"
    主任２ = "主任２"
    課員 = "課員"
