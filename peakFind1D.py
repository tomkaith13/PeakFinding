import sys
import ast



class PeakFinder(object):
    data=[]
    def __init__(self,data):
        self.data = data
    
    def print_data(self):
        print self.data
    
    def OneDPeak(self, start, end):
        """ finding a 1D peak using binary search"""
        peakLoc = []
        print self.data[start:end+1]
        
        # the two end conditions:
        # In the case of odd list, one element list can also be left
        # only only one , we pick that one
        if end == start:
            peakLoc.append(end)
            peakLoc.append(self.data[end])
            return peakLoc
        # 2 element list is left, then pick the max
        elif end == start + 1:
            if (self.data[end] > self.data[start]):
                peakLoc.append(end)
                peakLoc.append(self.data[end])
                return peakLoc
            else:
                peakLoc.append(start)
                peakLoc.append(self.data[start])
                return peakLoc
        # There are atleast three elements     
        mid = (end - start) // 2
        mid = start + mid      
        if self.data[mid] >= self.data[mid -1] and self.data[mid] >= self.data[mid+1]:
            peakLoc.append(mid)
            peakLoc.append(self.data[mid])
            return peakLoc        
        elif self.data[mid] < self.data[mid - 1]:
            return self.OneDPeak(start, mid - 1)
        else:
            return self.OneDPeak(mid+1, end)  
        
    def TwoDPeak(self, clow, chigh):
        """ Find a 2d peak in O(log(log n)) """
        PeakLoc = []
        
        """ boundary conditions"""
        if clow == chigh:
            # If this is the last            
            cPeak = OneDColPeak(clow,self.data)
            PeakLoc.extend((cPeak[0],clow))
            PeakLoc.append(cPeak[1])
            return PeakLoc
        
        mid = (chigh - clow)//2 
        mid = clow + mid
        print 'mid is:',mid
        cPeak = OneDColPeak(mid,self.data)
        row = cPeak[0]
        
        if self.data[row][mid] >= self.data[row][mid - 1] and self.data[row][mid] >= self.data[row][mid + 1]:
            PeakLoc.extend((row,mid))
            PeakLoc.append(self.data[row][mid])
            return PeakLoc
        elif self.data[row][mid] < self.data[row][mid - 1]:
            return self.TwoDPeak(clow, mid - 1)
        else:
            return self.TwoDPeak(mid + 1, chigh)
            
        
        
        
        pass
        
    def find_peak(self):
        item=self.data[0]
        
        if type(item) == list:
            return self.TwoDPeak(0,len(self.data[0]) - 1)
        else:            
            return self.OneDPeak(0,len(self.data) - 1)
        
def OneDColPeak(col, data):
        """ Find the OneD peak of a 2d matrix's column col """
        vlist = []
        """ First, we go through the matrix column and convert it to a oneD list """
        numRows = len(data)
        print "num of row",numRows
        for r in range(numRows):
            vlist.append(data[r][col])
        
        ColPeak = PeakFinder(vlist)
        return ColPeak.find_peak()        

def main():
    data = []
    with open("matrix.txt") as handle:
        strdata=handle.read()
    data = ast.literal_eval(strdata)    
    
    print 'type:',type(data)
    peak = PeakFinder(data)
    peak.print_data()
    i = peak.find_peak()
    
    print 'peak Location is:',i
    if len(i) == 3:
        print 'new peak:',i[2]
    else:
        print 'new peak:',i[1]
    
    
if __name__ == "__main__":
    main()
    
    
        
    
    
        