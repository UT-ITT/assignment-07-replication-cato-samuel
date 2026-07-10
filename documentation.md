# Documentation

## Selection Process
### Papers considered that were not chosen
Before deciding on the paper we chose in the end, we considered several other papers from the list on ILIAS, but decided against them for several reasons:

1. Mobile Phones as Pointing Devices (https://www.medien.ifi.lmu.de/permid2005/pdf/RafaelBallagas_Permid2005.pdf): This paper seemed interesting and pretty straightforward from the title, but upon reading it we found out that the technology used was outdated and also thought that the approach could be improved with a modern smartphone. In particular we thought that the approach with using camera input to find the cursor position was too data-heavy and unreliable (as described with the lacking performance of the sweep gesture in the paper) and an approach that uses the DIPPID sensor data would be more fitting. In the end we decided not to pursue that idea further, because we liked the PianoText Paper more.


### Final Selection
In the end we decided on implementing "PianoText: redesigning the piano keyboard for text entry" (https://dl.acm.org/doi/10.1145/2598510.2598547), which we found in the list of papers on ILIAS. We chose this paper because both of us are hobby musicians with access to an electric piano and thought that this was an interesting idea to use the piano for keyboard input. We also wanted to test if it can really be a (faster) alternative to a traditional computer keyboard for people already familiar with the piano keyboard and how well someone used to a traditional keyboard but not the one of a piano would perform. Since Samuel is a hobby pianist and Cato has seen a piano many times and understands the basic concept behind it, this seemed like the perfect opportunity.

As for the scope and relevance of the paper: from reading the paper it seemed like this was something both related to the last lecture where we talked about keyboards and of a scope that we should be able to implement in two weeks. This was also underlined by the paper already being on the list of papers on ILIAS which we could choose from.

## Implementation
Our first approach was to implement the piano keyboard to text keyboard input exactly as the authors of the papers did it. As we were both fairly familiar with python, we decided to use python as our programming language. To capture the midi input in python, we decided to use mido, because its documentation suggested that it would work reliably across plattforms.

The implementation of the basic mapping from the paper was implemented quickly and we therefore decided to expand beyond the original scope of the paper, which just includes lowercase letters on single keys and try different mappings. We considered and tested several ideas:

- Taking into account the amount of force with which a key is pressed -> implement a threshold above which the letter is considered uppercase instead of lowercase
- Taking advantage of the fact that we cannot just play single keys, but chords on the piano