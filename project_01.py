def record(patient_id, first_name, last_name, address, gender, contact):
    fw = open("patient_info.txt", "a")
    fw.write("%1s%20s%20s%20s%20s%20s\n" %(patient_id, first_name, last_name, address, gender, contact))
    fw.close()

def append(patient_id, invoice_id, treatment_id, bill_amount):
    fw = open("paymentdata.txt", "a")
    fw.write("%1s%20s%20s%20s\n" % (patient_id, invoice_id, treatment_id, bill_amount))
    fw.close()

def appoint(patient_id, appointment_id, specialist, status):
    fw = open("appointment_plan.txt", "a")
    fw.write("%1s%20s%20s%20s\n" % (patient_id, appointment_id, specialist, status))
    fw.close()

def treatment_plan(patient_id, treatment_id, complaint, treatment):
    fw = open("treatment_plan.txt", "a")
    fw.write("%1s%20s%20s%50s\n" % (patient_id, treatment_id, complaint, treatment))
    fw.close()

print("Welcome to Prudent Healthcare Service\n")
print("What type of login do you want?\n1. Reception Login\n2. Physician Login\n3. Accountant Login\n")

def login():
    username = input("\nEnter your username:")
    password = input("Enter your password:")
    print("\nWelcome to PMS", username)

def appointment():
    patient_id = input("\nEnter the patient ID:")
    appointment_id = input("Enter the appointment ID:")
    specialist = input("Enter the name of the specialist for checkup:")
    status = input("Enter the status:")
    appoint(patient_id, appointment_id, specialist, status)

def patient_treatment_plan():
    patient_id = input("\nEnter the patient ID:")
    treatment_id = input("Enter the treatment ID:")
    complaint = input("Enter the complaint of the patient:")
    treatment = input("Enter the suggested treatment to the patient:")
    treatment_plan(patient_id, treatment_id, complaint, treatment)

def read_treatment_plan():
    read = open("treatment_plan.txt")
    enter = input("\nPlease input patient ID:")
    for each_line in read:
        (patient_id, treatment_id, complaint, treatment) = each_line.split()

        if patient_id == enter:
            print(patient_id, treatment_id, complaint, treatment)
    read.close()


def entry():
    patient_id = input("\nEnter the Patient ID:")
    print(patient_id)
    first_name = input("Enter the First Name:")
    print(first_name)
    last_name = input("Enter the Last Name:")
    print(last_name)
    address = input("Enter the Address:")
    print(address)
    gender = input("Enter the Gender:")
    print(gender)
    contact = input("Enter the Contact:")
    print(contact)

    record(patient_id, first_name, last_name, address, gender, contact)

def read_patient_info():
    read = open("patient_info.txt")
    enter = input("\nPlease input patient ID:")
    for each_line in read:
        (patient_id, first_name, last_name, address, gender, contact) = each_line.split()

        if patient_id == enter:
            print(patient_id, first_name, last_name, address, gender, contact)
    read.close()

def logout():
    print("\nWe are glad to help you, Thank you!!!")

option = input("Choose your login type:")
choose = int(option)

if (choose == 1):
    login()
    while True:
        print("\n1. Record the patient information\n2. Search the patient information\n")
        menu = input("Choose any option from the menu:")
        choose = int(menu)

        if (choose == 1):
            entry()
        elif (choose == 2):
            read_patient_info()
        else:
            print("\nThe selected option is not in the menu")

elif (choose == 2):
    login()

    while True:
        print("\n1. Appointments management\n2. Patient Treatment Plan\n3. Extract Appointments management detail\n4. Extract Patient Treatment Plan detail\n5. Exit\n")
        menu = input("Choose any option from the menu:")
        choose = int(menu)

        if (choose == 1):
            appointment()

        elif (choose == 2):
            patient_treatment_plan()

        elif (choose == 3):
            read_again = open("appointment_plan.txt")
            extract = input("\nPlease input patient ID:")
            for each_line in read_again:
                (patient_id, appointment_id, specialist, status) = each_line.split()

                if patient_id == extract:
                    print(patient_id, appointment_id, specialist, status)
            read_again.close()

        elif (choose == 4):
            read_treatment_plan()

        elif(choose == 5):
            logout()

            break

        else:
            print("\nThe selected option is not in the menu")

elif (choose == 3):
    login()

else:
    print("Selected login type do not exist")



