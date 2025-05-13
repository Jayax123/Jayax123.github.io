def cap_af_space(word:float):
    pq = word.split()
    t = ""
    for nums in pq:
        t+=(f"{nums[0].upper()}{nums[1:].lower()} ")
    print(t[:-1])

def cap_af_period(word:float):
    pq = word.split('.')
    t = ""
    for nums in pq:
        t+=(f"{nums[0].upper()}{nums[1:].lower()} ")
    print(t[:-1])