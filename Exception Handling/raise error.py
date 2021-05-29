''' we can also raise error '''
def increment(num):
    try :
        return int(num)+1
    except:
        raise ValueError("Enter numeric value")


print(increment('df364'))