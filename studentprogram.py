
import studentclass as sc

studentid = 1001
name = 'John'
dob = '1/1/2000'
classification = 'Junior'

# create instance called john
john = sc.Student(studentid, name, dob, classification)

# don't need to give it any parameters because it's not expecting any. We are already doing that when we create the instance
john.calc_age()

john.register()


print("Student age is:", john.get_age())

print("Student can register beween:", john.get_registration())