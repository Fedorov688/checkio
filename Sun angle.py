def sun_angle(time):
    #replace this for solution
    time = time.split(":")
    min_angle = 360 / (24 * 60)
    correction = 6*60
    minutes = int(time[0]) * 60 + int(time[1])
    if 6*60-1<minutes<18*60+1:
        result = min_angle * (minutes - correction)
    else:
        result = "I don't see the sun!"
    return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
