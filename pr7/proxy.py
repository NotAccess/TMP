class Patient_Data_Manager:
    """ Real Subject"""
    def __init__(self):
        self.__patients = {}
        
    def _add_patients(self, patient_id, data):
        self.__patients[patient_id] = data
   
    def _get_patient(self, patient_id):
        Problem, Date = self.__patients[patient_id]
        return f"Name: {patient_id}, Problem: {Problem}, Date: {Date}"
class Access_Patient_Data(Patient_Data_Manager):
    """implimenting Proxy deisgn pattern Subject"""
    def __init__(self, fm):
        self.fm = fm
    
    def add_patients(self, patient_id, data, _password):
        if _password == '123456':
            self.fm._add_patients(patient_id, data)
        else:
            print("В доступе отказано.")
            
    def get_patient(self, patient_id, _password):
        if _password == '123456':
            return self.fm._get_patient(patient_id)
        else:
            print("В доступе отказано.")
obj = Access_Patient_Data(Patient_Data_Manager())
obj.add_patients('Джон', ['Сердечная недостаточность', '2022-12-11'], '123456')


print(obj.get_patient('Джон', '123456'))
obj2 = Access_Patient_Data(Patient_Data_Manager())
obj2.add_patients('Антон', ['Грипп', '2022-11-11'], '123456')
print(obj2.get_patient('Антон', '123456'))
obj3 = Access_Patient_Data(Patient_Data_Manager())
obj3.add_patients('Андрей', ['Здоров', '2022-11-11'], '12456')
print(obj3.get_patient('Андрей', '12356'))