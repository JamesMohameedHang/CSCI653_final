# Topological Insulator
Topological Insulators are a remarkable class of quantum material that bahave as **insulators in their inside** while **conducting in their outside**. In this way, we could greatly reduce the dissipation in current transportation. So far, physicists have proposed numerous physical and mathematical models in simulating the topological insulator.

# Next-Nearest-Neighbor Spin Chain
Among the physical models, Next-Nearest Neighbor Spin Chain is one of the most popular ones. The major reason is that 
1. It supports relatively rich quantum phases
2. It possesses robust surface state(the conducting surface), 
3. It could serve as paradigm of wide range of materials

# Model and Hamiltonian
For a spin chain, we'd use Spin operators for our study. The Hamiltonian is<br> 

<img width="240" alt="image" src="images/Hamiltonian.png"><br>

The schematic represents its interactions is

# Method
In this project, I'll be most interested in the Entanglement Entropy of the ground state. By probing the Entanglement Entropy, I'd like to construct a phase diagram of the model, and obtain an understanding of the property of each phase.
## Entanglement Entropy
I bet you guys have heard of Entanglement in Quantum Mechanis. There's a popular story of "spooky action at a distance": having two gloves - you send one to North Pole without looking, and when your friend at South Pole opens theirs and finds a left-handed glove, yours instantly becomes right-handed. This story demonstrates two particles, after interacting, even though being separated, would still affect each other

In modern physics, we have an important variable, called Entanglement Entropy, that could be used to describe how two parts of a system Entangles. This variable is super important since it carries out the property of the whole system and could be served to distinguish two different topological phases.

# Algorithm: Density Matrix Renormalization Group(DMRG)
Density Matrix Renormalization Group is a powerful algorithm in studying a relatively large system. In modern physics, we are sometimes interested a system with large amount of particles(like 50-100 or so), which is impossible to calculate even for a computer

However, through certain mathematical renormalization strategy, DMRG allows us to reduce the solution space we need to calculate, and calculate our most interested state(usually ground state) efficiently and precisely

### It's like a brilliant editor for a quantum story, cutting out the fluff and keeping only the essential plot. ###


