def calendar_calc():
    operating_date = date_processing()
    operating_date['year_type'] = leap_year(operating_date['year'])
    count_days_in_year(operating_date)
    check_february(operating_date)
    show_answer(operating_date)

def date_processing(date_option = 1):
    date_systems = ["YYYY/MM/DD, przykład 1381/07/04"]
    operating_date = {'year' : None, 'month' : None, 'day' : None}
    print("PODAJ DATĘ W FORMACIE", date_systems[date_option - 1])
    orginal_date_input = input("TWOJA DATA:")
    assert orginal_date_input.count('/') == 2,"nieprawidł•owa ilosc /"
    date_input = orginal_date_input.split('/')
    is_number(date_input)
    check_date_range(date_input)
    operating_date = set_operating_date(operating_date, date_input)
    operating_date['inputed date'] = orginal_date_input
    return operating_date

def set_operating_date(date,dinput, j = 0):
    for i in date.keys():
        date[i]=int(dinput[j])
        j+=1
    return date

def leap_year(year):
    leap = "rok nieprzestępny"
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        leap = "rok przestępny"
    return leap

def count_days_in_year(date):
    days_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    days_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
    date['days from first of january'] = int(0)
    
    if date['year_type'] == 'rok nieprzestępny':
        date['days in months'] = list(days_normal)
        date['sum days in year'] = int(365)
    else:
        date['days in months'] = list(days_leap)
        date['sum days in year'] = int(365)
    
    for i in range(len(date['days in months'])):
        if i+1 == date['month']:
            date['days from first of january'] += int(date['day'])
            break
        date['days from first of january'] += int(date['days in months'][i])
        print("dni od początku",date['days from first of january'])

def show_answer(operating_date):
    print("Twoja wprowadzona data :", operating_date['inputed date'],
          "\nluty ma", operating_date['days in months'][1], "dni bo",
          operating_date['year'],"to",operating_date['year_type'],
          "\nod początku",operating_date['year'],"roku minęło",
          operating_date['days from first of january'],"dni")

def is_number(date_input):
    for i in range(len(date_input)):
        assert date_input[i].isdigit(), "wprowadzaj tylko liczby oddzielone /"

def check_date_range(date_input):
    assert 0<len(date_input[0])<5,"zly zakres lat (0-9999)"
    assert "0"<date_input[1]<="12","zly zakres miesiecy(1-12)"
    assert "0"<date_input[2]<="31","zly zakres dni(1-31)"
    assert not(date_input[1] == '2' and ("0"<date_input[2]<="29")),"miesiąc luty ma zakres (1-29)"

def check_february(date):
    assert date['day'] <= date['days in months'][1],"podany dzień przekracza ilosć dni w lutym"
    
def main():
    calendar_calc()
    return 0

if __name__ == "__main__":
    main()

