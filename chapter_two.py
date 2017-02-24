"""
//chapter 2.
first_name = raw_input("Enter your first name: ");
last_name = raw_input("Enter your last name: ");
age = input("What is your age?: ");
print 'Hello', first_name, last_name;
print 'You are',age,'years old';


original_price = float(input("Enter the item's original price: "));
discount = original_price * 0.2;
sale_price = original_price - discount;

print "The sale price is",sale_price;

//2.
total_sale = float(input("Enter the projected amount of total sale: "));
annual_profit = total_sale *.23;
print "The total annual profit is:",annual_profit;

//3.
square_feet = float(input("Enter the amount of square footage: "));
acre = square_feet / 43560;
print square_feet,'square feet is equal to',acre,'acres';


//4.
item_one = float(input("Enter the price of the first item: "));
item_two = float(input("Enter the price of the second item: "));
item_three = float(input("Enter the price of the third item: "));
item_four = float(input("Enter the price of the fourth item: "));
item_five = float(input("Enter the price of the fifth item: "));
sub_total = item_one + item_two + item_three + item_four + item_five;
print 'Subtotal is:',sub_total;
sales_tax = .06
print 'Sales Tax:',sales_tax;
total = sub_total * (1 + sales_tax);
print 'Total with the sales tax:',total;

//5.
time_one = 5;
time_two = 8;
time_three = 12;
speed = 60;
distance_one = time_one *speed;
distance_two = time_two *speed;
distance_three = time_three *speed;
print "The distance of the will travel is",time_one,"hours:",distance_one;
print "The distance of the will travel is",time_two,"hours:",distance_two;
print "The distance of the will travel is",time_three,"hours:",distance_three;

//6.
purchase_amount = float(input("Enter the amount of a purchase: "));
state_sales_tax = purchase_amount * .04;
country_sales_tax = purchase_amount * .02;
total_sales_tax = state_sales_tax + country_sales_tax;
print "State sales tax is:",state_sales_tax;
print "Country sales tax is:",country_sales_tax;
print "Total sales tax:",total_sales_tax;
total_amount = purchase_amount + state_sales_tax + country_sales_tax;
print "Total amount:",total_amount;

//7.
miles_driven = float(input("Enter the miles driven:"));
gallons_of_gas = float(input("Enter the gallons of gas used:"));
MPG = miles_driven / gallons_of_gas;
print "The car's MPG is:", MPG;

//8.
charge = float(input("Enter the price of the food:"));
tip = .15;
total_tip = charge * tip;
print "Total tip is:",total_tip;
sales_tax = .07;
total_sales_tax = charge * sales_tax;
print "Sales Tax:",total_sales_tax;
total_amount = charge + total_tip + total_sales_tax;
print "Total amount is:",total_amount;

//9.
celsius = float(input("Enter the temperature:"));
farenheit = ((9 /5) * celsius) + 32;
print celsius,"degrees celsius is equal to",farenheit,"degrees farenheit";


//10.
num_of_stock = 1000;
first_stock_price = 32.87;
amount_paid = num_of_stock * first_stock_price;
first_commission = amount_paid * 0.02;
print "Amount paid:",amount_paid;
print "Stockbroker commission:",first_commission;

second_stock_price = 33.92;
amount_sold = num_of_stock * second_stock_price;
second_commission = amount_sold * 0.02;
print "Amount sold:", amount_sold;
print "Stockbroker commission for sold stock:",second_commission;

