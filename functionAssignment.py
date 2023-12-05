# Create a class and function, and list out the items in the list

class SubfieldsInAI:
           def Subfields():
            subfields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
            print("Sub-fields in AI are:")
            for subfield in subfields:
                print(subfield)

      
      
 # Create a function that checks whether the given number is Odd or Even
 
class OddEven:
    def OddEven():
        num=int(input("Enter a Number:"))
        if(num%2==1): 

            message=f"{num} is Odd Number"
        else:

            message=f"{num} is Even Number"
        return message
        
# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female

class ElegiblityForMarriage:
    def Elegible():
        Gender=str(input("Your Gender:"))
        Age=int(input("Your Age:"))
        if Gender=="Male"and Age==21:
            message="ELIGIBLE"
        elif Gender == "Female" and Age >= 18:
            message = "ELIGIBLE"
        else:
            message="NOT ELIGIBLE"
        return message
    
    
 # calculate the percentage of your 10th mark
 
class FindPercent:
    def percentage():
        subject1=int(input("Subject1: "))
        subject2=int(input("Subject2: "))
        subject3=int(input("Subject3: "))
        subject4=int(input("Subject4: "))
        subject5=int(input("Subject5: "))
        Total=subject1+subject2+subject3+subject4+subject5
        percentage=Total / 5
        print(f"Total: {Total}")
        print(f"Percentage: {percentage}")
        return percentage

#print area and perimeter of triangle using class and functions

class triangleClass:
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area formula=(Height*Breadth)/2
        print(f"Area formula: (Height * Breadth) / 2")
        Area of Triangle=Areaformula
        print(f"Area of Triangle :{AreaofTriangle}")
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter formula=Height1+Height2+Breadth
        print(f"Perimeter formula: Height1+Height2+Breadth")
        Perimeter of Triangle=Perimeter formula
        print(f"Perimeter of Triangle:{PerimeterofTriangle} ")




