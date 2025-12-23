marks=[2,3,4,5,6,6,1,7,8,9] 
import numpy as np
npmarks=np.array(marks)
print("highest marks:",np.max(npmarks))
print("lowest marks:",np.min(npmarks))
print("class average:",np.mean(npmarks))
print(npmarks)
print(np.where(npmarks>4,"pass","fail"))
print("highest marks:",max(marks))
print("lowest marks:",min(marks))
print(np.where(np.mean(npmarks)>5,"above avg",np.where(np.mean(npmarks)<5,"below avg","avg")))

