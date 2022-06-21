accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    }

]

# #q1 details of acno 1002
#
# ac_details=[ac for ac in accounts if ac["acno"]==1002]
# print(ac_details)
#
# # q2 print savings type account
#
# savings_types=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
# print(savings_types)

#sort account based on balance ordered by desc

# accounts.sort(reverse=True,key=lambda bal:bal["balance"])
# print(accounts)

#print all phone pay transaction
all_trans=[ac["transactions"] for ac in accounts]
phone_paytrans=[trans for trans_list in all_trans for trans in trans_list if trans["method"]=="phone-pay"]
print(phone_paytrans)

#prit all transactions where transaction amount > 500

all_trans_amd=[amd for amd_lst in all_trans for amd in amd_lst if amd["amount"]>500]
print(all_trans_amd)


# credit transactions of 1002
credi_trans=[trans for trans_list in all_trans for trans in trans_list if trans["to"]==1002]
print(credi_trans )


#agregate transactions based on payment mode
pay_method_sum={}
all_trans = [ac["transactions"] for ac in accounts]
transations=[trans for trans_list in all_trans for trans in trans_list]
for trans in transations:
    pay_method=trans["method"]
    amd=trans["amount"]
    if pay_method in pay_method_sum:
        pay_method_sum[pay_method]+=amd
    else:
        pay_method_sum[pay_method]=amd
print(pay_method_sum)
print(max(pay_method_sum.items(),key=lambda iteam:iteam[1]))


