import csv
import matplotlib.pyplot as plt

class Employee:
    """models an Employee record."""
    def __init__(self, first_name, last_name, email, years):
        self.first_name=first_name
        self.last_name=last_name
        self.email = email
        self.years = years

    #TODO1: make this class comparable.
    def __eq__(self,a):
        if self.first_name == a.first_name and self.last_name == a.last_name and self.years == a.years and self.email == a.email:
            return True
        else:
            return False
    
    def __lt__(self, oEmployee):
        if self.first_name == oEmployee.first_name and self.last_name == oEmployee.last_name and self.years == oEmployee.years and self.email == oEmployee.email:
            return False
        elif self.last_name != oEmployee.last_name:
            if self.last_name[0] > oEmployee.last_name[0]:
                return False
            elif self.last_name[0] < oEmployee.last_name[0]:
                return True
        elif self.first_name != oEmployee.first_name:
            if self.first_name[0] > oEmployee.first_name[0]:
                return False
            elif self.first_name[0] < oEmployee.first_name[0]:
                return True
        elif self.years != oEmployee.years:
            if self.years > oEmployee.years:
                return True
            if self.years < oEmployee.years:
                return False

    def __str__(self):
        info_str = f'{self.first_name} {self.last_name} {"email:"} {self.email}' \
                    f' {"years:"} {self.years}' 
        return(info_str)  

class EmployeeDataProcessor:

    def __init__(self, data_list=None):
        self.data_list = []

    #TODO2: implement this method.
    def get_data_list_from_csvfile(self, file_name):
        """This method opens the csv file passed in and 
            creates an Employee object for each row of data
            in the file. It appends each object to a list and 
            returns that list."""
        employee_list = []
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    employee_list.append(Employee(row[0],row[1],row[2],int(row[3])))
                    line_count += 1
        return employee_list



    def initialize(self, file_name):
        self.data_list = self.get_data_list_from_csvfile(file_name)

    def get_data_size(self):
        return len(self.data_list)

    #TODO3: implement this method.
    def get_employee_record(self, first_name, last_name, years):
        """Returns the first Employee object in the data_list that
           matches first_name, last_name, and years.
           Returns None if the record is not found."""
        for items in self.data_list:
            if items.first_name == first_name and items.last_name == last_name and items.years == years:
                return items
        




    #TODO4: implement this method.
    def get_employee_list(self, start, end, sorted=False):
        """ Returns a list of employee object from data_list that fall
            within a specific range as specified by start and end index parameters.
            The value of start can be: 0<= start < end.
            The value of end can be: start < end <= length of data_list.
            An Exception is raised if start and end values do not meet these constraints.
            Note that start and end are list indexes, and you should return Objects from start to end -1, 
            so the end index is not included in the range.
            Example:
            start 0, end 5
            first employee:  'hbartczak0@squidoo.com'
            last employee:  'bbamell4@cafepress.com'
            The list is returned in ascending order if the sorted parameter is True,
            unsorted otherwise (default)."""
        if not 0 <= start < end or not start < end <= len(self.data_list):
            raise Exception('ur uggo dumb dumb')
        un_sorted = self.data_list[start:end]
        if sorted == False:
            return un_sorted
        if sorted == True:
            n = len(un_sorted)
            for i in range(n):
                for j in range(n-1):
                    if un_sorted[j] > un_sorted[j+1]:
                        un_sorted[j], un_sorted[j+1] = un_sorted[j+1], un_sorted[j]
            return un_sorted






    #TODO5: implement this method.
    def get_years_list(self):
        """Returns a list that contains only the years from 
            all records on the data_list."""
        t = []
        for items in self.data_list:
            t.append(items.years)
        return t





    def plot_emp_years(self):
        """Creates and displays a histogram plot of all of the years
            that employees in data_list have worked."""
        data = self.get_years_list()
        #specify bin start and end points
        bin_ranges = [0,1,2,3,4,5,6,7,8,9,10]
        #create histogram with 4 bins
        plt.hist(data, bins=bin_ranges, edgecolor='black')
        plt.title("Years of Employment")
        plt.xlabel("Years")
        plt.ylabel("Frequency")
        plt.show()   

if __name__=="__main__":
    #file_name = "employee_data.csv"
    file_name = "test.csv"
    emp_proc = EmployeeDataProcessor()
    emp_proc.initialize(file_name)
    #emp_proc.plot_emp_years()
