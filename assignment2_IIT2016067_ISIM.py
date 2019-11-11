import math

def main():
    max_time = int(input())
    [XF, YF] = list(map(float, input().split(' ')))
    
    bomber_coordinates = []
    for i in range(max_time + 1) :
        B_i = list(map(float, input().split(' ')))
        bomber_coordinates.append(B_i)
    
    shooting_range = 10.0
    velocity = 20.0
    
    time = -1
    
    for i in range(max_time + 1) :
        dist = math.sqrt((XF - bomber_coordinates[i][0]) ** 2 + (YF - bomber_coordinates[i][1]) ** 2)
        if(dist <= shooting_range) :
            time = i
            break
        
        XF = XF + velocity * ((bomber_coordinates[i][0] - XF)/dist)
        YF = YF + velocity * ((bomber_coordinates[i][1] - YF)/dist)
        
    print(time)
    print("{0:.2f}".format(dist))

if __name__ == "__main__" :
    main()