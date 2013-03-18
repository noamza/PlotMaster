import matplotlib.pyplot as plt

def xyplot(xdata,ydata,title):
    fname = "/Users/nalmog/Desktop/swa_equipped_cumulative_"+title+".png"
    #plt.figure(figsize=(500,500))
    plt.plot(xdata, ydata)
    plt.ylabel('some numbers')  
#     plt.savefig("/Users/nalmog/Desktop/swa_equipped_cumulative_"+title+".png", format='png')
    #plt.show()
    #plt.savefig("/Users/nalmog/Desktop/swa_equipped_cumulative_"+title+".png", format='png')
    plt.title(title)        
    plt.xlabel("Percent of Fleet")
    plt.ylabel("Number of Passes")
    plt.savefig(fname)
    plt.clf();
    #plt.


