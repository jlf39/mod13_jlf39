import datetime

def main():
    x=symbolSelect()
    y=timeSeriesSelect()
    z=chartTypeSelect()
    ax=datesSelect()
    print(x,y,z,ax)

def symbolSelect():
    check = False
    while check == False:
        answer = input("Enter the stock symbol for the company: \n------------\n:")
        if (answer.isupper() == True and answer.isalpha()==True and len(answer)<=7):
            check=True
        else:
            check=False
    return answer
def timeSeriesSelect():
    check=False
    while check==False:
        answer = input("Enter the time series function you want the api to use: \n------------\n1.Intraday\n2.Daily\n3.Weekly\n4.Monthly\n------------\n:")
        if answer == "1" or answer == "2" or answer == "3" or answer == "4":
            check=True
        else:
            check=False
    return answer

    
def chartTypeSelect():
    check=False
    while check==False:
        answer = input("Enter the chart type you want the api to use: \n------------\n1.line\n2.bar\n------------\n:")
        if answer == "1" or answer == "2":
            check=True
        else:
            check=False
    return answer


def datesSelect():
    check=False
    check1=False
    while check==False:
        check1=False
        while check1 == False:
            answer1 = input("Enter the beginning date (Format:YYYY-MM-DD): ")
            answer2 = input("Enter the end date (Format:YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(answer1, '%Y-%m-%d')
                datetime.datetime.strptime(answer2, '%Y-%m-%d')
            except ValueError:
                check1=False
                print("Incorrect format try again \n")
            else:
                check1=True
        x = int(answer1[0:4])
        x1 = int(answer1[5:7])
        x2 = int(answer1[8:10])
        x3 = int(answer2[0:4])
        x4 = int(answer2[5:7])
        x5 = int(answer2[8:10])
        #print(x,x1,x2,x3,x4,x5)
        years = x3-x
        months = x4-x1
        days = x5-x2
        #print(days,months,years)
        total=((years*365)+(months*30)+(days))
        if total>=0:
            check=True
        else:
            print("\nStart date must be before end date, try again: \n")
            check=False
    return answer1,answer2
main()
