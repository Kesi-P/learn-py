import matplotlib.pyplot as plt
import numpy as np


# years = [1,2,3,4]
# pops = [1,2,3,4]
# death = [1,1,4,2]
# plt.plot(years,pops,'--',color=(255/255,100/255,100/255))
# plt.plot(years,death,color=(.6,.6,1))
# plt.ylabel('Populations in millions')
# plt.xlabel('Populations growth by year')
#
# lines = plt.plot(years,pops,years,death)
# plt.grid(True)
#
# plt.setp(lines,color=(1,.4,.4),marker='*')
# plt.show()

# labels = 'Cat','Dog','Cow','Rat','Pig','Hen'
# sizes=[11,22,33,44,55,66]
# explode = (0, 0.1, 0, 0,0,0)
#
#
# plt.pie(sizes,labels=labels,autopct='%1.1f%%',explode=explode)
# plt.axis('equal')
# plt.show()
col_count =3

korea_scores =(554,536,538)
canada_scores = (518,354,525)
china_scores =(613,570,580)
france_scores = (495,505,499)

index = np.arange(col_count)

k1=plt.bar(index,korea_scores,.5)
c1=plt.bar(index,canada_scores,.5)
plt.grid(True)
plt.show()