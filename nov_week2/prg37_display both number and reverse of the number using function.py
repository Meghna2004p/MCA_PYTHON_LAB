def rev_no(num):
    reverse=0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse
def reverse_number():
    num=int(iput("enter a number with at least 4 digits"))
    if num<1000:
        print("the number must have atleast 4 digits")
        return
    rev_num=rev_no(num)
    print("original number:",num)
    print("reversed number:",rev_num)
reverse_number()
