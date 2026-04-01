# Cfd-mockup
Actual CFD is incredibly complex, is a very computational intensive program, and isn't feasible for regualar people. Which is why its important to be able to simulate such flow using mathematics.


## Disclaimers, mentions, etc.
*This project is a mockup of pure LBM and Navier-Stokes CFD, this method uses doublets and particle discretization to achieve the same level of detail and accuracy as CFD models that use computational derivation. This project was also made in mind of the Jackpot (HackClub event) https://jackpot.hackclub.com/ , also a huge shout out to Claude and NotebookLM without you this project wouldn't have been possible.* 😭💀

## Review/General-Overview
+ Jan-Feb 15th - I started this project of in the beggining of the year, at this point it was pure research and understanding, I needed a strong grasp of calculus concepts and general methodologies for acheiving fluid flow sims. I discovered several methods, implementation of the Navier-Stokes equations or even the simplified Lattice Boltzman Method https://github.com/fabioskomori/lbsim/wiki, but all of these seemed incredibly difficult to implement and it would need at least a year of research and implementation.

+ Feb 15th-Mar 10th - Decided to just use doublets and mathematical graphing occurances to mimic the same results in CFD, this was through several versions and deliberation that I decicded to go forward with this method as it seemed the easiest to implement and the least technically demanding. 

+ Mar 10th-13th - Started reviewing basic Matplotlib vector graphs, and started understanding the funadmentals of the tools I was going to be using. 
    ### Tech Stack
  + Python
  + Matplotlib
  + Scipy
  + numpy

<img width="541" height="317" alt="Screenshot 2026-03-31 at 11 45 38 AM" src="https://github.com/user-attachments/assets/7a675106-fedb-4182-b9f7-b2ba681c361f" />
<img width="591" height="737" alt="Screenshot 2026-03-31 at 11 46 07 AM" src="https://github.com/user-attachments/assets/ad80dbe7-09c8-4ce0-a80e-af75e237c4b2" />

+ Started learning simple formatting and basic vector fields in Matplotlib, above are some examples of some tests I ran

+ Mar 13th-15th At this time I also started delving into vector mathematics and what it actually was, explored, Scalar multiplication, dot products and cross-products as well as radial and rotational fields. 

<img width="508" height="792" alt="Screenshot 2026-03-31 at 11 49 21 AM" src="https://github.com/user-attachments/assets/088e4bbc-0102-463f-bd68-6ec1a0b29787" />

+ Mar 15th-28 - Actually started building and implementing the project, for more indepth review of everything I just said visit https://jackpot.hackclub.com/deck (for reviewers) and a soon to be posted full pdf of my journalling and experiments.

## Comments for Reviewers
A lot of code is directly from doc pages, forums, and pdf's these code blocks still have their specific comments and info, so please don't consider that AI, I have probably editied a lot of the files to not have those comments and pasted them onto a seperate document for future reference but if you find any of those files please don
