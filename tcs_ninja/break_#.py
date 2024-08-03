# # # def breakIt(s,i,j,res):
# # #     if j>=len(s):
# # #         res.append(s[i:j+1])
# # #         return res
# # #     if s[j]!="#":
# # #         return breakIt(s,i,j+1,res)
# # #     else:
# # #         res.append(s[i:j])
# # #         while j<len(s) and s[j]=="#":
# # #             j+=1
# # #
# # #         return breakIt(s,j,j,res)
# # #
# # # res = breakIt("122345678#",0,0,[])
# # # print([i for i in res if i!=""])
# # arr = [1,2,3,4,5]
# # ans = []
# # for i in range(len(arr)):
# #     for j in range(i,len(arr)):
# #         a = arr[i:j]
# #         if a:
# #             ans.append(a)
# # print(ans)
# %---- Required
# Packages and Functions - ---
#
# \documentclass[a4paper, 11
# pt]{article}
# \usepackage
# {latexsym}
# \usepackage
# {xcolor}
# \usepackage
# {float}
# \usepackage
# {ragged2e}
# \usepackage[empty]
# {fullpage}
# \usepackage
# {wrapfig}
# \usepackage
# {lipsum}
# \usepackage
# {tabularx}
# \usepackage
# {titlesec}
# \usepackage
# {geometry}
# \usepackage
# {marvosym}
# \usepackage
# {verbatim}
# \usepackage
# {enumitem}
# \usepackage[hidelinks]
# {hyperref}
# \usepackage
# {fancyhdr}
# \usepackage
# {fontawesome5}
# \usepackage
# {multicol}
# \usepackage
# {graphicx}
# \usepackage
# {cfr - lm}
# \usepackage[T1]
# {fontenc}
# \setlength
# {\footskip}{4.08003
# pt}
# \pagestyle
# {fancy}
# \fancyhf
# {} % clear
# all
# header and footer
# fields
# \fancyfoot
# {}
# \renewcommand
# {\headrulewidth}{0
# pt}
# \renewcommand
# {\footrulewidth}{0
# pt}
# \geometry
# {left = 1.0
# cm, top = 1
# cm, right = 1
# cm, bottom = 1
# cm}
# %Adjust
# margins
# % \addtolength
# {\oddsidemargin}{-0.5 in}
# % \addtolength
# {\evensidemargin}{-0.5 in}
# % \addtolength
# {\textwidth}{1 in}
# \usepackage[most]
# {tcolorbox}
# \tcbset
# {
#     frame
# code = {}
# center
# title,
# left = 0
# pt,
# right = 0
# pt,
# top = 0
# pt,
# bottom = 0
# pt,
# colback = gray!20,
# colframe = white,
# width =\dimexpr\textwidth\relax,
# enlarge
# left
# by = -2
# mm,
# boxsep = 4
# pt,
# arc = 0
# pt, outer
# arc = 0
# pt,
# }
#
# \urlstyle
# {same}
#
# \raggedright
# \setlength
# {\footskip}{4.08003
# pt}
#
# %Sections
# formatting
# \titleformat
# {\section}{
# \vspace
# {-4
# pt}\scshape\raggedright\large
# }{}
# {0
# em}{}[\color
# {black}\titlerule \vspace
# {-7
# pt}]
#
# %-------------------------
# %Custom
# commands
# \newcommand
# {\resumeItem}[2]
# {
# \item
# {
# \textbf
# {  # 1}{\hspace{0.5mm}#2 \vspace{-0.5mm}}
# }
# }
#
# \newcommand
# {\resumePOR}[3]
# {
# \vspace
# {0.5
# mm}\item
# \begin
# {tabular *}
# {0.97\textwidth}[t]
# {l @ {\extracolsep
# {\fill}}r}
# \textbf
# {
# # 1}\hspace{0.3mm}#2 & \textit{\small{#3}}
# \end
# {tabular *}
# \vspace
# {-2
# mm}
# }
#
# \newcommand
# {\resumeSubheading}[4]
# {
# \vspace
# {0.5
# mm}\item
# \begin
# {tabular *}
# {0.98\textwidth}[t]
# {l @ {\extracolsep
# {\fill}}r}
# \textbf
# {
# # 1} & \textit{\footnotesize{#4}} \\
# \textit
# {\footnotesize
# {
# # 3}} &  \footnotesize{#2}\\
# \end
# {tabular *}
# \vspace
# {-2.4
# mm}
# }
#
# \newcommand
# {\resumeProject}[4]
# {
# \vspace
# {0.5
# mm}\item
# \begin
# {tabular *}
# {0.98\textwidth}[t]
# {l @ {\extracolsep
# {\fill}}r}
# \textbf
# {
# # 1} & \textit{\footnotesize{#3}} \\
# \footnotesize
# {\textit
# {
# # 2}} & \footnotesize{#4}
# \end
# {tabular *}
# \vspace
# {-2.4
# mm}
# }
#
# \newcommand
# {\resumeSubItem}[2]
# {\resumeItem
# {  # 1}{#2}\vspace{-4pt}}
#
# % \renewcommand
# {\labelitemii}{$\circ$}
# \renewcommand
# {\labelitemi}{$\vcenter
# {\hbox
# {\tiny$\bullet$}}$}
#
# \newcommand
# {\resumeSubHeadingListStart}{\begin
# {itemize}[leftmargin = *, labelsep = 0
# mm]}
# \newcommand
# {\resumeHeadingSkillStart}{\begin
# {itemize}[leftmargin = *, itemsep = 1.7
# mm, rightmargin = 2
# ex]}
# \newcommand
# {\resumeItemListStart}{\begin
# {justify}\begin
# {itemize}[leftmargin = 3
# ex, rightmargin = 2
# ex, noitemsep, labelsep = 1.2
# mm, itemsep = 0
# mm]\small}
#
# \newcommand
# {\resumeSubHeadingListEnd}{\end
# {itemize}\vspace
# {2
# mm}}
# \newcommand
# {\resumeHeadingSkillEnd}{\end
# {itemize}\vspace
# {-2
# mm}}
# \newcommand
# {\resumeItemListEnd}{\end
# {itemize}\end
# {justify}\vspace
# {-2
# mm}}
# \newcommand
# {\cvsection}[1]
# { %
# \vspace
# {2
# mm}
# \begin
# {tcolorbox}
# \textbf
# {\large  # 1}
# \end
# {tcolorbox}
# \vspace
# {-4
# mm}
# }
#
# \newcolumntype
# {L}
# { > {\raggedright\arraybackslash}X} %
# \newcolumntype
# {R}
# { > {\raggedleft\arraybackslash}X} %
# \newcolumntype
# {C}
# { > {\centering\arraybackslash}X} %
# %---- End
# of
# Packages and Functions - -----
#
# % -------------------------------------------
# %%%%%% CV
# STARTS
# HERE %%%%%%%%%%%
# %%%%%% DEFINE
# ELEMENTS
# HERE %%%%%%%
# \newcommand
# {\name}{Anup
# Kumar} %Your
# Name
# \newcommand
# {\phone}{7970954003}
# \newcommand
# {\emaila}{anup7970hm @ gmail.com}
#
#
#
# \begin
# {document}
# \fontfamily
# {cmr}\selectfont
#       % ----------HEADING - ----------------
#
#
# \parbox
# {\dimexpr\linewidth - 0.3
# cm\relax}{
# \begin
# {tabularx}
# {\linewidth}{L
# r} \ \
#     \textbf
# {\Large \name} \ \
#     {\raisebox
# {0.0\height}{\footnotesize \faPhone}\ +91 -\phone} &  \href
# {https: // github.com / anup - 66}{\raisebox
# {0.0\height}{\footnotesize \faGithub}\ {GitHub
# Profile}}\ \
#     \href
# {mailto:\emaila}{\raisebox
# {0.0\height}{\footnotesize
# \faEnvelope}\ {\emaila}} & \href
# {https: // www.linkedin.com / in / anup66 /}{\raisebox
# {0.0\height}{\footnotesize \faLinkedin}\ {LinkedIn
# Profile}}
# \end
# {tabularx}
# }
#
# %-----------EDUCATION - ----------
# \section
# {\textbf
# {Education}}
# \resumeSubHeadingListStart
# \resumeSubheading
# {Vellore
# Institute
# of
# Technology - AP}{CGPA: 9.31}
# {BTECH
# CSE
# CORE}{2021 - 2025}
# \resumeSubheading
# {BD
# Public
# School}{Percentage: 95}
# {CBSE, BIHAR}
# {2020}
# \resumeSubheading
# {Trident
# Public
# School}{Percentage: 92.8}
# {CBSE, BIHAR}
# {Year}
# \resumeSubHeadingListEnd
# \vspace
# {-5.5
# mm}
# %
#
# %-----------EXPERIENCE - ----------------
# \section
# {\textbf
# {Experience}}
# \resumeSubHeadingListStart
# \resumeSubheading
# {Techolution}
# {Hydrabad}
# {\textbf
# {AI - INTERN(AI
# Hand)}}{september
# 2023 - November
# 2023}
# \vspace
# {-2.0
# mm}
# \resumeItemListStart
# \item
# {
#     Developed
# a
# cutting - edge
# AI
# hand
# model as a
# prominent
# AI
# intern, showcasing
# expertise in computer
# vision and deep
# learning.}
# \item
# {
#     Executed
# robust
# real - time
# object
# detection
# with an impressive accuracy rate of 99.56 %,
# while spearheading the
# segmentation
# module \textbf
# {[Nano – Sam]} to
# enhance
# object
# recognition
# by
# precisely
# outlining and distinguishing
# objects
# from
#
# the
# background.}
# \item
# {
# Applied
# advanced
# algorithms
# to
# calculate
# object
# angles, offering
# valuable
# insights
# for spatial orientation, and engineered a
# dimension - capturing
# feature in the
# AI
# hand.Meticulously
# extracted
# height and width
# information
# for a comprehensive
#     understanding
#     of
#     objects
#     within
#     the
#     environment
#     with the help of Contour in an Image.}
#     \resumeItemListEnd
#
#     \vspace{-3.0mm}
#
#     \resumeSubheading
#     {Shuvidha Foundation}{Remote}
#     {\textbf{ML Intern}}{31 December 2022 - 31 December 2023}
#     \vspace{-2.0mm}
#     \resumeItemListStart
#     \item {Executed a real-time website article summarization model, enabling users to efficiently access relevant content by receiving
# concise
# article
# summaries.}
# \item
# {This
# innovation
# significantly
# streamlined
# the
# reading
# process and saved
# valuable
# time
# for users
#     seeking
#     specific
#     information.}
#     \resumeItemListEnd
#
#     \resumeSubHeadingListEnd
#     \vspace
#     {-8.5
#     mm}
#
#     %-----------PROJECTS - ----------------
#     \section
#     {\textbf
#     {Personal
#     Projects}}
#     \resumeSubHeadingListStart
#
#     \resumeProject
#     {AI
#     Helper
#     Chrome
#     Extension} %Project
#     Name
#     {Developed
#     this as a
#     personal
#     project
#     to
#     enhance
#     the
#     user
#     experience
#     on
#     any
#     websites.} %Project
#     Name, Location
#     Name
#     {june
#     2024} %Event
#     Dates
#
#     \resumeItemListStart
#     \item
#     {Tools \ & technologies
#     used: Python, Flask, llm, google - generativeai
#     library, web
#     scraping.}
#     \item
#     {This
#     extension
#     uses
#     a
#     llm
#     to
#     read
#     a
#     website and answer
#     to
#     any
#     user
#     queries
#     related
#     to
#     that
#     page and help
#     user
#     to
#     interact and help.}
#     \resumeItemListEnd
#     \vspace
#     {-2.0
#     mm}
#     \resumeProject
#     {Adaptive
#     Traffic
#     Forecasting
#     with Self - Learning Model, IBM Hackathon} %Project Name
#     {Worked as python backend and Ai developer.(build the whole ML pipeline)} %Project Name, Location Name
#     {june 2023} %Event Dates
#
#     \resumeItemListStart
#     \item {Tools \ & technologies used: Python, Flask, keras, Tensorflow, TimeseriesGenerator, sklearn, Pandas}
#     \item
#     {Developed
#     a
#     self - trainable
#     deep
#     learning
#     model
#     aimed
#     at
#     predicting
#     congestion
#     times
#     by
#     fetching and processing
#     live
#     traffic
#     data.
# The
# project
# was
# chosen
# to
# adopt
# a
# proactive
# approach in addressing
# traffic
# congestion, considering
# factors
# such as
# different
# times
# of
# the
# day and types
# of
# days.}
# \resumeItemListEnd
# \vspace
# {-2.0
# mm}
#
#
#
#
# \resumeSubHeadingListEnd
# \vspace
# {-5.5
# mm}
#
# %-----------Technical
# skills - ----------------
# \section
# {\textbf
# {Technical
# Skills and Interests}}
# \begin
# {itemize}[leftmargin = 0.1 in, label = {}]
# \small
# {\item
# {
# \textbf
# {Technical
# Skills}{:} \ \
#     \textbf
# {Soft
# Skills}{:} \ \
#     \textbf
# {Field
# of
# Interest}{:} \ \
#     \textbf
# {Hobbies}
# {:} \ \
#     }}
# \end
# {itemize}
# \vspace
# {-16
# pt}
#
# %-----------Positions
# of
# Responsibility - ----------------
# \section
# {\textbf
# {Positions
# of
# Responsibility}}
# \vspace
# {-0.4
# mm}
# \resumeSubHeadingListStart
# \resumePOR
# {Position, } % Position
# {Club or Event} % Club, Event
# {Position
# tenure} %Tenure
# Period
# - work
# description in 1
# line
# \resumePOR
# {Position, } % Position
# {Club or Event} % Club, Event
# {Position
# tenure} %Tenure
# Period
# - work
# description in 1
# line
#
# \resumeSubHeadingListEnd
# \vspace
# {-5
# mm}
#
# %-----------Achievements - ----------------
# \section
# {\textbf
# {Achievements}}
# \vspace
# {-0.4
# mm}
# \resumeSubHeadingListStart
# \resumePOR
# {Achievement} % Award
# {description} % Event
# {Event
# dates} %Event
# Year
#
# \resumePOR
# {Achievement} % Award
# {description} % Event
# {Event
# dates} %Event
# Year
# \resumeSubHeadingListEnd
# \vspace
# {-5
# mm}
#
# %-------------------------------------------
# \end
# {document}
