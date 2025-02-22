##     Assignment 1

##      23k-0072

##      Dania Khan

# Q1

Turing's 1950 paper on "Computing Machinery and Intelligence" proposed the Turing Test as a measure of machine intelligence. While influential, it faces enduring criticisms.  The "Argument from Consciousness" remains potent, as Turing's behavioral focus doesn't address subjective experience.  The "Argument from Informality of Behaviour," though weakened by AI advancements, still poses a challenge due to the complexity of human behavior.  Turing's refutations, like that of the "Mathematical Objection," are not entirely conclusive.

### 1. Which objections still carry some weight?

  The "Argument from Consciousness" (machines may mimic human behavior without genuine understanding) and the "Argument from Informality of Behaviour" (replicating the full spectrum of human action remains a challenge) still hold weight.

### 2. Are his refutations valid?

   Turing's refutations are not always fully convincing. For example, his response to the "Mathematical Objection" (Gödel's theorem) doesn't fully address the difference between computational systems and human thought.

### 3. Since he wrote the paper, can you think of new objections arising from developments?

   Modern concerns include the "Argument from Deception" (AI's potential for manipulation) and the narrow focus of the Turing Test on human-like conversation, potentially overlooking other forms of intelligence.
   
### 4. In the paper, he predicts that by the year 2000, a computer will have a 30% chance of passing a five-minute Turing Test with an unskilled interrogator. Do you think this is reasonable?

Turing's prediction of a 30% chance of passing the test by 2000 was slightly optimistic in its timing. While no definitive "pass" occurred, AI's progress in natural language processing makes his estimation of AI's potential reasonable.


# Q2

### TASK: Playing a decent game of table tennis (ping-pong).

Feasibility: Partially feasible

Challenges: Robots can play basic table tennis, but struggle with real-time reactions, predicting opponent moves, and adjusting strategies during the game.

### TASK: Playing a decent game of bridge at a competitive level.

Feasibility: Feasible 

Challenges:  AI can make strategic decisions, but understanding human psychology and non-verbal communication remain complex.

### TASK: Writing an intentionally funny story.

Feasibility: Currently infeasible

Challenges: AI struggles with humor as it relies on cultural context, wordplay, emotional intelligence

### TASK: Giving competent legal advice in a specialized area of law.

Feasibility: Partially feasible

Challenges:  AI can assist in legal research and document analysis but struggles with contextual understanding needed for complex legal advice.

### TASK:  Discover and prove a new mathematical theorem?

Feasibility:  Partially feasible 

Challenges:  AI can verify and explore patterns in data but often lacks the creativity, intuition.

### TASK:  Perform a surgical operation?

Feasibility: : Partially feasible

Challenges: : Robotic-assisted surgeries exist and enhance precision, but fully autonomous surgeries are still under development due to the need for decision-making and situational awareness

### TASK: Unload any dishwasher in any home?

Feasibility: Currently infeasibl

Challenges: Robots face difficulties with varying home environments, unpredictable object arrangements, and complex manipulation tasks, making this task hard to automate.

### TASK: Construct a building?

Feasibility:  Partially feasible

Challenges:   AI supports tasks like 3D printing and site surveying, but fully autonomous construction is not achievable due to the need for dynamic problem-solving, coordination, and adaptability on construction sites.

# Q3

## Agent Description:

An RTS game agent controls units to defeat the enemy, issuing move, attack, and gather commands. It receives sensory input about friendly/enemy unit positions, resources, and game time, making real-time decisions.

## Environment Characterization:

The RTS environment is mostly accessible (fog of war), mostly deterministic (predictable outcomes with slight randomness), episodic (distinct games), dynamic (enemy actions change the world), and continuous (actions happen in real-time).

## Best Agent Architecture:

A hybrid agent is ideal. A reactive component handles fast, low-level unit control (dodging, targeting). A deliberative component makes high-level strategic decisions (attack plans, defense). A learning component improves performance over time (strategy refinement). This combines quick reactions with strategic depth in a dynamic, partially observable, real-time game.

# Q4
 1. An agent that senses only partial information about the state cannot be perfectly rational.
    
    FALSE. An agent can still be perfectly rational given the information it perceives.Rationality depends on maximizing expected performance based on the percept history, even if the information is partial

    
 2. There exist task environments in which no pure reflex agent can behave rationally.
 
    TRUE. Pure reflex agents act solely based on the current percept, without considering       history.In environments where decisions depend on past events (like a maze where you        must remember visited paths), reflex agents fail to act rationally without memory.


 3. There exists a task environment in which every agent is rational.

    
    FALSE. In most environments, agents can have varying levels of rationality depending on their design and decision-making processes
  
 
 4. The input to an agent program is the same as the input to the agent function.

    FALSE. The agent function maps percept histories to actions, while the agent program processes percepts and contains the logic for deciding actions.
 
 5. Every agent function is implementable by some program/machine combination.

    FALSE. Some agent functions require infinite computation or memory, making them impossible to implement in practice.
 
 6. Suppose an agent selects its action uniformly at random from the set of possible actions. There exists a deterministic task environment in which this agent is rational.

    TRUE. In a game like rock-paper-scissors, choosing actions randomly can be rational since it prevents opponents from predicting the agent’s moves. T
 
 
 7. It is possible for a given agent to be perfectly rational in two distinct task environments.

    TRUE. An agent can be rational in different environments if its actions maximize expected performance in both. 



# Q5

![Screenshot 2025-02-22 191612](https://github.com/user-attachments/assets/ec7e100f-022e-4047-8667-d90ade30f3d3)

# COMPARISONS

![Screenshot 2025-02-22 192000](https://github.com/user-attachments/assets/3349c836-0fb7-4b2b-8408-ac728ceffc9c)









