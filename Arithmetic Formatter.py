def arithmetic_arranger(equations,h=""):
    result=0
    for i in range(len(equations)):
        if(i<5):
            continue
        else:
            return 'Error: Too many problems.'
    for i in range(len(equations)):
        equation=equations[i].split()
        if ((str(equation[1])=='-')or(str(equation[1])=='+')):
            if((int(equation[0])<10000)and(int(equation[2])<10000)):
                if(str(equation[1])=='-'):
                    result=int(equation[0])-int(equation[2])
                    print(equation[0].rjust(7))
                    print(equation[1].ljust(0),equation[2].rjust(5))
                    print('-------'.rjust(4))
                    if (h==1):
                        print(str(result).rjust(7))
                        print('\t')
                else:
                    result=int(equation[0])+int(equation[2])
                    print(equation[0].rjust(7))
                    print(equation[1].ljust(0),equation[2].rjust(5))
                    print('-------'.rjust(4))
                    if (h==1):
                        print(str(result).rjust(7))
                        print('\t')
            else:
                return 'Error: Numbers cannot be more than four digits.'
        else:
            return 'Error: Operator must be "+" or "-".'
        
       
                

        
       
        
    

    
        
    

        
