
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Reading in the file using a dynamic location
dirName = os.path.dirname(__file__)
absFileName = os.path.join(dirName, r'QueryWithDemographicsNoNullsAdditionalQuestions.xlsx')
df = pd.read_excel(absFileName)

# Data frame for column headers and the renaming to a relevant question description
df.rename(
    columns={
        "q1": "age", "q2": "sex", "q3": "grade", "q6": "height", "q7": "weight", "q47": "marijuana", 
        "q50": "cocaine", "q52": "heroin", "q53": "meth", "q54": "ecstasy"
        }, 
    inplace=True
)

# Data frames stored as variables
age = df["age"]
sex = df["sex"]
grade = df["grade"]
height = df["height"]
weight = df["weight"]
marijuana = df["marijuana"]
cocaine = df["cocaine"]
heroin = df["heroin"]
meth = df["meth"]
ecstasy = df["ecstasy"]

def heatmap():
    df_num = df.drop(columns=["grade"])
    plt.rcParams.update({'font.size': 8})
    plt.rcParams['figure.facecolor'] = 'xkcd:salmon'
    plt.figure(figsize=(12, 7),dpi=100)
    sns.heatmap(df_num.corr(),annot=True,vmin=0,vmax=1,cmap="viridis")
    plt.show()
def piechart():
    labels1 = ["No Usage","Marijuana User"]
    labels2 = ["No Usage","Illegal Drugs User"]
    labels3 = ["No Usage","Marijuana User","Illegal Drugs User","Marijauna and Illegal Drugs User"]
    labels4 = ["Marijuana User", "Marijauna and Illegal Drugs User"]
    pielist1 = [0,0]
    pielist2 = [0,0]
    pielist3 = [0,0,0,0]
    pielist4 = [0,0]
    for i in range(0,len(marijuana)):
        if marijuana[i]==1 and cocaine[i]==1 and heroin[i]==1 and meth[i]==1 and ecstasy[i]==1: # uses no drugs or marijuana
            pielist1[0]+=1
            pielist2[0]+=1
            pielist3[0]+=1
        elif marijuana[i]>1 and (cocaine[i]>1 or heroin[i]>1 or meth[i]>1 or ecstasy[i]>1): # use marijuana and illegal drugs
            pielist3[3]+=1
            pielist4[1]+=1
        elif marijuana[i]>1: # only use marijuana
            pielist1[1]+=1
            pielist3[1]+=1
            pielist4[0]+=1
        elif cocaine[i]>1 or heroin[i]>1 or meth[i]>1 or ecstasy[i]>1: # only use illegal drugs(not marijuana)
            pielist2[1]+=1
            pielist3[2]+=1
    pietotal1 = pielist1[0]+pielist1[1]
    pietotal2 = pielist2[0]+pielist2[1]
    pietotal3 = pielist3[0]+pielist3[1]+pielist3[2]+pielist3[3]
    pietotal4 = pielist4[0]+pielist4[1]
    # replacing values with percentages in the lists for easy data input later
    pielist1[0] = (pielist1[0]/pietotal1)*100
    pielist1[1] = (pielist1[1]/pietotal1)*100
    pielist2[0] = (pielist2[0]/pietotal2)*100
    pielist2[1] = (pielist2[1]/pietotal2)*100
    pielist3[0] = (pielist3[0]/pietotal3)*100
    pielist3[1] = (pielist3[1]/pietotal3)*100
    pielist3[2] = (pielist3[2]/pietotal3)*100
    pielist3[3] = (pielist3[3]/pietotal3)*100
    pielist4[0] = (pielist4[0]/pietotal4)*100
    pielist4[1] = (pielist4[1]/pietotal4)*100
    # size of subplot/figure area
    fig = plt.figure(figsize=(18,10), dpi=100)
    plt.rcParams.update({'font.size': 8})
    plt.rcParams['figure.facecolor'] = 'xkcd:salmon'
    #first row, first column
    ax1 = plt.subplot2grid((2,2),(0,0))
    plt.pie(pielist1, explode=[0,0.2], startangle=90, colors=["lightblue","green"])
    plt.title("Usage of Marijuana",fontsize=16)
    labels = [f"{labels1[0]} ({pielist1[0]:0.1f}%)",f"{labels1[1]} ({pielist1[1]:0.1f}%)"]
    ax1.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    #first row sec column
    ax2 = plt.subplot2grid((2,2), (0, 1))
    plt.pie(pielist2, explode=[0,0.2], startangle=90, colors=["lightblue","red"])
    plt.title("Usage of Illegal Drugs",fontsize=16)
    labels = [f"{labels2[0]} ({pielist2[0]:0.1f}%)",f"{labels2[1]} ({pielist2[1]:0.1f}%)"]
    ax2.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    #Second row first column
    ax3 = plt.subplot2grid((2,2), (1, 0))
    plt.pie(pielist3, explode=[0.2,0,0,0], startangle=90, colors=["lightblue","green","red","yellow"])
    plt.title("Usage of Marijuana and Illegal Drugs",fontsize=16)
    labels = [f"{labels3[0]} ({pielist3[0]:0.1f}%)",f"{labels3[1]} ({pielist3[1]:0.1f}%)",
              f"{labels3[2]} ({pielist3[2]:0.1f}%)",f"{labels3[3]} ({pielist3[3]:0.1f}%)"]
    ax3.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    #second row second column
    ax4 = plt.subplot2grid((2,2), (1, 1))
    plt.pie(pielist4, explode=[0,0.2], startangle=90, colors=["green","yellow"])
    plt.title("Marijuana VS Illegal Drugs",fontsize=16)
    labels = [f"{labels4[0]} ({pielist4[0]:0.1f}%)",f"{labels4[1]} ({pielist4[1]:0.1f}%)"]
    ax4.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    # show graph
    fig.tight_layout()
    plt.show()
def barchart():
    
    # Counters of users of specific drugs and drug combinations
    counter_m = 0
    for users in marijuana:
        if users != 1:
            counter_m += 1
        
    counter_c = 0
    for users in cocaine:
        if users != 1:
            counter_c += 1 
    
    counter_h = 0
    for users in heroin:
        if users != 1:
            counter_h += 1 
    
    counter_me = 0
    for users in meth:
        if users != 1:
            counter_me += 1 
            
    counter_e = 0
    for users in ecstasy:
        if users != 1:
            counter_e += 1         
    
    counter_mc = 0
    for i in range(0, len(marijuana)):
            if marijuana[i] > 1 and cocaine[i] > 1:
                counter_mc += 1
    
    counter_mh = 0
    for i in range(0, len(marijuana)):
            if marijuana[i] > 1 and heroin[i] > 1:
                counter_mh += 1
    
    counter_mm = 0
    for i in range(0, len(marijuana)):
            if marijuana[i] > 1 and meth[i] > 1:
                counter_mm += 1
    
    counter_mec = 0
    for i in range(0, len(marijuana)):
            if marijuana[i] > 1 and ecstasy[i] > 1:
                counter_mec += 1
    
    # Counters for totals of specific drug usage
    counter_m_illegal = counter_mc + counter_mh + counter_mm + counter_mec
    counter_m_only = counter_m - counter_m_illegal
    counter_percent = str(round(counter_m_illegal / counter_m_only, 2)).replace('0.', '')
    
    # Parameters for graphs to be uniform with one another in text size and background color
    plt.rcParams.update({'font.size': 8})
    plt.rcParams['figure.facecolor'] = 'xkcd:salmon'
    
    # Drug use graph
    plt.figure(figsize=(12, 7),dpi=100)
    x_axis = ['Marijuana', 'Cocaine', 'Heroin', 'Meth', 'Ecstacy']
    y_axis = [counter_m, counter_c , counter_h , counter_me , counter_e]
    plt.bar(x_axis, y_axis, color = (0.1 , 0.5 , 0.2 , 0.6))
    plt.title('Drug Use YRBS 2021', color = 'black')
    plt.xlabel('Questions', color = 'black')
    plt.ylabel('Number Of Users', color = 'black')
    plt.show()
    
    # Combined Usage
    plt.figure(figsize=(12, 7),dpi=100)
    x_axis = ['Marijuana Alone', 'M w/ Cocaine', 'M w/ Heroin', 'M w/ Meth', 'M w/ Ecstacy']
    y_axis = [counter_m_only, counter_mc , counter_mh , counter_mm , counter_mec]
    
    plt.bar(x_axis, y_axis, color = (0.1 , 0.5 , 0.2 , 0.6))
    plt.title('Marijuana Usage With Another Drug')
    plt.xlabel('Questions')
    plt.ylabel('Number Of Users')
    plt.show()
    
    # Drug Use Combined Overall
    plt.figure(figsize=(12, 7),dpi=100)
    x_axis = ['Marijuana Alone', 'Marijuana with Another Drug']
    y_axis = [counter_m_only, counter_m_illegal]
    plt.bar(x_axis, y_axis, color = (0.1 , 0.5 , 0.2 , 0.6))
    plt.title('Marijuana Usage With Another Drug')
    plt.xlabel('Questions')
    plt.ylabel('Number Of Users')
    plt.show()
    
    # Additional Statistics to accompany graph printed to console for quick reference
    print(f'\n\nMarijuana Users: {counter_m}')
    print(f'Cocaine Users: {counter_c}')
    print(f'Heroin Users: {counter_h}')
    print(f'Meth Users: {counter_me}')
    print(f'Ecstacy Users: {counter_e}')
    print('--------------------------------------------------------------------------------------')
    print(f'Marijuana with Cocaine Users: {counter_mc}')
    print(f'Marijuana with Heroin Users: {counter_mh}')
    print(f'Marijuana with Meth Users: {counter_mm}')
    print(f'Marijuana with Ecstacy Users: {counter_mec}')
    print('--------------------------------------------------------------------------------------')
    print(f'Marijuana Only: {counter_m_only}')
    print(f'Marijuana with Any Other Illicit Drug Users: {counter_m_illegal}')
    print('--------------------------------------------------------------------------------------')
    print(f'Percentage of users that use other illegal drugs along with marijuana: {counter_percent}%')

choice_list = ('heatmap', 'bar graph', 'pie chart', 'all')
choice = ''

print('\n\nWelcome to our program that explores the Youth Risk Behavior System\'s '
      'data set. This program is designed to explore the correlation and tendencies '
      'of youth who use Marijuana and other illegal drugs, as well as how they relate '
      'to each other.')
print('------------------------------------------------------------------------------------------')

# Overarching while loop that does not break until user inputs they would no longer like to continue
while True:
    # Inner while loop to solicit input from the user as to which graph they would like to see
    while True:
        print('\nWhat graph would you like to see?')
        choice = input('(Please enter Heatmap, Bar Graph, Pie Chart, All): ').lower()
        print('------------------------------------------------------------------------------------------')
        # Validation to ensure the choice selected is an option, and will notify the user if their choice is 
        # not an option.
        if choice not in choice_list:
            print('\n------------------------------------------------------------------------------------------')
            print(f'\'{choice}\' is not a valid option. Please try again and choose from the 4 options provided.')
            print('------------------------------------------------------------------------------------------')
        else:
            break
    
    # Choices calling their relevant functions when selected
    if choice == 'bar graph':
        barchart()
    elif choice == 'pie chart':
        piechart() 
    elif choice == 'heatmap':
        heatmap()
    elif choice == 'all':
        heatmap()
        piechart()
        barchart()
    
    # Solicting the user whether to run the loop again to see another graph or stop the program.
    print('Would you like to continue and see another graph?')
    print('------------------------------------------------------------------------------------------')
    cont = input('(Please enter Y/N): ').upper()
    
    # Stopping the program and thanking the user for using our program.
    if cont == 'N':
        print('------------------------------------------------------------------------------------------')
        print('\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------------------------------')
        print('Thank you for using our program and we hope you enjoyed the content!')
        print('------------------------------------------------------------------------------------------')
        break
