class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    def __init__(self,bottoml,topr,color):
        ''' (Point,str,number, number) -> None
        initialize point coordinates of bottom left and top right corners and colour''' 
        self.bottoml=bottoml
        self.topr=topr
        self.color=color
    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns bottom left point of Rectangle
        '''
        return self.bottoml

    def get_top_right(self):
        '''(Rectangle)->Point
        Returns top right point of Rectangle
        '''
        return self.topr

    def get_color(self):
        '''(Rectangle)->str
        Returns colour of Rectangle
        '''
        return self.color

    def reset_color(self,newcol):
        ''' (Rectangle,str)-> None
        Changes colour of Rectangle 
        '''
        self.color=newcol

    def move(self,dx,dy):
        '''(Rectangle,number,number)->None
        changes the x and y coordinates by dx and dy
        '''
        self.bottoml.move(dx,dy)
        self.topr.move(dx,dy)

    def get_perimeter(self):
        '''(Rectangle)-> number
        Computes perimeter of Rectangle
        '''
        bott=self.bottoml.get()
        top=self.topr.get()
        width=top[0]-bott[0]
        leng=top[1]-bott[1]
        peri=(2*width)+(2*leng)
        return peri

    def get_area(self):
        '''(Rectangle)-> number
        Computes area of Rectangle 
        '''
        bott=self.bottoml.get()
        top=self.topr.get()
        width=top[0]-bott[0]
        leng=top[1]-bott[1]
        area=leng*width
        return area

    def __eq__(self,other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the same coordinates
        '''
        return self.bottoml == other.bottoml and self.topr == other.topr

    def contains(self,x,y):
        '''(Rectangle,number,number)-> bool
        Returns True if the given point is inside Rectangle
        '''
        bott=self.bottoml.get()
        top=self.topr.get()
        return x>=bott[0] and x<=top[0] and y>=bott[1] and y<=top[1]

    def intersects(self,other):
        '''(Rectangle,Rectangle)-> bool
        Returns True if the Rectangles share a point
        '''
        bott2=other.bottoml.get()
        top2=other.topr.get()
        bott1=self.bottoml.get()
        top1=self.topr.get()
        return top1[0]>=top2[0] or top1[0]<=top2[0] or top1[1]>=top2[1] or top1[1]<=top2[1] or bott1[0]>=bott2[0] or bott1[0]<=bott2[0] or bott1[1]>=bott2[1] or bott1[1]<=bott2[1]

    def __str__(self):
        '''(Point)->str
        Returns nice string representation of Rectangle.
        '''
        return 'I am a '+str(self.color)+' rectangle with bottom left corner at '+str(self.bottoml.get())+' and top right corner at '+str(self.topr.get())+'.'

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Rectangle(Point(), Point(), colour)'''
        return 'Rectangle('+str(self.bottoml)+','+str(self.topr)+','+str(self.color)+')'
    
class Canvas:
    def __init__(self,rectangle=[]):
        '''(Canvas)->None
        initializes collection of Rectangles
        '''
        self.rect=rectangle
    def __len__(self):
        '''(Canvas)->None
        Returns length of list 
        '''
        try:
            return len(self.rect)
        except:
            return 0 
    def add_one_rectangle(self,rectangle2):
        '''(Canvas,Rectangle)->None
        Appends new rectangle to list of Rectangles
        '''
        self.rect2=rectangle2
        self.rect.append(self.rect2)

    def count_same_color(self,colour):
        '''(Canvas,str)->number
        Returns count of Rectangles with same colour
        '''
        count=0
        colorlist=[]
        for j in self.rect:
            colors= j.get_color()
            colorlist.append(colors)
        for k in colorlist:
            if k == colour:
                count=count+1
        return count

    def total_perimeter(self):
        '''(Canvas)->number
        Computes total perimeter of all Rectangles
        '''
        total=0
        for i in self.rect:
            peri=i.get_perimeter()
            total=total+peri
        return total
    def min_enclosing_rectangle(self):
        '''(Canvas)-> Rectangle
        returns Rectangle that encloses all rectangles in Canvas
        '''
        xmin=[]
        ymin=[]
        xmax=[]
        ymax=[]
        for i in self.rect:
            bottom=i.get_bottom_left()
            top=i.get_top_right()
            bottom2=bottom.get()
            top2=top.get()
            for j in top2:
                xmax.append(top2[0])
                xmax.sort()
            for m in top2:
                ymax.append(top2[1])
                ymax.sort()
            for k in bottom2:
                xmin.append(bottom2[0])
                xmin.sort()
            for z in bottom2:
                ymin.append(bottom2[1])
                ymin.sort()
        return 'Rectangle(Point('+str(xmin[0])+','+str(ymin[0])+'),Point('+str(xmax[-1])+','+str(ymax[-1])+'), "blue")'                         

    def common_point(self):
        '''(Rectangle)->bool
        Returns boolean value of existance of common point in Canvas 
        '''
        results=[]
        for i in self.rect:
            for j in self.rect:
                boole=i.intersects(j)
                results.append(str(boole))
        if boole=='False':
            return False
        else:
            return True 

    def __repr__(self):
        ''' (Canvas)-> str
        Returns canonical string representation of Canvas
        '''
        return 'Canvas'+str(self.rect)+''
        
        

