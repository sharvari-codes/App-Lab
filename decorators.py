def report_decorator(func):
    def wrapper(self):
        print("\n" + "=" * 40 )
        print("   MEDICAL REPORT")
        print("="*40)
        func(self)
        print("="*40)
    return wrapper 
    
class MedicalReport :
    def __init__(self,patient_name,age,disease,doctor_name):
        self.patient_name = patient_name 
        self.age  = age
        self.disease = disease 
        self.doctor_name = doctor_name 
        
    def __str__(self):
     return (
            f"Patient name : {self.patient_name}\n"
            f"Age : {self.age}\n"
            f"Disease : {self.disease}\n"
            f"Doctor_name : {self.doctor_name}\n"
        )
    @report_decorator
    def generate_report(self):
        print(self) 
                     
patient_name = input("Enter the patient name :") 
age = int(input("Enter the age of the patient :")) 
disease = input("Enter Disease :") 
doctor_name = input("Enter Doctor name:")   

report = MedicalReport(patient_name,age,disease,doctor_name)  
print("\n Generating MedicalReport..")
report.generate_report()
            
            