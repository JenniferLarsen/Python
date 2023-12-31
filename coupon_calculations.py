"""
Program: coupon_calculations.py
Author: Jennifer Larsen
Last date modified: 09/12/2023
The purpose of this program is to calculate the total price minus discounts plus tax of purchases.
The input are integers representing amount of purchase, cash coupon, percent coupon.
The output is the total order price.
"""

"""You are online shopping at SuperAwesomeCouponDealsAndStuff.com. They offer two types of discounts, cash-off coupons and percent discount coupons. You must add tax after applying coupons. If you have cash-off coupons, those must be applied first, then apply the percent discount coupons on the pre-tax amount.

The following is the order of calculations: 

The first is cash-off coupons, that you earn by shoppings. You may apply one $5 or $10 cash off per order.
The second is percent discount coupons for 10%, 15%, or 20% off.
The third is tax according to the the following guidelines:
up to $10 dollars, shipping is $5.95
$10 and up to $30 dollars, shipping is $7.95
$30 and up to $50 dollars, shipping is $11.95
Shipping is free for $50 and over
In this program, prompt the user for the the amount of the purchase, the cash coupon, the percent coupon. Then calculate and return the total order item.

For instance, you have $5 off and 30% coupons and your item is $15.99, you will first take

$15.99 - $5.00 = $10.99.
30% off $10.99 to get $7.69
Add tax at 6% to get $8.15
Add shipping cost before tax $5.95 to get $14.10  #(Assuming this means add shipping after tax - JLL)
Do not forget to use variables and constants where appropriate. Using varialabes, the first line might look like the following: 

cash_off_subtotal = price - cash_off 
Name your file coupon_calculations.py.  """

import decimal


TAX_PERCENTAGE = .06

purchase_amount = float(input ("Please enter the amount of your purchase: $ "))
cash_coupon = float(input("Please enter Cash coupon amount $(5, or 10): "))
percent_coupon = float(input("Please enter Percent off amount %(10, 15, or 20): "))

cash_off_subtotal = purchase_amount - cash_coupon
percent_off_subtotal = cash_off_subtotal - (cash_off_subtotal * (percent_coupon/100))
subtotal_with_tax = percent_off_subtotal  + (percent_off_subtotal * TAX_PERCENTAGE)

if 50 < subtotal_with_tax > 0:
    if 0 < subtotal_with_tax <= 10:
        shipping_amount = 5.99
    elif 10 < subtotal_with_tax <= 30:
        shipping_amount = 7.95
    elif 30 < subtotal_with_tax <= 50:
        shipping_amount = 11.95
else:
    shipping_amount = 0

total_price = subtotal_with_tax + shipping_amount

print(f"Total price including tax and shipping is: {total_price: .2f}.")



