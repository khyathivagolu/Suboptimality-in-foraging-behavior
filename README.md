### Exploring the dysregulations in foraging behavior caused due to stress, anxiety and depression <br /> SURGE, IIT Kanpur

#### Mentor: Prof. Arjun Ramakrishnan <br /> Co-Mentor: Peeusa Mitra

#### Introduction: 
The main aim of this project is to understand the correlation between foraging behavior and mental health conditions, namely stress, anxiety disorder, and depression, by designing a naturalistic foraging task and testing it on participants with self-reported stress and anxiety levels. 

A patch foraging task models foraging behavior in humans through deciding whether to forage in a particular patch or to move to another patch in hopes of a greater reward i.e., by making a tradeoff between exploitation and exploration. The foraging patterns of the participants are studied by making comparative analyses of the choices made by the participants and the optimal strategy, as suggested by algorithms such as the marginal value theorem (MVT) and the temporal difference (TD) learning algorithm. 

Continuous unmanageable stress can manifest behavioral changes like anxiety and depression, which interfere with the process of decision making in general. Foraging, a  neuroethological paradigm used to analyze decision making, would also be affected in these cases, leading to suboptimal behavior. This change in behavior must be understood and analyzed carefully as it would be helpful in determining biomarkers for these mental health conditions. 

#### Hypothesis: 
We hypothesize that anxiety and depression result in suboptimal decision making, which surfaces as leaving the patch early or over-exploiting in the patch foraging game. The suboptimality would be different in participants with different mental health conditions. In general, over-exploration and over-exploitation occur in highly anxious conditions.  

#### Method: 
The project consists of two steps:
1. Conducting a survey using self-assessment questionnaires to assess stress, anxiety, and depression levels in individual participants. 
For this, we will be using the STAI, the GAD-7, and the PHQ-9 questionnaires for the assessment of different mental conditions, namely stress, anxiety, and depression, respectively. 
Additionally, we will include questions regarding COVID related stress in the questionnaire. People who have undergone COVID related complicacies, either directly or indirectly, are likely to suffer from different mental conditions post COVID. We would be analyzing these aspects through the questionnaire to understand how it is linked to their foraging behavior.
The participants would then be asked to participate in the foraging game. Participants with negligible stress, anxiety, and depression levels would be our healthy controls and during the analysis, their results would be compared against the participants who reported high levels of the following conditions. 

2. Designing a naturalistic foraging task and testing the participants.
The idea for designing the foraging task is to build a virtual patch foraging game where the participants would be asked to maximize their reward by foraging in a time-bound setting. We would build this game on PsychoPy. Overstaying at the same patch during foraging would result in getting a lesser reward each time as the reward from the patch gets exhausted. Similarly, while moving to a new patch very often i.e., over-exploration leads to greater travel costs resulting in lesser time to forage and hence, lesser reward. There will be no reward in between patches, i.e., while traveling. The decision to forage at the same patch or move to a new one must be optimized in order to maximize the reward.

#### Survey
The survey consists of a self-assessment questionnaire designed from the various standard questionnaires. The sections were the following:
Section 1: General information
Section 2: PHQ-9
Section 3: GAD-7
Section 4: STAI Part 1
Section 5: STAI Part 2
Section 6: COVID related questions

#### Analysis: 
1. Calculation of optimal leaving time from a patch using Marginal Value Theorem
2. T-test for average leaving times for all the participants in the rich and poor environments

#### Expected result:
The participants would show suboptimal foraging behavior in highly stressed conditions. They would either leave the patch early or overexploit, resulting in lesser rewards than expected. 
Overexploitation can be associated with trait anxiety, while early leaving of the patch could be associated with state anxiety. Participants making more exploratory decisions can be associated with depressed individuals as they tend to be more risk-seeking.

#### Future work:
Further, we plan on working on the following aspects to complete the study:
1. Analyze the survey responses to assess stress levels in the individuals
2. Analyze the game data further using Reinforcement learning techniques such as Q-learning and TD-learning
3. Rectify the errors in the game design in order to design a fully functional game 
4. Couple the final game with EEG and pupillometry for future research

