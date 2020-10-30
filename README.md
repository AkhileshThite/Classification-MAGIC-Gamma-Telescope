# Classification: MAGIC Gamma Telescope
![](https://github.com/AkhileshThite/Portfolio/blob/master/MAGIC-telescope-twitter.jpg)

• It is used to find the "cosmic source" by registration of high energy gamma particles in a ground-based atmospheric Cherenkov gamma telescope using imaging technique.

• I tested all the classification algorithms and finally got the best results with **99.98%** accuracy by using **"Random Forest Classification"**. And then distinguished gamma rays (signal) from hadronic showers (background) for the further studies.

Attribute Information:

1. fLength: continuous # major axis of ellipse [mm] 
2. fWidth: continuous # minor axis of ellipse [mm] 
3. fSize: continuous # 10-log of sum of content of all pixels [in #phot] 
4. fConc: continuous # ratio of sum of two highest pixels over fSize [ratio] 
5. fConc1: continuous # ratio of highest pixel over fSize [ratio] 
6. fAsym: continuous # distance from highest pixel to center, projected onto major axis [mm] 
7. fM3Long: continuous # 3rd root of third moment along major axis [mm] 
8. fM3Trans: continuous # 3rd root of third moment along minor axis [mm] 
9. fAlpha: continuous # angle of major axis with vector to origin [deg] 
10. fDist: continuous # distance from origin to center of ellipse [mm] 
11. class: g,h # gamma (signal), hadron (background) 

g = gamma (signal): 12332 

h = hadron (background): 6688 

• Dataset source- https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope
