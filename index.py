import time





def main():
    min = int(input("enter time: "))
    stopwatch(min)


def stopwatch(user):
    min = user * 60
    s = 60
    for x in range(min,-1,-1):
        time.sleep(1)
        m = int(x/60)
        s = s - 1
        print(m, " minutes and ", s, " seconds ")
        if s == 0:
            s = 60




main()