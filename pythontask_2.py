import sys
def draw_graph(test_input):
    total_x=sum(test_input)
    coordinates=[]
    graph_array=[[' 'for column in range(total_x+3)] for row in range(0,1000)]
    #create with column of 1000 and row of 100
    calculating_array=[test_input[i]*-1 if i%2==1 else test_input[i] for i in range(0,len(test_input))]
    #array from which maximum value will be calculated.
    max1=calculating_array[0]
    sum1=0 # the sum to calculate
    point=0 
    # getting the index of the maximum value to use when plotting the points
    for i in range(0,len(calculating_array)):
            # for loop to calculate the maximum value
            sum1+=calculating_array[i]
            if max1<sum1:
                max1=sum1
                point=i # gets the index as the peak point for the x and y axis
    y_axis=len(graph_array)-10
    #getting the y axis
    x_axis=0 
    # getting the x axis
    for i in range(0,len(test_input)):
        #for loop to iterate through all the values of the input array to plot the point
        if i%2==0: 
            # checking if its an even number as it will be ascending line
            if i==point:
                # this will plot the man at the highest peak
                for i in range(y_axis,y_axis-int(test_input[i]),-1):
                    graph_array[i][x_axis]='/'
                    x_axis+=1
                    y_axis=i
                    coordinates.append([x_axis,y_axis,'/'])
            # creating the person who will sit at the top of the mountain
                graph_array[y_axis-1][x_axis-1]='<'
                graph_array[y_axis-2][x_axis-1]='/'
                graph_array[y_axis-2][x_axis]='|'
                graph_array[y_axis-2][x_axis+1]='\\'
                graph_array[y_axis-1][x_axis+1]='>'
                graph_array[y_axis-3][x_axis]='o'
                coordinates.append([x_axis,y_axis-3,'o'])
            else:            
                for i in range(y_axis,y_axis-int(test_input[i]),-1): 
                    # if its not highest peak it will just plot the ascending line  
                    graph_array[i][x_axis]='/'
                    x_axis+=1
                    y_axis=i   
                    coordinates.append([x_axis,y_axis,'/'])  
                    #takes the coordinates for the top and bottom peaks        
        elif i%2==1:
            # plots the descending line
            for i in range(y_axis,y_axis+int(test_input[i])):
                graph_array[i][x_axis]='\\'
                x_axis+=1
                y_axis=i
                coordinates.append([x_axis,y_axis,'\\'])
    minimum_value=min(c[1] for c in coordinates)
    maximum=max(i[1] for i in coordinates)
    print('\n'.join(map(''.join, graph_array[minimum_value:maximum+1])))
    return None  
if __name__=="__main__":
   test_case1=[int(i) for i in input('Enter the number in your graph: ').split(' ')]
   draw_graph(test_case1)