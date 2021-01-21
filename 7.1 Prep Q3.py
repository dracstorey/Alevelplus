## lists populated with test data
school = ["Alleyns","Brighton College","Colfes","Dulwich"]
medal = [4,7,1,3]

## Function adds a medal to the list and returns the value
def medal_update(sch):
    medal[sch-1] = medal[sch-1] + 1
    return medal[sch-1]
## End function

##Main program
## Set loop to true
done = 0
## While loop is true
while done == 0:
    ## input a school number
    sch = int(input("Enter school betwene 1 and 4: 99 will exit"))
    ## Test school value is between 1 and 4
    if sch >0 and sch < 5:
        ## Add a medal to the school 
        new_medals = medal_update(sch)
        print ("School number ", sch, " School name ", school[sch-1], " number of medals ", new_medals)
    else:
        ## 99 is the exit value
        if sch == 99:
            done = 1
        else:
            ## Prompt for correct value
            print ("Try a number between 1 and 4")
        ## End if
    ## End if
## End while




