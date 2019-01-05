def arithmetic_seq(f_term,c_diff,nth_term):
    nth_number = f_term + ((nth_term - 1)*c_diff)
    print("\nThe First term is               :",f_term)
    print("The Common Difference is        :",c_diff)
    print("The ",nth_term,"term of this sequence is:",nth_number)

f_term = int(input("Please enter the First Term             :"))
c_diff = int(input("Please enter the Common Difference      :"))
nth_term=int(input("Please enter the number of term to find :"))
arithmetic_seq(f_term,c_diff,nth_term)

bool = input("\nDo you want to continue (yes/no) ? ")

while bool=='yes':
    nth_term=int(input("\nPlease enter the number of term to find :"))
    arithmetic_seq(f_term,c_diff,nth_term)
    bool = input("\nDo you want to continue (yes/no) ? ")
else:
    print("The End.")
