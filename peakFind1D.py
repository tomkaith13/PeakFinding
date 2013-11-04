import sys
import ast



class PeakFinder(object):
    data=[]
    def __init__(self,data):
        self.data = data
    
    def print_data(self):
        print self.data
    
    def OneDPeak(self, start, end):
        """ finding a 1D peak """
        print self.data[start:end+1]
        
        # the two end conditions:
        # In the case of odd list, one element list can also be left
        # only only one , we pick that one
        if end == start:
            return self.data[end]
        # 2 element list is left, then pick the max
        elif end == start + 1:
            if (self.data[end] > self.data[start]):
                return self.data[end]  
            else:
                return self.data[start]
        # There are atleast three elements     
        mid = (end - start) // 2
              
        if self.data[mid] >= self.data[mid -1] and self.data[mid] >= self.data[mid+1]:
            return self.data[mid]        
        elif self.data[mid] < self.data[mid - 1]:
            return self.OneDPeak(start, mid - 1)
        else:
            return self.OneDPeak(mid+1, end)
        
    def __2DPeak(self):
        pass
        
    def find_peak(self):
        item=self.data[0]
        
        if type(item) == list:
            return self.__2DPeak()
        else:
            return self.OneDPeak(0,len(self.data) - 1)
        
        

def main():
    data = []
    with open("matrix.txt") as handle:
        strdata=handle.read()
    data = ast.literal_eval(strdata)    
    
    print 'type:',type(data)
    peak = PeakFinder(data)
    peak.print_data()
    i = peak.find_peak()
    
    print 'new peak:',i
    
    
if __name__ == "__main__":
    main()
    
    
        
    
    
        