import turtle

turtle.bgcolor("black")
tur= turtle.Turtle()

width = 5 
height = 7

dot_distance=25

tur.setpos(-250,250)
tur.color("white")

def spiral(m,n):
    k=0 #index of starting row
    l=0 #index of starting column
    f=0
    while k<m and l<n:
        if(f==1):
            tur.right(90)
        #printing first row
        for i in range(l,n):
            tur.forward(dot_distance)
        k+=1
        f=1
        tur.right(90)
        #printing last column
        for i in range(k,m):
            tur.forward(dot_distance)
        n-=1
        tur.right(90)
        #printing last row
        if(k<m):
            for i in range(n-1,l-1,-1):
                tur.forward(dot_distance)
            m-=1
            tur.right(90)
        #printing first column
        if(l<n):
            for i in range(m-1,k-1,-1):
                tur.forward(dot_distance)
            l+=1

spiral(20,20)