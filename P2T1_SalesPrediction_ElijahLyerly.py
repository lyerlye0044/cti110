# Write a program that asks the user to enter the
# projected amount of total sales, and then displays the
# profit that will be made from that amount.
# 02-11-19
# CTI-110 P2T1 - Sales Prediction
# Elijah Lyerly
#

totalsales = float(input('Total sales: '))
profit = totalsales*0.23 
print('Annual profit: $', \
      format(profit, ',.2f'), \
      sep='')
