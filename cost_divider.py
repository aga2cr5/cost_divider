#!/usr/bin/env python3

# put here names of the people who are sharing the costs and how much they have paid
kollektiivi = {
    "name1": 168.30,
    "name2": 99.0,
    "name3": 0,
    "name4": 0
}

# all paid amounts summed up
total = sum(kollektiivi.values())

# single share amount
share = total / 4

# calculates how much is the total sum left to be paid by those who's payments did not cover their share
total_left = total - share * len([ member for (member, paid) in kollektiivi.items() if paid > share ])

# calculates how much each member should be paid (if they should) and how much the amount is from the total_left amount
should_get = { member:[ paid - share, (paid - share) / total_left if (paid - share) > 0.0 else 0.0 ] for (member, paid) in kollektiivi.items() }

# calculates who needs to still pay and how much of their share is to be payed to whome
who_pays_who = { member: { recipient: recipient_info[1] * abs(payer_info[0]) for (recipient, recipient_info) in should_get.items() if recipient_info[1] > 0 } for (member, payer_info) in should_get.items() if payer_info[0] < 0 }

# prints out who pays who and what
for (payer, recipients) in who_pays_who.items():
    print("{:} pays the following to:".format(payer))
    for (getter, amount) in recipients.items():
        print("\t{:}: {:}€".format(getter, round(amount, 2)))
    print("\n")
