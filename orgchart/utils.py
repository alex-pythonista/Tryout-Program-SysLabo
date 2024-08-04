from django.db.models import Case, When, IntegerField
from .models import SysUser

def get_sales_department():
    employee_map = {
        "営業本部": {
            "head": "", # in the list, there will title and name
            "ソリューション営業部": {
                "head": [],
                "1課": {
                    "head": [],
                    "1G": {
                        "head": "",
                        "members": []
                    },
                    "2G": {
                        "head": "",
                        "members": []
                    },
                },
                "2課": {
                    "head": "",
                    "1G": {
                        "head": "",
                        "members": []
                    },
                    "2G": {
                        "head": "",
                        "members": []
                    },
                }
            }
        } 
    }
    sales_people = SysUser.objects.filter(department='営業本部')
    for people in sales_people:
        if people.title == '本部長':
            employee_map["営業本部"]["head"] = people.first_name + ' ' + people.last_name
        elif people.title == '部長':
            employee_map["営業本部"]["ソリューション営業部"]["head"] = people.first_name + ' ' + people.last_name
        
    課1_people = SysUser.objects.filter(section='1課')
    課2_people = SysUser.objects.filter(section='2課')

    for people in 課1_people:
        if people.title == '課長':
            employee_map["営業本部"]["ソリューション営業部"]["1課"]["head"] = people.first_name + ' ' + people.last_name
        elif people.title == '主任' and people.group == '1G':
            employee_map["営業本部"]["ソリューション営業部"]["1課"]["1G"]["head"] = people.first_name + ' ' + people.last_name
        elif people.title == '主任' and people.group == '2G':
            employee_map["営業本部"]["ソリューション営業部"]["1課"]["2G"]["head"] = people.first_name + ' ' + people.last_name
        elif people.group == '1G':
                employee_map["営業本部"]["ソリューション営業部"]["1課"]["1G"]["members"].append(people.first_name + ' ' + people.last_name)
        elif people.group == '2G':
            employee_map["営業本部"]["ソリューション営業部"]["1課"]["2G"]["members"].append(people.first_name + ' ' + people.last_name) 

    for people in 課2_people:
        if people.title == '課長':
            employee_map["営業本部"]["ソリューション営業部"]["2課"]["head"] = people.first_name + ' ' + people.last_name
        elif people.title == '主任' and people.group == '1G':
            employee_map["営業本部"]["ソリューション営業部"]["2課"]["1G"]["head"] = people.first_name + ' ' + people.last_name
        elif people.title == '主任' and people.group == '2G':
            employee_map["営業本部"]["ソリューション営業部"]["2課"]["2G"]["head"] = people.first_name + ' ' + people.last_name
        elif people.group == '1G':
            employee_map["営業本部"]["ソリューション営業部"]["2課"]["1G"]["members"].append(people.first_name + ' ' + people.last_name)
        elif people.group == '2G':
            employee_map["営業本部"]["ソリューション営業部"]["2課"]["2G"]["members"].append(people.first_name + ' ' + people.last_name)
    
    return employee_map

def get_system_department():
    employee_map = {
        "システム事業部": "",
        "研究開発課": {
            "head": "",
            "members": []
        },
        "システム課": {
            "head": "",
            "members": []
        },
        "SW開発課": {
            "head": "",
            "1G": {
                "head": [],
                "members": []
            },
            "2G": {
                "head": "",
                "members": []
            },
            "3G": {
                "head": "",
                "members": []
            },
            "4G": {
                "head": "",
                "members": []
            },
        }   
    }

    system_head = SysUser.objects.filter(department='システム事業部', title='事業部長').first()
    employee_map["システム事業部"] = system_head.first_name + ' ' + system_head.last_name

    section_managers = SysUser.objects.filter(title='課長')
    for people in section_managers:
        if people.division == '研究開発課':
            employee_map["研究開発課"]["head"] = people.first_name + ' ' + people.last_name
        if people.division == 'システム課':
            employee_map["システム課"]["head"] = people.first_name + ' ' + people.last_name
        if people.division == 'SW開発課':
            employee_map["SW開発課"]["head"] = people.first_name + ' ' + people.last_name

    section_staff = SysUser.objects.filter(department='システム事業部').exclude(title='課長').exclude(division='SW開発課')
    for people in section_staff:
        if people.division == '研究開発課':
            employee_map["研究開発課"]["members"].append(people.first_name + ' ' + people.last_name)
        if people.division == 'システム課':
            employee_map["システム課"]["members"].append(people.first_name + ' ' + people.last_name)

    g_leaders = SysUser.objects.filter(division='SW開発課', title__in=['主任', '主任２'])
    for people in g_leaders:
        if people.group == '1G':
            employee_map["SW開発課"]["1G"]["head"].append(people.first_name + ' ' + people.last_name)
            employee_map["SW開発課"]["1G"]["head"].append(people.title)
        elif people.group == '2G':
            employee_map["SW開発課"]["2G"]["head"].append(people.first_name + ' ' + people.last_name)
            employee_map["SW開発課"]["2G"]["head"].append(people.title)
        elif people.group == '3G':
            employee_map["SW開発課"]["3G"]["head"].append(people.first_name + ' ' + people.last_name)
            employee_map["SW開発課"]["3G"]["head"].append(people.title)
        elif people.group == '4G':
            employee_map["SW開発課"]["4G"]["head"].append(people.first_name + ' ' + people.last_name)
            employee_map["SW開発課"]["4G"]["head"].append(people.title)

    g_members = SysUser.objects.filter(division='SW開発課').exclude(title__in=['課長', '主任', '主任２'])
    for people in g_members:
        if people.group == '1G':
            employee_map["SW開発課"]["1G"]["members"].append(people.first_name + ' ' + people.last_name)
        elif people.group == '2G':
            employee_map["SW開発課"]["2G"]["members"].append(people.first_name + ' ' + people.last_name)
        elif people.group == '3G':
            employee_map["SW開発課"]["3G"]["members"].append(people.first_name + ' ' + people.last_name)
        elif people.group == '4G':
            employee_map["SW開発課"]["4G"]["members"].append(people.first_name + ' ' + people.last_name)

    return employee_map

def get_support_people():
    employee_map = {}
    title_hierarchy = [
        '代表取締役', '本部長', '事業部長', '部長', 
        '課長', '担当課長', '主任', '主任２'
    ]

    # Create a Case/When expression to assign a numerical value to each title
    title_order = Case(
        *[When(title=title, then=pos) for pos, title in enumerate(title_hierarchy)],
        output_field=IntegerField()
    )

    # Get the queryset and annotate with the numerical value
    g_leaders = SysUser.objects.filter(department='ITサポート事業部').exclude(title="課員").annotate(
        title_rank=title_order
    ).order_by('title_rank')
    employee_map["management"] = g_leaders

    staffs = SysUser.objects.filter(department='ITサポート事業部', title="課員")
    employee_map["staffs"] = staffs
    print(employee_map)
    return employee_map