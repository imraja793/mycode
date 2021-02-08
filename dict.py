my_dict = {"name": "raja", "dob_month": "october", "Macbook Air": "Yes", "Will learn everyday": "yes"}
new_dict = {"title": "Software Developer", "work_exp": "2.9years"}
a = my_dict.get("s", "not there")
print(a, "dldmdldmdlmd")
my_dict['work'] = new_dict
print(my_dict)
print(my_dict["work"]["title"])
for profile, proffesional in list(my_dict.items()):
    print(f"profile data {profile} and values {proffesional}")
