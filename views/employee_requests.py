EMPLOYEES = [
    {
      "name": "Jeremy Bakker",
       "address": "100 Infinity Way",
        "locationId": 1
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    chosen_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            chosen_employee = employee
    return chosen_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["locationId"]
    new_id = max_id + 1
    employee["locationId"] = new_id
    EMPLOYEES.append(employee)
    return employee
def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["locationId"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["locationId"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break


