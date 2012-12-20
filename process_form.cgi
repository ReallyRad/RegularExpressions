#!/usr/local/bin/python3

import cgi, re

def html_top():
    print("""Content-type:text/html\n\n
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8"/>
            </head>
            <body>""")

def html_tail():
    print("""    </body>
    </html>""")

def get_booking_details():
    form_data = cgi.FieldStorage()
    first_name = form_data.getvalue("first_name")
    last_name = form_data.getvalue("last_name")
    street = form_data.getvalue("street")
    town = form_data.getvalue("town")
    postcode = form_data.getvalue("postcode")
    phone = form_data.getvalue("phone")
    car = form_data.getvalue("car")
    date_in = form_data.getvalue("date_in")
    date_out = form_data.getvalue("date_out")
    return first_name, last_name,street, town, postcode, phone, car, date_in, date_out

def validate_form_field(field,regex):
    if re.match(regex,field,re.VERBOSE):
        return True
    else:
        return False

def validate_post_code(post_code):
    regex = """
                [A-Z]               #a single letter
                                    #followed by either:
                    (                   
                    [A-Z]           #an another letter
                                    #and either:
                        (
                        \d{1,2}     #one or two numbers
                        |           #or
                        \d[A-Z]     #a single number followed by a single letter
                        )   
                    |               #or
                    \d{1,2}         #one or two numbers
                    )
                \s\d                #space followed by a single number
                [A-Z]{2}$            #two letters
            """
    return validate_form_field(post_code,regex)

def validate_telephone_number(phone):
    regex = """\(0                   #open bracket followed by a zero
                                     #then either:
               (
                   1                 #1
                                     #followed by either:
                   (
                       \d{3}         #3 digits
                       \)            #close bracket
                       \s            #single space
                       \d{6}         #6 digits
                   |                 #or
                       (
                           \d1       #a single digit followed by a 1
                       |             #or
                           1\d       #a 1 followed by a single digit
                       )
                       \)            #a close bracket
                       \s            #a single space
                       \d{3}         #3 digits
                       \s            #a single space
                       \d{4}         #4 digits
                   )
               |                     #or
                   2\d\)             #2 followed by a digit and a close bracket
                   \s                #a single space
                   \d{4}             #4 digits
                   \s                #a single space
                   \d{4}             #4 digits
               )$"""
    return validate_form_field(phone,regex)

def validate_car_registration(car):
    regex = """
               [A-Z]            #single letter
                                #followed by either:
               (
                   (
                       [A-Z]    #single letter
                       \d{2}    #2 digits
                   |            #or
                       \d{1,3}  #between 1 and 3 digits
                   )
                                #followed by:
                   [A-Z]{3}     #3 letters
               |                #or
                   [A-Z]{2}     #two letters
                   \d{1,3}      #between 1 and 3 digits
                   [A-Z]?       #zero or one letters
               )$
            """

    return validate_form_field(car,regex)



#main program
if __name__ == "__main__":
    try:
        html_top()
        first_name, last_name, street, town, postcode,phone, car, date_in, date_out = get_booking_details()
        print("{0}<br/>".format(first_name))
        print("{0}<br/>".format(last_name))
        print("{0}<br/>".format(street))
        print("{0}<br/>".format(town))
        print("{0}, <b>post code is valid</b>: {1}<br/>".format(postcode,validate_post_code(postcode)))
        print("{0}, <b>phone number is valid</b>: {1}<br/>".format(phone,validate_telephone_number(phone)))
        print("{0}, <b>car registration is valid</b>: {1}<br/>".format(car,validate_car_registration(car)))
        print("{0}<br/>".format(date_in))
        print("{0}<br/>".format(date_out))
        html_tail()
    except:
        cgi.print_exception()
