# Documentation

## Selection Process

### Papers considered that were not chosen

Before deciding on the paper we chose in the end, we considered several other papers from the list on ILIAS, but decided against them for several reasons:

1. Mobile Phones as Pointing Devices (https://www.medien.ifi.lmu.de/permid2005/pdf/RafaelBallagas_Permid2005.pdf): This paper seemed interesting and pretty straightforward from the title, but upon reading it we found out that the technology used was outdated and also thought that the approach was not what we expected from the title and could be improved with a modern smartphone. In particular we thought that the approach with using camera input to find the cursor position was too data-heavy and unreliable (as described with the lacking performance of the sweep gesture in the paper) and an approach that uses the DIPPID sensor data would be more fitting. In the end we decided not to pursue that idea further because we liked the PianoText Paper more.

2. The bubble cursor: enhancing target acquisition by dynamic resizing of the cursor's activation area (https://dl.acm.org/doi/10.1145/1054972.1055012): This paper also seemed interesting, considering we had already talked about how cursor style and positioning can affect the effectiveness of cursor use in the lecture. In the end we decided against it, because we liked PianoText more and another group had already chosen this paper.

### Final Selection

We decided on implementing "PianoText: redesigning the piano keyboard for text entry" (https://dl.acm.org/doi/10.1145/2598510.2598547), which we found in the list of papers on ILIAS. We chose this paper because both of us are hobby musicians and thought that this was an interesting idea to use the piano for keyboard input. We also wanted to test if it can really be a (faster) alternative to a traditional computer keyboard for people already familiar with the piano keyboard and how well someone used to a traditional keyboard but not the one of a piano would perform. Since Samuel is a hobby pianist and Cato has seen a piano many times and understands the basic concept behind it, this seemed like the perfect opportunity.

As for the scope and relevance of the paper, just from reading the paper, it seemed like this was something both related to the last lecture where we talked about keyboards and of a scope that we should be able to implement in two weeks. This was also underlined by the paper already being on the list of papers on ILIAS which we could choose from.

### Implementation

Our first approach was to implement the piano keyboard to text keyboard input exactly as the authors of the papers did it, because they put a lot of thought into an optimal keyboard mapping for piano players who want to type english. As we were both fairly familiar with python, we decided to use python as our programming language. To capture the midi input in python, we decided to use mido, because its documentation suggested that it would work reliably across plattforms.

The implementation of the key to key mapping from the paper was straightforward and we therefore decided to expand beyond the original scope of the paper, which just includes lowercase letters and combinations of keys for common combinations of letters in the english language (like -ing). We considered and tested several ideas:

- Taking into account the amount of force with which a key is pressed -> implement a threshold above which the letter is considered uppercase instead of lowercase
- Add a number block in another octave because the paper only uses 4 1/2 octaves of the 8 available on a standard size piano. This was added to octave 0

However, after implementing the single-key upper-and lowercase mappings, we found out that implementing the combinations of keys was more complicated than expected and required us to implement a lot of edge cases. After that finally worked, we went on to also include numbers.
Additionally we also added some key combinations for exiting the program, space and backspace.
