import sys
def draw_graph(test_input):
    graph_array=[[' 'for column in range(0,1000)] for row in range(0,100)]
    #create with column of 1000 and row of 100
    calculating_array=[test_input[i]*-1 if i%2==1 else test_input[i] for i in range(0,len(test_input))]
    #array from which maximum value will be calculated.
    max=calculating_array[0]
    sum=0 # the sum to calculate
    point=0 
    # getting the index of the maximum value to use when plotting the points
    for i in range(0,len(calculating_array)):
            # for loop to calculate the maximum value
            sum+=calculating_array[i]
            if max<sum:
                max=sum
                point=i # gets the index as the peak point for the x and y axis
    y_axis=len(graph_array)-50
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
            # creating the person who will sit at the top of the mountain
                graph_array[y_axis-1][x_axis-1]='<'
                graph_array[y_axis-2][x_axis-1]='/'
                graph_array[y_axis-2][x_axis]='|'
                graph_array[y_axis-2][x_axis+1]='\\'
                graph_array[y_axis-1][x_axis+1]='>'
                graph_array[y_axis-3][x_axis]='o'
            else:            
                for i in range(y_axis,y_axis-int(test_input[i]),-1): 
                    # if its not highest peak it will just plot the ascending line  
                    graph_array[i][x_axis]='/'
                    x_axis+=1
                    y_axis=i              
        elif i%2==1:
            # plots the descending line
            for i in range(y_axis,y_axis+int(test_input[i])):
                graph_array[i][x_axis]='\\'
                x_axis+=1
                y_axis=i

    with open('out.txt', 'w') as f:  #creates a file called output called out.txt and prints the output please look for the output in the txt file 
        sys.stdout = f 
        print('\n'.join(map(''.join, graph_array)))
    return None
if __name__=="__main__":
    test_case1=[10,7,12,2,4,7,2,4,1,2,6,6,3,2,1,4,7,2,7,3,1,3,11,4,2,1,5,2,3,3,3,6,1,3,9,5,2,1,2,11,9,2,3,8,2,5,1,2,7,2,4,9]
    draw_graph(test_case1)

