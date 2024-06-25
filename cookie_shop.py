"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""
import csv

def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    cookies_list=[]
    with open(filepath,"r") as csvfile:
        cookies_csv=csv.reader(csvfile)
        for line in cookies_csv:
           if line[0].isdigit()==True:
               cookie_dict={"id": int(line[0]),"title": line[1],"description": line[2],"price": float(line[3][1:])}
               cookies_list.append(cookie_dict)
    return cookies_list
           


def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.")


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:")
    print("")
    for cookie_type in cookies:
        cookie_id=cookie_type["id"]
        cookie_title=cookie_type["title"]
        cookie_description=cookie_type["description"]
        cookie_price=cookie_type["price"]
        print("#"+str(cookie_id)+" - "+str(cookie_title))
        print(str(cookie_description))
        if len(str(cookie_price))==4:
           print("Price: $"+str(cookie_price))
        elif len(str(cookie_price))==3:
            print("Price: $"+str(cookie_price)+"0")
        print("")


def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    for line in cookies:
        if len(str(line["price"]))==3:
            line["price"]=format(line["price"],".2f")
    for cookie_type in cookies:
        if cookie_type["id"]==id:
            return cookie_type


def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line
    cookie_dict=get_cookie_from_dict(id,cookies)
    cookie_title=cookie_dict["title"]
    cookie_price=cookie_dict["price"]
    whether_valid=0
    while whether_valid<1:
        cookie_num=input("My favorite! How many "+str(cookie_title)+" would you like? ")
        if cookie_num.isdigit()==True and int(cookie_num)>0:
            whether_valid+=1
            cookie_subtotal=format(int(cookie_num)*float(cookie_price),".2f")
            print("Your subtotal for "+str(cookie_num)+" "+str(cookie_title)+" is $"+str(cookie_subtotal))
            return int(cookie_num)
        else:
            whether_valid=whether_valid






def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    whether_finish=0
    order_list=[]
    while whether_finish<1:
        user_id=input("enter the id of a cookie you want to order: ")
        if user_id.isdigit()==True and int(user_id)>=1 and int(user_id)<=10:
            user_quantity=solicit_quantity(int(user_id),cookies)
            order_list.append({"id": int(user_id),"quantity": user_quantity})
        else:
            if user_id in ["finished","done","quit","exit"]:
                whether_finish+=1
    return order_list
        

        
def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    print("Thank you for your order. You have ordered:")
    print("")
    total_cost=0
    for dict in order:
        order_id=dict["id"]
        order_quantity=dict["quantity"]
        order_info=get_cookie_from_dict(int(order_id),cookies)
        order_title=order_info["title"]
        order_price=order_info["price"]
        one_cost=int(order_quantity)*float(order_price)
        total_cost+=one_cost
        print("-"+str(order_quantity)+" "+str(order_title))
    total_cost=format(total_cost,".2f")
    print("")
    print("Your subtotal is $"+str(total_cost)+".")
    print("Please pay with Bitcoin before picking_up.")
    print("")
    print("Thank you!")
    print("-The Python Cookie Shop Robot.")




def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
