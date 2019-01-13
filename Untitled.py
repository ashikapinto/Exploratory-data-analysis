
# coding: utf-8

# In[2]:


#importing the essential libraries and the dataset.
get_ipython().magic('matplotlib inline')
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('dataset.csv')


# In[3]:


#cleaning the data:
#our dataset has missing values in certain columns.
#the following code replaces them with the medians of the respective columns. 
 
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False
    
    
for index,row in df.TOTPOPULAT.iteritems():
    if(isfloat(row)):   
        df.TOTPOPULAT.loc[index]=float(row)
    else:
        df.TOTPOPULAT.loc[index]=np.NaN
df.TOTPOPULAT=df.TOTPOPULAT.fillna(0)
for index,row in df.TOTPOPULAT.iteritems():
    if(float(row)==0):
        df.TOTPOPULAT.loc[index]=np.median(df.TOTPOPULAT)
    
        
        
for index,row in df.P_URB_POP.iteritems():
    if(isfloat(row)):   
            df.P_URB_POP.loc[index]=float(row)
        
    else:
        df.P_URB_POP.loc[index]=np.NaN
df.P_URB_POP=df.P_URB_POP.fillna(-1)          
for index,row in df.P_URB_POP.iteritems():
    if(float(row)<=-1):                              
        df.P_URB_POP.loc[index]=np.median(df.P_URB_POP)   #ALSO REPLACING SOME NEGATIVE VALUES OF PERCENTAGE

 
        
        
        
for index,row in df.POPULATION_0_6.iteritems():
    if(isfloat(row)):   
            df.POPULATION_0_6.loc[index]=float(row)
        
    else:
        df.POPULATION_0_6.loc[index]=np.NaN
df.POPULATION_0_6=df.POPULATION_0_6.fillna(0)
for index,row in df.POPULATION_0_6.iteritems():
    if(float(row)==0):
        df.POPULATION_0_6.loc[index]=np.median(df.POPULATION_0_6)

    
for index,row in df.SEXRATIO.iteritems():
    if(isfloat(row)):
        if(row>100):   
            df.SEXRATIO.loc[index]=float(row)
        else:
            df.SEXRATIO.loc[index]=np.NaN
    else:
        df.SEXRATIO.loc[index]=np.NaN
df.SEXRATIO=df.SEXRATIO.fillna(0)
for index,row in df.SEXRATIO.iteritems():
    if(float(row)<100):
        df.SEXRATIO.loc[index]=np.median(df.SEXRATIO)

    
for index,row in df.GROWTHRATE.iteritems():
    if(isfloat(row)):   
        df.GROWTHRATE.loc[index]=float(row)
    else:
        df.GROWTHRATE.loc[index]=np.NaN
df.GROWTHRATE=df.GROWTHRATE.fillna(0)
for index,row in df.GROWTHRATE.iteritems():
    if(float(row)==0):
        df.GROWTHRATE.loc[index]=np.median(df.GROWTHRATE)

for index,row in df.P_ST_POP.iteritems():
    if(isfloat(row)):   
            df.P_ST_POP.loc[index]=float(row)
        
    else:
        df.P_ST_POP.loc[index]=np.NaN
df.P_ST_POP=df.P_ST_POP.fillna(-1)
for index,row in df.P_ST_POP.iteritems():
    if(float(row)==-1):
        df.P_ST_POP.loc[index]=np.median(df.P_ST_POP)
        
        
for index,row in df.P_SC_POP.iteritems():
    if(isfloat(row)):   
            df.P_SC_POP.loc[index]=float(row)
        
    else:
        df.P_SC_POP.loc[index]=np.NaN
df.P_SC_POP=df.P_SC_POP.fillna(-1)
for index,row in df.P_SC_POP.iteritems():
    if(float(row)==-1):
        df.P_SC_POP.loc[index]=np.median(df.P_SC_POP)


# In[4]:


for index,row in df.OVERALL_LI.iteritems():
    if(isfloat(row)):   
            df.OVERALL_LI.loc[index]=float(row)
        
    else:
        df.OVERALL_LI.loc[index]=np.NaN
df.OVERALL_LI=df.OVERALL_LI.fillna(0)
for index,row in df.OVERALL_LI.iteritems():
    if(float(row)==0):
        df.OVERALL_LI.loc[index]=np.median(df.OVERALL_LI)
        
for index,row in df.FEMALE_LIT.iteritems():
    if(isfloat(row)):   
            df.FEMALE_LIT.loc[index]=float(row)
        
    else:
        df.FEMALE_LIT.loc[index]=np.NaN
df.FEMALE_LIT=df.FEMALE_LIT.fillna(0)
for index,row in df.FEMALE_LIT.iteritems():
    if(float(row)==0):
        df.FEMALE_LIT.loc[index]=np.median(df.FEMALE_LIT)
        
for index,row in df.MALE_LIT.iteritems():
    if(isfloat(row)):   
            df.MALE_LIT.loc[index]=float(row)
        
    else:
        df.MALE_LIT.loc[index]=np.NaN
df.MALE_LIT=df.MALE_LIT.fillna(0)
for index,row in df.MALE_LIT.iteritems():
    if(float(row)==0):
        df.MALE_LIT.loc[index]=np.median(df.MALE_LIT)
        
for index,row in df.AREA_SQKM.iteritems():
    if(isfloat(row)):   
            df.AREA_SQKM.loc[index]=float(row)
        
    else:
        df.AREA_SQKM.loc[index]=np.NaN
df.AREA_SQKM=df.AREA_SQKM.fillna(0)
for index,row in df.AREA_SQKM.iteritems():
    if(float(row)<=100):
        df.AREA_SQKM.loc[index]=np.median(df.AREA_SQKM)
        
for index,row in df.TOT_6_10_15.iteritems():
    if(isfloat(row)):   
            df.TOT_6_10_15.loc[index]=float(row)
        
    else:
        df.TOT_6_10_15.loc[index]=np.NaN
df.TOT_6_10_15=df.TOT_6_10_15.fillna(0)
for index,row in df.TOT_6_10_15.iteritems():
    if(float(row)==0):
        df.TOT_6_10_15.loc[index]=np.median(df.TOT_6_10_15)
        

for index,row in df.TOT_11_13_15.iteritems():
    if(isfloat(row)):   
            df.TOT_11_13_15.loc[index]=float(row)
        
    else:
        df.TOT_11_13_15.loc[index]=np.NaN
df.TOT_11_13_15=df.TOT_11_13_15.fillna(0)
for index,row in df.TOT_11_13_15.iteritems():
    if(float(row)==0):
        df.TOT_11_13_15.loc[index]=np.median(df.TOT_11_13_15)
        
#This completes Data cleaning.
#Measures taken: replacing missing values
#                replacing invalid entries for example: negative values for percentage
#                There are also some outliers in the data set.but we found it best to not replace
#                 them as those could be the actual data values,replacing them would affect our data.


# In[5]:


#INFERENCES TO MAKE

#question 1:more the number of private institutions more the literacy rate

#plotting literacy rate wrt states
import seaborn as sns
plt.figure(figsize=(10,12))
sns.barplot(df['OVERALL_LI'], df['STATNAME'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel("Literacy rate", fontsize=16)
plt.title('Literacy rate with respect to state')
plt.show()

#plotting number of private schools wrt states
plt.figure(figsize=(10,12))
sns.barplot(df['SCHTOTP'], df['STATNAME'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel('Number of private Schools', fontsize=14)
plt.ylabel('States in India', fontsize=14)
plt.title("Number of private schools wrt states in India", fontsize=16)
plt.show()

#plotting number of government schools wrt states
plt.figure(figsize=(10,12))
sns.barplot(df['SCHTOTG'], df['STATNAME'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel('Number of govt Schools', fontsize=14)
plt.ylabel('States in India', fontsize=14)
plt.title("Number of government schools wrt states in India", fontsize=16)
plt.show()




#inference:The number of government schools is high in all states except kerala.
#60% of schools in kerala are private.Incidentally it also has a very high literacy rate.
#In bihar only 3% schools are private.And its literacy rate is the least in the country.
#So we could conclude that having more private institutions helps increase the literacy rate of the country


# In[6]:


#QUESTION 2: RELATE URBAN POPULATION WITH LITERACY RATE

#plotting urban population in different states
plt.figure(figsize=(10,12))
sns.barplot(df['STATNAME'], df['P_URB_POP'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel('STATE', fontsize=14)
plt.ylabel('PERCENTAGE OF URBAN POPULATION', fontsize=14)
plt.title("PERCENTAGE OF URBAN POP IN DIFFERENT STATES", fontsize=16)
plt.show()

#plotting literacy rate in different states
import seaborn as sns
plt.figure(figsize=(10,12))
sns.barplot(df['STATNAME'],df['OVERALL_LI'], alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel("Literacy rate", fontsize=16)
plt.title('Literacy rate with respect to state')
plt.show()

#INFERENCE:
#it is observed that bihar,which has least literacy rate has the least percentage of urban population
#all states that have a fairly high percentage of urban population have good literacy rates.
#So it wont be incorrect if we say that the more the urban population in a state,the more is its 
#literacy rate
#probably because of better and convinient facilities in urban India.


# In[7]:


#question 3: comparing female and male literacy rates in india using histograms.

freq,bins,patches=plt.hist(df.FEMALE_LIT,bins=[i for i in range(50,100,5)])
print('count:',freq)
print('bins:',bins)
plt.title('Female literacy rate Histogram')
plt.xlabel('female literacy rates in india')
plt.ylabel('frequency')
plt.show()

freq,bins,patches=plt.hist(df.MALE_LIT,bins=[i for i in range(50,100,5)])
print('count:',freq)
print('bins:',bins)
plt.title('male literacy rate Histogram')
plt.xlabel('male literacy rates in india')
plt.ylabel('frequency')
plt.show()

#graph shows that lesser number of states in india have high female literacy rate whereas most of them 
#have pretty high male literacy rates
#Low female literacy rate means an overall sluggish growth of India, 
#as it impacts every arena of the development. 
#India is struggling hard to stabilize its growing population through family planning programs.
#But if females are illiterate, then this has a direct and negative impact on these initiatives.
#The negative attitude of parents towards the girl child and her education is one of the major 
#reasons of low female literacy rate in India.


# In[8]:


#question 4:NUMBER OF WELL EQUIPPED SCHOOLS IN INDIA
freq,bins,patches=plt.hist(df.SELETOT,bins=[i for i in range(0,1800,100)])
print('count:',freq)
print('bins:',bins)
plt.title('NUMBER OF SCHOOLS WITH ELECTRICITY-HISTOGRAM')
plt.xlabel('NUMBER OF SCHOOLS WITH ELECTRICITY')
plt.ylabel('frequency')
plt.show()

freq,bins,patches=plt.hist(df.SPLAYTOT,bins=[i for i in range(0,1800,100)])
print('count:',freq)
print('bins:',bins)
plt.title('NUMBER OF SCHOOLS WITH PLAY GROUND FACILITIES-Histogram')
plt.xlabel('NUMBER OF SCHOOLS WITH PLAY GROUND FACILITIES')
plt.ylabel('frequency')
plt.show()

freq,bins,patches=plt.hist(df.SWATTOT,bins=[i for i in range(0,1800,100)])
print('count:',freq)
print('bins:',bins)
plt.title('NUMBER OF SCHOOLS WITH WATER FACILITIES-Histogram')
plt.xlabel('NUMBER OF SCHOOLS WITH WATER FACILITIES')
plt.ylabel('frequency')
plt.show()

import seaborn as sns
sns.boxplot(x='SELETOT',data=df)
plt.title("NUMBER OF SCHOOLS WITH ELECTRICITY", fontsize=16)
plt.show()

import seaborn as sns
sns.boxplot(x='SPLAYTOT',data=df)
plt.title("NUMBER OF SCHOOLS WITH PLAY GROUND FACILITIES",fontsize=16)
plt.show()


import seaborn as sns
sns.boxplot(x='SWATTOT',data=df)
plt.title("NUMBER OF SCHOOLS WITH WATER FACILITIES",fontsize=16)
plt.show()


#Graphs show that number of districts having large number of well equipped schools is pretty less in 
#Indian states
#all boxplots are RIGHT SKEWED




# In[19]:


#QUESTION 5: Comparing enrolment in government and private schools

import seaborn as sns
sns.boxplot(x='ENRTOT',data=df)
plt.title("Enrolment in schools", fontsize=16)
plt.show()

import seaborn as sns
sns.boxplot(x='ENRTOTG',data=df)
plt.title("Enrolment in government schools",fontsize=16)
plt.show()


import seaborn as sns
sns.boxplot(x='ENRTOTGR',data=df)
plt.title("Enrolment in government schools in rural areas",fontsize=16)
plt.show()


import seaborn as sns
sns.boxplot(x='ENRTOTPR',data=df)
plt.title("Enrolment in private schools in rural areas",fontsize=16)
plt.show()



#first graph ->right skewed
#implies that enrolment is less in many districts
#second graph-.also right skewed
#comparing enrolment in private and government schools in rural areas:
#very less in private compared to government


# In[ ]:






# In[15]:


#QUESTION 6: DECREASING SEXRATION WITH INCREASE IN NUMBER OF VILLAGES

list1=[]
list2=[]
for i in range(625,663,1):
    list1.append(df.VILLAGES[i])
    list2.append(df.SEXRATIO[i])
plt.scatter(list1,list2)
plt.title('VARIATION OF SEXRATIO WITH NUMBER OF VILLAGES')
plt.xlabel('THE NUMBER OF VILLAGES')
plt.ylabel('THE SEXRATIO')

import seaborn as sns
plt.figure(figsize=(10,12))
sns.barplot(df['STATNAME'], df['VILLAGES'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel('STATE', fontsize=14)
plt.ylabel('NUMBER OF VILLAGES', fontsize=14)
plt.title("NUMBER OF VILLAGES IN DIFFERENT STATES", fontsize=16)
plt.show()

#Scatter plot shows that the literacy rates of states that have large number of villages 
#is lesser compared to those with less number of villages

#BAR PLOT INFERENCE: Kerala,the state that has the highest literacy rate has very less number of 
#villages


# In[16]:


#QUESTION 7: INCREASE IN THE GROWTHRATE WITH INCREASE IN NUMBER OF SCHOOLS
plt.figure(figsize=(5,5))
list1=[]
list2=[]
for i in range(620,633,1):
    list1.append(df.SCHTOT[i])
    list2.append(df.GROWTHRATE[i])
plt.scatter(list1,list2)
plt.title('VARIATION OF GROWTHRATE WITH NUMBER OF SCHOOLS')
plt.xlabel('THE NUMBER OF SCHOOLS')
plt.ylabel('THE GROWTHRATE')



# In[21]:


#QUESTION 8:CANNOT ASSUME THAT BETTER EQUIPPED SCHOOLS GUARANTEE BETTER LITERACY RATES
plt.figure(figsize=(5,5))
list1=[]
list2=[]
for i in range(420,433,1):
    list1.append(df.SWATTOT[i])
    list2.append(df.OVERALL_LI[i])
plt.scatter(list1,list2)
plt.title('VARIATION OF LITERACY RATE WITH NUMBER OF SCHOOLS WITH WATER FACILITIES')
plt.xlabel('THE NUMBER OF SCHOOLS WITH WATER FACILITIES')
plt.ylabel('THE LITERACY RATE')

plt.figure(figsize=(5,5))
list1=[]
list2=[]
for i in range(520,540,1):
    list1.append(df.SELETOT[i])
    list2.append(df.OVERALL_LI[i])
plt.scatter(list1,list2)
plt.title('VARIATION OF LITERACYRATE WITH NUMBER OF SCHOOLS WITH ELECTRICITY FACILITIES')
plt.xlabel('THE NUMBER OF SCHOOLS WITH ELECTRICITY RATES')
plt.ylabel('THE LITERACY RATE')



import seaborn as sns
plt.figure(figsize=(10,12))
sns.barplot(df['STATNAME'], df['SELETOT'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel('NAME OF STATES', fontsize=14)
plt.ylabel('NUMBER OF SCHOOLS WITH ELECTRICITY FACILITIES', fontsize=14)
plt.title("Number of schools WITH ELECTRICITY IN INDIA IN DIFFERENT STATES", fontsize=16)
plt.show()


import seaborn as sns
plt.figure(figsize=(10,12))
sns.barplot(df['STATNAME'], df['SPLAYTOT'],alpha=0.8)
plt.xticks(rotation='vertical')
plt.xlabel('sTATE', fontsize=14)
plt.ylabel('NUMBER OF SCHOOLS WITH PLAYGROUND FACILITIES', fontsize=14)
plt.title("Number of schools WITH PLAYGROUND FACILITIES IN INDIA IN DIFFERENT STATES", fontsize=16)
plt.show()

#GRAPHS SHOW THAT THERE IS NO REAL RELATION BETWEEN THE NUMBER OF WELL EQUIPPED SCHOOLS(IN TERMS OF ELECTRICITY AND WATER FACILITIES)
#AND LITERACY RATES
#KERALA(HAVING HIGHEST LITERACY RATE) HAS VERY LESS NUMBER OF WELL EQUIPPED SCHOOLS
#UTTAR PRADESH HAS HIGH NUMBER OF WELL EQUIPPED SCHOOLS BUT STILL HAS VERY LOW LITERACY RATES

