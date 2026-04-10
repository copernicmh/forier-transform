# forier-transform


## instruction set
  1. read paper

    April 5th: read section I and II.
    
    The topic of the paper is the use of a Fourier transform coupled with a Guassian window function to determine through
    a relatively short field line integration whether a particular magnetic field line lies on a analytic or a rough magnetic suurface or chaotically fills its volume. 

    It defines a chaotic magnetic field line B as having lines in its neighborhood that seperate from it exponentially as zeta increases.
    
    Cylindrical Coordinates (R, phi, Zeta) are used along with the poloidal angle to describe the surface on which the line lies. (Noted in Line 43)

    We want to analyze the broad/narrowness of the peaks by making the gaussian window lambda greater/smaller

  2. manually calculate trajectory then use that data for fft

    file path is tricky here

  3. run calculate_fft_fieldlines.py (r =0.4 at lambda = 100)
  4. Run the same code at (r = 0.4 at lambda = 100)

  5. write code to perform ftt on multiple radii or lambda values (10-300 50 increments) -- this might require automating the script such that we can change the r and lambda values in the CLI and thens ave the visual onto file paths within any respective computer.
