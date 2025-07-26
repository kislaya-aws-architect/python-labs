'''
Suppose this is a value of a list
spam =['apples','bananas','Mangoes','Tomatoes']
The output has to be 'apples,bananas,Mangoes and Tomatoes'

The input is further optimized to accept both strings and integers
'''
def returnwithand(somelist):
    assimilated =''
    for i in range(len(somelist)):
        if i != (len(somelist)-1):
            assimilated = assimilated + somelist[i]+','
        else:
            assimilated = assimilated + ' and '+ somelist[i]
    print(assimilated)

try:
   UserInput = input("Do you want to enter strings(1) or Integers(2), press 1 or 2:")
   if UserInput == '1':
       user_input_list=input("Enter strings with spaces as delimiters").split()
   elif UserInput == '2':
        user_input_list = list(map(int,input("Enter numbers with spaces as delimiters").split()))
   else:
        raise ValueError("Invalid choice. Please enter 1 or 2.")
   if user_input_list:
       returnwithand(user_input_list)

except ValueError as ve:
    print(f"Error: {ve}")