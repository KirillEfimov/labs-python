def print_names(emps):
    for emp in emps:
        for child in emp["children"]:
            if child["age"] > 18:
                print(emp["name"])
                break


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 23,
   }],
}

emps = [ivan, darja]
print_names(emps)
