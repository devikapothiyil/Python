
def cal_avg(phy,chem,maths):
    return (phy+chem+maths)/3

name=input("Enter your name:")
phy=int(input("Enter physics mark:"))
chem=int(input("Enter chemistry mark:"))
maths=int(input("Enter maths mark:"))
avg=round(cal_avg(phy,chem,maths),2)
print("Aveage marks is",avg)

report_card_content=f"""
REPORT CARD
------------
NAME:{name}
PHYSICS:{phy}
CHEMISTRY:{chem}
MATHS:{maths}
AVERAGE:{avg}
"""
print(report_card_content)

reportcard=f"{name}_reportcard.txt"

rp=open(reportcard,"w")
rp.write(report_card_content)
rp.close()



   
