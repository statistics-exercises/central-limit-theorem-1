import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand = plt.gca()
        figdat = fighand.get_lines()[2].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) :
           self.assertTrue( xmin + np.fabs( (xmax-xmin)*(i+0.5)/len(this_x) - this_x[i] )<1e-7, "the x-coordinates in your histogram are incorrect" )
  
    def test_normalised(self) :
        ssum = 0.
        fighand = plt.gca()
        figdat = fighand.get_lines()[2].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) : ssum = ssum + this_y[i]*(this_x[1]-this_x[0])
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "your histogram has not been normalised" )
    
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        delx = this_x[1] - this_x[0]
        for i in range( len(this_y) ) :
           pp = st.norm.cdf( this_x[i] + 0.5*delx, 0, np.sqrt(4/15) ) - st.norm.cdf( this_x[i] - 0.5*delx, 0, np.sqrt(4/15) )
           bar = np.sqrt( pp*(1-pp) )*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( this_y[i]- st.norm.pdf( this_x[i], 0, 1/np.sqrt(5) ) )<bar, "the y-coordinates in your histogram appear to be incorrect )
  
    def test_mean(self) : 
        for i in range(15,25) :
        smean = 0 
        for j in range(50) : 
            smean = smean + sample_mean(i)
        self.assertTrue( smean/i>st.norm.ppf(0.01) and smean/i<st.norm.ppf(0.99), "your code for calculating the sample mean does not appear to be sampling from the correct distribution" )
